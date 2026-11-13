# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **106** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 17 · +12%* | 38 · +0% | 53 · -10% | 72 · -20% | 80 · -16% | 14 · +9%* |
| H6 | 20 · -33%* | 38 · -15% | 61 · -3% | 81 · -8% | 92 · -5% | 14 · -32%* |
| D | 23 · -25%* | 38 · +0% | 59 · +3% | 81 · -4% | 96 · -1% | 10 · -24%* |
| L | 24 · -28%* | 40 · -9% | 59 · +4% | 79 · +4% | 91 · +1% | 15 · -75%* |
| D+conf | 2 · -7%* | 5 · +14%* | 10 · +54%* | 15 · +15%* | 16 · +8%* | 3 · -100%* |
| D+fade | 16 · -17%* | 20 · +5%* | 26 · +10%* | 32 · +7% | 32 · +7% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 19 · -40%* | 32 · -22% | 52 · -12% | 69 · -14% | 80 · -5% | 14 · -32%* |
| H6 | 23 · -18%* | 39 · -8% | 53 · -18% | 83 · -13% | 95 · -10% | 11 · -47%* |
| D | 23 · -25%* | 42 · -9% | 56 · -4% | 84 · -9% | 97 · -5% | 9 · -36%* |
| L | 23 · -42%* | 43 · -20% | 55 · -20% | 72 · -18% | 89 · -19% | 17 · -56%* |
| D+conf | 2 · -100%* | 6 · -36%* | 8 · -4%* | 17 · -9%* | 19 · -9%* | – |
| D+fade | 10 · -4%* | 15 · +2%* | 22 · +13%* | 29 · +5%* | 30 · +1% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · -38%* | 36 · -36% | 48 · -29% | 72 · -30% | 86 · -31% | 8 · +30%* |
| H6 | 25 · -85%* | 45 · -47% | 59 · -45% | 82 · -29% | 88 · -27% | 18 · -6%* |
| D | 23 · -84%* | 42 · -47% | 58 · -38% | 79 · -26% | 91 · -23% | 15 · -36%* |
| L | 28 · -69%* | 42 · -45% | 59 · -38% | 79 · -20% | 91 · -28% | 15 · -12%* |
| D+conf | – | 7 · -11%* | 13 · -1%* | 16 · -2%* | 19 · +11%* | 3 · -56%* |
| D+fade | 19 · -81%* | 27 · -46%* | 32 · -54% | 36 · -41% | 37 · -42% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 19 · -53%* | 34 · -51% | 46 · -42% | 69 · -36% | 78 · -33% | 16 · -14%* |
| H6 | 26 · -62%* | 39 · -45% | 62 · -36% | 86 · -39% | 97 · -32% | 9 · -18%* |
| D | 23 · -65%* | 41 · -55% | 62 · -38% | 89 · -34% | 99 · -31% | 7 · +21%* |
| L | 26 · -63%* | 41 · -57% | 57 · -54% | 79 · -41% | 92 · -40% | 14 · +36%* |
| D+conf | 1 · -100%* | 5 · -72%* | 12 · -39%* | 17 · -49%* | 19 · -36%* | – |
| D+fade | 17 · -73%* | 22 · -69%* | 30 · -54% | 38 · -47% | 38 · -47% | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 10 · -4%* | 32 · -5% | 39 · -7% | 55 · -13% | 75 · -11% | 19 · +1%* |
| H6 | 10 · -5%* | 31 · -14% | 50 · -13% | 57 · -7% | 77 · -4% | 29 · -34%* |
| D | 9 · -36%* | 28 · -11%* | 46 · -4% | 64 · -4% | 82 · -5% | 24 · +3%* |
| L | 7 · -45%* | 31 · -14% | 47 · -7% | 66 · -7% | 76 · -4% | 30 · -24% |
| D+conf | 2 · -4%* | 5 · -23%* | 12 · -4%* | 17 · +2%* | 21 · +1%* | 12 · +27%* |
| D+fade | 4 · -53%* | 12 · -21%* | 20 · -5%* | 26 · -5%* | 28 · -5%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 88. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | -0.019 (n=53) | -0.098 (n=61) | -0.119 (n=59) | -0.017 (n=59) | -0.100 (n=10) | -0.192 (n=26) |
| spread · B | +0.154 (n=52) | -0.057 (n=53) | -0.036 (n=56) | +0.036 (n=55) | +0.125 (n=8) | -0.091 (n=22) |
| ml · A | -0.003 (n=48) | -0.001 (n=59) | -0.000 (n=58) | +0.000 (n=59) | +0.003 (n=13) | -0.003 (n=32) |
| ml · B | -0.000 (n=46) | -0.000 (n=62) | -0.002 (n=62) | +0.000 (n=57) | -0.002 (n=12) | -0.003 (n=30) |
| total · T | +1.538 (n=39) | +0.540 (n=50) | +0.174 (n=46) | -0.128 (n=47) | +0.083 (n=12) | +0.100 (n=20) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 94 | -0.644 (-1.26) | – | – | – |
| spread · A · D | 106 | -0.546 (-1.23) | – | – | – |
| spread · B · E | 94 | -1.073 (-2.24) | – | – | – |
| spread · B · D | 106 | -0.902 (-1.90) | – | – | – |
| ml · A · E | 94 | – | 0.1933 | 0.1758 | +0.0176 (2.48) |
| ml · A · D | 106 | – | 0.1953 | 0.1758 | +0.0196 (2.82) |
| ml · B · E | 94 | – | 0.1969 | 0.1758 | +0.0211 (2.82) |
| ml · B · D | 106 | – | 0.1957 | 0.1758 | +0.0199 (2.88) |
| total · T · E | 94 | +0.332 (0.64) | – | – | – |
| total · T · D | 106 | +0.109 (0.22) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._