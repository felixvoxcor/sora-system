# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **54** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 10 · -5%* | 19 · +0%* | 25 · -1%* | 34 · -10% | 39 · -2% | 8 · +20%* |
| H6 | 9 · -58%* | 16 · -5%* | 27 · -8%* | 41 · -7% | 46 · -0% | 8 · -29%* |
| D | 10 · -24%* | 18 · +6%* | 26 · -5%* | 40 · +0% | 49 · +1% | 5 · -25%* |
| L | 10 · -42%* | 17 · -20%* | 26 · -4%* | 38 · +11% | 46 · +4% | 8 · -100%* |
| D+conf | 1 · -100%* | 4 · -4%* | 6 · +29%* | 9 · +8%* | 10 · -3%* | 1 · -100%* |
| D+fade | 6 · +27%* | 9 · +48%* | 11 · +38%* | 15 · +26%* | 15 · +26%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 8 · -4%* | 16 · -4%* | 26 · -5%* | 35 · -7% | 41 · +2% | 6 · -67%* |
| H6 | 9 · +6%* | 14 · -4%* | 23 · -9%* | 46 · -13% | 50 · -12% | 4 · -51%* |
| D | 11 · -12%* | 16 · -4%* | 26 · +3%* | 43 · -7% | 50 · -5% | 4 · -51%* |
| L | 10 · -24%* | 16 · -29%* | 26 · -19%* | 36 · -21% | 47 · -19% | 7 · -46%* |
| D+conf | 1 · -100%* | 2 · -2%* | 4 · +46%* | 11 · -13%* | 11 · -13%* | – |
| D+fade | 4 · +45%* | 5 · +53%* | 9 · +48%* | 13 · +32%* | 14 · +22%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 13 · -26%* | 21 · -27%* | 23 · -23%* | 34 · -13% | 43 · -14% | 4 · +30%* |
| H6 | 10 · -100%* | 20 · -35%* | 28 · -35%* | 44 · -18% | 47 · -16% | 7 · +21%* |
| D | 8 · -100%* | 22 · -40%* | 27 · -32%* | 42 · -13% | 48 · -12% | 6 · -31%* |
| L | 11 · -76%* | 20 · -42%* | 27 · -42%* | 39 · -6% | 45 · -16% | 9 · +11%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 11 · +19%* | 12 · +34%* | 2 · -34%* |
| D+fade | 5 · -100%* | 9 · -39%* | 10 · -45%* | 14 · -13%* | 15 · -19%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 11 · -47%* | 18 · -49%* | 24 · -35%* | 37 · -29% | 41 · -22% | 6 · +42%* |
| H6 | 9 · -46%* | 17 · -49%* | 30 · -34% | 45 · -37% | 51 · -36% | 3 · +27%* |
| D | 10 · -52%* | 18 · -57%* | 29 · -41%* | 46 · -32% | 52 · -33% | 2 · -18%* |
| L | 10 · -55%* | 16 · -62%* | 28 · -59%* | 42 · -43% | 48 · -40% | 6 · +65%* |
| D+conf | – | 2 · -100%* | 6 · -49%* | 10 · -56%* | 11 · -45%* | – |
| D+fade | 6 · -51%* | 6 · -51%* | 10 · -46%* | 14 · -17%* | 14 · -17%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 6 · +60%* | 18 · +17%* | 21 · +18%* | 28 · -11%* | 40 · -5% | 7 · -18%* |
| H6 | 6 · +27%* | 16 · +19%* | 24 · +19%* | 30 · +20% | 38 · +10% | 16 · -52%* |
| D | 4 · -5%* | 16 · +8%* | 24 · +12%* | 35 · +15% | 42 · +5% | 12 · -5%* |
| L | 3 · -37%* | 16 · +8%* | 27 · +6%* | 38 · +6% | 41 · +7% | 13 · -12%* |
| D+conf | 1 · +93%* | 3 · +28%* | 6 · +60%* | 10 · +54%* | 11 · +40%* | 4 · +43%* |
| D+fade | 3 · -38%* | 7 · -18%* | 11 · -13%* | 15 · -11%* | 16 · -17%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 40. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.160 (n=25) | -0.222 (n=27) | +0.000 (n=26) | -0.077 (n=26) | -0.333 (n=6) | +0.091 (n=11) |
| spread · B | +0.269 (n=26) | -0.087 (n=23) | -0.077 (n=26) | +0.077 (n=26) | +0.000 (n=4) | -0.111 (n=9) |
| ml · A | +0.003 (n=23) | -0.005 (n=28) | +0.003 (n=27) | +0.000 (n=27) | +0.000 (n=10) | +0.003 (n=10) |
| ml · B | +0.007 (n=24) | +0.001 (n=30) | +0.001 (n=29) | -0.000 (n=28) | -0.001 (n=6) | +0.003 (n=10) |
| total · T | +1.333 (n=21) | +0.250 (n=24) | -0.083 (n=24) | -0.333 (n=27) | -0.167 (n=6) | -0.182 (n=11) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 47 | -0.215 (-0.36) | – | – | – |
| spread · A · D | 54 | -0.115 (-0.20) | – | – | – |
| spread · B · E | 47 | -0.298 (-0.52) | – | – | – |
| spread · B · D | 54 | -0.224 (-0.38) | – | – | – |
| ml · A · E | 47 | – | 0.2146 | 0.1992 | +0.0154 (1.38) |
| ml · A · D | 54 | – | 0.2182 | 0.2015 | +0.0167 (1.69) |
| ml · B · E | 47 | – | 0.2230 | 0.1992 | +0.0238 (1.96) |
| ml · B · D | 54 | – | 0.2228 | 0.2015 | +0.0213 (2.02) |
| total · T · E | 47 | +0.715 (0.76) | – | – | – |
| total · T · D | 54 | +0.107 (0.14) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._