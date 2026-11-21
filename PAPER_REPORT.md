# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **166** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · +0%* | 48 · -5% | 70 · -15% | 106 · -28% | 121 · -23% | 23 · -8%* |
| H6 | 25 · -17%* | 52 · -9% | 87 · -6% | 126 · -11% | 140 · -7% | 26 · -12%* |
| D | 31 · -14% | 55 · -3% | 89 · -2% | 125 · -7% | 148 · -6% | 18 · +6%* |
| L | 30 · -30% | 56 · -14% | 82 · -4% | 117 · -0% | 137 · -4% | 26 · -34%* |
| D+conf | 3 · -38%* | 9 · -15%* | 15 · +28%* | 21 · +10%* | 26 · -4%* | 5 · -23%* |
| D+fade | 18 · -16%* | 25 · -1%* | 37 · +2% | 47 · -3% | 48 · -5% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 29 · -34%* | 48 · -28% | 75 · -16% | 106 · -17% | 124 · -8% | 20 · -33%* |
| H6 | 33 · -2% | 58 · -5% | 84 · -10% | 126 · -9% | 147 · -8% | 19 · -29%* |
| D | 33 · -13% | 58 · -5% | 89 · -4% | 128 · -6% | 153 · -7% | 13 · -26%* |
| L | 29 · -28%* | 58 · -15% | 85 · -11% | 111 · -6% | 137 · -11% | 26 · -42%* |
| D+conf | 3 · -100%* | 8 · -29%* | 14 · -4%* | 27 · -7%* | 34 · -10% | 1 · -100%* |
| D+fade | 14 · -4%* | 21 · -0%* | 33 · -2% | 41 · -8% | 42 · -10% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 25 · -48%* | 46 · -27% | 67 · -31% | 106 · -30% | 128 · -32% | 16 · +30%* |
| H6 | 32 · -58% | 61 · -30% | 83 · -30% | 130 · -22% | 143 · -21% | 23 · -12%* |
| D | 32 · -50% | 61 · -27% | 87 · -21% | 125 · -20% | 147 · -18% | 19 · -49%* |
| L | 37 · -54% | 58 · -33% | 85 · -19% | 121 · -13% | 141 · -19% | 21 · -24%* |
| D+conf | 2 · -100%* | 10 · -38%* | 16 · -19%* | 26 · -33%* | 32 · -21% | 4 · -67%* |
| D+fade | 22 · -49%* | 36 · -26% | 45 · -41% | 57 · -36% | 58 · -37% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 28 · -51%* | 49 · -42% | 70 · -35% | 107 · -30% | 121 · -28% | 23 · -40%* |
| H6 | 36 · -58% | 62 · -26% | 94 · -20% | 128 · -27% | 147 · -20% | 19 · -42%* |
| D | 32 · -56% | 59 · -39% | 90 · -20% | 132 · -20% | 146 · -18% | 20 · -44%* |
| L | 34 · -34% | 55 · -42% | 84 · -36% | 118 · -24% | 140 · -26% | 22 · +34%* |
| D+conf | 1 · -100%* | 5 · -72%* | 15 · -42%* | 25 · -48%* | 28 · -30%* | 8 · -64%* |
| D+fade | 24 · -81%* | 33 · -51% | 44 · -41% | 55 · -39% | 55 · -39% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · -15%* | 46 · -5% | 60 · -5% | 86 · -9% | 116 · -3% | 28 · -25%* |
| H6 | 15 · -36%* | 47 · -19% | 74 · -15% | 91 · -6% | 121 · -4% | 45 · -7% |
| D | 13 · -56%* | 46 · -13% | 73 · -6% | 99 · -7% | 128 · -3% | 38 · +5% |
| L | 14 · -45%* | 49 · -10% | 71 · -1% | 100 · -5% | 123 · +1% | 40 · -15% |
| D+conf | 2 · -4%* | 10 · +14%* | 20 · +15%* | 29 · +19%* | 37 · +24% | 15 · +27%* |
| D+fade | 7 · -73%* | 19 · -40%* | 31 · -20% | 38 · -20% | 41 · -16% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 110. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.214 (n=70) | -0.023 (n=87) | +0.034 (n=89) | -0.037 (n=82) | -0.067 (n=15) | -0.054 (n=37) |
| spread · B | +0.267 (n=75) | -0.083 (n=84) | -0.011 (n=89) | +0.012 (n=85) | -0.214 (n=14) | -0.030 (n=33) |
| ml · A | +0.002 (n=67) | -0.002 (n=83) | +0.000 (n=87) | +0.001 (n=85) | +0.002 (n=16) | -0.002 (n=45) |
| ml · B | -0.001 (n=70) | -0.002 (n=94) | -0.003 (n=90) | -0.000 (n=84) | -0.006 (n=15) | -0.004 (n=44) |
| total · T | +1.367 (n=60) | +0.405 (n=74) | +0.068 (n=73) | -0.028 (n=71) | -0.050 (n=20) | +0.032 (n=31) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 144 | -0.733 (-1.67) | – | – | – |
| spread · A · D | 166 | -0.375 (-1.01) | – | – | – |
| spread · B · E | 144 | -0.893 (-2.25) | – | – | – |
| spread · B · D | 166 | -0.572 (-1.48) | – | – | – |
| ml · A · E | 144 | – | 0.2101 | 0.1946 | +0.0155 (2.93) |
| ml · A · D | 166 | – | 0.2075 | 0.1937 | +0.0139 (2.46) |
| ml · B · E | 144 | – | 0.2132 | 0.1946 | +0.0186 (3.14) |
| ml · B · D | 166 | – | 0.2083 | 0.1937 | +0.0146 (2.59) |
| total · T · E | 144 | +0.362 (0.94) | – | – | – |
| total · T · D | 166 | -0.016 (-0.04) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._