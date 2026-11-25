# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **192** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · +8%* | 53 · +1% | 83 · -8% | 125 · -22% | 142 · -17% | 26 · -12%* |
| H6 | 28 · -12%* | 60 · -11% | 102 · -3% | 145 · -8% | 160 · -6% | 32 · -5% |
| D | 34 · -11% | 63 · -7% | 102 · -3% | 142 · -5% | 169 · -4% | 23 · +8%* |
| L | 35 · -18% | 67 · -9% | 94 · -3% | 135 · +3% | 157 · -0% | 32 · -28% |
| D+conf | 4 · -4%* | 10 · -4%* | 18 · +39%* | 26 · +26%* | 33 · +11% | 8 · -4%* |
| D+fade | 20 · -15%* | 31 · -8% | 43 · -3% | 53 · -7% | 54 · -9% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 34 · -21% | 56 · -15% | 86 · -7% | 127 · -10% | 147 · -4% | 21 · -37%* |
| H6 | 39 · +2% | 66 · +1% | 99 · -4% | 149 · -5% | 173 · -4% | 19 · -29%* |
| D | 37 · -7% | 64 · -2% | 103 · +4% | 150 · -3% | 178 · -4% | 14 · -18%* |
| L | 33 · -19% | 65 · -6% | 97 · -4% | 131 · +2% | 160 · -4% | 29 · -35%* |
| D+conf | 5 · -23%* | 11 · +4%* | 18 · +17%* | 32 · +8% | 40 · +5% | 1 · -100%* |
| D+fade | 15 · -11%* | 23 · -9%* | 39 · -3% | 50 · -9% | 51 · -11% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 29 · -28%* | 51 · -19% | 79 · -18% | 124 · -17% | 149 · -20% | 19 · +20%* |
| H6 | 37 · -43% | 70 · -17% | 94 · -19% | 149 · -11% | 167 · -12% | 25 · -1%* |
| D | 37 · -43% | 70 · -24% | 99 · -15% | 143 · -8% | 169 · -10% | 23 · -58%* |
| L | 45 · -38% | 69 · -26% | 98 · -9% | 137 · -3% | 161 · -9% | 27 · -19%* |
| D+conf | 3 · +27%* | 12 · +14%* | 18 · +13%* | 29 · +4%* | 37 · +8% | 5 · -74%* |
| D+fade | 26 · -51%* | 41 · -32% | 50 · -44% | 62 · -39% | 63 · -40% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 35 · -15% | 57 · -22% | 84 · -11% | 129 · -17% | 145 · -17% | 23 · -40%* |
| H6 | 43 · -34% | 72 · -13% | 110 · -8% | 153 · -15% | 172 · -11% | 20 · -45%* |
| D | 37 · -21% | 66 · -20% | 107 · -4% | 156 · -10% | 170 · -9% | 22 · -26%* |
| L | 39 · -4% | 62 · -18% | 98 · -18% | 139 · -14% | 163 · -15% | 25 · +39%* |
| D+conf | 2 · +91%* | 7 · -2%* | 18 · -12%* | 28 · -28%* | 31 · -14% | 10 · -21%* |
| D+fade | 25 · -77%* | 35 · -50% | 51 · -35% | 64 · -33% | 64 · -33% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · -15%* | 52 · -12% | 69 · -12% | 96 · -13% | 132 · -5% | 36 · -31% |
| H6 | 16 · -29%* | 53 · -25% | 83 · -20% | 108 · -10% | 143 · -9% | 49 · -6% |
| D | 14 · -45%* | 54 · -19% | 83 · -12% | 115 · -14% | 147 · -8% | 45 · -3% |
| L | 16 · -28%* | 55 · -13% | 81 · -6% | 118 · -13% | 145 · -6% | 44 · -22% |
| D+conf | 2 · -4%* | 10 · +14%* | 21 · +9%* | 31 · +11% | 39 · +18% | 18 · +17%* |
| D+fade | 8 · -52%* | 27 · -43%* | 39 · -27% | 48 · -29% | 51 · -25% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 118. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.217 (n=83) | +0.029 (n=102) | +0.020 (n=102) | -0.064 (n=94) | -0.167 (n=18) | -0.093 (n=43) |
| spread · B | +0.198 (n=86) | -0.010 (n=99) | +0.049 (n=103) | +0.031 (n=97) | -0.167 (n=18) | +0.051 (n=39) |
| ml · A | +0.000 (n=79) | -0.003 (n=94) | -0.001 (n=99) | +0.000 (n=98) | +0.001 (n=18) | -0.003 (n=50) |
| ml · B | -0.003 (n=84) | -0.003 (n=110) | -0.002 (n=107) | -0.001 (n=98) | -0.005 (n=18) | -0.001 (n=51) |
| total · T | +1.130 (n=69) | +0.410 (n=83) | +0.096 (n=83) | -0.025 (n=81) | -0.143 (n=21) | +0.179 (n=39) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 168 | -0.371 (-0.93) | – | – | – |
| spread · A · D | 192 | -0.193 (-0.57) | – | – | – |
| spread · B · E | 168 | -0.523 (-1.46) | – | – | – |
| spread · B · D | 192 | -0.282 (-0.81) | – | – | – |
| ml · A · E | 168 | – | 0.2109 | 0.2002 | +0.0107 (2.12) |
| ml · A · D | 192 | – | 0.2075 | 0.1974 | +0.0100 (1.91) |
| ml · B · E | 168 | – | 0.2095 | 0.2002 | +0.0093 (1.59) |
| ml · B · D | 192 | – | 0.2051 | 0.1974 | +0.0076 (1.42) |
| total · T · E | 168 | +0.124 (0.32) | – | – | – |
| total · T · D | 192 | -0.316 (-0.86) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._