# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **11** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 1 · +91%* | 3 · -36%* | 5 · -24%* | 6 · -36%* | 7 · -18%* | 1 · -100%* |
| H6 | 1 · -100%* | 3 · +29%* | 5 · -23%* | 5 · -23%* | 7 · +9%* | 4 · -100%* |
| D | 1 · -100%* | 3 · +29%* | 4 · -3%* | 6 · -4%* | 8 · +19%* | 3 · -100%* |
| L | 1 · -100%* | 2 · -7%* | 4 · -7%* | 5 · +12%* | 7 · +34%* | 4 · -100%* |
| D+conf | – | 1 · +95%* | 1 · +95%* | 1 · +95%* | 1 · +95%* | 1 · -100%* |
| D+fade | 1 · -100%* | 2 · -4%* | 2 · -4%* | 2 · -4%* | 2 · -4%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 1 · +91%* | 5 · +15%* | 6 · -4%* | 6 · -4%* | 7 · +10%* | 1 · +95%* |
| H6 | 2 · +88%* | 4 · +43%* | 6 · +26%* | 9 · +5%* | 10 · -6%* | 1 · +95%* |
| D | 1 · +93%* | 4 · +45%* | 6 · +29%* | 8 · +43%* | 9 · +49%* | 2 · -100%* |
| L | 1 · +87%* | 3 · +25%* | 5 · +13%* | 6 · -6%* | 10 · +33%* | 1 · -100%* |
| D+conf | – | 1 · +95%* | 2 · +93%* | 2 · +93%* | 2 · +93%* | – |
| D+fade | 1 · +93%* | 1 · +93%* | 1 · +93%* | 2 · +89%* | 2 · +89%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | – | 2 · -100%* | 3 · -100%* | 6 · -34%* | 7 · -43%* | 1 · -100%* |
| H6 | 3 · -100%* | 4 · -26%* | 4 · -26%* | 7 · -31%* | 7 · -31%* | 4 · -30%* |
| D | 1 · -100%* | 4 · -26%* | 4 · -26%* | 6 · +18%* | 8 · -11%* | 3 · +37%* |
| L | 1 · -100%* | 3 · -100%* | 3 · -100%* | 6 · +13%* | 7 · -3%* | 4 · +3%* |
| D+conf | – | – | – | – | – | 1 · +32%* |
| D+fade | – | 2 · +48%* | 2 · +48%* | 2 · +48%* | 3 · -2%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 3 · +33%* | 4 · +0%* | 5 · -20%* | 7 · -23%* | 8 · -15%* | – |
| H6 | 2 · +48%* | 5 · -13%* | 6 · -5%* | 8 · -6%* | 11 · -19%* | – |
| D | 2 · +48%* | 4 · +9%* | 6 · -5%* | 8 · +11%* | 10 · +12%* | 1 · -100%* |
| L | 2 · +32%* | 4 · -34%* | 5 · -21%* | 8 · -28%* | 10 · +7%* | 1 · +38%* |
| D+conf | – | 1 · -100%* | 2 · -34%* | 3 · -10%* | 3 · -10%* | – |
| D+fade | 1 · +195%* | 1 · +195%* | 1 · +195%* | 1 · +195%* | 1 · +195%* | – |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 1 · +95%* | 2 · -2%* | 3 · +29%* | 5 · -22%* | 7 · -17%* | 1 · +91%* |
| H6 | 2 · -4%* | 5 · +15%* | 7 · +9%* | 8 · -4%* | 9 · +7%* | 2 · -100%* |
| D | 1 · -100%* | 5 · +16%* | 7 · +10%* | 9 · +6%* | 9 · +6%* | 2 · +87%* |
| L | 1 · -100%* | 5 · +16%* | 7 · +10%* | 9 · +7%* | 9 · +7%* | 2 · -7%* |
| D+conf | – | 1 · +91%* | 1 · +91%* | 1 · +91%* | 1 · +91%* | 1 · +87%* |
| D+fade | 1 · -100%* | 2 · -100%* | 4 · -53%* | 4 · -53%* | 4 · -53%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Ninguna celda tiene aun 30+ apuestas.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +1.000 (n=5) | +0.400 (n=5) | +0.250 (n=4) | +0.000 (n=4) | +0.000 (n=1) | +0.500 (n=2) |
| spread · B | +1.167 (n=6) | +0.333 (n=6) | +0.167 (n=6) | +0.000 (n=5) | +0.000 (n=2) | +1.000 (n=1) |
| ml · A | -0.016 (n=3) | +0.014 (n=4) | +0.007 (n=4) | +0.002 (n=3) | – | +0.015 (n=2) |
| ml · B | +0.011 (n=5) | +0.007 (n=6) | +0.005 (n=6) | -0.004 (n=5) | -0.002 (n=2) | +0.038 (n=1) |
| total · T | -0.333 (n=3) | +0.429 (n=7) | -0.143 (n=7) | -0.429 (n=7) | +0.000 (n=1) | -0.250 (n=4) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · D | 11 | -1.244 (-0.61) | – | – | – |
| spread · B · D | 11 | +0.569 (0.37) | – | – | – |
| ml · A · D | 11 | – | 0.2429 | 0.2368 | +0.0061 (0.34) |
| ml · B · D | 11 | – | 0.2242 | 0.2368 | -0.0127 (-0.44) |
| total · T · D | 11 | -0.421 (-0.23) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._