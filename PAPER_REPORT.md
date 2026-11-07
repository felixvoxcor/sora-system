# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **64** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 12 · -5%* | 21 · -0%* | 29 · -1%* | 39 · -12% | 45 · -7% | 11 · +39%* |
| H6 | 11 · -48%* | 20 · -5%* | 31 · -8% | 46 · -5% | 54 · -1% | 10 · -24%* |
| D | 12 · -21%* | 21 · +9%* | 29 · -1%* | 44 · +4% | 57 · +4% | 7 · -19%* |
| L | 12 · -36%* | 20 · -13%* | 29 · -0%* | 43 · +15% | 54 · +6% | 10 · -81%* |
| D+conf | 1 · -100%* | 4 · -4%* | 6 · +29%* | 9 · +8%* | 10 · -3%* | 2 · -100%* |
| D+fade | 8 · +19%* | 12 · +43%* | 14 · +36%* | 19 · +30%* | 19 · +30%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 13 · -41%* | 22 · -22%* | 35 · -7% | 44 · -9% | 50 · -1% | 6 · -67%* |
| H6 | 13 · -12%* | 20 · -5%* | 31 · -14% | 55 · -13% | 60 · -14% | 4 · -51%* |
| D | 13 · -26%* | 23 · -16%* | 34 · -4% | 52 · -8% | 59 · -6% | 5 · -23%* |
| L | 13 · -42%* | 24 · -28%* | 34 · -21% | 45 · -19% | 56 · -18% | 8 · -29%* |
| D+conf | 2 · -100%* | 5 · -61%* | 7 · -17%* | 15 · -23%* | 15 · -23%* | – |
| D+fade | 5 · +16%* | 9 · +28%* | 14 · +36%* | 18 · +27%* | 19 · +20%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 15 · -36%* | 23 · -33%* | 26 · -24%* | 41 · -15% | 51 · -17% | 5 · +36%* |
| H6 | 12 · -100%* | 24 · -36%* | 32 · -36% | 48 · -20% | 52 · -17% | 12 · +10%* |
| D | 10 · -100%* | 25 · -38%* | 30 · -31% | 46 · -12% | 54 · -13% | 10 · -43%* |
| L | 14 · -65%* | 23 · -39%* | 30 · -40% | 44 · -5% | 51 · -16% | 13 · -11%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 11 · +19%* | 12 · +34%* | 3 · -56%* |
| D+fade | 7 · -100%* | 12 · -36%* | 13 · -40%* | 17 · -15%* | 18 · -20%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 14 · -58%* | 25 · -56%* | 32 · -41% | 46 · -32% | 50 · -26% | 6 · +42%* |
| H6 | 13 · -63%* | 22 · -50%* | 38 · -39% | 54 · -38% | 60 · -37% | 4 · +29%* |
| D | 12 · -60%* | 24 · -58%* | 38 · -41% | 55 · -34% | 62 · -35% | 2 · -18%* |
| L | 14 · -52%* | 24 · -60%* | 37 · -55% | 51 · -43% | 57 · -40% | 7 · +41%* |
| D+conf | 1 · -100%* | 4 · -100%* | 10 · -53%* | 14 · -57%* | 15 · -48%* | – |
| D+fade | 7 · -58%* | 10 · -48%* | 14 · -45%* | 18 · -23%* | 18 · -23%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 8 · +20%* | 21 · +9%* | 25 · +14%* | 33 · -13% | 48 · -13% | 8 · -4%* |
| H6 | 7 · +9%* | 21 · -9%* | 31 · +4% | 38 · +10% | 48 · -1% | 16 · -52%* |
| D | 5 · -24%* | 20 · -4%* | 30 · +2% | 43 · +2% | 52 · -4% | 12 · -5%* |
| L | 3 · -37%* | 21 · -9%* | 33 · -2% | 45 · -2% | 50 · -1% | 14 · -19%* |
| D+conf | 2 · -4%* | 5 · -23%* | 8 · +20%* | 12 · +28%* | 15 · +15%* | 4 · +43%* |
| D+fade | 3 · -38%* | 9 · -15%* | 15 · -11%* | 19 · -10%* | 20 · -14%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 55. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.103 (n=29) | -0.161 (n=31) | +0.000 (n=29) | -0.069 (n=29) | -0.333 (n=6) | +0.071 (n=14) |
| spread · B | +0.257 (n=35) | +0.032 (n=31) | +0.000 (n=34) | +0.088 (n=34) | +0.143 (n=7) | +0.000 (n=14) |
| ml · A | -0.001 (n=26) | -0.003 (n=32) | +0.002 (n=30) | +0.000 (n=30) | +0.000 (n=10) | +0.001 (n=13) |
| ml · B | +0.008 (n=32) | +0.003 (n=38) | +0.001 (n=38) | -0.000 (n=37) | +0.002 (n=10) | +0.001 (n=14) |
| total · T | +1.360 (n=25) | +0.419 (n=31) | +0.000 (n=30) | -0.182 (n=33) | +0.000 (n=8) | -0.067 (n=15) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 56 | -0.450 (-0.75) | – | – | – |
| spread · A · D | 64 | -0.270 (-0.50) | – | – | – |
| spread · B · E | 56 | -0.769 (-1.43) | – | – | – |
| spread · B · D | 64 | -0.623 (-1.12) | – | – | – |
| ml · A · E | 56 | – | 0.2035 | 0.1889 | +0.0145 (1.50) |
| ml · A · D | 64 | – | 0.2059 | 0.1911 | +0.0148 (1.68) |
| ml · B · E | 56 | – | 0.2157 | 0.1889 | +0.0267 (2.41) |
| ml · B · D | 64 | – | 0.2144 | 0.1911 | +0.0233 (2.41) |
| total · T · E | 56 | +0.174 (0.24) | – | – | – |
| total · T · D | 64 | -0.192 (-0.29) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._