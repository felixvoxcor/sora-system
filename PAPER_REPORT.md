# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **196** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · +8%* | 54 · +3% | 85 · -5% | 129 · -20% | 146 · -15% | 26 · -12%* |
| H6 | 28 · -12%* | 61 · -10% | 104 · -1% | 148 · -6% | 163 · -4% | 33 · -8% |
| D | 34 · -11% | 63 · -7% | 104 · -1% | 145 · -3% | 172 · -2% | 24 · +3%* |
| L | 35 · -18% | 67 · -9% | 97 · +0% | 139 · +6% | 161 · +2% | 32 · -28% |
| D+conf | 4 · -4%* | 10 · -4%* | 19 · +42%* | 27 · +28%* | 34 · +13% | 9 · -15%* |
| D+fade | 20 · -15%* | 31 · -8% | 43 · -3% | 53 · -7% | 54 · -9% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 34 · -21% | 56 · -15% | 87 · -6% | 131 · -8% | 151 · -3% | 21 · -37%* |
| H6 | 39 · +2% | 66 · +1% | 100 · -3% | 152 · -3% | 176 · -3% | 20 · -32%* |
| D | 37 · -7% | 65 · -0% | 104 · +5% | 152 · -2% | 180 · -3% | 16 · -28%* |
| L | 33 · -19% | 65 · -6% | 98 · -3% | 133 · +3% | 164 · -1% | 29 · -35%* |
| D+conf | 5 · -23%* | 11 · +4%* | 18 · +17%* | 32 · +8% | 40 · +5% | 2 · -100%* |
| D+fade | 15 · -11%* | 23 · -9%* | 39 · -3% | 50 · -9% | 51 · -11% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 29 · -28%* | 52 · -17% | 81 · -13% | 127 · -15% | 153 · -17% | 19 · +20%* |
| H6 | 38 · -41% | 71 · -16% | 96 · -15% | 151 · -9% | 170 · -9% | 26 · +3%* |
| D | 37 · -43% | 71 · -23% | 101 · -12% | 146 · -5% | 173 · -6% | 23 · -58%* |
| L | 45 · -38% | 70 · -25% | 99 · -9% | 141 · +1% | 165 · -6% | 27 · -19%* |
| D+conf | 3 · +27%* | 13 · +17%* | 20 · +26%* | 31 · +14% | 39 · +15% | 5 · -74%* |
| D+fade | 26 · -51%* | 41 · -32% | 50 · -44% | 62 · -39% | 63 · -40% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 35 · -15% | 57 · -22% | 86 · -8% | 133 · -13% | 149 · -14% | 23 · -40%* |
| H6 | 43 · -34% | 72 · -13% | 112 · -6% | 156 · -11% | 175 · -8% | 21 · -39%* |
| D | 37 · -21% | 67 · -18% | 108 · -2% | 158 · -8% | 173 · -6% | 23 · -22%* |
| L | 39 · -4% | 62 · -18% | 100 · -16% | 141 · -12% | 167 · -13% | 25 · +39%* |
| D+conf | 2 · +91%* | 7 · -2%* | 18 · -12%* | 29 · -19%* | 32 · -6% | 11 · -14%* |
| D+fade | 25 · -77%* | 35 · -50% | 51 · -35% | 64 · -33% | 64 · -33% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · -15%* | 53 · -14% | 70 · -13% | 98 · -14% | 134 · -6% | 38 · -29% |
| H6 | 17 · -33%* | 55 · -27% | 85 · -22% | 111 · -11% | 147 · -9% | 49 · -6% |
| D | 15 · -49%* | 56 · -21% | 85 · -15% | 117 · -15% | 151 · -8% | 45 · -3% |
| L | 17 · -32%* | 56 · -15% | 83 · -8% | 120 · -14% | 148 · -7% | 45 · -24% |
| D+conf | 2 · -4%* | 10 · +14%* | 21 · +9%* | 31 · +11% | 39 · +18% | 18 · +17%* |
| D+fade | 9 · -58%* | 29 · -47%* | 41 · -30% | 50 · -31% | 54 · -26% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 119. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.235 (n=85) | +0.048 (n=104) | +0.029 (n=104) | -0.062 (n=97) | -0.158 (n=19) | -0.093 (n=43) |
| spread · B | +0.184 (n=87) | -0.020 (n=100) | +0.038 (n=104) | +0.031 (n=98) | -0.167 (n=18) | +0.051 (n=39) |
| ml · A | +0.001 (n=81) | -0.002 (n=96) | -0.000 (n=101) | +0.000 (n=99) | +0.002 (n=20) | -0.003 (n=50) |
| ml · B | -0.003 (n=86) | -0.003 (n=112) | -0.002 (n=108) | -0.001 (n=100) | -0.005 (n=18) | -0.001 (n=51) |
| total · T | +1.057 (n=70) | +0.376 (n=85) | +0.094 (n=85) | -0.024 (n=83) | -0.143 (n=21) | +0.171 (n=41) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 172 | -0.255 (-0.64) | – | – | – |
| spread · A · D | 196 | -0.113 (-0.33) | – | – | – |
| spread · B · E | 172 | -0.451 (-1.26) | – | – | – |
| spread · B · D | 196 | -0.226 (-0.65) | – | – | – |
| ml · A · E | 172 | – | 0.2122 | 0.2027 | +0.0095 (1.89) |
| ml · A · D | 196 | – | 0.2087 | 0.1998 | +0.0089 (1.72) |
| ml · B · E | 172 | – | 0.2109 | 0.2027 | +0.0081 (1.42) |
| ml · B · D | 196 | – | 0.2064 | 0.1998 | +0.0066 (1.25) |
| total · T · E | 172 | +0.083 (0.22) | – | – | – |
| total · T · D | 196 | -0.341 (-0.94) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._