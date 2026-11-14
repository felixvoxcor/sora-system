# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **114** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 19 · +0%* | 41 · -2% | 59 · -12% | 78 · -22% | 87 · -19% | 15 · +15%* |
| H6 | 21 · -28%* | 41 · -17% | 66 · -8% | 87 · -10% | 98 · -7% | 16 · -16%* |
| D | 24 · -21%* | 42 · -5% | 64 · -2% | 87 · -6% | 102 · -3% | 12 · -5%* |
| L | 24 · -28%* | 44 · -13% | 64 · -1% | 84 · -0% | 96 · -3% | 18 · -47%* |
| D+conf | 2 · -7%* | 7 · -18%* | 12 · +28%* | 17 · +2%* | 18 · -4%* | 4 · -53%* |
| D+fade | 17 · -11%* | 22 · +4%* | 28 · +8%* | 34 · +6% | 34 · +6% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 22 · -39%* | 35 · -23% | 56 · -11% | 76 · -17% | 88 · -9% | 14 · -32%* |
| H6 | 24 · -13%* | 42 · -5% | 59 · -20% | 90 · -15% | 103 · -13% | 11 · -47%* |
| D | 24 · -20%* | 45 · -7% | 60 · -4% | 90 · -9% | 105 · -7% | 9 · -36%* |
| L | 23 · -42%* | 47 · -23% | 60 · -21% | 78 · -17% | 96 · -18% | 18 · -48%* |
| D+conf | 2 · -100%* | 6 · -36%* | 9 · -15%* | 18 · -14%* | 21 · -18%* | – |
| D+fade | 10 · -4%* | 17 · +1%* | 24 · +11%* | 32 · +1% | 33 · -2% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · -44%* | 39 · -33% | 54 · -31% | 78 · -32% | 94 · -32% | 8 · +30%* |
| H6 | 27 · -74%* | 49 · -45% | 63 · -43% | 89 · -27% | 95 · -25% | 19 · -11%* |
| D | 25 · -72%* | 47 · -46% | 63 · -38% | 86 · -24% | 99 · -23% | 15 · -36%* |
| L | 29 · -70%* | 47 · -44% | 64 · -38% | 86 · -19% | 99 · -27% | 15 · -12%* |
| D+conf | 1 · -100%* | 9 · -31%* | 15 · -14%* | 19 · -18%* | 22 · -4%* | 3 · -56%* |
| D+fade | 20 · -65%* | 30 · -40% | 35 · -49% | 39 · -37% | 40 · -39% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · -57%* | 38 · -48% | 51 · -42% | 76 · -36% | 85 · -33% | 17 · -19%* |
| H6 | 27 · -63%* | 41 · -40% | 67 · -34% | 94 · -40% | 105 · -33% | 9 · -18%* |
| D | 24 · -67%* | 43 · -50% | 66 · -35% | 96 · -33% | 106 · -30% | 8 · +6%* |
| L | 27 · -65%* | 43 · -59% | 61 · -50% | 87 · -40% | 100 · -39% | 14 · +36%* |
| D+conf | 1 · -100%* | 5 · -72%* | 13 · -44%* | 20 · -57%* | 22 · -45%* | – |
| D+fade | 18 · -75%* | 24 · -58%* | 33 · -45% | 41 · -40% | 41 · -40% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 11 · -13%* | 35 · -2% | 44 · -0% | 60 · -8% | 81 · -6% | 21 · +0%* |
| H6 | 11 · -13%* | 32 · -17% | 52 · -12% | 61 · -3% | 81 · -1% | 33 · -19% |
| D | 10 · -43%* | 29 · -14%* | 48 · -4% | 68 · -2% | 88 · -0% | 26 · +10%* |
| L | 8 · -52%* | 33 · -13% | 49 · -7% | 70 · -4% | 83 · +1% | 31 · -20% |
| D+conf | 2 · -4%* | 5 · -23%* | 13 · +3%* | 20 · +15%* | 24 · +12%* | 13 · +32%* |
| D+fade | 5 · -63%* | 13 · -27%* | 21 · -9%* | 27 · -8%* | 29 · -8%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 90. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.034 (n=59) | -0.091 (n=66) | -0.094 (n=64) | -0.016 (n=64) | -0.083 (n=12) | -0.143 (n=28) |
| spread · B | +0.179 (n=56) | -0.068 (n=59) | -0.033 (n=60) | +0.033 (n=60) | +0.000 (n=9) | -0.042 (n=24) |
| ml · A | -0.003 (n=54) | -0.001 (n=63) | -0.000 (n=63) | +0.000 (n=64) | +0.002 (n=15) | -0.003 (n=35) |
| ml · B | +0.001 (n=51) | -0.000 (n=67) | -0.002 (n=66) | +0.000 (n=61) | -0.002 (n=13) | -0.003 (n=33) |
| total · T | +1.500 (n=44) | +0.500 (n=52) | +0.167 (n=48) | -0.102 (n=49) | +0.000 (n=13) | +0.143 (n=21) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 102 | -0.828 (-1.71) | – | – | – |
| spread · A · D | 114 | -0.670 (-1.55) | – | – | – |
| spread · B · E | 102 | -1.127 (-2.50) | – | – | – |
| spread · B · D | 114 | -0.804 (-1.79) | – | – | – |
| ml · A · E | 102 | – | 0.1939 | 0.1766 | +0.0173 (2.57) |
| ml · A · D | 114 | – | 0.1957 | 0.1770 | +0.0187 (2.79) |
| ml · B · E | 102 | – | 0.1987 | 0.1766 | +0.0220 (3.06) |
| ml · B · D | 114 | – | 0.1962 | 0.1770 | +0.0192 (2.88) |
| total · T · E | 102 | +0.441 (0.92) | – | – | – |
| total · T · D | 114 | +0.148 (0.32) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._