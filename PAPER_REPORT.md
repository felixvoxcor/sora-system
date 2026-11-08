# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **65** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 12 · -5%* | 22 · -5%* | 30 · -4% | 40 · -14% | 46 · -9% | 11 · +39%* |
| H6 | 12 · -53%* | 21 · -10%* | 32 · -10% | 47 · -7% | 55 · -3% | 10 · -24%* |
| D | 13 · -27%* | 22 · +4%* | 30 · -5% | 45 · +2% | 58 · +2% | 7 · -19%* |
| L | 13 · -40%* | 21 · -17%* | 30 · -4% | 44 · +13% | 55 · +4% | 10 · -81%* |
| D+conf | 1 · -100%* | 4 · -4%* | 6 · +29%* | 9 · +8%* | 10 · -3%* | 2 · -100%* |
| D+fade | 9 · +6%* | 13 · +32%* | 15 · +27%* | 20 · +23%* | 20 · +23%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 13 · -41%* | 22 · -22%* | 35 · -7% | 44 · -9% | 51 · +1% | 6 · -67%* |
| H6 | 13 · -12%* | 20 · -5%* | 31 · -14% | 55 · -13% | 60 · -14% | 5 · -61%* |
| D | 13 · -26%* | 23 · -16%* | 34 · -4% | 52 · -8% | 59 · -6% | 6 · -36%* |
| L | 13 · -42%* | 24 · -28%* | 34 · -21% | 46 · -21% | 57 · -19% | 8 · -29%* |
| D+conf | 2 · -100%* | 5 · -61%* | 7 · -17%* | 15 · -23%* | 15 · -23%* | – |
| D+fade | 5 · +16%* | 9 · +28%* | 14 · +36%* | 18 · +27%* | 19 · +20%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 15 · -36%* | 23 · -33%* | 27 · -27%* | 42 · -17% | 52 · -19% | 5 · +36%* |
| H6 | 12 · -100%* | 25 · -39%* | 33 · -38% | 49 · -22% | 53 · -18% | 12 · +10%* |
| D | 11 · -100%* | 26 · -40%* | 31 · -33% | 47 · -14% | 55 · -14% | 10 · -43%* |
| L | 15 · -67%* | 24 · -42%* | 31 · -42% | 45 · -7% | 52 · -17% | 13 · -11%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 11 · +19%* | 12 · +34%* | 3 · -56%* |
| D+fade | 8 · -100%* | 13 · -40%* | 14 · -45%* | 18 · -20%* | 19 · -24%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 14 · -58%* | 25 · -56%* | 32 · -41% | 46 · -32% | 51 · -25% | 6 · +42%* |
| H6 | 13 · -63%* | 22 · -50%* | 38 · -39% | 54 · -38% | 60 · -37% | 5 · +3%* |
| D | 12 · -60%* | 24 · -58%* | 38 · -41% | 56 · -35% | 63 · -36% | 2 · -18%* |
| L | 14 · -52%* | 24 · -60%* | 38 · -56% | 52 · -44% | 58 · -41% | 7 · +41%* |
| D+conf | 1 · -100%* | 4 · -100%* | 10 · -53%* | 14 · -57%* | 15 · -48%* | – |
| D+fade | 7 · -58%* | 10 · -48%* | 14 · -45%* | 18 · -23%* | 18 · -23%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 8 · +20%* | 21 · +9%* | 25 · +14%* | 33 · -13% | 49 · -14% | 8 · -4%* |
| H6 | 7 · +9%* | 21 · -9%* | 31 · +4% | 38 · +10% | 48 · -1% | 17 · -55%* |
| D | 5 · -24%* | 20 · -4%* | 30 · +2% | 43 · +2% | 52 · -4% | 13 · -12%* |
| L | 3 · -37%* | 21 · -9%* | 33 · -2% | 45 · -2% | 50 · -1% | 15 · -24%* |
| D+conf | 2 · -4%* | 5 · -23%* | 8 · +20%* | 12 · +28%* | 15 · +15%* | 5 · +14%* |
| D+fade | 3 · -38%* | 9 · -15%* | 15 · -11%* | 19 · -10%* | 20 · -14%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 58. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.033 (n=30) | -0.188 (n=32) | -0.033 (n=30) | -0.100 (n=30) | -0.333 (n=6) | +0.000 (n=15) |
| spread · B | +0.257 (n=35) | +0.032 (n=31) | +0.000 (n=34) | +0.088 (n=34) | +0.143 (n=7) | +0.000 (n=14) |
| ml · A | -0.003 (n=27) | -0.004 (n=33) | +0.002 (n=31) | +0.000 (n=31) | +0.000 (n=10) | +0.001 (n=14) |
| ml · B | +0.008 (n=32) | +0.003 (n=38) | +0.001 (n=38) | -0.000 (n=38) | +0.002 (n=10) | +0.001 (n=14) |
| total · T | +1.360 (n=25) | +0.419 (n=31) | +0.000 (n=30) | -0.182 (n=33) | +0.000 (n=8) | -0.067 (n=15) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 57 | -0.471 (-0.80) | – | – | – |
| spread · A · D | 65 | -0.287 (-0.54) | – | – | – |
| spread · B · E | 57 | -0.753 (-1.41) | – | – | – |
| spread · B · D | 65 | -0.617 (-1.11) | – | – | – |
| ml · A · E | 57 | – | 0.2027 | 0.1875 | +0.0152 (1.60) |
| ml · A · D | 65 | – | 0.2052 | 0.1893 | +0.0159 (1.82) |
| ml · B · E | 57 | – | 0.2135 | 0.1875 | +0.0260 (2.39) |
| ml · B · D | 65 | – | 0.2125 | 0.1893 | +0.0232 (2.44) |
| total · T · E | 57 | +0.121 (0.17) | – | – | – |
| total · T · D | 65 | -0.216 (-0.33) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._