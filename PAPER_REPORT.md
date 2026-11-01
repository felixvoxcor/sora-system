# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **15** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 2 · -5%* | 4 · -52%* | 6 · -36%* | 7 · -45%* | 8 · -28%* | 2 · -100%* |
| H6 | 2 · -100%* | 4 · -3%* | 7 · -45%* | 9 · -36%* | 11 · -13%* | 4 · -100%* |
| D | 2 · -100%* | 4 · -3%* | 7 · -45%* | 10 · -24%* | 12 · -5%* | 3 · -100%* |
| L | 2 · -100%* | 4 · -53%* | 7 · -47%* | 9 · -17%* | 11 · +2%* | 4 · -100%* |
| D+conf | – | 1 · +95%* | 1 · +95%* | 1 · +95%* | 1 · +95%* | 1 · -100%* |
| D+fade | 1 · -100%* | 2 · -4%* | 2 · -4%* | 2 · -4%* | 2 · -4%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 2 · -5%* | 7 · -18%* | 8 · -28%* | 8 · -28%* | 9 · -15%* | 1 · +95%* |
| H6 | 3 · +25%* | 5 · +14%* | 8 · -5%* | 13 · -27%* | 14 · -33%* | 1 · +95%* |
| D | 3 · -36%* | 6 · -3%* | 9 · -14%* | 12 · -5%* | 13 · +3%* | 2 · -100%* |
| L | 3 · -38%* | 5 · -25%* | 8 · -29%* | 9 · -37%* | 14 · -5%* | 1 · -100%* |
| D+conf | – | 1 · +95%* | 2 · +93%* | 3 · +29%* | 3 · +29%* | – |
| D+fade | 1 · +93%* | 1 · +93%* | 1 · +93%* | 2 · +89%* | 2 · +89%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 1 · -100%* | 3 · -100%* | 4 · -100%* | 7 · -43%* | 9 · -56%* | 1 · -100%* |
| H6 | 4 · -100%* | 5 · -41%* | 7 · -58%* | 10 · -52%* | 11 · -36%* | 4 · -30%* |
| D | 2 · -100%* | 6 · -51%* | 6 · -51%* | 10 · -6%* | 12 · -22%* | 3 · +37%* |
| L | 2 · -100%* | 4 · -100%* | 6 · -100%* | 10 · -9%* | 11 · -17%* | 4 · +3%* |
| D+conf | – | – | – | – | – | 1 · +32%* |
| D+fade | 1 · -100%* | 3 · -2%* | 3 · -2%* | 3 · -2%* | 4 · -26%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 5 · -20%* | 6 · -33%* | 7 · -43%* | 9 · -40%* | 10 · -32%* | – |
| H6 | 3 · -2%* | 7 · -38%* | 9 · -37%* | 11 · -31%* | 15 · -41%* | – |
| D | 3 · -2%* | 7 · -38%* | 9 · -37%* | 12 · -26%* | 14 · -20%* | 1 · -100%* |
| L | 4 · -34%* | 6 · -56%* | 8 · -51%* | 12 · -52%* | 14 · -24%* | 1 · +38%* |
| D+conf | – | 1 · -100%* | 2 · -34%* | 4 · -33%* | 4 · -33%* | – |
| D+fade | 2 · +48%* | 2 · +48%* | 2 · +48%* | 2 · +48%* | 2 · +48%* | – |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 2 · +92%* | 4 · -4%* | 5 · +15%* | 7 · -18%* | 9 · -15%* | 1 · +91%* |
| H6 | 2 · -4%* | 7 · +9%* | 9 · +6%* | 11 · +4%* | 13 · +17%* | 2 · -100%* |
| D | 1 · -100%* | 7 · +10%* | 9 · +6%* | 11 · +4%* | 12 · +11%* | 3 · +89%* |
| L | 1 · -100%* | 7 · +10%* | 9 · +6%* | 12 · +12%* | 12 · +12%* | 3 · +26%* |
| D+conf | – | 1 · +91%* | 1 · +91%* | 1 · +91%* | 1 · +91%* | 1 · +87%* |
| D+fade | 1 · -100%* | 2 · -100%* | 4 · -53%* | 4 · -53%* | 4 · -53%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Ninguna celda tiene aun 30+ apuestas.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +1.000 (n=6) | +0.143 (n=7) | +0.286 (n=7) | +0.143 (n=7) | +0.000 (n=1) | +0.500 (n=2) |
| spread · B | +1.250 (n=8) | +0.250 (n=8) | +0.222 (n=9) | +0.125 (n=8) | +0.000 (n=2) | +1.000 (n=1) |
| ml · A | -0.013 (n=4) | +0.007 (n=7) | +0.012 (n=6) | +0.002 (n=6) | – | +0.013 (n=3) |
| ml · B | +0.013 (n=7) | +0.005 (n=9) | +0.004 (n=9) | -0.002 (n=8) | -0.002 (n=2) | +0.023 (n=2) |
| total · T | -0.200 (n=5) | +0.333 (n=9) | -0.111 (n=9) | -0.333 (n=9) | +0.000 (n=1) | -0.250 (n=4) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 10 | -0.798 (-0.57) | – | – | – |
| spread · A · D | 15 | -1.274 (-0.88) | – | – | – |
| spread · B · E | 10 | -0.680 (-0.75) | – | – | – |
| spread · B · D | 15 | -0.421 (-0.37) | – | – | – |
| ml · A · E | 10 | – | 0.2405 | 0.2064 | +0.0340 (2.03) |
| ml · A · D | 15 | – | 0.2441 | 0.2275 | +0.0166 (1.06) |
| ml · B · E | 10 | – | 0.2477 | 0.2064 | +0.0412 (1.10) |
| ml · B · D | 15 | – | 0.2490 | 0.2275 | +0.0214 (0.79) |
| total · T · E | 10 | +0.744 (0.26) | – | – | – |
| total · T · D | 15 | -0.268 (-0.17) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._