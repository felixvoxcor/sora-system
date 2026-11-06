# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **55** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 10 · -5%* | 19 · +0%* | 25 · -1%* | 34 · -10% | 40 · -4% | 8 · +20%* |
| H6 | 9 · -58%* | 17 · -10%* | 28 · -11%* | 42 · -9% | 47 · -2% | 8 · -29%* |
| D | 10 · -24%* | 18 · +6%* | 26 · -5%* | 40 · +0% | 49 · +1% | 6 · -38%* |
| L | 10 · -42%* | 17 · -20%* | 26 · -4%* | 38 · +11% | 46 · +4% | 9 · -100%* |
| D+conf | 1 · -100%* | 4 · -4%* | 6 · +29%* | 9 · +8%* | 10 · -3%* | 2 · -100%* |
| D+fade | 6 · +27%* | 9 · +48%* | 11 · +38%* | 15 · +26%* | 15 · +26%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 9 · -15%* | 17 · -10%* | 27 · -8%* | 36 · -10% | 42 · -0% | 6 · -67%* |
| H6 | 10 · -5%* | 15 · -10%* | 24 · -12%* | 47 · -14% | 51 · -14% | 4 · -51%* |
| D | 12 · -20%* | 17 · -9%* | 27 · -1%* | 44 · -9% | 51 · -6% | 4 · -51%* |
| L | 11 · -31%* | 17 · -33%* | 27 · -22%* | 37 · -23% | 48 · -20% | 7 · -46%* |
| D+conf | 2 · -100%* | 3 · -35%* | 5 · +16%* | 12 · -20%* | 12 · -20%* | – |
| D+fade | 4 · +45%* | 5 · +53%* | 9 · +48%* | 13 · +32%* | 14 · +22%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 13 · -26%* | 21 · -27%* | 23 · -23%* | 35 · -16% | 44 · -16% | 4 · +30%* |
| H6 | 10 · -100%* | 21 · -38%* | 29 · -37%* | 45 · -20% | 48 · -18% | 7 · +21%* |
| D | 8 · -100%* | 22 · -40%* | 27 · -32%* | 42 · -13% | 48 · -12% | 7 · -41%* |
| L | 11 · -76%* | 20 · -42%* | 27 · -42%* | 39 · -6% | 45 · -16% | 10 · -0%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 11 · +19%* | 12 · +34%* | 3 · -56%* |
| D+fade | 5 · -100%* | 9 · -39%* | 10 · -45%* | 14 · -13%* | 15 · -19%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 12 · -51%* | 19 · -52%* | 25 · -37%* | 38 · -31% | 42 · -24% | 6 · +42%* |
| H6 | 10 · -52%* | 18 · -52%* | 31 · -36% | 46 · -39% | 52 · -37% | 3 · +27%* |
| D | 11 · -56%* | 19 · -59%* | 30 · -43% | 47 · -34% | 53 · -34% | 2 · -18%* |
| L | 11 · -59%* | 17 · -65%* | 29 · -61%* | 43 · -44% | 49 · -41% | 6 · +65%* |
| D+conf | 1 · -100%* | 3 · -100%* | 7 · -56%* | 11 · -60%* | 12 · -49%* | – |
| D+fade | 6 · -51%* | 6 · -51%* | 10 · -46%* | 14 · -17%* | 14 · -17%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 6 · +60%* | 18 · +17%* | 21 · +18%* | 28 · -11%* | 40 · -5% | 8 · -4%* |
| H6 | 6 · +27%* | 17 · +12%* | 25 · +14%* | 31 · +17% | 39 · +7% | 16 · -52%* |
| D | 4 · -5%* | 16 · +8%* | 24 · +12%* | 36 · +11% | 43 · +2% | 12 · -5%* |
| L | 3 · -37%* | 16 · +8%* | 27 · +6%* | 39 · +3% | 42 · +5% | 13 · -12%* |
| D+conf | 1 · +93%* | 3 · +28%* | 6 · +60%* | 10 · +54%* | 11 · +40%* | 4 · +43%* |
| D+fade | 3 · -38%* | 7 · -18%* | 11 · -13%* | 15 · -11%* | 16 · -17%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 41. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.160 (n=25) | -0.107 (n=28) | +0.000 (n=26) | -0.077 (n=26) | -0.333 (n=6) | +0.091 (n=11) |
| spread · B | +0.296 (n=27) | +0.042 (n=24) | -0.074 (n=27) | +0.074 (n=27) | +0.000 (n=5) | -0.111 (n=9) |
| ml · A | +0.003 (n=23) | -0.001 (n=29) | +0.003 (n=27) | +0.000 (n=27) | +0.000 (n=10) | +0.003 (n=10) |
| ml · B | +0.008 (n=25) | +0.004 (n=31) | +0.001 (n=30) | -0.000 (n=29) | -0.001 (n=7) | +0.003 (n=10) |
| total · T | +1.333 (n=21) | +0.400 (n=25) | -0.083 (n=24) | -0.333 (n=27) | -0.167 (n=6) | -0.182 (n=11) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 48 | -0.257 (-0.43) | – | – | – |
| spread · A · D | 55 | -0.146 (-0.26) | – | – | – |
| spread · B · E | 48 | -0.462 (-0.84) | – | – | – |
| spread · B · D | 55 | -0.398 (-0.70) | – | – | – |
| ml · A · E | 48 | – | 0.2134 | 0.1979 | +0.0156 (1.43) |
| ml · A · D | 55 | – | 0.2172 | 0.2007 | +0.0164 (1.69) |
| ml · B · E | 48 | – | 0.2247 | 0.1979 | +0.0268 (2.18) |
| ml · B · D | 55 | – | 0.2245 | 0.2007 | +0.0237 (2.23) |
| total · T · E | 48 | +0.641 (0.68) | – | – | – |
| total · T · D | 55 | +0.032 (0.04) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._