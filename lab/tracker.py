"""CLI: python -m lab.tracker {bootstrap|settle|snapshot|report|run}"""
import json, sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

from . import MODEL_VERSION, NON_NBA, espn, injury, ratings, rawstore, report, store

ROOT = Path(__file__).resolve().parent.parent
HISTORY = ROOT / "data" / "history.csv"
ET = ZoneInfo("America/New_York")


def now_utc():
    return datetime.now(timezone.utc)


def parse_ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00")).astimezone(timezone.utc)


def day_et(ts):
    return parse_ts(ts).astimezone(ET).strftime("%Y-%m-%d")


def _store_minutes(con, event_id, day, rows):
    con.executemany("INSERT OR IGNORE INTO minutes VALUES (?,?,?,?,?,?)",
                    [(event_id, pid, team, day, mins, pm) for pid, team, mins, pm in rows])


def bootstrap(con, n=400):
    """Siembra minutos por jugador con los ultimos n partidos del historial."""
    h = pd.read_csv(HISTORY).tail(n)
    todo = [(str(r.event_id), str(r.day_et)[:10]) for r in h.itertuples()]
    with ThreadPoolExecutor(8) as ex:
        res = list(ex.map(lambda t: espn.boxscore_minutes(t[0]), todo))
    for (eid, day), rows in zip(todo, res):
        _store_minutes(con, eid, day, rows)
    con.commit()
    print(f"bootstrap: {len(todo)} partidos, {con.execute('SELECT COUNT(*) FROM minutes').fetchone()[0]} filas de minutos")


def settle(con, days_back=4):
    """Guarda resultados, minutos y lineas de cierre de partidos terminados."""
    today = now_utc().astimezone(ET).date()
    n_res = n_close = 0
    for d in range(days_back + 1):
        day = (today - timedelta(days=d)).strftime("%Y%m%d")
        for g in espn.scoreboard(day):
            if g["home"] in NON_NBA or g["away"] in NON_NBA or g["season_type"] not in (2, 3):
                continue
            eid, dte = g["event_id"], day_et(g["ts"])
            if g["completed"]:
                if not con.execute("SELECT 1 FROM results WHERE event_id=?", (eid,)).fetchone():
                    con.execute("INSERT OR IGNORE INTO results VALUES (?,?,?,?,?,?,?,?)",
                                (eid, g["ts"], dte, ratings.season_of(dte), g["home"], g["away"],
                                 g["home_score"], g["away_score"]))
                    _store_minutes(con, eid, dte, espn.boxscore_minutes(eid))
                    n_res += 1
                snap = con.execute("SELECT provider_id FROM snapshots WHERE event_id=? ORDER BY (label='D') DESC LIMIT 1",
                                   (eid,)).fetchone()
                if snap and not con.execute("SELECT 1 FROM closes WHERE event_id=?", (eid,)).fetchone():
                    o = espn.odds(eid, "close", prefer_provider=snap["provider_id"])
                    if o:
                        con.execute("INSERT OR IGNORE INTO closes VALUES (?,?,?,?,?,?)",
                                    (eid, o["provider_id"], o["line"], o["home_px"], o["away_px"],
                                     now_utc().isoformat()))
                        n_close += 1
    con.commit()
    print(f"settle: {n_res} resultados nuevos, {n_close} cierres nuevos")


def label_for(tte_h):
    """E = exploratoria (~24h). D = unica ventana confirmatoria (1-2h antes del tip).
    DX = respaldo (30-60 min antes) solo si D fallo; se guarda pero NO entra al veredicto."""
    if 20 <= tte_h <= 26:
        return "E"
    if 1.0 <= tte_h <= 2.0:
        return "D"
    if 0.5 <= tte_h < 1.0:
        return "DX"
    return None


PATH_HOURS = 28          # se registra la trayectoria de la linea desde 28 h antes del tip hasta el tip


def log_injury_changes(con, inj, t0):
    """Registro append-only de CAMBIOS de estado de lesiones observados (con la hora en que se vieron).
    Si la API devolvio una lista vacia (fallo), no se registra nada para no inventar 'remociones'."""
    if not inj:
        return 0
    last = {}
    for r in con.execute("SELECT team, player_id, name, status FROM injury_log WHERE id IN "
                         "(SELECT MAX(id) FROM injury_log GROUP BY player_id)"):
        last[r["player_id"]] = (r["team"], r["name"], r["status"])
    cur = {pid: (team, name, status) for team, pid, name, status in inj}
    n = 0
    for pid, (team, name, status) in cur.items():
        if last.get(pid, (None, None, None))[2] != status:
            con.execute("INSERT INTO injury_log(taken_at,team,player_id,name,status) VALUES (?,?,?,?,?)",
                        (t0.isoformat(), team, pid, name, status)); n += 1
    for pid, (team, name, status) in last.items():
        if pid not in cur and status != "REMOVED":
            con.execute("INSERT INTO injury_log(taken_at,team,player_id,name,status) VALUES (?,?,?,?,?)",
                        (t0.isoformat(), team, pid, name, "REMOVED")); n += 1
    return n


