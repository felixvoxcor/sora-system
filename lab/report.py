"""Reporte de CLV y veredicto segun FALSIFICATION.md. Solo usa el snapshot 'D' (decision)."""
import numpy as np
from scipy import stats

ALPHA = 0.025          # un-sided, por brazo (Bonferroni entre A y B)
N_DECIDE = 300         # apuestas hipoteticas con |edge| >= PRIMARY_THR
N_FUTILITY = 150
FUTILITY_CLV = -0.10
PRIMARY_THR = 2.0
THRESHOLDS = (1.0, 2.0, 3.0)


def load(con):
    q = """SELECT s.event_id, s.line, s.home_px, s.away_px, s.pred_a, s.pred_b, s.inj_adj,
                  c.close_line, r.home_score - r.away_score AS margin
           FROM snapshots s
           JOIN closes c ON c.event_id = s.event_id
           JOIN results r ON r.event_id = s.event_id
           WHERE s.label = 'D'"""
    return [dict(r) for r in con.execute(q)]


def _payout(px):
    px = px if px else -110.0
    return px / 100.0 if px > 0 else 100.0 / abs(px)


def arm_stats(rows, arm, thr):
    clv, profit, wins, n_bets = [], 0.0, 0, 0
    for r in rows:
        pred = r["pred_a"] if arm == "A" else r["pred_b"]
        edge = pred - r["line"]
        if abs(edge) < thr:
            continue
        side = 1 if edge > 0 else -1
        clv.append(side * (r["close_line"] - r["line"]))
        cover = side * (r["margin"] - r["line"])
        if cover == 0:
            continue
        n_bets += 1
        px = r["home_px"] if side == 1 else r["away_px"]
        if cover > 0:
            wins += 1
            profit += _payout(px)
        else:
            profit -= 1.0
    clv = np.array(clv)
    n = len(clv)
    out = dict(n=n, n_bets=n_bets, clv=float("nan"), se=float("nan"), t=float("nan"),
               p=float("nan"), win=float("nan"), roi=float("nan"))
    if n >= 2 and clv.std(ddof=1) > 0:
        se = clv.std(ddof=1) / np.sqrt(n)
        t = clv.mean() / se
        out.update(clv=float(clv.mean()), se=float(se), t=float(t),
                   p=float(stats.t.sf(t, n - 1)))
    if n_bets:
        out.update(win=wins / n_bets, roi=profit / n_bets)
    return out


def verdict(st):
    n = st["n"]
    if n >= N_DECIDE:
        return "PASA" if (st["clv"] > 0 and st["p"] < ALPHA) else "ARCHIVAR (no supera el criterio)"
    if n >= N_FUTILITY and st["clv"] < FUTILITY_CLV:
        return "ARCHIVAR (futilidad)"
    return f"EN CURSO ({n}/{N_DECIDE})"


def _ols_slope(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    if len(x) < 10 or x.std() == 0:
        return float("nan"), float("nan")
    xc = x - x.mean()
    b = (xc * (y - y.mean())).sum() / (xc ** 2).sum()
    res = y - y.mean() - b * xc
    se = np.sqrt(res.var(ddof=2) / (xc ** 2).sum())
    return float(b), float(b / se) if se > 0 else float("nan")


def render(con):
    rows = load(con)
    L = ["# Reporte NBA CLV Lab", "",
         f"Partidos con snapshot D + cierre + resultado: **{len(rows)}**", ""]
    if not rows:
        L.append("_Aun no hay partidos liquidados. El rastreador empieza a acumular desde el 2026-10-20._")
        return "\n".join(L)
    L += ["## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)", "",
          "| Brazo | Umbral | n | CLV medio | t | p (1 cola) | Win% vs snapshot | ROI papel |",
          "|---|---|---|---|---|---|---|---|"]
    for arm in ("A", "B"):
        for thr in THRESHOLDS:
            s = arm_stats(rows, arm, thr)
            L.append(f"| {arm} | {thr:g} | {s['n']} | {s['clv']:+.3f} | {s['t']:.2f} | "
                     f"{s['p']:.3f} | {s['win']*100:.1f}% | {s['roi']*100:+.2f}% |")
    L += ["", "## Veredicto pre-registrado (umbral primario = %g pts)" % PRIMARY_THR, ""]
    for arm in ("A", "B"):
        L.append(f"- Brazo {arm}: **{verdict(arm_stats(rows, arm, PRIMARY_THR))}**")
    mv = [r["close_line"] - r["line"] for r in rows]
    bA, tA = _ols_slope([r["pred_a"] - r["line"] for r in rows], mv)
    bI, tI = _ols_slope([r["inj_adj"] for r in rows], mv)
    L += ["", "## Prueba de liderazgo (exploratoria)", "",
          f"- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente {bA:.3f}, t = {tA:.2f}",
          f"- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente {bI:.3f}, t = {tI:.2f}",
          "", "_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._"]
    return "\n".join(L)
