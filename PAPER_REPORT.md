# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **25** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 4 · -3%* | 8 · -27%* | 11 · -12%* | 13 · -26%* | 15 · -23%* | 3 · -35%* |
| H6 | 5 · -63%* | 8 · -5%* | 13 · -26%* | 17 · -33%* | 19 · -20%* | 6 · -36%* |
| D | 5 · -62%* | 9 · +6%* | 12 · -20%* | 18 · -16%* | 21 · -10%* | 4 · -53%* |
| L | 5 · -61%* | 9 · -15%* | 12 · -20%* | 16 · -5%* | 20 · -5%* | 5 · -100%* |
| D+conf | – | 1 · +95%* | 1 · +95%* | 2 · -2%* | 2 · -2%* | 1 · -100%* |
| D+fade | 2 · -5%* | 4 · +44%* | 4 · +44%* | 6 · +27%* | 6 · +27%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 4 · -3%* | 9 · -14%* | 12 · -20%* | 13 · -26%* | 16 · -4%* | 2 · -2%* |
| H6 | 6 · -6%* | 8 · -5%* | 12 · -21%* | 23 · -9%* | 24 · -13%* | 1 · +95%* |
| D | 5 · -23%* | 9 · -14%* | 13 · -11%* | 21 · +0%* | 23 · +8%* | 2 · -100%* |
| L | 5 · -24%* | 8 · -29%* | 12 · -21%* | 16 · -17%* | 22 · -5%* | 3 · -100%* |
| D+conf | – | 1 · +95%* | 2 · +93%* | 5 · +16%* | 5 · +16%* | – |
| D+fade | 2 · +92%* | 2 · +92%* | 3 · +92%* | 5 · +90%* | 5 · +90%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 3 · -100%* | 7 · -64%* | 9 · -46%* | 15 · -29%* | 17 · -38%* | 1 · -100%* |
| H6 | 7 · -100%* | 10 · -20%* | 13 · -39%* | 19 · -39%* | 20 · -31%* | 5 · -10%* |
| D | 5 · -100%* | 10 · -45%* | 12 · -34%* | 18 · -10%* | 20 · -19%* | 5 · -18%* |
| L | 6 · -56%* | 9 · -43%* | 12 · -57%* | 17 · -6%* | 20 · -20%* | 5 · -18%* |
| D+conf | – | – | 2 · +21%* | 2 · +21%* | 2 · +21%* | 2 · -34%* |
| D+fade | 2 · -100%* | 5 · +10%* | 5 · +10%* | 6 · +22%* | 7 · +4%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 7 · -43%* | 8 · -50%* | 10 · -36%* | 14 · -44%* | 16 · -35%* | 2 · +93%* |
| H6 | 6 · -51%* | 10 · -56%* | 15 · -35%* | 21 · -19%* | 25 · -26%* | – |
| D | 5 · -41%* | 10 · -56%* | 14 · -42%* | 21 · -20%* | 23 · -17%* | 2 · -18%* |
| L | 6 · -56%* | 9 · -71%* | 12 · -48%* | 20 · -44%* | 22 · -27%* | 3 · +88%* |
| D+conf | – | 1 · -100%* | 2 · -34%* | 5 · -46%* | 5 · -46%* | – |
| D+fade | 3 · -2%* | 3 · -2%* | 4 · -26%* | 6 · +13%* | 6 · +13%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 3 · +28%* | 8 · -5%* | 10 · +14%* | 14 · -18%* | 17 · -22%* | 1 · +91%* |
| H6 | 3 · +27%* | 9 · +6%* | 13 · +17%* | 17 · +12%* | 20 · +14%* | 5 · -61%* |
| D | 2 · -7%* | 10 · -5%* | 14 · +9%* | 19 · +10%* | 20 · +14%* | 5 · +51%* |
| L | 1 · -100%* | 10 · -4%* | 15 · +15%* | 20 · +15%* | 20 · +15%* | 5 · +13%* |
| D+conf | – | 2 · -5%* | 3 · +27%* | 5 · +15%* | 5 · +15%* | 1 · +87%* |
| D+fade | 2 · -7%* | 4 · -53%* | 7 · -19%* | 7 · -19%* | 7 · -19%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Ninguna celda tiene aun 30+ apuestas.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.545 (n=11) | +0.077 (n=13) | +0.167 (n=12) | +0.083 (n=12) | +0.000 (n=1) | +0.000 (n=4) |
| spread · B | +0.917 (n=12) | +0.333 (n=12) | +0.154 (n=13) | +0.167 (n=12) | +0.000 (n=2) | +0.000 (n=3) |
| ml · A | -0.006 (n=9) | +0.005 (n=13) | +0.008 (n=12) | +0.002 (n=12) | +0.014 (n=2) | +0.006 (n=5) |
| ml · B | +0.009 (n=10) | +0.003 (n=15) | +0.005 (n=14) | +0.001 (n=12) | -0.002 (n=2) | +0.014 (n=4) |
| total · T | +0.600 (n=10) | +0.385 (n=13) | -0.071 (n=14) | -0.333 (n=15) | +0.000 (n=3) | -0.143 (n=7) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 18 | -0.506 (-0.50) | – | – | – |
| spread · A · D | 25 | -0.502 (-0.58) | – | – | – |
| spread · B · E | 18 | -0.536 (-0.66) | – | – | – |
| spread · B · D | 25 | -0.221 (-0.26) | – | – | – |
| ml · A · E | 18 | – | 0.2275 | 0.2037 | +0.0238 (1.62) |
| ml · A · D | 25 | – | 0.2319 | 0.2137 | +0.0182 (1.30) |
| ml · B · E | 18 | – | 0.2367 | 0.2037 | +0.0330 (1.49) |
| ml · B · D | 25 | – | 0.2342 | 0.2137 | +0.0205 (1.15) |
| total · T · E | 18 | +0.893 (0.48) | – | – | – |
| total · T · D | 25 | +0.295 (0.24) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._