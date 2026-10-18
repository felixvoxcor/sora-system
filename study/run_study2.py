import sys, time, pickle, numpy as np, pandas as pd
from scipy.stats import norm
from features import load
import signals2 as sg, engine2 as en

n_perm = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
df = load(); S = sg.build_all(df)
t0 = time.time()
res, st, null = en.run(df, S, n_perm=n_perm)
res["p_gan"] = 1 - norm.cdf(res.t_dia)            # H0: ROI <= 0, con t agrupado por dia
crit = max(null["perm"]["crit_t95"], null["shift"]["crit_t95"])
pw = {r: en.plant_power(df, r, crit, n_sim=150) for r in (0.02, 0.05)}
res.to_csv("cells_v2.csv", index=False)
pickle.dump(dict(null={k: v for k, v in null.items() if k != "tmat_shift"}, crit=crit, power=pw), open("v2_meta.pkl", "wb"))
print("listo", round(time.time() - t0), "s; crit_t95 =", crit)

# ------------------------------------------------------------------ informe
fam = res[res.family]
v1 = pd.read_csv("cells.csv")
L, w = [], None
w = L.append
w("# Estudio v2 (sin fuga de informacion): resultados\n")
w(f"Evaluacion fuera de muestra 2024-25 y 2025-26 ({int((df.season>=en.OOS_FROM).sum())} partidos; calentamiento 2023-24). "
  f"Senales actualizadas **por dia de calendario**; nula = barajar el residuo respecto a la MISMA linea que usa cada estrategia; "
  f"dos esquemas (permutacion iid y desplazamiento circular en el tiempo), {n_perm:,} repeticiones cada uno, se usa el p mas conservador; "
  f"t con errores estandar agrupados por dia. Celdas reales: {len(fam)} (11 estrategias x 5 niveles; ST_ABS y ST_PLAYER salen por cuarentena).\n")
nf = int((fam.p_fwer < .05).sum()); ng = int((fam.p_gan < .05).sum()); nb = int(((fam.p_fwer < .05) & (fam.p_gan < .05)).sum())
w(f"## Resumen\n\n- Celdas con evidencia familiar (p_familia < 0.05): **{nf}** de {len(fam)}. Con ROI > 0 significativo (p_gan < 0.05): **{ng}**. Ambas: **{nb}**.\n")
w("- Varias conclusiones del estudio v1 cambian: ver seccion 4 (fuga) y seccion 5 (nula).\n")
w("## 1. Validacion del motor y potencia\n")
w("| Control | Nivel 1: n | Win% | ROI | t |\n|---|---|---|---|---|")
for nm in ("CTRL_HOME", "CTRL_RANDOM", "PLANT2", "PLANT5"):
    r = res[(res.strategy == nm) & (res.level == 1)].iloc[0]
    w(f"| {nm} | {int(r.n)} | {r.win*100:.1f}% | {r.roi*100:+.1f}% | {r.t:.2f} |")
w(f"\n**Potencia**: se siembra una ventaja REAL (PLANT) y se mide con que frecuencia el motor la detecta, exigiendo el t critico familiar "
  f"(max-t al 95% de la nula = {crit:.2f}); 150 plantas independientes por fila.\n")
w("| Ventaja sembrada | Nivel | t medio | Detectada (familia) | Detectada (celda sola) |\n|---|---|---|---|---|")
for roi_, d in pw.items():
    for lv, x in d.items():
        w(f"| +{roi_*100:.0f}% ROI | {lv} {en.LEVELS[lv][1]} | {x['t_mean']:.2f} | {x['power_family']*100:.0f}% | {x['power_single']*100:.0f}% |")
w("\nLectura: con ~2.600 partidos este estudio **no puede** detectar de forma fiable una ventaja de +2% (potencia familiar 8-51%). "
  "Solo ventajas de ~+5% se ven casi siempre. Un resultado nulo aqui no descarta edges pequenos.\n")
