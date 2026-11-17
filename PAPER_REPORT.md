# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **137** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 20 · +5%* | 43 · +2% | 62 · -7% | 89 · -23% | 100 · -20% | 16 · +20%* |
| H6 | 24 · -13%* | 49 · -3% | 75 · +1% | 104 · -3% | 116 · -1% | 21 · -1%* |
| D | 29 · -8%* | 50 · +6% | 74 · +5% | 104 · +1% | 122 · -0% | 15 · +14%* |
| L | 27 · -22%* | 50 · -8% | 71 · +2% | 98 · +5% | 115 · -0% | 22 · -30%* |
| D+conf | 2 · -7%* | 8 · -4%* | 13 · +33%* | 19 · +11%* | 22 · -4%* | 4 · -53%* |
| D+fade | 17 · -11%* | 23 · +7%* | 31 · +10% | 39 · +7% | 39 · +7% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 26 · -41%* | 43 · -29% | 65 · -15% | 89 · -21% | 102 · -12% | 14 · -32%* |
| H6 | 30 · -6% | 51 · -3% | 72 · -13% | 106 · -12% | 122 · -11% | 15 · -48%* |
| D | 31 · -14% | 53 · -6% | 73 · -3% | 106 · -8% | 125 · -8% | 12 · -36%* |
| L | 27 · -29%* | 53 · -17% | 71 · -17% | 92 · -11% | 115 · -15% | 22 · -48%* |
| D+conf | 3 · -100%* | 7 · -45%* | 13 · -12%* | 23 · -16%* | 28 · -25%* | 1 · -100%* |
| D+fade | 13 · -12%* | 20 · -5%* | 27 · +6%* | 35 · -2% | 36 · -5% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · -44%* | 42 · -20% | 59 · -25% | 88 · -26% | 106 · -29% | 10 · +69%* |
| H6 | 31 · -57% | 57 · -33% | 74 · -30% | 106 · -15% | 115 · -16% | 22 · -16%* |
| D | 30 · -47% | 55 · -28% | 75 · -18% | 103 · -13% | 120 · -13% | 17 · -43%* |
| L | 34 · -50% | 53 · -35% | 74 · -16% | 103 · -9% | 118 · -16% | 19 · -22%* |
| D+conf | 1 · -100%* | 9 · -31%* | 15 · -14%* | 21 · -25%* | 25 · -5%* | 4 · -67%* |
| D+fade | 21 · -46%* | 32 · -31% | 39 · -43% | 45 · -32% | 46 · -33% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 25 · -45%* | 45 · -36% | 61 · -33% | 86 · -31% | 96 · -29% | 20 · -31%* |
| H6 | 32 · -52% | 53 · -20% | 82 · -16% | 110 · -26% | 124 · -22% | 13 · -26%* |
| D | 30 · -53% | 52 · -35% | 79 · -18% | 113 · -19% | 123 · -18% | 14 · -40%* |
| L | 33 · -32% | 49 · -38% | 72 · -38% | 101 · -25% | 120 · -26% | 17 · +32%* |
| D+conf | 1 · -100%* | 5 · -72%* | 15 · -42%* | 22 · -54%* | 24 · -43%* | 4 · -100%* |
| D+fade | 22 · -79%* | 29 · -50%* | 38 · -41% | 46 · -37% | 46 · -37% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 14 · -4%* | 39 · +3% | 50 · +7% | 67 · -0% | 93 · +0% | 23 · -8%* |
| H6 | 12 · -21%* | 37 · -7% | 60 · -5% | 72 · +3% | 99 · +4% | 38 · -14% |
| D | 11 · -48%* | 36 · +1% | 58 · +6% | 80 · +5% | 106 · +4% | 31 · +11% |
| L | 10 · -43%* | 41 · -2% | 60 · +5% | 84 · +5% | 102 · +9% | 35 · -19% |
| D+conf | 2 · -4%* | 8 · +19%* | 17 · +24%* | 25 · +30%* | 31 · +30% | 15 · +27%* |
| D+fade | 6 · -69%* | 14 · -32%* | 22 · -13%* | 28 · -12%* | 31 · -8% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 102. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.081 (n=62) | -0.093 (n=75) | -0.027 (n=74) | -0.028 (n=71) | -0.077 (n=13) | -0.097 (n=31) |
| spread · B | +0.138 (n=65) | -0.139 (n=72) | -0.082 (n=73) | +0.028 (n=71) | -0.231 (n=13) | -0.074 (n=27) |
| ml · A | -0.002 (n=59) | -0.002 (n=74) | +0.001 (n=75) | +0.000 (n=74) | +0.002 (n=15) | -0.002 (n=39) |
| ml · B | +0.000 (n=61) | -0.003 (n=82) | -0.003 (n=79) | +0.000 (n=72) | -0.006 (n=15) | -0.003 (n=38) |
| total · T | +1.500 (n=50) | +0.450 (n=60) | +0.103 (n=58) | -0.067 (n=60) | +0.059 (n=17) | +0.136 (n=22) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 116 | -0.672 (-1.42) | – | – | – |
| spread · A · D | 137 | -0.360 (-0.91) | – | – | – |
| spread · B · E | 116 | -0.954 (-2.24) | – | – | – |
| spread · B · D | 137 | -0.640 (-1.55) | – | – | – |
| ml · A · E | 116 | – | 0.2002 | 0.1858 | +0.0145 (2.31) |
| ml · A · D | 137 | – | 0.1997 | 0.1878 | +0.0119 (1.82) |
| ml · B · E | 116 | – | 0.2053 | 0.1858 | +0.0195 (2.82) |
| ml · B · D | 137 | – | 0.2021 | 0.1878 | +0.0143 (2.22) |
| total · T · E | 116 | +0.693 (1.60) | – | – | – |
| total · T · D | 137 | +0.329 (0.80) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._