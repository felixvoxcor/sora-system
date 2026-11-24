# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **189** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · +8%* | 52 · +3% | 81 · -6% | 122 · -22% | 139 · -16% | 26 · -12%* |
| H6 | 28 · -12%* | 58 · -8% | 100 · -1% | 143 · -7% | 158 · -5% | 31 · -8% |
| D | 34 · -11% | 61 · -3% | 100 · -1% | 139 · -4% | 166 · -3% | 23 · +8%* |
| L | 35 · -18% | 66 · -7% | 92 · -0% | 133 · +5% | 155 · +1% | 31 · -32% |
| D+conf | 4 · -4%* | 10 · -4%* | 18 · +39%* | 26 · +26%* | 33 · +11% | 8 · -4%* |
| D+fade | 20 · -15%* | 30 · -5% | 42 · -1% | 52 · -5% | 53 · -7% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 34 · -21% | 56 · -15% | 86 · -7% | 125 · -8% | 144 · -2% | 21 · -37%* |
| H6 | 39 · +2% | 66 · +1% | 97 · -2% | 146 · -3% | 170 · -2% | 19 · -29%* |
| D | 37 · -7% | 64 · -2% | 103 · +4% | 147 · -1% | 175 · -2% | 14 · -18%* |
| L | 33 · -19% | 65 · -6% | 96 · -3% | 129 · +3% | 157 · -2% | 29 · -35%* |
| D+conf | 5 · -23%* | 11 · +4%* | 18 · +17%* | 32 · +8% | 40 · +5% | 1 · -100%* |
| D+fade | 15 · -11%* | 23 · -9%* | 39 · -3% | 49 · -7% | 50 · -9% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 28 · -25%* | 49 · -15% | 77 · -16% | 121 · -16% | 146 · -20% | 19 · +20%* |
| H6 | 35 · -40% | 68 · -14% | 92 · -17% | 147 · -10% | 164 · -12% | 25 · -1%* |
| D | 36 · -41% | 68 · -22% | 97 · -14% | 140 · -8% | 166 · -9% | 23 · -58%* |
| L | 43 · -36% | 67 · -24% | 96 · -7% | 134 · -2% | 158 · -9% | 27 · -19%* |
| D+conf | 3 · +27%* | 12 · +14%* | 18 · +13%* | 29 · +4%* | 37 · +8% | 5 · -74%* |
| D+fade | 25 · -49%* | 40 · -30% | 49 · -43% | 61 · -38% | 62 · -39% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 35 · -15% | 57 · -22% | 84 · -11% | 127 · -15% | 142 · -15% | 23 · -40%* |
| H6 | 43 · -34% | 71 · -12% | 109 · -8% | 150 · -13% | 169 · -9% | 20 · -45%* |
| D | 37 · -21% | 66 · -20% | 106 · -3% | 153 · -8% | 167 · -7% | 22 · -26%* |
| L | 39 · -4% | 62 · -18% | 97 · -17% | 136 · -12% | 160 · -14% | 25 · +39%* |
| D+conf | 2 · +91%* | 7 · -2%* | 18 · -12%* | 28 · -28%* | 31 · -14% | 10 · -21%* |
| D+fade | 25 · -77%* | 35 · -50% | 50 · -33% | 63 · -32% | 63 · -32% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · -15%* | 52 · -12% | 68 · -10% | 95 · -12% | 130 · -5% | 35 · -34% |
| H6 | 16 · -29%* | 51 · -22% | 81 · -18% | 106 · -8% | 141 · -8% | 48 · -4% |
| D | 14 · -45%* | 53 · -17% | 81 · -10% | 113 · -12% | 145 · -6% | 44 · -0% |
| L | 16 · -28%* | 53 · -10% | 79 · -4% | 116 · -11% | 143 · -5% | 43 · -20% |
| D+conf | 2 · -4%* | 10 · +14%* | 21 · +9%* | 31 · +11% | 39 · +18% | 18 · +17%* |
| D+fade | 8 · -52%* | 26 · -41%* | 38 · -25% | 47 · -27% | 50 · -24% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 118. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.235 (n=81) | +0.030 (n=100) | +0.020 (n=100) | -0.054 (n=92) | -0.167 (n=18) | -0.095 (n=42) |
| spread · B | +0.198 (n=86) | -0.072 (n=97) | +0.049 (n=103) | -0.031 (n=96) | -0.167 (n=18) | +0.051 (n=39) |
| ml · A | +0.000 (n=77) | -0.003 (n=92) | -0.001 (n=97) | +0.000 (n=96) | +0.001 (n=18) | -0.003 (n=49) |
| ml · B | -0.003 (n=84) | -0.003 (n=109) | -0.002 (n=106) | -0.001 (n=97) | -0.005 (n=18) | -0.001 (n=50) |
| total · T | +1.206 (n=68) | +0.457 (n=81) | +0.136 (n=81) | +0.000 (n=79) | -0.143 (n=21) | +0.237 (n=38) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 165 | -0.389 (-0.96) | – | – | – |
| spread · A · D | 189 | -0.212 (-0.62) | – | – | – |
| spread · B · E | 165 | -0.515 (-1.43) | – | – | – |
| spread · B · D | 189 | -0.280 (-0.80) | – | – | – |
| ml · A · E | 165 | – | 0.2127 | 0.2021 | +0.0107 (2.07) |
| ml · A · D | 189 | – | 0.2090 | 0.1991 | +0.0099 (1.86) |
| ml · B · E | 165 | – | 0.2112 | 0.2021 | +0.0091 (1.54) |
| ml · B · D | 189 | – | 0.2065 | 0.1991 | +0.0074 (1.36) |
| total · T · E | 165 | +0.128 (0.33) | – | – | – |
| total · T · D | 189 | -0.232 (-0.63) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._