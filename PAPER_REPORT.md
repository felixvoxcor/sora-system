# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **188** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · +8%* | 52 · +3% | 80 · -7% | 121 · -23% | 138 · -17% | 26 · -12%* |
| H6 | 28 · -12%* | 58 · -8% | 99 · -2% | 142 · -7% | 157 · -5% | 31 · -8% |
| D | 34 · -11% | 61 · -3% | 100 · -1% | 139 · -4% | 165 · -4% | 23 · +8%* |
| L | 34 · -21% | 65 · -9% | 91 · -1% | 132 · +4% | 154 · +0% | 31 · -32% |
| D+conf | 4 · -4%* | 10 · -4%* | 18 · +39%* | 26 · +26%* | 32 · +8% | 8 · -4%* |
| D+fade | 20 · -15%* | 30 · -5% | 42 · -1% | 52 · -5% | 53 · -7% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 34 · -21% | 56 · -15% | 86 · -7% | 125 · -8% | 144 · -2% | 20 · -33%* |
| H6 | 39 · +2% | 66 · +1% | 97 · -2% | 145 · -3% | 169 · -2% | 19 · -29%* |
| D | 37 · -7% | 63 · -0% | 102 · +5% | 146 · -1% | 174 · -1% | 14 · -18%* |
| L | 33 · -19% | 65 · -6% | 96 · -3% | 128 · +4% | 156 · -1% | 29 · -35%* |
| D+conf | 5 · -23%* | 11 · +4%* | 18 · +17%* | 32 · +8% | 40 · +5% | 1 · -100%* |
| D+fade | 15 · -11%* | 22 · -5%* | 38 · -0% | 48 · -5% | 49 · -7% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 28 · -25%* | 49 · -15% | 77 · -16% | 120 · -17% | 145 · -20% | 19 · +20%* |
| H6 | 35 · -40% | 68 · -14% | 92 · -17% | 146 · -10% | 163 · -12% | 25 · -1%* |
| D | 36 · -41% | 68 · -22% | 97 · -14% | 140 · -8% | 166 · -9% | 22 · -56%* |
| L | 42 · -37% | 66 · -25% | 95 · -8% | 133 · -2% | 157 · -9% | 27 · -19%* |
| D+conf | 3 · +27%* | 12 · +14%* | 18 · +13%* | 29 · +4%* | 37 · +8% | 5 · -74%* |
| D+fade | 25 · -49%* | 40 · -30% | 49 · -43% | 61 · -38% | 62 · -39% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 35 · -15% | 57 · -22% | 84 · -11% | 126 · -15% | 141 · -15% | 23 · -40%* |
| H6 | 43 · -34% | 71 · -12% | 109 · -8% | 149 · -12% | 168 · -8% | 20 · -45%* |
| D | 37 · -21% | 65 · -19% | 105 · -2% | 152 · -8% | 166 · -6% | 22 · -26%* |
| L | 39 · -4% | 62 · -18% | 97 · -17% | 135 · -11% | 159 · -13% | 25 · +39%* |
| D+conf | 2 · +91%* | 7 · -2%* | 18 · -12%* | 28 · -28%* | 31 · -14% | 10 · -21%* |
| D+fade | 25 · -77%* | 34 · -48% | 49 · -32% | 62 · -31% | 62 · -31% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · -15%* | 51 · -10% | 67 · -9% | 94 · -11% | 129 · -4% | 35 · -34% |
| H6 | 16 · -29%* | 51 · -22% | 80 · -17% | 105 · -7% | 140 · -7% | 48 · -4% |
| D | 14 · -45%* | 52 · -15% | 80 · -9% | 112 · -11% | 144 · -6% | 44 · -0% |
| L | 16 · -28%* | 53 · -10% | 78 · -2% | 115 · -10% | 142 · -5% | 43 · -20% |
| D+conf | 2 · -4%* | 10 · +14%* | 21 · +9%* | 31 · +11% | 39 · +18% | 18 · +17%* |
| D+fade | 8 · -52%* | 25 · -39%* | 37 · -23% | 46 · -26% | 49 · -22% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 118. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.263 (n=80) | +0.051 (n=99) | +0.020 (n=100) | -0.055 (n=91) | -0.167 (n=18) | -0.095 (n=42) |
| spread · B | +0.198 (n=86) | -0.072 (n=97) | +0.010 (n=102) | -0.031 (n=96) | -0.167 (n=18) | -0.053 (n=38) |
| ml · A | +0.000 (n=77) | -0.003 (n=92) | -0.001 (n=97) | +0.000 (n=95) | +0.001 (n=18) | -0.003 (n=49) |
| ml · B | -0.003 (n=84) | -0.003 (n=109) | -0.003 (n=105) | -0.001 (n=97) | -0.005 (n=18) | -0.003 (n=49) |
| total · T | +1.194 (n=67) | +0.450 (n=80) | +0.100 (n=80) | -0.013 (n=78) | -0.143 (n=21) | +0.162 (n=37) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 164 | -0.408 (-1.00) | – | – | – |
| spread · A · D | 188 | -0.217 (-0.63) | – | – | – |
| spread · B · E | 164 | -0.516 (-1.43) | – | – | – |
| spread · B · D | 188 | -0.275 (-0.78) | – | – | – |
| ml · A · E | 164 | – | 0.2138 | 0.2030 | +0.0108 (2.09) |
| ml · A · D | 188 | – | 0.2100 | 0.2000 | +0.0100 (1.86) |
| ml · B · E | 164 | – | 0.2121 | 0.2030 | +0.0091 (1.52) |
| ml · B · D | 188 | – | 0.2073 | 0.2000 | +0.0073 (1.33) |
| total · T · E | 164 | +0.140 (0.36) | – | – | – |
| total · T · D | 188 | -0.225 (-0.60) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._