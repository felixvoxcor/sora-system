# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **102** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 17 · +12%* | 36 · -4% | 51 · -14% | 69 · -25% | 77 · -21% | 14 · +9%* |
| H6 | 19 · -30%* | 37 · -13% | 57 · -6% | 77 · -11% | 88 · -7% | 14 · -32%* |
| D | 22 · -22%* | 37 · +3% | 55 · +1% | 77 · -6% | 92 · -2% | 10 · -24%* |
| L | 23 · -25%* | 39 · -6% | 55 · +1% | 75 · +2% | 87 · -1% | 15 · -75%* |
| D+conf | 2 · -7%* | 5 · +14%* | 8 · +45%* | 13 · +4%* | 14 · -3%* | 3 · -100%* |
| D+fade | 16 · -17%* | 20 · +5%* | 25 · +7%* | 31 · +4% | 31 · +4% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 19 · -40%* | 32 · -22% | 51 · -10% | 68 · -13% | 79 · -4% | 12 · -52%* |
| H6 | 23 · -18%* | 38 · -5% | 51 · -14% | 80 · -12% | 91 · -8% | 11 · -47%* |
| D | 23 · -25%* | 41 · -7% | 54 · -1% | 81 · -8% | 93 · -3% | 9 · -36%* |
| L | 23 · -42%* | 42 · -18% | 53 · -17% | 69 · -17% | 85 · -17% | 17 · -56%* |
| D+conf | 2 · -100%* | 6 · -36%* | 8 · -4%* | 17 · -9%* | 19 · -9%* | – |
| D+fade | 10 · -4%* | 15 · +2%* | 21 · +18%* | 27 · +6%* | 28 · +2%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · -38%* | 35 · -38% | 46 · -30% | 69 · -30% | 83 · -30% | 8 · +30%* |
| H6 | 24 · -85%* | 43 · -45% | 55 · -43% | 78 · -28% | 84 · -25% | 18 · -6%* |
| D | 22 · -83%* | 41 · -46% | 54 · -36% | 75 · -24% | 87 · -22% | 15 · -36%* |
| L | 27 · -68%* | 41 · -44% | 55 · -36% | 75 · -18% | 87 · -26% | 15 · -12%* |
| D+conf | – | 7 · -11%* | 11 · +4%* | 14 · +2%* | 17 · +16%* | 3 · -56%* |
| D+fade | 19 · -81%* | 27 · -46%* | 31 · -53% | 35 · -39% | 36 · -41% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 19 · -53%* | 33 · -54% | 45 · -44% | 68 · -37% | 77 · -34% | 14 · -13%* |
| H6 | 25 · -66%* | 38 · -48% | 59 · -35% | 82 · -38% | 93 · -31% | 9 · -18%* |
| D | 23 · -65%* | 41 · -55% | 60 · -38% | 85 · -33% | 95 · -30% | 7 · +21%* |
| L | 26 · -63%* | 41 · -57% | 55 · -55% | 75 · -40% | 88 · -39% | 14 · +36%* |
| D+conf | 1 · -100%* | 5 · -72%* | 12 · -39%* | 17 · -49%* | 19 · -36%* | – |
| D+fade | 17 · -73%* | 22 · -69%* | 29 · -57%* | 36 · -48% | 36 · -48% | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 10 · -4%* | 31 · -2% | 38 · -5% | 54 · -12% | 74 · -10% | 17 · +2%* |
| H6 | 10 · -5%* | 31 · -14% | 49 · -11% | 56 · -5% | 73 · -3% | 29 · -34%* |
| D | 9 · -36%* | 28 · -11%* | 45 · -2% | 63 · -3% | 79 · -3% | 23 · -1%* |
| L | 7 · -45%* | 31 · -14% | 46 · -5% | 65 · -6% | 73 · -3% | 29 · -21%* |
| D+conf | 2 · -4%* | 5 · -23%* | 11 · +5%* | 16 · +8%* | 20 · +6%* | 11 · +21%* |
| D+fade | 4 · -53%* | 12 · -21%* | 20 · -5%* | 26 · -5%* | 28 · -5%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 86. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | -0.059 (n=51) | -0.140 (n=57) | -0.145 (n=55) | -0.036 (n=55) | -0.125 (n=8) | -0.240 (n=25) |
| spread · B | +0.176 (n=51) | -0.078 (n=51) | -0.037 (n=54) | +0.038 (n=53) | +0.125 (n=8) | -0.095 (n=21) |
| ml · A | -0.005 (n=46) | -0.002 (n=55) | -0.000 (n=54) | +0.000 (n=55) | +0.002 (n=11) | -0.003 (n=31) |
| ml · B | +0.000 (n=45) | -0.001 (n=59) | -0.002 (n=60) | +0.000 (n=55) | -0.002 (n=12) | -0.003 (n=29) |
| total · T | +1.553 (n=38) | +0.551 (n=49) | +0.178 (n=45) | -0.130 (n=46) | +0.091 (n=11) | +0.100 (n=20) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 91 | -0.806 (-1.58) | – | – | – |
| spread · A · D | 102 | -0.624 (-1.38) | – | – | – |
| spread · B · E | 91 | -1.038 (-2.19) | – | – | – |
| spread · B · D | 102 | -0.832 (-1.74) | – | – | – |
| ml · A · E | 91 | – | 0.1964 | 0.1783 | +0.0181 (2.49) |
| ml · A · D | 102 | – | 0.1983 | 0.1791 | +0.0192 (2.68) |
| ml · B · E | 91 | – | 0.2006 | 0.1783 | +0.0223 (2.91) |
| ml · B · D | 102 | – | 0.1993 | 0.1791 | +0.0202 (2.82) |
| total · T · E | 91 | +0.325 (0.66) | – | – | – |
| total · T · D | 102 | +0.139 (0.29) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._