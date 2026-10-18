# Estudio v2 (sin fuga de informacion): resultados

Evaluacion fuera de muestra 2024-25 y 2025-26 (2637 partidos; calentamiento 2023-24). Senales actualizadas **por dia de calendario**; nula = barajar el residuo respecto a la MISMA linea que usa cada estrategia; dos esquemas (permutacion iid y desplazamiento circular en el tiempo), 10,000 repeticiones cada uno, se usa el p mas conservador; t con errores estandar agrupados por dia. Celdas reales: 60 (11 estrategias x 5 niveles; ST_ABS y ST_PLAYER salen por cuarentena).

## Resumen

- Celdas con evidencia familiar (p_familia < 0.05): **0** de 60. Con ROI > 0 significativo (p_gan < 0.05): **1**. Ambas: **0**.

- Varias conclusiones del estudio v1 cambian: ver seccion 4 (fuga) y seccion 5 (nula).

## 1. Validacion del motor y potencia

| Control | Nivel 1: n | Win% | ROI | t |
|---|---|---|---|---|
| CTRL_HOME | 2637 | 50.8% | -3.1% | -1.65 |
| CTRL_RANDOM | 2637 | 50.7% | -3.1% | -1.69 |
| PLANT2 | 2637 | 53.2% | +1.6% | 0.85 |
| PLANT5 | 2637 | 55.9% | +6.8% | 3.68 |

**Potencia**: se siembra una ventaja REAL (PLANT) y se mide con que frecuencia el motor la detecta, exigiendo el t critico familiar (max-t al 95% de la nula = 2.51); 150 plantas independientes por fila.

| Ventaja sembrada | Nivel | t medio | Detectada (familia) | Detectada (celda sola) |
|---|---|---|---|---|
| +2% ROI | 1 Temerario | 1.16 | 8% | 29% |
| +2% ROI | 2 Agresivo | 2.21 | 33% | 75% |
| +2% ROI | 3 Equilibrado | 2.49 | 45% | 80% |
| +2% ROI | 4 Prudente | 2.46 | 51% | 80% |
| +2% ROI | 5 Conservador | 1.78 | 21% | 56% |
| +5% ROI | 1 Temerario | 2.76 | 55% | 87% |
| +5% ROI | 2 Agresivo | 4.12 | 96% | 99% |
| +5% ROI | 3 Equilibrado | 4.36 | 97% | 100% |
| +5% ROI | 4 Prudente | 4.16 | 93% | 98% |
| +5% ROI | 5 Conservador | 2.99 | 73% | 93% |

Lectura: con ~2.600 partidos este estudio **no puede** detectar de forma fiable una ventaja de +2% (potencia familiar 8-51%). Solo ventajas de ~+5% se ven casi siempre. Un resultado nulo aqui no descarta edges pequenos.

## 2. Ranking de celdas reales (por p_familia, luego t)

p_azar = mejor que apostar al azar pagando el vig (habilidad). p_familia = corrige por las 60 celdas (min-p). p_gan = ROI > 0 (t agrupado por dia). p_binom = binomial exacta contra 52,38%.

