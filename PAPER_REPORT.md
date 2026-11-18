# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **138** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 20 · +5%* | 43 · +2% | 62 · -7% | 89 · -23% | 100 · -20% | 17 · +13%* |
| H6 | 24 · -13%* | 49 · -3% | 75 · +1% | 104 · -3% | 116 · -1% | 22 · -5%* |
| D | 29 · -8%* | 50 · +6% | 74 · +5% | 105 · -0% | 123 · -1% | 15 · +14%* |
| L | 27 · -22%* | 50 · -8% | 71 · +2% | 98 · +5% | 116 · +0% | 22 · -30%* |
| D+conf | 2 · -7%* | 8 · -4%* | 13 · +33%* | 19 · +11%* | 22 · -4%* | 4 · -53%* |
| D+fade | 17 · -11%* | 23 · +7%* | 31 · +10% | 40 · +4% | 40 · +4% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 26 · -41%* | 43 · -29% | 65 · -15% | 90 · -19% | 103 · -11% | 14 · -32%* |
| H6 | 30 · -6% | 51 · -3% | 73 · -12% | 107 · -11% | 123 · -10% | 15 · -48%* |
| D | 31 · -14% | 53 · -6% | 73 · -3% | 107 · -7% | 126 · -8% | 12 · -36%* |
| L | 27 · -29%* | 53 · -17% | 72 · -15% | 93 · -10% | 116 · -14% | 22 · -48%* |
| D+conf | 3 · -100%* | 7 · -45%* | 13 · -12%* | 24 · -12%* | 29 · -21%* | 1 · -100%* |
| D+fade | 13 · -12%* | 20 · -5%* | 27 · +6%* | 35 · -2% | 36 · -5% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · -44%* | 42 · -20% | 59 · -25% | 88 · -26% | 106 · -29% | 11 · +69%* |
| H6 | 31 · -57% | 57 · -33% | 74 · -30% | 106 · -15% | 115 · -16% | 23 · -12%* |
| D | 30 · -47% | 55 · -28% | 75 · -18% | 103 · -13% | 121 · -14% | 17 · -43%* |
| L | 34 · -50% | 53 · -35% | 74 · -16% | 103 · -9% | 119 · -15% | 19 · -22%* |
| D+conf | 1 · -100%* | 9 · -31%* | 15 · -14%* | 21 · -25%* | 25 · -5%* | 4 · -67%* |
| D+fade | 21 · -46%* | 32 · -31% | 39 · -43% | 45 · -32% | 46 · -33% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 25 · -45%* | 45 · -36% | 62 · -32% | 87 · -30% | 97 · -29% | 20 · -31%* |
| H6 | 32 · -52% | 54 · -19% | 83 · -15% | 111 · -25% | 125 · -22% | 13 · -26%* |
| D | 30 · -53% | 52 · -35% | 79 · -18% | 114 · -18% | 124 · -17% | 14 · -40%* |
| L | 33 · -32% | 50 · -36% | 73 · -36% | 102 · -24% | 121 · -26% | 17 · +32%* |
| D+conf | 1 · -100%* | 5 · -72%* | 15 · -42%* | 23 · -49%* | 25 · -39%* | 4 · -100%* |
| D+fade | 22 · -79%* | 29 · -50%* | 38 · -41% | 46 · -37% | 46 · -37% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 14 · -4%* | 39 · +3% | 50 · +7% | 68 · -2% | 94 · -1% | 23 · -8%* |
| H6 | 12 · -21%* | 38 · -10% | 61 · -6% | 73 · +2% | 100 · +3% | 38 · -14% |
| D | 11 · -48%* | 37 · -2% | 59 · +4% | 81 · +4% | 107 · +4% | 31 · +11% |
| L | 10 · -43%* | 41 · -2% | 61 · +3% | 85 · +3% | 103 · +8% | 35 · -19% |
| D+conf | 2 · -4%* | 8 · +19%* | 17 · +24%* | 25 · +30%* | 31 · +30% | 15 · +27%* |
| D+fade | 6 · -69%* | 15 · -36%* | 23 · -17%* | 29 · -15%* | 32 · -11% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 102. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.081 (n=62) | -0.093 (n=75) | -0.027 (n=74) | -0.028 (n=71) | -0.077 (n=13) | -0.097 (n=31) |
| spread · B | +0.138 (n=65) | -0.151 (n=73) | -0.082 (n=73) | +0.028 (n=72) | -0.231 (n=13) | -0.074 (n=27) |
| ml · A | -0.002 (n=59) | -0.002 (n=74) | +0.001 (n=75) | +0.000 (n=74) | +0.002 (n=15) | -0.002 (n=39) |
| ml · B | +0.000 (n=62) | -0.003 (n=83) | -0.003 (n=79) | +0.000 (n=73) | -0.006 (n=15) | -0.003 (n=38) |
| total · T | +1.500 (n=50) | +0.459 (n=61) | +0.119 (n=59) | -0.066 (n=61) | +0.059 (n=17) | +0.174 (n=23) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 117 | -0.669 (-1.41) | – | – | – |
| spread · A · D | 138 | -0.361 (-0.92) | – | – | – |
| spread · B · E | 117 | -0.932 (-2.20) | – | – | – |
| spread · B · D | 138 | -0.623 (-1.52) | – | – | – |
| ml · A · E | 117 | – | 0.2000 | 0.1857 | +0.0143 (2.30) |
| ml · A · D | 138 | – | 0.1995 | 0.1875 | +0.0120 (1.85) |
| ml · B · E | 117 | – | 0.2046 | 0.1857 | +0.0189 (2.74) |
| ml · B · D | 138 | – | 0.2014 | 0.1875 | +0.0139 (2.17) |
| total · T · E | 117 | +0.686 (1.60) | – | – | – |
| total · T · D | 138 | +0.321 (0.79) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._