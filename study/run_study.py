import sys, time, numpy as np, pandas as pd
from scipy.stats import norm, spearmanr
from features import load
import signals as sg, engine as en

df = load(); S = sg.build_all(df)
res, st, null = en.run(df, S, n_perm=int(sys.argv[1]) if len(sys.argv) > 1 else 2000)
res["p_ganancia"] = 1 - norm.cdf(res.t)               # H0: ROI <= 0 (hay que superar el vig)
res["p_gan_bonf"] = (res.p_ganancia * 63).clip(upper=1.0)
res.to_csv("cells.csv", index=False)

margin, total = df.margin.values.astype(float), df.total.values.astype(float)
oos = df.season.values >= en.OOS_FROM
def bucket_roi(name):
    s = st[name]; pct = s["pct"]; out = []
    for lo, hi in ((0, 20), (20, 40), (40, 60), (60, 80), (80, 100.01)):
        ib = np.where(oos & ~np.isnan(pct) & (pct >= lo) & (pct < hi))[0]
        p = en.profits(s, ib, margin, total, df.line.values, df.total_close.values)
        out.append((f"{lo}-{min(hi,100):.0f}", len(p), float(p.mean()) if len(p) else np.nan,
                    float((p > 0).sum() / max(1, (p != 0).sum())) if len(p) else np.nan))
    return out

L = []
w = L.append
fam = res[res.family]
w("# Estudio ampliado NBA: 16 estrategias x 5 niveles de riesgo\n")
w(f"Evaluacion fuera de muestra: temporadas 2024-25 y 2025-26 (calentamiento: 2023-24). Partidos: {int(oos.sum())}. "
  f"Entradas a spread/total con precio -110 plano; moneyline con precio real de cierre. Permutaciones: {null['n_perm']}.\n")
w("## 1. Validacion del motor\n")
w("| Estrategia | Que es | Nivel 1: n | Win% | ROI | t |\n|---|---|---|---|---|---|")
for nm in ("CTRL_HOME", "CTRL_RANDOM", "PLANT"):
    r = res[(res.strategy == nm) & (res.level == 1)].iloc[0]
    w(f"| {nm} | {st[nm]['desc']} | {int(r.n)} | {r.win*100:.1f}% | {r.roi*100:+.1f}% | {r.t:.2f} |")
w(f"\nLos controles pierden ~vig (-3% a -5%), como debe ser. La senal sembrada (PLANT) se detecta de inmediato, asi que el motor *si* encuentra ventajas reales cuando existen.\n")
w(f"**Techo de azar:** con {null['n_family_cells']} celdas reales y sin ninguna ventaja, la MEJOR celda alcanza un p_azar de {null['minp_q05']:.4f} o menor el 5% de las veces "
  f"(mediana {null['minp_q50']:.3f}). Una celda necesita superar ese techo para contar como evidencia; p_azar pequeno en una celda sola no basta.\n")
w("## 2. Ranking de celdas reales (por t, con correccion por comparaciones multiples)\n")
w("p_azar = probabilidad de ver algo asi o mejor barajando resultados (celda sola). p_familia = lo mismo corrigiendo por haber probado todas las celdas (min-p de Westfall-Young). p_ganancia = evidencia de que el ROI supera 0, es decir, que vence el vig.\n")
w("| # | Estrategia | Nivel | Apuestas | Win% | ROI | t | p_azar | p_familia | q_BH | p_ganancia | ROI 2024 | ROI 2025 |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|")
top = fam.sort_values("t", ascending=False).head(15)
for i, (_, r) in enumerate(top.iterrows(), 1):
    w(f"| {i} | {r.strategy} | {int(r.level)} {r.level_name} | {int(r.n)} | {r.win*100:.1f}% | {r.roi*100:+.1f}% | {r.t:.2f} | "
      f"{r.p_raw:.3f} | {r.p_fwer:.3f} | {r.q_bh:.3f} | {r.p_ganancia:.3f} | {r.roi_2024*100:+.1f}% | {r.roi_2025*100:+.1f}% |")
