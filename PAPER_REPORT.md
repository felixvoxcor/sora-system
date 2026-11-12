# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **95** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 17 · +12%* | 34 · -4% | 49 · -14% | 66 · -25% | 73 · -19% | 13 · +18%* |
| H6 | 18 · -37%* | 35 · -19% | 52 · -8% | 70 · -10% | 81 · -6% | 14 · -32%* |
| D | 21 · -27%* | 34 · +1% | 51 · +1% | 70 · -2% | 85 · +1% | 10 · -24%* |
| L | 22 · -30%* | 36 · -9% | 51 · +2% | 69 · +5% | 81 · +1% | 14 · -73%* |
| D+conf | 2 · -7%* | 5 · +14%* | 8 · +45%* | 13 · +4%* | 14 · -3%* | 3 · -100%* |
| D+fade | 15 · -24%* | 19 · +0%* | 23 · +7%* | 28 · +8%* | 28 · +8%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 17 · -55%* | 30 · -30% | 48 · -13% | 64 · -16% | 74 · -5% | 12 · -52%* |
| H6 | 20 · -33%* | 33 · -13% | 46 · -21% | 74 · -15% | 84 · -9% | 11 · -47%* |
| D | 21 · -36%* | 36 · -15% | 48 · -4% | 74 · -9% | 86 · -4% | 9 · -36%* |
| L | 21 · -55%* | 37 · -28% | 48 · -24% | 63 · -21% | 78 · -19% | 17 · -56%* |
| D+conf | 2 · -100%* | 5 · -61%* | 7 · -17%* | 16 · -15%* | 18 · -14%* | – |
| D+fade | 10 · -4%* | 15 · +2%* | 21 · +18%* | 26 · +10%* | 27 · +6%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · -38%* | 34 · -36% | 44 · -26% | 65 · -25% | 78 · -28% | 8 · +30%* |
| H6 | 22 · -83%* | 41 · -42% | 51 · -39% | 73 · -23% | 77 · -20% | 18 · -6%* |
| D | 20 · -82%* | 39 · -43% | 50 · -31% | 69 · -17% | 80 · -15% | 15 · -36%* |
| L | 25 · -65%* | 38 · -39% | 52 · -33% | 69 · -11% | 80 · -20% | 15 · -12%* |
| D+conf | – | 7 · -11%* | 11 · +4%* | 14 · +2%* | 17 · +16%* | 3 · -56%* |
| D+fade | 17 · -78%* | 25 · -42%* | 27 · -46%* | 31 · -31% | 32 · -33% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · -59%* | 31 · -56% | 43 · -45% | 63 · -35% | 72 · -31% | 14 · -13%* |
| H6 | 22 · -71%* | 33 · -50% | 54 · -35% | 75 · -37% | 86 · -29% | 9 · -18%* |
| D | 21 · -62%* | 36 · -58% | 54 · -37% | 78 · -31% | 88 · -28% | 7 · +21%* |
| L | 24 · -60%* | 36 · -60% | 50 · -57% | 68 · -39% | 81 · -38% | 14 · +36%* |
| D+conf | 1 · -100%* | 4 · -100%* | 11 · -46%* | 16 · -55%* | 18 · -40%* | – |
| D+fade | 15 · -70%* | 20 · -66%* | 26 · -52%* | 32 · -42% | 32 · -42% | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 10 · -4%* | 30 · +2% | 36 · +1% | 51 · -10% | 70 · -8% | 16 · +8%* |
| H6 | 9 · -15%* | 30 · -18% | 46 · -9% | 53 · -3% | 69 · -3% | 26 · -41%* |
| D | 8 · -53%* | 27 · -15%* | 43 · -2% | 59 · -3% | 75 · -3% | 20 · -5%* |
| L | 6 · -69%* | 30 · -17% | 45 · -7% | 62 · -8% | 69 · -3% | 26 · -20%* |
| D+conf | 2 · -4%* | 5 · -23%* | 10 · +15%* | 15 · +15%* | 19 · +11%* | 9 · +27%* |
| D+fade | 4 · -53%* | 12 · -21%* | 20 · -5%* | 26 · -5%* | 28 · -5%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 83. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | -0.082 (n=49) | -0.212 (n=52) | -0.157 (n=51) | -0.039 (n=51) | -0.125 (n=8) | -0.217 (n=23) |
| spread · B | +0.146 (n=48) | -0.174 (n=46) | -0.062 (n=48) | +0.062 (n=48) | +0.143 (n=7) | -0.095 (n=21) |
| ml · A | -0.003 (n=44) | -0.001 (n=51) | -0.000 (n=50) | +0.000 (n=52) | +0.002 (n=11) | -0.003 (n=27) |
| ml · B | +0.000 (n=43) | -0.002 (n=54) | -0.001 (n=54) | +0.001 (n=50) | -0.001 (n=11) | -0.002 (n=26) |
| total · T | +1.500 (n=36) | +0.500 (n=46) | +0.116 (n=43) | -0.133 (n=45) | +0.000 (n=10) | +0.100 (n=20) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 86 | -0.831 (-1.65) | – | – | – |
| spread · A · D | 95 | -0.618 (-1.35) | – | – | – |
| spread · B · E | 86 | -1.175 (-2.47) | – | – | – |
| spread · B · D | 95 | -0.880 (-1.82) | – | – | – |
| ml · A · E | 86 | – | 0.1978 | 0.1802 | +0.0176 (2.31) |
| ml · A · D | 95 | – | 0.1996 | 0.1823 | +0.0173 (2.28) |
| ml · B · E | 86 | – | 0.2034 | 0.1802 | +0.0232 (2.90) |
| ml · B · D | 95 | – | 0.2022 | 0.1823 | +0.0199 (2.64) |
| total · T · E | 86 | +0.318 (0.63) | – | – | – |
| total · T · D | 95 | -0.010 (-0.02) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._