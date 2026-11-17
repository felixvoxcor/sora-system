# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **134** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 19 · +0%* | 42 · +0% | 61 · -9% | 87 · -23% | 98 · -20% | 15 · +15%* |
| H6 | 24 · -13%* | 48 · -5% | 74 · +0% | 102 · -5% | 113 · -2% | 21 · -1%* |
| D | 29 · -8%* | 49 · +5% | 73 · +4% | 102 · -1% | 119 · -1% | 15 · +14%* |
| L | 27 · -22%* | 49 · -10% | 70 · +1% | 96 · +3% | 112 · -1% | 22 · -30%* |
| D+conf | 2 · -7%* | 7 · -18%* | 12 · +28%* | 18 · +7%* | 20 · -4%* | 4 · -53%* |
| D+fade | 17 · -11%* | 23 · +7%* | 31 · +10% | 38 · +5% | 38 · +5% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 26 · -41%* | 42 · -32% | 64 · -17% | 86 · -20% | 99 · -11% | 14 · -32%* |
| H6 | 30 · -6% | 51 · -3% | 71 · -15% | 105 · -13% | 120 · -11% | 14 · -45%* |
| D | 31 · -14% | 53 · -6% | 72 · -5% | 105 · -9% | 123 · -9% | 11 · -30%* |
| L | 27 · -29%* | 53 · -17% | 70 · -18% | 91 · -12% | 113 · -16% | 21 · -46%* |
| D+conf | 3 · -100%* | 7 · -45%* | 12 · -20%* | 22 · -22%* | 26 · -26%* | – |
| D+fade | 13 · -12%* | 20 · -5%* | 27 · +6%* | 35 · -2% | 36 · -5% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · -44%* | 41 · -28% | 57 · -29% | 85 · -30% | 103 · -32% | 10 · +69%* |
| H6 | 30 · -69% | 56 · -39% | 73 · -35% | 103 · -18% | 112 · -19% | 22 · -16%* |
| D | 29 · -60%* | 54 · -34% | 74 · -23% | 100 · -17% | 117 · -16% | 17 · -43%* |
| L | 33 · -62% | 52 · -42% | 72 · -22% | 100 · -12% | 115 · -19% | 19 · -22%* |
| D+conf | 1 · -100%* | 9 · -31%* | 15 · -14%* | 20 · -22%* | 24 · -2%* | 4 · -67%* |
| D+fade | 20 · -65%* | 31 · -42% | 38 · -53% | 43 · -43% | 44 · -44% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 25 · -45%* | 44 · -44% | 59 · -38% | 84 · -34% | 93 · -31% | 20 · -31%* |
| H6 | 32 · -52% | 52 · -27% | 81 · -20% | 109 · -29% | 122 · -25% | 12 · -20%* |
| D | 30 · -53% | 51 · -42% | 78 · -23% | 112 · -22% | 122 · -20% | 12 · -30%* |
| L | 32 · -44% | 48 · -46% | 71 · -43% | 100 · -28% | 118 · -29% | 16 · +29%* |
| D+conf | 1 · -100%* | 5 · -72%* | 15 · -42%* | 22 · -54%* | 24 · -43%* | 2 · -100%* |
| D+fade | 22 · -79%* | 28 · -64%* | 37 · -51% | 45 · -46% | 45 · -46% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 13 · +3%* | 38 · +6% | 49 · +9% | 65 · -0% | 90 · +2% | 23 · -8%* |
| H6 | 11 · -13%* | 36 · -5% | 59 · -3% | 71 · +5% | 97 · +4% | 37 · -12% |
| D | 10 · -43%* | 35 · +4% | 57 · +7% | 79 · +6% | 104 · +5% | 30 · +15% |
| L | 9 · -36%* | 40 · +0% | 59 · +7% | 83 · +6% | 100 · +9% | 34 · -16% |
| D+conf | 2 · -4%* | 8 · +19%* | 17 · +24%* | 25 · +30%* | 30 · +28% | 14 · +36%* |
| D+fade | 5 · -63%* | 13 · -27%* | 21 · -9%* | 27 · -8%* | 30 · -5% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 101. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.066 (n=61) | -0.095 (n=74) | -0.027 (n=73) | -0.029 (n=70) | -0.083 (n=12) | -0.097 (n=31) |
| spread · B | +0.125 (n=64) | -0.141 (n=71) | -0.083 (n=72) | +0.029 (n=70) | -0.250 (n=12) | -0.074 (n=27) |
| ml · A | -0.002 (n=57) | -0.002 (n=73) | +0.001 (n=74) | +0.000 (n=72) | +0.002 (n=15) | -0.002 (n=38) |
| ml · B | +0.000 (n=59) | -0.003 (n=81) | -0.003 (n=78) | +0.000 (n=71) | -0.006 (n=15) | -0.004 (n=37) |
| total · T | +1.592 (n=49) | +0.458 (n=59) | +0.105 (n=57) | -0.068 (n=59) | +0.059 (n=17) | +0.143 (n=21) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 113 | -0.773 (-1.61) | – | – | – |
| spread · A · D | 134 | -0.416 (-1.05) | – | – | – |
| spread · B · E | 113 | -1.035 (-2.42) | – | – | – |
| spread · B · D | 134 | -0.694 (-1.68) | – | – | – |
| ml · A · E | 113 | – | 0.1968 | 0.1813 | +0.0155 (2.48) |
| ml · A · D | 134 | – | 0.1968 | 0.1834 | +0.0134 (2.06) |
| ml · B · E | 113 | – | 0.2015 | 0.1813 | +0.0202 (2.88) |
| ml · B · D | 134 | – | 0.1988 | 0.1834 | +0.0154 (2.38) |
| total · T · E | 113 | +0.838 (1.87) | – | – | – |
| total · T · D | 134 | +0.458 (1.06) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._