# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **140** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 20 · +5%* | 43 · +2% | 62 · -7% | 90 · -24% | 101 · -21% | 18 · +7%* |
| H6 | 24 · -13%* | 49 · -3% | 76 · +0% | 106 · -3% | 118 · -1% | 22 · -5%* |
| D | 29 · -8%* | 50 · +6% | 74 · +5% | 107 · -0% | 125 · -1% | 15 · +14%* |
| L | 27 · -22%* | 50 · -8% | 71 · +2% | 100 · +5% | 118 · +0% | 22 · -30%* |
| D+conf | 2 · -7%* | 8 · -4%* | 13 · +33%* | 19 · +11%* | 22 · -4%* | 4 · -53%* |
| D+fade | 17 · -11%* | 23 · +7%* | 31 · +10% | 40 · +4% | 40 · +4% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 26 · -41%* | 44 · -30% | 66 · -16% | 92 · -19% | 105 · -11% | 14 · -32%* |
| H6 | 30 · -6% | 51 · -3% | 73 · -12% | 108 · -12% | 124 · -11% | 16 · -39%* |
| D | 31 · -14% | 53 · -6% | 74 · -2% | 109 · -7% | 128 · -8% | 12 · -36%* |
| L | 27 · -29%* | 53 · -17% | 72 · -15% | 94 · -11% | 117 · -15% | 23 · -42%* |
| D+conf | 3 · -100%* | 7 · -45%* | 13 · -12%* | 25 · -15%* | 30 · -23% | 1 · -100%* |
| D+fade | 13 · -12%* | 20 · -5%* | 27 · +6%* | 35 · -2% | 36 · -5% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · -44%* | 42 · -20% | 60 · -23% | 90 · -22% | 108 · -25% | 11 · +69%* |
| H6 | 31 · -57% | 58 · -26% | 76 · -24% | 108 · -11% | 117 · -12% | 23 · -12%* |
| D | 30 · -47% | 56 · -21% | 76 · -14% | 105 · -9% | 123 · -10% | 17 · -43%* |
| L | 34 · -50% | 54 · -28% | 76 · -10% | 105 · -5% | 121 · -12% | 19 · -22%* |
| D+conf | 1 · -100%* | 9 · -31%* | 15 · -14%* | 22 · -21%* | 26 · -3%* | 4 · -67%* |
| D+fade | 21 · -46%* | 33 · -19% | 40 · -33% | 46 · -24% | 47 · -25% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 25 · -45%* | 45 · -36% | 62 · -32% | 88 · -31% | 98 · -29% | 21 · -35%* |
| H6 | 32 · -52% | 54 · -19% | 83 · -15% | 111 · -25% | 125 · -22% | 15 · -36%* |
| D | 30 · -53% | 52 · -35% | 80 · -19% | 115 · -19% | 125 · -18% | 15 · -44%* |
| L | 33 · -32% | 50 · -36% | 73 · -36% | 102 · -24% | 122 · -25% | 18 · +24%* |
| D+conf | 1 · -100%* | 5 · -72%* | 15 · -42%* | 23 · -49%* | 25 · -39%* | 5 · -100%* |
| D+fade | 22 · -79%* | 29 · -50%* | 39 · -42% | 47 · -39% | 47 · -39% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 14 · -4%* | 39 · +3% | 51 · +5% | 70 · -2% | 96 · -1% | 23 · -8%* |
| H6 | 12 · -21%* | 38 · -10% | 62 · -5% | 74 · +3% | 102 · +3% | 38 · -14% |
| D | 11 · -48%* | 37 · -2% | 59 · +4% | 82 · +2% | 109 · +3% | 31 · +11% |
| L | 10 · -43%* | 41 · -2% | 62 · +4% | 87 · +3% | 105 · +7% | 35 · -19% |
| D+conf | 2 · -4%* | 8 · +19%* | 17 · +24%* | 26 · +25%* | 33 · +28% | 15 · +27%* |
| D+fade | 6 · -69%* | 15 · -36%* | 23 · -17%* | 29 · -15%* | 32 · -11% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 103. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.081 (n=62) | -0.053 (n=76) | -0.027 (n=74) | -0.028 (n=71) | -0.077 (n=13) | -0.097 (n=31) |
| spread · B | +0.167 (n=66) | -0.151 (n=73) | -0.108 (n=74) | +0.028 (n=72) | -0.231 (n=13) | -0.074 (n=27) |
| ml · A | -0.000 (n=60) | -0.001 (n=76) | +0.001 (n=76) | +0.001 (n=76) | +0.002 (n=15) | -0.002 (n=40) |
| ml · B | +0.000 (n=62) | -0.003 (n=83) | -0.004 (n=80) | +0.000 (n=73) | -0.006 (n=15) | -0.005 (n=39) |
| total · T | +1.490 (n=51) | +0.484 (n=62) | +0.119 (n=59) | -0.032 (n=62) | +0.059 (n=17) | +0.174 (n=23) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 119 | -0.653 (-1.38) | – | – | – |
| spread · A · D | 140 | -0.304 (-0.77) | – | – | – |
| spread · B · E | 119 | -0.967 (-2.30) | – | – | – |
| spread · B · D | 140 | -0.616 (-1.51) | – | – | – |
| ml · A · E | 119 | – | 0.2021 | 0.1890 | +0.0131 (2.13) |
| ml · A · D | 140 | – | 0.2013 | 0.1905 | +0.0108 (1.67) |
| ml · B · E | 119 | – | 0.2081 | 0.1890 | +0.0192 (2.82) |
| ml · B · D | 140 | – | 0.2047 | 0.1905 | +0.0142 (2.25) |
| total · T · E | 119 | +0.647 (1.51) | – | – | – |
| total · T · D | 140 | +0.303 (0.75) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._