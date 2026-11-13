# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **105** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 17 · +12%* | 37 · -2% | 52 · -12% | 71 · -22% | 79 · -18% | 14 · +9%* |
| H6 | 20 · -33%* | 38 · -15% | 60 · -5% | 80 · -10% | 91 · -6% | 14 · -32%* |
| D | 23 · -25%* | 38 · +0% | 58 · +2% | 80 · -5% | 95 · -2% | 10 · -24%* |
| L | 24 · -28%* | 40 · -9% | 58 · +2% | 78 · +3% | 90 · -0% | 15 · -75%* |
| D+conf | 2 · -7%* | 5 · +14%* | 9 · +50%* | 14 · +10%* | 15 · +3%* | 3 · -100%* |
| D+fade | 16 · -17%* | 20 · +5%* | 26 · +10%* | 32 · +7% | 32 · +7% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 19 · -40%* | 32 · -22% | 51 · -10% | 68 · -13% | 79 · -4% | 14 · -32%* |
| H6 | 23 · -18%* | 38 · -5% | 52 · -16% | 82 · -12% | 94 · -9% | 11 · -47%* |
| D | 23 · -25%* | 42 · -9% | 55 · -3% | 83 · -8% | 96 · -5% | 9 · -36%* |
| L | 23 · -42%* | 43 · -20% | 54 · -19% | 71 · -17% | 88 · -18% | 17 · -56%* |
| D+conf | 2 · -100%* | 6 · -36%* | 8 · -4%* | 17 · -9%* | 19 · -9%* | – |
| D+fade | 10 · -4%* | 15 · +2%* | 21 · +18%* | 28 · +9%* | 29 · +5%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · -38%* | 36 · -36% | 47 · -28% | 71 · -29% | 85 · -30% | 8 · +30%* |
| H6 | 25 · -85%* | 45 · -47% | 58 · -44% | 81 · -29% | 87 · -26% | 18 · -6%* |
| D | 23 · -84%* | 42 · -47% | 57 · -37% | 78 · -25% | 90 · -23% | 15 · -36%* |
| L | 28 · -69%* | 42 · -45% | 58 · -37% | 78 · -19% | 90 · -27% | 15 · -12%* |
| D+conf | – | 7 · -11%* | 12 · +7%* | 15 · +4%* | 18 · +18%* | 3 · -56%* |
| D+fade | 19 · -81%* | 27 · -46%* | 32 · -54% | 36 · -41% | 37 · -42% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 19 · -53%* | 33 · -54% | 45 · -44% | 68 · -37% | 77 · -34% | 16 · -14%* |
| H6 | 25 · -66%* | 38 · -48% | 61 · -37% | 85 · -40% | 96 · -33% | 9 · -18%* |
| D | 23 · -65%* | 41 · -55% | 61 · -39% | 88 · -35% | 98 · -32% | 7 · +21%* |
| L | 26 · -63%* | 41 · -57% | 56 · -56% | 78 · -43% | 91 · -41% | 14 · +36%* |
| D+conf | 1 · -100%* | 5 · -72%* | 12 · -39%* | 17 · -49%* | 19 · -36%* | – |
| D+fade | 17 · -73%* | 22 · -69%* | 29 · -57%* | 37 · -50% | 37 · -50% | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 10 · -4%* | 31 · -2% | 38 · -5% | 54 · -12% | 74 · -10% | 19 · +1%* |
| H6 | 10 · -5%* | 31 · -14% | 49 · -11% | 56 · -5% | 76 · -2% | 29 · -34%* |
| D | 9 · -36%* | 28 · -11%* | 45 · -2% | 63 · -3% | 81 · -3% | 24 · +3%* |
| L | 7 · -45%* | 31 · -14% | 46 · -5% | 65 · -6% | 75 · -3% | 30 · -24% |
| D+conf | 2 · -4%* | 5 · -23%* | 11 · +5%* | 16 · +8%* | 20 · +6%* | 12 · +27%* |
| D+fade | 4 · -53%* | 12 · -21%* | 20 · -5%* | 26 · -5%* | 28 · -5%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 86. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | -0.038 (n=52) | -0.100 (n=60) | -0.121 (n=58) | -0.017 (n=58) | -0.111 (n=9) | -0.192 (n=26) |
| spread · B | +0.176 (n=51) | -0.058 (n=52) | -0.036 (n=55) | +0.037 (n=54) | +0.125 (n=8) | -0.095 (n=21) |
| ml · A | -0.004 (n=47) | -0.001 (n=58) | -0.000 (n=57) | -0.000 (n=58) | +0.002 (n=12) | -0.003 (n=32) |
| ml · B | +0.000 (n=45) | -0.000 (n=61) | -0.002 (n=61) | +0.000 (n=56) | -0.002 (n=12) | -0.003 (n=29) |
| total · T | +1.553 (n=38) | +0.551 (n=49) | +0.178 (n=45) | -0.130 (n=46) | +0.091 (n=11) | +0.100 (n=20) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 93 | -0.681 (-1.31) | – | – | – |
| spread · A · D | 105 | -0.564 (-1.25) | – | – | – |
| spread · B · E | 93 | -1.069 (-2.21) | – | – | – |
| spread · B · D | 105 | -0.900 (-1.89) | – | – | – |
| ml · A · E | 93 | – | 0.1938 | 0.1766 | +0.0172 (2.40) |
| ml · A · D | 105 | – | 0.1958 | 0.1764 | +0.0194 (2.77) |
| ml · B · E | 93 | – | 0.1984 | 0.1766 | +0.0218 (2.90) |
| ml · B · D | 105 | – | 0.1969 | 0.1764 | +0.0205 (2.94) |
| total · T · E | 93 | +0.407 (0.78) | – | – | – |
| total · T · D | 105 | +0.160 (0.32) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._