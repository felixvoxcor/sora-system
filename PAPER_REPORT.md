# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **2** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| H6 | – | – | – | – | 2 · +90%* | – |
| D | – | – | – | – | 1 · +95%* | 1 · -100%* |
| L | – | – | – | – | 1 · +95%* | 1 · -100%* |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| H6 | 1 · +85%* | 1 · +85%* | 1 · +85%* | 1 · +85%* | 1 · +85%* | 1 · +95%* |
| D | – | 1 · +93%* | 1 · +93%* | 1 · +93%* | 2 · +94%* | – |
| L | – | – | – | – | 2 · +94%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| H6 | – | – | – | 1 · +87%* | 1 · +87%* | 1 · -100%* |
| D | – | – | – | 1 · +85%* | 1 · +85%* | 1 · -100%* |
| L | – | – | – | 1 · +85%* | 1 · +85%* | 1 · -100%* |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| H6 | – | 1 · +42%* | 1 · +42%* | 2 · +64%* | 2 · +64%* | – |
| D | – | 1 · +42%* | 1 · +42%* | 2 · +63%* | 2 · +63%* | – |
| L | – | – | – | 1 · +85%* | 2 · +63%* | – |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| H6 | – | 1 · +95%* | 2 · -2%* | 2 · -2%* | 2 · -2%* | – |
| D | – | 1 · +93%* | 1 · +93%* | 2 · -4%* | 2 · -4%* | – |
| L | – | 1 · +93%* | 1 · +93%* | 2 · -4%* | 2 · -4%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Ninguna celda tiene aun 30+ apuestas.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | – | – | – | – | – | – |
| spread · B | – | +1.000 (n=1) | +0.000 (n=1) | – | – | – |
| ml · A | – | – | – | – | – | – |
| ml · B | – | +0.000 (n=1) | +0.000 (n=1) | – | – | – |
| total · T | – | +1.000 (n=2) | +0.000 (n=1) | +0.000 (n=1) | – | – |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._