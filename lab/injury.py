"""Capa de lesiones (brazo B). Hipotesis: el mercado tarda en incorporar noticias de lesiones.
Ajuste = INJ_BETA * sum_i p_out_i * (min_prom_i / 36)^2   (puntos de margen perdidos por equipo).
Los parametros estan congelados; NO se calibran sobre estos datos (no hay lesiones historicas)."""
import json
from . import INJ_BETA, P_OUT


def avg_minutes(con, n=10):
    """Minutos promedio por jugador en sus ultimas n apariciones (>0 min)."""
    out = {}
    for r in con.execute("SELECT player_id, minutes FROM minutes WHERE minutes>0 "
                         "ORDER BY day_et DESC, event_id DESC"):
        lst = out.setdefault(r["player_id"], [])
        if len(lst) < n:
            lst.append(r["minutes"])
    return {p: sum(v) / len(v) for p, v in out.items()}


def team_loss(team, injuries, mins):
    """Puntos perdidos por el equipo por jugadores ausentes."""
    loss, detail = 0.0, []
    for t, pid, name, status in injuries:
        if t != team:
            continue
        p = P_OUT.get(status, 0.0)
        m = mins.get(pid)
        if not p or not m:
            continue
        v = INJ_BETA * p * (m / 36.0) ** 2
        loss += v
        detail.append(dict(player=name, status=status, avg_min=round(m, 1), pts=round(v, 2)))
    return loss, detail


def adjustment(home, away, injuries, mins):
    """Ajuste al margen esperado del LOCAL (positivo = favorece al local) y detalle JSON."""
    lh, dh = team_loss(home, injuries, mins)
    la, da = team_loss(away, injuries, mins)
    return la - lh, json.dumps({"home": dh, "away": da})
