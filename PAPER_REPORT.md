# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **93** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 17 · +12%* | 33 · -2% | 48 · -12% | 65 · -24% | 72 · -18% | 13 · +18%* |
| H6 | 18 · -37%* | 34 · -16% | 50 · -8% | 68 · -10% | 79 · -6% | 14 · -32%* |
| D | 21 · -27%* | 33 · +4% | 49 · +1% | 68 · -2% | 83 · +1% | 10 · -24%* |
| L | 22 · -30%* | 35 · -7% | 49 · +2% | 67 · +6% | 79 · +1% | 14 · -73%* |
| D+conf | 2 · -7%* | 5 · +14%* | 8 · +45%* | 13 · +4%* | 14 · -3%* | 3 · -100%* |
| D+fade | 15 · -24%* | 19 · +0%* | 23 · +7%* | 28 · +8%* | 28 · +8%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 17 · -55%* | 30 · -30% | 47 · -11% | 63 · -15% | 73 · -3% | 12 · -52%* |
| H6 | 20 · -33%* | 32 · -11% | 44 · -18% | 72 · -12% | 82 · -7% | 11 · -47%* |
| D | 21 · -36%* | 36 · -15% | 48 · -4% | 72 · -7% | 84 · -2% | 9 · -36%* |
| L | 20 · -52%* | 36 · -26% | 47 · -23% | 62 · -20% | 76 · -17% | 17 · -56%* |
| D+conf | 2 · -100%* | 5 · -61%* | 7 · -17%* | 16 · -15%* | 18 · -14%* | – |
| D+fade | 10 · -4%* | 15 · +2%* | 21 · +18%* | 26 · +10%* | 27 · +6%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · -38%* | 33 · -35% | 43 · -25% | 64 · -24% | 77 · -27% | 8 · +30%* |
| H6 | 22 · -83%* | 39 · -39% | 49 · -36% | 71 · -20% | 75 · -18% | 18 · -6%* |
| D | 20 · -82%* | 38 · -41% | 48 · -28% | 67 · -15% | 78 · -13% | 15 · -36%* |
| L | 25 · -65%* | 38 · -39% | 50 · -30% | 67 · -8% | 78 · -18% | 15 · -12%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 13 · +9%* | 16 · +23%* | 3 · -56%* |
| D+fade | 17 · -78%* | 25 · -42%* | 27 · -46%* | 31 · -31% | 32 · -33% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · -59%* | 31 · -56% | 42 · -44% | 62 · -34% | 71 · -30% | 14 · -13%* |
| H6 | 22 · -71%* | 33 · -50% | 52 · -36% | 73 · -37% | 84 · -29% | 9 · -18%* |
| D | 21 · -62%* | 36 · -58% | 54 · -37% | 76 · -31% | 86 · -28% | 7 · +21%* |
| L | 23 · -59%* | 35 · -59% | 49 · -56% | 67 · -38% | 79 · -38% | 14 · +36%* |
| D+conf | 1 · -100%* | 4 · -100%* | 11 · -46%* | 15 · -51%* | 17 · -37%* | – |
| D+fade | 15 · -70%* | 20 · -66%* | 26 · -52%* | 32 · -42% | 32 · -42% | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 10 · -4%* | 30 · +2% | 36 · +1% | 51 · -10% | 70 · -8% | 15 · +15%* |
| H6 | 9 · -15%* | 29 · -15%* | 45 · -7% | 52 · -1% | 67 · -3% | 26 · -41%* |
| D | 8 · -53%* | 26 · -12%* | 42 · +0% | 58 · -1% | 74 · -2% | 19 · -0%* |
| L | 6 · -69%* | 29 · -15%* | 44 · -5% | 61 · -6% | 68 · -2% | 25 · -16%* |
| D+conf | 2 · -4%* | 5 · -23%* | 10 · +15%* | 15 · +15%* | 19 · +11%* | 9 · +27%* |
| D+fade | 4 · -53%* | 12 · -21%* | 20 · -5%* | 26 · -5%* | 28 · -5%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 81. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | -0.083 (n=48) | -0.220 (n=50) | -0.163 (n=49) | -0.041 (n=49) | -0.125 (n=8) | -0.217 (n=23) |
| spread · B | +0.149 (n=47) | -0.182 (n=44) | -0.062 (n=48) | +0.064 (n=47) | +0.143 (n=7) | -0.095 (n=21) |
| ml · A | -0.004 (n=43) | -0.003 (n=49) | -0.001 (n=48) | +0.000 (n=50) | +0.000 (n=10) | -0.003 (n=27) |
| ml · B | -0.001 (n=42) | -0.002 (n=52) | -0.001 (n=54) | +0.001 (n=49) | -0.001 (n=11) | -0.002 (n=26) |
| total · T | +1.500 (n=36) | +0.511 (n=45) | +0.119 (n=42) | -0.136 (n=44) | +0.000 (n=10) | +0.100 (n=20) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 85 | -0.798 (-1.58) | – | – | – |
| spread · A · D | 93 | -0.595 (-1.29) | – | – | – |
| spread · B · E | 85 | -1.156 (-2.42) | – | – | – |
| spread · B · D | 93 | -0.883 (-1.80) | – | – | – |
| ml · A · E | 85 | – | 0.1942 | 0.1779 | +0.0163 (2.14) |
| ml · A · D | 93 | – | 0.1967 | 0.1808 | +0.0159 (2.06) |
| ml · B · E | 85 | – | 0.2003 | 0.1779 | +0.0224 (2.78) |
| ml · B · D | 93 | – | 0.2007 | 0.1808 | +0.0199 (2.59) |
| total · T · E | 85 | +0.316 (0.62) | – | – | – |
| total · T · D | 93 | +0.087 (0.17) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._