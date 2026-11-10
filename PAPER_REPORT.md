# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **83** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 15 · +15%* | 30 · +2% | 42 · -4% | 57 · -19% | 63 · -15% | 12 · +28%* |
| H6 | 17 · -44%* | 30 · -11% | 45 · -2% | 61 · -3% | 70 · -2% | 13 · -26%* |
| D | 19 · -30%* | 31 · +4% | 45 · +6% | 62 · +5% | 76 · +5% | 7 · -19%* |
| L | 20 · -33%* | 32 · -4% | 45 · +7% | 61 · +13% | 72 · +6% | 11 · -83%* |
| D+conf | 1 · -100%* | 4 · -4%* | 7 · +39%* | 11 · +6%* | 12 · -3%* | 2 · -100%* |
| D+fade | 14 · -19%* | 18 · +6%* | 22 · +12%* | 27 · +12%* | 27 · +12%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 15 · -49%* | 25 · -31%* | 41 · -11% | 55 · -13% | 64 · -2% | 11 · -47%* |
| H6 | 17 · -22%* | 28 · -5%* | 40 · -14% | 68 · -10% | 76 · -7% | 7 · -45%* |
| D | 18 · -25%* | 31 · -13% | 43 · -2% | 67 · -6% | 75 · -3% | 8 · -28%* |
| L | 17 · -44%* | 32 · -23% | 43 · -20% | 58 · -18% | 70 · -15% | 13 · -56%* |
| D+conf | 2 · -100%* | 5 · -61%* | 7 · -17%* | 16 · -15%* | 16 · -15%* | – |
| D+fade | 9 · +7%* | 14 · +9%* | 20 · +24%* | 25 · +14%* | 26 · +10%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 19 · -32%* | 30 · -28% | 40 · -19% | 58 · -16% | 69 · -19% | 6 · +14%* |
| H6 | 19 · -81%* | 34 · -30% | 44 · -29% | 64 · -14% | 68 · -12% | 15 · +5%* |
| D | 18 · -79%* | 34 · -34% | 43 · -20% | 62 · -8% | 72 · -7% | 11 · -37%* |
| L | 22 · -60%* | 34 · -32% | 45 · -22% | 62 · -1% | 70 · -10% | 13 · -11%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 13 · +9%* | 16 · +23%* | 3 · -56%* |
| D+fade | 15 · -75%* | 21 · -30%* | 23 · -36%* | 27 · -21%* | 28 · -24%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 16 · -54%* | 29 · -53%* | 37 · -41% | 56 · -33% | 63 · -30% | 12 · -12%* |
| H6 | 19 · -66%* | 29 · -50%* | 48 · -35% | 67 · -34% | 76 · -29% | 7 · -10%* |
| D | 17 · -62%* | 31 · -63% | 49 · -38% | 70 · -30% | 79 · -28% | 4 · +3%* |
| L | 20 · -52%* | 31 · -60% | 45 · -57% | 63 · -37% | 74 · -37% | 9 · +25%* |
| D+conf | 1 · -100%* | 4 · -100%* | 11 · -46%* | 15 · -51%* | 16 · -44%* | – |
| D+fade | 11 · -73%* | 16 · -68%* | 22 · -51%* | 27 · -37%* | 27 · -37%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 9 · +6%* | 27 · +6%* | 32 · +7% | 45 · -7% | 63 · -6% | 12 · -4%* |
| H6 | 8 · -5%* | 26 · -12%* | 40 · -0% | 47 · +5% | 59 · -3% | 24 · -36%* |
| D | 6 · -37%* | 23 · -8%* | 38 · +6% | 53 · +1% | 67 · -3% | 16 · +7%* |
| L | 4 · -53%* | 26 · -12%* | 40 · +0% | 57 · -3% | 62 · -1% | 21 · -10%* |
| D+conf | 2 · -4%* | 5 · -23%* | 9 · +28%* | 14 · +23%* | 18 · +18%* | 8 · +43%* |
| D+fade | 3 · -38%* | 11 · -13%* | 19 · +0%* | 24 · -5%* | 25 · -9%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 72. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | -0.167 (n=42) | -0.267 (n=45) | -0.178 (n=45) | -0.044 (n=45) | -0.286 (n=7) | -0.227 (n=22) |
| spread · B | +0.122 (n=41) | -0.125 (n=40) | -0.070 (n=43) | +0.070 (n=43) | +0.143 (n=7) | -0.100 (n=20) |
| ml · A | -0.005 (n=40) | -0.005 (n=44) | -0.001 (n=43) | -0.000 (n=45) | +0.000 (n=10) | -0.004 (n=23) |
| ml · B | +0.003 (n=37) | -0.001 (n=48) | -0.002 (n=49) | +0.000 (n=45) | -0.001 (n=11) | -0.004 (n=22) |
| total · T | +1.438 (n=32) | +0.550 (n=40) | +0.132 (n=38) | -0.150 (n=40) | +0.000 (n=9) | +0.105 (n=19) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 75 | -0.504 (-0.95) | – | – | – |
| spread · A · D | 83 | -0.166 (-0.35) | – | – | – |
| spread · B · E | 75 | -0.902 (-1.78) | – | – | – |
| spread · B · D | 83 | -0.615 (-1.22) | – | – | – |
| ml · A · E | 75 | – | 0.1981 | 0.1844 | +0.0137 (1.62) |
| ml · A · D | 83 | – | 0.2006 | 0.1872 | +0.0134 (1.59) |
| ml · B · E | 75 | – | 0.2066 | 0.1844 | +0.0222 (2.57) |
| ml · B · D | 83 | – | 0.2073 | 0.1872 | +0.0201 (2.48) |
| total · T · E | 75 | +0.494 (0.84) | – | – | – |
| total · T · D | 83 | +0.117 (0.20) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._