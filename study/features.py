"""Une odds + resultados + summaries en una tabla ordenada por fecha. Sin transformaciones con lookahead."""
import gzip, json, re
from pathlib import Path
import numpy as np, pandas as pd

NON_NBA = {"CAN", "CHK", "KEN", "SHQ"}
DATA = Path(__file__).resolve().parent / "data"
BASE = DATA / "games_odds.csv.gz"
SUMS = DATA / "summaries.jsonl.gz"


def _f(x):
    try:
        return float(str(x).replace("+", ""))
    except Exception:
        return np.nan


def _pair(s):
    try:
        a, b = str(s).split("-"); return float(a), float(b)
    except Exception:
        return np.nan, np.nan


def team_factors(ts):
    """Four factors a partir de las estadisticas de equipo del summary."""
    fgm, fga = _pair(ts.get("fieldGoalsMade-fieldGoalsAttempted"))
    tpm, _ = _pair(ts.get("threePointFieldGoalsMade-threePointFieldGoalsAttempted"))
    ftm, fta = _pair(ts.get("freeThrowsMade-freeThrowsAttempted"))
    oreb, dreb, to = _f(ts.get("offensiveRebounds")), _f(ts.get("defensiveRebounds")), _f(ts.get("turnovers"))
    return dict(fgm=fgm, fga=fga, tpm=tpm, ftm=ftm, fta=fta, oreb=oreb, dreb=dreb, to=to)


def load():
    df = pd.read_csv(BASE, dtype={"event_id": str})
    df = df[~df.home.isin(NON_NBA) & ~df.away.isin(NON_NBA)].copy()
    sums = {}
    for l in gzip.open(SUMS, "rt"):
        r = json.loads(l)
        if "error" not in r:
            sums[r["event_id"]] = r
    df = df[df.event_id.isin(sums)].copy()
    df = df.sort_values(["ts", "event_id"]).reset_index(drop=True)
    df["total"] = df.home_score + df.away_score
    df = df.dropna(subset=["total_close", "line", "line_open"]).reset_index(drop=True)
    df["res_m"] = df.margin - df.line            # >0: el local supero la linea
    df["res_t"] = df.total - df.total_close      # >0: salio mas alto que el total
    recs = []
    for r in df.itertuples():
        s = sums[r.event_id]
        h, a = s["team_stats"].get(r.home, {}), s["team_stats"].get(r.away, {})
        recs.append(dict(refs=s["officials"], fh=team_factors(h), fa=team_factors(a), players=s["players"]))
    df["refs"] = [x["refs"] for x in recs]
    df["fh"] = [x["fh"] for x in recs]
    df["fa"] = [x["fa"] for x in recs]
    df["players"] = [x["players"] for x in recs]
    return df


if __name__ == "__main__":
    d = load(); print(len(d), d.season.value_counts().sort_index().to_dict())
    print(d[["res_m", "res_t"]].describe().loc[["mean", "std"]])
