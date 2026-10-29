"""Apuestas FICTICIAS con los mercados reales (spread, moneyline, total) y precios reales de la casa (ESPN/DraftKings).
No son parte del veredicto de FALSIFICATION.md: son un laboratorio exploratorio para medir como habria ido y que ajustar.
Regla clave: se registra la EVALUACION de cada partido en cada punto de entrada (apostado o no), con el borde del modelo.
Los 'niveles de riesgo' son umbrales que se aplican despues, sobre estas filas inmutables (paper_eval es append-only)."""
import math
from statistics import NormalDist

PAPER_VERSION = "p1.0"
SD_MARGIN = 13.8                       # desvio del margen NBA contra la linea de cierre, medido en el historial 2023-26 (congelado)
N01 = NormalDist()

# Puntos de entrada (horas antes del tip). La primera captura dentro de la ventana fija la entrada.
ENTRIES = {"E": (20.0, 26.0), "H6": (5.0, 7.0), "D": (1.0, 2.0), "L": (0.1, 0.5)}

# Niveles de riesgo 1 (muy selectivo) .. 5 (casi todo): umbral minimo del borde en PUNTOS, por mercado.
LEVELS = {
    "spread": (4.0, 3.0, 2.0, 1.0, 0.5),
    "ml": (4.0, 3.0, 2.0, 1.0, 0.5),
    "total": (6.0, 4.0, 3.0, 2.0, 1.0),
}
STAKE = 1.0                            # unidad fija; otros tamanos (Kelly) se calculan despues sobre las mismas filas


def entry_for(tte):
    return [k for k, (a, b) in ENTRIES.items() if a <= tte <= b]


def payout(px):
    """Ganancia neta por unidad apostada con cuota americana px (si px falta se asume -110)."""
    px = -110.0 if px is None else px
    return px / 100.0 if px > 0 else 100.0 / abs(px)


def implied(px):
    px = -110.0 if px is None else px
    return 100.0 / (px + 100.0) if px > 0 else abs(px) / (abs(px) + 100.0)


def novig(px_a, px_b):
    a, b = implied(px_a), implied(px_b)
    return a / (a + b)


def margin_from_prob(p_home):
    p = min(max(p_home, 0.001), 0.999)
    return SD_MARGIN * N01.inv_cdf(p)


def prob_from_margin(m):
    return N01.cdf(m / SD_MARGIN)


def candidates(o, pred_a, pred_b, pred_total):
    """Filas candidatas (sin guardar) para un partido y un instante. o = parse_odds(...,'current')."""
    out = []
    preds = (("A", pred_a), ("B", pred_b))
    for model, pred in preds:
        # --- spread: linea = margen esperado del local
        if o.get("line") is not None:
            edge = pred - o["line"]
            home = edge > 0
            px = o["home_px"] if home else o["away_px"]
            other = o["away_px"] if home else o["home_px"]
            out.append(dict(model=model, market="spread", side="home" if home else "away", line=o["line"],
                            price=px, edge=edge, p_model=None,
                            p_mkt=novig(px, other) if (px is not None and other is not None) else 0.5, ev=None))
        # --- moneyline: borde en puntos = pred - margen implicito del mercado (sin vig)
        if o.get("ml_home") is not None and o.get("ml_away") is not None:
            p_mkt_home = novig(o["ml_home"], o["ml_away"])
            edge = pred - margin_from_prob(p_mkt_home)
            home = edge > 0
            p_mod = prob_from_margin(pred) if home else 1 - prob_from_margin(pred)
            px = o["ml_home"] if home else o["ml_away"]
            out.append(dict(model=model, market="ml", side="home" if home else "away", line=None, price=px,
                            edge=edge, p_model=p_mod, p_mkt=p_mkt_home if home else 1 - p_mkt_home,
                            ev=p_mod * payout(px) - (1 - p_mod)))
    # --- total: modelo propio de totales
    if pred_total is not None and o.get("total") is not None:
        edge = pred_total - o["total"]
        over = edge > 0
        px = o["over_px"] if over else o["under_px"]
        other = o["under_px"] if over else o["over_px"]
        out.append(dict(model="T", market="total", side="over" if over else "under", line=o["total"], price=px,
                        edge=edge, p_model=None,
                        p_mkt=novig(px, other) if (px is not None and other is not None) else 0.5, ev=None))
    return out


def record(con, event_id, tte, t0, o, pred_a, pred_b, pred_total):
    """Guarda las evaluaciones de los puntos de entrada cuya ventana contiene tte y que aun no existen. Devuelve n filas."""
    n = 0
    for entry in entry_for(tte):
        if con.execute("SELECT 1 FROM paper_eval WHERE event_id=? AND entry=? LIMIT 1", (event_id, entry)).fetchone():
            continue
        for c in candidates(o, pred_a, pred_b, pred_total):
            cur = con.execute(
                "INSERT OR IGNORE INTO paper_eval(event_id,entry,taken_at,tte_hours,model,market,side,line,price,"
                "edge,p_model,p_mkt,ev,provider_id,version) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (event_id, entry, t0.isoformat(), tte, c["model"], c["market"], c["side"], c["line"], c["price"],
                 c["edge"], c["p_model"], c["p_mkt"], c["ev"], o.get("provider_id"), PAPER_VERSION))
            n += cur.rowcount
    return n


def settle_row(r, home_score, away_score):
    """Resultado de una fila: (profit_en_unidades, resultado 'W'/'L'/'P')."""
    margin, total = home_score - away_score, home_score + away_score
    if r["market"] == "spread":
        s = 1 if r["side"] == "home" else -1
        cover = s * (margin - r["line"])
    elif r["market"] == "ml":
        cover = (margin if r["side"] == "home" else -margin)
    else:
        s = 1 if r["side"] == "over" else -1
        cover = s * (total - r["line"])
    if cover == 0:
        return 0.0, "P"
    return (STAKE * payout(r["price"]), "W") if cover > 0 else (-STAKE, "L")
