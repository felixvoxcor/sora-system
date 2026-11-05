# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **49** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 8 · -5%* | 17 · +1%* | 22 · +4%* | 31 · -7% | 35 · -2% | 7 · +9%* |
| H6 | 7 · -73%* | 14 · -5%* | 25 · -8%* | 37 · -7% | 41 · -2% | 8 · -29%* |
| D | 8 · -29%* | 16 · +7%* | 24 · -5%* | 36 · +1% | 44 · -0% | 5 · -25%* |
| L | 8 · -52%* | 15 · -23%* | 24 · -4%* | 34 · +12% | 41 · +2% | 8 · -100%* |
| D+conf | 1 · -100%* | 4 · -4%* | 6 · +29%* | 8 · +21%* | 9 · +8%* | 1 · -100%* |
| D+fade | 4 · +42%* | 7 · +62%* | 9 · +47%* | 12 · +26%* | 12 · +26%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 7 · -18%* | 14 · -18%* | 23 · -9%* | 31 · -14% | 37 · -2% | 5 · -61%* |
| H6 | 7 · -20%* | 12 · -21%* | 20 · -24%* | 41 · -16% | 45 · -15% | 4 · -51%* |
| D | 9 · -36%* | 14 · -18%* | 23 · -9%* | 39 · -12% | 45 · -7% | 4 · -51%* |
| L | 9 · -37%* | 14 · -46%* | 23 · -34%* | 33 · -31% | 42 · -23% | 7 · -46%* |
| D+conf | 1 · -100%* | 2 · -2%* | 4 · +46%* | 10 · -4%* | 10 · -4%* | – |
| D+fade | 3 · +28%* | 4 · +43%* | 7 · +36%* | 11 · +21%* | 11 · +21%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 11 · -13%* | 19 · -19%* | 21 · -16%* | 30 · -8% | 38 · -7% | 4 · +30%* |
| H6 | 8 · -100%* | 18 · -28%* | 26 · -30%* | 39 · -12% | 42 · -10% | 7 · +21%* |
| D | 6 · -100%* | 20 · -34%* | 25 · -26%* | 37 · -6% | 43 · -6% | 6 · -31%* |
| L | 9 · -71%* | 18 · -35%* | 25 · -37%* | 34 · +2% | 40 · -10% | 9 · +11%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 11 · +19%* | 12 · +34%* | 2 · -34%* |
| D+fade | 3 · -100%* | 7 · -22%* | 8 · -31%* | 11 · +11%* | 12 · +1%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 10 · -60%* | 16 · -54%* | 22 · -37%* | 32 · -24% | 36 · -17% | 6 · +42%* |
| H6 | 7 · -58%* | 15 · -55%* | 26 · -31%* | 40 · -34% | 46 · -33% | 3 · +27%* |
| D | 8 · -63%* | 16 · -63%* | 26 · -41%* | 41 · -29% | 47 · -29% | 2 · -18%* |
| L | 9 · -71%* | 14 · -70%* | 25 · -62%* | 38 · -42% | 43 · -37% | 6 · +65%* |
| D+conf | – | 2 · -100%* | 6 · -49%* | 10 · -56%* | 11 · -45%* | – |
| D+fade | 5 · -41%* | 5 · -41%* | 8 · -32%* | 11 · +6%* | 11 · +6%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 5 · +53%* | 16 · +19%* | 19 · +20%* | 26 · -12%* | 36 · -10% | 6 · -5%* |
| H6 | 6 · +27%* | 15 · +27%* | 22 · +21%* | 28 · +22%* | 36 · +11% | 13 · -56%* |
| D | 4 · -5%* | 15 · +15%* | 22 · +13%* | 33 · +16% | 40 · +5% | 9 · +5%* |
| L | 3 · -37%* | 15 · +15%* | 25 · +7%* | 36 · +6% | 39 · +8% | 10 · -6%* |
| D+conf | 1 · +93%* | 3 · +28%* | 5 · +53%* | 9 · +49%* | 10 · +34%* | 3 · +25%* |
| D+fade | 3 · -38%* | 7 · -18%* | 11 · -13%* | 15 · -11%* | 16 · -17%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 38. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.318 (n=22) | -0.200 (n=25) | +0.042 (n=24) | -0.042 (n=24) | -0.333 (n=6) | +0.222 (n=9) |
| spread · B | +0.391 (n=23) | -0.050 (n=20) | -0.043 (n=23) | +0.130 (n=23) | +0.000 (n=4) | +0.000 (n=7) |
| ml · A | +0.005 (n=21) | -0.005 (n=26) | +0.003 (n=25) | +0.000 (n=25) | +0.000 (n=10) | +0.004 (n=8) |
| ml · B | +0.008 (n=22) | -0.001 (n=26) | +0.001 (n=26) | -0.000 (n=25) | -0.001 (n=6) | +0.003 (n=8) |
| total · T | +1.263 (n=19) | +0.273 (n=22) | -0.091 (n=22) | -0.360 (n=25) | -0.200 (n=5) | -0.182 (n=11) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 42 | -0.240 (-0.35) | – | – | – |
| spread · A · D | 49 | -0.217 (-0.34) | – | – | – |
| spread · B · E | 42 | -0.411 (-0.67) | – | – | – |
| spread · B · D | 49 | -0.408 (-0.65) | – | – | – |
| ml · A · E | 42 | – | 0.2196 | 0.2082 | +0.0113 (0.97) |
| ml · A · D | 49 | – | 0.2228 | 0.2100 | +0.0128 (1.27) |
| ml · B · E | 42 | – | 0.2337 | 0.2082 | +0.0255 (1.94) |
| ml · B · D | 49 | – | 0.2324 | 0.2100 | +0.0224 (2.00) |
| total · T · E | 42 | +0.759 (0.74) | – | – | – |
| total · T · D | 49 | +0.230 (0.29) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._