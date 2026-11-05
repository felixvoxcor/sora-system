# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **50** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 8 · -5%* | 17 · +1%* | 23 · -0%* | 32 · -10% | 36 · -4% | 7 · +9%* |
| H6 | 7 · -73%* | 14 · -5%* | 25 · -8%* | 38 · -10% | 42 · -5% | 8 · -29%* |
| D | 8 · -29%* | 16 · +7%* | 24 · -5%* | 37 · -2% | 45 · -3% | 5 · -25%* |
| L | 8 · -52%* | 15 · -23%* | 24 · -4%* | 35 · +9% | 42 · -0% | 8 · -100%* |
| D+conf | 1 · -100%* | 4 · -4%* | 6 · +29%* | 9 · +8%* | 10 · -3%* | 1 · -100%* |
| D+fade | 4 · +42%* | 7 · +62%* | 9 · +47%* | 12 · +26%* | 12 · +26%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 7 · -18%* | 14 · -18%* | 24 · -13%* | 32 · -16% | 38 · -5% | 5 · -61%* |
| H6 | 7 · -20%* | 12 · -21%* | 20 · -24%* | 42 · -18% | 46 · -17% | 4 · -51%* |
| D | 9 · -36%* | 14 · -18%* | 23 · -9%* | 40 · -14% | 46 · -9% | 4 · -51%* |
| L | 9 · -37%* | 14 · -46%* | 23 · -34%* | 33 · -31% | 43 · -25% | 7 · -46%* |
| D+conf | 1 · -100%* | 2 · -2%* | 4 · +46%* | 11 · -13%* | 11 · -13%* | – |
| D+fade | 3 · +28%* | 4 · +43%* | 7 · +36%* | 11 · +21%* | 11 · +21%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 11 · -13%* | 19 · -19%* | 21 · -16%* | 31 · -11% | 39 · -9% | 4 · +30%* |
| H6 | 8 · -100%* | 18 · -28%* | 26 · -30%* | 40 · -14% | 43 · -12% | 7 · +21%* |
| D | 6 · -100%* | 20 · -34%* | 25 · -26%* | 38 · -8% | 44 · -9% | 6 · -31%* |
| L | 9 · -71%* | 18 · -35%* | 25 · -37%* | 35 · -1% | 41 · -12% | 9 · +11%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 11 · +19%* | 12 · +34%* | 2 · -34%* |
| D+fade | 3 · -100%* | 7 · -22%* | 8 · -31%* | 11 · +11%* | 12 · +1%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 10 · -60%* | 16 · -54%* | 22 · -37%* | 33 · -26% | 37 · -19% | 6 · +42%* |
| H6 | 7 · -58%* | 15 · -55%* | 27 · -34%* | 41 · -36% | 47 · -34% | 3 · +27%* |
| D | 8 · -63%* | 16 · -63%* | 26 · -41%* | 42 · -30% | 48 · -31% | 2 · -18%* |
| L | 9 · -71%* | 14 · -70%* | 25 · -62%* | 38 · -42% | 44 · -39% | 6 · +65%* |
| D+conf | – | 2 · -100%* | 6 · -49%* | 10 · -56%* | 11 · -45%* | – |
| D+fade | 5 · -41%* | 5 · -41%* | 8 · -32%* | 11 · +6%* | 11 · +6%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 5 · +53%* | 17 · +12%* | 20 · +14%* | 27 · -15%* | 37 · -12% | 6 · -5%* |
| H6 | 6 · +27%* | 16 · +19%* | 23 · +16%* | 29 · +18%* | 37 · +8% | 13 · -56%* |
| D | 4 · -5%* | 16 · +8%* | 23 · +8%* | 34 · +12% | 41 · +2% | 9 · +5%* |
| L | 3 · -37%* | 16 · +8%* | 26 · +3%* | 37 · +4% | 40 · +5% | 10 · -6%* |
| D+conf | 1 · +93%* | 3 · +28%* | 5 · +53%* | 9 · +49%* | 10 · +34%* | 3 · +25%* |
| D+fade | 3 · -38%* | 7 · -18%* | 11 · -13%* | 15 · -11%* | 16 · -17%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 38. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.304 (n=23) | -0.200 (n=25) | +0.042 (n=24) | -0.042 (n=24) | -0.333 (n=6) | +0.222 (n=9) |
| spread · B | +0.375 (n=24) | -0.050 (n=20) | -0.043 (n=23) | +0.130 (n=23) | +0.000 (n=4) | +0.000 (n=7) |
| ml · A | +0.005 (n=21) | -0.005 (n=26) | +0.003 (n=25) | +0.000 (n=25) | +0.000 (n=10) | +0.004 (n=8) |
| ml · B | +0.008 (n=22) | +0.000 (n=27) | +0.001 (n=26) | -0.000 (n=25) | -0.001 (n=6) | +0.003 (n=8) |
| total · T | +1.200 (n=20) | +0.261 (n=23) | -0.087 (n=23) | -0.346 (n=26) | -0.200 (n=5) | -0.182 (n=11) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 43 | -0.296 (-0.44) | – | – | – |
| spread · A · D | 50 | -0.230 (-0.37) | – | – | – |
| spread · B · E | 43 | -0.461 (-0.76) | – | – | – |
| spread · B · D | 50 | -0.425 (-0.68) | – | – | – |
| ml · A · E | 43 | – | 0.2195 | 0.2077 | +0.0118 (1.04) |
| ml · A · D | 50 | – | 0.2227 | 0.2094 | +0.0133 (1.33) |
| ml · B · E | 43 | – | 0.2337 | 0.2077 | +0.0260 (2.03) |
| ml · B · D | 50 | – | 0.2323 | 0.2094 | +0.0228 (2.08) |
| total · T · E | 43 | +0.583 (0.57) | – | – | – |
| total · T · D | 50 | +0.068 (0.09) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._