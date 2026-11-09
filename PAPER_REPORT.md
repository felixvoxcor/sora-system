# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **76** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 13 · +2%* | 26 · -5%* | 37 · -7% | 50 · -20% | 56 · -15% | 12 · +28%* |
| H6 | 14 · -59%* | 25 · -17%* | 38 · -10% | 54 · -8% | 63 · -6% | 13 · -26%* |
| D | 16 · -40%* | 27 · -1%* | 38 · +0% | 55 · +0% | 69 · +2% | 7 · -19%* |
| L | 17 · -44%* | 26 · -19%* | 38 · +1% | 54 · +9% | 65 · +3% | 11 · -83%* |
| D+conf | 1 · -100%* | 4 · -4%* | 7 · +39%* | 11 · +6%* | 12 · -3%* | 2 · -100%* |
| D+fade | 12 · -21%* | 16 · +7%* | 19 · +10%* | 24 · +10%* | 24 · +10%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 14 · -45%* | 24 · -28%* | 39 · -7% | 50 · -8% | 58 · +2% | 10 · -61%* |
| H6 | 15 · -24%* | 24 · -13%* | 35 · -19% | 63 · -12% | 71 · -9% | 5 · -61%* |
| D | 15 · -36%* | 27 · -22%* | 39 · -7% | 62 · -7% | 70 · -4% | 6 · -36%* |
| L | 15 · -49%* | 29 · -28%* | 40 · -24% | 53 · -21% | 65 · -18% | 11 · -48%* |
| D+conf | 2 · -100%* | 5 · -61%* | 7 · -17%* | 16 · -15%* | 16 · -15%* | – |
| D+fade | 7 · -17%* | 12 · -4%* | 18 · +17%* | 22 · +12%* | 23 · +8%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 16 · -40%* | 26 · -36%* | 35 · -27% | 52 · -22% | 62 · -23% | 6 · +14%* |
| H6 | 16 · -100%* | 30 · -38% | 39 · -39% | 57 · -23% | 61 · -20% | 15 · +5%* |
| D | 15 · -100%* | 31 · -40% | 38 · -29% | 56 · -15% | 65 · -14% | 11 · -37%* |
| L | 19 · -74%* | 30 · -43% | 38 · -36% | 55 · -8% | 63 · -18% | 13 · -11%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 13 · +9%* | 15 · +24%* | 3 · -56%* |
| D+fade | 12 · -100%* | 18 · -39%* | 20 · -45%* | 24 · -27%* | 25 · -30%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 15 · -61%* | 27 · -60%* | 34 · -45% | 52 · -34% | 58 · -29% | 10 · -15%* |
| H6 | 17 · -72%* | 26 · -58%* | 43 · -38% | 62 · -37% | 69 · -34% | 7 · -10%* |
| D | 15 · -68%* | 29 · -66%* | 44 · -42% | 65 · -32% | 72 · -33% | 4 · +3%* |
| L | 17 · -60%* | 28 · -65%* | 42 · -60% | 60 · -38% | 67 · -38% | 9 · +25%* |
| D+conf | 1 · -100%* | 4 · -100%* | 10 · -53%* | 14 · -57%* | 15 · -48%* | – |
| D+fade | 10 · -70%* | 15 · -65%* | 20 · -46%* | 25 · -32%* | 25 · -32%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 9 · +6%* | 25 · -1%* | 29 · +5%* | 40 · -14% | 58 · -11% | 10 · -23%* |
| H6 | 8 · -5%* | 24 · -13%* | 36 · -5% | 43 · +2% | 53 · -7% | 23 · -41%* |
| D | 6 · -37%* | 23 · -8%* | 35 · +4% | 50 · -1% | 61 · -3% | 15 · +1%* |
| L | 4 · -53%* | 25 · -8%* | 37 · -2% | 52 · -4% | 57 · -3% | 19 · -10%* |
| D+conf | 2 · -4%* | 5 · -23%* | 8 · +20%* | 13 · +18%* | 16 · +8%* | 7 · +36%* |
| D+fade | 3 · -38%* | 11 · -13%* | 18 · -5%* | 23 · -9%* | 24 · -13%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 62. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.027 (n=37) | -0.158 (n=38) | -0.053 (n=38) | -0.079 (n=38) | -0.286 (n=7) | +0.000 (n=19) |
| spread · B | +0.179 (n=39) | +0.029 (n=35) | -0.026 (n=39) | +0.075 (n=40) | +0.143 (n=7) | -0.056 (n=18) |
| ml · A | +0.000 (n=35) | -0.003 (n=39) | +0.001 (n=38) | +0.000 (n=38) | +0.000 (n=10) | -0.001 (n=20) |
| ml · B | +0.006 (n=34) | +0.002 (n=43) | +0.001 (n=44) | +0.000 (n=42) | +0.002 (n=10) | +0.000 (n=20) |
| total · T | +1.276 (n=29) | +0.444 (n=36) | +0.057 (n=35) | -0.162 (n=37) | +0.000 (n=8) | +0.111 (n=18) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 68 | -0.714 (-1.29) | – | – | – |
| spread · A · D | 76 | -0.397 (-0.78) | – | – | – |
| spread · B · E | 68 | -0.888 (-1.71) | – | – | – |
| spread · B · D | 76 | -0.709 (-1.33) | – | – | – |
| ml · A · E | 68 | – | 0.1958 | 0.1799 | +0.0159 (1.90) |
| ml · A · D | 76 | – | 0.1988 | 0.1830 | +0.0158 (1.96) |
| ml · B · E | 68 | – | 0.2046 | 0.1799 | +0.0247 (2.66) |
| ml · B · D | 76 | – | 0.2053 | 0.1830 | +0.0223 (2.63) |
| total · T · E | 68 | -0.111 (-0.18) | – | – | – |
| total · T · D | 76 | -0.205 (-0.35) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._