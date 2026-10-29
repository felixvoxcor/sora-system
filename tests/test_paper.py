import json
from datetime import datetime, timezone
from pathlib import Path
import pytest
from lab import espn, paper, paper_report, store, totals, tracker

FX = Path(__file__).parent / "fixtures"
T0 = datetime(2026, 10, 25, 12, 0, tzinfo=timezone.utc)


@pytest.fixture
def con(tmp_path):
    return store.connect(tmp_path / "t.db")


def odds(**kw):
    o = dict(provider_id="100", line=-3.5, home_px=-110.0, away_px=-110.0, total=220.5, ml_home=-160.0, ml_away=140.0,
             over_px=-110.0, under_px=-110.0)
    o.update(kw)
    return o


def test_payout_and_novig():
    assert paper.payout(-110) == pytest.approx(100 / 110)
    assert paper.payout(150) == 1.5
    assert paper.payout(None) == pytest.approx(100 / 110)
    assert paper.novig(-110, -110) == pytest.approx(0.5)
    assert 0.5 < paper.novig(-200, 170) < 0.7


def test_candidates_sides_and_edges():
    c = {(x["model"], x["market"]): x for x in paper.candidates(odds(), pred_a=-1.0, pred_b=-6.0, pred_total=225.0)}
    assert c[("A", "spread")]["side"] == "home" and c[("A", "spread")]["edge"] == pytest.approx(2.5)
    assert c[("B", "spread")]["side"] == "away" and c[("B", "spread")]["edge"] == pytest.approx(-2.5)
    assert c[("T", "total")]["side"] == "over" and c[("T", "total")]["edge"] == pytest.approx(4.5)
    assert c[("A", "ml")]["side"] in ("home", "away") and c[("A", "ml")]["ev"] is not None
    assert len(c) == 5


def test_candidates_missing_markets():
    c = paper.candidates(odds(ml_home=None, ml_away=None, total=None), 1.0, 1.0, None)
    assert {(x["model"], x["market"]) for x in c} == {("A", "spread"), ("B", "spread")}


def test_settle_rows():
    r = dict(market="spread", side="home", line=-3.5, price=-110)
    assert paper.settle_row(r, 100, 95) == (pytest.approx(100 / 110), "W")        # margen 5 > -3.5
    assert paper.settle_row(dict(r, side="away"), 100, 95)[1] == "L"
    assert paper.settle_row(dict(r, line=5.0), 100, 95)[1] == "P"                   # push
    t = dict(market="total", side="over", line=200.5, price=-105)
    assert paper.settle_row(t, 110, 95)[1] == "W" and paper.settle_row(dict(t, side="under"), 110, 95)[1] == "L"
    m = dict(market="ml", side="away", line=None, price=140)
    assert paper.settle_row(m, 90, 100) == (1.4, "W")


def test_entry_windows():
    assert paper.entry_for(24.0) == ["E"] and paper.entry_for(6.0) == ["H6"] and paper.entry_for(1.5) == ["D"]
    assert paper.entry_for(0.3) == ["L"] and paper.entry_for(10.0) == []


def test_record_once_per_entry_and_append_only(con):
    n1 = paper.record(con, "1", 1.5, T0, odds(), -1.0, -2.0, 224.0)
    n2 = paper.record(con, "1", 1.2, T0, odds(line=-4.5), -1.0, -2.0, 224.0)       # misma entrada: no se repite
    assert n1 == 5 and n2 == 0
    con.commit()
    with pytest.raises(Exception):
        con.execute("UPDATE paper_eval SET edge=99")
    with pytest.raises(Exception):
        con.execute("DELETE FROM paper_eval")


def _fill(con, n=120):
    import random
    rnd = random.Random(1)
    for i in range(n):
        hs, as_ = 100 + rnd.randint(-15, 25), 100 + rnd.randint(-15, 25)
        eid = str(1000 + i)
        con.execute("INSERT INTO results VALUES (?,?,?,?,?,?,?,?)", (eid, "2026-10-25T23:00Z", "2026-10-25", 2026, "AAA", "BBB", hs, as_))
        for tte, entry_line in ((24.0, -3.0), (1.5, -3.5)):
            o = odds(line=entry_line + rnd.choice([-0.5, 0, 0.5]))
            paper.record(con, eid, tte, T0, o, rnd.uniform(-8, 3), rnd.uniform(-8, 3), 220 + rnd.uniform(-8, 8))
        con.execute("INSERT INTO line_path(event_id,taken_at,tte_hours,provider_id,line,home_px,away_px,total,ml_home,ml_away,over_px,under_px)"
                    " VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (eid, T0.isoformat(), 0.2, "100", -3.5, -110, -110, 220.5, -160, 140, -110, -110))
    con.commit()


def test_report_renders_with_data(con):
    _fill(con)
    txt = paper_report.render(con)
    assert "SPREAD · modelo A" in txt and "TOTAL · modelo T" in txt and "Eficiencia del mercado" in txt
    assert "D+conf" in txt


def test_report_matches_manual_roi(con):
    _fill(con)
    rows = [r for r in paper_report._rows(con) if r["market"] == "spread" and r["model"] == "A" and r["entry"] == "D"
            and r["abs_edge"] >= 2.0]
    manual = sum(r["profit"] for r in rows) / len(rows)
    assert paper_report.cell(rows)["roi"] == pytest.approx(manual)


def test_bh_controls():
    assert paper_report.bh([0.001, 0.2, 0.9, 0.8], q=0.10) == {0}
    assert paper_report.bh([0.5, 0.6, 0.7], q=0.10) == set()


def test_total_model_online_no_lookahead():
    m = totals.TotalModel()
    p0 = m.predict("A", "B")
    m.update(2026, "A", "B", 140, 130)
    assert p0 == totals.MU0 * 2
    assert m.predict("A", "B") > p0


def test_parse_odds_full_markets():
    o = espn.parse_odds(json.load(open(FX / "odds_pre.json")), "current")
    assert o["ml_home"] == -115 and o["ml_away"] == -105 and o["over_px"] == -105 and o["under_px"] == -115


def test_line_path_dedup(con):
    o = odds()
    tracker._log_path(con, "9", T0, 2.0, o)
    tracker._log_path(con, "9", T0.replace(minute=3), 1.95, o)                      # igual y <10 min: no se guarda
    tracker._log_path(con, "9", T0.replace(minute=15), 1.75, o)                     # igual pero >=10 min: se guarda
    tracker._log_path(con, "9", T0.replace(minute=16), 1.7, odds(line=-4.0))        # cambio: se guarda
    assert con.execute("SELECT COUNT(*) FROM line_path").fetchone()[0] == 3


def test_watch_survives_snapshot_error(con, monkeypatch):
    calls = {"n": 0}
    def boom(c):
        calls["n"] += 1
        raise RuntimeError("falla de red")
    monkeypatch.setattr(tracker, "snapshot", boom)
    monkeypatch.setattr(tracker, "settle", lambda c: None)
    monkeypatch.setattr(tracker, "write_report", lambda c: None)
    monkeypatch.setattr(tracker.time, "sleep", lambda s: None)
    tracker.watch(con, minutes=0.002, every=0.001)
    assert calls["n"] >= 1
    assert con.execute("SELECT COUNT(*) FROM poll_log WHERE status LIKE 'error:%'").fetchone()[0] >= 1
