# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **9** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 1 · +91%* | 2 · -5%* | 3 · -36%* | 4 · -52%* | 5 · -23%* | 1 · -100%* |
| H6 | – | 1 · +95%* | 3 · -35%* | 3 · -35%* | 5 · +15%* | 4 · -100%* |
| D | – | 1 · +95%* | 2 · -2%* | 4 · -4%* | 6 · +27%* | 3 · -100%* |
| L | – | 1 · +87%* | 2 · -7%* | 3 · +25%* | 5 · +51%* | 4 · -100%* |
| D+conf | – | 1 · +95%* | 1 · +95%* | 1 · +95%* | 1 · +95%* | 1 · -100%* |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | – | 3 · -36%* | 4 · -52%* | 4 · -52%* | 5 · -24%* | 1 · +95%* |
| H6 | 1 · +85%* | 3 · +27%* | 4 · -5%* | 7 · -19%* | 8 · -29%* | 1 · +95%* |
| D | – | 3 · +29%* | 4 · -3%* | 6 · +27%* | 7 · +36%* | 2 · -100%* |
| L | – | 2 · -7%* | 3 · -38%* | 4 · -53%* | 8 · +19%* | 1 · -100%* |
| D+conf | – | 1 · +95%* | 1 · +95%* | 1 · +95%* | 1 · +95%* | – |
| D+fade | – | – | – | 1 · +85%* | 1 · +85%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | – | 2 · -100%* | 2 · -100%* | 4 · -65%* | 5 · -72%* | 1 · -100%* |
| H6 | 2 · -100%* | 2 · -100%* | 2 · -100%* | 5 · -63%* | 5 · -63%* | 4 · -30%* |
| D | 1 · -100%* | 2 · -100%* | 2 · -100%* | 4 · +4%* | 6 · -31%* | 3 · +37%* |
| L | – | 2 · -100%* | 2 · -100%* | 4 · +4%* | 5 · -17%* | 4 · +3%* |
| D+conf | – | – | – | – | – | 1 · +32%* |
| D+fade | – | – | – | – | 1 · -100%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 1 · -100%* | 2 · -100%* | 3 · -100%* | 5 · -72%* | 6 · -53%* | – |
| H6 | 1 · -100%* | 4 · -64%* | 4 · -64%* | 6 · -45%* | 9 · -48%* | – |
| D | 1 · -100%* | 3 · -53%* | 4 · -64%* | 6 · -23%* | 8 · -13%* | 1 · -100%* |
| L | 1 · -100%* | 3 · -100%* | 3 · -100%* | 6 · -69%* | 8 · -15%* | 1 · +38%* |
| D+conf | – | 1 · -100%* | 1 · -100%* | 2 · -31%* | 2 · -31%* | – |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 1 · +95%* | 2 · -2%* | 3 · +29%* | 4 · -3%* | 5 · -22%* | 1 · +91%* |
| H6 | 2 · -4%* | 5 · +15%* | 7 · +9%* | 8 · -4%* | 8 · -4%* | 1 · -100%* |
| D | 1 · -100%* | 5 · +16%* | 7 · +10%* | 8 · -4%* | 8 · -4%* | 1 · +87%* |
| L | 1 · -100%* | 5 · +16%* | 7 · +10%* | 8 · -4%* | 8 · -4%* | 1 · -100%* |
| D+conf | – | 1 · +91%* | 1 · +91%* | 1 · +91%* | 1 · +91%* | 1 · +87%* |
| D+fade | 1 · -100%* | 2 · -100%* | 4 · -53%* | 4 · -53%* | 4 · -53%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Ninguna celda tiene aun 30+ apuestas.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +2.000 (n=3) | +0.333 (n=3) | +0.000 (n=2) | +0.000 (n=2) | +0.000 (n=1) | – |
| spread · B | +1.500 (n=4) | +0.250 (n=4) | +0.000 (n=4) | +0.000 (n=3) | +0.000 (n=1) | – |
| ml · A | +0.000 (n=2) | +0.008 (n=2) | -0.001 (n=2) | +0.000 (n=2) | – | – |
| ml · B | +0.005 (n=3) | +0.001 (n=4) | -0.004 (n=4) | -0.004 (n=3) | -0.013 (n=1) | – |
| total · T | -0.333 (n=3) | +0.429 (n=7) | -0.143 (n=7) | -0.429 (n=7) | +0.000 (n=1) | -0.250 (n=4) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._