# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **19** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 4 · -3%* | 7 · -45%* | 10 · -23%* | 11 · -30%* | 12 · -20%* | 2 · -100%* |
| H6 | 4 · -53%* | 7 · +9%* | 11 · -31%* | 13 · -27%* | 15 · -12%* | 4 · -100%* |
| D | 4 · -52%* | 7 · +10%* | 10 · -23%* | 14 · -18%* | 16 · -5%* | 3 · -100%* |
| L | 4 · -51%* | 7 · -18%* | 10 · -24%* | 12 · -5%* | 14 · +8%* | 5 · -100%* |
| D+conf | – | 1 · +95%* | 1 · +95%* | 2 · -2%* | 2 · -2%* | 1 · -100%* |
| D+fade | 2 · -5%* | 4 · +44%* | 4 · +44%* | 4 · +44%* | 4 · +44%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 4 · -3%* | 9 · -14%* | 10 · -23%* | 10 · -23%* | 13 · +3%* | 1 · +95%* |
| H6 | 5 · +13%* | 7 · +8%* | 10 · -6%* | 17 · -11%* | 18 · -16%* | 1 · +95%* |
| D | 5 · -23%* | 8 · -4%* | 12 · -4%* | 16 · +7%* | 17 · +13%* | 2 · -100%* |
| L | 5 · -24%* | 7 · -19%* | 10 · -24%* | 12 · -21%* | 17 · +1%* | 2 · -100%* |
| D+conf | – | 1 · +95%* | 2 · +93%* | 3 · +29%* | 3 · +29%* | – |
| D+fade | 2 · +92%* | 2 · +92%* | 3 · +92%* | 5 · +90%* | 5 · +90%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 3 · -100%* | 6 · -100%* | 8 · -71%* | 11 · -43%* | 13 · -52%* | 1 · -100%* |
| H6 | 6 · -100%* | 8 · -32%* | 11 · -50%* | 14 · -48%* | 15 · -36%* | 4 · -30%* |
| D | 4 · -100%* | 9 · -39%* | 10 · -45%* | 14 · -15%* | 16 · -25%* | 3 · +37%* |
| L | 5 · -47%* | 7 · -62%* | 9 · -71%* | 13 · -10%* | 15 · -22%* | 4 · +3%* |
| D+conf | – | – | 1 · -100%* | 1 · -100%* | 1 · -100%* | 1 · +32%* |
| D+fade | 2 · -100%* | 5 · +10%* | 5 · +10%* | 5 · +10%* | 6 · -8%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 7 · -43%* | 8 · -50%* | 9 · -56%* | 11 · -51%* | 13 · -38%* | 1 · +130%* |
| H6 | 5 · -41%* | 9 · -51%* | 11 · -48%* | 15 · -25%* | 19 · -33%* | – |
| D | 5 · -41%* | 9 · -51%* | 11 · -48%* | 16 · -20%* | 18 · -16%* | 1 · -100%* |
| L | 6 · -56%* | 8 · -67%* | 10 · -61%* | 15 · -53%* | 17 · -29%* | 2 · +101%* |
| D+conf | – | 1 · -100%* | 2 · -34%* | 4 · -33%* | 4 · -33%* | – |
| D+fade | 3 · -2%* | 3 · -2%* | 3 · -2%* | 5 · +35%* | 5 · +35%* | – |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 3 · +28%* | 6 · -5%* | 7 · +9%* | 11 · -31%* | 13 · -27%* | 1 · +91%* |
| H6 | 3 · +27%* | 9 · +6%* | 11 · +4%* | 13 · +2%* | 15 · +14%* | 4 · -52%* |
| D | 2 · -7%* | 10 · -5%* | 12 · -5%* | 15 · +1%* | 16 · +7%* | 3 · +89%* |
| L | 1 · -100%* | 10 · -4%* | 13 · +3%* | 16 · +7%* | 16 · +7%* | 3 · +26%* |
| D+conf | – | 2 · -5%* | 2 · -5%* | 2 · -5%* | 2 · -5%* | 1 · +87%* |
| D+fade | 2 · -7%* | 4 · -53%* | 6 · -37%* | 6 · -37%* | 6 · -37%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Ninguna celda tiene aun 30+ apuestas.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.600 (n=10) | +0.182 (n=11) | +0.100 (n=10) | +0.000 (n=10) | +0.000 (n=1) | +0.000 (n=4) |
| spread · B | +0.900 (n=10) | +0.200 (n=10) | +0.083 (n=12) | +0.100 (n=10) | +0.000 (n=2) | +0.000 (n=3) |
| ml · A | -0.008 (n=8) | +0.007 (n=11) | +0.009 (n=10) | +0.002 (n=9) | +0.033 (n=1) | +0.006 (n=5) |
| ml · B | +0.008 (n=9) | +0.005 (n=11) | +0.004 (n=11) | -0.001 (n=10) | -0.002 (n=2) | +0.017 (n=3) |
| total · T | +0.000 (n=7) | +0.364 (n=11) | -0.083 (n=12) | -0.385 (n=13) | +0.000 (n=2) | -0.167 (n=6) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 14 | -0.676 (-0.63) | – | – | – |
| spread · A · D | 19 | -0.544 (-0.52) | – | – | – |
| spread · B · E | 14 | -0.745 (-0.85) | – | – | – |
| spread · B · D | 19 | -0.270 (-0.28) | – | – | – |
| ml · A · E | 14 | – | 0.2174 | 0.1823 | +0.0351 (2.33) |
| ml · A · D | 19 | – | 0.2274 | 0.2080 | +0.0194 (1.24) |
| ml · B · E | 14 | – | 0.2221 | 0.1823 | +0.0398 (1.46) |
| ml · B · D | 19 | – | 0.2308 | 0.2080 | +0.0229 (1.02) |
| total · T · E | 14 | +0.613 (0.26) | – | – | – |
| total · T · D | 19 | +0.125 (0.09) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._