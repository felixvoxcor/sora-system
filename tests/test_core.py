import json, sqlite3
from pathlib import Path
import numpy as np
import pytest
from lab import espn, injury, ratings, rawstore, report, store
from lab.tracker import label_for

FX = Path(__file__).parent / "fixtures"


@pytest.fixture
def con(tmp_path):
    return store.connect(tmp_path / "t.db")


def test_parse_odds_final_close():
    o = espn.parse_odds(json.load(open(FX / "odds_final.json")), "close")
    assert o["line"] == -5.5 and o["open_line"] == -6.5      # NY (visitante) favorito por 5.5
    assert o["provider_id"] == "58"


def test_parse_odds_pre_current_home_favorite():
    o = espn.parse_odds(json.load(open(FX / "odds_pre.json")), "current")
    assert o["line"] == 1.5 and o["open_line"] == 2.5          # DET -1.5 local => margen esperado +1.5
    assert espn.parse_odds(json.load(open(FX / "odds_pre.json")), "close") is None


def test_ratings_no_lookahead():
    R = ratings.Ratings()
    p_before = R.predict("A", "B")
    R.update(2025, "A", "B", 30)
    assert p_before == R.hca                                   # la prediccion previa no cambia
    assert R.predict("A", "B") > p_before                      # y el update si sube a A


def test_ratings_carry_between_seasons():
    R = ratings.Ratings()
    for _ in range(50):
        R.update(2024, "A", "B", 20)
    before = R.r["A"]
    R.update(2025, "C", "D", 0)
    assert abs(R.r["A"] - before * R.carry) < 1e-9


def test_non_nba_teams_ignored():
    R = ratings.Ratings()
    R.update(2025, "CAN", "KEN", 40)
    assert R.r == {}


def test_snapshots_append_only(con):
    con.execute("INSERT INTO snapshots(event_id,label) VALUES ('1','D')")
    with pytest.raises(sqlite3.DatabaseError):
        con.execute("UPDATE snapshots SET label='E'")
    with pytest.raises(sqlite3.DatabaseError):
        con.execute("DELETE FROM snapshots")


def test_unique_snapshot_per_label(con):
    con.execute("INSERT INTO snapshots(event_id,label) VALUES ('1','D')")
    with pytest.raises(sqlite3.IntegrityError):
        con.execute("INSERT INTO snapshots(event_id,label) VALUES ('1','D')")


def test_label_windows():
    assert label_for(24) == "E" and label_for(1.5) == "D" and label_for(1.0) == "D" and label_for(2.0) == "D"
    assert label_for(0.75) == "DX" and label_for(0.5) == "DX"          # respaldo, fuera del veredicto
    assert label_for(0.4) is None and label_for(2.5) is None and label_for(3.0) is None
    assert label_for(10) is None and label_for(30) is None


def test_injury_adjustment_sign_and_scale():
    mins = {"p1": 36.0, "p2": 12.0}
    inj = [("BOS", "p1", "Star", "Out"), ("NY", "p2", "Role", "Out"), ("NY", "p1", "X", "Day-To-Day")]
    adj, _ = injury.adjustment("BOS", "NY", inj, mins)
    # BOS pierde 3.0; NY pierde 3*(12/36)^2 + 3*0.25*1 = 0.333+0.75 => local se perjudica menos
    assert adj == pytest.approx((3 * (1 / 3) ** 2 + 0.75) - 3.0)
    assert injury.adjustment("BOS", "NY", [], mins)[0] == 0.0


def _seed(con, line, close, margin, pa, pb, i):
    eid = str(i)
    con.execute("INSERT INTO snapshots(event_id,label,line,home_px,away_px,pred_a,pred_b,inj_adj) "
                "VALUES (?,?,?,?,?,?,?,?)", (eid, "D", line, -110, -110, pa, pb, pb - pa))
    con.execute("INSERT INTO closes VALUES (?,?,?,?,?,?)", (eid, "58", close, -110, -110, ""))
    con.execute("INSERT INTO results VALUES (?,?,?,?,?,?,?,?)", (eid, "", "", 2026, "H", "A", 100 + margin, 100))


