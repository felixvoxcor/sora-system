# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **129** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 19 · +0%* | 42 · +0% | 61 · -9% | 84 · -20% | 93 · -18% | 15 · +15%* |
| H6 | 24 · -13%* | 48 · -5% | 74 · +0% | 100 · -3% | 111 · -0% | 18 · -5%* |
| D | 29 · -8%* | 49 · +5% | 73 · +4% | 100 · +1% | 116 · +2% | 13 · +2%* |
| L | 27 · -22%* | 49 · -10% | 70 · +1% | 94 · +6% | 109 · +2% | 20 · -43%* |
| D+conf | 2 · -7%* | 7 · -18%* | 12 · +28%* | 18 · +7%* | 19 · +1%* | 4 · -53%* |
| D+fade | 17 · -11%* | 23 · +7%* | 31 · +10% | 37 · +8% | 37 · +8% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 25 · -39%* | 39 · -26% | 60 · -14% | 81 · -17% | 94 · -9% | 14 · -32%* |
| H6 | 29 · -2%* | 49 · +0% | 69 · -12% | 102 · -10% | 117 · -9% | 12 · -52%* |
| D | 29 · -8%* | 51 · -3% | 70 · -2% | 102 · -7% | 119 · -5% | 10 · -23%* |
| L | 26 · -27%* | 51 · -14% | 67 · -15% | 88 · -9% | 109 · -12% | 20 · -43%* |
| D+conf | 2 · -100%* | 6 · -36%* | 11 · -13%* | 20 · -14%* | 23 · -17%* | – |
| D+fade | 12 · -4%* | 19 · +0%* | 26 · +10%* | 34 · +0% | 35 · -2% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · -44%* | 41 · -28% | 56 · -28% | 83 · -29% | 100 · -30% | 8 · +30%* |
| H6 | 30 · -69% | 56 · -39% | 73 · -35% | 102 · -18% | 109 · -17% | 20 · -16%* |
| D | 29 · -60%* | 54 · -34% | 74 · -23% | 98 · -15% | 113 · -14% | 16 · -40%* |
| L | 33 · -62% | 52 · -42% | 72 · -22% | 98 · -10% | 113 · -18% | 16 · -17%* |
| D+conf | 1 · -100%* | 9 · -31%* | 15 · -14%* | 20 · -22%* | 24 · -2%* | 3 · -56%* |
| D+fade | 20 · -65%* | 31 · -42% | 38 · -53% | 42 · -42% | 43 · -43% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 25 · -45%* | 42 · -41% | 55 · -37% | 80 · -33% | 89 · -31% | 19 · -28%* |
| H6 | 31 · -51% | 50 · -24% | 78 · -17% | 106 · -27% | 119 · -23% | 10 · -26%* |
| D | 28 · -49%* | 49 · -39% | 75 · -19% | 109 · -20% | 119 · -18% | 10 · -15%* |
| L | 31 · -42% | 47 · -45% | 68 · -40% | 97 · -26% | 114 · -26% | 15 · +37%* |
| D+conf | 1 · -100%* | 5 · -72%* | 14 · -38%* | 21 · -52%* | 23 · -41%* | 1 · -100%* |
| D+fade | 20 · -77%* | 26 · -61%* | 35 · -48% | 43 · -43% | 43 · -43% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 12 · -4%* | 36 · +1% | 46 · +4% | 62 · -5% | 86 · -0% | 22 · -4%* |
| H6 | 11 · -13%* | 34 · -10% | 56 · -8% | 68 · +1% | 92 · +3% | 37 · -12% |
| D | 10 · -43%* | 33 · -1% | 55 · +4% | 76 · +3% | 99 · +4% | 30 · +15% |
| L | 8 · -52%* | 39 · -2% | 58 · +5% | 81 · +4% | 95 · +9% | 34 · -16% |
| D+conf | 2 · -4%* | 6 · -5%* | 15 · +15%* | 22 · +22%* | 27 · +21%* | 14 · +36%* |
| D+fade | 5 · -63%* | 13 · -27%* | 21 · -9%* | 27 · -8%* | 30 · -5% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 97. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.066 (n=61) | -0.095 (n=74) | -0.027 (n=73) | -0.029 (n=70) | -0.083 (n=12) | -0.097 (n=31) |
| spread · B | +0.100 (n=60) | -0.145 (n=69) | -0.071 (n=70) | +0.045 (n=67) | -0.182 (n=11) | -0.077 (n=26) |
| ml · A | -0.003 (n=56) | -0.002 (n=73) | +0.001 (n=74) | +0.000 (n=72) | +0.002 (n=15) | -0.002 (n=38) |
| ml · B | -0.001 (n=55) | -0.003 (n=78) | -0.004 (n=75) | +0.000 (n=68) | -0.007 (n=14) | -0.004 (n=35) |
| total · T | +1.500 (n=46) | +0.429 (n=56) | +0.091 (n=55) | -0.069 (n=58) | +0.000 (n=15) | +0.143 (n=21) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 108 | -0.766 (-1.59) | – | – | – |
| spread · A · D | 129 | -0.399 (-1.00) | – | – | – |
| spread · B · E | 108 | -1.026 (-2.36) | – | – | – |
| spread · B · D | 129 | -0.604 (-1.44) | – | – | – |
| ml · A · E | 108 | – | 0.1941 | 0.1783 | +0.0158 (2.42) |
| ml · A · D | 129 | – | 0.1943 | 0.1811 | +0.0133 (1.96) |
| ml · B · E | 108 | – | 0.1981 | 0.1783 | +0.0198 (2.74) |
| ml · B · D | 129 | – | 0.1947 | 0.1811 | +0.0136 (2.06) |
| total · T · E | 108 | +0.714 (1.53) | – | – | – |
| total · T · D | 129 | +0.399 (0.91) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._