# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **126** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 19 · +0%* | 42 · +0% | 61 · -9% | 81 · -17% | 90 · -15% | 15 · +15%* |
| H6 | 24 · -13%* | 47 · -7% | 73 · -1% | 97 · -2% | 108 · +1% | 18 · -5%* |
| D | 29 · -8%* | 48 · +3% | 71 · +5% | 97 · +2% | 113 · +3% | 13 · +2%* |
| L | 27 · -22%* | 47 · -10% | 68 · +1% | 92 · +6% | 107 · +2% | 19 · -40%* |
| D+conf | 2 · -7%* | 7 · -18%* | 12 · +28%* | 18 · +7%* | 19 · +1%* | 4 · -53%* |
| D+fade | 17 · -11%* | 22 · +4%* | 29 · +11%* | 35 · +8% | 35 · +8% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · -33%* | 37 · -22% | 58 · -11% | 79 · -15% | 91 · -8% | 14 · -32%* |
| H6 | 27 · -2%* | 47 · +1% | 67 · -12% | 100 · -10% | 114 · -10% | 12 · -52%* |
| D | 27 · -8%* | 49 · -3% | 68 · -2% | 100 · -7% | 117 · -5% | 9 · -36%* |
| L | 25 · -31%* | 50 · -16% | 65 · -18% | 86 · -11% | 107 · -14% | 19 · -40%* |
| D+conf | 2 · -100%* | 6 · -36%* | 11 · -13%* | 20 · -14%* | 23 · -17%* | – |
| D+fade | 10 · -4%* | 17 · +1%* | 24 · +11%* | 32 · +1% | 33 · -2% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · -44%* | 40 · -26% | 55 · -27% | 80 · -26% | 97 · -28% | 8 · +30%* |
| H6 | 30 · -69% | 55 · -38% | 71 · -33% | 99 · -15% | 106 · -14% | 20 · -16%* |
| D | 29 · -60%* | 53 · -33% | 72 · -21% | 95 · -12% | 110 · -12% | 16 · -40%* |
| L | 32 · -61% | 50 · -40% | 70 · -20% | 95 · -8% | 110 · -15% | 16 · -17%* |
| D+conf | 1 · -100%* | 9 · -31%* | 15 · -14%* | 19 · -18%* | 23 · +3%* | 3 · -56%* |
| D+fade | 20 · -65%* | 30 · -40% | 36 · -50% | 40 · -39% | 41 · -40% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · -40%* | 40 · -38% | 53 · -35% | 78 · -32% | 87 · -29% | 18 · -24%* |
| H6 | 29 · -47%* | 48 · -21% | 76 · -15% | 104 · -26% | 117 · -21% | 9 · -18%* |
| D | 26 · -45%* | 47 · -37% | 73 · -17% | 107 · -18% | 117 · -17% | 9 · -6%* |
| L | 30 · -40% | 46 · -43% | 67 · -39% | 96 · -25% | 111 · -25% | 15 · +37%* |
| D+conf | 1 · -100%* | 5 · -72%* | 14 · -38%* | 21 · -52%* | 23 · -41%* | – |
| D+fade | 18 · -75%* | 24 · -58%* | 33 · -45% | 41 · -40% | 41 · -40% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 12 · -4%* | 36 · +1% | 45 · +2% | 61 · -6% | 83 · -4% | 22 · -4%* |
| H6 | 11 · -13%* | 34 · -10% | 56 · -8% | 66 · -2% | 89 · +1% | 37 · -12% |
| D | 10 · -43%* | 33 · -1% | 54 · +3% | 75 · +2% | 96 · +1% | 30 · +15% |
| L | 8 · -52%* | 39 · -2% | 56 · +2% | 79 · +2% | 92 · +6% | 34 · -16% |
| D+conf | 2 · -4%* | 6 · -5%* | 14 · +9%* | 21 · +19%* | 25 · +15%* | 14 · +36%* |
| D+fade | 5 · -63%* | 13 · -27%* | 21 · -9%* | 27 · -8%* | 29 · -8%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 94. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.066 (n=61) | -0.096 (n=73) | -0.014 (n=71) | -0.029 (n=68) | -0.083 (n=12) | -0.069 (n=29) |
| spread · B | +0.172 (n=58) | -0.119 (n=67) | -0.059 (n=68) | +0.031 (n=65) | -0.182 (n=11) | -0.042 (n=24) |
| ml · A | -0.002 (n=55) | -0.002 (n=71) | +0.002 (n=72) | +0.000 (n=70) | +0.002 (n=15) | -0.001 (n=36) |
| ml · B | +0.001 (n=53) | -0.002 (n=76) | -0.003 (n=73) | +0.000 (n=67) | -0.007 (n=14) | -0.003 (n=33) |
| total · T | +1.511 (n=45) | +0.429 (n=56) | +0.093 (n=54) | -0.071 (n=56) | +0.000 (n=14) | +0.143 (n=21) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 105 | -0.756 (-1.56) | – | – | – |
| spread · A · D | 126 | -0.396 (-0.99) | – | – | – |
| spread · B · E | 105 | -1.034 (-2.34) | – | – | – |
| spread · B · D | 126 | -0.606 (-1.41) | – | – | – |
| ml · A · E | 105 | – | 0.1969 | 0.1815 | +0.0153 (2.29) |
| ml · A · D | 126 | – | 0.1967 | 0.1839 | +0.0128 (1.84) |
| ml · B · E | 105 | – | 0.2002 | 0.1815 | +0.0187 (2.54) |
| ml · B · D | 126 | – | 0.1963 | 0.1839 | +0.0123 (1.84) |
| total · T · E | 105 | +0.578 (1.24) | – | – | – |
| total · T · D | 126 | +0.298 (0.68) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._