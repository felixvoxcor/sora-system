# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **103** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 17 · +12%* | 36 · -4% | 51 · -14% | 69 · -25% | 77 · -21% | 14 · +9%* |
| H6 | 20 · -33%* | 38 · -15% | 58 · -8% | 78 · -12% | 89 · -8% | 14 · -32%* |
| D | 23 · -25%* | 38 · +0% | 56 · -1% | 78 · -7% | 93 · -4% | 10 · -24%* |
| L | 24 · -28%* | 40 · -9% | 56 · -1% | 76 · +0% | 88 · -2% | 15 · -75%* |
| D+conf | 2 · -7%* | 5 · +14%* | 8 · +45%* | 13 · +4%* | 14 · -3%* | 3 · -100%* |
| D+fade | 16 · -17%* | 20 · +5%* | 25 · +7%* | 31 · +4% | 31 · +4% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 19 · -40%* | 32 · -22% | 51 · -10% | 68 · -13% | 79 · -4% | 12 · -52%* |
| H6 | 23 · -18%* | 38 · -5% | 52 · -16% | 81 · -13% | 92 · -9% | 11 · -47%* |
| D | 23 · -25%* | 42 · -9% | 55 · -3% | 82 · -9% | 94 · -4% | 9 · -36%* |
| L | 23 · -42%* | 43 · -20% | 54 · -19% | 70 · -18% | 86 · -18% | 17 · -56%* |
| D+conf | 2 · -100%* | 6 · -36%* | 8 · -4%* | 17 · -9%* | 19 · -9%* | – |
| D+fade | 10 · -4%* | 15 · +2%* | 21 · +18%* | 27 · +6%* | 28 · +2%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · -38%* | 35 · -38% | 46 · -30% | 69 · -30% | 83 · -30% | 8 · +30%* |
| H6 | 25 · -85%* | 44 · -46% | 56 · -44% | 79 · -29% | 85 · -26% | 18 · -6%* |
| D | 23 · -84%* | 42 · -47% | 55 · -38% | 76 · -25% | 88 · -23% | 15 · -36%* |
| L | 28 · -69%* | 42 · -45% | 56 · -37% | 76 · -19% | 88 · -27% | 15 · -12%* |
| D+conf | – | 7 · -11%* | 11 · +4%* | 14 · +2%* | 17 · +16%* | 3 · -56%* |
| D+fade | 19 · -81%* | 27 · -46%* | 31 · -53% | 35 · -39% | 36 · -41% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 19 · -53%* | 33 · -54% | 45 · -44% | 68 · -37% | 77 · -34% | 14 · -13%* |
| H6 | 25 · -66%* | 38 · -48% | 60 · -36% | 83 · -39% | 94 · -32% | 9 · -18%* |
| D | 23 · -65%* | 41 · -55% | 61 · -39% | 86 · -34% | 96 · -31% | 7 · +21%* |
| L | 26 · -63%* | 41 · -57% | 56 · -56% | 76 · -41% | 89 · -40% | 14 · +36%* |
| D+conf | 1 · -100%* | 5 · -72%* | 12 · -39%* | 17 · -49%* | 19 · -36%* | – |
| D+fade | 17 · -73%* | 22 · -69%* | 29 · -57%* | 36 · -48% | 36 · -48% | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 10 · -4%* | 31 · -2% | 38 · -5% | 54 · -12% | 74 · -10% | 17 · +2%* |
| H6 | 10 · -5%* | 31 · -14% | 49 · -11% | 56 · -5% | 74 · -5% | 29 · -34%* |
| D | 9 · -36%* | 28 · -11%* | 45 · -2% | 63 · -3% | 80 · -5% | 23 · -1%* |
| L | 7 · -45%* | 31 · -14% | 46 · -5% | 65 · -6% | 74 · -4% | 29 · -21%* |
| D+conf | 2 · -4%* | 5 · -23%* | 11 · +5%* | 16 · +8%* | 20 · +6%* | 11 · +21%* |
| D+fade | 4 · -53%* | 12 · -21%* | 20 · -5%* | 26 · -5%* | 28 · -5%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 86. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | -0.059 (n=51) | -0.121 (n=58) | -0.143 (n=56) | -0.036 (n=56) | -0.125 (n=8) | -0.240 (n=25) |
| spread · B | +0.176 (n=51) | -0.058 (n=52) | -0.036 (n=55) | +0.037 (n=54) | +0.125 (n=8) | -0.095 (n=21) |
| ml · A | -0.005 (n=46) | -0.001 (n=56) | -0.000 (n=55) | -0.000 (n=56) | +0.002 (n=11) | -0.003 (n=31) |
| ml · B | +0.000 (n=45) | -0.000 (n=60) | -0.002 (n=61) | +0.000 (n=56) | -0.002 (n=12) | -0.003 (n=29) |
| total · T | +1.553 (n=38) | +0.551 (n=49) | +0.178 (n=45) | -0.130 (n=46) | +0.091 (n=11) | +0.100 (n=20) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 91 | -0.806 (-1.58) | – | – | – |
| spread · A · D | 103 | -0.618 (-1.39) | – | – | – |
| spread · B · E | 91 | -1.038 (-2.19) | – | – | – |
| spread · B · D | 103 | -0.826 (-1.76) | – | – | – |
| ml · A · E | 91 | – | 0.1964 | 0.1783 | +0.0181 (2.49) |
| ml · A · D | 103 | – | 0.1980 | 0.1782 | +0.0198 (2.79) |
| ml · B · E | 91 | – | 0.2006 | 0.1783 | +0.0223 (2.91) |
| ml · B · D | 103 | – | 0.1988 | 0.1782 | +0.0205 (2.89) |
| total · T · E | 91 | +0.325 (0.66) | – | – | – |
| total · T · D | 103 | +0.129 (0.27) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._