# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **22** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 4 · -3%* | 7 · -45%* | 10 · -23%* | 11 · -30%* | 13 · -26%* | 2 · -100%* |
| H6 | 5 · -63%* | 8 · -5%* | 12 · -37%* | 16 · -41%* | 18 · -26%* | 4 · -100%* |
| D | 5 · -62%* | 8 · -4%* | 11 · -30%* | 16 · -28%* | 19 · -20%* | 3 · -100%* |
| L | 5 · -61%* | 8 · -28%* | 11 · -31%* | 14 · -19%* | 17 · -11%* | 5 · -100%* |
| D+conf | – | 1 · +95%* | 1 · +95%* | 2 · -2%* | 2 · -2%* | 1 · -100%* |
| D+fade | 2 · -5%* | 4 · +44%* | 4 · +44%* | 5 · +15%* | 5 · +15%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 4 · -3%* | 9 · -14%* | 11 · -13%* | 11 · -13%* | 14 · +9%* | 1 · +95%* |
| H6 | 5 · +13%* | 7 · +8%* | 10 · -6%* | 20 · -5%* | 21 · -9%* | 1 · +95%* |
| D | 5 · -23%* | 9 · -14%* | 13 · -11%* | 19 · +11%* | 20 · +15%* | 2 · -100%* |
| L | 5 · -24%* | 8 · -29%* | 12 · -21%* | 15 · -12%* | 20 · +5%* | 2 · -100%* |
| D+conf | – | 1 · +95%* | 2 · +93%* | 4 · +45%* | 4 · +45%* | – |
| D+fade | 2 · +92%* | 2 · +92%* | 3 · +92%* | 5 · +90%* | 5 · +90%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 3 · -100%* | 6 · -100%* | 8 · -71%* | 12 · -48%* | 14 · -55%* | 1 · -100%* |
| H6 | 7 · -100%* | 9 · -39%* | 12 · -55%* | 17 · -57%* | 18 · -47%* | 4 · -30%* |
| D | 5 · -100%* | 10 · -45%* | 11 · -50%* | 16 · -25%* | 18 · -34%* | 4 · +3%* |
| L | 6 · -56%* | 8 · -67%* | 11 · -76%* | 15 · -22%* | 17 · -31%* | 5 · -18%* |
| D+conf | – | – | 1 · -100%* | 1 · -100%* | 1 · -100%* | 1 · +32%* |
| D+fade | 2 · -100%* | 5 · +10%* | 5 · +10%* | 5 · +10%* | 6 · -8%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 7 · -43%* | 8 · -50%* | 10 · -36%* | 12 · -35%* | 14 · -25%* | 1 · +130%* |
| H6 | 5 · -41%* | 9 · -51%* | 13 · -25%* | 18 · -15%* | 22 · -24%* | – |
| D | 5 · -41%* | 10 · -56%* | 13 · -38%* | 19 · -11%* | 21 · -9%* | 1 · -100%* |
| L | 6 · -56%* | 9 · -71%* | 12 · -48%* | 18 · -38%* | 20 · -19%* | 2 · +101%* |
| D+conf | – | 1 · -100%* | 2 · -34%* | 4 · -33%* | 4 · -33%* | – |
| D+fade | 3 · -2%* | 3 · -2%* | 3 · -2%* | 5 · +35%* | 5 · +35%* | – |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 3 · +28%* | 6 · -5%* | 8 · +19%* | 12 · -21%* | 14 · -18%* | 1 · +91%* |
| H6 | 3 · +27%* | 9 · +6%* | 12 · +11%* | 14 · +9%* | 17 · +12%* | 5 · -61%* |
| D | 2 · -7%* | 10 · -5%* | 12 · -5%* | 16 · +7%* | 17 · +12%* | 5 · +51%* |
| L | 1 · -100%* | 10 · -4%* | 13 · +3%* | 17 · +12%* | 17 · +12%* | 5 · +13%* |
| D+conf | – | 2 · -5%* | 2 · -5%* | 3 · +28%* | 3 · +28%* | 1 · +87%* |
| D+fade | 2 · -7%* | 4 · -53%* | 6 · -37%* | 6 · -37%* | 6 · -37%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Ninguna celda tiene aun 30+ apuestas.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.600 (n=10) | +0.167 (n=12) | +0.182 (n=11) | +0.091 (n=11) | +0.000 (n=1) | +0.000 (n=4) |
| spread · B | +0.909 (n=11) | +0.200 (n=10) | +0.154 (n=13) | +0.167 (n=12) | +0.000 (n=2) | +0.000 (n=3) |
| ml · A | -0.008 (n=8) | +0.005 (n=12) | +0.009 (n=11) | +0.001 (n=11) | +0.033 (n=1) | +0.006 (n=5) |
| ml · B | +0.009 (n=10) | +0.004 (n=13) | +0.005 (n=13) | +0.001 (n=12) | -0.002 (n=2) | +0.017 (n=3) |
| total · T | +0.125 (n=8) | +0.417 (n=12) | -0.083 (n=12) | -0.385 (n=13) | +0.000 (n=2) | -0.167 (n=6) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 15 | -0.839 (-0.77) | – | – | – |
| spread · A · D | 22 | -0.766 (-0.82) | – | – | – |
| spread · B · E | 15 | -0.437 (-0.49) | – | – | – |
| spread · B · D | 22 | -0.123 (-0.14) | – | – | – |
| ml · A · E | 15 | – | 0.2311 | 0.1949 | +0.0362 (2.58) |
| ml · A · D | 22 | – | 0.2350 | 0.2085 | +0.0265 (1.81) |
| ml · B · E | 15 | – | 0.2271 | 0.1949 | +0.0322 (1.22) |
| ml · B · D | 22 | – | 0.2263 | 0.2085 | +0.0178 (0.89) |
| total · T · E | 15 | +0.594 (0.24) | – | – | – |
| total · T · D | 22 | -0.017 (-0.01) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._