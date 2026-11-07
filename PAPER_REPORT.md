# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **60** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 11 · -14%* | 20 · -5%* | 27 · -1%* | 36 · -10% | 42 · -4% | 10 · +34%* |
| H6 | 10 · -62%* | 19 · -10%* | 30 · -11% | 45 · -7% | 51 · -3% | 9 · -37%* |
| D | 11 · -31%* | 20 · +5%* | 28 · -5%* | 43 · +2% | 54 · +3% | 6 · -38%* |
| L | 11 · -47%* | 19 · -19%* | 28 · -4%* | 41 · +12% | 51 · +5% | 9 · -100%* |
| D+conf | 1 · -100%* | 4 · -4%* | 6 · +29%* | 9 · +8%* | 10 · -3%* | 2 · -100%* |
| D+fade | 7 · +9%* | 11 · +38%* | 13 · +31%* | 18 · +26%* | 18 · +26%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 11 · -30%* | 19 · -19%* | 31 · -8% | 40 · -9% | 46 · -1% | 6 · -67%* |
| H6 | 12 · -20%* | 19 · -10%* | 28 · -12%* | 51 · -14% | 56 · -15% | 4 · -51%* |
| D | 13 · -26%* | 20 · -13%* | 31 · -1% | 48 · -9% | 55 · -6% | 5 · -23%* |
| L | 12 · -37%* | 21 · -27%* | 31 · -20% | 41 · -21% | 52 · -19% | 8 · -29%* |
| D+conf | 2 · -100%* | 3 · -35%* | 5 · +16%* | 12 · -20%* | 12 · -20%* | – |
| D+fade | 5 · +16%* | 8 · +20%* | 13 · +32%* | 17 · +23%* | 18 · +16%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 14 · -32%* | 22 · -30%* | 25 · -21%* | 38 · -13% | 47 · -14% | 5 · +36%* |
| H6 | 11 · -100%* | 23 · -34%* | 31 · -34% | 47 · -18% | 51 · -15% | 9 · +12%* |
| D | 9 · -100%* | 24 · -36%* | 29 · -29%* | 45 · -10% | 52 · -12% | 8 · -48%* |
| L | 13 · -62%* | 22 · -37%* | 29 · -38%* | 42 · -4% | 49 · -15% | 11 · -9%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 11 · +19%* | 12 · +34%* | 3 · -56%* |
| D+fade | 6 · -100%* | 11 · -30%* | 12 · -36%* | 16 · -10%* | 17 · -15%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 14 · -58%* | 21 · -56%* | 28 · -39%* | 42 · -29% | 46 · -23% | 6 · +42%* |
| H6 | 12 · -60%* | 21 · -48%* | 35 · -33% | 50 · -36% | 56 · -35% | 4 · +29%* |
| D | 12 · -60%* | 22 · -55%* | 34 · -39% | 51 · -32% | 58 · -33% | 2 · -18%* |
| L | 13 · -48%* | 21 · -54%* | 33 · -54% | 47 · -41% | 53 · -39% | 7 · +41%* |
| D+conf | 1 · -100%* | 3 · -100%* | 7 · -56%* | 11 · -60%* | 12 · -49%* | – |
| D+fade | 7 · -58%* | 9 · -42%* | 13 · -41%* | 17 · -18%* | 17 · -18%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 7 · +37%* | 19 · +10%* | 23 · +16%* | 30 · -11% | 44 · -9% | 8 · -4%* |
| H6 | 7 · +9%* | 19 · +0%* | 29 · +11%* | 35 · +14% | 44 · +4% | 16 · -52%* |
| D | 5 · -24%* | 18 · +6%* | 28 · +9%* | 41 · +7% | 48 · -1% | 12 · -5%* |
| L | 3 · -37%* | 19 · +1%* | 31 · +5% | 43 · +2% | 46 · +4% | 14 · -19%* |
| D+conf | 2 · -4%* | 4 · -4%* | 7 · +37%* | 11 · +40%* | 12 · +28%* | 4 · +43%* |
| D+fade | 3 · -38%* | 8 · -5%* | 14 · -5%* | 18 · -5%* | 19 · -10%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 49. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.037 (n=27) | -0.167 (n=30) | +0.000 (n=28) | -0.071 (n=28) | -0.333 (n=6) | +0.077 (n=13) |
| spread · B | +0.129 (n=31) | +0.000 (n=28) | -0.032 (n=31) | +0.097 (n=31) | +0.000 (n=5) | +0.000 (n=13) |
| ml · A | -0.000 (n=25) | -0.003 (n=31) | +0.002 (n=29) | +0.000 (n=29) | +0.000 (n=10) | +0.001 (n=12) |
| ml · B | +0.006 (n=28) | +0.002 (n=35) | +0.000 (n=34) | -0.000 (n=33) | -0.001 (n=7) | +0.001 (n=13) |
| total · T | +1.261 (n=23) | +0.448 (n=29) | +0.000 (n=28) | -0.194 (n=31) | +0.000 (n=7) | -0.071 (n=14) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 52 | -0.447 (-0.70) | – | – | – |
| spread · A · D | 60 | -0.339 (-0.59) | – | – | – |
| spread · B · E | 52 | -0.784 (-1.36) | – | – | – |
| spread · B · D | 60 | -0.609 (-1.04) | – | – | – |
| ml · A · E | 52 | – | 0.2092 | 0.1943 | +0.0149 (1.43) |
| ml · A · D | 60 | – | 0.2110 | 0.1957 | +0.0153 (1.64) |
| ml · B · E | 52 | – | 0.2215 | 0.1943 | +0.0272 (2.32) |
| ml · B · D | 60 | – | 0.2183 | 0.1957 | +0.0226 (2.23) |
| total · T · E | 52 | +0.319 (0.41) | – | – | – |
| total · T · D | 60 | -0.085 (-0.12) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._