w("## 2. Ranking de celdas reales (por p_familia, luego t)\n")
w("p_azar = mejor que apostar al azar pagando el vig (habilidad). p_familia = corrige por las 60 celdas (min-p). p_gan = ROI > 0 (t agrupado por dia). p_binom = binomial exacta contra 52,38%.\n")
w("| # | Estrategia | Nivel | n | Win% | ROI | t | t por dia | p_binom | p_azar | p_familia | q_BH | p_gan | ROI 2024 | ROI 2025 |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for i, (_, r) in enumerate(fam.sort_values(["p_fwer", "t"], ascending=[True, False]).head(15).iterrows(), 1):
    w(f"| {i} | {r.strategy} | {int(r.level)} {r.level_name} | {int(r.n)} | {r.win*100:.1f}% | {r.roi*100:+.1f}% | {r.t:.2f} | {r.t_dia:.2f} | "
      f"{r.p_binom:.3f} | {r.p_raw:.4f} | {r.p_fwer:.3f} | {r.q_bh:.3f} | {r.p_gan:.3f} | {r.roi_2024*100:+.1f}% | {r.roi_2025*100:+.1f}% |")
w("\n## 3. Matriz ROI por estrategia x nivel (%)\n")
piv = fam.pivot(index="strategy", columns="level", values="roi") * 100
w("| Estrategia | " + " | ".join(f"N{k} {en.LEVELS[k][1]}" for k in range(1, 6)) + " |\n|---|---|---|---|---|---|")
for nm in piv.index:
    w(f"| {nm} | " + " | ".join(f"{piv.loc[nm, k]:+.1f}" for k in range(1, 6)) + " |")
w("\n## 4. Prueba de fuga (R1): version limpia vs version con jugadores del propio partido\n")
w("Si la fuga explicara el rendimiento, la version contaminada (LEAK_) deberia rendir claramente MAS que la limpia.\n")
w("| Par | Nivel | ROI limpia | t limpia | ROI contaminada | t contaminada |\n|---|---|---|---|---|---|")
for a, b in (("ST_ENS_OPEN", "LEAK_ENS_OPEN"), ("ST_ENS", "LEAK_ENS")):
    for lv in range(1, 6):
        x = res[(res.strategy == a) & (res.level == lv)].iloc[0]; y = res[(res.strategy == b) & (res.level == lv)].iloc[0]
        w(f"| {a} vs {b} | {lv} | {x.roi*100:+.1f}% | {x.t:.2f} | {y.roi*100:+.1f}% | {y.t:.2f} |")
w("\n## 5. Cambio de la hipotesis nula (v1 vs v2)\n")
if v1 is not None:
    w("| Celda | p_familia v1 | p_familia v2 |\n|---|---|---|")
    for nm, lv in (("ST_ENS_OPEN", 5), ("ST_ENS_OPEN", 3), ("TT_ENS", 5), ("TT_MODEL", 5), ("STEAM_FOLLOW", 3)):
        a = v1[(v1.strategy == nm) & (v1.level == lv)]; b = res[(res.strategy == nm) & (res.level == lv)]
        if len(a) and len(b):
            w(f"| {nm} N{lv} | {a.iloc[0].p_fwer:.3f} | {b.iloc[0].p_fwer:.3f} |")
w("\nEn v1 las celdas de apertura se comparaban con una nula construida sobre el cierre; los p_familia de esas celdas no eran validos.\n")
w("## 6. Oportunidades no apostadas (mejores celdas por t)\n")
w("| Estrategia | Nivel | No apostados | Win% omitidos | ROI omitidos | Neto (u) |\n|---|---|---|---|---|---|")
for _, r in fam.sort_values("t", ascending=False).head(6).iterrows():
    if r.get("skip_n", 0) == r.get("skip_n", 0) and r.get("skip_n", 0) > 0:
        w(f"| {r.strategy} | {int(r.level)} {r.level_name} | {int(r.skip_n)} | {r.skip_win*100:.1f}% | {r.skip_roi*100:+.1f}% | {r.skip_net:+.0f} |")
w("\n## 7. Limitaciones\n")
w("- ESPN no da apertura con hora ni libro verificable: ninguna celda *_OPEN* demuestra que el precio fuera apostable.\n"
  "- Precio -110 plano en spread/total. Solo 2 temporadas de evaluacion. 60 celdas con libertad de diseno previa.\n"
  "- 'Ruina' = caer por debajo de 25 (perdida de 75%), no ruina literal.\n"
  "- Las senales de jugadores del propio partido siguen en cuarentena (solo controles LEAK_).\n")
open("REPORT_STUDY_V2.md", "w", encoding="utf-8").write("\n".join(L))
print("informe escrito")
