# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **111** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · +6%* | 40 · +0% | 56 · -11% | 75 · -21% | 84 · -18% | 15 · +15%* |
| H6 | 21 · -28%* | 40 · -15% | 64 · -5% | 85 · -8% | 96 · -5% | 15 · -24%* |
| D | 24 · -21%* | 41 · -3% | 62 · +1% | 85 · -4% | 100 · -1% | 11 · -13%* |
| L | 24 · -28%* | 43 · -11% | 62 · +2% | 82 · +2% | 94 · -1% | 17 · -55%* |
| D+conf | 2 · -7%* | 6 · -5%* | 11 · +40%* | 16 · +8%* | 17 · +2%* | 3 · -100%* |
| D+fade | 17 · -11%* | 22 · +4%* | 28 · +8%* | 34 · +6% | 34 · +6% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 22 · -39%* | 35 · -23% | 56 · -11% | 73 · -14% | 85 · -6% | 14 · -32%* |
| H6 | 24 · -13%* | 41 · -3% | 57 · -17% | 88 · -13% | 100 · -11% | 11 · -47%* |
| D | 24 · -20%* | 44 · -4% | 59 · -3% | 89 · -8% | 102 · -5% | 9 · -36%* |
| L | 23 · -42%* | 46 · -21% | 59 · -19% | 77 · -16% | 94 · -17% | 17 · -56%* |
| D+conf | 2 · -100%* | 6 · -36%* | 9 · -15%* | 18 · -14%* | 20 · -14%* | – |
| D+fade | 10 · -4%* | 16 · +7%* | 23 · +16%* | 31 · +4% | 32 · +1% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · -38%* | 37 · -29% | 51 · -27% | 75 · -29% | 91 · -30% | 8 · +30%* |
| H6 | 26 · -73%* | 47 · -42% | 61 · -41% | 86 · -25% | 92 · -22% | 19 · -11%* |
| D | 24 · -71%* | 45 · -43% | 61 · -36% | 83 · -21% | 96 · -20% | 15 · -36%* |
| L | 28 · -69%* | 45 · -42% | 62 · -36% | 83 · -16% | 96 · -25% | 15 · -12%* |
| D+conf | – | 7 · -11%* | 13 · -1%* | 16 · -2%* | 19 · +11%* | 3 · -56%* |
| D+fade | 20 · -65%* | 30 · -40% | 35 · -49% | 39 · -37% | 40 · -39% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · -57%* | 37 · -46% | 49 · -39% | 73 · -35% | 82 · -32% | 17 · -19%* |
| H6 | 27 · -63%* | 41 · -40% | 65 · -34% | 91 · -39% | 102 · -32% | 9 · -18%* |
| D | 24 · -67%* | 43 · -50% | 65 · -36% | 93 · -32% | 103 · -29% | 8 · +6%* |
| L | 27 · -65%* | 43 · -59% | 60 · -51% | 84 · -39% | 97 · -39% | 14 · +36%* |
| D+conf | 1 · -100%* | 5 · -72%* | 13 · -44%* | 18 · -52%* | 20 · -39%* | – |
| D+fade | 18 · -75%* | 24 · -58%* | 32 · -47% | 40 · -42% | 40 · -42% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 10 · -4%* | 33 · -2% | 42 · -0% | 58 · -8% | 78 · -7% | 21 · +0%* |
| H6 | 10 · -5%* | 31 · -14% | 51 · -11% | 59 · -3% | 79 · -1% | 32 · -22% |
| D | 9 · -36%* | 28 · -11%* | 47 · -2% | 66 · -2% | 85 · -1% | 26 · +10%* |
| L | 7 · -45%* | 32 · -11% | 48 · -5% | 69 · -3% | 80 · +0% | 31 · -20% |
| D+conf | 2 · -4%* | 5 · -23%* | 13 · +3%* | 19 · +11%* | 23 · +9%* | 13 · +32%* |
| D+fade | 4 · -53%* | 12 · -21%* | 20 · -5%* | 26 · -5%* | 28 · -5%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 90. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | -0.018 (n=56) | -0.094 (n=64) | -0.097 (n=62) | -0.016 (n=62) | -0.091 (n=11) | -0.143 (n=28) |
| spread · B | +0.179 (n=56) | -0.070 (n=57) | -0.034 (n=59) | +0.034 (n=59) | +0.000 (n=9) | -0.043 (n=23) |
| ml · A | -0.004 (n=51) | -0.001 (n=61) | -0.000 (n=61) | +0.000 (n=62) | +0.003 (n=13) | -0.003 (n=35) |
| ml · B | +0.000 (n=49) | -0.000 (n=65) | -0.002 (n=65) | +0.000 (n=60) | -0.002 (n=13) | -0.003 (n=32) |
| total · T | +1.500 (n=42) | +0.510 (n=51) | +0.149 (n=47) | -0.125 (n=48) | +0.000 (n=13) | +0.100 (n=20) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 99 | -0.751 (-1.51) | – | – | – |
| spread · A · D | 111 | -0.583 (-1.33) | – | – | – |
| spread · B · E | 99 | -1.058 (-2.33) | – | – | – |
| spread · B · D | 111 | -0.737 (-1.63) | – | – | – |
| ml · A · E | 99 | – | 0.1982 | 0.1813 | +0.0168 (2.43) |
| ml · A · D | 111 | – | 0.1995 | 0.1811 | +0.0185 (2.69) |
| ml · B · E | 99 | – | 0.2035 | 0.1813 | +0.0221 (2.99) |
| ml · B · D | 111 | – | 0.2006 | 0.1811 | +0.0195 (2.85) |
| total · T · E | 99 | +0.424 (0.84) | – | – | – |
| total · T · D | 111 | +0.178 (0.37) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._