| # | Estrategia | Nivel | n | Win% | ROI | t | t por dia | p_binom | p_azar | p_familia | q_BH | p_gan | ROI 2024 | ROI 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | STEAM_FOLLOW | 3 Equilibrado | 865 | 54.7% | +4.4% | 1.36 | 1.26 | 0.093 | 0.0042 | 0.156 | 0.138 | 0.105 | +2.9% | +5.7% |
| 2 | ST_ENS_OPEN | 3 Equilibrado | 1091 | 53.9% | +2.9% | 1.00 | 1.00 | 0.166 | 0.0069 | 0.235 | 0.138 | 0.159 | +7.1% | -1.5% |
| 3 | ST_ENS_OPEN | 2 Agresivo | 1612 | 53.2% | +1.5% | 0.63 | 0.64 | 0.273 | 0.0069 | 0.235 | 0.138 | 0.261 | +4.0% | -1.1% |
| 4 | ST_ENS_OPEN | 5 Conservador | 145 | 60.0% | +14.5% | 1.87 | 2.01 | 0.039 | 0.0092 | 0.301 | 0.138 | 0.022 | +29.5% | -6.1% |
| 5 | ST_ENS_OPEN | 1 Temerario | 2637 | 52.1% | -0.5% | -0.24 | -0.25 | 0.604 | 0.0138 | 0.406 | 0.166 | 0.599 | -1.4% | +0.5% |
| 6 | STEAM_FOLLOW | 2 Agresivo | 1019 | 53.3% | +1.7% | 0.58 | 0.54 | 0.292 | 0.0198 | 0.500 | 0.166 | 0.293 | -1.6% | +5.7% |
| 7 | STEAM_FOLLOW | 4 Prudente | 421 | 55.1% | +5.2% | 1.12 | 1.09 | 0.142 | 0.0207 | 0.526 | 0.166 | 0.138 | +6.5% | +4.1% |
| 8 | TT_MODEL | 5 Conservador | 159 | 57.9% | +10.5% | 1.40 | 1.42 | 0.096 | 0.0222 | 0.552 | 0.166 | 0.079 | +12.4% | +7.9% |
| 9 | STEAM_FOLLOW | 1 Temerario | 2012 | 52.2% | -0.4% | -0.17 | -0.17 | 0.578 | 0.0274 | 0.603 | 0.169 | 0.569 | -1.2% | +0.4% |
| 10 | TT_MODEL | 4 Prudente | 548 | 53.8% | +2.8% | 0.68 | 0.65 | 0.262 | 0.0282 | 0.635 | 0.169 | 0.258 | +0.4% | +5.4% |
| 11 | TT_ENS | 5 Conservador | 150 | 58.0% | +10.7% | 1.39 | 1.35 | 0.097 | 0.0324 | 0.660 | 0.177 | 0.089 | +14.5% | +7.4% |
| 12 | TT_ENS | 3 Equilibrado | 1068 | 52.7% | +0.6% | 0.22 | 0.21 | 0.426 | 0.0508 | 0.811 | 0.240 | 0.416 | -0.3% | +1.5% |
| 13 | ST_ENS_OPEN | 4 Prudente | 561 | 53.5% | +2.1% | 0.52 | 0.51 | 0.317 | 0.0520 | 0.825 | 0.240 | 0.305 | +7.1% | -3.5% |
| 14 | TT_REF | 5 Conservador | 145 | 57.2% | +9.3% | 1.18 | 1.17 | 0.138 | 0.0560 | 0.843 | 0.240 | 0.121 | -3.2% | +21.3% |
| 15 | TT_ENS | 4 Prudente | 549 | 53.6% | +2.2% | 0.55 | 0.53 | 0.306 | 0.0647 | 0.874 | 0.259 | 0.296 | -1.4% | +5.9% |

## 3. Matriz ROI por estrategia x nivel (%)

| Estrategia | N1 Temerario | N2 Agresivo | N3 Equilibrado | N4 Prudente | N5 Conservador |
|---|---|---|---|---|---|
| ML_ENS | -6.1 | -6.5 | -3.7 | -6.0 | -8.2 |
| STEAM_FADE | -8.7 | -10.8 | -13.5 | -14.3 | -3.7 |
| STEAM_FOLLOW | -0.4 | +1.7 | +4.4 | +5.2 | -5.4 |
| ST_ENS | -5.8 | -5.5 | -5.2 | -2.8 | +7.5 |
| ST_ENS_OPEN | -0.5 | +1.5 | +2.9 | +2.1 | +14.5 |
| ST_FF | -3.1 | -2.8 | -3.8 | -2.0 | -1.1 |
| ST_RATING | -4.7 | -4.3 | -4.1 | -0.2 | -1.8 |
| ST_REF | -4.2 | -4.5 | -3.9 | -1.3 | -16.6 |
| ST_REST | -4.9 | -4.4 | -2.8 | -2.5 | +7.7 |
| TT_ENS | -3.4 | -2.2 | +0.6 | +2.2 | +10.7 |
| TT_MODEL | -4.7 | -3.4 | -1.3 | +2.8 | +10.5 |
| TT_REF | -2.8 | -0.4 | -2.0 | -1.3 | +9.3 |

