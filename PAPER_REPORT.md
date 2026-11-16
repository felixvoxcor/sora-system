# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **124** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 19 · +0%* | 42 · +0% | 61 · -9% | 80 · -19% | 89 · -16% | 15 · +15%* |
| H6 | 24 · -13%* | 46 · -5% | 72 · +0% | 95 · -2% | 106 · +1% | 18 · -5%* |
| D | 28 · -5%* | 47 · +5% | 69 · +5% | 95 · +2% | 111 · +3% | 13 · +2%* |
| L | 26 · -19%* | 46 · -8% | 67 · +3% | 91 · +7% | 105 · +4% | 19 · -40%* |
| D+conf | 2 · -7%* | 7 · -18%* | 12 · +28%* | 18 · +7%* | 19 · +1%* | 4 · -53%* |
| D+fade | 17 · -11%* | 22 · +4%* | 28 · +8%* | 34 · +6% | 34 · +6% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · -33%* | 36 · -20% | 57 · -10% | 78 · -14% | 90 · -7% | 14 · -32%* |
| H6 | 27 · -2%* | 46 · +3% | 65 · -10% | 98 · -9% | 112 · -8% | 12 · -52%* |
| D | 27 · -8%* | 48 · -1% | 66 · +1% | 98 · -5% | 115 · -4% | 9 · -36%* |
| L | 24 · -36%* | 49 · -18% | 64 · -20% | 85 · -13% | 105 · -14% | 19 · -40%* |
| D+conf | 2 · -100%* | 6 · -36%* | 10 · -4%* | 19 · -9%* | 22 · -13%* | – |
| D+fade | 10 · -4%* | 17 · +1%* | 24 · +11%* | 32 · +1% | 33 · -2% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · -44%* | 40 · -26% | 55 · -27% | 80 · -26% | 96 · -28% | 8 · +30%* |
| H6 | 29 · -68%* | 54 · -37% | 70 · -32% | 97 · -13% | 104 · -13% | 20 · -16%* |
| D | 28 · -58%* | 52 · -32% | 70 · -19% | 93 · -10% | 108 · -10% | 16 · -40%* |
| L | 31 · -59% | 49 · -39% | 69 · -18% | 94 · -7% | 109 · -15% | 15 · -12%* |
| D+conf | 1 · -100%* | 9 · -31%* | 15 · -14%* | 19 · -18%* | 23 · +3%* | 3 · -56%* |
| D+fade | 20 · -65%* | 30 · -40% | 35 · -49% | 39 · -37% | 40 · -39% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 22 · -44%* | 39 · -41% | 52 · -36% | 77 · -33% | 86 · -30% | 18 · -24%* |
| H6 | 29 · -47%* | 46 · -21% | 74 · -15% | 102 · -26% | 115 · -21% | 9 · -18%* |
| D | 26 · -45%* | 46 · -35% | 71 · -17% | 105 · -18% | 115 · -17% | 9 · -6%* |
| L | 29 · -44%* | 45 · -46% | 66 · -41% | 94 · -26% | 109 · -26% | 15 · +37%* |
| D+conf | 1 · -100%* | 5 · -72%* | 13 · -44%* | 20 · -57%* | 22 · -45%* | – |
| D+fade | 18 · -75%* | 24 · -58%* | 33 · -45% | 41 · -40% | 41 · -40% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 12 · -4%* | 36 · +1% | 45 · +2% | 61 · -6% | 83 · -4% | 21 · +0%* |
| H6 | 11 · -13%* | 34 · -10% | 55 · -10% | 65 · -3% | 88 · -0% | 36 · -15% |
| D | 10 · -43%* | 32 · -4% | 53 · +1% | 74 · +1% | 95 · +1% | 29 · +12%* |
| L | 8 · -52%* | 38 · -5% | 55 · +0% | 78 · +0% | 91 · +5% | 33 · -19% |
| D+conf | 2 · -4%* | 6 · -5%* | 14 · +9%* | 21 · +19%* | 25 · +15%* | 14 · +36%* |
| D+fade | 5 · -63%* | 13 · -27%* | 21 · -9%* | 27 · -8%* | 29 · -8%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 92. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.066 (n=61) | -0.069 (n=72) | -0.029 (n=69) | -0.015 (n=67) | -0.083 (n=12) | -0.143 (n=28) |
| spread · B | +0.193 (n=57) | -0.077 (n=65) | -0.015 (n=66) | +0.031 (n=64) | +0.000 (n=10) | -0.042 (n=24) |
| ml · A | -0.002 (n=55) | -0.002 (n=70) | +0.001 (n=70) | +0.000 (n=69) | +0.002 (n=15) | -0.003 (n=35) |
| ml · B | +0.001 (n=52) | -0.001 (n=74) | -0.002 (n=71) | +0.000 (n=66) | -0.002 (n=13) | -0.003 (n=33) |
| total · T | +1.511 (n=45) | +0.473 (n=55) | +0.113 (n=53) | -0.073 (n=55) | +0.000 (n=14) | +0.143 (n=21) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 104 | -0.756 (-1.56) | – | – | – |
| spread · A · D | 124 | -0.311 (-0.77) | – | – | – |
| spread · B · E | 104 | -1.059 (-2.36) | – | – | – |
| spread · B · D | 124 | -0.543 (-1.24) | – | – | – |
| ml · A · E | 104 | – | 0.1971 | 0.1818 | +0.0153 (2.27) |
| ml · A · D | 124 | – | 0.1980 | 0.1858 | +0.0123 (1.74) |
| ml · B · E | 104 | – | 0.2014 | 0.1818 | +0.0196 (2.66) |
| ml · B · D | 124 | – | 0.1985 | 0.1858 | +0.0127 (1.87) |
| total · T · E | 104 | +0.576 (1.23) | – | – | – |
| total · T · D | 124 | +0.283 (0.64) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._