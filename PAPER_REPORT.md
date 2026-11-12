# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **100** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 17 · +12%* | 36 · -4% | 51 · -14% | 69 · -25% | 77 · -21% | 13 · +18%* |
| H6 | 19 · -30%* | 37 · -13% | 56 · -8% | 75 · -11% | 86 · -7% | 14 · -32%* |
| D | 22 · -22%* | 37 · +3% | 55 · +1% | 75 · -3% | 90 · -0% | 10 · -24%* |
| L | 23 · -25%* | 39 · -6% | 55 · +1% | 73 · +5% | 85 · +1% | 15 · -75%* |
| D+conf | 2 · -7%* | 5 · +14%* | 8 · +45%* | 13 · +4%* | 14 · -3%* | 3 · -100%* |
| D+fade | 16 · -17%* | 20 · +5%* | 25 · +7%* | 30 · +8% | 30 · +8% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · -47%* | 31 · -26% | 50 · -12% | 67 · -14% | 78 · -5% | 12 · -52%* |
| H6 | 22 · -22%* | 36 · -10% | 49 · -19% | 78 · -14% | 89 · -10% | 11 · -47%* |
| D | 23 · -25%* | 39 · -11% | 52 · -4% | 79 · -10% | 91 · -5% | 9 · -36%* |
| L | 23 · -42%* | 40 · -24% | 51 · -21% | 67 · -20% | 83 · -19% | 17 · -56%* |
| D+conf | 2 · -100%* | 5 · -61%* | 7 · -17%* | 16 · -15%* | 18 · -14%* | – |
| D+fade | 10 · -4%* | 15 · +2%* | 21 · +18%* | 27 · +6%* | 28 · +2%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · -38%* | 35 · -38% | 46 · -30% | 69 · -30% | 82 · -31% | 8 · +30%* |
| H6 | 24 · -85%* | 43 · -45% | 55 · -43% | 77 · -27% | 82 · -25% | 18 · -6%* |
| D | 22 · -83%* | 41 · -46% | 54 · -36% | 73 · -22% | 85 · -20% | 15 · -36%* |
| L | 27 · -68%* | 41 · -44% | 55 · -36% | 73 · -16% | 85 · -24% | 15 · -12%* |
| D+conf | – | 7 · -11%* | 11 · +4%* | 14 · +2%* | 17 · +16%* | 3 · -56%* |
| D+fade | 19 · -81%* | 27 · -46%* | 31 · -53% | 35 · -39% | 36 · -41% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · -59%* | 32 · -57% | 44 · -46% | 67 · -38% | 76 · -35% | 14 · -13%* |
| H6 | 24 · -73%* | 36 · -54% | 57 · -39% | 80 · -40% | 91 · -33% | 9 · -18%* |
| D | 23 · -65%* | 39 · -61% | 58 · -41% | 83 · -35% | 93 · -32% | 7 · +21%* |
| L | 26 · -63%* | 39 · -63% | 53 · -59% | 73 · -43% | 86 · -41% | 14 · +36%* |
| D+conf | 1 · -100%* | 4 · -100%* | 11 · -46%* | 16 · -55%* | 18 · -40%* | – |
| D+fade | 17 · -73%* | 22 · -69%* | 29 · -57%* | 36 · -48% | 36 · -48% | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 10 · -4%* | 31 · -2% | 38 · -5% | 54 · -12% | 74 · -10% | 16 · +8%* |
| H6 | 10 · -5%* | 31 · -14% | 48 · -9% | 55 · -3% | 71 · -3% | 29 · -34%* |
| D | 9 · -36%* | 28 · -11%* | 45 · -2% | 61 · -3% | 77 · -3% | 23 · -1%* |
| L | 7 · -45%* | 31 · -14% | 46 · -5% | 63 · -6% | 71 · -3% | 29 · -21%* |
| D+conf | 2 · -4%* | 5 · -23%* | 11 · +5%* | 16 · +8%* | 20 · +6%* | 11 · +21%* |
| D+fade | 4 · -53%* | 12 · -21%* | 20 · -5%* | 26 · -5%* | 28 · -5%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 86. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | -0.059 (n=51) | -0.214 (n=56) | -0.145 (n=55) | -0.036 (n=55) | -0.125 (n=8) | -0.240 (n=25) |
| spread · B | +0.160 (n=50) | -0.163 (n=49) | -0.038 (n=52) | +0.039 (n=51) | +0.143 (n=7) | -0.095 (n=21) |
| ml · A | -0.005 (n=46) | -0.002 (n=55) | -0.000 (n=54) | +0.000 (n=55) | +0.002 (n=11) | -0.003 (n=31) |
| ml · B | -0.001 (n=44) | -0.002 (n=57) | -0.002 (n=58) | +0.000 (n=53) | -0.001 (n=11) | -0.003 (n=29) |
| total · T | +1.553 (n=38) | +0.542 (n=48) | +0.178 (n=45) | -0.130 (n=46) | +0.091 (n=11) | +0.100 (n=20) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 90 | -0.806 (-1.57) | – | – | – |
| spread · A · D | 100 | -0.612 (-1.33) | – | – | – |
| spread · B · E | 90 | -1.065 (-2.21) | – | – | – |
| spread · B · D | 100 | -0.854 (-1.76) | – | – | – |
| ml · A · E | 90 | – | 0.1972 | 0.1787 | +0.0185 (2.53) |
| ml · A · D | 100 | – | 0.1987 | 0.1799 | +0.0188 (2.58) |
| ml · B · E | 90 | – | 0.2023 | 0.1787 | +0.0236 (3.08) |
| ml · B · D | 100 | – | 0.2016 | 0.1799 | +0.0217 (3.00) |
| total · T · E | 90 | +0.323 (0.65) | – | – | – |
| total · T · D | 100 | +0.135 (0.28) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._