def snapshot(con):
    """Registra prediccion + linea actual para partidos en la ventana E (24h), D (1-2h) o DX (respaldo).
    Archiva la respuesta cruda de ESPN (hash en la fila) y registra cada intento en capture_log."""
    R = ratings.build(HISTORY, con)
    mins = injury.avg_minutes(con)
    inj_payload = espn.injuries_payload()
    inj = espn.injuries(inj_payload)
    t0, n_new = now_utc(), 0
    log_injury_changes(con, inj, t0)
    stamp = t0.strftime("%Y%m%dT%H%M")
    inj_sha = None
    for off in (0, 1, 2):
        day = (t0.astimezone(ET).date() + timedelta(days=off)).strftime("%Y%m%d")
        for g in espn.scoreboard(day):
            if g["completed"] or g["season_type"] not in (2, 3):
                continue
            if g["home"] in NON_NBA or g["away"] in NON_NBA:
                continue
            con.execute("INSERT OR IGNORE INTO games_seen VALUES (?,?,?,?,?)",
                        (g["event_id"], g["ts"], g["home"], g["away"], t0.isoformat()))
            tte = (parse_ts(g["ts"]) - t0).total_seconds() / 3600
            lab = label_for(tte)
            need = bool(lab) and not con.execute("SELECT 1 FROM snapshots WHERE event_id=? AND label=?",
                                                 (g["event_id"], lab)).fetchone()
            if need and lab == "DX" and con.execute("SELECT 1 FROM snapshots WHERE event_id=? AND label='D'",
                                                    (g["event_id"],)).fetchone():
                need = False
            in_path = 0 < tte <= PATH_HOURS
            if not need and not in_path:
                continue
            payload = espn.odds_payload(g["event_id"])
            o = espn.parse_odds(payload, "current")
            if o and in_path:
                con.execute("INSERT INTO line_path(event_id,taken_at,tte_hours,provider_id,line,home_px,away_px,total)"
                            " VALUES (?,?,?,?,?,?,?,?)", (g["event_id"], t0.isoformat(), tte, o["provider_id"],
                                                          o["line"], o["home_px"], o["away_px"], o["total"]))
            if not need:
                continue
            if not o:
                con.execute("INSERT INTO capture_log(event_id,label,attempted_at,tte_hours,status) "
                            "VALUES (?,?,?,?,?)", (g["event_id"], lab, t0.isoformat(), tte, "no_odds"))
                continue
            raw_sha = rawstore.save(f"{g['event_id']}_{lab}_odds", payload)
            if inj_sha is None:
                inj_sha = rawstore.save(f"inj_{stamp}", inj_payload)
            pa = R.predict(g["home"], g["away"])
            adj, detail = injury.adjustment(g["home"], g["away"], inj, mins)
            cur = con.execute(
                "INSERT OR IGNORE INTO snapshots(event_id,label,taken_at,tip_ts,home,away,provider_id,line,"
                "home_px,away_px,open_line,total,pred_a,pred_b,inj_adj,model_version,injuries_json,"
                "raw_sha256,inj_sha256) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (g["event_id"], lab, t0.isoformat(), g["ts"], g["home"], g["away"], o["provider_id"],
                 o["line"], o["home_px"], o["away_px"], o["open_line"], o["total"], pa, pa + adj,
                 adj, MODEL_VERSION, detail, raw_sha, inj_sha))
            con.execute("INSERT INTO capture_log(event_id,label,attempted_at,tte_hours,status) "
                        "VALUES (?,?,?,?,?)", (g["event_id"], lab, t0.isoformat(), tte, "ok"))
            n_new += cur.rowcount
            print(f"  [{lab}] {g['away']}@{g['home']} linea={o['line']:+.1f} A={pa:+.1f} B={pa+adj:+.1f}")
    con.commit()
    print(f"snapshot: {n_new} nuevos")


def write_report(con):
    txt = report.render(con)
    (ROOT / "REPORT.md").write_text(txt, encoding="utf-8")
    print(txt)


def main(argv):
    cmd = argv[1] if len(argv) > 1 else "run"
    con = store.connect()
    if cmd == "bootstrap":
        bootstrap(con)
    elif cmd == "settle":
        settle(con)
    elif cmd == "snapshot":
        snapshot(con)
    elif cmd == "report":
        write_report(con)
    elif cmd == "run":
        if not con.execute("SELECT 1 FROM minutes LIMIT 1").fetchone():
            bootstrap(con)
        settle(con)
        snapshot(con)
        write_report(con)
    else:
        print(__doc__)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
