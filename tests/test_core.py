import json, sqlite3
from pathlib import Path
import numpy as np
import pytest
from lab import espn, injury, ratings, report, store
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
    assert label_for(24) == "E" and label_for(2) == "D" and label_for(0.5) is None
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
    assert report.verdict(dict(n=300, clv=0.2, p=0.01)) == "PASA"
    assert report.verdict(dict(n=300, clv=0.2, p=0.20)).startswith("ARCHIVAR")
    assert report.verdict(dict(n=300, clv=-0.1, p=0.9)).startswith("ARCHIVAR")
    assert report.verdict(dict(n=150, clv=-0.2, p=0.9)) == "ARCHIVAR (futilidad)"
    assert report.verdict(dict(n=100, clv=-0.5, p=0.9)).startswith("EN CURSO")


def test_empty_report(con):
    assert "Aun no hay partidos" in report.render(con)
