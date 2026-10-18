# Estudio ampliado NBA: 16 estrategias x 5 niveles de riesgo

Evaluacion fuera de muestra: temporadas 2024-25 y 2025-26 (calentamiento: 2023-24). Partidos: 2637. Entradas a spread/total con precio -110 plano; moneyline con precio real de cierre. Permutaciones: 2000.

## 1. Validacion del motor

| Estrategia | Que es | Nivel 1: n | Win% | ROI | t |
|---|---|---|---|---|---|
| CTRL_HOME | CONTROL: siempre local al cierre | 2637 | 50.8% | -3.1% | -1.65 |
| CTRL_RANDOM | CONTROL: lado y confianza al azar | 2637 | 49.5% | -5.5% | -2.93 |
| PLANT | VALIDACION: senal con ventaja real sembrada | 2637 | 60.8% | +16.0% | 8.80 |

Los controles pierden ~vig (-3% a -5%), como debe ser. La senal sembrada (PLANT) se detecta de inmediato, asi que el motor *si* encuentra ventajas reales cuando existen.

**Techo de azar:** con 70 celdas reales y sin ninguna ventaja, la MEJOR celda alcanza un p_azar de 0.0015 o menor el 5% de las veces (mediana 0.017). Una celda necesita superar ese techo para contar como evidencia; p_azar pequeno en una celda sola no basta.

## 2. Ranking de celdas reales (por t, con correccion por comparaciones multiples)

p_azar = probabilidad de ver algo asi o mejor barajando resultados (celda sola). p_familia = lo mismo corrigiendo por haber probado todas las celdas (min-p de Westfall-Young). p_ganancia = evidencia de que el ROI supera 0, es decir, que vence el vig.

| # | Estrategia | Nivel | Apuestas | Win% | ROI | t | p_azar | p_familia | q_BH | p_ganancia | ROI 2024 | ROI 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ST_ENS_OPEN | 5 Conservador | 132 | 59.8% | +14.3% | 1.74 | 0.334 | 1.000 | 0.668 | 0.041 | +27.3% | -2.9% |
| 2 | TT_ENS | 5 Conservador | 157 | 58.6% | +11.9% | 1.58 | 0.024 | 0.621 | 0.236 | 0.057 | +16.5% | +7.4% |
| 3 | STEAM_FOLLOW | 3 Equilibrado | 865 | 54.7% | +4.4% | 1.36 | 0.004 | 0.183 | 0.236 | 0.087 | +2.9% | +5.7% |
| 4 | ST_ENS_OPEN | 4 Prudente | 515 | 55.1% | +5.3% | 1.26 | 0.379 | 1.000 | 0.687 | 0.104 | +9.9% | +0.4% |
| 5 | TT_MODEL | 5 Conservador | 168 | 57.1% | +9.1% | 1.24 | 0.026 | 0.640 | 0.236 | 0.107 | +10.7% | +6.7% |
| 6 | TT_MODEL | 4 Prudente | 547 | 54.8% | +4.7% | 1.16 | 0.009 | 0.338 | 0.236 | 0.124 | +2.5% | +7.2% |
| 7 | STEAM_FOLLOW | 4 Prudente | 421 | 55.1% | +5.2% | 1.12 | 0.020 | 0.549 | 0.236 | 0.131 | +6.5% | +4.1% |
| 8 | TT_ENS | 4 Prudente | 546 | 54.6% | +4.2% | 1.03 | 0.027 | 0.652 | 0.236 | 0.151 | +0.3% | +8.3% |
| 9 | TT_REF | 5 Conservador | 145 | 56.6% | +8.0% | 1.01 | 0.075 | 0.932 | 0.477 | 0.156 | -5.9% | +22.0% |
| 10 | ST_PLAYER | 5 Conservador | 220 | 54.5% | +4.1% | 0.64 | 0.090 | 0.958 | 0.513 | 0.260 | +4.3% | +3.9% |
| 11 | ST_ENS | 5 Conservador | 125 | 55.2% | +5.4% | 0.63 | 0.156 | 0.999 | 0.577 | 0.264 | +21.8% | -8.8% |
| 12 | STEAM_FOLLOW | 2 Agresivo | 1019 | 53.3% | +1.7% | 0.58 | 0.017 | 0.511 | 0.236 | 0.281 | -1.6% | +5.7% |
| 13 | ST_REST | 5 Conservador | 82 | 54.9% | +4.8% | 0.45 | 0.197 | 1.000 | 0.577 | 0.326 | +7.2% | -0.7% |
| 14 | ST_FF | 5 Conservador | 263 | 53.6% | +2.4% | 0.40 | 0.107 | 0.979 | 0.513 | 0.345 | -0.2% | +4.9% |
| 15 | ST_ENS_OPEN | 3 Equilibrado | 1042 | 53.0% | +1.1% | 0.38 | 0.596 | 1.000 | 0.835 | 0.350 | +5.8% | -3.5% |

