# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **71** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 12 · -5%* | 23 · -9%* | 33 · -7% | 45 · -19% | 51 · -14% | 12 · +28%* |
| H6 | 13 · -56%* | 23 · -17%* | 35 · -13% | 50 · -9% | 59 · -6% | 12 · -37%* |
| D | 15 · -37%* | 24 · -5%* | 34 · -5% | 50 · -1% | 64 · +1% | 7 · -19%* |
| L | 15 · -48%* | 23 · -24%* | 34 · -4% | 49 · +9% | 60 · +2% | 11 · -83%* |
| D+conf | 1 · -100%* | 4 · -4%* | 6 · +29%* | 9 · +8%* | 10 · -3%* | 2 · -100%* |
| D+fade | 11 · -13%* | 15 · +14%* | 18 · +16%* | 23 · +15%* | 23 · +15%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 14 · -45%* | 23 · -25%* | 37 · -7% | 48 · -8% | 55 · +1% | 8 · -76%* |
| H6 | 14 · -18%* | 22 · -13%* | 33 · -19% | 60 · -14% | 66 · -13% | 5 · -61%* |
| D | 14 · -31%* | 25 · -23%* | 36 · -10% | 58 · -11% | 65 · -9% | 6 · -36%* |
| L | 14 · -46%* | 26 · -34%* | 37 · -28% | 50 · -24% | 61 · -22% | 10 · -43%* |
| D+conf | 2 · -100%* | 5 · -61%* | 7 · -17%* | 15 · -23%* | 15 · -23%* | – |
| D+fade | 6 · -4%* | 11 · +4%* | 16 · +19%* | 20 · +14%* | 21 · +9%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 15 · -36%* | 24 · -36%* | 30 · -19% | 47 · -17% | 57 · -18% | 6 · +14%* |
| H6 | 14 · -100%* | 28 · -34%* | 36 · -34% | 53 · -19% | 57 · -16% | 14 · -6%* |
| D | 13 · -100%* | 29 · -36%* | 35 · -32% | 51 · -15% | 60 · -14% | 11 · -37%* |
| L | 17 · -71%* | 28 · -39%* | 35 · -40% | 50 · -7% | 58 · -18% | 13 · -11%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 11 · +19%* | 13 · +34%* | 3 · -56%* |
| D+fade | 10 · -100%* | 16 · -32%* | 18 · -39%* | 22 · -20%* | 23 · -23%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 14 · -58%* | 26 · -58%* | 33 · -43% | 50 · -31% | 55 · -25% | 8 · +7%* |
| H6 | 15 · -68%* | 24 · -55%* | 41 · -35% | 59 · -38% | 66 · -35% | 5 · +3%* |
| D | 13 · -63%* | 27 · -63%* | 42 · -39% | 62 · -34% | 69 · -35% | 2 · -18%* |
| L | 15 · -55%* | 26 · -63%* | 40 · -58% | 56 · -40% | 63 · -39% | 8 · +24%* |
| D+conf | 1 · -100%* | 4 · -100%* | 10 · -53%* | 14 · -57%* | 15 · -48%* | – |
| D+fade | 8 · -63%* | 13 · -60%* | 18 · -40%* | 23 · -26%* | 23 · -26%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 8 · +20%* | 23 · +8%* | 27 · +13%* | 36 · -10% | 53 · -10% | 10 · -23%* |
| H6 | 7 · +9%* | 22 · -5%* | 34 · +1% | 41 · +7% | 51 · -3% | 20 · -42%* |
| D | 5 · -24%* | 21 · +0%* | 32 · +8% | 47 · +2% | 57 · -3% | 14 · -5%* |
| L | 3 · -37%* | 22 · -4%* | 34 · +1% | 49 · -2% | 54 · -1% | 17 · -21%* |
| D+conf | 2 · -4%* | 5 · -23%* | 8 · +20%* | 13 · +18%* | 16 · +8%* | 6 · +27%* |
| D+fade | 3 · -38%* | 10 · -5%* | 17 · +1%* | 22 · -5%* | 23 · -9%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 59. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | -0.030 (n=33) | -0.171 (n=35) | -0.029 (n=34) | -0.088 (n=34) | -0.333 (n=6) | +0.000 (n=18) |
| spread · B | +0.216 (n=37) | +0.030 (n=33) | +0.000 (n=36) | +0.081 (n=37) | +0.143 (n=7) | +0.000 (n=16) |
| ml · A | -0.005 (n=30) | -0.003 (n=36) | +0.001 (n=35) | +0.000 (n=35) | +0.000 (n=10) | +0.000 (n=18) |
| ml · B | +0.007 (n=33) | +0.002 (n=41) | +0.001 (n=42) | -0.000 (n=40) | +0.002 (n=10) | +0.001 (n=18) |
| total · T | +1.370 (n=27) | +0.471 (n=34) | +0.062 (n=32) | -0.176 (n=34) | +0.000 (n=8) | +0.059 (n=17) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 63 | -0.594 (-1.03) | – | – | – |
| spread · A · D | 71 | -0.376 (-0.72) | – | – | – |
| spread · B · E | 63 | -0.845 (-1.61) | – | – | – |
| spread · B · D | 71 | -0.767 (-1.42) | – | – | – |
| ml · A · E | 63 | – | 0.2001 | 0.1861 | +0.0141 (1.58) |
| ml · A · D | 71 | – | 0.2029 | 0.1865 | +0.0164 (1.94) |
| ml · B · E | 63 | – | 0.2112 | 0.1861 | +0.0251 (2.51) |
| ml · B · D | 71 | – | 0.2100 | 0.1865 | +0.0235 (2.61) |
| total · T · E | 63 | -0.027 (-0.04) | – | – | – |
| total · T · D | 71 | -0.217 (-0.34) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._