# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **115** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 19 · +0%* | 42 · +0% | 60 · -11% | 79 · -20% | 88 · -18% | 15 · +15%* |
| H6 | 21 · -28%* | 42 · -14% | 67 · -6% | 88 · -9% | 99 · -6% | 16 · -16%* |
| D | 24 · -21%* | 43 · -3% | 65 · -0% | 88 · -5% | 103 · -2% | 12 · -5%* |
| L | 24 · -28%* | 44 · -13% | 65 · +0% | 85 · +1% | 97 · -2% | 18 · -47%* |
| D+conf | 2 · -7%* | 7 · -18%* | 12 · +28%* | 17 · +2%* | 18 · -4%* | 4 · -53%* |
| D+fade | 17 · -11%* | 22 · +4%* | 28 · +8%* | 34 · +6% | 34 · +6% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · -33%* | 36 · -20% | 57 · -10% | 77 · -16% | 89 · -8% | 14 · -32%* |
| H6 | 25 · -9%* | 43 · -3% | 60 · -18% | 91 · -14% | 104 · -12% | 11 · -47%* |
| D | 25 · -15%* | 46 · -4% | 61 · -3% | 91 · -8% | 106 · -6% | 9 · -36%* |
| L | 24 · -36%* | 48 · -21% | 61 · -19% | 79 · -16% | 97 · -17% | 18 · -48%* |
| D+conf | 2 · -100%* | 6 · -36%* | 9 · -15%* | 18 · -14%* | 21 · -18%* | – |
| D+fade | 10 · -4%* | 17 · +1%* | 24 · +11%* | 32 · +1% | 33 · -2% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · -44%* | 40 · -26% | 55 · -27% | 79 · -28% | 95 · -29% | 8 · +30%* |
| H6 | 27 · -74%* | 50 · -39% | 64 · -39% | 90 · -24% | 96 · -22% | 19 · -11%* |
| D | 25 · -72%* | 48 · -40% | 64 · -34% | 87 · -21% | 100 · -20% | 15 · -36%* |
| L | 29 · -70%* | 47 · -44% | 65 · -34% | 87 · -16% | 100 · -25% | 15 · -12%* |
| D+conf | 1 · -100%* | 9 · -31%* | 15 · -14%* | 19 · -18%* | 22 · -4%* | 3 · -56%* |
| D+fade | 20 · -65%* | 30 · -40% | 35 · -49% | 39 · -37% | 40 · -39% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 22 · -44%* | 39 · -41% | 52 · -36% | 77 · -33% | 86 · -30% | 17 · -19%* |
| H6 | 28 · -53%* | 42 · -33% | 68 · -30% | 95 · -37% | 106 · -31% | 9 · -18%* |
| D | 25 · -55%* | 44 · -44% | 67 · -31% | 97 · -30% | 107 · -28% | 8 · +6%* |
| L | 28 · -55%* | 44 · -53% | 62 · -46% | 88 · -37% | 101 · -37% | 14 · +36%* |
| D+conf | 1 · -100%* | 5 · -72%* | 13 · -44%* | 20 · -57%* | 22 · -45%* | – |
| D+fade | 18 · -75%* | 24 · -58%* | 33 · -45% | 41 · -40% | 41 · -40% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 11 · -13%* | 35 · -2% | 44 · -0% | 60 · -8% | 82 · -5% | 21 · +0%* |
| H6 | 11 · -13%* | 32 · -17% | 52 · -12% | 61 · -3% | 81 · -1% | 34 · -15% |
| D | 10 · -43%* | 29 · -14%* | 48 · -4% | 68 · -2% | 88 · -0% | 27 · +13%* |
| L | 8 · -52%* | 33 · -13% | 49 · -7% | 70 · -4% | 83 · +1% | 32 · -17% |
| D+conf | 2 · -4%* | 5 · -23%* | 13 · +3%* | 20 · +15%* | 24 · +12%* | 14 · +36%* |
| D+fade | 5 · -63%* | 13 · -27%* | 21 · -9%* | 27 · -8%* | 29 · -8%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 90. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.050 (n=60) | -0.075 (n=67) | -0.077 (n=65) | -0.015 (n=65) | -0.083 (n=12) | -0.143 (n=28) |
| spread · B | +0.193 (n=57) | -0.050 (n=60) | -0.016 (n=61) | +0.033 (n=61) | +0.000 (n=9) | -0.042 (n=24) |
| ml · A | -0.002 (n=55) | -0.000 (n=64) | +0.000 (n=64) | +0.000 (n=65) | +0.002 (n=15) | -0.003 (n=35) |
| ml · B | +0.001 (n=52) | +0.000 (n=68) | -0.001 (n=67) | +0.000 (n=62) | -0.002 (n=13) | -0.003 (n=33) |
| total · T | +1.500 (n=44) | +0.500 (n=52) | +0.167 (n=48) | -0.102 (n=49) | +0.000 (n=13) | +0.143 (n=21) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 103 | -0.801 (-1.66) | – | – | – |
| spread · A · D | 115 | -0.653 (-1.52) | – | – | – |
| spread · B · E | 103 | -1.063 (-2.39) | – | – | – |
| spread · B · D | 115 | -0.752 (-1.69) | – | – | – |
| ml · A · E | 103 | – | 0.1957 | 0.1798 | +0.0160 (2.35) |
| ml · A · D | 115 | – | 0.1973 | 0.1799 | +0.0174 (2.58) |
| ml · B · E | 103 | – | 0.1996 | 0.1798 | +0.0198 (2.66) |
| ml · B · D | 115 | – | 0.1971 | 0.1799 | +0.0172 (2.49) |
| total · T · E | 103 | +0.447 (0.94) | – | – | – |
| total · T · D | 115 | +0.151 (0.33) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._