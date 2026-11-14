# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **112** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · +6%* | 40 · +0% | 57 · -9% | 76 · -20% | 85 · -17% | 15 · +15%* |
| H6 | 21 · -28%* | 40 · -15% | 64 · -5% | 85 · -8% | 96 · -5% | 16 · -16%* |
| D | 24 · -21%* | 41 · -3% | 62 · +1% | 85 · -4% | 100 · -1% | 12 · -5%* |
| L | 24 · -28%* | 43 · -11% | 62 · +2% | 82 · +2% | 94 · -1% | 18 · -47%* |
| D+conf | 2 · -7%* | 6 · -5%* | 11 · +40%* | 16 · +8%* | 17 · +2%* | 4 · -53%* |
| D+fade | 17 · -11%* | 22 · +4%* | 28 · +8%* | 34 · +6% | 34 · +6% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 22 · -39%* | 35 · -23% | 56 · -11% | 74 · -15% | 86 · -7% | 14 · -32%* |
| H6 | 24 · -13%* | 42 · -5% | 58 · -18% | 89 · -14% | 101 · -11% | 11 · -47%* |
| D | 24 · -20%* | 45 · -7% | 60 · -4% | 90 · -9% | 103 · -5% | 9 · -36%* |
| L | 23 · -42%* | 47 · -23% | 60 · -21% | 78 · -17% | 95 · -18% | 17 · -56%* |
| D+conf | 2 · -100%* | 6 · -36%* | 9 · -15%* | 18 · -14%* | 20 · -14%* | – |
| D+fade | 10 · -4%* | 17 · +1%* | 24 · +11%* | 32 · +1% | 33 · -2% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · -38%* | 37 · -29% | 52 · -29% | 76 · -30% | 92 · -31% | 8 · +30%* |
| H6 | 26 · -73%* | 47 · -42% | 61 · -41% | 87 · -25% | 93 · -23% | 19 · -11%* |
| D | 24 · -71%* | 45 · -43% | 61 · -36% | 84 · -22% | 97 · -21% | 15 · -36%* |
| L | 28 · -69%* | 45 · -42% | 62 · -36% | 84 · -17% | 97 · -25% | 15 · -12%* |
| D+conf | – | 7 · -11%* | 13 · -1%* | 17 · -8%* | 20 · +6%* | 3 · -56%* |
| D+fade | 20 · -65%* | 30 · -40% | 35 · -49% | 39 · -37% | 40 · -39% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · -57%* | 37 · -46% | 49 · -39% | 74 · -35% | 83 · -32% | 17 · -19%* |
| H6 | 27 · -63%* | 41 · -40% | 66 · -33% | 92 · -38% | 103 · -32% | 9 · -18%* |
| D | 24 · -67%* | 43 · -50% | 66 · -35% | 94 · -31% | 104 · -29% | 8 · +6%* |
| L | 27 · -65%* | 43 · -59% | 61 · -50% | 85 · -39% | 98 · -38% | 14 · +36%* |
| D+conf | 1 · -100%* | 5 · -72%* | 13 · -44%* | 18 · -52%* | 20 · -39%* | – |
| D+fade | 18 · -75%* | 24 · -58%* | 33 · -45% | 41 · -40% | 41 · -40% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 10 · -4%* | 34 · +1% | 43 · +2% | 59 · -6% | 79 · -6% | 21 · +0%* |
| H6 | 10 · -5%* | 31 · -14% | 51 · -11% | 60 · -2% | 80 · -0% | 32 · -22% |
| D | 9 · -36%* | 28 · -11%* | 47 · -2% | 67 · -0% | 86 · -0% | 26 · +10%* |
| L | 7 · -45%* | 32 · -11% | 48 · -5% | 69 · -3% | 81 · +1% | 31 · -20% |
| D+conf | 2 · -4%* | 5 · -23%* | 13 · +3%* | 20 · +15%* | 24 · +12%* | 13 · +32%* |
| D+fade | 4 · -53%* | 12 · -21%* | 20 · -5%* | 26 · -5%* | 28 · -5%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 90. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.018 (n=57) | -0.094 (n=64) | -0.097 (n=62) | -0.016 (n=62) | -0.091 (n=11) | -0.143 (n=28) |
| spread · B | +0.179 (n=56) | -0.069 (n=58) | -0.033 (n=60) | +0.033 (n=60) | +0.000 (n=9) | -0.042 (n=24) |
| ml · A | -0.004 (n=52) | -0.001 (n=61) | -0.000 (n=61) | +0.000 (n=62) | +0.003 (n=13) | -0.003 (n=35) |
| ml · B | +0.000 (n=49) | -0.000 (n=66) | -0.002 (n=66) | +0.000 (n=61) | -0.002 (n=13) | -0.003 (n=33) |
| total · T | +1.558 (n=43) | +0.510 (n=51) | +0.149 (n=47) | -0.125 (n=48) | +0.000 (n=13) | +0.100 (n=20) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 100 | -0.701 (-1.42) | – | – | – |
| spread · A · D | 112 | -0.570 (-1.30) | – | – | – |
| spread · B · E | 100 | -1.068 (-2.36) | – | – | – |
| spread · B · D | 112 | -0.757 (-1.68) | – | – | – |
| ml · A · E | 100 | – | 0.1964 | 0.1796 | +0.0167 (2.44) |
| ml · A · D | 112 | – | 0.1979 | 0.1796 | +0.0183 (2.69) |
| ml · B · E | 100 | – | 0.2015 | 0.1796 | +0.0219 (2.99) |
| ml · B · D | 112 | – | 0.1988 | 0.1796 | +0.0193 (2.84) |
| total · T · E | 100 | +0.534 (1.07) | – | – | – |
| total · T · D | 112 | +0.223 (0.46) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._