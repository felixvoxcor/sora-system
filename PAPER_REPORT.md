# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **177** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · +0%* | 48 · -5% | 73 · -16% | 112 · -28% | 129 · -22% | 24 · -12%* |
| H6 | 26 · -20%* | 54 · -12% | 92 · -7% | 134 · -12% | 148 · -9% | 29 · -8%* |
| D | 31 · -14% | 57 · -7% | 93 · -6% | 131 · -8% | 155 · -8% | 22 · +4%* |
| L | 32 · -28% | 59 · -16% | 85 · -6% | 124 · +0% | 145 · -3% | 29 · -34%* |
| D+conf | 3 · -38%* | 9 · -15%* | 15 · +28%* | 22 · +13%* | 27 · -0%* | 8 · -4%* |
| D+fade | 18 · -16%* | 27 · -9%* | 39 · -3% | 49 · -7% | 50 · -9% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 30 · -30% | 50 · -23% | 80 · -12% | 115 · -15% | 133 · -7% | 20 · -33%* |
| H6 | 36 · -0% | 62 · -2% | 90 · -7% | 136 · -6% | 158 · -5% | 19 · -29%* |
| D | 34 · -10% | 60 · -2% | 95 · +0% | 138 · -5% | 164 · -5% | 13 · -26%* |
| L | 30 · -24% | 62 · -8% | 91 · -6% | 119 · -1% | 147 · -5% | 27 · -44%* |
| D+conf | 3 · -100%* | 9 · -16%* | 16 · +7%* | 30 · +2% | 37 · -2% | 1 · -100%* |
| D+fade | 14 · -4%* | 21 · -0%* | 35 · -2% | 44 · -10% | 45 · -12% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 25 · -48%* | 46 · -27% | 70 · -30% | 111 · -26% | 135 · -28% | 18 · +27%* |
| H6 | 32 · -58% | 64 · -23% | 87 · -23% | 138 · -17% | 153 · -18% | 24 · -7%* |
| D | 33 · -52% | 63 · -30% | 91 · -20% | 131 · -16% | 155 · -16% | 22 · -56%* |
| L | 39 · -52% | 61 · -33% | 90 · -12% | 126 · -8% | 147 · -15% | 26 · -26%* |
| D+conf | 2 · -100%* | 10 · -38%* | 16 · -19%* | 27 · -16%* | 33 · -7% | 5 · -74%* |
| D+fade | 23 · -51%* | 37 · -28% | 46 · -42% | 58 · -37% | 59 · -38% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 30 · -48% | 51 · -41% | 76 · -27% | 115 · -26% | 130 · -25% | 23 · -40%* |
| H6 | 39 · -56% | 67 · -23% | 101 · -16% | 139 · -19% | 158 · -14% | 19 · -42%* |
| D | 34 · -42% | 61 · -32% | 98 · -11% | 142 · -14% | 156 · -12% | 21 · -39%* |
| L | 36 · -22% | 58 · -31% | 90 · -26% | 126 · -17% | 149 · -19% | 24 · +29%* |
| D+conf | 1 · -100%* | 5 · -72%* | 16 · -35%* | 26 · -44%* | 29 · -27%* | 9 · -52%* |
| D+fade | 24 · -81%* | 33 · -51% | 45 · -39% | 57 · -35% | 57 · -35% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · -15%* | 49 · -7% | 64 · -8% | 90 · -11% | 123 · -4% | 30 · -30% |
| H6 | 15 · -36%* | 48 · -21% | 75 · -16% | 97 · -8% | 129 · -7% | 48 · -4% |
| D | 13 · -56%* | 48 · -16% | 76 · -9% | 105 · -11% | 137 · -5% | 40 · +5% |
| L | 15 · -36%* | 51 · -10% | 74 · -2% | 107 · -9% | 132 · -2% | 42 · -19% |
| D+conf | 2 · -4%* | 10 · +14%* | 21 · +9%* | 30 · +15% | 38 · +21% | 16 · +19%* |
| D+fade | 7 · -73%* | 21 · -45%* | 33 · -25% | 41 · -26% | 44 · -22% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 115. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.233 (n=73) | +0.054 (n=92) | +0.000 (n=93) | -0.047 (n=85) | -0.067 (n=15) | -0.103 (n=39) |
| spread · B | +0.250 (n=80) | -0.100 (n=90) | -0.032 (n=95) | -0.022 (n=91) | -0.188 (n=16) | -0.057 (n=35) |
| ml · A | +0.001 (n=70) | -0.002 (n=87) | -0.001 (n=91) | +0.001 (n=90) | +0.002 (n=16) | -0.002 (n=46) |
| ml · B | -0.002 (n=76) | -0.003 (n=101) | -0.003 (n=98) | -0.001 (n=90) | -0.004 (n=16) | -0.003 (n=45) |
| total · T | +1.156 (n=64) | +0.387 (n=75) | +0.053 (n=76) | -0.027 (n=74) | -0.143 (n=21) | +0.061 (n=33) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 153 | -0.718 (-1.68) | – | – | – |
| spread · A · D | 177 | -0.416 (-1.16) | – | – | – |
| spread · B · E | 153 | -0.827 (-2.15) | – | – | – |
| spread · B · D | 177 | -0.484 (-1.31) | – | – | – |
| ml · A · E | 153 | – | 0.2122 | 0.1978 | +0.0144 (2.85) |
| ml · A · D | 177 | – | 0.2084 | 0.1953 | +0.0132 (2.45) |
| ml · B · E | 153 | – | 0.2132 | 0.1978 | +0.0155 (2.70) |
| ml · B · D | 177 | – | 0.2070 | 0.1953 | +0.0117 (2.15) |
| total · T · E | 153 | +0.289 (0.75) | – | – | – |
| total · T · D | 177 | -0.139 (-0.37) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._