# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **141** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 20 · +5%* | 43 · +2% | 63 · -9% | 91 · -24% | 102 · -21% | 18 · +7%* |
| H6 | 24 · -13%* | 49 · -3% | 76 · +0% | 107 · -4% | 119 · -2% | 22 · -5%* |
| D | 29 · -8%* | 50 · +6% | 75 · +4% | 108 · -1% | 126 · -2% | 15 · +14%* |
| L | 27 · -22%* | 50 · -8% | 72 · +1% | 101 · +4% | 119 · -0% | 22 · -30%* |
| D+conf | 2 · -7%* | 8 · -4%* | 13 · +33%* | 19 · +11%* | 22 · -4%* | 4 · -53%* |
| D+fade | 17 · -11%* | 23 · +7%* | 31 · +10% | 40 · +4% | 40 · +4% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 27 · -43%* | 45 · -32% | 67 · -17% | 93 · -20% | 106 · -12% | 14 · -32%* |
| H6 | 30 · -6% | 52 · -5% | 74 · -13% | 109 · -13% | 125 · -12% | 16 · -39%* |
| D | 32 · -16% | 54 · -8% | 75 · -3% | 110 · -8% | 129 · -8% | 12 · -36%* |
| L | 28 · -32%* | 54 · -19% | 73 · -17% | 95 · -12% | 118 · -16% | 23 · -42%* |
| D+conf | 3 · -100%* | 7 · -45%* | 13 · -12%* | 25 · -15%* | 30 · -23% | 1 · -100%* |
| D+fade | 13 · -12%* | 20 · -5%* | 27 · +6%* | 35 · -2% | 36 · -5% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · -44%* | 42 · -20% | 61 · -24% | 91 · -23% | 109 · -26% | 11 · +69%* |
| H6 | 31 · -57% | 58 · -26% | 76 · -24% | 109 · -12% | 118 · -13% | 23 · -12%* |
| D | 30 · -47% | 56 · -21% | 77 · -15% | 106 · -10% | 124 · -11% | 17 · -43%* |
| L | 34 · -50% | 54 · -28% | 77 · -11% | 106 · -6% | 122 · -12% | 19 · -22%* |
| D+conf | 1 · -100%* | 9 · -31%* | 15 · -14%* | 22 · -21%* | 26 · -3%* | 4 · -67%* |
| D+fade | 21 · -46%* | 33 · -19% | 40 · -33% | 46 · -24% | 47 · -25% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 25 · -45%* | 46 · -38% | 63 · -33% | 89 · -31% | 99 · -30% | 21 · -35%* |
| H6 | 32 · -52% | 55 · -20% | 84 · -16% | 112 · -26% | 126 · -22% | 15 · -36%* |
| D | 30 · -53% | 53 · -36% | 81 · -20% | 116 · -19% | 126 · -18% | 15 · -44%* |
| L | 33 · -32% | 51 · -37% | 74 · -37% | 103 · -25% | 123 · -25% | 18 · +24%* |
| D+conf | 1 · -100%* | 5 · -72%* | 15 · -42%* | 23 · -49%* | 25 · -39%* | 5 · -100%* |
| D+fade | 22 · -79%* | 29 · -50%* | 39 · -42% | 47 · -39% | 47 · -39% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 15 · +2%* | 40 · +5% | 52 · +6% | 71 · -1% | 97 · +0% | 23 · -8%* |
| H6 | 12 · -21%* | 39 · -7% | 63 · -3% | 75 · +4% | 103 · +4% | 38 · -14% |
| D | 11 · -48%* | 38 · +1% | 60 · +5% | 83 · +4% | 110 · +4% | 31 · +11% |
| L | 10 · -43%* | 41 · -2% | 63 · +6% | 88 · +4% | 106 · +8% | 35 · -19% |
| D+conf | 2 · -4%* | 9 · +27%* | 18 · +27%* | 27 · +27%* | 34 · +30% | 15 · +27%* |
| D+fade | 6 · -69%* | 15 · -36%* | 23 · -17%* | 29 · -15%* | 32 · -11% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 103. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.079 (n=63) | -0.053 (n=76) | -0.027 (n=75) | -0.028 (n=72) | -0.077 (n=13) | -0.097 (n=31) |
| spread · B | +0.164 (n=67) | -0.162 (n=74) | -0.107 (n=75) | +0.027 (n=73) | -0.231 (n=13) | -0.074 (n=27) |
| ml · A | -0.000 (n=61) | -0.001 (n=76) | +0.001 (n=77) | +0.001 (n=77) | +0.002 (n=15) | -0.002 (n=40) |
| ml · B | +0.000 (n=63) | -0.003 (n=84) | -0.004 (n=81) | +0.000 (n=74) | -0.006 (n=15) | -0.005 (n=39) |
| total · T | +1.538 (n=52) | +0.508 (n=63) | +0.133 (n=60) | -0.032 (n=63) | +0.111 (n=18) | +0.174 (n=23) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 120 | -0.708 (-1.48) | – | – | – |
| spread · A · D | 141 | -0.336 (-0.84) | – | – | – |
| spread · B · E | 120 | -1.041 (-2.46) | – | – | – |
| spread · B · D | 141 | -0.683 (-1.66) | – | – | – |
| ml · A · E | 120 | – | 0.2047 | 0.1910 | +0.0137 (2.24) |
| ml · A · D | 141 | – | 0.2036 | 0.1924 | +0.0112 (1.74) |
| ml · B · E | 120 | – | 0.2111 | 0.1910 | +0.0201 (2.96) |
| ml · B · D | 141 | – | 0.2073 | 0.1924 | +0.0150 (2.37) |
| total · T · E | 120 | +0.693 (1.65) | – | – | – |
| total · T · D | 141 | +0.328 (0.81) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._