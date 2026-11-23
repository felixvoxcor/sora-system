# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **180** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 22 · +4%* | 50 · -1% | 75 · -13% | 115 · -27% | 132 · -20% | 24 · -12%* |
| H6 | 27 · -16%* | 57 · -10% | 95 · -6% | 137 · -11% | 151 · -8% | 29 · -8%* |
| D | 33 · -14% | 59 · -7% | 96 · -5% | 134 · -8% | 158 · -7% | 22 · +4%* |
| L | 33 · -25% | 62 · -14% | 88 · -5% | 127 · +1% | 148 · -2% | 29 · -34%* |
| D+conf | 3 · -38%* | 9 · -15%* | 16 · +32%* | 23 · +17%* | 28 · +3%* | 8 · -4%* |
| D+fade | 20 · -15%* | 29 · -9%* | 41 · -3% | 51 · -7% | 52 · -9% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 31 · -32% | 52 · -23% | 82 · -12% | 118 · -14% | 136 · -6% | 20 · -33%* |
| H6 | 37 · -3% | 63 · -4% | 91 · -8% | 139 · -7% | 161 · -5% | 19 · -29%* |
| D | 35 · -13% | 61 · -3% | 96 · -1% | 140 · -5% | 167 · -5% | 13 · -26%* |
| L | 31 · -26% | 63 · -9% | 93 · -6% | 121 · -1% | 149 · -5% | 28 · -39%* |
| D+conf | 3 · -100%* | 9 · -16%* | 16 · +7%* | 30 · +2% | 37 · -2% | 1 · -100%* |
| D+fade | 15 · -11%* | 22 · -5%* | 36 · -5% | 46 · -9% | 47 · -11% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 27 · -37%* | 48 · -22% | 73 · -26% | 114 · -23% | 138 · -26% | 18 · +27%* |
| H6 | 34 · -49% | 67 · -19% | 90 · -20% | 141 · -16% | 156 · -16% | 24 · -7%* |
| D | 35 · -51% | 66 · -25% | 94 · -17% | 134 · -14% | 158 · -15% | 22 · -56%* |
| L | 41 · -45% | 64 · -28% | 93 · -10% | 129 · -7% | 150 · -13% | 26 · -26%* |
| D+conf | 2 · -100%* | 11 · -10%* | 17 · -3%* | 28 · -6%* | 34 · +1% | 5 · -74%* |
| D+fade | 25 · -49%* | 39 · -28% | 48 · -42% | 60 · -37% | 61 · -38% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 31 · -46% | 53 · -40% | 79 · -23% | 118 · -23% | 133 · -22% | 23 · -40%* |
| H6 | 40 · -54% | 68 · -23% | 103 · -16% | 141 · -19% | 160 · -14% | 20 · -45%* |
| D | 35 · -40% | 62 · -31% | 100 · -11% | 144 · -14% | 158 · -12% | 22 · -26%* |
| L | 37 · -21% | 59 · -30% | 92 · -26% | 128 · -17% | 151 · -19% | 25 · +39%* |
| D+conf | 1 · -100%* | 5 · -72%* | 16 · -35%* | 26 · -44%* | 29 · -27%* | 10 · -21%* |
| D+fade | 25 · -77%* | 34 · -48% | 47 · -39% | 59 · -35% | 59 · -35% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · -15%* | 50 · -8% | 65 · -9% | 91 · -12% | 124 · -5% | 32 · -28% |
| H6 | 15 · -36%* | 49 · -22% | 76 · -17% | 99 · -8% | 132 · -6% | 48 · -4% |
| D | 13 · -56%* | 50 · -16% | 78 · -9% | 107 · -11% | 139 · -5% | 41 · +2% |
| L | 15 · -36%* | 51 · -10% | 76 · -2% | 109 · -9% | 135 · -2% | 42 · -19% |
| D+conf | 2 · -4%* | 10 · +14%* | 21 · +9%* | 30 · +15% | 38 · +21% | 17 · +12%* |
| D+fade | 7 · -73%* | 23 · -42%* | 35 · -24% | 43 · -25% | 46 · -21% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 115. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.213 (n=75) | +0.032 (n=95) | -0.010 (n=96) | -0.057 (n=88) | -0.125 (n=16) | -0.098 (n=41) |
| spread · B | +0.183 (n=82) | -0.121 (n=91) | -0.042 (n=96) | -0.032 (n=93) | -0.188 (n=16) | -0.083 (n=36) |
| ml · A | -0.001 (n=73) | -0.003 (n=90) | -0.001 (n=94) | +0.000 (n=93) | +0.001 (n=17) | -0.003 (n=48) |
| ml · B | -0.003 (n=79) | -0.003 (n=103) | -0.003 (n=100) | -0.001 (n=92) | -0.004 (n=16) | -0.004 (n=47) |
| total · T | +1.123 (n=65) | +0.395 (n=76) | +0.090 (n=78) | -0.013 (n=76) | -0.143 (n=21) | +0.143 (n=35) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 156 | -0.673 (-1.61) | – | – | – |
| spread · A · D | 180 | -0.381 (-1.09) | – | – | – |
| spread · B · E | 156 | -0.815 (-2.15) | – | – | – |
| spread · B · D | 180 | -0.489 (-1.34) | – | – | – |
| ml · A · E | 156 | – | 0.2121 | 0.1984 | +0.0137 (2.67) |
| ml · A · D | 180 | – | 0.2083 | 0.1957 | +0.0126 (2.33) |
| ml · B · E | 156 | – | 0.2131 | 0.1984 | +0.0147 (2.58) |
| ml · B · D | 180 | – | 0.2071 | 0.1957 | +0.0113 (2.11) |
| total · T · E | 156 | +0.198 (0.50) | – | – | – |
| total · T · D | 180 | -0.213 (-0.56) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._