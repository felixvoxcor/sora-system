# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **128** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 19 · +0%* | 42 · +0% | 61 · -9% | 83 · -19% | 92 · -17% | 15 · +15%* |
| H6 | 24 · -13%* | 48 · -5% | 74 · +0% | 99 · -2% | 110 · +0% | 18 · -5%* |
| D | 29 · -8%* | 49 · +5% | 72 · +6% | 99 · +2% | 115 · +3% | 13 · +2%* |
| L | 27 · -22%* | 48 · -8% | 69 · +2% | 93 · +7% | 108 · +2% | 20 · -43%* |
| D+conf | 2 · -7%* | 7 · -18%* | 12 · +28%* | 18 · +7%* | 19 · +1%* | 4 · -53%* |
| D+fade | 17 · -11%* | 23 · +7%* | 30 · +14% | 36 · +11% | 36 · +11% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 24 · -36%* | 38 · -24% | 59 · -13% | 80 · -16% | 93 · -8% | 14 · -32%* |
| H6 | 28 · +1%* | 48 · +3% | 68 · -11% | 101 · -10% | 116 · -8% | 12 · -52%* |
| D | 28 · -4%* | 50 · -1% | 69 · -1% | 101 · -6% | 118 · -5% | 10 · -23%* |
| L | 26 · -27%* | 51 · -14% | 67 · -15% | 88 · -9% | 109 · -12% | 19 · -40%* |
| D+conf | 2 · -100%* | 6 · -36%* | 11 · -13%* | 20 · -14%* | 23 · -17%* | – |
| D+fade | 11 · +4%* | 18 · +6%* | 25 · +14%* | 33 · +3% | 34 · +0% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · -44%* | 41 · -28% | 56 · -28% | 82 · -28% | 99 · -30% | 8 · +30%* |
| H6 | 30 · -69% | 56 · -39% | 72 · -34% | 101 · -17% | 108 · -16% | 20 · -16%* |
| D | 29 · -60%* | 54 · -34% | 73 · -22% | 97 · -14% | 112 · -13% | 16 · -40%* |
| L | 33 · -62% | 51 · -41% | 71 · -21% | 97 · -9% | 112 · -17% | 16 · -17%* |
| D+conf | 1 · -100%* | 9 · -31%* | 15 · -14%* | 20 · -22%* | 24 · -2%* | 3 · -56%* |
| D+fade | 20 · -65%* | 31 · -42% | 37 · -52% | 41 · -40% | 42 · -42% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 24 · -42%* | 41 · -40% | 54 · -36% | 79 · -33% | 88 · -30% | 19 · -28%* |
| H6 | 30 · -49% | 49 · -23% | 77 · -16% | 105 · -26% | 118 · -22% | 10 · -26%* |
| D | 27 · -47%* | 48 · -38% | 74 · -18% | 108 · -19% | 118 · -18% | 10 · -15%* |
| L | 31 · -42% | 47 · -45% | 68 · -40% | 97 · -26% | 113 · -26% | 15 · +37%* |
| D+conf | 1 · -100%* | 5 · -72%* | 14 · -38%* | 21 · -52%* | 23 · -41%* | 1 · -100%* |
| D+fade | 19 · -76%* | 25 · -60%* | 34 · -46% | 42 · -42% | 42 · -42% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 12 · -4%* | 36 · +1% | 46 · +4% | 62 · -5% | 85 · -1% | 22 · -4%* |
| H6 | 11 · -13%* | 34 · -10% | 56 · -8% | 68 · +1% | 91 · +3% | 37 · -12% |
| D | 10 · -43%* | 33 · -1% | 55 · +4% | 76 · +3% | 98 · +3% | 30 · +15% |
| L | 8 · -52%* | 39 · -2% | 57 · +4% | 80 · +3% | 94 · +8% | 34 · -16% |
| D+conf | 2 · -4%* | 6 · -5%* | 15 · +15%* | 22 · +22%* | 26 · +18%* | 14 · +36%* |
| D+fade | 5 · -63%* | 13 · -27%* | 21 · -9%* | 27 · -8%* | 30 · -5% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 97. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.066 (n=61) | -0.095 (n=74) | -0.014 (n=72) | -0.029 (n=69) | -0.083 (n=12) | -0.067 (n=30) |
| spread · B | +0.136 (n=59) | -0.118 (n=68) | -0.058 (n=69) | +0.045 (n=67) | -0.182 (n=11) | -0.040 (n=25) |
| ml · A | -0.003 (n=56) | -0.002 (n=72) | +0.001 (n=73) | +0.000 (n=71) | +0.002 (n=15) | -0.001 (n=37) |
| ml · B | +0.000 (n=54) | -0.002 (n=77) | -0.003 (n=74) | +0.000 (n=68) | -0.007 (n=14) | -0.003 (n=34) |
| total · T | +1.500 (n=46) | +0.429 (n=56) | +0.091 (n=55) | -0.070 (n=57) | +0.000 (n=15) | +0.143 (n=21) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 107 | -0.761 (-1.57) | – | – | – |
| spread · A · D | 128 | -0.390 (-0.98) | – | – | – |
| spread · B · E | 107 | -0.996 (-2.27) | – | – | – |
| spread · B · D | 128 | -0.566 (-1.34) | – | – | – |
| ml · A · E | 107 | – | 0.1953 | 0.1795 | +0.0158 (2.40) |
| ml · A · D | 128 | – | 0.1954 | 0.1822 | +0.0132 (1.93) |
| ml · B · E | 107 | – | 0.1990 | 0.1795 | +0.0195 (2.67) |
| ml · B · D | 128 | – | 0.1953 | 0.1822 | +0.0131 (1.98) |
| total · T · E | 107 | +0.707 (1.50) | – | – | – |
| total · T · D | 128 | +0.396 (0.90) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._