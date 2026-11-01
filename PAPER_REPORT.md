# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **16** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 2 · -5%* | 4 · -52%* | 7 · -18%* | 8 · -28%* | 9 · -15%* | 2 · -100%* |
| H6 | 2 · -100%* | 5 · +15%* | 8 · -28%* | 10 · -24%* | 12 · -5%* | 4 · -100%* |
| D | 2 · -100%* | 5 · +16%* | 8 · -28%* | 11 · -13%* | 13 · +3%* | 3 · -100%* |
| L | 2 · -100%* | 5 · -24%* | 8 · -29%* | 10 · -6%* | 12 · +10%* | 4 · -100%* |
| D+conf | – | 1 · +95%* | 1 · +95%* | 1 · +95%* | 1 · +95%* | 1 · -100%* |
| D+fade | 1 · -100%* | 3 · +28%* | 3 · +28%* | 3 · +28%* | 3 · +28%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 2 · -5%* | 7 · -18%* | 8 · -28%* | 8 · -28%* | 10 · -4%* | 1 · +95%* |
| H6 | 3 · +25%* | 5 · +14%* | 8 · -5%* | 14 · -19%* | 15 · -25%* | 1 · +95%* |
| D | 3 · -36%* | 6 · -3%* | 9 · -14%* | 13 · +3%* | 14 · +9%* | 2 · -100%* |
| L | 3 · -38%* | 5 · -25%* | 8 · -29%* | 9 · -37%* | 14 · -5%* | 2 · -100%* |
| D+conf | – | 1 · +95%* | 2 · +93%* | 3 · +29%* | 3 · +29%* | – |
| D+fade | 1 · +93%* | 1 · +93%* | 1 · +93%* | 3 · +89%* | 3 · +89%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 1 · -100%* | 3 · -100%* | 5 · -54%* | 8 · -21%* | 10 · -37%* | 1 · -100%* |
| H6 | 4 · -100%* | 6 · -9%* | 8 · -32%* | 11 · -33%* | 12 · -20%* | 4 · -30%* |
| D | 2 · -100%* | 7 · -22%* | 7 · -22%* | 11 · +9%* | 13 · -8%* | 3 · +37%* |
| L | 3 · -12%* | 5 · -47%* | 7 · -62%* | 11 · +7%* | 12 · -2%* | 4 · +3%* |
| D+conf | – | – | – | – | – | 1 · +32%* |
| D+fade | 1 · -100%* | 4 · +37%* | 4 · +37%* | 4 · +37%* | 5 · +10%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 5 · -20%* | 6 · -33%* | 7 · -43%* | 9 · -40%* | 10 · -32%* | 1 · +130%* |
| H6 | 3 · -2%* | 7 · -38%* | 9 · -37%* | 12 · -16%* | 16 · -29%* | – |
| D | 3 · -2%* | 7 · -38%* | 9 · -37%* | 13 · -12%* | 15 · -8%* | 1 · -100%* |
| L | 4 · -34%* | 6 · -56%* | 8 · -51%* | 12 · -52%* | 14 · -24%* | 2 · +101%* |
| D+conf | – | 1 · -100%* | 2 · -34%* | 4 · -33%* | 4 · -33%* | – |
| D+fade | 2 · +48%* | 2 · +48%* | 2 · +48%* | 3 · +83%* | 3 · +83%* | – |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 2 · +92%* | 5 · +14%* | 6 · +27%* | 8 · -4%* | 10 · -5%* | 1 · +91%* |
| H6 | 3 · +27%* | 8 · +19%* | 10 · +14%* | 12 · +11%* | 14 · +22%* | 2 · -100%* |
| D | 2 · -7%* | 8 · +19%* | 10 · +14%* | 12 · +11%* | 13 · +17%* | 3 · +89%* |
| L | 1 · -100%* | 8 · +20%* | 10 · +15%* | 13 · +18%* | 13 · +18%* | 3 · +26%* |
| D+conf | – | 1 · +91%* | 1 · +91%* | 1 · +91%* | 1 · +91%* | 1 · +87%* |
| D+fade | 2 · -7%* | 3 · -38%* | 5 · -25%* | 5 · -25%* | 5 · -25%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Ninguna celda tiene aun 30+ apuestas.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.571 (n=7) | +0.000 (n=8) | +0.125 (n=8) | +0.000 (n=8) | +0.000 (n=1) | +0.000 (n=3) |
| spread · B | +1.250 (n=8) | +0.250 (n=8) | +0.222 (n=9) | +0.125 (n=8) | +0.000 (n=2) | +1.000 (n=1) |
| ml · A | -0.022 (n=5) | +0.004 (n=8) | +0.008 (n=7) | +0.002 (n=7) | – | +0.006 (n=4) |
| ml · B | +0.013 (n=7) | +0.005 (n=9) | +0.004 (n=9) | -0.002 (n=8) | -0.002 (n=2) | +0.023 (n=2) |
| total · T | -0.167 (n=6) | +0.400 (n=10) | +0.100 (n=10) | -0.300 (n=10) | +0.000 (n=1) | +0.200 (n=5) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 11 | +0.085 (0.06) | – | – | – |
| spread · A · D | 16 | -0.422 (-0.28) | – | – | – |
| spread · B · E | 11 | -0.686 (-0.70) | – | – | – |
| spread · B · D | 16 | -0.433 (-0.36) | – | – | – |
| ml · A · E | 11 | – | 0.2434 | 0.2186 | +0.0248 (1.40) |
| ml · A · D | 16 | – | 0.2459 | 0.2375 | +0.0084 (0.50) |
| ml · B · E | 11 | – | 0.2550 | 0.2186 | +0.0364 (1.06) |
| ml · B · D | 16 | – | 0.2539 | 0.2375 | +0.0164 (0.63) |
| total · T · E | 11 | +0.917 (0.34) | – | – | – |
| total · T · D | 16 | +0.078 (0.05) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._