# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **108** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 17 · +12%* | 38 · +0% | 53 · -10% | 72 · -20% | 81 · -18% | 15 · +15%* |
| H6 | 20 · -33%* | 38 · -15% | 61 · -3% | 82 · -7% | 93 · -4% | 15 · -24%* |
| D | 23 · -25%* | 38 · +0% | 59 · +3% | 82 · -2% | 97 · +0% | 11 · -13%* |
| L | 24 · -28%* | 40 · -9% | 59 · +4% | 79 · +4% | 91 · +1% | 17 · -55%* |
| D+conf | 2 · -7%* | 5 · +14%* | 10 · +54%* | 15 · +15%* | 16 · +8%* | 3 · -100%* |
| D+fade | 16 · -17%* | 20 · +5%* | 26 · +10%* | 32 · +7% | 32 · +7% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · -36%* | 34 · -21% | 54 · -12% | 71 · -14% | 82 · -5% | 14 · -32%* |
| H6 | 24 · -13%* | 40 · -5% | 55 · -17% | 85 · -13% | 97 · -10% | 11 · -47%* |
| D | 24 · -20%* | 43 · -6% | 58 · -4% | 86 · -9% | 99 · -5% | 9 · -36%* |
| L | 23 · -42%* | 45 · -20% | 57 · -20% | 74 · -18% | 91 · -18% | 17 · -56%* |
| D+conf | 2 · -100%* | 6 · -36%* | 9 · -15%* | 18 · -14%* | 20 · -14%* | – |
| D+fade | 10 · -4%* | 15 · +2%* | 22 · +13%* | 29 · +5%* | 30 · +1% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · -38%* | 36 · -36% | 48 · -29% | 72 · -30% | 88 · -31% | 8 · +30%* |
| H6 | 25 · -85%* | 45 · -47% | 59 · -45% | 83 · -26% | 89 · -23% | 19 · -11%* |
| D | 23 · -84%* | 42 · -47% | 58 · -38% | 80 · -22% | 93 · -21% | 15 · -36%* |
| L | 28 · -69%* | 42 · -45% | 59 · -38% | 80 · -17% | 93 · -25% | 15 · -12%* |
| D+conf | – | 7 · -11%* | 13 · -1%* | 16 · -2%* | 19 · +11%* | 3 · -56%* |
| D+fade | 19 · -81%* | 27 · -46%* | 32 · -54% | 36 · -41% | 37 · -42% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · -57%* | 36 · -54% | 48 · -45% | 71 · -38% | 80 · -34% | 16 · -14%* |
| H6 | 27 · -63%* | 40 · -47% | 64 · -38% | 88 · -40% | 99 · -34% | 9 · -18%* |
| D | 24 · -67%* | 42 · -57% | 64 · -40% | 91 · -36% | 101 · -33% | 7 · +21%* |
| L | 27 · -65%* | 42 · -58% | 58 · -55% | 81 · -43% | 94 · -42% | 14 · +36%* |
| D+conf | 1 · -100%* | 5 · -72%* | 13 · -44%* | 18 · -52%* | 20 · -39%* | – |
| D+fade | 18 · -75%* | 23 · -71%* | 31 · -55% | 39 · -48% | 39 · -48% | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 10 · -4%* | 32 · -5% | 40 · -5% | 56 · -11% | 76 · -10% | 20 · +6%* |
| H6 | 10 · -5%* | 31 · -14% | 50 · -13% | 57 · -7% | 77 · -4% | 31 · -26% |
| D | 9 · -36%* | 28 · -11%* | 46 · -4% | 64 · -4% | 82 · -5% | 26 · +10%* |
| L | 7 · -45%* | 31 · -14% | 47 · -7% | 66 · -7% | 77 · -3% | 31 · -20% |
| D+conf | 2 · -4%* | 5 · -23%* | 12 · -4%* | 17 · +2%* | 21 · +1%* | 13 · +32%* |
| D+fade | 4 · -53%* | 12 · -21%* | 20 · -5%* | 26 · -5%* | 28 · -5%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 88. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | -0.019 (n=53) | -0.098 (n=61) | -0.119 (n=59) | -0.017 (n=59) | -0.100 (n=10) | -0.192 (n=26) |
| spread · B | +0.167 (n=54) | -0.073 (n=55) | -0.052 (n=58) | +0.035 (n=57) | +0.000 (n=9) | -0.091 (n=22) |
| ml · A | -0.003 (n=48) | -0.001 (n=59) | -0.000 (n=58) | +0.000 (n=59) | +0.003 (n=13) | -0.003 (n=32) |
| ml · B | -0.000 (n=48) | -0.001 (n=64) | -0.002 (n=64) | +0.000 (n=58) | -0.002 (n=13) | -0.004 (n=31) |
| total · T | +1.550 (n=40) | +0.540 (n=50) | +0.174 (n=46) | -0.128 (n=47) | +0.083 (n=12) | +0.100 (n=20) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 96 | -0.652 (-1.29) | – | – | – |
| spread · A · D | 108 | -0.541 (-1.22) | – | – | – |
| spread · B · E | 96 | -0.992 (-2.19) | – | – | – |
| spread · B · D | 108 | -0.840 (-1.87) | – | – | – |
| ml · A · E | 96 | – | 0.1950 | 0.1777 | +0.0174 (2.50) |
| ml · A · D | 108 | – | 0.1968 | 0.1781 | +0.0187 (2.73) |
| ml · B · E | 96 | – | 0.2011 | 0.1777 | +0.0234 (3.12) |
| ml · B · D | 108 | – | 0.1995 | 0.1781 | +0.0214 (3.11) |
| total · T · E | 96 | +0.340 (0.66) | – | – | – |
| total · T · D | 108 | +0.108 (0.22) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._