# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **173** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · +0%* | 48 · -5% | 71 · -17% | 109 · -30% | 126 · -23% | 24 · -12%* |
| H6 | 25 · -17%* | 53 · -11% | 90 · -7% | 131 · -13% | 145 · -9% | 28 · -12%* |
| D | 31 · -14% | 56 · -5% | 92 · -5% | 128 · -9% | 152 · -8% | 21 · -0%* |
| L | 31 · -26% | 58 · -14% | 84 · -5% | 121 · -1% | 142 · -3% | 28 · -38%* |
| D+conf | 3 · -38%* | 9 · -15%* | 15 · +28%* | 21 · +10%* | 26 · -4%* | 7 · -17%* |
| D+fade | 18 · -16%* | 26 · -5%* | 38 · -0% | 48 · -5% | 49 · -7% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 29 · -34%* | 48 · -28% | 77 · -16% | 112 · -18% | 130 · -9% | 20 · -33%* |
| H6 | 35 · -3% | 60 · -5% | 88 · -9% | 132 · -9% | 154 · -7% | 19 · -29%* |
| D | 34 · -10% | 59 · -3% | 93 · -2% | 134 · -6% | 160 · -6% | 13 · -26%* |
| L | 30 · -24% | 61 · -10% | 89 · -8% | 116 · -3% | 144 · -7% | 26 · -42%* |
| D+conf | 3 · -100%* | 8 · -29%* | 14 · -4%* | 27 · -7%* | 34 · -10% | 1 · -100%* |
| D+fade | 14 · -4%* | 21 · -0%* | 35 · -2% | 44 · -10% | 45 · -12% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 25 · -48%* | 46 · -27% | 68 · -32% | 109 · -27% | 133 · -29% | 17 · +22%* |
| H6 | 32 · -58% | 63 · -22% | 85 · -24% | 135 · -19% | 150 · -19% | 23 · -12%* |
| D | 32 · -50% | 62 · -29% | 89 · -21% | 129 · -17% | 152 · -16% | 21 · -54%* |
| L | 38 · -50% | 60 · -32% | 88 · -13% | 124 · -9% | 144 · -15% | 25 · -23%* |
| D+conf | 2 · -100%* | 10 · -38%* | 16 · -19%* | 27 · -16%* | 33 · -7% | 5 · -74%* |
| D+fade | 22 · -49%* | 36 · -26% | 45 · -41% | 57 · -36% | 58 · -37% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 29 · -52%* | 50 · -43% | 73 · -33% | 112 · -30% | 127 · -28% | 23 · -40%* |
| H6 | 38 · -60% | 65 · -27% | 97 · -21% | 135 · -22% | 154 · -17% | 19 · -42%* |
| D | 34 · -42% | 61 · -32% | 94 · -16% | 138 · -17% | 152 · -15% | 21 · -39%* |
| L | 36 · -22% | 57 · -34% | 88 · -30% | 123 · -20% | 145 · -22% | 24 · +29%* |
| D+conf | 1 · -100%* | 5 · -72%* | 15 · -42%* | 25 · -48%* | 28 · -30%* | 9 · -52%* |
| D+fade | 24 · -81%* | 33 · -51% | 45 · -39% | 57 · -35% | 57 · -35% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · -15%* | 47 · -7% | 62 · -8% | 88 · -11% | 121 · -4% | 29 · -27%* |
| H6 | 15 · -36%* | 47 · -19% | 74 · -15% | 93 · -8% | 125 · -7% | 48 · -4% |
| D | 13 · -56%* | 47 · -15% | 75 · -8% | 102 · -10% | 133 · -5% | 40 · +5% |
| L | 14 · -45%* | 49 · -10% | 72 · -2% | 104 · -8% | 128 · -2% | 42 · -19% |
| D+conf | 2 · -4%* | 10 · +14%* | 21 · +9%* | 30 · +15% | 38 · +21% | 16 · +19%* |
| D+fade | 7 · -73%* | 20 · -43%* | 32 · -22% | 39 · -22% | 42 · -18% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 112. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.254 (n=71) | +0.011 (n=90) | +0.011 (n=92) | -0.048 (n=84) | -0.067 (n=15) | -0.079 (n=38) |
| spread · B | +0.221 (n=77) | -0.136 (n=88) | -0.032 (n=93) | -0.011 (n=89) | -0.214 (n=14) | -0.057 (n=35) |
| ml · A | +0.002 (n=68) | -0.002 (n=85) | -0.001 (n=89) | +0.001 (n=88) | +0.002 (n=16) | -0.002 (n=45) |
| ml · B | -0.003 (n=73) | -0.004 (n=97) | -0.003 (n=94) | -0.000 (n=88) | -0.006 (n=15) | -0.003 (n=45) |
| total · T | +1.323 (n=62) | +0.405 (n=74) | +0.067 (n=75) | -0.028 (n=72) | -0.143 (n=21) | +0.094 (n=32) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 150 | -0.760 (-1.78) | – | – | – |
| spread · A · D | 173 | -0.407 (-1.13) | – | – | – |
| spread · B · E | 150 | -0.930 (-2.41) | – | – | – |
| spread · B · D | 173 | -0.518 (-1.39) | – | – | – |
| ml · A · E | 150 | – | 0.2106 | 0.1957 | +0.0149 (2.91) |
| ml · A · D | 173 | – | 0.2069 | 0.1938 | +0.0132 (2.41) |
| ml · B · E | 150 | – | 0.2132 | 0.1957 | +0.0175 (3.06) |
| ml · B · D | 173 | – | 0.2072 | 0.1938 | +0.0134 (2.43) |
| total · T · E | 150 | +0.299 (0.77) | – | – | – |
| total · T · D | 173 | -0.114 (-0.30) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._