"""Reporte de las apuestas ficticias (EXPLORATORIO: no decide nada; el veredicto sigue en REPORT.md).
Matriz entrada x nivel de riesgo x mercado, con ROI en unidades fijas, CLV contra la ultima linea previa al tip,
eficiencia del mercado (pendiente del resultado sobre el borde, Brier) y correccion Benjamini-Hochberg por numero de celdas."""
import numpy as np
from scipy import stats
from . import paper

MIN_N = 30
CONF_MOVE = {"spread": 0.5, "total": 0.5, "ml": 0.01}


def _rows(con):
    q = """SELECT p.*, r.home_score, r.away_score,
                  (SELECT line FROM line_path l WHERE l.event_id=p.event_id AND l.tte_hours>0 ORDER BY l.id DESC LIMIT 1) AS c_line,
                  (SELECT total FROM line_path l WHERE l.event_id=p.event_id AND l.tte_hours>0 ORDER BY l.id DESC LIMIT 1) AS c_total,
                  (SELECT ml_home FROM line_path l WHERE l.event_id=p.event_id AND l.tte_hours>0 ORDER BY l.id DESC LIMIT 1) AS c_mlh,
                  (SELECT ml_away FROM line_path l WHERE l.event_id=p.event_id AND l.tte_hours>0 ORDER BY l.id DESC LIMIT 1) AS c_mla
           FROM paper_eval p JOIN results r ON r.event_id = p.event_id"""
    out = []
    for r in con.execute(q):
        d = dict(r)
        d["profit"], d["res"] = paper.settle_row(d, d["home_score"], d["away_score"])
        d["clv"] = _clv(d)
        d["abs_edge"] = abs(d["edge"])
        out.append(d)
    return out


def _clv(d):
    if d["market"] == "spread":
        if d["c_line"] is None:
            return None
        return (1 if d["side"] == "home" else -1) * (d["c_line"] - d["line"])
    if d["market"] == "total":
        if d["c_total"] is None:
            return None
        return (1 if d["side"] == "over" else -1) * (d["c_total"] - d["line"])
    if d["c_mlh"] is None or d["c_mla"] is None:
        return None
    p_home = paper.novig(d["c_mlh"], d["c_mla"])
    return (p_home if d["side"] == "home" else 1 - p_home) - d["p_mkt"]


def derived_entries(rows):
    """D+conf / D+fade: entrada en D solo si el mercado ya se movio hacia (conf) o contra (fade) nuestro lado desde E."""
    e = {(r["event_id"], r["model"], r["market"]): r for r in rows if r["entry"] == "E"}
    out = []
    for r in rows:
        if r["entry"] != "D":
            continue
        r0 = e.get((r["event_id"], r["model"], r["market"]))
        if not r0 or r0["side"] != r["side"]:
            continue
        s = 1 if r["side"] in ("home", "over") else -1
        move = (r["p_mkt"] - r0["p_mkt"]) if r["market"] == "ml" else s * (r["line"] - r0["line"])
        thr = CONF_MOVE[r["market"]]
        tag = "D+conf" if move >= thr else ("D+fade" if move <= -thr else None)
        if tag:
            out.append(dict(r, entry=tag))
    return out


def cell(rows):
    n = len(rows)
    prof = np.array([r["profit"] for r in rows], float)
    nb = [r for r in rows if r["res"] != "P"]
    wins = sum(1 for r in nb if r["res"] == "W")
    clv = np.array([r["clv"] for r in rows if r["clv"] is not None], float)
    out = dict(n=n, win=(wins / len(nb) if nb else float("nan")), roi=float("nan"), lo=float("nan"), hi=float("nan"),
               p=float("nan"), clv=(float(clv.mean()) if len(clv) else float("nan")), n_clv=len(clv))
    if n >= 2 and prof.std(ddof=1) > 0:
        se = prof.std(ddof=1) / np.sqrt(n)
        t = prof.mean() / se
        tc = stats.t.ppf(0.975, n - 1)
        out.update(roi=float(prof.mean()), lo=float(prof.mean() - tc * se), hi=float(prof.mean() + tc * se),
                   p=float(stats.t.sf(t, n - 1)))
    elif n:
        out["roi"] = float(prof.mean())
    return out


def bh(pvals, q=0.10):
    """Benjamini-Hochberg: devuelve conjunto de indices significativos."""
    idx = [i for i, p in enumerate(pvals) if p == p]
    idx.sort(key=lambda i: pvals[i])
    m, k = len(idx), 0
    for rank, i in enumerate(idx, 1):
        if pvals[i] <= q * rank / m:
            k = rank
    return set(idx[:k])


def _fmt(c):
    if c["n"] == 0:
        return "–"
    roi = f"{c['roi']*100:+.0f}%" if c["roi"] == c["roi"] else "n/a"
    return f"{c['n']} · {roi}" + ("" if c["n"] >= MIN_N else "*")


