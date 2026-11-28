# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **208** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 24 · +11%* | 57 · +4% | 91 · -5% | 139 · -18% | 157 · -12% | 27 · -8%* |
| H6 | 29 · -15%* | 64 · -11% | 110 · -1% | 159 · -7% | 174 · -5% | 34 · -5% |
| D | 36 · -10% | 68 · -8% | 111 · -1% | 155 · -4% | 182 · -4% | 26 · +3%* |
| L | 37 · -18% | 72 · -10% | 104 · +1% | 149 · +4% | 171 · +0% | 34 · -26% |
| D+conf | 5 · +14%* | 11 · +4%* | 20 · +45%* | 28 · +31%* | 35 · +16% | 10 · -3%* |
| D+fade | 21 · -19%* | 34 · -17% | 48 · -5% | 58 · -9% | 59 · -10% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 35 · -18% | 59 · -12% | 92 · -7% | 143 · -10% | 163 · -5% | 21 · -37%* |
| H6 | 43 · +1% | 71 · -1% | 109 · -8% | 162 · -7% | 187 · -6% | 21 · -26%* |
| D | 40 · -4% | 69 · -0% | 112 · +1% | 162 · -5% | 192 · -6% | 16 · -28%* |
| L | 36 · -15% | 69 · -6% | 106 · -7% | 143 · -2% | 175 · -5% | 30 · -30% |
| D+conf | 5 · -23%* | 11 · +4%* | 18 · +17%* | 32 · +8% | 40 · +5% | 2 · -100%* |
| D+fade | 18 · -4%* | 26 · -5%* | 46 · -9% | 58 · -15% | 60 · -18% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 30 · -30% | 56 · -13% | 87 · -13% | 137 · -13% | 165 · -16% | 19 · +20%* |
| H6 | 39 · -42% | 75 · -13% | 103 · -14% | 162 · -9% | 182 · -8% | 26 · +3%* |
| D | 39 · -46% | 76 · -21% | 109 · -12% | 156 · -5% | 184 · -6% | 24 · -54%* |
| L | 47 · -41% | 76 · -21% | 107 · -8% | 151 · +1% | 176 · -5% | 28 · -22%* |
| D+conf | 3 · +27%* | 15 · +36%* | 22 · +39%* | 33 · +23% | 41 · +22% | 6 · -56%* |
| D+fade | 27 · -53%* | 43 · -35% | 54 · -44% | 68 · -38% | 69 · -39% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 38 · -16% | 62 · -24% | 94 · -11% | 144 · -14% | 160 · -15% | 24 · -36%* |
| H6 | 46 · -33% | 79 · -15% | 120 · -9% | 167 · -15% | 187 · -9% | 21 · -39%* |
| D | 41 · -17% | 72 · -17% | 116 · -5% | 169 · -9% | 185 · -7% | 23 · -22%* |
| L | 43 · -2% | 67 · -17% | 108 · -18% | 152 · -13% | 179 · -14% | 25 · +39%* |
| D+conf | 2 · +91%* | 7 · -2%* | 18 · -12%* | 30 · -8% | 33 · +3% | 11 · -14%* |
| D+fade | 29 · -64%* | 39 · -43% | 56 · -33% | 70 · -33% | 71 · -34% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 19 · -19%* | 56 · -11% | 75 · -8% | 105 · -11% | 144 · -5% | 40 · -33% |
| H6 | 17 · -33%* | 59 · -26% | 91 · -21% | 120 · -8% | 159 · -9% | 49 · -6% |
| D | 17 · -32%* | 61 · -15% | 92 · -9% | 128 · -12% | 163 · -6% | 45 · -3% |
| L | 18 · -36%* | 62 · -11% | 92 · -5% | 131 · -13% | 160 · -7% | 45 · -24% |
| D+conf | 2 · -4%* | 10 · +14%* | 21 · +9%* | 32 · +14% | 40 · +20% | 18 · +17%* |
| D+fade | 11 · -31%* | 33 · -36% | 46 · -21% | 57 · -26% | 61 · -22% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 122. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.231 (n=91) | +0.018 (n=110) | +0.027 (n=111) | -0.058 (n=104) | -0.150 (n=20) | -0.083 (n=48) |
| spread · B | +0.120 (n=92) | -0.037 (n=109) | +0.036 (n=112) | +0.028 (n=106) | -0.167 (n=18) | +0.043 (n=46) |
| ml · A | +0.000 (n=87) | -0.002 (n=103) | -0.001 (n=109) | +0.000 (n=107) | +0.001 (n=22) | -0.003 (n=54) |
| ml · B | -0.004 (n=94) | -0.003 (n=120) | -0.002 (n=116) | -0.001 (n=108) | -0.005 (n=18) | -0.001 (n=56) |
| total · T | +0.973 (n=75) | +0.352 (n=91) | +0.109 (n=92) | +0.011 (n=92) | -0.143 (n=21) | +0.196 (n=46) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 184 | -0.172 (-0.45) | – | – | – |
| spread · A · D | 208 | -0.116 (-0.36) | – | – | – |
| spread · B · E | 184 | -0.462 (-1.34) | – | – | – |
| spread · B · D | 208 | -0.251 (-0.77) | – | – | – |
| ml · A · E | 184 | – | 0.2138 | 0.2044 | +0.0093 (1.92) |
| ml · A · D | 208 | – | 0.2103 | 0.2009 | +0.0094 (1.85) |
| ml · B · E | 184 | – | 0.2131 | 0.2044 | +0.0087 (1.57) |
| ml · B · D | 208 | – | 0.2078 | 0.2009 | +0.0069 (1.33) |
| total · T · E | 184 | +0.187 (0.49) | – | – | – |
| total · T · D | 208 | -0.154 (-0.44) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._