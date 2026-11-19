# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **154** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · +0%* | 44 · -0% | 66 · -13% | 100 · -27% | 113 · -22% | 20 · -4%* |
| H6 | 25 · -17%* | 50 · -5% | 82 · -7% | 116 · -10% | 130 · -6% | 24 · -5%* |
| D | 31 · -14% | 53 · +0% | 82 · -2% | 116 · -6% | 138 · -5% | 16 · +19%* |
| L | 29 · -27%* | 54 · -11% | 77 · -3% | 108 · +1% | 127 · -2% | 24 · -28%* |
| D+conf | 3 · -38%* | 9 · -15%* | 14 · +24%* | 20 · +6%* | 24 · -4%* | 5 · -23%* |
| D+fade | 18 · -16%* | 25 · -1%* | 34 · +0% | 44 · -5% | 45 · -7% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 27 · -43%* | 45 · -32% | 70 · -21% | 100 · -20% | 115 · -10% | 18 · -36%* |
| H6 | 31 · -9% | 54 · -9% | 78 · -15% | 117 · -14% | 135 · -11% | 19 · -29%* |
| D | 32 · -16% | 54 · -8% | 81 · -8% | 119 · -9% | 141 · -9% | 13 · -26%* |
| L | 28 · -32%* | 54 · -19% | 78 · -15% | 102 · -10% | 126 · -15% | 25 · -39%* |
| D+conf | 3 · -100%* | 7 · -45%* | 13 · -12%* | 26 · -11%* | 32 · -16% | 1 · -100%* |
| D+fade | 13 · -12%* | 20 · -5%* | 31 · -8% | 39 · -12% | 40 · -15% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 24 · -46%* | 43 · -22% | 63 · -27% | 98 · -26% | 118 · -27% | 15 · +38%* |
| H6 | 32 · -58% | 59 · -27% | 79 · -27% | 119 · -16% | 131 · -15% | 23 · -12%* |
| D | 31 · -48% | 58 · -24% | 82 · -16% | 115 · -14% | 135 · -12% | 19 · -49%* |
| L | 36 · -53% | 57 · -32% | 80 · -14% | 112 · -7% | 130 · -13% | 20 · -26%* |
| D+conf | 2 · -100%* | 10 · -38%* | 16 · -19%* | 25 · -31%* | 29 · -13%* | 4 · -67%* |
| D+fade | 21 · -46%* | 34 · -22% | 42 · -37% | 50 · -30% | 51 · -31% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 25 · -45%* | 46 · -38% | 65 · -35% | 99 · -30% | 110 · -28% | 23 · -40%* |
| H6 | 33 · -54% | 57 · -23% | 87 · -19% | 119 · -27% | 137 · -20% | 17 · -35%* |
| D | 30 · -53% | 54 · -37% | 83 · -19% | 123 · -19% | 136 · -17% | 18 · -46%* |
| L | 33 · -32% | 51 · -37% | 78 · -35% | 109 · -23% | 131 · -25% | 19 · +34%* |
| D+conf | 1 · -100%* | 5 · -72%* | 15 · -42%* | 24 · -51%* | 27 · -32%* | 7 · -81%* |
| D+fade | 22 · -79%* | 30 · -52% | 40 · -44% | 50 · -39% | 50 · -39% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 16 · -4%* | 43 · +2% | 57 · +0% | 78 · -5% | 107 · -0% | 26 · -19%* |
| H6 | 14 · -32%* | 43 · -11% | 67 · -6% | 83 · +1% | 113 · +1% | 41 · -16% |
| D | 12 · -52%* | 41 · -2% | 65 · +3% | 91 · -1% | 119 · +1% | 35 · +4% |
| L | 12 · -36%* | 45 · -3% | 67 · +5% | 93 · +3% | 113 · +6% | 38 · -20% |
| D+conf | 2 · -4%* | 9 · +27%* | 19 · +21%* | 28 · +23%* | 35 · +26% | 15 · +27%* |
| D+fade | 7 · -73%* | 18 · -36%* | 27 · -15%* | 34 · -16% | 37 · -13% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 107. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.182 (n=66) | -0.024 (n=82) | +0.024 (n=82) | -0.039 (n=77) | -0.071 (n=14) | -0.088 (n=34) |
| spread · B | +0.271 (n=70) | -0.090 (n=78) | -0.025 (n=81) | +0.013 (n=78) | -0.231 (n=13) | -0.065 (n=31) |
| ml · A | +0.000 (n=63) | -0.002 (n=79) | -0.000 (n=82) | +0.001 (n=80) | +0.002 (n=16) | -0.002 (n=42) |
| ml · B | -0.001 (n=65) | -0.003 (n=87) | -0.004 (n=83) | +0.000 (n=78) | -0.006 (n=15) | -0.004 (n=40) |
| total · T | +1.421 (n=57) | +0.418 (n=67) | +0.015 (n=65) | -0.060 (n=67) | +0.000 (n=19) | -0.037 (n=27) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 133 | -0.688 (-1.49) | – | – | – |
| spread · A · D | 154 | -0.352 (-0.91) | – | – | – |
| spread · B · E | 133 | -0.971 (-2.32) | – | – | – |
| spread · B · D | 154 | -0.655 (-1.61) | – | – | – |
| ml · A · E | 133 | – | 0.2122 | 0.1981 | +0.0141 (2.50) |
| ml · A · D | 154 | – | 0.2101 | 0.1978 | +0.0122 (2.04) |
| ml · B · E | 133 | – | 0.2170 | 0.1981 | +0.0189 (3.03) |
| ml · B · D | 154 | – | 0.2121 | 0.1978 | +0.0143 (2.43) |
| total · T · E | 133 | +0.500 (1.26) | – | – | – |
| total · T · D | 154 | +0.141 (0.37) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._