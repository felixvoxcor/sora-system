# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **202** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · +8%* | 54 · +3% | 87 · -5% | 135 · -18% | 152 · -13% | 26 · -12%* |
| H6 | 28 · -12%* | 62 · -11% | 106 · -1% | 153 · -5% | 168 · -4% | 34 · -5% |
| D | 34 · -11% | 64 · -8% | 107 · -0% | 149 · -3% | 176 · -2% | 26 · +3%* |
| L | 35 · -18% | 69 · -9% | 100 · +1% | 143 · +5% | 165 · +2% | 34 · -26% |
| D+conf | 4 · -4%* | 10 · -4%* | 19 · +42%* | 27 · +28%* | 34 · +13% | 10 · -3%* |
| D+fade | 20 · -15%* | 32 · -11% | 46 · -1% | 56 · -5% | 57 · -7% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 35 · -18% | 59 · -12% | 90 · -5% | 137 · -9% | 157 · -4% | 21 · -37%* |
| H6 | 41 · +6% | 69 · +2% | 106 · -5% | 158 · -5% | 182 · -4% | 20 · -32%* |
| D | 39 · -2% | 68 · +1% | 110 · +2% | 158 · -3% | 186 · -4% | 16 · -28%* |
| L | 35 · -13% | 68 · -5% | 103 · -4% | 139 · +1% | 170 · -3% | 29 · -35%* |
| D+conf | 5 · -23%* | 11 · +4%* | 18 · +17%* | 32 · +8% | 40 · +5% | 2 · -100%* |
| D+fade | 17 · +1%* | 25 · -1%* | 44 · -5% | 55 · -10% | 56 · -12% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 30 · -30% | 53 · -19% | 83 · -16% | 132 · -14% | 159 · -16% | 19 · +20%* |
| H6 | 39 · -42% | 72 · -17% | 99 · -16% | 156 · -8% | 176 · -8% | 26 · +3%* |
| D | 38 · -44% | 72 · -24% | 104 · -12% | 150 · -5% | 178 · -6% | 24 · -54%* |
| L | 46 · -40% | 72 · -24% | 102 · -9% | 145 · +1% | 170 · -5% | 28 · -22%* |
| D+conf | 3 · +27%* | 13 · +17%* | 20 · +26%* | 31 · +14% | 39 · +15% | 6 · -56%* |
| D+fade | 26 · -51%* | 41 · -32% | 51 · -41% | 64 · -34% | 65 · -35% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 36 · -11% | 60 · -22% | 92 · -9% | 139 · -14% | 155 · -15% | 23 · -40%* |
| H6 | 44 · -30% | 77 · -13% | 118 · -7% | 162 · -12% | 181 · -8% | 21 · -39%* |
| D | 39 · -13% | 70 · -15% | 114 · -3% | 164 · -8% | 179 · -7% | 23 · -22%* |
| L | 41 · +3% | 65 · -14% | 105 · -15% | 147 · -12% | 173 · -13% | 25 · +39%* |
| D+conf | 2 · +91%* | 7 · -2%* | 18 · -12%* | 29 · -19%* | 32 · -6% | 11 · -14%* |
| D+fade | 27 · -62%* | 37 · -40% | 54 · -30% | 67 · -30% | 67 · -30% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 19 · -19%* | 55 · -13% | 73 · -11% | 102 · -14% | 139 · -7% | 39 · -31% |
| H6 | 17 · -33%* | 58 · -28% | 89 · -21% | 116 · -10% | 153 · -9% | 49 · -6% |
| D | 17 · -32%* | 59 · -19% | 89 · -12% | 123 · -13% | 157 · -6% | 45 · -3% |
| L | 18 · -36%* | 59 · -16% | 88 · -7% | 126 · -14% | 154 · -7% | 45 · -24% |
| D+conf | 2 · -4%* | 10 · +14%* | 21 · +9%* | 32 · +14% | 40 · +20% | 18 · +17%* |
| D+fade | 11 · -31%* | 32 · -40% | 44 · -26% | 54 · -30% | 58 · -25% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 121. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.253 (n=87) | +0.047 (n=106) | +0.028 (n=107) | -0.050 (n=100) | -0.158 (n=19) | -0.087 (n=46) |
| spread · B | +0.156 (n=90) | -0.047 (n=106) | +0.036 (n=110) | +0.039 (n=103) | -0.167 (n=18) | +0.045 (n=44) |
| ml · A | +0.001 (n=83) | -0.002 (n=99) | -0.000 (n=104) | +0.001 (n=102) | +0.002 (n=20) | -0.003 (n=51) |
| ml · B | -0.004 (n=92) | -0.003 (n=118) | -0.002 (n=114) | -0.001 (n=105) | -0.005 (n=18) | -0.001 (n=54) |
| total · T | +1.027 (n=73) | +0.371 (n=89) | +0.135 (n=89) | +0.000 (n=88) | -0.143 (n=21) | +0.250 (n=44) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 178 | -0.219 (-0.56) | – | – | – |
| spread · A · D | 202 | -0.103 (-0.31) | – | – | – |
| spread · B · E | 178 | -0.452 (-1.29) | – | – | – |
| spread · B · D | 202 | -0.212 (-0.64) | – | – | – |
| ml · A · E | 178 | – | 0.2115 | 0.2023 | +0.0092 (1.88) |
| ml · A · D | 202 | – | 0.2082 | 0.1995 | +0.0086 (1.70) |
| ml · B · E | 178 | – | 0.2103 | 0.2023 | +0.0080 (1.41) |
| ml · B · D | 202 | – | 0.2057 | 0.1995 | +0.0062 (1.17) |
| total · T · E | 178 | +0.087 (0.23) | – | – | – |
| total · T · D | 202 | -0.235 (-0.67) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._