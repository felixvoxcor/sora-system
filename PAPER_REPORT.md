# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **74** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 13 · +2%* | 25 · -1%* | 35 · -2% | 48 · -16% | 54 · -11% | 12 · +28%* |
| H6 | 13 · -56%* | 24 · -13%* | 37 · -7% | 52 · -5% | 61 · -3% | 13 · -26%* |
| D | 15 · -37%* | 26 · +2%* | 37 · +3% | 53 · +4% | 67 · +5% | 7 · -19%* |
| L | 16 · -40%* | 25 · -16%* | 37 · +4% | 52 · +14% | 63 · +6% | 11 · -83%* |
| D+conf | 1 · -100%* | 4 · -4%* | 7 · +39%* | 10 · +17%* | 11 · +6%* | 2 · -100%* |
| D+fade | 11 · -13%* | 15 · +14%* | 18 · +16%* | 23 · +15%* | 23 · +15%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 14 · -45%* | 23 · -25%* | 38 · -4% | 49 · -6% | 57 · +4% | 9 · -57%* |
| H6 | 14 · -18%* | 23 · -9%* | 34 · -16% | 62 · -11% | 69 · -9% | 5 · -61%* |
| D | 14 · -31%* | 26 · -19%* | 38 · -4% | 61 · -6% | 68 · -4% | 6 · -36%* |
| L | 14 · -46%* | 28 · -25%* | 39 · -22% | 52 · -19% | 63 · -18% | 11 · -48%* |
| D+conf | 2 · -100%* | 5 · -61%* | 7 · -17%* | 16 · -15%* | 16 · -15%* | – |
| D+fade | 6 · -4%* | 11 · +4%* | 17 · +23%* | 21 · +18%* | 22 · +12%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 15 · -36%* | 25 · -34%* | 33 · -23% | 50 · -19% | 60 · -20% | 6 · +14%* |
| H6 | 15 · -100%* | 29 · -36%* | 37 · -36% | 55 · -20% | 59 · -17% | 15 · +5%* |
| D | 14 · -100%* | 30 · -38% | 37 · -27% | 54 · -11% | 63 · -11% | 11 · -37%* |
| L | 18 · -73%* | 29 · -41%* | 37 · -34% | 53 · -4% | 61 · -15% | 13 · -11%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 12 · +18%* | 14 · +32%* | 3 · -56%* |
| D+fade | 11 · -100%* | 17 · -36%* | 19 · -43%* | 23 · -23%* | 24 · -27%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 14 · -58%* | 26 · -58%* | 33 · -43% | 51 · -32% | 57 · -27% | 9 · -5%* |
| H6 | 16 · -70%* | 25 · -56%* | 42 · -37% | 61 · -36% | 68 · -33% | 6 · +5%* |
| D | 14 · -66%* | 28 · -64%* | 43 · -40% | 64 · -31% | 71 · -32% | 3 · -7%* |
| L | 16 · -58%* | 27 · -64%* | 41 · -59% | 59 · -37% | 66 · -37% | 8 · +24%* |
| D+conf | 1 · -100%* | 4 · -100%* | 10 · -53%* | 14 · -57%* | 15 · -48%* | – |
| D+fade | 9 · -67%* | 14 · -63%* | 19 · -43%* | 24 · -29%* | 24 · -29%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 9 · +6%* | 25 · -1%* | 29 · +5%* | 39 · -17% | 56 · -15% | 10 · -23%* |
| H6 | 8 · -5%* | 24 · -13%* | 36 · -5% | 43 · +2% | 53 · -7% | 21 · -45%* |
| D | 6 · -37%* | 23 · -8%* | 35 · +4% | 50 · -1% | 60 · -4% | 14 · -5%* |
| L | 4 · -53%* | 25 · -8%* | 37 · -2% | 52 · -4% | 57 · -3% | 17 · -21%* |
| D+conf | 2 · -4%* | 5 · -23%* | 8 · +20%* | 13 · +18%* | 16 · +8%* | 6 · +27%* |
| D+fade | 3 · -38%* | 11 · -13%* | 18 · -5%* | 23 · -9%* | 24 · -13%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 60. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.029 (n=35) | -0.162 (n=37) | -0.054 (n=37) | -0.081 (n=37) | -0.286 (n=7) | +0.000 (n=18) |
| spread · B | +0.211 (n=38) | +0.029 (n=34) | -0.026 (n=38) | +0.077 (n=39) | +0.143 (n=7) | -0.059 (n=17) |
| ml · A | +0.001 (n=33) | -0.003 (n=37) | +0.001 (n=37) | +0.000 (n=37) | +0.000 (n=10) | +0.000 (n=19) |
| ml · B | +0.007 (n=33) | +0.002 (n=42) | +0.001 (n=43) | +0.000 (n=41) | +0.002 (n=10) | +0.001 (n=19) |
| total · T | +1.276 (n=29) | +0.444 (n=36) | +0.057 (n=35) | -0.162 (n=37) | +0.000 (n=8) | +0.111 (n=18) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 66 | -0.541 (-0.97) | – | – | – |
| spread · A · D | 74 | -0.271 (-0.54) | – | – | – |
| spread · B · E | 66 | -0.819 (-1.59) | – | – | – |
| spread · B · D | 74 | -0.668 (-1.27) | – | – | – |
| ml · A · E | 66 | – | 0.1990 | 0.1839 | +0.0152 (1.76) |
| ml · A · D | 74 | – | 0.2018 | 0.1866 | +0.0152 (1.84) |
| ml · B · E | 66 | – | 0.2086 | 0.1839 | +0.0247 (2.58) |
| ml · B · D | 74 | – | 0.2088 | 0.1866 | +0.0223 (2.56) |
| total · T · E | 66 | -0.153 (-0.24) | – | – | – |
| total · T · D | 74 | -0.203 (-0.34) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._