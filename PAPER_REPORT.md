# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **175** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · +0%* | 48 · -5% | 72 · -18% | 111 · -29% | 128 · -22% | 24 · -12%* |
| H6 | 26 · -20%* | 54 · -12% | 91 · -8% | 132 · -13% | 146 · -10% | 29 · -8%* |
| D | 31 · -14% | 57 · -7% | 93 · -6% | 129 · -10% | 153 · -9% | 22 · +4%* |
| L | 32 · -28% | 59 · -16% | 85 · -6% | 122 · -1% | 143 · -4% | 29 · -34%* |
| D+conf | 3 · -38%* | 9 · -15%* | 15 · +28%* | 21 · +10%* | 26 · -4%* | 8 · -4%* |
| D+fade | 18 · -16%* | 27 · -9%* | 39 · -3% | 49 · -7% | 50 · -9% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 30 · -30% | 50 · -23% | 79 · -13% | 114 · -16% | 132 · -8% | 20 · -33%* |
| H6 | 35 · -3% | 61 · -4% | 89 · -8% | 134 · -8% | 156 · -6% | 19 · -29%* |
| D | 34 · -10% | 60 · -2% | 95 · +0% | 136 · -5% | 162 · -5% | 13 · -26%* |
| L | 30 · -24% | 62 · -8% | 91 · -6% | 118 · -2% | 146 · -6% | 26 · -42%* |
| D+conf | 3 · -100%* | 9 · -16%* | 16 · +7%* | 29 · -1%* | 36 · -5% | 1 · -100%* |
| D+fade | 14 · -4%* | 21 · -0%* | 35 · -2% | 44 · -10% | 45 · -12% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 25 · -48%* | 46 · -27% | 69 · -33% | 110 · -27% | 134 · -29% | 18 · +27%* |
| H6 | 32 · -58% | 64 · -23% | 86 · -25% | 136 · -20% | 151 · -20% | 24 · -7%* |
| D | 33 · -52% | 63 · -30% | 90 · -22% | 130 · -18% | 153 · -17% | 22 · -56%* |
| L | 39 · -52% | 61 · -33% | 89 · -14% | 125 · -10% | 145 · -16% | 26 · -26%* |
| D+conf | 2 · -100%* | 10 · -38%* | 16 · -19%* | 27 · -16%* | 33 · -7% | 5 · -74%* |
| D+fade | 23 · -51%* | 37 · -28% | 46 · -42% | 58 · -37% | 59 · -38% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 30 · -48% | 51 · -41% | 75 · -30% | 114 · -27% | 129 · -26% | 23 · -40%* |
| H6 | 38 · -60% | 66 · -25% | 99 · -19% | 137 · -21% | 156 · -16% | 19 · -42%* |
| D | 34 · -42% | 61 · -32% | 96 · -14% | 140 · -16% | 154 · -14% | 21 · -39%* |
| L | 36 · -22% | 58 · -31% | 89 · -28% | 125 · -18% | 147 · -21% | 24 · +29%* |
| D+conf | 1 · -100%* | 5 · -72%* | 16 · -35%* | 26 · -44%* | 29 · -27%* | 9 · -52%* |
| D+fade | 24 · -81%* | 33 · -51% | 45 · -39% | 57 · -35% | 57 · -35% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · -15%* | 48 · -5% | 63 · -6% | 89 · -10% | 122 · -3% | 30 · -30% |
| H6 | 15 · -36%* | 47 · -19% | 74 · -15% | 95 · -8% | 127 · -7% | 48 · -4% |
| D | 13 · -56%* | 47 · -15% | 75 · -8% | 104 · -10% | 135 · -5% | 40 · +5% |
| L | 15 · -36%* | 50 · -8% | 73 · -1% | 106 · -8% | 130 · -2% | 42 · -19% |
| D+conf | 2 · -4%* | 10 · +14%* | 21 · +9%* | 30 · +15% | 38 · +21% | 16 · +19%* |
| D+fade | 7 · -73%* | 20 · -43%* | 32 · -22% | 40 · -24% | 43 · -20% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 114. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.222 (n=72) | +0.011 (n=91) | +0.000 (n=93) | -0.047 (n=85) | -0.067 (n=15) | -0.103 (n=39) |
| spread · B | +0.241 (n=79) | -0.146 (n=89) | -0.032 (n=95) | -0.022 (n=91) | -0.188 (n=16) | -0.057 (n=35) |
| ml · A | +0.000 (n=69) | -0.002 (n=86) | -0.001 (n=90) | +0.001 (n=89) | +0.002 (n=16) | -0.002 (n=46) |
| ml · B | -0.002 (n=75) | -0.003 (n=99) | -0.003 (n=96) | -0.001 (n=89) | -0.004 (n=16) | -0.003 (n=45) |
| total · T | +1.222 (n=63) | +0.405 (n=74) | +0.067 (n=75) | -0.027 (n=73) | -0.143 (n=21) | +0.094 (n=32) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 152 | -0.769 (-1.82) | – | – | – |
| spread · A · D | 175 | -0.427 (-1.20) | – | – | – |
| spread · B · E | 152 | -0.869 (-2.27) | – | – | – |
| spread · B · D | 175 | -0.494 (-1.34) | – | – | – |
| ml · A · E | 152 | – | 0.2114 | 0.1963 | +0.0151 (2.98) |
| ml · A · D | 175 | – | 0.2077 | 0.1940 | +0.0136 (2.52) |
| ml · B · E | 152 | – | 0.2125 | 0.1963 | +0.0162 (2.82) |
| ml · B · D | 175 | – | 0.2066 | 0.1940 | +0.0125 (2.29) |
| total · T · E | 152 | +0.307 (0.79) | – | – | – |
| total · T · D | 175 | -0.128 (-0.34) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._