# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **178** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 22 · +4%* | 49 · -3% | 74 · -15% | 113 · -27% | 130 · -21% | 24 · -12%* |
| H6 | 27 · -16%* | 55 · -10% | 93 · -6% | 135 · -11% | 149 · -8% | 29 · -8%* |
| D | 32 · -11% | 58 · -5% | 94 · -5% | 132 · -8% | 156 · -7% | 22 · +4%* |
| L | 33 · -25% | 60 · -14% | 86 · -5% | 125 · +1% | 146 · -2% | 29 · -34%* |
| D+conf | 3 · -38%* | 9 · -15%* | 15 · +28%* | 22 · +13%* | 27 · -0%* | 8 · -4%* |
| D+fade | 19 · -10%* | 28 · -5%* | 40 · -1% | 50 · -5% | 51 · -7% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 30 · -30% | 51 · -21% | 81 · -10% | 116 · -14% | 134 · -6% | 20 · -33%* |
| H6 | 36 · -0% | 62 · -2% | 90 · -7% | 137 · -5% | 159 · -4% | 19 · -29%* |
| D | 34 · -10% | 60 · -2% | 95 · +0% | 139 · -4% | 165 · -4% | 13 · -26%* |
| L | 30 · -24% | 62 · -8% | 92 · -5% | 120 · -0% | 148 · -5% | 27 · -44%* |
| D+conf | 3 · -100%* | 9 · -16%* | 16 · +7%* | 30 · +2% | 37 · -2% | 1 · -100%* |
| D+fade | 14 · -4%* | 21 · -0%* | 35 · -2% | 45 · -7% | 46 · -9% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 26 · -50%* | 47 · -29% | 71 · -31% | 112 · -26% | 136 · -28% | 18 · +27%* |
| H6 | 33 · -60% | 65 · -24% | 88 · -24% | 139 · -18% | 154 · -18% | 24 · -7%* |
| D | 34 · -53% | 64 · -31% | 92 · -21% | 132 · -17% | 156 · -17% | 22 · -56%* |
| L | 40 · -53% | 62 · -34% | 91 · -13% | 127 · -9% | 148 · -16% | 26 · -26%* |
| D+conf | 2 · -100%* | 10 · -38%* | 16 · -19%* | 27 · -16%* | 33 · -7% | 5 · -74%* |
| D+fade | 24 · -53%* | 38 · -30% | 47 · -43% | 59 · -38% | 60 · -39% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 30 · -48% | 52 · -42% | 77 · -28% | 116 · -26% | 131 · -25% | 23 · -40%* |
| H6 | 39 · -56% | 67 · -23% | 102 · -16% | 140 · -19% | 159 · -14% | 19 · -42%* |
| D | 34 · -42% | 61 · -32% | 99 · -12% | 143 · -15% | 157 · -13% | 21 · -39%* |
| L | 36 · -22% | 58 · -31% | 91 · -27% | 127 · -18% | 150 · -20% | 24 · +29%* |
| D+conf | 1 · -100%* | 5 · -72%* | 16 · -35%* | 26 · -44%* | 29 · -27%* | 9 · -52%* |
| D+fade | 24 · -81%* | 33 · -51% | 46 · -40% | 58 · -37% | 58 · -37% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · -15%* | 49 · -7% | 64 · -8% | 90 · -11% | 123 · -4% | 31 · -32% |
| H6 | 15 · -36%* | 48 · -21% | 75 · -16% | 97 · -8% | 130 · -6% | 48 · -4% |
| D | 13 · -56%* | 48 · -16% | 76 · -9% | 105 · -11% | 137 · -5% | 41 · +2% |
| L | 15 · -36%* | 51 · -10% | 74 · -2% | 107 · -9% | 133 · -2% | 42 · -19% |
| D+conf | 2 · -4%* | 10 · +14%* | 21 · +9%* | 30 · +15% | 38 · +21% | 17 · +12%* |
| D+fade | 7 · -73%* | 21 · -45%* | 33 · -25% | 41 · -26% | 44 · -22% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 115. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.216 (n=74) | +0.054 (n=93) | +0.011 (n=94) | -0.035 (n=86) | -0.067 (n=15) | -0.075 (n=40) |
| spread · B | +0.235 (n=81) | -0.100 (n=90) | -0.032 (n=95) | -0.011 (n=92) | -0.188 (n=16) | -0.057 (n=35) |
| ml · A | +0.000 (n=71) | -0.002 (n=88) | -0.001 (n=92) | +0.001 (n=91) | +0.002 (n=16) | -0.002 (n=47) |
| ml · B | -0.003 (n=77) | -0.003 (n=102) | -0.003 (n=99) | -0.001 (n=91) | -0.004 (n=16) | -0.003 (n=46) |
| total · T | +1.156 (n=64) | +0.387 (n=75) | +0.053 (n=76) | -0.027 (n=74) | -0.143 (n=21) | +0.061 (n=33) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 154 | -0.695 (-1.65) | – | – | – |
| spread · A · D | 178 | -0.391 (-1.11) | – | – | – |
| spread · B · E | 154 | -0.821 (-2.14) | – | – | – |
| spread · B · D | 178 | -0.482 (-1.31) | – | – | – |
| ml · A · E | 154 | – | 0.2119 | 0.1969 | +0.0150 (2.96) |
| ml · A · D | 178 | – | 0.2082 | 0.1945 | +0.0137 (2.55) |
| ml · B · E | 154 | – | 0.2126 | 0.1969 | +0.0158 (2.76) |
| ml · B · D | 178 | – | 0.2062 | 0.1945 | +0.0118 (2.18) |
| total · T · E | 154 | +0.275 (0.69) | – | – | – |
| total · T · D | 178 | -0.171 (-0.45) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._