"""Modelo de totales (puntos de ambos equipos). Online, sin mirar el partido que predice.
Parametros CONGELADOS (iguales a los del estudio de totales): K=0.05, carry=0.5, mu inicial 112, mu aprende 0.01."""
import pandas as pd
from . import NON_NBA

TOTAL_K = 0.05
TOTAL_CARRY = 0.5
MU0, MU_RATE = 112.0, 0.01


class TotalModel:
    def __init__(self):
        self.o, self.d, self.mu, self.season = {}, {}, MU0, None

    def _parts(self, home, away):
        ph = self.mu + self.o.get(home, 0.0) + self.d.get(away, 0.0)
        pa = self.mu + self.o.get(away, 0.0) + self.d.get(home, 0.0)
        return ph, pa

    def predict(self, home, away):
        ph, pa = self._parts(home, away)
        return ph + pa

    def update(self, season, home, away, hs, as_):
        if home in NON_NBA or away in NON_NBA:
            return
        if self.season is not None and season != self.season:
            self.o = {t: v * TOTAL_CARRY for t, v in self.o.items()}
            self.d = {t: v * TOTAL_CARRY for t, v in self.d.items()}
        self.season = season
        ph, pa = self._parts(home, away)
        eh, ea = hs - ph, as_ - pa
        self.o[home] = self.o.get(home, 0.0) + TOTAL_K * eh
        self.d[away] = self.d.get(away, 0.0) + TOTAL_K * eh
        self.o[away] = self.o.get(away, 0.0) + TOTAL_K * ea
        self.d[home] = self.d.get(home, 0.0) + TOTAL_K * ea
        self.mu += MU_RATE * ((hs + as_) / 2 - self.mu)


def build(scores_csv, con):
    """Historial de marcadores + resultados nuevos de la DB, en orden de fecha."""
    rows = []
    for r in pd.read_csv(scores_csv, dtype={"event_id": str}).itertuples():
        rows.append((str(r.day_et)[:10], r.event_id, int(r.season), r.home, r.away, float(r.home_score), float(r.away_score)))
    known = {r[1] for r in rows}
    for r in con.execute("SELECT event_id, day_et, season, home, away, home_score, away_score FROM results"):
        if str(r["event_id"]) not in known:
            rows.append((r["day_et"], str(r["event_id"]), r["season"], r["home"], r["away"],
                         float(r["home_score"]), float(r["away_score"])))
    rows.sort(key=lambda x: (x[0], x[1]))
    m = TotalModel()
    for day, _, season, home, away, hs, as_ in rows:
        m.update(season, home, away, hs, as_)
    return m
