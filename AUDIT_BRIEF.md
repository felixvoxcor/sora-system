# NBA CLV Lab / Estudio "Moneyball 5.0" — Dossier para auditoría y premortem

**Propósito de este documento:** que un auditor independiente (otra IA o una persona) intente romper este sistema. No se pide validación: se pide encontrar fallos, fugas de información, sesgos estadísticos, errores de ingeniería y supuestos falsos. Todo lo que sigue es declarativo; el auditor no necesita confiar en nada, pero debe saber qué se afirma y qué NO se afirma.

Repositorio: `felixvoxcor/sora-system` (rama `main` = rastreador en vivo; rama `nba-study` / PR #2 = estudio amplio).
Fecha del dossier: 2026-10-17. Dueño: Felix (economista, no programador; ejecuta con IA). Objetivo declarado: encontrar, si existe, una ventaja apostadora real en la NBA; si no existe, saberlo barato y rápido.

---

## 1. Qué afirmamos y qué no

- **NO afirmamos** que exista ventaja. A la fecha, **ninguna celda del estudio pasa corrección por comparaciones múltiples** (0 de 70, Westfall-Young min-p < 0,05) y ninguna supera el vig de forma significativa.
- **Afirmamos** que el *marco de medición* es honesto en lo básico: walk-forward, controles negativos que pierden ≈ el vig, una señal sembrada (PLANT) que sí se detecta, y un criterio de falsificación escrito antes de ver datos en vivo.
- La prior es **baja**: la línea de cierre de la NBA es muy eficiente. El backtest 2023-26 mostró RMSE del modelo 14,45 vs 13,90 de la línea de cierre (el mercado gana).

## 2. Arquitectura (resumen)

### 2.1 Rastreador en vivo (`main`)
- GitHub Actions, cron horario (`7 * * * *`), corre `pytest` y luego `python -m lab.tracker run`; hace commit de `data/lab.db` y `REPORT.md`.
- SQLite **append-only** (triggers bloquean UPDATE/DELETE en `snapshots`; `UNIQUE(event_id,label)`).
- Etiquetas de captura: **E** (20–26 h antes del tip, exploratoria) y **D** (0,75–3 h antes; única que decide).
- Dos brazos pre-registrados (parámetros congelados v1.0):
  - **A:** ratings de margen online (K=0,05; arrastre entre temporadas 0,5; ventaja local 2,5; tope de margen 25).
  - **B:** A + ajuste por lesiones = `3,0 × P(fuera) × (min_prom/36)²` por jugador (Out=1,0; Day-To-Day=0,25), sin calibrar.
- Métrica: CLV = `lado × (línea_cierre − línea_snapshot)`; apuesta hipotética si `|predicción − línea| ≥ 2`.
- Decisión (`FALSIFICATION.md`): t de una cola, α=0,025 por brazo, **n=300**; futilidad en n=150 si CLV < −0,10; todo lo demás exploratorio; cambios de parámetros ⇒ nueva versión y reinicio.
- Primer partido rastreado: 2026-10-20. **Hoy no hay ni un resultado en vivo.**

### 2.2 Estudio amplio (`nba-study`)
- Datos: 3.948 partidos 2023-24 a 2025-26 con spread/total/moneyline de **apertura y cierre** (ESPN, proveedor ESPN BET/DraftKings) + resúmenes de partido (cajas, árbitros).
- Evaluación fuera de muestra: 2024-25 y 2025-26 (2.637 partidos); calentamiento 2023-24.
- **Señales** (todas walk-forward, actualizando después de usar): ratings de margen; ausencias (minutos esperados²); +/- por jugador encogido; four factors (pesos de Oliver); modelo de totales ofensiva/defensiva; efecto de tríos arbitrales (encogimiento k=40); descanso/back-to-back; movimiento de línea (steam).
- **Combinación:** ridge expansivo walk-forward (λ=300, mín. 300 filas, escala fija con las primeras 500).
- **17 estrategias × 5 niveles de riesgo** (85 celdas: 70 "reales" de 14 estrategias + 15 de control/validación). Nivel = percentil de confianza en ventana móvil de 400 señales: N1 (1-20) apuesta todo con 3 % del bankroll … N5 (81-100) solo percentil ≥ 95 con 0,25 %.
- Precio de spread/total: **−110 plano** (supuesto). Moneyline: precio real de cierre.
- Pruebas: permutación (2.000), Westfall-Young min-p (FWER), Benjamini-Hochberg, bootstrap de ruina, análisis de "oportunidades no apostadas" (lo que el filtro del nivel dejó fuera).

## 3. Resultados actuales (honestos)

| Hallazgo | Valor |
|---|---|
| Controles (siempre local / azar) | ROI −3,1 % / −5,5 % (≈ vig; correcto) |
| PLANT (ventaja sembrada) | ROI +16 %, t = 8,8 (el motor detecta lo real) |
| Mejor celda por t | ST_ENS_OPEN N5: 132 apuestas, ROI +14,3 %, t = 1,74, **p_familia = 1,000** |
| Celdas con p_familia < 0,05 | **0 de 70** |
| Piso de azar | con 70 celdas y cero ventaja, la mejor celda llega a p_azar ≤ 0,0015 el 5 % de las veces |
| Líderes por t | ST_ENS_OPEN, TT_ENS/TT_MODEL (totales), STEAM_FOLLOW N3 (865 apuestas, +4,4 %, t = 1,36) |
| Inestabilidad | ROI 2024 vs 2025 cambia de signo en varias celdas (p. ej. ST_ENS_OPEN N5 +27,3 % → −2,9 %) |

Lectura honesta: ruido consistente con **cero ventaja**, con algunas pistas débiles (totales, steam) que no sobreviven a la corrección.

## 4. Riesgos conocidos y premortem (ordenados por gravedad)

> Premortem: "Es abril de 2027, el sistema perdió dinero real / publicó un falso positivo. ¿Por qué?"

### R1 — FUGA DE INFORMACIÓN en ST_ENS_OPEN (la mejor celda probablemente es artefacto) — **ALTA**
`abs_diff` y `pl_gap` se construyen con **quién jugó realmente** (DNP y minutos del box score del propio partido). Eso se conoce al final del partido, o como mucho minutos antes del tip. La estrategia ST_ENS_OPEN apuesta contra la **línea de apertura** (publicada ~24 h antes), cuando esas ausencias aún no se conocían; el movimiento apertura→cierre refleja precisamente esas noticias. El modelo "adivina" lo que el mercado aprendió después. Para las estrategias al **cierre** la fuga es menor (el mercado ya incorporó la mayoría) pero no nula: descartes tardíos, "DNP – decisión técnica", etc.
**Acción:** no confiar en ninguna celda ST_ENS_OPEN ni en ST_ABS/ST_PLAYER hasta reconstruir esas señales con **información timestamped previa a la línea usada** (reportes oficiales de lesiones; ver §6).

### R2 — Línea de "apertura" de ESPN no es un precio operable — **ALTA**
No tiene hora ni libro verificable; puede ser una cotización nominal no ofrecida a clientes, o ser tardía. El CLV contra "apertura" (+0,48 pts, decayendo +0,81 → +0,16) podría no ser capturable.

### R3 — Mezcla de proveedores / calidad del cierre — **MEDIA**
Prioridad de proveedor 58 → 100 → 38 según disponibilidad; el CLV puede mezclar libros. "Cierre" de ESPN ≠ cierre de Pinnacle (referencia de eficiencia). Sin Pinnacle no se puede afirmar eficiencia vs el mercado más afilado.

### R4 — Precio −110 plano — **MEDIA**
Subestima/sobreestima según libro y momento; el ROI de spread/total en el estudio es indicativo, no operable.

### R5 — Comparaciones múltiples y "garden of forking paths" — **ALTA**
70 celdas reales, muchos grados de libertad (λ, ventanas, percentiles, pesos). Mitigado con min-p y BH, pero las **decisiones de diseño** (qué señales, qué niveles) se tomaron viendo el mismo conjunto 2023-26. No hay holdout verdaderamente virgen salvo el rastreador en vivo.

### R6 — Potencia estadística insuficiente — **ALTA**
Con SD de CLV ~1,5–2 pts, detectar un CLV real de +0,2 con α=0,025 requiere del orden de varios cientos de apuestas **por brazo y por umbral**; n=300 es justo. Muchas celdas (N5) tienen 80–170 apuestas: casi todo su ROI es ruido.

### R7 — Tamaño y ruina — **MEDIA**
Los 5 niveles usan fracción fija sobre el bankroll; la prob. de ruina del nivel 1 con edge ≈ 0 es 57–100 %. Es "coherente con el diseño" pero un usuario podría leerlo como recomendación.

### R8 — Ingeniería — **MEDIA**
- Dependencia de la API pública no documentada de ESPN (puede cambiar o limitar).
- Cron de GitHub Actions: retrasos/omisiones; solo corre desde la rama por defecto.
- `ratings.py` y el estudio duplican lógica (riesgo de divergencia).
- El snapshot D depende de que el cron caiga en la ventana 0,75–3 h; si falla, el partido se pierde (sesgo de selección leve).
- Escala del ridge usa primeras 500 filas (fuga mínima en esas filas).

### R9 — Humano — **ALTA**
Usuario no técnico, con fuerte motivación de "encontrar algo". Riesgo de apostar dinero real ante una celda bonita. Mitigación: sección "Prohibido" en `FALSIFICATION.md`; fase 2 obligatoria antes de dinero real.

### R10 — Seguridad — **BAJA**
Revisión de 4 repos: sin claves expuestas. Quedan credenciales locales (`cdp_api_key.json`, `.env` de SORA) en la máquina del usuario, fuera de los repos; se recomienda rotarlas. Los datos son públicos; no hay claves en el rastreador.

## 5. Preguntas concretas para el auditor

1. ¿Hay otras fugas temporales además de R1? Revisar `study/signals.py` (en especial `player_signals`, `referee_effects`, `wf_ridge`) y `study/engine.py` (percentiles, `cell_metrics`).
2. ¿El procedimiento min-p de Westfall-Young con 2.000 permutaciones **barajando resultados** respeta la dependencia entre celdas (las celdas comparten partidos y señales)? ¿Qué barajado es correcto?
3. ¿El percentil con ventana móvil de 400 introduce sesgo de selección por nivel?
4. ¿El criterio n=300 / α=0,025 / futilidad −0,10 es coherente? ¿Falta corrección por mirar dos umbrales y dos ventanas?
5. ¿CLV positivo contra una línea de ESPN es evidencia de algo si el libro no es afilado? ¿Qué referencia mínima exigirías (Pinnacle, consenso de varios libros)?
6. ¿Qué haría fracasar el rastreador en vivo en la práctica (cron, ventanas, cambios de API)?
7. ¿Qué prueba mínima convencería de que **no** hay ventaja, para dejar de invertir tiempo? (criterio de abandono).
8. ¿Qué pruebas añadirías con datos gratuitos antes de pagar por datos históricos intradía?

## 6. Plan de mejora gratuito (aprobado por el usuario, en curso)

1. **Reportes oficiales de lesiones de la NBA** (PDF con hora; verificado reachable y parseable, desde 2020-21). Lector propio (el paquete público `nba-injury-report` es AGPL: no se copia su código). Sirve para: (a) reconstruir `abs_diff`/`pl_gap` sin fuga con estado pre-línea; (b) probar si el mercado tarda en reaccionar a lesiones (movimiento de línea vs hora de publicación).
2. **Ampliar muestra a 2021-22 y 2022-23** con líneas finales multi-libro de ESPN (sin apertura/cierre diferenciados): útil para estrategias al cierre, **no** para CLV.
3. Reconstruir el estudio con las señales sin fuga, mismas celdas, y comparar contra el estudio actual como **prueba de contaminación**: si ST_ENS_OPEN colapsa, R1 queda confirmado.
4. Decidir, con el veredicto del auditor, qué pistas entran al rastreador en vivo como brazos **pre-registrados** (no más de 3), con n=500.

## 7. Lo que NO está hecho (honestidad)

- No se probó stats.nba.com (inalcanzable desde el entorno de ejecución).
- No hay datos de Pinnacle ni de líneas intradía; The Odds API histórico es de pago y no se compró.
- No hay un solo resultado en vivo.
- Los 12 tests unitarios cubren el rastreador, no el estudio amplio.