def test_clv_sign_convention(con):
    # modelo ve +4 vs linea +1 => apuesta local; la linea sube a +3 => CLV +2
    _seed(con, 1.0, 3.0, 5, 4.0, 4.0, 1)
    # modelo ve -2 vs linea +1 => apuesta visitante; la linea baja a 0 => CLV +1
    _seed(con, 1.0, 0.0, -5, -2.0, -2.0, 2)
    s = report.arm_stats(report.load(con), "A", 2.0)
    assert s["n"] == 2 and s["clv"] == pytest.approx(1.5)
    assert s["win"] == 1.0 and s["roi"] == pytest.approx(100 / 110)


def test_verdicts():
    ok = dict(n=500, clv=0.2, p=0.01, ub=0.4)
    assert report.verdict(ok) == "PASA"
    assert report.verdict(dict(ok, p=0.20)).startswith("ARCHIVAR")
    assert report.verdict(dict(ok, clv=-0.1, p=0.9)).startswith("ARCHIVAR")
    assert report.verdict(ok, coverage_ok=False).startswith("INVALIDO")
    # futilidad solo en el interim y por limite superior del IC
    assert report.verdict(dict(n=250, clv=-0.3, p=0.99, ub=0.0)) == "ARCHIVAR (futilidad)"
    assert report.verdict(dict(n=250, clv=-0.1, p=0.9, ub=0.2)).startswith("EN CURSO")
    # nunca se declara exito antes de N_DECIDE
    assert report.verdict(dict(n=499, clv=1.0, p=0.0001, ub=2.0)).startswith("EN CURSO")


def test_ci_and_mde():
    rows = []
    for i in range(40):
        rows.append(dict(event_id=str(i), line=0.0, home_px=-110, away_px=-110, pred_a=3.0, pred_b=3.0,
                         inj_adj=0.0, close_line=1.0 if i % 2 else 0.0, margin=5))
    s = report.arm_stats(rows, "A", 2.0)
    assert s["n"] == 40 and s["lo"] < s["clv"] < s["hi"] and s["ub"] > s["clv"]
    assert report.mde(2.0) == pytest.approx(2.9696 * 2.0 / np.sqrt(500), rel=1e-3)


def test_snapshot_insert_or_ignore_is_safe(con):
    con.execute("INSERT OR IGNORE INTO snapshots(event_id,label) VALUES ('1','D')")
    cur = con.execute("INSERT OR IGNORE INTO snapshots(event_id,label) VALUES ('1','D')")
    assert cur.rowcount == 0 and con.execute("SELECT COUNT(*) FROM snapshots").fetchone()[0] == 1


def test_schema_migration_adds_hash_columns(tmp_path):
    import sqlite3 as sq
    p = tmp_path / "old.db"
    old = sq.connect(p)
    old.executescript("CREATE TABLE snapshots(id INTEGER PRIMARY KEY AUTOINCREMENT, event_id TEXT, label TEXT,"
                      " UNIQUE(event_id,label));")
    old.commit(); old.close()
    con = store.connect(p)
    cols = {r["name"] for r in con.execute("PRAGMA table_info(snapshots)")}
    assert {"raw_sha256", "inj_sha256"} <= cols


def test_rawstore_deterministic_and_append_only(tmp_path):
    a = {"b": 1, "a": [1, 2]}
    h1 = rawstore.save("x", a, root=tmp_path)
    b1 = (tmp_path / "x.json.gz").read_bytes()
    h2 = rawstore.save("x", {"a": [1, 2], "b": 1}, root=tmp_path)       # mismo contenido, otro orden de claves
    assert h1 == h2 == rawstore.sha256(a) and (tmp_path / "x.json.gz").read_bytes() == b1
    rawstore.save("x", {"cambiado": True}, root=tmp_path)               # no sobreescribe
    assert (tmp_path / "x.json.gz").read_bytes() == b1
    assert rawstore.save("y", None, root=tmp_path) is None


