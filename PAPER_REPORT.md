# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **52** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 9 · -16%* | 18 · -5%* | 24 · -4%* | 33 · -13% | 37 · -7% | 8 · +20%* |
| H6 | 8 · -77%* | 15 · -12%* | 26 · -12%* | 40 · -9% | 44 · -5% | 8 · -29%* |
| D | 9 · -37%* | 17 · +0%* | 25 · -9%* | 39 · -2% | 47 · -3% | 5 · -25%* |
| L | 9 · -57%* | 16 · -28%* | 25 · -8%* | 37 · +8% | 44 · -0% | 8 · -100%* |
| D+conf | 1 · -100%* | 4 · -4%* | 6 · +29%* | 9 · +8%* | 10 · -3%* | 1 · -100%* |
| D+fade | 5 · +13%* | 8 · +42%* | 10 · +32%* | 14 · +21%* | 14 · +21%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 7 · -18%* | 14 · -18%* | 24 · -13%* | 33 · -13% | 39 · -2% | 6 · -67%* |
| H6 | 7 · -20%* | 12 · -21%* | 21 · -19%* | 44 · -18% | 48 · -17% | 4 · -51%* |
| D | 9 · -36%* | 14 · -18%* | 24 · -5%* | 41 · -12% | 48 · -9% | 4 · -51%* |
| L | 9 · -37%* | 14 · -46%* | 24 · -29%* | 34 · -27% | 45 · -24% | 7 · -46%* |
| D+conf | 1 · -100%* | 2 · -2%* | 4 · +46%* | 11 · -13%* | 11 · -13%* | – |
| D+fade | 3 · +28%* | 4 · +43%* | 8 · +43%* | 12 · +26%* | 13 · +17%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 12 · -20%* | 20 · -23%* | 22 · -19%* | 32 · -13% | 41 · -14% | 4 · +30%* |
| H6 | 9 · -100%* | 19 · -31%* | 27 · -32%* | 42 · -18% | 45 · -16% | 7 · +21%* |
| D | 7 · -100%* | 21 · -37%* | 26 · -29%* | 40 · -13% | 46 · -13% | 6 · -31%* |
| L | 10 · -74%* | 19 · -39%* | 26 · -40%* | 37 · -6% | 43 · -16% | 9 · +11%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 11 · +19%* | 12 · +34%* | 2 · -34%* |
| D+fade | 4 · -100%* | 8 · -31%* | 9 · -39%* | 13 · -6%* | 14 · -13%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 10 · -60%* | 16 · -54%* | 22 · -37%* | 35 · -30% | 39 · -23% | 6 · +42%* |
| H6 | 7 · -58%* | 15 · -55%* | 28 · -36%* | 43 · -39% | 49 · -37% | 3 · +27%* |
| D | 8 · -63%* | 16 · -63%* | 27 · -43%* | 44 · -33% | 50 · -34% | 2 · -18%* |
| L | 9 · -71%* | 14 · -70%* | 26 · -63%* | 40 · -45% | 46 · -41% | 6 · +65%* |
| D+conf | – | 2 · -100%* | 6 · -49%* | 10 · -56%* | 11 · -45%* | – |
| D+fade | 5 · -41%* | 5 · -41%* | 9 · -40%* | 13 · -10%* | 13 · -10%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 6 · +60%* | 18 · +17%* | 21 · +18%* | 28 · -11%* | 39 · -7% | 6 · -5%* |
| H6 | 6 · +27%* | 16 · +19%* | 24 · +19%* | 30 · +20% | 38 · +10% | 14 · -45%* |
| D | 4 · -5%* | 16 · +8%* | 24 · +12%* | 35 · +15% | 42 · +5% | 10 · +14%* |
| L | 3 · -37%* | 16 · +8%* | 27 · +6%* | 38 · +6% | 41 · +7% | 11 · +4%* |
| D+conf | 1 · +93%* | 3 · +28%* | 6 · +60%* | 10 · +54%* | 11 · +40%* | 4 · +43%* |
| D+fade | 3 · -38%* | 7 · -18%* | 11 · -13%* | 15 · -11%* | 16 · -17%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 39. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.250 (n=24) | -0.192 (n=26) | +0.040 (n=25) | -0.040 (n=25) | -0.333 (n=6) | +0.200 (n=10) |
| spread · B | +0.375 (n=24) | -0.048 (n=21) | -0.042 (n=24) | +0.125 (n=24) | +0.000 (n=4) | +0.000 (n=8) |
| ml · A | +0.004 (n=22) | -0.005 (n=27) | +0.003 (n=26) | +0.000 (n=26) | +0.000 (n=10) | +0.004 (n=9) |
| ml · B | +0.008 (n=22) | +0.000 (n=28) | +0.001 (n=27) | -0.000 (n=26) | -0.001 (n=6) | +0.003 (n=9) |
| total · T | +1.333 (n=21) | +0.250 (n=24) | -0.083 (n=24) | -0.333 (n=27) | -0.167 (n=6) | -0.182 (n=11) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 45 | -0.291 (-0.45) | – | – | – |
| spread · A · D | 52 | -0.175 (-0.29) | – | – | – |
| spread · B · E | 45 | -0.419 (-0.70) | – | – | – |
| spread · B · D | 52 | -0.339 (-0.56) | – | – | – |
| ml · A · E | 45 | – | 0.2129 | 0.2000 | +0.0129 (1.18) |
| ml · A · D | 52 | – | 0.2168 | 0.2025 | +0.0143 (1.49) |
| ml · B · E | 45 | – | 0.2255 | 0.2000 | +0.0255 (2.08) |
| ml · B · D | 52 | – | 0.2251 | 0.2025 | +0.0226 (2.14) |
| total · T · E | 45 | +0.715 (0.73) | – | – | – |
| total · T · D | 52 | +0.096 (0.12) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._