def render(con):
    rows = _rows(con)
    L = ["# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)", ""]
    if not rows:
        L.append("_Aun no hay partidos liquidados con entradas registradas._")
        return "\n".join(L)
    rows = rows + derived_entries(rows)
    n_games = len({r["event_id"] for r in rows})
    L += [f"Partidos liquidados con evaluacion: **{n_games}** · version {paper.PAPER_VERSION} · unidad fija 1u por apuesta · "
          "`*` = menos de %d apuestas (no interpretable)." % MIN_N, "",
          "Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. "
          "Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.", ""]
    entries = ["E", "H6", "D", "L", "D+conf", "D+fade"]
    pvals, keys = [], []
    tables = []
    for market, models in (("spread", ("A", "B")), ("ml", ("A", "B")), ("total", ("T",))):
        for model in models:
            t = [f"### {market.upper()} · modelo {model}", "", "| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |",
                 "|---|---|---|---|---|---|---|"]
            for en in entries:
                sub = [r for r in rows if r["market"] == market and r["model"] == model and r["entry"] == en]
                if not sub:
                    continue
                cells = []
                for li, thr in enumerate(paper.LEVELS[market], 1):
                    c = cell([r for r in sub if r["abs_edge"] >= thr])
                    cells.append(_fmt(c))
                    if c["n"] >= MIN_N:
                        keys.append((market, model, en, li, c)); pvals.append(c["p"])
                nb = cell([r for r in sub if r["abs_edge"] < paper.LEVELS[market][-1]])
                t.append(f"| {en} | " + " | ".join(cells) + f" | {_fmt(nb)} |")
            tables.append("\n".join(t) + "\n")
    L += tables
    sig = bh(pvals)
    L += ["## Celdas que sobreviven a la correccion por multiples comparaciones", ""]
    if not keys:
        L.append(f"Ninguna celda tiene aun {MIN_N}+ apuestas.")
    else:
        L.append(f"Celdas evaluables: {len(keys)}. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).")
        if not sig:
            L.append("\n**Ninguna.** Las celdas positivas son compatibles con ruido.")
        for i in sorted(sig, key=lambda i: pvals[i]):
            m, mo, en, li, c = keys[i]
            L.append(f"- {m} {mo} {en} L{li}: n={c['n']} ROI {c['roi']*100:+.1f}% IC95 [{c['lo']*100:+.1f}%, {c['hi']*100:+.1f}%] CLV {c['clv']:+.3f}")
    # CLV por entrada (todas las apuestas con borde >= L3)
    L += ["", "## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)", "",
          "| Mercado · modelo | " + " | ".join(entries) + " |", "|---|" + "---|" * len(entries)]
    for market, models in (("spread", ("A", "B")), ("ml", ("A", "B")), ("total", ("T",))):
        for model in models:
            cs = []
            for en in entries:
                sub = [r for r in rows if r["market"] == market and r["model"] == model and r["entry"] == en
                       and r["abs_edge"] >= paper.LEVELS[market][2] and r["clv"] is not None]
                cs.append(f"{np.mean([r['clv'] for r in sub]):+.3f} (n={len(sub)})" if sub else "–")
            L.append(f"| {market} · {model} | " + " | ".join(cs) + " |")
    # Eficiencia del mercado
    L += ["", "## Eficiencia del mercado (todos los partidos, sin umbral)", "",
          "Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. "
          "En moneyline: Brier del modelo vs el del mercado (menor = mejor).", "",
          "| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |", "|---|---|---|---|---|---|"]
    for market, models in (("spread", ("A", "B")), ("ml", ("A", "B")), ("total", ("T",))):
        for model in models:
            for en in ("E", "D"):
                sub = [r for r in rows if r["market"] == market and r["model"] == model and r["entry"] == en]
                if len(sub) < 10:
                    continue
                if market == "ml":
                    pm = np.array([r["p_model"] if r["side"] == "home" else 1 - r["p_model"] for r in sub])
                    pk = np.array([r["p_mkt"] if r["side"] == "home" else 1 - r["p_mkt"] for r in sub])
                    y = np.array([1.0 if r["home_score"] > r["away_score"] else 0.0 for r in sub])
                    d = (pm - y) ** 2 - (pk - y) ** 2
                    t = d.mean() / (d.std(ddof=1) / np.sqrt(len(d))) if d.std(ddof=1) > 0 else float("nan")
                    L.append(f"| {market} · {model} · {en} | {len(sub)} | – | {np.mean((pm-y)**2):.4f} | {np.mean((pk-y)**2):.4f} | {d.mean():+.4f} ({t:.2f}) |")
                else:
                    x = np.array([r["edge"] for r in sub])
                    if market == "spread":
                        y = np.array([r["home_score"] - r["away_score"] - r["line"] for r in sub])
                    else:
                        y = np.array([r["home_score"] + r["away_score"] - r["line"] for r in sub])
                    xc = x - x.mean()
                    b = (xc * (y - y.mean())).sum() / (xc ** 2).sum() if (xc ** 2).sum() > 0 else float("nan")
                    res = y - y.mean() - b * xc
                    se = np.sqrt(res.var(ddof=2) / (xc ** 2).sum()) if (xc ** 2).sum() > 0 else float("nan")
                    L.append(f"| {market} · {model} · {en} | {len(sub)} | {b:+.3f} ({b/se:.2f}) | – | – | – |")
    L += ["", "_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._"]
    return "\n".join(L)
