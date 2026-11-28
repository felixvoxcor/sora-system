# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **207** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 24 · +11%* | 57 · +4% | 90 · -4% | 138 · -17% | 156 · -12% | 27 · -8%* |
| H6 | 29 · -15%* | 64 · -11% | 109 · -0% | 158 · -6% | 173 · -4% | 34 · -5% |
| D | 36 · -10% | 67 · -6% | 110 · +0% | 154 · -3% | 181 · -3% | 26 · +3%* |
| L | 37 · -18% | 71 · -9% | 103 · +2% | 148 · +4% | 170 · +1% | 34 · -26% |
| D+conf | 5 · +14%* | 11 · +4%* | 20 · +45%* | 28 · +31%* | 35 · +16% | 10 · -3%* |
| D+fade | 21 · -19%* | 33 · -14% | 47 · -3% | 57 · -7% | 58 · -9% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 35 · -18% | 59 · -12% | 92 · -7% | 142 · -10% | 162 · -5% | 21 · -37%* |
| H6 | 43 · +1% | 71 · -1% | 109 · -8% | 161 · -7% | 186 · -6% | 21 · -26%* |
| D | 40 · -4% | 69 · -0% | 112 · +1% | 161 · -4% | 191 · -5% | 16 · -28%* |
| L | 36 · -15% | 69 · -6% | 106 · -7% | 142 · -1% | 174 · -5% | 30 · -30% |
| D+conf | 5 · -23%* | 11 · +4%* | 18 · +17%* | 32 · +8% | 40 · +5% | 2 · -100%* |
| D+fade | 18 · -4%* | 26 · -5%* | 46 · -9% | 57 · -14% | 59 · -17% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 30 · -30% | 56 · -13% | 86 · -12% | 136 · -12% | 164 · -15% | 19 · +20%* |
| H6 | 39 · -42% | 75 · -13% | 103 · -14% | 161 · -8% | 181 · -8% | 26 · +3%* |
| D | 39 · -46% | 75 · -20% | 108 · -11% | 155 · -4% | 183 · -5% | 24 · -54%* |
| L | 47 · -41% | 75 · -20% | 106 · -7% | 150 · +1% | 175 · -5% | 28 · -22%* |
| D+conf | 3 · +27%* | 15 · +36%* | 22 · +39%* | 33 · +23% | 41 · +22% | 6 · -56%* |
| D+fade | 27 · -53%* | 42 · -33% | 53 · -43% | 67 · -37% | 68 · -38% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 38 · -16% | 62 · -24% | 94 · -11% | 143 · -14% | 159 · -14% | 24 · -36%* |
| H6 | 46 · -33% | 79 · -15% | 120 · -9% | 166 · -14% | 186 · -9% | 21 · -39%* |
| D | 41 · -17% | 72 · -17% | 116 · -5% | 168 · -8% | 184 · -7% | 23 · -22%* |
| L | 43 · -2% | 67 · -17% | 108 · -18% | 151 · -12% | 178 · -13% | 25 · +39%* |
| D+conf | 2 · +91%* | 7 · -2%* | 18 · -12%* | 30 · -8% | 33 · +3% | 11 · -14%* |
| D+fade | 29 · -64%* | 39 · -43% | 56 · -33% | 69 · -32% | 70 · -33% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 19 · -19%* | 55 · -13% | 74 · -10% | 104 · -12% | 143 · -5% | 40 · -33% |
| H6 | 17 · -33%* | 59 · -26% | 91 · -21% | 119 · -9% | 158 · -10% | 49 · -6% |
| D | 17 · -32%* | 60 · -17% | 91 · -10% | 127 · -13% | 162 · -7% | 45 · -3% |
| L | 18 · -36%* | 61 · -12% | 91 · -6% | 130 · -13% | 159 · -8% | 45 · -24% |
| D+conf | 2 · -4%* | 10 · +14%* | 21 · +9%* | 32 · +14% | 40 · +20% | 18 · +17%* |
| D+fade | 11 · -31%* | 33 · -36% | 46 · -21% | 57 · -26% | 61 · -22% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 122. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.244 (n=90) | +0.028 (n=109) | +0.027 (n=110) | -0.058 (n=103) | -0.150 (n=20) | -0.085 (n=47) |
| spread · B | +0.120 (n=92) | -0.037 (n=109) | +0.036 (n=112) | +0.028 (n=106) | -0.167 (n=18) | +0.043 (n=46) |
| ml · A | +0.000 (n=86) | -0.002 (n=103) | -0.001 (n=108) | +0.000 (n=106) | +0.001 (n=22) | -0.003 (n=53) |
| ml · B | -0.004 (n=94) | -0.003 (n=120) | -0.002 (n=116) | -0.001 (n=108) | -0.005 (n=18) | -0.001 (n=56) |
| total · T | +0.986 (n=74) | +0.352 (n=91) | +0.110 (n=91) | +0.000 (n=91) | -0.143 (n=21) | +0.196 (n=46) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 183 | -0.163 (-0.43) | – | – | – |
| spread · A · D | 207 | -0.107 (-0.33) | – | – | – |
| spread · B · E | 183 | -0.457 (-1.32) | – | – | – |
| spread · B · D | 207 | -0.249 (-0.76) | – | – | – |
| ml · A · E | 183 | – | 0.2126 | 0.2036 | +0.0089 (1.83) |
| ml · A · D | 207 | – | 0.2092 | 0.2003 | +0.0089 (1.75) |
| ml · B · E | 183 | – | 0.2120 | 0.2036 | +0.0084 (1.50) |
| ml · B · D | 207 | – | 0.2070 | 0.2003 | +0.0067 (1.29) |
| total · T · E | 183 | +0.181 (0.47) | – | – | – |
| total · T · D | 207 | -0.159 (-0.45) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._