Celdas reales con p_familia < 0.05: **0** de 70. De ellas, con ROI significativamente > 0 tras el vig: **0**.

## 3. Matriz ROI por estrategia x nivel (%)

| Estrategia | N1 Temerario | N2 Agresivo | N3 Equilibrado | N4 Prudente | N5 Conservador |
|---|---|---|---|---|---|
| ST_RATING | -4.7 | -4.9 | -4.2 | -0.1 | +0.9 |
| ST_ABS | -5.8 | -7.9 | -7.3 | -13.6 | -6.1 |
| ST_PLAYER | -7.0 | -5.3 | -3.2 | +1.1 | +4.1 |
| ST_FF | -2.8 | -1.7 | -2.3 | -1.8 | +2.4 |
| ST_REF | -3.9 | -4.2 | -3.9 | -1.3 | -15.8 |
| ST_REST | -4.8 | -4.2 | -2.6 | -1.8 | +4.8 |
| ST_ENS | -6.6 | -5.8 | -5.6 | -0.7 | +5.4 |
| ST_ENS_OPEN | -0.8 | -2.1 | +1.1 | +5.3 | +14.3 |
| TT_MODEL | -3.7 | -3.8 | -1.9 | +4.7 | +9.1 |
| TT_REF | -2.8 | -0.7 | -1.8 | -1.5 | +8.0 |
| TT_ENS | -3.1 | -2.2 | +0.6 | +4.2 | +11.9 |
| ML_ENS | -6.4 | -6.9 | -5.4 | -7.6 | -10.2 |
| STEAM_FOLLOW | -0.4 | +1.7 | +4.4 | +5.2 | -5.4 |
| STEAM_FADE | -8.7 | -10.8 | -13.5 | -14.3 | -3.7 |

Apuestas por celda (N1..N5) para dimensionar el ruido: 1: 2637, 2: 1559, 3: 1035, 4: 492, 5: 125 (ejemplo ST_ENS).

## 4. Perfil de riesgo de los 5 niveles (estrategia ST_ENS y mejor celda por nivel)

| Nivel | Rango 1-100 | % bankroll/apuesta | Estrategia | Apuestas | ROI | Bankroll final (100 inicial) | Caida maxima | Prob. ruina (<25) | Prob. terminar en ganancia |
|---|---|---|---|---|---|---|---|---|---|
| 1 Temerario | 1-20 | 3.0 | ST_ENS | 2637 | -6.6% | 0 | 100% | 100% | 0% |
| 1 Temerario | 1-20 | 3.0 | STEAM_FOLLOW (mejor t) | 2012 | -0.4% | 35 | 85% | 57% | 19% |
| 2 Agresivo | 21-40 | 2.0 | ST_ENS | 1559 | -5.8% | 12 | 91% | 90% | 0% |
| 2 Agresivo | 21-40 | 2.0 | STEAM_FOLLOW (mejor t) | 1019 | +1.7% | 118 | 50% | 0% | 60% |
| 3 Equilibrado | 41-60 | 1.0 | ST_ENS | 1035 | -5.6% | 54 | 57% | 0% | 2% |
| 3 Equilibrado | 41-60 | 1.0 | STEAM_FOLLOW (mejor t) | 865 | +4.4% | 141 | 15% | 0% | 86% |
| 4 Prudente | 61-80 | 0.5 | ST_ENS | 492 | -0.7% | 98 | 12% | 0% | 40% |
| 4 Prudente | 61-80 | 0.5 | ST_ENS_OPEN (mejor t) | 515 | +5.3% | 114 | 10% | 0% | 88% |
| 5 Conservador | 81-100 | 0.25 | ST_ENS | 125 | +5.4% | 102 | 4% | 0% | 73% |
| 5 Conservador | 81-100 | 0.25 | ST_ENS_OPEN (mejor t) | 132 | +14.3% | 105 | 3% | 0% | 95% |

## 5. Oportunidades no apostadas (lo que quedo fuera por la regla del nivel)

Para cada celda: los partidos donde la estrategia tenia un lado pero la regla del nivel dijo NO. 'Neto' = ganancia en unidades si hubieras apostado todo eso. Positivo = el filtro dejo dinero en la mesa; negativo = el filtro evito perdidas.

