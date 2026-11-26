# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **201** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · +8%* | 54 · +3% | 87 · -5% | 134 · -19% | 151 · -14% | 26 · -12%* |
| H6 | 28 · -12%* | 62 · -11% | 105 · -2% | 152 · -6% | 167 · -4% | 34 · -5% |
| D | 34 · -11% | 64 · -8% | 106 · -1% | 148 · -3% | 175 · -3% | 26 · +3%* |
| L | 35 · -18% | 68 · -10% | 99 · +0% | 142 · +5% | 164 · +1% | 34 · -26% |
| D+conf | 4 · -4%* | 10 · -4%* | 19 · +42%* | 27 · +28%* | 34 · +13% | 10 · -3%* |
| D+fade | 20 · -15%* | 32 · -11% | 45 · -3% | 55 · -7% | 56 · -9% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 34 · -21% | 58 · -14% | 89 · -6% | 136 · -10% | 156 · -5% | 21 · -37%* |
| H6 | 40 · +4% | 68 · +0% | 105 · -6% | 157 · -5% | 181 · -4% | 20 · -32%* |
| D | 38 · -4% | 67 · -0% | 109 · +2% | 157 · -4% | 185 · -4% | 16 · -28%* |
| L | 34 · -16% | 67 · -6% | 102 · -5% | 138 · +1% | 169 · -3% | 29 · -35%* |
| D+conf | 5 · -23%* | 11 · +4%* | 18 · +17%* | 32 · +8% | 40 · +5% | 2 · -100%* |
| D+fade | 16 · -4%* | 24 · -5%* | 43 · -7% | 54 · -12% | 55 · -14% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 30 · -30% | 53 · -19% | 83 · -16% | 131 · -15% | 158 · -17% | 19 · +20%* |
| H6 | 39 · -42% | 72 · -17% | 98 · -17% | 155 · -9% | 175 · -9% | 26 · +3%* |
| D | 38 · -44% | 72 · -24% | 103 · -14% | 149 · -6% | 177 · -7% | 24 · -54%* |
| L | 46 · -40% | 71 · -26% | 101 · -10% | 144 · +0% | 169 · -6% | 28 · -22%* |
| D+conf | 3 · +27%* | 13 · +17%* | 20 · +26%* | 31 · +14% | 39 · +15% | 6 · -56%* |
| D+fade | 26 · -51%* | 41 · -32% | 50 · -44% | 63 · -37% | 64 · -38% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 35 · -15% | 59 · -24% | 91 · -11% | 138 · -15% | 154 · -16% | 23 · -40%* |
| H6 | 43 · -34% | 76 · -15% | 117 · -9% | 161 · -13% | 180 · -9% | 21 · -39%* |
| D | 38 · -17% | 69 · -17% | 113 · -5% | 163 · -9% | 178 · -7% | 23 · -22%* |
| L | 40 · -1% | 64 · -17% | 104 · -17% | 146 · -13% | 172 · -14% | 25 · +39%* |
| D+conf | 2 · +91%* | 7 · -2%* | 18 · -12%* | 29 · -19%* | 32 · -6% | 11 · -14%* |
| D+fade | 26 · -69%* | 36 · -45% | 53 · -33% | 66 · -32% | 66 · -32% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · -15%* | 54 · -12% | 72 · -10% | 101 · -13% | 138 · -6% | 39 · -31% |
| H6 | 17 · -33%* | 57 · -26% | 88 · -20% | 115 · -9% | 152 · -9% | 49 · -6% |
| D | 16 · -40%* | 58 · -21% | 88 · -13% | 122 · -14% | 156 · -7% | 45 · -3% |
| L | 17 · -32%* | 58 · -14% | 87 · -6% | 125 · -13% | 153 · -6% | 45 · -24% |
| D+conf | 2 · -4%* | 10 · +14%* | 21 · +9%* | 32 · +14% | 40 · +20% | 18 · +17%* |
| D+fade | 10 · -43%* | 31 · -45% | 43 · -29% | 53 · -32% | 57 · -27% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 121. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.253 (n=87) | +0.048 (n=105) | +0.028 (n=106) | -0.061 (n=99) | -0.158 (n=19) | -0.089 (n=45) |
| spread · B | +0.169 (n=89) | -0.048 (n=105) | +0.037 (n=109) | +0.029 (n=102) | -0.167 (n=18) | +0.047 (n=43) |
| ml · A | +0.001 (n=83) | -0.002 (n=98) | -0.000 (n=103) | +0.000 (n=101) | +0.002 (n=20) | -0.003 (n=50) |
| ml · B | -0.004 (n=91) | -0.003 (n=117) | -0.002 (n=113) | -0.001 (n=104) | -0.005 (n=18) | -0.001 (n=53) |
| total · T | +1.014 (n=72) | +0.364 (n=88) | +0.102 (n=88) | -0.023 (n=87) | -0.143 (n=21) | +0.186 (n=43) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 177 | -0.224 (-0.58) | – | – | – |
| spread · A · D | 201 | -0.111 (-0.33) | – | – | – |
| spread · B · E | 177 | -0.476 (-1.36) | – | – | – |
| spread · B · D | 201 | -0.238 (-0.71) | – | – | – |
| ml · A · E | 177 | – | 0.2111 | 0.2015 | +0.0096 (1.96) |
| ml · A · D | 201 | – | 0.2078 | 0.1988 | +0.0091 (1.78) |
| ml · B · E | 177 | – | 0.2104 | 0.2015 | +0.0089 (1.58) |
| ml · B · D | 201 | – | 0.2058 | 0.1988 | +0.0070 (1.34) |
| total · T · E | 177 | +0.094 (0.24) | – | – | – |
| total · T · D | 201 | -0.241 (-0.67) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._