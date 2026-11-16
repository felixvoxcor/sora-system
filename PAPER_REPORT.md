# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **125** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 19 · +0%* | 42 · +0% | 61 · -9% | 80 · -19% | 89 · -16% | 15 · +15%* |
| H6 | 24 · -13%* | 47 · -7% | 73 · -1% | 96 · -3% | 107 · -0% | 18 · -5%* |
| D | 29 · -8%* | 48 · +3% | 70 · +3% | 96 · +1% | 112 · +2% | 13 · +2%* |
| L | 27 · -22%* | 47 · -10% | 68 · +1% | 92 · +6% | 106 · +3% | 19 · -40%* |
| D+conf | 2 · -7%* | 7 · -18%* | 12 · +28%* | 18 · +7%* | 19 · +1%* | 4 · -53%* |
| D+fade | 17 · -11%* | 22 · +4%* | 28 · +8%* | 34 · +6% | 34 · +6% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · -33%* | 36 · -20% | 57 · -10% | 78 · -14% | 90 · -7% | 14 · -32%* |
| H6 | 27 · -2%* | 46 · +3% | 66 · -11% | 99 · -10% | 113 · -9% | 12 · -52%* |
| D | 27 · -8%* | 49 · -3% | 67 · -0% | 99 · -6% | 116 · -5% | 9 · -36%* |
| L | 24 · -36%* | 49 · -18% | 64 · -20% | 85 · -13% | 106 · -15% | 19 · -40%* |
| D+conf | 2 · -100%* | 6 · -36%* | 10 · -4%* | 19 · -9%* | 22 · -13%* | – |
| D+fade | 10 · -4%* | 17 · +1%* | 24 · +11%* | 32 · +1% | 33 · -2% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · -44%* | 40 · -26% | 55 · -27% | 80 · -26% | 96 · -28% | 8 · +30%* |
| H6 | 30 · -69% | 55 · -38% | 71 · -33% | 98 · -14% | 105 · -14% | 20 · -16%* |
| D | 29 · -60%* | 53 · -33% | 71 · -20% | 94 · -11% | 109 · -11% | 16 · -40%* |
| L | 32 · -61% | 50 · -40% | 70 · -20% | 95 · -8% | 110 · -15% | 15 · -12%* |
| D+conf | 1 · -100%* | 9 · -31%* | 15 · -14%* | 19 · -18%* | 23 · +3%* | 3 · -56%* |
| D+fade | 20 · -65%* | 30 · -40% | 35 · -49% | 39 · -37% | 40 · -39% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 22 · -44%* | 39 · -41% | 52 · -36% | 77 · -33% | 86 · -30% | 18 · -24%* |
| H6 | 29 · -47%* | 47 · -22% | 75 · -16% | 103 · -26% | 116 · -22% | 9 · -18%* |
| D | 26 · -45%* | 47 · -37% | 72 · -18% | 106 · -19% | 116 · -18% | 9 · -6%* |
| L | 29 · -44%* | 45 · -46% | 66 · -41% | 95 · -26% | 110 · -26% | 15 · +37%* |
| D+conf | 1 · -100%* | 5 · -72%* | 13 · -44%* | 20 · -57%* | 22 · -45%* | – |
| D+fade | 18 · -75%* | 24 · -58%* | 33 · -45% | 41 · -40% | 41 · -40% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 12 · -4%* | 36 · +1% | 45 · +2% | 61 · -6% | 83 · -4% | 21 · +0%* |
| H6 | 11 · -13%* | 34 · -10% | 56 · -8% | 66 · -2% | 89 · +1% | 36 · -15% |
| D | 10 · -43%* | 33 · -1% | 54 · +3% | 75 · +2% | 96 · +1% | 29 · +12%* |
| L | 8 · -52%* | 39 · -2% | 56 · +2% | 79 · +2% | 92 · +6% | 33 · -19% |
| D+conf | 2 · -4%* | 6 · -5%* | 14 · +9%* | 21 · +19%* | 25 · +15%* | 14 · +36%* |
| D+fade | 5 · -63%* | 13 · -27%* | 21 · -9%* | 27 · -8%* | 29 · -8%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 93. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.066 (n=61) | -0.096 (n=73) | -0.043 (n=70) | -0.029 (n=68) | -0.083 (n=12) | -0.143 (n=28) |
| spread · B | +0.193 (n=57) | -0.106 (n=66) | -0.030 (n=67) | +0.031 (n=64) | +0.000 (n=10) | -0.042 (n=24) |
| ml · A | -0.002 (n=55) | -0.002 (n=71) | +0.001 (n=71) | +0.000 (n=70) | +0.002 (n=15) | -0.003 (n=35) |
| ml · B | +0.001 (n=52) | -0.002 (n=75) | -0.002 (n=72) | +0.000 (n=66) | -0.002 (n=13) | -0.003 (n=33) |
| total · T | +1.511 (n=45) | +0.429 (n=56) | +0.093 (n=54) | -0.071 (n=56) | +0.000 (n=14) | +0.143 (n=21) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 104 | -0.756 (-1.56) | – | – | – |
| spread · A · D | 125 | -0.396 (-0.99) | – | – | – |
| spread · B · E | 104 | -1.059 (-2.36) | – | – | – |
| spread · B · D | 125 | -0.615 (-1.42) | – | – | – |
| ml · A · E | 104 | – | 0.1971 | 0.1818 | +0.0153 (2.27) |
| ml · A · D | 125 | – | 0.1969 | 0.1844 | +0.0124 (1.79) |
| ml · B · E | 104 | – | 0.2014 | 0.1818 | +0.0196 (2.66) |
| ml · B · D | 125 | – | 0.1972 | 0.1844 | +0.0128 (1.90) |
| total · T · E | 104 | +0.576 (1.23) | – | – | – |
| total · T · D | 125 | +0.297 (0.68) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._