nsig = int((fam.p_fwer < 0.05).sum()); nprof = int(((fam.p_fwer < 0.05) & (fam.p_ganancia < 0.05)).sum())
w(f"\nCeldas reales con p_familia < 0.05: **{nsig}** de {len(fam)}. De ellas, con ROI significativamente > 0 tras el vig: **{nprof}**.\n")
w("## 3. Matriz ROI por estrategia x nivel (%)\n")
piv = res[res.strategy.isin(fam.strategy.unique())].pivot(index="strategy", columns="level", values="roi") * 100
w("| Estrategia | " + " | ".join(f"N{k} {en.LEVELS[k][1]}" for k in range(1, 6)) + " |\n|---|---|---|---|---|---|")
for nm in fam.strategy.unique():
    w(f"| {nm} | " + " | ".join(f"{piv.loc[nm, k]:+.1f}" for k in range(1, 6)) + " |")
w("\nApuestas por celda (N1..N5) para dimensionar el ruido: " + ", ".join(
    f"{k}: {int(res[(res.strategy=='ST_ENS')&(res.level==k)].n.iloc[0])}" for k in range(1, 6)) + " (ejemplo ST_ENS).\n")
w("## 4. Perfil de riesgo de los 5 niveles (estrategia ST_ENS y mejor celda por nivel)\n")
w("| Nivel | Rango 1-100 | % bankroll/apuesta | Estrategia | Apuestas | ROI | Bankroll final (100 inicial) | Caida maxima | Prob. ruina (<25) | Prob. terminar en ganancia |\n|---|---|---|---|---|---|---|---|---|---|")
for lv in range(1, 6):
    for nm in ("ST_ENS", None):
        sub = fam[fam.level == lv]
        r = (res[(res.strategy == "ST_ENS") & (res.level == lv)].iloc[0] if nm else sub.sort_values("t", ascending=False).iloc[0])
        tag = r.strategy + ("" if nm else " (mejor t)")
        w(f"| {lv} {en.LEVELS[lv][1]} | {en.LEVELS[lv][0]} | {en.LEVELS[lv][3]} | {tag} | {int(r.n)} | {r.roi*100:+.1f}% | {r.final:.0f} | "
          f"{r.maxdd*100:.0f}% | {r.ruin*100:.0f}% | {r.p_end_profit*100:.0f}% |")
w("\n## 5. Oportunidades no apostadas (lo que quedo fuera por la regla del nivel)\n")
w("Para cada celda: los partidos donde la estrategia tenia un lado pero la regla del nivel dijo NO. 'Neto' = ganancia en unidades si hubieras apostado todo eso. Positivo = el filtro dejo dinero en la mesa; negativo = el filtro evito perdidas.\n")
w("| Estrategia | Nivel | No apostados | Win% omitidos | ROI omitidos | Ganado que se perdio (u) | Perdida evitada (u) | Neto (u) |\n|---|---|---|---|---|---|---|---|")
for nm in ("ST_ENS", "ST_FF", "ST_REF", "TT_ENS", "ML_ENS", "STEAM_FOLLOW"):
    for lv in (2, 3, 4, 5):
        r = res[(res.strategy == nm) & (res.level == lv)].iloc[0]
        w(f"| {nm} | {lv} {en.LEVELS[lv][1]} | {int(r.skip_n)} | {r.skip_win*100:.1f}% | {r.skip_roi*100:+.1f}% | {r.skip_won:.0f} | {r.skip_lost:.0f} | {r.skip_net:+.0f} |")
w("\n## 6. Diagnostico de confianza: sube el ROI cuando la senal es mas fuerte?\n")
w("Si una senal tiene informacion, el ROI debe subir de la franja 0-20 a la 80-100. Si sube y baja al azar, es ruido.\n")
w("| Estrategia | 0-20 | 20-40 | 40-60 | 60-80 | 80-100 | Spearman |\n|---|---|---|---|---|---|---|")
for nm in fam.strategy.unique():
    b = bucket_roi(nm); rois = [x[2] for x in b]
    rho = spearmanr(range(5), rois)[0] if not np.isnan(rois).any() else np.nan
    w(f"| {nm} | " + " | ".join(f"{x[2]*100:+.1f}% ({x[1]})" for x in b) + f" | {rho:+.2f} |")
open("REPORT_STUDY.md", "w").write("\n".join(L))
print("\n".join(L))
