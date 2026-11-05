# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **40** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 7 · -18%* | 13 · -12%* | 17 · +2%* | 24 · -12%* | 26 · -11%* | 7 · +9%* |
| H6 | 7 · -73%* | 12 · -5%* | 21 · -9%* | 30 · -11% | 33 · -8% | 7 · -19%* |
| D | 7 · -46%* | 13 · +2%* | 20 · -5%* | 29 · -2%* | 35 · -8% | 5 · -25%* |
| L | 8 · -52%* | 12 · -20%* | 20 · -4%* | 27 · +6%* | 34 · -5% | 6 · -100%* |
| D+conf | 1 · -100%* | 3 · -35%* | 5 · +17%* | 6 · -2%* | 7 · -16%* | 1 · -100%* |
| D+fade | 3 · +26%* | 6 · +58%* | 8 · +42%* | 11 · +20%* | 11 · +20%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 6 · -4%* | 12 · -20%* | 18 · -15%* | 24 · -20%* | 29 · -8%* | 4 · -51%* |
| H6 | 6 · -6%* | 10 · -24%* | 15 · -24%* | 32 · -17% | 36 · -16% | 4 · -51%* |
| D | 7 · -45%* | 11 · -30%* | 18 · -4%* | 32 · -11% | 37 · -2% | 3 · -35%* |
| L | 7 · -45%* | 11 · -48%* | 19 · -30%* | 26 · -27%* | 34 · -22% | 6 · -67%* |
| D+conf | 1 · -100%* | 2 · -2%* | 4 · +46%* | 10 · -4%* | 10 · -4%* | – |
| D+fade | 3 · +28%* | 3 · +28%* | 5 · +52%* | 9 · +26%* | 9 · +26%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 9 · -32%* | 14 · -38%* | 16 · -31%* | 24 · -26%* | 31 · -22% | 2 · -9%* |
| H6 | 8 · -100%* | 15 · -35%* | 22 · -38%* | 33 · -23% | 35 · -21% | 5 · -10%* |
| D | 6 · -100%* | 16 · -47%* | 21 · -35%* | 31 · -16% | 34 · -23% | 6 · -31%* |
| L | 8 · -67%* | 14 · -51%* | 21 · -48%* | 28 · -7%* | 33 · -21% | 7 · -15%* |
| D+conf | – | 4 · -26%* | 8 · +2%* | 8 · +2%* | 8 · +2%* | 2 · -34%* |
| D+fade | 3 · -100%* | 7 · -22%* | 8 · -31%* | 10 · -3%* | 11 · -11%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 9 · -56%* | 12 · -52%* | 16 · -37%* | 25 · -22%* | 28 · -17%* | 5 · +2%* |
| H6 | 6 · -51%* | 12 · -64%* | 20 · -30%* | 31 · -31% | 37 · -30% | 3 · +27%* |
| D | 6 · -51%* | 12 · -64%* | 21 · -34%* | 34 · -25% | 38 · -23% | 2 · -18%* |
| L | 7 · -62%* | 12 · -65%* | 20 · -52%* | 31 · -41% | 34 · -32% | 6 · +65%* |
| D+conf | – | 2 · -100%* | 5 · -39%* | 9 · -51%* | 10 · -39%* | – |
| D+fade | 4 · -26%* | 4 · -26%* | 7 · -23%* | 9 · +3%* | 9 · +3%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 5 · +53%* | 15 · +27%* | 17 · +35%* | 22 · +4%* | 29 · +5%* | 4 · -5%* |
| H6 | 5 · +52%* | 13 · +32%* | 17 · +34%* | 23 · +32%* | 29 · +18%* | 11 · -48%* |
| D | 3 · +27%* | 12 · +12%* | 17 · +24%* | 26 · +25%* | 32 · +13% | 8 · +18%* |
| L | 2 · -6%* | 12 · +12%* | 20 · +15%* | 30 · +15% | 31 · +17% | 9 · +5%* |
| D+conf | 1 · +93%* | 3 · +28%* | 5 · +53%* | 9 · +49%* | 10 · +34%* | 2 · +88%* |
| D+fade | 2 · -7%* | 4 · -53%* | 7 · -19%* | 9 · -16%* | 10 · -24%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 24. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.235 (n=17) | -0.190 (n=21) | +0.000 (n=20) | -0.050 (n=20) | -0.600 (n=5) | +0.125 (n=8) |
| spread · B | +0.667 (n=18) | +0.067 (n=15) | +0.056 (n=18) | +0.158 (n=19) | +0.000 (n=4) | -0.200 (n=5) |
| ml · A | +0.000 (n=16) | -0.004 (n=22) | +0.004 (n=21) | +0.000 (n=21) | +0.001 (n=8) | +0.004 (n=8) |
| ml · B | +0.015 (n=16) | +0.002 (n=20) | +0.002 (n=21) | -0.000 (n=20) | +0.001 (n=5) | +0.005 (n=7) |
| total · T | +1.412 (n=17) | +0.412 (n=17) | -0.118 (n=17) | -0.450 (n=20) | -0.200 (n=5) | -0.143 (n=7) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 33 | -0.525 (-0.69) | – | – | – |
| spread · A · D | 40 | -0.336 (-0.48) | – | – | – |
| spread · B · E | 33 | -0.441 (-0.65) | – | – | – |
| spread · B · D | 40 | -0.230 (-0.33) | – | – | – |
| ml · A · E | 33 | – | 0.2174 | 0.1999 | +0.0175 (1.42) |
| ml · A · D | 40 | – | 0.2217 | 0.2040 | +0.0177 (1.61) |
| ml · B · E | 33 | – | 0.2259 | 0.1999 | +0.0261 (1.70) |
| ml · B · D | 40 | – | 0.2225 | 0.2040 | +0.0185 (1.47) |
| total · T · E | 33 | +1.099 (0.90) | – | – | – |
| total · T · D | 40 | +0.486 (0.51) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._