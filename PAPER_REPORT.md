# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **31** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 6 · -4%* | 10 · -23%* | 14 · -4%* | 18 · -25%* | 20 · -23%* | 4 · -3%* |
| H6 | 6 · -69%* | 10 · -5%* | 17 · -22%* | 22 · -22%* | 24 · -13%* | 7 · -19%* |
| D | 6 · -37%* | 12 · +11%* | 16 · -17%* | 23 · -9%* | 26 · -5%* | 5 · -25%* |
| L | 7 · -45%* | 11 · -13%* | 16 · -16%* | 21 · -1%* | 26 · -5%* | 5 · -100%* |
| D+conf | – | 2 · -2%* | 2 · -2%* | 3 · -35%* | 3 · -35%* | 1 · -100%* |
| D+fade | 3 · +26%* | 6 · +58%* | 7 · +36%* | 9 · +26%* | 9 · +26%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 4 · -3%* | 10 · -23%* | 13 · -26%* | 17 · -44%* | 22 · -22%* | 2 · -2%* |
| H6 | 6 · -6%* | 8 · -5%* | 12 · -21%* | 25 · -16%* | 27 · -16%* | 4 · -51%* |
| D | 5 · -23%* | 9 · -14%* | 13 · -11%* | 25 · -16%* | 28 · -5%* | 3 · -35%* |
| L | 5 · -24%* | 9 · -37%* | 15 · -37%* | 20 · -34%* | 27 · -22%* | 4 · -100%* |
| D+conf | – | 1 · +95%* | 2 · +93%* | 7 · -17%* | 7 · -17%* | – |
| D+fade | 2 · +92%* | 2 · +92%* | 3 · +92%* | 6 · +59%* | 6 · +59%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 6 · -79%* | 11 · -65%* | 13 · -53%* | 20 · -41%* | 23 · -48%* | 1 · -100%* |
| H6 | 7 · -100%* | 13 · -39%* | 19 · -52%* | 25 · -49%* | 26 · -42%* | 5 · -10%* |
| D | 6 · -100%* | 14 · -52%* | 18 · -49%* | 24 · -28%* | 26 · -33%* | 5 · -18%* |
| L | 7 · -62%* | 12 · -57%* | 18 · -65%* | 23 · -25%* | 26 · -34%* | 5 · -18%* |
| D+conf | – | 2 · -38%* | 5 · -27%* | 5 · -27%* | 5 · -27%* | 2 · -34%* |
| D+fade | 3 · -100%* | 7 · -22%* | 8 · -31%* | 9 · -19%* | 10 · -27%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 7 · -43%* | 9 · -56%* | 12 · -46%* | 17 · -47%* | 19 · -39%* | 5 · +2%* |
| H6 | 6 · -51%* | 10 · -56%* | 16 · -39%* | 25 · -32%* | 30 · -34% | 1 · +130%* |
| D | 5 · -41%* | 10 · -56%* | 16 · -49%* | 27 · -33%* | 29 · -30%* | 2 · -18%* |
| L | 6 · -56%* | 9 · -71%* | 16 · -61%* | 25 · -50%* | 28 · -38%* | 3 · +88%* |
| D+conf | – | 1 · -100%* | 3 · -56%* | 7 · -61%* | 7 · -61%* | – |
| D+fade | 3 · -2%* | 3 · -2%* | 5 · -41%* | 7 · -3%* | 7 · -3%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 4 · +44%* | 12 · +27%* | 14 · +36%* | 18 · +6%* | 22 · +4%* | 2 · +91%* |
| H6 | 5 · +52%* | 11 · +21%* | 15 · +27%* | 20 · +24%* | 23 · +24%* | 8 · -28%* |
| D | 3 · +27%* | 11 · +4%* | 15 · +14%* | 22 · +21%* | 24 · +19%* | 7 · +35%* |
| L | 2 · -6%* | 11 · +4%* | 18 · +17%* | 24 · +20%* | 24 · +20%* | 7 · +35%* |
| D+conf | 1 · +93%* | 3 · +28%* | 4 · +43%* | 8 · +44%* | 8 · +44%* | 2 · +88%* |
| D+fade | 2 · -7%* | 4 · -53%* | 7 · -19%* | 7 · -19%* | 7 · -19%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 1. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.214 (n=14) | -0.235 (n=17) | +0.125 (n=16) | +0.000 (n=16) | -0.500 (n=2) | +0.143 (n=7) |
| spread · B | +0.923 (n=13) | +0.333 (n=12) | +0.154 (n=13) | +0.200 (n=15) | +0.000 (n=2) | +0.000 (n=3) |
| ml · A | -0.003 (n=13) | -0.004 (n=19) | +0.007 (n=18) | +0.001 (n=18) | +0.010 (n=5) | +0.004 (n=8) |
| ml · B | +0.015 (n=12) | +0.003 (n=16) | +0.005 (n=16) | -0.000 (n=16) | -0.002 (n=3) | +0.012 (n=5) |
| total · T | +1.214 (n=14) | +0.267 (n=15) | -0.200 (n=15) | -0.500 (n=18) | -0.500 (n=4) | -0.143 (n=7) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 24 | -1.021 (-1.22) | – | – | – |
| spread · A · D | 31 | -0.555 (-0.74) | – | – | – |
| spread · B · E | 24 | -0.708 (-0.88) | – | – | – |
| spread · B · D | 31 | -0.316 (-0.39) | – | – | – |
| ml · A · E | 24 | – | 0.2106 | 0.1793 | +0.0312 (2.29) |
| ml · A · D | 31 | – | 0.2181 | 0.1918 | +0.0262 (2.07) |
| ml · B · E | 24 | – | 0.2106 | 0.1793 | +0.0313 (1.82) |
| ml · B · D | 31 | – | 0.2131 | 0.1918 | +0.0213 (1.46) |
| total · T · E | 24 | +1.093 (0.74) | – | – | – |
| total · T · D | 31 | +0.060 (0.06) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._