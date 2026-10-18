"""Baja el summary de ESPN de cada partido historico: arbitros, box score completo, DNP, lesiones del partido."""
import json, sys, pandas as pd
from concurrent.futures import ThreadPoolExecutor
import requests
S = requests.Session()
URL = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary"

def fetch(eid):
    try:
        return _fetch(eid)
    except Exception as e:
        return {"event_id": eid, "error": repr(e)}

def _fetch(eid):
    for i in range(4):
        try:
            r = S.get(URL, params={"event": eid}, timeout=30)
            if r.status_code == 200:
                d = r.json(); break
            if r.status_code == 404: return {"event_id": eid, "error": 404}
        except Exception:
            d = None
    else:
        return {"event_id": eid, "error": "fail"}
    rec = {"event_id": eid}
    rec["officials"] = [o.get("displayName") for o in d.get("gameInfo", {}).get("officials", [])]
    rec["attendance"] = d.get("gameInfo", {}).get("attendance")
    teams = {}
    for t in d.get("boxscore", {}).get("teams", []):
        teams[t["team"]["abbreviation"]] = {s["name"]: s.get("displayValue") for s in t.get("statistics", [])}
    rec["team_stats"] = teams
    players = []
    for tm in d.get("boxscore", {}).get("players", []):
        ab = tm["team"]["abbreviation"]
        for grp in tm.get("statistics", []):
            labels = grp.get("labels", [])
            for a in grp.get("athletes", []):
                p = {"team": ab, "id": a["athlete"].get("id"), "name": a["athlete"].get("displayName"),
                     "starter": a.get("starter"), "dnp": a.get("didNotPlay"), "reason": a.get("reason")}
                if a.get("stats") and labels:
                    p["stats"] = dict(zip(labels, a["stats"]))
                players.append(p)
    rec["players"] = players
    inj = []
    for t in d.get("injuries", []) or []:
        ab = t.get("team", {}).get("abbreviation")
        for i in t.get("injuries", []):
            inj.append({"team": ab, "name": i.get("athlete", {}).get("displayName"),
                        "status": i.get("status"), "type": (i.get("type") or {}).get("description") if isinstance(i.get("type"), dict) else None})
    rec["injuries"] = inj
    return rec

if __name__ == "__main__":
    ids = pd.read_csv("data/games_odds.csv.gz", dtype={"event_id": str}).event_id.tolist()
    with ThreadPoolExecutor(12) as ex, open("summaries.jsonl", "w") as f:
        for n, rec in enumerate(ex.map(fetch, ids)):
            f.write(json.dumps(rec) + "\n")
            if n % 500 == 0: print(n, flush=True)
    print("done", len(ids))
