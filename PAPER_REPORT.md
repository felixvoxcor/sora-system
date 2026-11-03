# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **39** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 7 · -18%* | 13 · -12%* | 17 · +2%* | 24 · -12%* | 26 · -11%* | 6 · +27%* |
| H6 | 7 · -73%* | 12 · -5%* | 21 · -9%* | 29 · -8%* | 32 · -5% | 7 · -19%* |
| D | 7 · -46%* | 13 · +2%* | 20 · -5%* | 28 · +2%* | 34 · -5% | 5 · -25%* |
| L | 8 · -52%* | 12 · -20%* | 20 · -4%* | 27 · +6%* | 34 · -5% | 5 · -100%* |
| D+conf | 1 · -100%* | 3 · -35%* | 5 · +17%* | 6 · -2%* | 7 · -16%* | 1 · -100%* |
| D+fade | 3 · +26%* | 6 · +58%* | 8 · +42%* | 10 · +32%* | 10 · +32%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 6 · -4%* | 12 · -20%* | 17 · -21%* | 23 · -25%* | 28 · -11%* | 4 · -51%* |
| H6 | 6 · -6%* | 10 · -24%* | 15 · -24%* | 31 · -20% | 35 · -19% | 4 · -51%* |
| D | 7 · -45%* | 11 · -30%* | 18 · -4%* | 31 · -14% | 36 · -5% | 3 · -35%* |
| L | 7 · -45%* | 11 · -48%* | 19 · -30%* | 26 · -27%* | 33 · -19% | 6 · -67%* |
| D+conf | 1 · -100%* | 2 · -2%* | 4 · +46%* | 9 · -14%* | 9 · -14%* | – |
| D+fade | 3 · +28%* | 3 · +28%* | 5 · +52%* | 9 · +26%* | 9 · +26%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 9 · -32%* | 14 · -38%* | 16 · -31%* | 24 · -26%* | 31 · -22% | 1 · -100%* |
| H6 | 8 · -100%* | 15 · -35%* | 22 · -38%* | 32 · -20% | 34 · -18% | 5 · -10%* |
| D | 6 · -100%* | 16 · -47%* | 21 · -35%* | 30 · -13% | 33 · -21% | 6 · -31%* |
| L | 8 · -67%* | 14 · -51%* | 21 · -48%* | 28 · -7%* | 33 · -21% | 6 · -31%* |
| D+conf | – | 4 · -26%* | 8 · +2%* | 8 · +2%* | 8 · +2%* | 2 · -34%* |
| D+fade | 3 · -100%* | 7 · -22%* | 8 · -31%* | 10 · -3%* | 11 · -11%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 9 · -56%* | 11 · -64%* | 15 · -45%* | 24 · -26%* | 27 · -21%* | 5 · +2%* |
| H6 | 6 · -51%* | 12 · -64%* | 20 · -30%* | 31 · -31% | 36 · -33% | 3 · +27%* |
| D | 6 · -51%* | 12 · -64%* | 21 · -34%* | 34 · -25% | 37 · -25% | 2 · -18%* |
| L | 7 · -62%* | 12 · -65%* | 20 · -52%* | 31 · -41% | 34 · -32% | 5 · +98%* |
| D+conf | – | 2 · -100%* | 5 · -39%* | 9 · -51%* | 9 · -51%* | – |
| D+fade | 4 · -26%* | 4 · -26%* | 7 · -23%* | 9 · +3%* | 9 · +3%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 4 · +44%* | 14 · +23%* | 16 · +31%* | 21 · -0%* | 28 · +2%* | 4 · -5%* |
| H6 | 5 · +52%* | 12 · +27%* | 16 · +30%* | 22 · +29%* | 28 · +15%* | 11 · -48%* |
| D | 3 · +27%* | 12 · +12%* | 16 · +19%* | 25 · +22%* | 31 · +11% | 8 · +18%* |
| L | 2 · -6%* | 12 · +12%* | 20 · +15%* | 29 · +12%* | 30 · +15% | 9 · +5%* |
| D+conf | 1 · +93%* | 3 · +28%* | 4 · +43%* | 8 · +44%* | 9 · +28%* | 2 · +88%* |
| D+fade | 2 · -7%* | 4 · -53%* | 7 · -19%* | 9 · -16%* | 10 · -24%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 22. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.235 (n=17) | -0.190 (n=21) | +0.000 (n=20) | -0.050 (n=20) | -0.600 (n=5) | +0.125 (n=8) |
| spread · B | +0.706 (n=17) | +0.067 (n=15) | +0.056 (n=18) | +0.158 (n=19) | +0.000 (n=4) | -0.200 (n=5) |
| ml · A | +0.000 (n=16) | -0.004 (n=22) | +0.004 (n=21) | +0.000 (n=21) | +0.001 (n=8) | +0.004 (n=8) |
| ml · B | +0.015 (n=15) | +0.002 (n=20) | +0.002 (n=21) | -0.000 (n=20) | +0.001 (n=5) | +0.005 (n=7) |
| total · T | +1.188 (n=16) | +0.250 (n=16) | -0.188 (n=16) | -0.450 (n=20) | -0.500 (n=4) | -0.143 (n=7) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 32 | -0.512 (-0.67) | – | – | – |
| spread · A · D | 39 | -0.322 (-0.46) | – | – | – |
| spread · B · E | 32 | -0.564 (-0.83) | – | – | – |
| spread · B · D | 39 | -0.306 (-0.43) | – | – | – |
| ml · A · E | 32 | – | 0.2175 | 0.1991 | +0.0184 (1.45) |
| ml · A · D | 39 | – | 0.2219 | 0.2048 | +0.0171 (1.52) |
| ml · B · E | 32 | – | 0.2285 | 0.1991 | +0.0294 (1.91) |
| ml · B · D | 39 | – | 0.2242 | 0.2048 | +0.0194 (1.50) |
| total · T · E | 32 | +1.094 (0.85) | – | – | – |
| total · T · D | 39 | +0.483 (0.50) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._