def test_coverage_counts(con):
    for i, (d, dx, noodds) in enumerate([(1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 0, 0)]):
        eid = str(i)
        con.execute("INSERT INTO games_seen VALUES (?,?,?,?,?)", (eid, "", "H", "A", ""))
        con.execute("INSERT INTO results VALUES (?,?,?,?,?,?,?,?)", (eid, "", "", 2026, "H", "A", 100, 90))
        if d:
            con.execute("INSERT INTO snapshots(event_id,label) VALUES (?,?)", (eid, "D"))
        if dx:
            con.execute("INSERT INTO snapshots(event_id,label) VALUES (?,?)", (eid, "DX"))
        if noodds:
            con.execute("INSERT INTO capture_log(event_id,label,attempted_at,tte_hours,status) "
                        "VALUES (?,?,?,?,?)", (eid, "D", "", 1.5, "no_odds"))
    c = report.coverage(con)
    assert (c["n"], c["d"], c["dx"], c["no_odds"], c["missed"]) == (4, 1, 1, 1, 1)
    assert c["frac"] == 0.25


def test_dx_never_enters_verdict(con):
    con.execute("INSERT INTO snapshots(event_id,label,line,home_px,away_px,pred_a,pred_b,inj_adj) "
                "VALUES ('1','DX',1,-110,-110,5,5,0)")
    con.execute("INSERT INTO closes VALUES ('1','58',3.0,-110,-110,'')")
    con.execute("INSERT INTO results VALUES ('1','','',2026,'H','A',110,100)")
    assert report.load(con) == []


def test_empty_report(con):
    assert "Aun no hay partidos" in report.render(con)


def test_snapshot_end_to_end_offline(con, tmp_path, monkeypatch):
    """Simula un partido a 1.5 h del tip: debe crear snapshot D, archivar el crudo con hash y registrar el intento."""
    from datetime import datetime, timedelta, timezone
    from lab import tracker
    now = datetime(2026, 10, 21, 22, 0, tzinfo=timezone.utc)
    tip = now + timedelta(hours=1.5)
    payload = json.load(open(FX / "odds_pre.json"))
    game = dict(event_id="999", ts=tip.isoformat().replace("+00:00", "Z"), season_type=2, home="DET",
                away="NY", completed=False, home_score=0, away_score=0)
    monkeypatch.setattr(tracker, "now_utc", lambda: now)
    monkeypatch.setattr(tracker.espn, "scoreboard", lambda d: [game] if d == "20261021" else [])
    monkeypatch.setattr(tracker.espn, "odds_payload", lambda e: payload)
    monkeypatch.setattr(tracker.espn, "injuries_payload", lambda: {"injuries": []})
    monkeypatch.setattr(rawstore, "RAW_DIR", tmp_path / "raw")
    tracker.snapshot(con)
    tracker.snapshot(con)                                   # segunda corrida: no duplica
    rows = con.execute("SELECT label, raw_sha256, inj_sha256, model_version FROM snapshots").fetchall()
    assert len(rows) == 1 and rows[0]["label"] == "D" and rows[0]["model_version"] == "v1.2"
    assert rows[0]["raw_sha256"] == rawstore.sha256(payload)
    assert (tmp_path / "raw" / "999_D_odds.json.gz").exists()
    assert con.execute("SELECT status FROM capture_log").fetchone()[0] == "ok"
    assert con.execute("SELECT COUNT(*) FROM games_seen").fetchone()[0] == 1


def test_snapshot_logs_missing_odds(con, tmp_path, monkeypatch):
    from datetime import datetime, timedelta, timezone
    from lab import tracker
    now = datetime(2026, 10, 21, 22, 0, tzinfo=timezone.utc)
    game = dict(event_id="998", ts=(now + timedelta(hours=1.5)).isoformat().replace("+00:00", "Z"),
                season_type=2, home="DET", away="NY", completed=False, home_score=0, away_score=0)
    monkeypatch.setattr(tracker, "now_utc", lambda: now)
    monkeypatch.setattr(tracker.espn, "scoreboard", lambda d: [game] if d == "20261021" else [])
    monkeypatch.setattr(tracker.espn, "odds_payload", lambda e: {"items": []})
    monkeypatch.setattr(tracker.espn, "injuries_payload", lambda: {"injuries": []})
    monkeypatch.setattr(rawstore, "RAW_DIR", tmp_path / "raw")
    tracker.snapshot(con)
    assert con.execute("SELECT COUNT(*) FROM snapshots").fetchone()[0] == 0
    assert con.execute("SELECT status FROM capture_log").fetchone()[0] == "no_odds"


def test_alpha_is_bonferroni_over_three_arms():
    assert report.ALPHA == pytest.approx(0.05 / 3)
    assert [a[0] for a in report.ARMS] == ["A", "B", "C"] and report.ARMS[2][1:] == ("A", "E")


