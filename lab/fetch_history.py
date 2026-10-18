"""Descarga partidos NBA + lineas open/close desde la API publica de ESPN.
Uso: python fetch_espn.py START END out.csv   (fechas YYYYMMDD)
"""
import sys, json, csv, time, datetime as dt
from concurrent.futures import ThreadPoolExecutor
import requests

S = requests.Session()
SB = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard"
ODDS = "https://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/events/{e}/competitions/{e}/odds?lang=en&region=us"


def get(url, params=None, tries=4):
    for i in range(tries):
        try:
            r = S.get(url, params=params, timeout=25)
            if r.status_code == 200:
                return r.json()
            if r.status_code == 404:
                return None
        except Exception:
            pass
        time.sleep(1.5 * (i + 1))
    return None


def days(a, b):
    d = dt.datetime.strptime(a, "%Y%m%d")
    e = dt.datetime.strptime(b, "%Y%m%d")
    while d <= e:
        yield d.strftime("%Y%m%d")
        d += dt.timedelta(days=1)


def games_for_day(day):
    j = get(SB, {"dates": day, "limit": 100})
    out = []
    if not j:
        return out
    for ev in j.get("events", []):
        c = ev["competitions"][0]
        if not c["status"]["type"].get("completed"):
            continue
        h = next(t for t in c["competitors"] if t["homeAway"] == "home")
        a = next(t for t in c["competitors"] if t["homeAway"] == "away")
        out.append(dict(
            event_id=ev["id"], date=ev["date"], day=day,
            season_type=ev.get("season", {}).get("type"),
            home=h["team"]["abbreviation"], away=a["team"]["abbreviation"],
            home_score=int(h.get("score", 0)), away_score=int(a.get("score", 0)),
        ))
    return out


def am(x):
    try:
        return float(x["american"].replace("+", ""))
    except Exception:
        return None


def pt(x):
    try:
        return float(x["pointSpread"]["american"].replace("+", "").replace("PK", "0"))
    except Exception:
        return None


def odds_for(g):
    j = get(ODDS.format(e=g["event_id"]))
    row = dict(g)
    if not j:
        return row
    items = j.get("items", [])
    # preferimos proveedor con open+close (ESPN BET id 58, o el primero con 'close')
    pick = None
    for it in items:
        if it["provider"]["id"] in ("58", "100", "38") and "close" in (it.get("homeTeamOdds") or {}):
            pick = it
            break
    if pick is None and items:
        pick = items[0]
    if pick is None:
        return row
    ho, ao = pick.get("homeTeamOdds") or {}, pick.get("awayTeamOdds") or {}
    row.update(
        provider=pick["provider"]["name"],
        total_close=pick.get("overUnder"),
        # spread desde la perspectiva del LOCAL (negativo = local favorito)
        h_spread_open=pt(ho.get("open", {})), h_spread_close=pt(ho.get("close", {})),
        h_spread_open_px=am(ho.get("open", {}).get("spread", {})) if ho.get("open") else None,
        h_spread_close_px=am(ho.get("close", {}).get("spread", {})) if ho.get("close") else None,
        a_spread_close_px=am(ao.get("close", {}).get("spread", {})) if ao.get("close") else None,
        h_ml_open=am(ho.get("open", {}).get("moneyLine", {})) if ho.get("open") else None,
        h_ml_close=am(ho.get("close", {}).get("moneyLine", {})) if ho.get("close") else None,
        a_ml_close=am(ao.get("close", {}).get("moneyLine", {})) if ao.get("close") else None,
    )
    return row


if __name__ == "__main__":
    a, b, out = sys.argv[1:4]
    with ThreadPoolExecutor(8) as ex:
        games = [g for lst in ex.map(games_for_day, days(a, b)) for g in lst]
    print("games", len(games), flush=True)
    with ThreadPoolExecutor(10) as ex:
        rows = list(ex.map(odds_for, games))
    keys = sorted({k for r in rows for k in r})
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        w.writerows(rows)
    n = sum(1 for r in rows if r.get("h_spread_close") is not None)
    print("rows", len(rows), "with close spread", n)
