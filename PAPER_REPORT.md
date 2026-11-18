# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **142** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 20 · +5%* | 43 · +2% | 63 · -9% | 92 · -25% | 103 · -22% | 18 · +7%* |
| H6 | 24 · -13%* | 49 · -3% | 77 · -1% | 108 · -5% | 120 · -3% | 22 · -5%* |
| D | 29 · -8%* | 51 · +4% | 76 · +3% | 109 · -2% | 127 · -2% | 15 · +14%* |
| L | 27 · -22%* | 50 · -8% | 73 · -0% | 102 · +3% | 120 · -1% | 22 · -30%* |
| D+conf | 2 · -7%* | 8 · -4%* | 13 · +33%* | 19 · +11%* | 22 · -4%* | 4 · -53%* |
| D+fade | 17 · -11%* | 24 · +3%* | 32 · +7% | 41 · +2% | 41 · +2% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 27 · -43%* | 45 · -32% | 67 · -17% | 93 · -20% | 106 · -12% | 15 · -36%* |
| H6 | 30 · -6% | 52 · -5% | 74 · -13% | 110 · -13% | 126 · -12% | 16 · -39%* |
| D | 32 · -16% | 54 · -8% | 76 · -5% | 111 · -9% | 130 · -9% | 12 · -36%* |
| L | 28 · -32%* | 54 · -19% | 74 · -18% | 96 · -13% | 119 · -17% | 23 · -42%* |
| D+conf | 3 · -100%* | 7 · -45%* | 13 · -12%* | 25 · -15%* | 30 · -23% | 1 · -100%* |
| D+fade | 13 · -12%* | 20 · -5%* | 28 · +2%* | 36 · -5% | 37 · -8% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · -44%* | 42 · -20% | 61 · -24% | 91 · -23% | 109 · -26% | 12 · +55%* |
| H6 | 31 · -57% | 58 · -26% | 76 · -24% | 110 · -11% | 119 · -12% | 23 · -12%* |
| D | 30 · -47% | 56 · -21% | 78 · -14% | 107 · -9% | 125 · -10% | 17 · -43%* |
| L | 34 · -50% | 54 · -28% | 77 · -11% | 107 · -5% | 123 · -12% | 19 · -22%* |
| D+conf | 1 · -100%* | 9 · -31%* | 15 · -14%* | 22 · -21%* | 26 · -3%* | 4 · -67%* |
| D+fade | 21 · -46%* | 33 · -19% | 40 · -33% | 46 · -24% | 47 · -25% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 25 · -45%* | 46 · -38% | 63 · -33% | 90 · -32% | 100 · -31% | 21 · -35%* |
| H6 | 32 · -52% | 55 · -20% | 84 · -16% | 112 · -26% | 127 · -22% | 15 · -36%* |
| D | 30 · -53% | 53 · -36% | 81 · -20% | 116 · -19% | 127 · -18% | 15 · -44%* |
| L | 33 · -32% | 51 · -37% | 75 · -36% | 104 · -24% | 124 · -25% | 18 · +24%* |
| D+conf | 1 · -100%* | 5 · -72%* | 15 · -42%* | 23 · -49%* | 25 · -39%* | 5 · -100%* |
| D+fade | 22 · -79%* | 29 · -50%* | 39 · -42% | 47 · -39% | 47 · -39% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 15 · +2%* | 41 · +7% | 53 · +8% | 72 · +1% | 98 · +1% | 23 · -8%* |
| H6 | 12 · -21%* | 39 · -7% | 63 · -3% | 75 · +4% | 104 · +4% | 38 · -14% |
| D | 11 · -48%* | 38 · +1% | 60 · +5% | 83 · +4% | 110 · +4% | 32 · +7% |
| L | 10 · -43%* | 41 · -2% | 63 · +6% | 88 · +4% | 107 · +9% | 35 · -19% |
| D+conf | 2 · -4%* | 9 · +27%* | 18 · +27%* | 27 · +27%* | 34 · +30% | 15 · +27%* |
| D+fade | 6 · -69%* | 15 · -36%* | 23 · -17%* | 29 · -15%* | 32 · -11% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 103. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.079 (n=63) | -0.065 (n=77) | -0.026 (n=76) | -0.041 (n=73) | -0.077 (n=13) | -0.094 (n=32) |
| spread · B | +0.164 (n=67) | -0.162 (n=74) | -0.105 (n=76) | +0.014 (n=74) | -0.231 (n=13) | -0.071 (n=28) |
| ml · A | -0.000 (n=61) | -0.001 (n=76) | +0.001 (n=78) | +0.001 (n=77) | +0.002 (n=15) | -0.002 (n=40) |
| ml · B | +0.000 (n=63) | -0.003 (n=84) | -0.004 (n=81) | +0.000 (n=75) | -0.006 (n=15) | -0.005 (n=39) |
| total · T | +1.566 (n=53) | +0.508 (n=63) | +0.133 (n=60) | -0.032 (n=63) | +0.111 (n=18) | +0.174 (n=23) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 121 | -0.710 (-1.49) | – | – | – |
| spread · A · D | 142 | -0.340 (-0.86) | – | – | – |
| spread · B · E | 121 | -1.036 (-2.46) | – | – | – |
| spread · B · D | 142 | -0.684 (-1.67) | – | – | – |
| ml · A · E | 121 | – | 0.2035 | 0.1899 | +0.0136 (2.24) |
| ml · A · D | 142 | – | 0.2026 | 0.1916 | +0.0110 (1.72) |
| ml · B · E | 121 | – | 0.2100 | 0.1899 | +0.0201 (2.98) |
| ml · B · D | 142 | – | 0.2064 | 0.1916 | +0.0148 (2.35) |
| total · T · E | 121 | +0.719 (1.73) | – | – | – |
| total · T · D | 142 | +0.325 (0.81) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._