## 4. Prueba de fuga (R1): version limpia vs version con jugadores del propio partido

Si la fuga explicara el rendimiento, la version contaminada (LEAK_) deberia rendir claramente MAS que la limpia.

| Par | Nivel | ROI limpia | t limpia | ROI contaminada | t contaminada |
|---|---|---|---|---|---|
| ST_ENS_OPEN vs LEAK_ENS_OPEN | 1 | -0.5% | -0.24 | -0.6% | -0.32 |
| ST_ENS_OPEN vs LEAK_ENS_OPEN | 2 | +1.5% | 0.63 | -1.3% | -0.53 |
| ST_ENS_OPEN vs LEAK_ENS_OPEN | 3 | +2.9% | 1.00 | +1.3% | 0.45 |
| ST_ENS_OPEN vs LEAK_ENS_OPEN | 4 | +2.1% | 0.52 | +6.5% | 1.55 |
| ST_ENS_OPEN vs LEAK_ENS_OPEN | 5 | +14.5% | 1.87 | +16.3% | 2.01 |
| ST_ENS vs LEAK_ENS | 1 | -5.8% | -3.13 | -7.6% | -4.10 |
| ST_ENS vs LEAK_ENS | 2 | -5.5% | -2.28 | -6.3% | -2.59 |
| ST_ENS vs LEAK_ENS | 3 | -5.2% | -1.74 | -4.6% | -1.56 |
| ST_ENS vs LEAK_ENS | 4 | -2.8% | -0.64 | +0.3% | 0.08 |
| ST_ENS vs LEAK_ENS | 5 | +7.5% | 0.86 | -0.1% | -0.01 |

## 5. Cambio de la hipotesis nula (v1 vs v2)

| Celda | p_familia v1 | p_familia v2 |
|---|---|---|
| ST_ENS_OPEN N5 | 1.000 | 0.301 |
| ST_ENS_OPEN N3 | 1.000 | 0.235 |
| TT_ENS N5 | 0.621 | 0.660 |
| TT_MODEL N5 | 0.640 | 0.552 |
| STEAM_FOLLOW N3 | 0.183 | 0.156 |

En v1 las celdas de apertura se comparaban con una nula construida sobre el cierre; los p_familia de esas celdas no eran validos.

## 6. Oportunidades no apostadas (mejores celdas por t)

| Estrategia | Nivel | No apostados | Win% omitidos | ROI omitidos | Neto (u) |
|---|---|---|---|---|---|
| ST_ENS_OPEN | 5 Conservador | 2492 | 51.7% | -1.3% | -33 |
| TT_MODEL | 5 Conservador | 2478 | 49.4% | -5.6% | -139 |
| TT_ENS | 5 Conservador | 2487 | 50.2% | -4.2% | -104 |
| STEAM_FOLLOW | 3 Equilibrado | 1147 | 50.3% | -4.0% | -45 |
| TT_REF | 5 Conservador | 2492 | 50.5% | -3.5% | -88 |
| STEAM_FOLLOW | 4 Prudente | 1591 | 51.4% | -1.8% | -29 |

## 7. Limitaciones

- ESPN no da apertura con hora ni libro verificable: ninguna celda *_OPEN* demuestra que el precio fuera apostable.
- Precio -110 plano en spread/total. Solo 2 temporadas de evaluacion. 60 celdas con libertad de diseno previa.
- 'Ruina' = caer por debajo de 25 (perdida de 75%), no ruina literal.
- Las senales de jugadores del propio partido siguen en cuarentena (solo controles LEAK_).
