# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **191** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · +8%* | 52 · +3% | 82 · -7% | 124 · -21% | 141 · -16% | 26 · -12%* |
| H6 | 28 · -12%* | 59 · -10% | 101 · -2% | 144 · -7% | 159 · -5% | 32 · -5% |
| D | 34 · -11% | 62 · -5% | 101 · -2% | 141 · -4% | 168 · -4% | 23 · +8%* |
| L | 35 · -18% | 66 · -7% | 93 · -1% | 134 · +4% | 156 · +0% | 32 · -28% |
| D+conf | 4 · -4%* | 10 · -4%* | 18 · +39%* | 26 · +26%* | 33 · +11% | 8 · -4%* |
| D+fade | 20 · -15%* | 31 · -8% | 43 · -3% | 53 · -7% | 54 · -9% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 34 · -21% | 56 · -15% | 86 · -7% | 126 · -9% | 146 · -3% | 21 · -37%* |
| H6 | 39 · +2% | 66 · +1% | 99 · -4% | 148 · -5% | 172 · -4% | 19 · -29%* |
| D | 37 · -7% | 64 · -2% | 103 · +4% | 149 · -3% | 177 · -3% | 14 · -18%* |
| L | 33 · -19% | 65 · -6% | 97 · -4% | 130 · +3% | 159 · -3% | 29 · -35%* |
| D+conf | 5 · -23%* | 11 · +4%* | 18 · +17%* | 32 · +8% | 40 · +5% | 1 · -100%* |
| D+fade | 15 · -11%* | 23 · -9%* | 39 · -3% | 50 · -9% | 51 · -11% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 28 · -25%* | 50 · -17% | 78 · -17% | 123 · -16% | 148 · -19% | 19 · +20%* |
| H6 | 36 · -42% | 69 · -16% | 93 · -18% | 148 · -11% | 166 · -12% | 25 · -1%* |
| D | 37 · -43% | 69 · -23% | 98 · -15% | 142 · -8% | 168 · -9% | 23 · -58%* |
| L | 44 · -37% | 68 · -25% | 97 · -8% | 136 · -2% | 160 · -9% | 27 · -19%* |
| D+conf | 3 · +27%* | 12 · +14%* | 18 · +13%* | 29 · +4%* | 37 · +8% | 5 · -74%* |
| D+fade | 26 · -51%* | 41 · -32% | 50 · -44% | 62 · -39% | 63 · -40% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 35 · -15% | 57 · -22% | 84 · -11% | 128 · -16% | 144 · -17% | 23 · -40%* |
| H6 | 43 · -34% | 72 · -13% | 110 · -8% | 152 · -14% | 171 · -10% | 20 · -45%* |
| D | 37 · -21% | 66 · -20% | 107 · -4% | 155 · -10% | 169 · -8% | 22 · -26%* |
| L | 39 · -4% | 62 · -18% | 98 · -18% | 138 · -13% | 162 · -15% | 25 · +39%* |
| D+conf | 2 · +91%* | 7 · -2%* | 18 · -12%* | 28 · -28%* | 31 · -14% | 10 · -21%* |
| D+fade | 25 · -77%* | 35 · -50% | 51 · -35% | 64 · -33% | 64 · -33% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · -15%* | 52 · -12% | 69 · -12% | 96 · -13% | 132 · -5% | 35 · -34% |
| H6 | 16 · -29%* | 53 · -25% | 83 · -20% | 108 · -10% | 143 · -9% | 48 · -4% |
| D | 14 · -45%* | 54 · -19% | 83 · -12% | 115 · -14% | 147 · -8% | 44 · -0% |
| L | 16 · -28%* | 55 · -13% | 81 · -6% | 118 · -13% | 145 · -6% | 43 · -20% |
| D+conf | 2 · -4%* | 10 · +14%* | 21 · +9%* | 31 · +11% | 39 · +18% | 18 · +17%* |
| D+fade | 8 · -52%* | 27 · -43%* | 39 · -27% | 48 · -29% | 51 · -25% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 118. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.220 (n=82) | +0.030 (n=101) | +0.020 (n=101) | -0.065 (n=93) | -0.167 (n=18) | -0.093 (n=43) |
| spread · B | +0.198 (n=86) | -0.010 (n=99) | +0.049 (n=103) | +0.031 (n=97) | -0.167 (n=18) | +0.051 (n=39) |
| ml · A | +0.000 (n=78) | -0.003 (n=93) | -0.001 (n=98) | +0.000 (n=97) | +0.001 (n=18) | -0.003 (n=50) |
| ml · B | -0.003 (n=84) | -0.003 (n=110) | -0.002 (n=107) | -0.001 (n=98) | -0.005 (n=18) | -0.001 (n=51) |
| total · T | +1.130 (n=69) | +0.410 (n=83) | +0.096 (n=83) | -0.025 (n=81) | -0.143 (n=21) | +0.179 (n=39) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 167 | -0.363 (-0.90) | – | – | – |
| spread · A · D | 191 | -0.186 (-0.55) | – | – | – |
| spread · B · E | 167 | -0.522 (-1.45) | – | – | – |
| spread · B · D | 191 | -0.282 (-0.81) | – | – | – |
| ml · A · E | 167 | – | 0.2116 | 0.2011 | +0.0105 (2.05) |
| ml · A · D | 191 | – | 0.2080 | 0.1982 | +0.0098 (1.86) |
| ml · B · E | 167 | – | 0.2103 | 0.2011 | +0.0092 (1.57) |
| ml · B · D | 191 | – | 0.2058 | 0.1982 | +0.0076 (1.41) |
| total · T · E | 167 | +0.119 (0.31) | – | – | – |
| total · T · D | 191 | -0.299 (-0.81) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._