| Estrategia | Nivel | No apostados | Win% omitidos | ROI omitidos | Ganado que se perdio (u) | Perdida evitada (u) | Neto (u) |
|---|---|---|---|---|---|---|---|
| ST_ENS | 2 Agresivo | 1078 | 48.3% | -7.7% | 474 | 557 | -83 |
| ST_ENS | 3 Equilibrado | 1602 | 48.6% | -7.3% | 707 | 824 | -117 |
| ST_ENS | 4 Prudente | 2145 | 48.2% | -8.0% | 940 | 1111 | -171 |
| ST_ENS | 5 Conservador | 2512 | 48.6% | -7.2% | 1110 | 1291 | -181 |
| ST_FF | 2 Agresivo | 949 | 49.8% | -4.8% | 430 | 476 | -46 |
| ST_FF | 3 Equilibrado | 1412 | 50.6% | -3.3% | 650 | 697 | -47 |
| ST_FF | 4 Prudente | 1902 | 50.7% | -3.2% | 876 | 938 | -62 |
| ST_FF | 5 Conservador | 2374 | 50.6% | -3.4% | 1092 | 1173 | -81 |
| ST_REF | 2 Agresivo | 1162 | 50.6% | -3.4% | 535 | 574 | -39 |
| ST_REF | 3 Equilibrado | 1672 | 50.4% | -3.9% | 765 | 830 | -65 |
| ST_REF | 4 Prudente | 2169 | 50.1% | -4.4% | 987 | 1083 | -96 |
| ST_REF | 5 Conservador | 2501 | 50.7% | -3.2% | 1153 | 1233 | -80 |
| TT_ENS | 2 Agresivo | 1034 | 50.0% | -4.5% | 470 | 517 | -47 |
| TT_ENS | 3 Equilibrado | 1551 | 49.4% | -5.7% | 696 | 785 | -89 |
| TT_ENS | 4 Prudente | 2091 | 49.7% | -5.0% | 945 | 1051 | -106 |
| TT_ENS | 5 Conservador | 2480 | 50.2% | -4.1% | 1133 | 1234 | -101 |
| ML_ENS | 2 Agresivo | 1057 | 54.3% | -5.8% | 422 | 483 | -61 |
| ML_ENS | 3 Equilibrado | 1593 | 55.8% | -7.1% | 591 | 704 | -113 |
| ML_ENS | 4 Prudente | 2106 | 57.3% | -6.1% | 770 | 899 | -129 |
| ML_ENS | 5 Conservador | 2507 | 57.9% | -6.2% | 898 | 1055 | -157 |
| STEAM_FOLLOW | 2 Agresivo | 993 | 51.1% | -2.5% | 461 | 486 | -25 |
| STEAM_FOLLOW | 3 Equilibrado | 1147 | 50.3% | -4.0% | 525 | 570 | -45 |
| STEAM_FOLLOW | 4 Prudente | 1591 | 51.4% | -1.8% | 744 | 773 | -29 |
| STEAM_FOLLOW | 5 Conservador | 1905 | 52.3% | -0.1% | 906 | 908 | -2 |

## 6. Diagnostico de confianza: sube el ROI cuando la senal es mas fuerte?

Si una senal tiene informacion, el ROI debe subir de la franja 0-20 a la 80-100. Si sube y baja al azar, es ruido.

| Estrategia | 0-20 | 20-40 | 40-60 | 60-80 | 80-100 | Spearman |
|---|---|---|---|---|---|---|
| ST_RATING | -6.7% (567) | -2.3% (561) | -6.4% (473) | -9.0% (476) | -0.1% (560) | +0.30 |
| ST_ABS | -2.1% (538) | -4.1% (460) | -8.9% (438) | -1.1% (442) | -13.6% (444) | -0.40 |
| ST_PLAYER | -6.9% (597) | -13.0% (476) | -10.5% (446) | -9.0% (470) | +1.1% (648) | +0.40 |
| ST_FF | +2.3% (472) | -11.9% (477) | -0.2% (463) | -3.0% (490) | -1.8% (735) | -0.30 |
| ST_REF | +2.6% (584) | -9.5% (578) | -4.9% (510) | -6.3% (497) | -1.3% (468) | -0.10 |
| ST_REST | -2.4% (364) | -9.7% (279) | -6.9% (320) | -3.2% (288) | -1.8% (241) | +0.40 |
| ST_ENS | -3.3% (543) | -12.2% (535) | -6.4% (524) | -10.0% (543) | -0.7% (492) | +0.30 |
| ST_ENS_OPEN | -0.4% (529) | +2.5% (531) | -8.3% (535) | -2.9% (527) | +5.3% (515) | +0.20 |
| TT_MODEL | +1.0% (497) | -7.8% (530) | -7.8% (534) | -8.7% (529) | +4.7% (547) | +0.10 |
| TT_REF | -0.9% (526) | -11.1% (528) | +1.4% (518) | -2.0% (534) | -1.5% (531) | -0.10 |
| TT_ENS | -3.6% (519) | -5.5% (515) | -8.1% (517) | -3.1% (540) | +4.2% (546) | +0.60 |
| ML_ENS | -3.7% (539) | -8.0% (518) | -9.6% (536) | -3.2% (513) | -7.6% (529) | +0.10 |
| STEAM_FOLLOW | -0.5% (71) | -2.7% (922) | -13.2% (154) | +3.6% (444) | +5.2% (421) | +0.60 |
| STEAM_FADE | -8.6% (71) | -6.4% (922) | +4.1% (154) | -12.7% (444) | -14.3% (421) | -0.60 |