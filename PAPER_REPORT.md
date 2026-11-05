# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **45** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 7 · -18%* | 14 · -18%* | 18 · -4%* | 27 · -15%* | 31 · -7% | 7 · +9%* |
| H6 | 7 · -73%* | 13 · -13%* | 22 · -13%* | 33 · -14% | 37 · -7% | 8 · -29%* |
| D | 7 · -46%* | 14 · -5%* | 21 · -9%* | 32 · -5% | 40 · -5% | 5 · -25%* |
| L | 8 · -52%* | 13 · -26%* | 21 · -9%* | 30 · +8% | 37 · -2% | 8 · -100%* |
| D+conf | 1 · -100%* | 3 · -35%* | 5 · +17%* | 6 · -2%* | 7 · -16%* | 1 · -100%* |
| D+fade | 3 · +26%* | 6 · +58%* | 8 · +42%* | 11 · +20%* | 11 · +20%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 7 · -18%* | 14 · -18%* | 21 · -9%* | 29 · -14%* | 34 · -5% | 4 · -51%* |
| H6 | 7 · -20%* | 12 · -21%* | 18 · -15%* | 37 · -12% | 41 · -12% | 4 · -51%* |
| D | 9 · -36%* | 13 · -26%* | 20 · -4%* | 36 · -10% | 41 · -2% | 4 · -51%* |
| L | 9 · -37%* | 13 · -42%* | 21 · -28%* | 30 · -24% | 38 · -20% | 7 · -46%* |
| D+conf | 1 · -100%* | 2 · -2%* | 4 · +46%* | 10 · -4%* | 10 · -4%* | – |
| D+fade | 3 · +28%* | 3 · +28%* | 5 · +52%* | 9 · +26%* | 9 · +26%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 10 · -38%* | 15 · -42%* | 17 · -35%* | 26 · -19%* | 34 · -16% | 4 · +30%* |
| H6 | 8 · -100%* | 16 · -39%* | 23 · -41%* | 35 · -20% | 38 · -17% | 7 · +21%* |
| D | 6 · -100%* | 17 · -50%* | 22 · -38%* | 33 · -14% | 39 · -13% | 6 · -31%* |
| L | 9 · -71%* | 15 · -54%* | 22 · -51%* | 30 · -5% | 36 · -18% | 9 · +11%* |
| D+conf | – | 5 · -41%* | 9 · -9%* | 9 · -9%* | 10 · +11%* | 2 · -34%* |
| D+fade | 3 · -100%* | 7 · -22%* | 8 · -31%* | 11 · +11%* | 12 · +1%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 10 · -60%* | 14 · -58%* | 20 · -38%* | 30 · -24% | 33 · -19% | 5 · +2%* |
| H6 | 7 · -58%* | 15 · -55%* | 24 · -32%* | 36 · -31% | 42 · -30% | 3 · +27%* |
| D | 8 · -63%* | 14 · -69%* | 24 · -42%* | 38 · -27% | 43 · -26% | 2 · -18%* |
| L | 9 · -71%* | 14 · -70%* | 23 · -58%* | 35 · -41% | 39 · -35% | 6 · +65%* |
| D+conf | – | 2 · -100%* | 6 · -49%* | 10 · -56%* | 11 · -45%* | – |
| D+fade | 5 · -41%* | 5 · -41%* | 8 · -32%* | 11 · +6%* | 11 · +6%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 5 · +53%* | 16 · +19%* | 18 · +27%* | 24 · -5%* | 33 · -8% | 5 · +15%* |
| H6 | 6 · +27%* | 15 · +27%* | 20 · +23%* | 26 · +24%* | 33 · +9% | 12 · -52%* |
| D | 4 · -5%* | 14 · +10%* | 20 · +15%* | 30 · +15% | 37 · +3% | 8 · +18%* |
| L | 3 · -37%* | 14 · +9%* | 23 · +8%* | 34 · +7% | 36 · +6% | 9 · +5%* |
| D+conf | 1 · +93%* | 3 · +28%* | 5 · +53%* | 9 · +49%* | 10 · +34%* | 2 · +88%* |
| D+fade | 3 · -38%* | 6 · -36%* | 10 · -24%* | 13 · -27%* | 14 · -32%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 35. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.222 (n=18) | -0.182 (n=22) | +0.000 (n=21) | -0.048 (n=21) | -0.600 (n=5) | +0.125 (n=8) |
| spread · B | +0.476 (n=21) | +0.000 (n=18) | -0.050 (n=20) | +0.143 (n=21) | +0.000 (n=4) | -0.200 (n=5) |
| ml · A | +0.002 (n=17) | -0.004 (n=23) | +0.003 (n=22) | +0.000 (n=22) | +0.000 (n=9) | +0.004 (n=8) |
| ml · B | +0.009 (n=20) | +0.001 (n=24) | +0.001 (n=24) | -0.000 (n=23) | -0.001 (n=6) | +0.003 (n=8) |
| total · T | +1.278 (n=18) | +0.300 (n=20) | -0.150 (n=20) | -0.435 (n=23) | -0.200 (n=5) | -0.200 (n=10) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 38 | -0.495 (-0.68) | – | – | – |
| spread · A · D | 45 | -0.332 (-0.49) | – | – | – |
| spread · B · E | 38 | -0.381 (-0.61) | – | – | – |
| spread · B · D | 45 | -0.313 (-0.48) | – | – | – |
| ml · A · E | 38 | – | 0.2221 | 0.2040 | +0.0181 (1.57) |
| ml · A · D | 45 | – | 0.2253 | 0.2082 | +0.0170 (1.66) |
| ml · B · E | 38 | – | 0.2322 | 0.2040 | +0.0282 (1.98) |
| ml · B · D | 45 | – | 0.2306 | 0.2082 | +0.0223 (1.86) |
| total · T · E | 38 | +0.712 (0.64) | – | – | – |
| total · T · D | 45 | +0.127 (0.15) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._