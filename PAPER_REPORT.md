# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **159** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · +0%* | 47 · -3% | 69 · -14% | 103 · -28% | 117 · -23% | 20 · -4%* |
| H6 | 25 · -17%* | 51 · -7% | 84 · -7% | 121 · -10% | 135 · -7% | 24 · -5%* |
| D | 31 · -14% | 54 · -1% | 86 · -3% | 120 · -6% | 143 · -5% | 16 · +19%* |
| L | 29 · -27%* | 55 · -13% | 80 · -4% | 112 · +1% | 132 · -3% | 24 · -28%* |
| D+conf | 3 · -38%* | 9 · -15%* | 15 · +28%* | 21 · +10%* | 26 · -4%* | 5 · -23%* |
| D+fade | 18 · -16%* | 25 · -1%* | 35 · -2% | 45 · -7% | 46 · -9% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 28 · -39%* | 46 · -29% | 73 · -16% | 103 · -17% | 119 · -9% | 18 · -36%* |
| H6 | 32 · -5% | 56 · -5% | 81 · -11% | 122 · -9% | 140 · -7% | 19 · -29%* |
| D | 32 · -16% | 56 · -5% | 85 · -3% | 123 · -5% | 146 · -6% | 13 · -26%* |
| L | 28 · -32%* | 56 · -15% | 81 · -11% | 106 · -7% | 130 · -12% | 26 · -42%* |
| D+conf | 3 · -100%* | 8 · -29%* | 14 · -4%* | 27 · -7%* | 34 · -10% | 1 · -100%* |
| D+fade | 13 · -12%* | 20 · -5%* | 31 · -8% | 39 · -12% | 40 · -15% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 25 · -48%* | 45 · -26% | 66 · -30% | 101 · -28% | 122 · -30% | 15 · +38%* |
| H6 | 32 · -58% | 59 · -27% | 81 · -28% | 124 · -20% | 136 · -18% | 23 · -12%* |
| D | 31 · -48% | 59 · -25% | 84 · -18% | 119 · -17% | 140 · -15% | 19 · -49%* |
| L | 36 · -53% | 57 · -32% | 82 · -16% | 116 · -11% | 135 · -16% | 20 · -26%* |
| D+conf | 2 · -100%* | 10 · -38%* | 16 · -19%* | 26 · -33%* | 31 · -18% | 4 · -67%* |
| D+fade | 21 · -46%* | 34 · -22% | 42 · -37% | 51 · -31% | 52 · -33% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 26 · -47%* | 47 · -39% | 68 · -33% | 103 · -29% | 114 · -27% | 23 · -40%* |
| H6 | 34 · -55% | 60 · -24% | 91 · -19% | 124 · -26% | 142 · -20% | 17 · -35%* |
| D | 30 · -53% | 57 · -37% | 87 · -19% | 128 · -19% | 141 · -16% | 18 · -46%* |
| L | 33 · -32% | 53 · -40% | 82 · -34% | 113 · -22% | 135 · -24% | 20 · +35%* |
| D+conf | 1 · -100%* | 5 · -72%* | 15 · -42%* | 25 · -48%* | 28 · -30%* | 7 · -81%* |
| D+fade | 22 · -79%* | 31 · -48% | 41 · -40% | 51 · -37% | 51 · -37% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 17 · -10%* | 45 · -2% | 59 · -3% | 81 · -6% | 110 · -1% | 27 · -22%* |
| H6 | 15 · -36%* | 45 · -15% | 70 · -10% | 86 · -3% | 116 · -1% | 43 · -11% |
| D | 13 · -56%* | 44 · -9% | 68 · -2% | 94 · -4% | 123 · -1% | 36 · +6% |
| L | 13 · -41%* | 47 · -7% | 69 · +2% | 96 · -1% | 117 · +4% | 39 · -17% |
| D+conf | 2 · -4%* | 9 · +27%* | 19 · +21%* | 28 · +23%* | 36 · +28% | 15 · +27%* |
| D+fade | 7 · -73%* | 18 · -36%* | 27 · -15%* | 34 · -16% | 37 · -13% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 108. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.232 (n=69) | -0.024 (n=84) | +0.035 (n=86) | -0.037 (n=80) | -0.067 (n=15) | -0.086 (n=35) |
| spread · B | +0.301 (n=73) | -0.086 (n=81) | -0.012 (n=85) | +0.012 (n=81) | -0.214 (n=14) | -0.065 (n=31) |
| ml · A | +0.002 (n=66) | -0.002 (n=81) | +0.000 (n=84) | +0.001 (n=82) | +0.002 (n=16) | -0.002 (n=42) |
| ml · B | -0.000 (n=68) | -0.003 (n=91) | -0.003 (n=87) | -0.000 (n=82) | -0.006 (n=15) | -0.004 (n=41) |
| total · T | +1.390 (n=59) | +0.429 (n=70) | +0.059 (n=68) | -0.029 (n=69) | +0.000 (n=19) | -0.037 (n=27) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 137 | -0.742 (-1.66) | – | – | – |
| spread · A · D | 159 | -0.382 (-1.01) | – | – | – |
| spread · B · E | 137 | -0.928 (-2.27) | – | – | – |
| spread · B · D | 159 | -0.590 (-1.49) | – | – | – |
| ml · A · E | 137 | – | 0.2103 | 0.1954 | +0.0149 (2.71) |
| ml · A · D | 159 | – | 0.2076 | 0.1948 | +0.0128 (2.19) |
| ml · B · E | 137 | – | 0.2133 | 0.1954 | +0.0179 (2.93) |
| ml · B · D | 159 | – | 0.2081 | 0.1948 | +0.0133 (2.31) |
| total · T · E | 137 | +0.474 (1.23) | – | – | – |
| total · T · D | 159 | +0.113 (0.30) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._