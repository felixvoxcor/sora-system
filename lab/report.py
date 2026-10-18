"""Reporte de CLV y veredicto segun FALSIFICATION.md (v1.1). Solo usa el snapshot 'D' (1-2 h antes del tip)."""
import numpy as np
from scipy import stats

ALPHA = 0.025            # una cola, por brazo (Bonferroni entre A y B)
N_DECIDE = 500           # apuestas hipoteticas con |edge| >= PRIMARY_THR, por brazo. Un solo analisis final.
N_INTERIM = 250          # unica revision intermedia: SOLO futilidad, nunca exito
FUTILITY_UB = 0.05       # futilidad si el limite superior (97.5%, 1 cola) del CLV < +0.05 pts
PRIMARY_THR = 2.0
THRESHOLDS = (1.0, 2.0, 3.0)
MIN_COVERAGE = 0.80      # cobertura minima de la ventana D para que el veredicto sea valido


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
    out = dict(n=n, n_bets=n_bets, clv=float("nan"), se=float("nan"), sd=float("nan"), t=float("nan"),
               p=float("nan"), lo=float("nan"), hi=float("nan"), ub=float("nan"),
               win=float("nan"), roi=float("nan"))
    if n >= 2 and clv.std(ddof=1) > 0:
        sd = clv.std(ddof=1)
        se = sd / np.sqrt(n)
        t = clv.mean() / se
        out.update(clv=float(clv.mean()), se=float(se), sd=float(sd), t=float(t),
                   p=float(stats.t.sf(t, n - 1)),
                   lo=float(clv.mean() - stats.t.ppf(0.975, n - 1) * se),
                   hi=float(clv.mean() + stats.t.ppf(0.975, n - 1) * se),
                   ub=float(clv.mean() + stats.t.ppf(1 - ALPHA, n - 1) * se))
    if n_bets:
        out.update(win=wins / n_bets, roi=profit / n_bets)
    return out


def verdict(st, coverage_ok=True):
    """Reglas v1.1: un unico analisis final en N_DECIDE; futilidad (solo futilidad) en N_INTERIM."""
    n = st["n"]
    if n >= N_DECIDE:
        if not coverage_ok:
            return "INVALIDO (cobertura de la ventana D < 80%)"
        return "PASA" if (st["clv"] > 0 and st["p"] < ALPHA) else "ARCHIVAR (no supera el criterio)"
    if n >= N_INTERIM and st["ub"] < FUTILITY_UB:
        return "ARCHIVAR (futilidad)"
    return f"EN CURSO ({n}/{N_DECIDE})"


def mde(sd, n=N_DECIDE):
    """Efecto minimo detectable (80% de potencia, alfa 1 cola 0.025) para una SD de CLV dada."""
    return (1.96 + 0.8416) * sd / np.sqrt(n)


def coverage(con):
    """Cobertura: partidos terminados que el sistema vio vs los que tienen snapshot D."""
    q = """SELECT r.event_id, r.ts,
                  EXISTS(SELECT 1 FROM snapshots s WHERE s.event_id=r.event_id AND s.label='D') AS d,
                  EXISTS(SELECT 1 FROM snapshots s WHERE s.event_id=r.event_id AND s.label='DX') AS dx,
                  EXISTS(SELECT 1 FROM capture_log c WHERE c.event_id=r.event_id AND c.status='no_odds') AS noodds,
                  EXISTS(SELECT 1 FROM games_seen g WHERE g.event_id=r.event_id) AS seen
           FROM results r
           WHERE r.event_id IN (SELECT event_id FROM games_seen)"""
    rows = [dict(r) for r in con.execute(q)]
    n = len(rows)
    nd = sum(r["d"] for r in rows)
    ndx = sum(1 for r in rows if not r["d"] and r["dx"])
    nno = sum(1 for r in rows if not r["d"] and not r["dx"] and r["noodds"])
    nmiss = n - nd - ndx - nno
    return dict(n=n, d=nd, dx=ndx, no_odds=nno, missed=nmiss, frac=(nd / n if n else float("nan")))


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
    cov = coverage(con)
    L = ["# Reporte NBA CLV Lab (protocolo v1.1)", "",
         f"Partidos con snapshot D + cierre + resultado: **{len(rows)}**", ""]
    if not rows:
        L.append("_Aun no hay partidos liquidados. El rastreador empieza a acumular desde el 2026-10-20._")
        return "\n".join(L)
    L += ["## Cobertura de la ventana D (control de sesgo de seleccion)", "",
          f"- Partidos terminados observados: {cov['n']} · con D: **{cov['d']} ({cov['frac']*100:.0f}%)** · "
          f"solo respaldo DX: {cov['dx']} · sin cuotas: {cov['no_odds']} · perdidos por el cron: {cov['missed']}",
          f"- Minimo exigido para que el veredicto sea valido: {MIN_COVERAGE*100:.0f}%", ""]
    cov_ok = (cov["n"] == 0) or cov["frac"] >= MIN_COVERAGE
    L += ["## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)", "",
          "| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |",
          "|---|---|---|---|---|---|---|---|"]
    for arm in ("A", "B"):
        for thr in THRESHOLDS:
            s = arm_stats(rows, arm, thr)
            L.append(f"| {arm} | {thr:g} | {s['n']} | {s['clv']:+.3f} | [{s['lo']:+.3f}, {s['hi']:+.3f}] | "
                     f"{s['t']:.2f} | {s['p']:.3f} | {s['roi']*100:+.2f}% |")
    L += ["", "Decide SOLO el umbral %g y el CLV; el ROI en papel no decide nada." % PRIMARY_THR,
          "", "## Veredicto pre-registrado (umbral primario = %g pts)" % PRIMARY_THR, ""]
    for arm in ("A", "B"):
        s = arm_stats(rows, arm, PRIMARY_THR)
        extra = f" · SD observada {s['sd']:.2f} → efecto minimo detectable con n={N_DECIDE}: {mde(s['sd']):.2f} pts" \
            if s["sd"] == s["sd"] else ""
        L.append(f"- Brazo {arm}: **{verdict(s, cov_ok)}**{extra}")
    mv = [r["close_line"] - r["line"] for r in rows]
    bA, tA = _ols_slope([r["pred_a"] - r["line"] for r in rows], mv)
    bI, tI = _ols_slope([r["inj_adj"] for r in rows], mv)
    L += ["", "## Prueba de liderazgo (exploratoria)", "",
          f"- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente {bA:.3f}, t = {tA:.2f}",
          f"- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente {bI:.3f}, t = {tI:.2f}",
          "", "_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._"]
    return "\n".join(L)
