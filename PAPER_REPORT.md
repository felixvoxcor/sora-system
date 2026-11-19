# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **149** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 20 · +5%* | 43 · +2% | 65 · -12% | 97 · -25% | 109 · -21% | 19 · +1%* |
| H6 | 24 · -13%* | 49 · -3% | 80 · -5% | 113 · -7% | 126 · -5% | 23 · -9%* |
| D | 30 · -11% | 52 · +2% | 79 · -1% | 113 · -6% | 133 · -4% | 16 · +19%* |
| L | 28 · -25%* | 52 · -11% | 75 · -3% | 106 · +1% | 125 · -2% | 24 · -28%* |
| D+conf | 2 · -7%* | 8 · -4%* | 13 · +33%* | 19 · +11%* | 23 · +0%* | 5 · -23%* |
| D+fade | 18 · -16%* | 25 · -1%* | 33 · +3% | 43 · -3% | 43 · -3% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 27 · -43%* | 45 · -32% | 69 · -20% | 98 · -20% | 113 · -11% | 15 · -36%* |
| H6 | 30 · -6% | 53 · -7% | 76 · -15% | 114 · -15% | 132 · -12% | 17 · -43%* |
| D | 32 · -16% | 54 · -8% | 79 · -8% | 116 · -9% | 137 · -9% | 12 · -36%* |
| L | 28 · -32%* | 54 · -19% | 76 · -17% | 100 · -12% | 124 · -17% | 25 · -39%* |
| D+conf | 3 · -100%* | 7 · -45%* | 13 · -12%* | 26 · -11%* | 32 · -16% | 1 · -100%* |
| D+fade | 13 · -12%* | 20 · -5%* | 30 · -5% | 38 · -10% | 39 · -12% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · -44%* | 42 · -20% | 62 · -26% | 96 · -24% | 116 · -26% | 12 · +55%* |
| H6 | 31 · -57% | 58 · -26% | 78 · -26% | 116 · -14% | 126 · -13% | 23 · -12%* |
| D | 30 · -47% | 57 · -22% | 80 · -16% | 112 · -13% | 131 · -12% | 18 · -46%* |
| L | 35 · -52% | 56 · -31% | 79 · -13% | 111 · -7% | 129 · -12% | 20 · -26%* |
| D+conf | 1 · -100%* | 9 · -31%* | 15 · -14%* | 24 · -28%* | 28 · -10%* | 4 · -67%* |
| D+fade | 21 · -46%* | 34 · -22% | 42 · -37% | 49 · -28% | 50 · -30% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 25 · -45%* | 46 · -38% | 65 · -35% | 97 · -30% | 107 · -28% | 21 · -35%* |
| H6 | 32 · -52% | 56 · -22% | 86 · -18% | 117 · -27% | 133 · -21% | 16 · -31%* |
| D | 30 · -53% | 54 · -37% | 83 · -19% | 120 · -20% | 132 · -17% | 17 · -42%* |
| L | 33 · -32% | 51 · -37% | 77 · -36% | 108 · -23% | 130 · -25% | 19 · +34%* |
| D+conf | 1 · -100%* | 5 · -72%* | 15 · -42%* | 24 · -51%* | 27 · -32%* | 7 · -81%* |
| D+fade | 22 · -79%* | 30 · -52% | 40 · -44% | 49 · -41% | 49 · -41% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 15 · +2%* | 42 · +5% | 54 · +6% | 74 · -2% | 103 · +2% | 25 · -16%* |
| H6 | 13 · -27%* | 40 · -10% | 64 · -5% | 78 · +3% | 108 · +2% | 41 · -16% |
| D | 12 · -52%* | 39 · -2% | 62 · +5% | 87 · +1% | 114 · +2% | 35 · +4% |
| L | 11 · -48%* | 43 · -3% | 65 · +5% | 91 · +3% | 111 · +7% | 38 · -20% |
| D+conf | 2 · -4%* | 9 · +27%* | 18 · +27%* | 27 · +27%* | 34 · +30% | 15 · +27%* |
| D+fade | 7 · -73%* | 16 · -40%* | 25 · -16%* | 32 · -17% | 35 · -13% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 107. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.154 (n=65) | -0.025 (n=80) | +0.038 (n=79) | -0.040 (n=75) | -0.077 (n=13) | -0.091 (n=33) |
| spread · B | +0.203 (n=69) | -0.105 (n=76) | -0.025 (n=79) | +0.013 (n=76) | -0.231 (n=13) | -0.067 (n=30) |
| ml · A | -0.000 (n=62) | -0.002 (n=78) | +0.000 (n=80) | +0.001 (n=79) | +0.002 (n=15) | -0.002 (n=42) |
| ml · B | -0.001 (n=65) | -0.004 (n=86) | -0.004 (n=83) | +0.000 (n=77) | -0.006 (n=15) | -0.004 (n=40) |
| total · T | +1.481 (n=54) | +0.469 (n=64) | +0.065 (n=62) | -0.062 (n=65) | +0.111 (n=18) | +0.000 (n=25) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 128 | -0.618 (-1.30) | – | – | – |
| spread · A · D | 149 | -0.312 (-0.80) | – | – | – |
| spread · B · E | 128 | -0.990 (-2.36) | – | – | – |
| spread · B · D | 149 | -0.668 (-1.64) | – | – | – |
| ml · A · E | 128 | – | 0.2093 | 0.1957 | +0.0136 (2.35) |
| ml · A · D | 149 | – | 0.2075 | 0.1954 | +0.0121 (1.97) |
| ml · B · E | 128 | – | 0.2154 | 0.1957 | +0.0198 (3.06) |
| ml · B · D | 149 | – | 0.2102 | 0.1954 | +0.0148 (2.44) |
| total · T · E | 128 | +0.641 (1.57) | – | – | – |
| total · T · D | 149 | +0.239 (0.61) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._