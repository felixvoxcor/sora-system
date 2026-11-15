# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **121** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 19 · +0%* | 42 · +0% | 61 · -9% | 80 · -19% | 89 · -16% | 15 · +15%* |
| H6 | 23 · -17%* | 45 · -7% | 70 · -2% | 93 · -4% | 104 · -1% | 17 · -10%* |
| D | 27 · -8%* | 46 · +3% | 68 · +4% | 93 · +0% | 108 · +2% | 13 · +2%* |
| L | 26 · -19%* | 46 · -8% | 67 · +3% | 90 · +6% | 102 · +3% | 19 · -40%* |
| D+conf | 2 · -7%* | 7 · -18%* | 12 · +28%* | 18 · +7%* | 19 · +1%* | 4 · -53%* |
| D+fade | 17 · -11%* | 22 · +4%* | 28 · +8%* | 34 · +6% | 34 · +6% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · -33%* | 36 · -20% | 57 · -10% | 78 · -14% | 90 · -7% | 14 · -32%* |
| H6 | 26 · -5%* | 45 · +1% | 64 · -11% | 96 · -9% | 110 · -8% | 11 · -47%* |
| D | 26 · -11%* | 47 · -2% | 64 · +1% | 95 · -4% | 112 · -3% | 9 · -36%* |
| L | 24 · -36%* | 49 · -18% | 63 · -18% | 83 · -13% | 102 · -14% | 19 · -40%* |
| D+conf | 2 · -100%* | 6 · -36%* | 10 · -4%* | 19 · -9%* | 22 · -13%* | – |
| D+fade | 10 · -4%* | 17 · +1%* | 24 · +11%* | 32 · +1% | 33 · -2% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · -44%* | 40 · -26% | 55 · -27% | 80 · -26% | 96 · -28% | 8 · +30%* |
| H6 | 29 · -68%* | 53 · -35% | 68 · -33% | 95 · -14% | 102 · -13% | 19 · -11%* |
| D | 28 · -58%* | 51 · -34% | 68 · -19% | 91 · -10% | 105 · -10% | 16 · -40%* |
| L | 31 · -59% | 49 · -39% | 68 · -20% | 92 · -7% | 106 · -14% | 15 · -12%* |
| D+conf | 1 · -100%* | 9 · -31%* | 15 · -14%* | 19 · -18%* | 23 · +3%* | 3 · -56%* |
| D+fade | 20 · -65%* | 30 · -40% | 35 · -49% | 39 · -37% | 40 · -39% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 22 · -44%* | 39 · -41% | 52 · -36% | 77 · -33% | 86 · -30% | 18 · -24%* |
| H6 | 29 · -47%* | 45 · -23% | 72 · -15% | 100 · -26% | 112 · -21% | 9 · -18%* |
| D | 26 · -45%* | 45 · -38% | 69 · -17% | 103 · -18% | 113 · -17% | 8 · +6%* |
| L | 29 · -44%* | 45 · -46% | 64 · -42% | 92 · -26% | 106 · -25% | 15 · +37%* |
| D+conf | 1 · -100%* | 5 · -72%* | 13 · -44%* | 20 · -57%* | 22 · -45%* | – |
| D+fade | 18 · -75%* | 24 · -58%* | 33 · -45% | 41 · -40% | 41 · -40% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 12 · -4%* | 36 · +1% | 45 · +2% | 61 · -6% | 83 · -4% | 21 · +0%* |
| H6 | 11 · -13%* | 33 · -14% | 54 · -12% | 63 · -3% | 85 · -1% | 36 · -15% |
| D | 10 · -43%* | 31 · -7% | 50 · -0% | 71 · -0% | 92 · -0% | 29 · +12%* |
| L | 8 · -52%* | 36 · -5% | 52 · -1% | 75 · -1% | 88 · +4% | 33 · -19% |
| D+conf | 2 · -4%* | 6 · -5%* | 14 · +9%* | 21 · +19%* | 25 · +15%* | 14 · +36%* |
| D+fade | 5 · -63%* | 13 · -27%* | 21 · -9%* | 27 · -8%* | 29 · -8%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 92. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.066 (n=61) | -0.143 (n=70) | -0.074 (n=68) | -0.015 (n=67) | -0.083 (n=12) | -0.143 (n=28) |
| spread · B | +0.193 (n=57) | -0.125 (n=64) | -0.062 (n=64) | +0.032 (n=63) | +0.000 (n=10) | -0.042 (n=24) |
| ml · A | -0.002 (n=55) | -0.002 (n=68) | +0.001 (n=68) | +0.000 (n=68) | +0.002 (n=15) | -0.003 (n=35) |
| ml · B | +0.001 (n=52) | -0.001 (n=72) | -0.002 (n=69) | +0.000 (n=64) | -0.002 (n=13) | -0.003 (n=33) |
| total · T | +1.511 (n=45) | +0.500 (n=54) | +0.160 (n=50) | -0.077 (n=52) | +0.000 (n=14) | +0.143 (n=21) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 104 | -0.756 (-1.56) | – | – | – |
| spread · A · D | 121 | -0.337 (-0.82) | – | – | – |
| spread · B · E | 104 | -1.059 (-2.36) | – | – | – |
| spread · B · D | 121 | -0.556 (-1.25) | – | – | – |
| ml · A · E | 104 | – | 0.1971 | 0.1818 | +0.0153 (2.27) |
| ml · A · D | 121 | – | 0.1999 | 0.1868 | +0.0131 (1.82) |
| ml · B · E | 104 | – | 0.2014 | 0.1818 | +0.0196 (2.66) |
| ml · B · D | 121 | – | 0.2000 | 0.1868 | +0.0132 (1.92) |
| total · T · E | 104 | +0.576 (1.23) | – | – | – |
| total · T · D | 121 | +0.249 (0.55) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._