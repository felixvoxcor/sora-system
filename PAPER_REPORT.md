# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **57** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 11 · -14%* | 20 · -5%* | 26 · -4%* | 35 · -13% | 41 · -7% | 8 · +20%* |
| H6 | 10 · -62%* | 18 · -15%* | 29 · -14%* | 43 · -11% | 48 · -4% | 9 · -37%* |
| D | 11 · -31%* | 19 · +0%* | 27 · -8%* | 41 · -2% | 51 · +1% | 6 · -38%* |
| L | 11 · -47%* | 18 · -25%* | 27 · -7%* | 39 · +8% | 48 · +3% | 9 · -100%* |
| D+conf | 1 · -100%* | 4 · -4%* | 6 · +29%* | 9 · +8%* | 10 · -3%* | 2 · -100%* |
| D+fade | 7 · +9%* | 10 · +33%* | 12 · +27%* | 16 · +18%* | 16 · +18%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 10 · -23%* | 18 · -15%* | 28 · -11%* | 37 · -12% | 43 · -3% | 6 · -67%* |
| H6 | 11 · -13%* | 16 · -16%* | 25 · -16%* | 48 · -16% | 53 · -17% | 4 · -51%* |
| D | 12 · -20%* | 18 · -14%* | 28 · -4%* | 45 · -11% | 52 · -8% | 5 · -23%* |
| L | 11 · -31%* | 18 · -37%* | 28 · -25%* | 38 · -25% | 49 · -22% | 8 · -29%* |
| D+conf | 2 · -100%* | 3 · -35%* | 5 · +16%* | 12 · -20%* | 12 · -20%* | – |
| D+fade | 4 · +45%* | 6 · +28%* | 10 · +34%* | 14 · +22%* | 15 · +14%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 14 · -32%* | 22 · -30%* | 24 · -26%* | 36 · -18% | 45 · -17% | 4 · +30%* |
| H6 | 11 · -100%* | 22 · -41%* | 30 · -39% | 46 · -21% | 49 · -19% | 8 · +6%* |
| D | 9 · -100%* | 23 · -43%* | 28 · -34%* | 43 · -15% | 50 · -16% | 7 · -41%* |
| L | 12 · -78%* | 21 · -45%* | 28 · -44%* | 40 · -8% | 47 · -20% | 10 · -0%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 11 · +19%* | 12 · +34%* | 3 · -56%* |
| D+fade | 6 · -100%* | 10 · -45%* | 11 · -50%* | 15 · -19%* | 16 · -24%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 13 · -55%* | 20 · -54%* | 26 · -40%* | 39 · -33% | 43 · -26% | 6 · +42%* |
| H6 | 11 · -56%* | 19 · -54%* | 32 · -38% | 47 · -40% | 53 · -38% | 4 · +29%* |
| D | 11 · -56%* | 20 · -61%* | 31 · -45% | 48 · -35% | 55 · -36% | 2 · -18%* |
| L | 11 · -59%* | 18 · -67%* | 30 · -62% | 44 · -46% | 50 · -42% | 7 · +41%* |
| D+conf | 1 · -100%* | 3 · -100%* | 7 · -56%* | 11 · -60%* | 12 · -49%* | – |
| D+fade | 6 · -51%* | 7 · -58%* | 11 · -51%* | 15 · -22%* | 15 · -22%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 6 · +60%* | 18 · +17%* | 21 · +18%* | 28 · -11%* | 41 · -7% | 8 · -4%* |
| H6 | 6 · +27%* | 18 · +6%* | 26 · +10%* | 32 · +13% | 41 · +2% | 16 · -52%* |
| D | 4 · -5%* | 16 · +8%* | 25 · +7%* | 38 · +6% | 45 · -2% | 12 · -5%* |
| L | 3 · -37%* | 17 · +1%* | 28 · +2%* | 40 · +0% | 43 · +2% | 14 · -19%* |
| D+conf | 1 · +93%* | 3 · +28%* | 6 · +60%* | 10 · +54%* | 11 · +40%* | 4 · +43%* |
| D+fade | 3 · -38%* | 7 · -18%* | 12 · -21%* | 16 · -17%* | 17 · -22%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 43. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.077 (n=26) | -0.172 (n=29) | +0.000 (n=27) | -0.074 (n=27) | -0.333 (n=6) | +0.083 (n=12) |
| spread · B | +0.214 (n=28) | -0.040 (n=25) | -0.071 (n=28) | +0.071 (n=28) | +0.000 (n=5) | -0.100 (n=10) |
| ml · A | +0.002 (n=24) | -0.003 (n=30) | +0.002 (n=28) | +0.000 (n=28) | +0.000 (n=10) | +0.002 (n=11) |
| ml · B | +0.006 (n=26) | +0.002 (n=32) | +0.000 (n=31) | -0.000 (n=30) | -0.001 (n=7) | +0.002 (n=11) |
| total · T | +1.333 (n=21) | +0.462 (n=26) | -0.040 (n=25) | -0.250 (n=28) | -0.167 (n=6) | -0.083 (n=12) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 49 | -0.611 (-1.00) | – | – | – |
| spread · A · D | 57 | -0.479 (-0.86) | – | – | – |
| spread · B · E | 49 | -0.688 (-1.22) | – | – | – |
| spread · B · D | 57 | -0.527 (-0.91) | – | – | – |
| ml · A · E | 49 | – | 0.2128 | 0.1952 | +0.0177 (1.62) |
| ml · A · D | 57 | – | 0.2143 | 0.1959 | +0.0184 (1.92) |
| ml · B · E | 49 | – | 0.2233 | 0.1952 | +0.0281 (2.32) |
| ml · B · D | 57 | – | 0.2196 | 0.1959 | +0.0237 (2.31) |
| total · T · E | 49 | +0.536 (0.59) | – | – | – |
| total · T · D | 57 | -0.077 (-0.10) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._