# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **78** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 14 · +9%* | 28 · +2%* | 39 · -2% | 52 · -15% | 58 · -11% | 12 · +28%* |
| H6 | 15 · -49%* | 27 · -9%* | 40 · -5% | 56 · -5% | 65 · -3% | 13 · -26%* |
| D | 17 · -33%* | 29 · +5%* | 40 · +5% | 57 · +4% | 71 · +5% | 7 · -19%* |
| L | 18 · -36%* | 28 · -11%* | 40 · +5% | 56 · +12% | 67 · +5% | 11 · -83%* |
| D+conf | 1 · -100%* | 4 · -4%* | 7 · +39%* | 11 · +6%* | 12 · -3%* | 2 · -100%* |
| D+fade | 13 · -12%* | 17 · +12%* | 20 · +14%* | 25 · +14%* | 25 · +14%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 14 · -45%* | 24 · -28%* | 39 · -7% | 51 · -6% | 60 · +5% | 10 · -61%* |
| H6 | 15 · -24%* | 25 · -9%* | 36 · -16% | 64 · -11% | 72 · -7% | 6 · -67%* |
| D | 16 · -28%* | 28 · -18%* | 40 · -4% | 63 · -6% | 71 · -3% | 7 · -45%* |
| L | 15 · -49%* | 30 · -24% | 41 · -21% | 54 · -19% | 66 · -16% | 12 · -53%* |
| D+conf | 2 · -100%* | 5 · -61%* | 7 · -17%* | 16 · -15%* | 16 · -15%* | – |
| D+fade | 8 · -4%* | 13 · +3%* | 19 · +20%* | 23 · +16%* | 24 · +11%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 17 · -44%* | 27 · -38%* | 37 · -26% | 54 · -21% | 64 · -22% | 6 · +14%* |
| H6 | 17 · -100%* | 31 · -40% | 41 · -37% | 59 · -22% | 63 · -19% | 15 · +5%* |
| D | 16 · -100%* | 32 · -42% | 40 · -27% | 58 · -14% | 67 · -13% | 11 · -37%* |
| L | 20 · -75%* | 31 · -45% | 40 · -34% | 57 · -7% | 65 · -17% | 13 · -11%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 13 · +9%* | 15 · +24%* | 3 · -56%* |
| D+fade | 13 · -100%* | 19 · -43%* | 21 · -48%* | 25 · -30%* | 26 · -32%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 15 · -61%* | 27 · -60%* | 34 · -45% | 52 · -34% | 59 · -30% | 11 · -4%* |
| H6 | 18 · -73%* | 27 · -60%* | 44 · -40% | 63 · -38% | 71 · -36% | 7 · -10%* |
| D | 16 · -70%* | 30 · -67% | 45 · -43% | 66 · -33% | 74 · -35% | 4 · +3%* |
| L | 18 · -63%* | 29 · -67%* | 43 · -61% | 61 · -39% | 69 · -39% | 9 · +25%* |
| D+conf | 1 · -100%* | 4 · -100%* | 10 · -53%* | 14 · -57%* | 15 · -48%* | – |
| D+fade | 11 · -73%* | 16 · -68%* | 21 · -48%* | 26 · -34%* | 26 · -34%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 9 · +6%* | 26 · +3%* | 30 · +8% | 41 · -12% | 59 · -10% | 11 · -13%* |
| H6 | 8 · -5%* | 24 · -13%* | 37 · -2% | 44 · +4% | 54 · -5% | 24 · -36%* |
| D | 6 · -37%* | 23 · -8%* | 36 · +6% | 51 · +1% | 63 · -3% | 15 · +1%* |
| L | 4 · -53%* | 25 · -8%* | 38 · +0% | 54 · -4% | 59 · -3% | 19 · -10%* |
| D+conf | 2 · -4%* | 5 · -23%* | 9 · +28%* | 14 · +23%* | 17 · +13%* | 7 · +36%* |
| D+fade | 3 · -38%* | 11 · -13%* | 18 · -5%* | 23 · -9%* | 24 · -13%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 65. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | -0.051 (n=39) | -0.175 (n=40) | -0.050 (n=40) | -0.075 (n=40) | -0.286 (n=7) | +0.000 (n=20) |
| spread · B | +0.179 (n=39) | +0.000 (n=36) | -0.025 (n=40) | +0.073 (n=41) | +0.143 (n=7) | -0.053 (n=19) |
| ml · A | -0.003 (n=37) | -0.004 (n=41) | -0.000 (n=40) | -0.000 (n=40) | +0.000 (n=10) | -0.001 (n=21) |
| ml · B | +0.006 (n=34) | +0.001 (n=44) | +0.001 (n=45) | +0.000 (n=43) | +0.002 (n=10) | -0.000 (n=21) |
| total · T | +1.267 (n=30) | +0.432 (n=37) | +0.056 (n=36) | -0.158 (n=38) | +0.000 (n=9) | +0.111 (n=18) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 70 | -0.591 (-1.09) | – | – | – |
| spread · A · D | 78 | -0.270 (-0.56) | – | – | – |
| spread · B · E | 70 | -0.884 (-1.71) | – | – | – |
| spread · B · D | 78 | -0.680 (-1.30) | – | – | – |
| ml · A · E | 70 | – | 0.1956 | 0.1798 | +0.0158 (1.89) |
| ml · A · D | 78 | – | 0.1985 | 0.1823 | +0.0162 (2.00) |
| ml · B · E | 70 | – | 0.2038 | 0.1798 | +0.0240 (2.66) |
| ml · B · D | 78 | – | 0.2053 | 0.1823 | +0.0230 (2.77) |
| total · T · E | 70 | +0.189 (0.31) | – | – | – |
| total · T · D | 78 | -0.036 (-0.06) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._