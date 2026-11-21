# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **168** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · +0%* | 48 · -5% | 71 · -17% | 107 · -29% | 122 · -23% | 23 · -8%* |
| H6 | 25 · -17%* | 52 · -9% | 88 · -7% | 127 · -12% | 141 · -8% | 27 · -9%* |
| D | 31 · -14% | 55 · -3% | 90 · -3% | 126 · -8% | 150 · -7% | 18 · +6%* |
| L | 30 · -30% | 56 · -14% | 82 · -4% | 118 · -1% | 139 · -4% | 26 · -34%* |
| D+conf | 3 · -38%* | 9 · -15%* | 15 · +28%* | 21 · +10%* | 26 · -4%* | 5 · -23%* |
| D+fade | 18 · -16%* | 25 · -1%* | 37 · +2% | 47 · -3% | 48 · -5% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 29 · -34%* | 48 · -28% | 75 · -16% | 107 · -18% | 125 · -8% | 20 · -33%* |
| H6 | 34 · +0% | 59 · -4% | 85 · -8% | 128 · -9% | 149 · -8% | 19 · -29%* |
| D | 34 · -10% | 59 · -3% | 90 · -3% | 130 · -6% | 155 · -7% | 13 · -26%* |
| L | 29 · -28%* | 59 · -13% | 86 · -9% | 112 · -5% | 139 · -9% | 26 · -42%* |
| D+conf | 3 · -100%* | 8 · -29%* | 14 · -4%* | 27 · -7%* | 34 · -10% | 1 · -100%* |
| D+fade | 14 · -4%* | 21 · -0%* | 33 · -2% | 41 · -8% | 42 · -10% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 25 · -48%* | 46 · -27% | 67 · -31% | 107 · -31% | 129 · -32% | 16 · +30%* |
| H6 | 32 · -58% | 61 · -30% | 83 · -30% | 131 · -23% | 145 · -22% | 23 · -12%* |
| D | 32 · -50% | 61 · -27% | 87 · -21% | 126 · -21% | 148 · -19% | 20 · -52%* |
| L | 37 · -54% | 58 · -33% | 85 · -19% | 121 · -13% | 141 · -19% | 23 · -16%* |
| D+conf | 2 · -100%* | 10 · -38%* | 16 · -19%* | 26 · -33%* | 32 · -21% | 4 · -67%* |
| D+fade | 22 · -49%* | 36 · -26% | 45 · -41% | 57 · -36% | 58 · -37% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 28 · -51%* | 49 · -42% | 70 · -35% | 108 · -31% | 122 · -29% | 23 · -40%* |
| H6 | 37 · -59% | 63 · -27% | 95 · -21% | 130 · -28% | 149 · -22% | 19 · -42%* |
| D | 33 · -57% | 60 · -40% | 91 · -21% | 134 · -21% | 148 · -19% | 20 · -44%* |
| L | 35 · -36% | 56 · -43% | 85 · -36% | 119 · -25% | 141 · -27% | 23 · +28%* |
| D+conf | 1 · -100%* | 5 · -72%* | 15 · -42%* | 25 · -48%* | 28 · -30%* | 8 · -64%* |
| D+fade | 24 · -81%* | 33 · -51% | 44 · -41% | 55 · -39% | 55 · -39% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · -15%* | 46 · -5% | 60 · -5% | 86 · -9% | 117 · -2% | 28 · -25%* |
| H6 | 15 · -36%* | 47 · -19% | 74 · -15% | 91 · -6% | 122 · -5% | 46 · -5% |
| D | 13 · -56%* | 46 · -13% | 73 · -6% | 100 · -8% | 130 · -3% | 38 · +5% |
| L | 14 · -45%* | 49 · -10% | 71 · -1% | 101 · -5% | 125 · +1% | 40 · -15% |
| D+conf | 2 · -4%* | 10 · +14%* | 20 · +15%* | 29 · +19%* | 37 · +24% | 15 · +27%* |
| D+fade | 7 · -73%* | 19 · -40%* | 31 · -20% | 38 · -20% | 41 · -16% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 110. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.254 (n=71) | +0.011 (n=88) | +0.067 (n=90) | -0.037 (n=82) | -0.067 (n=15) | -0.054 (n=37) |
| spread · B | +0.267 (n=75) | -0.071 (n=85) | -0.011 (n=90) | +0.000 (n=86) | -0.214 (n=14) | -0.030 (n=33) |
| ml · A | +0.002 (n=67) | -0.002 (n=83) | +0.000 (n=87) | +0.001 (n=85) | +0.002 (n=16) | -0.002 (n=45) |
| ml · B | -0.001 (n=70) | -0.002 (n=95) | -0.003 (n=91) | -0.000 (n=85) | -0.006 (n=15) | -0.004 (n=44) |
| total · T | +1.367 (n=60) | +0.405 (n=74) | +0.068 (n=73) | -0.028 (n=71) | -0.050 (n=20) | +0.032 (n=31) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 145 | -0.748 (-1.72) | – | – | – |
| spread · A · D | 168 | -0.385 (-1.04) | – | – | – |
| spread · B · E | 145 | -0.904 (-2.29) | – | – | – |
| spread · B · D | 168 | -0.533 (-1.41) | – | – | – |
| ml · A · E | 145 | – | 0.2105 | 0.1948 | +0.0157 (2.98) |
| ml · A · D | 168 | – | 0.2069 | 0.1929 | +0.0140 (2.51) |
| ml · B · E | 145 | – | 0.2135 | 0.1948 | +0.0187 (3.18) |
| ml · B · D | 168 | – | 0.2079 | 0.1929 | +0.0150 (2.70) |
| total · T · E | 145 | +0.391 (1.01) | – | – | – |
| total · T · D | 168 | -0.041 (-0.11) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._