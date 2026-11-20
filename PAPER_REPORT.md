# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **158** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · +0%* | 47 · -3% | 69 · -14% | 103 · -28% | 116 · -23% | 20 · -4%* |
| H6 | 25 · -17%* | 51 · -7% | 84 · -7% | 120 · -10% | 134 · -6% | 24 · -5%* |
| D | 31 · -14% | 54 · -1% | 85 · -1% | 119 · -6% | 142 · -5% | 16 · +19%* |
| L | 29 · -27%* | 55 · -13% | 79 · -3% | 111 · +1% | 131 · -2% | 24 · -28%* |
| D+conf | 3 · -38%* | 9 · -15%* | 15 · +28%* | 21 · +10%* | 26 · -4%* | 5 · -23%* |
| D+fade | 18 · -16%* | 25 · -1%* | 34 · +0% | 44 · -5% | 45 · -7% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 28 · -39%* | 46 · -29% | 72 · -18% | 102 · -18% | 118 · -10% | 18 · -36%* |
| H6 | 32 · -5% | 56 · -5% | 81 · -11% | 121 · -10% | 139 · -8% | 19 · -29%* |
| D | 32 · -16% | 56 · -5% | 85 · -3% | 123 · -5% | 145 · -7% | 13 · -26%* |
| L | 28 · -32%* | 56 · -15% | 81 · -11% | 106 · -7% | 130 · -12% | 25 · -39%* |
| D+conf | 3 · -100%* | 8 · -29%* | 14 · -4%* | 27 · -7%* | 33 · -13% | 1 · -100%* |
| D+fade | 13 · -12%* | 20 · -5%* | 31 · -8% | 39 · -12% | 40 · -15% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 25 · -48%* | 45 · -26% | 66 · -30% | 101 · -28% | 121 · -29% | 15 · +38%* |
| H6 | 32 · -58% | 59 · -27% | 81 · -28% | 123 · -19% | 135 · -18% | 23 · -12%* |
| D | 31 · -48% | 59 · -25% | 84 · -18% | 118 · -17% | 139 · -15% | 19 · -49%* |
| L | 36 · -53% | 57 · -32% | 81 · -15% | 115 · -10% | 134 · -16% | 20 · -26%* |
| D+conf | 2 · -100%* | 10 · -38%* | 16 · -19%* | 26 · -33%* | 31 · -18% | 4 · -67%* |
| D+fade | 21 · -46%* | 34 · -22% | 42 · -37% | 50 · -30% | 51 · -31% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 26 · -47%* | 47 · -39% | 67 · -34% | 102 · -30% | 113 · -28% | 23 · -40%* |
| H6 | 34 · -55% | 60 · -24% | 90 · -20% | 123 · -26% | 141 · -20% | 17 · -35%* |
| D | 30 · -53% | 57 · -37% | 87 · -19% | 127 · -19% | 140 · -17% | 18 · -46%* |
| L | 33 · -32% | 53 · -40% | 82 · -34% | 113 · -22% | 135 · -24% | 19 · +34%* |
| D+conf | 1 · -100%* | 5 · -72%* | 15 · -42%* | 24 · -51%* | 27 · -32%* | 7 · -81%* |
| D+fade | 22 · -79%* | 31 · -48% | 41 · -40% | 51 · -37% | 51 · -37% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 17 · -10%* | 44 · -0% | 58 · -1% | 80 · -5% | 109 · -0% | 27 · -22%* |
| H6 | 15 · -36%* | 44 · -13% | 69 · -9% | 85 · -1% | 115 · -1% | 43 · -11% |
| D | 13 · -56%* | 43 · -7% | 67 · -0% | 93 · -3% | 122 · +0% | 36 · +6% |
| L | 13 · -41%* | 46 · -5% | 68 · +4% | 95 · +0% | 116 · +5% | 39 · -17% |
| D+conf | 2 · -4%* | 9 · +27%* | 19 · +21%* | 28 · +23%* | 36 · +28% | 15 · +27%* |
| D+fade | 7 · -73%* | 18 · -36%* | 27 · -15%* | 34 · -16% | 37 · -13% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 108. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.232 (n=69) | -0.024 (n=84) | +0.035 (n=85) | -0.038 (n=79) | -0.067 (n=15) | -0.088 (n=34) |
| spread · B | +0.278 (n=72) | -0.086 (n=81) | -0.012 (n=85) | +0.012 (n=81) | -0.214 (n=14) | -0.065 (n=31) |
| ml · A | +0.002 (n=66) | -0.002 (n=81) | +0.000 (n=84) | +0.001 (n=81) | +0.002 (n=16) | -0.002 (n=42) |
| ml · B | -0.001 (n=67) | -0.003 (n=90) | -0.003 (n=87) | -0.000 (n=82) | -0.006 (n=15) | -0.004 (n=41) |
| total · T | +1.397 (n=58) | +0.420 (n=69) | +0.045 (n=67) | -0.044 (n=68) | +0.000 (n=19) | -0.037 (n=27) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 136 | -0.732 (-1.63) | – | – | – |
| spread · A · D | 158 | -0.370 (-0.97) | – | – | – |
| spread · B · E | 136 | -0.945 (-2.30) | – | – | – |
| spread · B · D | 158 | -0.588 (-1.48) | – | – | – |
| ml · A · E | 136 | – | 0.2109 | 0.1960 | +0.0149 (2.70) |
| ml · A · D | 158 | – | 0.2081 | 0.1954 | +0.0126 (2.16) |
| ml · B · E | 136 | – | 0.2143 | 0.1960 | +0.0183 (2.99) |
| ml · B · D | 158 | – | 0.2089 | 0.1954 | +0.0135 (2.34) |
| total · T · E | 136 | +0.498 (1.28) | – | – | – |
| total · T · D | 158 | +0.132 (0.35) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._