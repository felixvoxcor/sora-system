# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **23** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 4 · -3%* | 7 · -45%* | 10 · -23%* | 11 · -30%* | 13 · -26%* | 3 · -35%* |
| H6 | 5 · -63%* | 8 · -5%* | 12 · -37%* | 16 · -41%* | 18 · -26%* | 5 · -60%* |
| D | 5 · -62%* | 8 · -4%* | 11 · -30%* | 17 · -22%* | 20 · -14%* | 3 · -100%* |
| L | 5 · -61%* | 8 · -28%* | 11 · -31%* | 15 · -12%* | 18 · -5%* | 5 · -100%* |
| D+conf | – | 1 · +95%* | 1 · +95%* | 2 · -2%* | 2 · -2%* | 1 · -100%* |
| D+fade | 2 · -5%* | 4 · +44%* | 4 · +44%* | 6 · +27%* | 6 · +27%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 4 · -3%* | 9 · -14%* | 12 · -20%* | 12 · -20%* | 15 · +2%* | 1 · +95%* |
| H6 | 6 · -6%* | 8 · -5%* | 11 · -14%* | 21 · -9%* | 22 · -13%* | 1 · +95%* |
| D | 5 · -23%* | 9 · -14%* | 13 · -11%* | 20 · +5%* | 21 · +9%* | 2 · -100%* |
| L | 5 · -24%* | 8 · -29%* | 12 · -21%* | 16 · -17%* | 21 · -0%* | 2 · -100%* |
| D+conf | – | 1 · +95%* | 2 · +93%* | 5 · +16%* | 5 · +16%* | – |
| D+fade | 2 · +92%* | 2 · +92%* | 3 · +92%* | 5 · +90%* | 5 · +90%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 3 · -100%* | 6 · -100%* | 8 · -71%* | 13 · -38%* | 15 · -46%* | 1 · -100%* |
| H6 | 7 · -100%* | 9 · -39%* | 12 · -55%* | 18 · -50%* | 19 · -40%* | 4 · -30%* |
| D | 5 · -100%* | 10 · -45%* | 11 · -50%* | 17 · -19%* | 19 · -28%* | 4 · +3%* |
| L | 6 · -56%* | 8 · -67%* | 11 · -76%* | 16 · -15%* | 18 · -25%* | 5 · -18%* |
| D+conf | – | – | 1 · -100%* | 1 · -100%* | 1 · -100%* | 1 · +32%* |
| D+fade | 2 · -100%* | 5 · +10%* | 5 · +10%* | 6 · +22%* | 7 · +4%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 7 · -43%* | 8 · -50%* | 10 · -36%* | 13 · -40%* | 15 · -30%* | 1 · +130%* |
| H6 | 6 · -51%* | 10 · -56%* | 14 · -30%* | 19 · -19%* | 23 · -27%* | – |
| D | 5 · -41%* | 10 · -56%* | 13 · -38%* | 20 · -16%* | 22 · -13%* | 1 · -100%* |
| L | 6 · -56%* | 9 · -71%* | 12 · -48%* | 19 · -41%* | 21 · -23%* | 2 · +101%* |
| D+conf | – | 1 · -100%* | 2 · -34%* | 5 · -46%* | 5 · -46%* | – |
| D+fade | 3 · -2%* | 3 · -2%* | 3 · -2%* | 5 · +35%* | 5 · +35%* | – |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 3 · +28%* | 7 · +9%* | 9 · +27%* | 13 · -12%* | 15 · -11%* | 1 · +91%* |
| H6 | 3 · +27%* | 9 · +6%* | 12 · +11%* | 15 · +14%* | 18 · +16%* | 5 · -61%* |
| D | 2 · -7%* | 10 · -5%* | 13 · +3%* | 17 · +12%* | 18 · +16%* | 5 · +51%* |
| L | 1 · -100%* | 10 · -4%* | 14 · +9%* | 18 · +17%* | 18 · +17%* | 5 · +13%* |
| D+conf | – | 2 · -5%* | 3 · +27%* | 4 · +43%* | 4 · +43%* | 1 · +87%* |
| D+fade | 2 · -7%* | 4 · -53%* | 6 · -37%* | 6 · -37%* | 6 · -37%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Ninguna celda tiene aun 30+ apuestas.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.600 (n=10) | +0.167 (n=12) | +0.182 (n=11) | +0.091 (n=11) | +0.000 (n=1) | +0.000 (n=4) |
| spread · B | +0.917 (n=12) | +0.273 (n=11) | +0.154 (n=13) | +0.167 (n=12) | +0.000 (n=2) | +0.000 (n=3) |
| ml · A | -0.008 (n=8) | +0.005 (n=12) | +0.009 (n=11) | +0.001 (n=11) | +0.033 (n=1) | +0.006 (n=5) |
| ml · B | +0.009 (n=10) | +0.004 (n=14) | +0.005 (n=13) | +0.001 (n=12) | -0.002 (n=2) | +0.017 (n=3) |
| total · T | +0.222 (n=9) | +0.417 (n=12) | -0.077 (n=13) | -0.357 (n=14) | +0.000 (n=3) | -0.167 (n=6) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 16 | -0.807 (-0.77) | – | – | – |
| spread · A · D | 23 | -0.744 (-0.81) | – | – | – |
| spread · B · E | 16 | -0.477 (-0.56) | – | – | – |
| spread · B · D | 23 | -0.209 (-0.24) | – | – | – |
| ml · A · E | 16 | – | 0.2277 | 0.1958 | +0.0319 (2.30) |
| ml · A · D | 23 | – | 0.2324 | 0.2089 | +0.0235 (1.64) |
| ml · B · E | 16 | – | 0.2292 | 0.1958 | +0.0334 (1.35) |
| ml · B · D | 23 | – | 0.2277 | 0.2089 | +0.0188 (0.98) |
| total · T · E | 16 | +1.487 (0.79) | – | – | – |
| total · T · D | 23 | +0.391 (0.32) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._