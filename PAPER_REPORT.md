# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **4** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | – | – | 1 · -100%* | 1 · -100%* | 1 · -100%* | – |
| H6 | – | – | 2 · -100%* | 2 · -100%* | 4 · -5%* | – |
| D | – | – | 1 · -100%* | 2 · -100%* | 3 · -35%* | 1 · -100%* |
| L | – | – | 1 · -100%* | 1 · -100%* | 2 · -2%* | 2 · -100%* |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | – | – | 1 · -100%* | 1 · -100%* | 1 · -100%* | – |
| H6 | 1 · +85%* | 1 · +85%* | 2 · -8%* | 3 · -38%* | 3 · -38%* | 1 · +95%* |
| D | – | 1 · +93%* | 2 · -4%* | 2 · -4%* | 3 · +29%* | 1 · -100%* |
| L | – | – | 1 · -100%* | 1 · -100%* | 4 · +46%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | – | 1 · -100%* | 1 · -100%* | 1 · -100%* | 1 · -100%* | – |
| H6 | 1 · -100%* | 1 · -100%* | 1 · -100%* | 3 · -38%* | 3 · -38%* | 1 · -100%* |
| D | – | 1 · -100%* | 1 · -100%* | 2 · -8%* | 3 · -38%* | 1 · -100%* |
| L | – | 1 · -100%* | 1 · -100%* | 2 · -8%* | 2 · -8%* | 2 · -100%* |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | – | 1 · -100%* | 1 · -100%* | 1 · -100%* | 1 · -100%* | – |
| H6 | – | 2 · -29%* | 2 · -29%* | 3 · +10%* | 4 · -18%* | – |
| D | – | 1 · +42%* | 2 · -29%* | 3 · +9%* | 3 · +9%* | 1 · -100%* |
| L | – | 1 · -100%* | 1 · -100%* | 2 · -8%* | 4 · +69%* | – |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | – | – | – | – | 1 · -100%* | – |
| H6 | – | 3 · +27%* | 4 · -4%* | 4 · -4%* | 4 · -4%* | – |
| D | – | 3 · +29%* | 3 · +29%* | 4 · -3%* | 4 · -3%* | – |
| L | – | 3 · +29%* | 3 · +29%* | 4 · -3%* | 4 · -3%* | – |
| D+fade | – | 1 · -100%* | 1 · -100%* | 1 · -100%* | 1 · -100%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Ninguna celda tiene aun 30+ apuestas.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.000 (n=1) | +0.500 (n=2) | +0.000 (n=1) | +0.000 (n=1) | – | – |
| spread · B | +0.000 (n=1) | +0.500 (n=2) | +0.000 (n=2) | +0.000 (n=1) | – | – |
| ml · A | +0.000 (n=1) | +0.007 (n=1) | -0.007 (n=1) | +0.000 (n=1) | – | – |
| ml · B | +0.000 (n=1) | +0.003 (n=2) | -0.003 (n=2) | +0.000 (n=1) | – | – |
| total · T | – | +0.500 (n=4) | +0.000 (n=3) | -0.333 (n=3) | – | +0.000 (n=1) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._