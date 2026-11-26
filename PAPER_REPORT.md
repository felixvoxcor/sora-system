# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **199** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · +8%* | 54 · +3% | 85 · -5% | 132 · -19% | 149 · -14% | 26 · -12%* |
| H6 | 28 · -12%* | 61 · -10% | 104 · -1% | 150 · -6% | 165 · -4% | 34 · -5% |
| D | 34 · -11% | 63 · -7% | 105 · -0% | 147 · -3% | 174 · -2% | 25 · +7%* |
| L | 35 · -18% | 67 · -9% | 98 · +1% | 141 · +5% | 163 · +2% | 33 · -24% |
| D+conf | 4 · -4%* | 10 · -4%* | 19 · +42%* | 27 · +28%* | 34 · +13% | 10 · -3%* |
| D+fade | 20 · -15%* | 31 · -8% | 44 · -1% | 54 · -5% | 55 · -7% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 34 · -21% | 58 · -14% | 89 · -6% | 134 · -9% | 154 · -3% | 21 · -37%* |
| H6 | 40 · +4% | 68 · +0% | 103 · -4% | 155 · -4% | 179 · -3% | 20 · -32%* |
| D | 38 · -4% | 67 · -0% | 107 · +3% | 155 · -3% | 183 · -3% | 16 · -28%* |
| L | 34 · -16% | 67 · -6% | 101 · -4% | 136 · +2% | 167 · -2% | 29 · -35%* |
| D+conf | 5 · -23%* | 11 · +4%* | 18 · +17%* | 32 · +8% | 40 · +5% | 2 · -100%* |
| D+fade | 16 · -4%* | 24 · -5%* | 41 · -3% | 52 · -9% | 53 · -11% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 29 · -28%* | 52 · -17% | 82 · -14% | 129 · -15% | 156 · -17% | 19 · +20%* |
| H6 | 38 · -41% | 71 · -16% | 97 · -16% | 153 · -9% | 173 · -9% | 26 · +3%* |
| D | 37 · -43% | 71 · -23% | 102 · -13% | 148 · -5% | 176 · -6% | 23 · -58%* |
| L | 45 · -38% | 70 · -25% | 100 · -9% | 143 · +1% | 168 · -5% | 27 · -19%* |
| D+conf | 3 · +27%* | 13 · +17%* | 20 · +26%* | 31 · +14% | 39 · +15% | 5 · -74%* |
| D+fade | 26 · -51%* | 41 · -32% | 50 · -44% | 63 · -37% | 64 · -38% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 35 · -15% | 58 · -23% | 89 · -9% | 136 · -14% | 152 · -15% | 23 · -40%* |
| H6 | 43 · -34% | 74 · -13% | 115 · -7% | 159 · -12% | 178 · -8% | 21 · -39%* |
| D | 38 · -17% | 69 · -17% | 111 · -3% | 161 · -8% | 176 · -6% | 23 · -22%* |
| L | 40 · -1% | 64 · -17% | 103 · -16% | 144 · -12% | 170 · -13% | 25 · +39%* |
| D+conf | 2 · +91%* | 7 · -2%* | 18 · -12%* | 29 · -19%* | 32 · -6% | 11 · -14%* |
| D+fade | 26 · -69%* | 36 · -45% | 52 · -32% | 65 · -31% | 65 · -31% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · -15%* | 54 · -12% | 71 · -11% | 100 · -14% | 137 · -7% | 38 · -29% |
| H6 | 17 · -33%* | 56 · -29% | 87 · -21% | 114 · -10% | 150 · -9% | 49 · -6% |
| D | 15 · -49%* | 57 · -23% | 87 · -14% | 120 · -14% | 154 · -7% | 45 · -3% |
| L | 17 · -32%* | 57 · -16% | 86 · -7% | 123 · -13% | 151 · -6% | 45 · -24% |
| D+conf | 2 · -4%* | 10 · +14%* | 21 · +9%* | 32 · +14% | 40 · +20% | 18 · +17%* |
| D+fade | 9 · -58%* | 30 · -49% | 42 · -32% | 51 · -33% | 55 · -27% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 120. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.235 (n=85) | +0.048 (n=104) | +0.029 (n=105) | -0.061 (n=98) | -0.158 (n=19) | -0.091 (n=44) |
| spread · B | +0.169 (n=89) | -0.029 (n=103) | +0.037 (n=107) | +0.030 (n=101) | -0.167 (n=18) | +0.049 (n=41) |
| ml · A | +0.001 (n=82) | -0.002 (n=97) | -0.000 (n=102) | +0.000 (n=100) | +0.002 (n=20) | -0.003 (n=50) |
| ml · B | -0.003 (n=89) | -0.003 (n=115) | -0.002 (n=111) | -0.001 (n=103) | -0.005 (n=18) | -0.001 (n=52) |
| total · T | +1.056 (n=71) | +0.368 (n=87) | +0.092 (n=87) | -0.023 (n=86) | -0.143 (n=21) | +0.167 (n=42) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 175 | -0.240 (-0.61) | – | – | – |
| spread · A · D | 199 | -0.098 (-0.29) | – | – | – |
| spread · B · E | 175 | -0.452 (-1.28) | – | – | – |
| spread · B · D | 199 | -0.216 (-0.64) | – | – | – |
| ml · A · E | 175 | – | 0.2124 | 0.2029 | +0.0095 (1.92) |
| ml · A · D | 199 | – | 0.2090 | 0.2001 | +0.0089 (1.73) |
| ml · B · E | 175 | – | 0.2114 | 0.2029 | +0.0085 (1.49) |
| ml · B · D | 199 | – | 0.2069 | 0.2001 | +0.0068 (1.28) |
| total · T · E | 175 | +0.063 (0.16) | – | – | – |
| total · T · D | 199 | -0.295 (-0.82) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._