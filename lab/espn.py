"""Cliente minimo de las APIs publicas de ESPN (scoreboard, odds, lesiones, box score)."""
import re, time
import requests

SB = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard"
INJ = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/injuries"
SUMMARY = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary"
ODDS = ("https://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/"
        "events/{e}/competitions/{e}/odds?lang=en&region=us")
PROVIDER_PRIORITY = ["58", "100", "38"]   # ESPN BET, DraftKings, Caesars

TEAM_ABBR = {
    "Atlanta Hawks": "ATL", "Boston Celtics": "BOS", "Brooklyn Nets": "BKN",
    "Charlotte Hornets": "CHA", "Chicago Bulls": "CHI", "Cleveland Cavaliers": "CLE",
    "Dallas Mavericks": "DAL", "Denver Nuggets": "DEN", "Detroit Pistons": "DET",
    "Golden State Warriors": "GS", "Houston Rockets": "HOU", "Indiana Pacers": "IND",
    "LA Clippers": "LAC", "Los Angeles Clippers": "LAC", "Los Angeles Lakers": "LAL",
    "Memphis Grizzlies": "MEM", "Miami Heat": "MIA", "Milwaukee Bucks": "MIL",
    "Minnesota Timberwolves": "MIN", "New Orleans Pelicans": "NO", "New York Knicks": "NY",
    "Oklahoma City Thunder": "OKC", "Orlando Magic": "ORL", "Philadelphia 76ers": "PHI",
    "Phoenix Suns": "PHX", "Portland Trail Blazers": "POR", "Sacramento Kings": "SAC",
    "San Antonio Spurs": "SA", "Toronto Raptors": "TOR", "Utah Jazz": "UTAH",
    "Washington Wizards": "WSH",
}

_S = requests.Session()


def get(url, params=None, tries=4):
    for i in range(tries):
        try:
            r = _S.get(url, params=params, timeout=25)
            if r.status_code == 200:
                return r.json()
            if r.status_code == 404:
                return None
        except Exception:
            pass
        time.sleep(1.5 * (i + 1))
    return None


def scoreboard(day_yyyymmdd):
    """Partidos de un dia: dict(event_id, ts, home, away, completed, home_score, away_score)."""
    j = get(SB, {"dates": day_yyyymmdd, "limit": 100}) or {}
    out = []
    for ev in j.get("events", []):
        c = ev["competitions"][0]
        h = next(t for t in c["competitors"] if t["homeAway"] == "home")
        a = next(t for t in c["competitors"] if t["homeAway"] == "away")
        out.append(dict(
            event_id=ev["id"], ts=ev["date"],
            season_type=ev.get("season", {}).get("type"),
            home=h["team"]["abbreviation"], away=a["team"]["abbreviation"],
            completed=bool(c["status"]["type"].get("completed")),
            home_score=int(h.get("score") or 0), away_score=int(a.get("score") or 0)))
    return out


def _american(node):
    try:
        v = str(node["american"]).replace("+", "").strip()
        if v.upper() in ("PK", "EVEN", "PICK"):
            return 0.0
        return float(v)
    except Exception:
        return None


def parse_odds(payload, kind, prefer_provider=None):
    """kind = 'current' (pre-partido) o 'close' (terminado).
    Devuelve line = margen esperado del LOCAL (= -spread local), o None."""
    items = (payload or {}).get("items", [])
    cands = []
    for it in items:
        ho = it.get("homeTeamOdds") or {}
        if ho.get(kind) and (ho[kind].get("pointSpread") is not None):
            cands.append(it)
    if not cands:
        return None

    def rank(it):
        pid = it["provider"]["id"]
        if prefer_provider and pid == prefer_provider:
            return -1
        return PROVIDER_PRIORITY.index(pid) if pid in PROVIDER_PRIORITY else 99
    it = sorted(cands, key=rank)[0]
    ho, ao = it["homeTeamOdds"], it.get("awayTeamOdds") or {}
    sp = _american(ho[kind]["pointSpread"])
    if sp is None:
        return None
    op = _american((ho.get("open") or {}).get("pointSpread") or {})
    return dict(
        provider_id=it["provider"]["id"], provider=it["provider"]["name"],
        line=-sp, open_line=(-op if op is not None else None),
        total=it.get("overUnder"),
        home_px=_american(((ho.get(kind) or {}).get("spread")) or {}),
        away_px=_american(((ao.get(kind) or {}).get("spread")) or {}))


def odds_payload(event_id):
    """Respuesta cruda de ESPN para las cuotas de un partido (se archiva con su hash)."""
    return get(ODDS.format(e=event_id))


def odds(event_id, kind, prefer_provider=None):
    return parse_odds(odds_payload(event_id), kind, prefer_provider)


def injuries_payload():
    return get(INJ)


def injuries(payload=None):
    """Lista de (team_abbr, player_id, name, status)."""
    j = (payload if payload is not None else get(INJ)) or {}
    out = []
    for t in j.get("injuries", []):
        team = TEAM_ABBR.get(t.get("displayName"))
        if not team:
            continue
        for i in t.get("injuries", []):
            a = i.get("athlete", {})
            href = next((l["href"] for l in a.get("links", [])
                         if "athlete" in l.get("rel", [])), "")
            m = re.search(r"/id/(\d+)", href)
            if m:
                out.append((team, m.group(1), a.get("displayName", ""), i.get("status", "")))
    return out


def boxscore_minutes(event_id):
    """Lista de (player_id, team_abbr, minutos, plus_minus) de un partido terminado."""
    j = get(SUMMARY, {"event": event_id}) or {}
    out = []
    for tm in j.get("boxscore", {}).get("players", []):
        team = tm["team"]["abbreviation"]
        for grp in tm.get("statistics", []):
            labels = grp.get("labels", [])
            if "MIN" not in labels:
                continue
            im = labels.index("MIN")
            ipm = labels.index("+/-") if "+/-" in labels else None
            for a in grp.get("athletes", []):
                st = a.get("stats", [])
                try:
                    mins = float(st[im])
                except Exception:
                    continue
                pm = None
                try:
                    pm = float(str(st[ipm]).replace("+", "")) if ipm is not None else None
                except Exception:
                    pass
                out.append((a["athlete"]["id"], team, mins, pm))
    return out