def _seed_label(con, label, i, line, close, margin, pa):
    eid = str(i)
    con.execute("INSERT INTO snapshots(event_id,label,line,home_px,away_px,pred_a,pred_b,inj_adj) "
                "VALUES (?,?,?,?,?,?,?,?)", (eid, label, line, -110, -110, pa, pa, 0.0))
    con.execute("INSERT OR IGNORE INTO closes VALUES (?,?,?,?,?,?)", (eid, "58", close, -110, -110, ""))
    con.execute("INSERT OR IGNORE INTO results VALUES (?,?,?,?,?,?,?,?)", (eid, "", "", 2026, "H", "A", 100 + margin, 100))


def test_arm_c_reads_only_label_e(con):
    _seed_label(con, "E", 1, 1.0, 3.0, 5, 4.0)          # E: CLV +2
    _seed_label(con, "E", 3, 1.0, 3.5, 5, 4.0)          # E: CLV +2.5
    _seed_label(con, "D", 2, 1.0, 1.0, 5, 4.0)          # D: CLV 0 (no debe entrar al brazo C)
    _seed_label(con, "D", 4, 1.0, 0.0, 5, 4.0)          # CLV -1
    e, d = report.load(con, "E"), report.load(con, "D")
    assert len(e) == 2 and len(d) == 2
    assert report.arm_stats(e, "A", 2.0)["clv"] == pytest.approx(2.25)
    assert report.arm_stats(d, "A", 2.0)["clv"] == pytest.approx(-0.5)


def test_render_has_three_arms(con):
    _seed_label(con, "E", 1, 1.0, 3.0, 5, 4.0)
    txt = report.render(con)
    assert "Brazo C (A@E)" in txt and "Brazo A (A@D)" in txt and "Brazo B (B@D)" in txt


def test_line_path_and_injury_log_end_to_end(con, tmp_path, monkeypatch):
    from datetime import datetime, timedelta, timezone
    from lab import tracker
    now = datetime(2026, 10, 21, 18, 0, tzinfo=timezone.utc)
    payload = json.load(open(FX / "odds_pre.json"))
    game = dict(event_id="777", ts=(now + timedelta(hours=10)).isoformat().replace("+00:00", "Z"), season_type=2,
                home="DET", away="NY", completed=False, home_score=0, away_score=0)
    state = {"inj": [{"displayName": "New York Knicks", "injuries": [
        {"status": "Out", "athlete": {"displayName": "Star", "links": [{"rel": ["athlete"], "href": "x/id/123/star"}]}}]}]}
    monkeypatch.setattr(tracker, "now_utc", lambda: now)
    monkeypatch.setattr(tracker.espn, "scoreboard", lambda d: [game] if d == "20261021" else [])
    monkeypatch.setattr(tracker.espn, "odds_payload", lambda e: payload)
    monkeypatch.setattr(tracker.espn, "injuries_payload", lambda: {"injuries": state["inj"]})
    monkeypatch.setattr(rawstore, "RAW_DIR", tmp_path / "raw")
    tracker.snapshot(con)
    # 10 h antes del tip: no hay snapshot (fuera de E/D) pero SI un punto de trayectoria y un registro de lesion
    assert con.execute("SELECT COUNT(*) FROM snapshots").fetchone()[0] == 0
    assert con.execute("SELECT COUNT(*) FROM line_path").fetchone()[0] == 1
    assert con.execute("SELECT status FROM injury_log").fetchall()[0][0] == "Out"
    tracker.snapshot(con)                                    # mismo estado: la lesion no se vuelve a registrar
    assert con.execute("SELECT COUNT(*) FROM injury_log").fetchone()[0] == 1
    assert con.execute("SELECT COUNT(*) FROM line_path").fetchone()[0] == 2
    state["inj"][0]["injuries"][0]["status"] = "Day-To-Day"   # cambio de estado: se registra
    tracker.snapshot(con)
    assert [r[0] for r in con.execute("SELECT status FROM injury_log ORDER BY id")] == ["Out", "Day-To-Day"]
    state["inj"] = []                                         # API vacia (fallo): no inventa remociones
    tracker.snapshot(con)
    assert con.execute("SELECT COUNT(*) FROM injury_log").fetchone()[0] == 2
