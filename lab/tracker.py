"""CLI: python -m lab.tracker {bootstrap|settle|snapshot|report|run}"""
import json, sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

from . import MODEL_VERSION, NON_NBA, espn, injury, ratings, report, store

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
                    con.execute("INSERT INTO results VALUES (?,?,?,?,?,?,?,?)",
                                (eid, g["ts"], dte, ratings.season_of(dte), g["home"], g["away"],
                                 g["home_score"], g["away_score"]))
                    _store_minutes(con, eid, dte, espn.boxscore_minutes(eid))
                    n_res += 1
                snap = con.execute("SELECT provider_id FROM snapshots WHERE event_id=? LIMIT 1",
                                   (eid,)).fetchone()
                if snap and not con.execute("SELECT 1 FROM closes WHERE event_id=?", (eid,)).fetchone():
                    o = espn.odds(eid, "close", prefer_provider=snap["provider_id"])
                    if o:
                        con.execute("INSERT INTO closes VALUES (?,?,?,?,?,?)",
                                    (eid, o["provider_id"], o["line"], o["home_px"], o["away_px"],
                                     now_utc().isoformat()))
                        n_close += 1
    con.commit()
    print(f"settle: {n_res} resultados nuevos, {n_close} cierres nuevos")


def label_for(tte_h):
    if 20 <= tte_h <= 26:
        return "E"
    if 0.75 <= tte_h <= 3:
        return "D"
    return None


def snapshot(con):
    """Registra prediccion + linea actual para partidos en la ventana E (24h) o D (decision)."""
    R = ratings.build(HISTORY, con)
    mins = injury.avg_minutes(con)
    inj = espn.injuries()
    t0, n_new = now_utc(), 0
    for off in (0, 1, 2):
        day = (t0.astimezone(ET).date() + timedelta(days=off)).strftime("%Y%m%d")
        for g in espn.scoreboard(day):
            if g["completed"] or g["season_type"] not in (2, 3):
                continue
            if g["home"] in NON_NBA or g["away"] in NON_NBA:
                continue
            tte = (parse_ts(g["ts"]) - t0).total_seconds() / 3600
            lab = label_for(tte)
            if not lab or con.execute("SELECT 1 FROM snapshots WHERE event_id=? AND label=?",
                                      (g["event_id"], lab)).fetchone():
                continue
            o = espn.odds(g["event_id"], "current")
            if not o:
                continue
            pa = R.predict(g["home"], g["away"])
            adj, detail = injury.adjustment(g["home"], g["away"], inj, mins)
            con.execute(
                "INSERT INTO snapshots(event_id,label,taken_at,tip_ts,home,away,provider_id,line,"
                "home_px,away_px,open_line,total,pred_a,pred_b,inj_adj,model_version,injuries_json)"
                " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (g["event_id"], lab, t0.isoformat(), g["ts"], g["home"], g["away"], o["provider_id"],
                 o["line"], o["home_px"], o["away_px"], o["open_line"], o["total"], pa, pa + adj,
                 adj, MODEL_VERSION, detail))
            n_new += 1
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
