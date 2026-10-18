"""Ratings online de margen. predict() nunca ve el partido que predice."""
import pandas as pd
from . import RATING_K, RATING_CARRY, HOME_ADV, MARGIN_CAP, NON_NBA


def season_of(day_et):
    """Octubre-junio comparten temporada: el anio en que EMPIEZA."""
    return (pd.Timestamp(day_et) - pd.Timedelta(days=200)).year


class Ratings:
    def __init__(self, k=RATING_K, carry=RATING_CARRY, hca=HOME_ADV, cap=MARGIN_CAP):
        self.k, self.carry, self.hca, self.cap = k, carry, hca, cap
        self.r, self.season = {}, None

    def predict(self, home, away):
        return self.r.get(home, 0.0) - self.r.get(away, 0.0) + self.hca

    def update(self, season, home, away, margin):
        if home in NON_NBA or away in NON_NBA:
            return
        if self.season is not None and season != self.season:
            self.r = {t: v * self.carry for t, v in self.r.items()}
        self.season = season
        pred = self.predict(home, away)
        err = max(-self.cap, min(self.cap, margin)) - pred
        self.r[home] = self.r.get(home, 0.0) + self.k * err
        self.r[away] = self.r.get(away, 0.0) - self.k * err


def build(history_csv, con):
    """Reconstruye ratings: historial inicial + resultados nuevos de la DB, en orden de fecha."""
    rows = []
    h = pd.read_csv(history_csv)
    for r in h.itertuples():
        rows.append((str(r.day_et)[:10], r.event_id, int(r.season), r.home, r.away, float(r.margin)))
    known = {r[1] for r in rows}
    for r in con.execute("SELECT event_id, day_et, season, home, away, home_score, away_score "
                         "FROM results"):
        if r["event_id"] not in known:
            rows.append((r["day_et"], r["event_id"], r["season"], r["home"], r["away"],
                         float(r["home_score"] - r["away_score"])))
    rows.sort(key=lambda x: (x[0], str(x[1])))
    R = Ratings()
    for day, _, season, home, away, margin in rows:
        R.update(season, home, away, margin)
    return R
