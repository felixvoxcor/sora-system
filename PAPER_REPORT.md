# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **170** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · +0%* | 48 · -5% | 71 · -17% | 107 · -29% | 123 · -22% | 24 · -12%* |
| H6 | 25 · -17%* | 52 · -9% | 88 · -7% | 129 · -13% | 143 · -9% | 27 · -9%* |
| D | 31 · -14% | 55 · -3% | 91 · -4% | 127 · -9% | 151 · -8% | 19 · +0%* |
| L | 31 · -26% | 57 · -13% | 83 · -3% | 119 · -0% | 140 · -3% | 27 · -36%* |
| D+conf | 3 · -38%* | 9 · -15%* | 15 · +28%* | 21 · +10%* | 26 · -4%* | 5 · -23%* |
| D+fade | 18 · -16%* | 25 · -1%* | 37 · +2% | 47 · -3% | 48 · -5% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 29 · -34%* | 48 · -28% | 76 · -15% | 109 · -18% | 127 · -8% | 20 · -33%* |
| H6 | 34 · +0% | 59 · -4% | 86 · -10% | 130 · -9% | 151 · -8% | 19 · -29%* |
| D | 34 · -10% | 59 · -3% | 90 · -3% | 131 · -7% | 157 · -7% | 13 · -26%* |
| L | 29 · -28%* | 60 · -11% | 87 · -8% | 113 · -4% | 141 · -8% | 26 · -42%* |
| D+conf | 3 · -100%* | 8 · -29%* | 14 · -4%* | 27 · -7%* | 34 · -10% | 1 · -100%* |
| D+fade | 14 · -4%* | 21 · -0%* | 33 · -2% | 42 · -10% | 43 · -12% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 25 · -48%* | 46 · -27% | 67 · -31% | 107 · -31% | 130 · -32% | 17 · +22%* |
| H6 | 32 · -58% | 61 · -30% | 83 · -30% | 133 · -23% | 147 · -22% | 23 · -12%* |
| D | 32 · -50% | 61 · -27% | 88 · -20% | 127 · -20% | 150 · -19% | 20 · -52%* |
| L | 38 · -50% | 59 · -31% | 86 · -18% | 122 · -12% | 142 · -18% | 24 · -20%* |
| D+conf | 2 · -100%* | 10 · -38%* | 16 · -19%* | 26 · -33%* | 32 · -21% | 4 · -67%* |
| D+fade | 22 · -49%* | 36 · -26% | 45 · -41% | 57 · -36% | 58 · -37% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 28 · -51%* | 49 · -42% | 72 · -32% | 110 · -30% | 124 · -27% | 23 · -40%* |
| H6 | 37 · -59% | 64 · -26% | 96 · -20% | 132 · -27% | 151 · -21% | 19 · -42%* |
| D | 33 · -57% | 60 · -40% | 91 · -21% | 135 · -21% | 149 · -18% | 21 · -39%* |
| L | 35 · -36% | 56 · -43% | 86 · -35% | 120 · -24% | 142 · -26% | 24 · +29%* |
| D+conf | 1 · -100%* | 5 · -72%* | 15 · -42%* | 25 · -48%* | 28 · -30%* | 9 · -52%* |
| D+fade | 24 · -81%* | 33 · -51% | 44 · -41% | 56 · -37% | 56 · -37% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · -15%* | 46 · -5% | 60 · -5% | 86 · -9% | 118 · -1% | 29 · -27%* |
| H6 | 15 · -36%* | 47 · -19% | 74 · -15% | 91 · -6% | 123 · -6% | 47 · -2% |
| D | 13 · -56%* | 46 · -13% | 73 · -6% | 100 · -8% | 131 · -4% | 39 · +8% |
| L | 14 · -45%* | 49 · -10% | 72 · -2% | 102 · -6% | 126 · +0% | 41 · -17% |
| D+conf | 2 · -4%* | 10 · +14%* | 20 · +15%* | 29 · +19%* | 37 · +24% | 15 · +27%* |
| D+fade | 7 · -73%* | 19 · -40%* | 31 · -20% | 38 · -20% | 41 · -16% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 110. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.254 (n=71) | +0.011 (n=88) | +0.022 (n=91) | -0.036 (n=83) | -0.067 (n=15) | -0.054 (n=37) |
| spread · B | +0.263 (n=76) | -0.128 (n=86) | -0.011 (n=90) | +0.000 (n=87) | -0.214 (n=14) | -0.030 (n=33) |
| ml · A | +0.002 (n=67) | -0.002 (n=83) | -0.001 (n=88) | +0.001 (n=86) | +0.002 (n=16) | -0.002 (n=45) |
| ml · B | -0.003 (n=72) | -0.004 (n=96) | -0.003 (n=91) | -0.000 (n=86) | -0.006 (n=15) | -0.004 (n=44) |
| total · T | +1.367 (n=60) | +0.405 (n=74) | +0.068 (n=73) | -0.028 (n=72) | -0.050 (n=20) | +0.032 (n=31) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 147 | -0.744 (-1.72) | – | – | – |
| spread · A · D | 170 | -0.389 (-1.06) | – | – | – |
| spread · B · E | 147 | -0.901 (-2.30) | – | – | – |
| spread · B · D | 170 | -0.534 (-1.42) | – | – | – |
| ml · A · E | 147 | – | 0.2094 | 0.1940 | +0.0154 (2.97) |
| ml · A · D | 170 | – | 0.2060 | 0.1923 | +0.0136 (2.46) |
| ml · B · E | 147 | – | 0.2118 | 0.1940 | +0.0179 (3.07) |
| ml · B · D | 170 | – | 0.2070 | 0.1923 | +0.0147 (2.66) |
| total · T · E | 147 | +0.396 (1.01) | – | – | – |
| total · T · D | 170 | -0.043 (-0.11) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._