# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **62** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 11 · -14%* | 20 · -5%* | 28 · -4%* | 38 · -14% | 44 · -9% | 10 · +34%* |
| H6 | 10 · -62%* | 19 · -10%* | 30 · -11% | 45 · -7% | 52 · -1% | 10 · -24%* |
| D | 11 · -31%* | 20 · +5%* | 28 · -5%* | 43 · +2% | 55 · +4% | 7 · -19%* |
| L | 11 · -47%* | 19 · -19%* | 28 · -4%* | 42 · +14% | 52 · +6% | 10 · -81%* |
| D+conf | 1 · -100%* | 4 · -4%* | 6 · +29%* | 9 · +8%* | 10 · -3%* | 2 · -100%* |
| D+fade | 7 · +9%* | 11 · +38%* | 13 · +31%* | 18 · +26%* | 18 · +26%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 13 · -41%* | 21 · -27%* | 33 · -13% | 42 · -14% | 48 · -5% | 6 · -67%* |
| H6 | 12 · -20%* | 19 · -10%* | 30 · -17% | 53 · -17% | 58 · -18% | 4 · -51%* |
| D | 13 · -26%* | 22 · -21%* | 33 · -7% | 50 · -12% | 57 · -10% | 5 · -23%* |
| L | 13 · -42%* | 23 · -34%* | 33 · -25% | 43 · -25% | 54 · -22% | 8 · -29%* |
| D+conf | 2 · -100%* | 5 · -61%* | 7 · -17%* | 14 · -31%* | 14 · -31%* | – |
| D+fade | 5 · +16%* | 8 · +20%* | 13 · +32%* | 17 · +23%* | 18 · +16%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 14 · -32%* | 22 · -30%* | 25 · -21%* | 39 · -15% | 49 · -17% | 5 · +36%* |
| H6 | 11 · -100%* | 23 · -34%* | 31 · -34% | 47 · -18% | 51 · -15% | 11 · +20%* |
| D | 9 · -100%* | 24 · -36%* | 29 · -29%* | 45 · -10% | 53 · -11% | 9 · -36%* |
| L | 13 · -62%* | 22 · -37%* | 29 · -38%* | 43 · -3% | 50 · -14% | 12 · -4%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 11 · +19%* | 12 · +34%* | 3 · -56%* |
| D+fade | 6 · -100%* | 11 · -30%* | 12 · -36%* | 16 · -10%* | 17 · -15%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 14 · -58%* | 23 · -60%* | 30 · -43% | 44 · -33% | 48 · -27% | 6 · +42%* |
| H6 | 12 · -60%* | 21 · -48%* | 37 · -37% | 52 · -39% | 58 · -37% | 4 · +29%* |
| D | 12 · -60%* | 23 · -57%* | 36 · -42% | 53 · -34% | 60 · -35% | 2 · -18%* |
| L | 14 · -52%* | 23 · -58%* | 35 · -57% | 49 · -44% | 55 · -41% | 7 · +41%* |
| D+conf | 1 · -100%* | 4 · -100%* | 9 · -66%* | 13 · -66%* | 14 · -57%* | – |
| D+fade | 7 · -58%* | 9 · -42%* | 13 · -41%* | 17 · -18%* | 17 · -18%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 7 · +37%* | 20 · +14%* | 24 · +19%* | 32 · -11% | 46 · -9% | 8 · -4%* |
| H6 | 7 · +9%* | 19 · +0%* | 29 · +11%* | 36 · +16% | 46 · +3% | 16 · -52%* |
| D | 5 · -24%* | 18 · +6%* | 28 · +9%* | 41 · +7% | 50 · -1% | 12 · -5%* |
| L | 3 · -37%* | 19 · +1%* | 31 · +5% | 43 · +2% | 48 · +3% | 14 · -19%* |
| D+conf | 2 · -4%* | 4 · -4%* | 7 · +37%* | 11 · +40%* | 14 · +24%* | 4 · +43%* |
| D+fade | 3 · -38%* | 8 · -5%* | 14 · -5%* | 18 · -5%* | 19 · -10%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 51. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.179 (n=28) | -0.167 (n=30) | +0.000 (n=28) | -0.071 (n=28) | -0.333 (n=6) | +0.077 (n=13) |
| spread · B | +0.303 (n=33) | +0.033 (n=30) | +0.000 (n=33) | +0.091 (n=33) | +0.143 (n=7) | +0.000 (n=13) |
| ml · A | -0.000 (n=25) | -0.003 (n=31) | +0.002 (n=29) | +0.000 (n=29) | +0.000 (n=10) | +0.001 (n=12) |
| ml · B | +0.009 (n=30) | +0.003 (n=37) | +0.001 (n=36) | -0.000 (n=35) | +0.002 (n=9) | +0.001 (n=13) |
| total · T | +1.333 (n=24) | +0.448 (n=29) | +0.000 (n=28) | -0.194 (n=31) | +0.000 (n=7) | -0.071 (n=14) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 54 | -0.470 (-0.76) | – | – | – |
| spread · A · D | 62 | -0.306 (-0.54) | – | – | – |
| spread · B · E | 54 | -0.794 (-1.44) | – | – | – |
| spread · B · D | 62 | -0.642 (-1.13) | – | – | – |
| ml · A · E | 54 | – | 0.2067 | 0.1917 | +0.0150 (1.50) |
| ml · A · D | 62 | – | 0.2088 | 0.1943 | +0.0145 (1.60) |
| ml · B · E | 54 | – | 0.2205 | 0.1917 | +0.0288 (2.54) |
| ml · B · D | 62 | – | 0.2188 | 0.1943 | +0.0245 (2.48) |
| total · T · E | 54 | +0.293 (0.39) | – | – | – |
| total · T · D | 62 | -0.097 (-0.14) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._