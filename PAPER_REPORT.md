# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **132** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 19 · +0%* | 42 · +0% | 61 · -9% | 86 · -22% | 96 · -20% | 15 · +15%* |
| H6 | 24 · -13%* | 48 · -5% | 74 · +0% | 101 · -4% | 112 · -1% | 20 · +4%* |
| D | 29 · -8%* | 49 · +5% | 73 · +4% | 101 · -0% | 117 · +1% | 15 · +14%* |
| L | 27 · -22%* | 49 · -10% | 70 · +1% | 94 · +6% | 110 · +1% | 22 · -30%* |
| D+conf | 2 · -7%* | 7 · -18%* | 12 · +28%* | 18 · +7%* | 19 · +1%* | 4 · -53%* |
| D+fade | 17 · -11%* | 23 · +7%* | 31 · +10% | 38 · +5% | 38 · +5% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 26 · -41%* | 41 · -30% | 62 · -17% | 84 · -20% | 97 · -12% | 14 · -32%* |
| H6 | 30 · -6% | 50 · -2% | 70 · -13% | 104 · -12% | 119 · -10% | 13 · -55%* |
| D | 30 · -11% | 52 · -5% | 71 · -3% | 104 · -8% | 122 · -8% | 10 · -23%* |
| L | 26 · -27%* | 52 · -16% | 69 · -17% | 90 · -11% | 112 · -15% | 20 · -43%* |
| D+conf | 2 · -100%* | 6 · -36%* | 11 · -13%* | 21 · -18%* | 25 · -23%* | – |
| D+fade | 13 · -12%* | 20 · -5%* | 27 · +6%* | 35 · -2% | 36 · -5% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · -44%* | 41 · -28% | 57 · -29% | 84 · -30% | 102 · -32% | 9 · +63%* |
| H6 | 30 · -69% | 56 · -39% | 73 · -35% | 102 · -18% | 111 · -18% | 21 · -12%* |
| D | 29 · -60%* | 54 · -34% | 74 · -23% | 98 · -15% | 115 · -14% | 17 · -43%* |
| L | 33 · -62% | 52 · -42% | 72 · -22% | 98 · -10% | 113 · -18% | 19 · -22%* |
| D+conf | 1 · -100%* | 9 · -31%* | 15 · -14%* | 20 · -22%* | 24 · -2%* | 4 · -67%* |
| D+fade | 20 · -65%* | 31 · -42% | 38 · -53% | 42 · -42% | 43 · -43% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 25 · -45%* | 44 · -44% | 57 · -39% | 82 · -35% | 91 · -32% | 20 · -31%* |
| H6 | 32 · -52% | 51 · -26% | 80 · -19% | 108 · -28% | 121 · -24% | 11 · -33%* |
| D | 29 · -51%* | 50 · -41% | 77 · -22% | 111 · -21% | 121 · -20% | 11 · -23%* |
| L | 31 · -42% | 47 · -45% | 70 · -42% | 99 · -28% | 116 · -28% | 16 · +29%* |
| D+conf | 1 · -100%* | 5 · -72%* | 15 · -42%* | 22 · -54%* | 24 · -43%* | 2 · -100%* |
| D+fade | 21 · -78%* | 27 · -63%* | 36 · -49% | 44 · -44% | 44 · -44% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 13 · +3%* | 38 · +6% | 48 · +7% | 64 · -2% | 88 · +2% | 23 · -8%* |
| H6 | 11 · -13%* | 36 · -5% | 58 · -5% | 70 · +3% | 95 · +4% | 37 · -12% |
| D | 10 · -43%* | 35 · +4% | 57 · +7% | 78 · +5% | 102 · +5% | 30 · +15% |
| L | 9 · -36%* | 40 · +0% | 59 · +7% | 83 · +6% | 98 · +9% | 34 · -16% |
| D+conf | 2 · -4%* | 8 · +19%* | 17 · +24%* | 24 · +28%* | 29 · +26%* | 14 · +36%* |
| D+fade | 5 · -63%* | 13 · -27%* | 21 · -9%* | 27 · -8%* | 30 · -5% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 99. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.066 (n=61) | -0.095 (n=74) | -0.027 (n=73) | -0.029 (n=70) | -0.083 (n=12) | -0.097 (n=31) |
| spread · B | +0.113 (n=62) | -0.143 (n=70) | -0.070 (n=71) | +0.029 (n=69) | -0.182 (n=11) | -0.074 (n=27) |
| ml · A | -0.002 (n=57) | -0.002 (n=73) | +0.001 (n=74) | +0.000 (n=72) | +0.002 (n=15) | -0.002 (n=38) |
| ml · B | -0.000 (n=57) | -0.002 (n=80) | -0.003 (n=77) | +0.000 (n=70) | -0.006 (n=15) | -0.003 (n=36) |
| total · T | +1.521 (n=48) | +0.431 (n=58) | +0.105 (n=57) | -0.068 (n=59) | +0.059 (n=17) | +0.143 (n=21) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 111 | -0.766 (-1.60) | – | – | – |
| spread · A · D | 132 | -0.389 (-0.98) | – | – | – |
| spread · B · E | 111 | -1.059 (-2.48) | – | – | – |
| spread · B · D | 132 | -0.651 (-1.57) | – | – | – |
| ml · A · E | 111 | – | 0.1963 | 0.1806 | +0.0156 (2.46) |
| ml · A · D | 132 | – | 0.1962 | 0.1830 | +0.0131 (1.98) |
| ml · B · E | 111 | – | 0.2013 | 0.1806 | +0.0207 (2.92) |
| ml · B · D | 132 | – | 0.1976 | 0.1830 | +0.0146 (2.23) |
| total · T · E | 111 | +0.833 (1.86) | – | – | – |
| total · T · D | 132 | +0.478 (1.11) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._