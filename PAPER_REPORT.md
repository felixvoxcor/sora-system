# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **91** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 17 · +12%* | 33 · -2% | 48 · -12% | 64 · -22% | 71 · -17% | 12 · +28%* |
| H6 | 18 · -37%* | 34 · -16% | 50 · -8% | 68 · -10% | 78 · -7% | 13 · -26%* |
| D | 21 · -27%* | 33 · +4% | 49 · +1% | 68 · -2% | 83 · +1% | 8 · -5%* |
| L | 22 · -30%* | 35 · -7% | 49 · +2% | 67 · +6% | 79 · +1% | 12 · -68%* |
| D+conf | 2 · -7%* | 5 · +14%* | 8 · +45%* | 13 · +4%* | 14 · -3%* | 2 · -100%* |
| D+fade | 15 · -24%* | 19 · +0%* | 23 · +7%* | 28 · +8%* | 28 · +8%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 17 · -55%* | 29 · -34%* | 46 · -13% | 61 · -15% | 71 · -3% | 12 · -52%* |
| H6 | 20 · -33%* | 31 · -14% | 43 · -20% | 71 · -14% | 81 · -8% | 10 · -61%* |
| D | 21 · -36%* | 35 · -18% | 47 · -6% | 71 · -8% | 82 · -2% | 9 · -36%* |
| L | 20 · -52%* | 35 · -29% | 46 · -25% | 61 · -22% | 75 · -18% | 16 · -53%* |
| D+conf | 2 · -100%* | 5 · -61%* | 7 · -17%* | 16 · -15%* | 17 · -9%* | – |
| D+fade | 10 · -4%* | 15 · +2%* | 21 · +18%* | 26 · +10%* | 27 · +6%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · -38%* | 33 · -35% | 43 · -25% | 64 · -24% | 76 · -26% | 7 · +25%* |
| H6 | 22 · -83%* | 39 · -39% | 49 · -36% | 70 · -22% | 74 · -20% | 17 · -1%* |
| D | 20 · -82%* | 38 · -41% | 48 · -28% | 67 · -15% | 78 · -13% | 13 · -38%* |
| L | 25 · -65%* | 38 · -39% | 50 · -30% | 67 · -8% | 77 · -17% | 14 · -17%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 13 · +9%* | 16 · +23%* | 3 · -56%* |
| D+fade | 17 · -78%* | 25 · -42%* | 27 · -46%* | 31 · -31% | 32 · -33% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · -59%* | 31 · -56% | 41 · -47% | 61 · -36% | 70 · -32% | 13 · -19%* |
| H6 | 22 · -71%* | 32 · -55% | 51 · -38% | 72 · -39% | 82 · -32% | 9 · -18%* |
| D | 21 · -62%* | 35 · -62% | 53 · -40% | 75 · -33% | 85 · -29% | 6 · +13%* |
| L | 23 · -59%* | 34 · -63% | 48 · -59% | 66 · -40% | 78 · -40% | 13 · +34%* |
| D+conf | 1 · -100%* | 4 · -100%* | 11 · -46%* | 15 · -51%* | 17 · -37%* | – |
| D+fade | 15 · -70%* | 20 · -66%* | 26 · -52%* | 32 · -42% | 32 · -42% | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 10 · -4%* | 29 · -1%* | 35 · -2% | 50 · -12% | 69 · -9% | 14 · +10%* |
| H6 | 9 · -15%* | 28 · -19%* | 44 · -9% | 51 · -3% | 66 · -5% | 25 · -38%* |
| D | 8 · -53%* | 25 · -16%* | 41 · -2% | 57 · -3% | 73 · -3% | 18 · -5%* |
| L | 6 · -69%* | 28 · -18%* | 43 · -7% | 60 · -8% | 67 · -3% | 24 · -13%* |
| D+conf | 2 · -4%* | 5 · -23%* | 10 · +15%* | 15 · +15%* | 19 · +11%* | 9 · +27%* |
| D+fade | 4 · -53%* | 12 · -21%* | 20 · -5%* | 26 · -5%* | 28 · -5%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 79. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | -0.083 (n=48) | -0.220 (n=50) | -0.163 (n=49) | -0.041 (n=49) | -0.125 (n=8) | -0.217 (n=23) |
| spread · B | +0.152 (n=46) | -0.186 (n=43) | -0.064 (n=47) | +0.065 (n=46) | +0.143 (n=7) | -0.095 (n=21) |
| ml · A | -0.004 (n=43) | -0.003 (n=49) | -0.001 (n=48) | +0.000 (n=50) | +0.000 (n=10) | -0.003 (n=27) |
| ml · B | -0.001 (n=41) | -0.002 (n=51) | -0.002 (n=53) | +0.000 (n=48) | -0.001 (n=11) | -0.002 (n=26) |
| total · T | +1.543 (n=35) | +0.523 (n=44) | +0.122 (n=41) | -0.140 (n=43) | +0.000 (n=10) | +0.100 (n=20) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 83 | -0.755 (-1.49) | – | – | – |
| spread · A · D | 91 | -0.552 (-1.19) | – | – | – |
| spread · B · E | 83 | -1.216 (-2.55) | – | – | – |
| spread · B · D | 91 | -0.927 (-1.89) | – | – | – |
| ml · A · E | 83 | – | 0.1933 | 0.1768 | +0.0165 (2.12) |
| ml · A · D | 91 | – | 0.1959 | 0.1797 | +0.0162 (2.05) |
| ml · B · E | 83 | – | 0.2007 | 0.1768 | +0.0239 (2.94) |
| ml · B · D | 91 | – | 0.2010 | 0.1797 | +0.0213 (2.75) |
| total · T · E | 83 | +0.339 (0.66) | – | – | – |
| total · T · D | 91 | +0.097 (0.19) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._