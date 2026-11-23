# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **179** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 22 · +4%* | 49 · -3% | 74 · -15% | 114 · -28% | 131 · -21% | 24 · -12%* |
| H6 | 27 · -16%* | 56 · -12% | 94 · -7% | 136 · -12% | 150 · -8% | 29 · -8%* |
| D | 33 · -14% | 59 · -7% | 95 · -6% | 133 · -8% | 157 · -8% | 22 · +4%* |
| L | 33 · -25% | 61 · -15% | 87 · -6% | 126 · -0% | 147 · -3% | 29 · -34%* |
| D+conf | 3 · -38%* | 9 · -15%* | 15 · +28%* | 22 · +13%* | 27 · -0%* | 8 · -4%* |
| D+fade | 20 · -15%* | 29 · -9%* | 41 · -3% | 51 · -7% | 52 · -9% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 31 · -32% | 52 · -23% | 82 · -12% | 117 · -15% | 135 · -7% | 20 · -33%* |
| H6 | 37 · -3% | 63 · -4% | 91 · -8% | 138 · -6% | 160 · -5% | 19 · -29%* |
| D | 35 · -13% | 61 · -3% | 96 · -1% | 140 · -5% | 166 · -5% | 13 · -26%* |
| L | 31 · -26% | 63 · -9% | 93 · -6% | 121 · -1% | 149 · -5% | 27 · -44%* |
| D+conf | 3 · -100%* | 9 · -16%* | 16 · +7%* | 30 · +2% | 37 · -2% | 1 · -100%* |
| D+fade | 15 · -11%* | 22 · -5%* | 36 · -5% | 46 · -9% | 47 · -11% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 26 · -50%* | 47 · -29% | 72 · -31% | 113 · -26% | 137 · -28% | 18 · +27%* |
| H6 | 33 · -60% | 66 · -23% | 89 · -23% | 140 · -18% | 155 · -18% | 24 · -7%* |
| D | 35 · -51% | 65 · -30% | 93 · -20% | 133 · -16% | 157 · -17% | 22 · -56%* |
| L | 40 · -53% | 63 · -33% | 92 · -13% | 128 · -9% | 149 · -15% | 26 · -26%* |
| D+conf | 2 · -100%* | 10 · -38%* | 16 · -19%* | 27 · -16%* | 33 · -7% | 5 · -74%* |
| D+fade | 25 · -49%* | 39 · -28% | 48 · -42% | 60 · -37% | 61 · -38% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 31 · -46% | 53 · -40% | 78 · -28% | 117 · -26% | 132 · -25% | 23 · -40%* |
| H6 | 40 · -54% | 68 · -23% | 103 · -16% | 141 · -19% | 160 · -14% | 19 · -42%* |
| D | 35 · -40% | 62 · -31% | 100 · -11% | 144 · -14% | 158 · -12% | 21 · -39%* |
| L | 37 · -21% | 59 · -30% | 92 · -26% | 128 · -17% | 151 · -19% | 24 · +29%* |
| D+conf | 1 · -100%* | 5 · -72%* | 16 · -35%* | 26 · -44%* | 29 · -27%* | 9 · -52%* |
| D+fade | 25 · -77%* | 34 · -48% | 47 · -39% | 59 · -35% | 59 · -35% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · -15%* | 49 · -7% | 64 · -8% | 90 · -11% | 123 · -4% | 32 · -28% |
| H6 | 15 · -36%* | 48 · -21% | 75 · -16% | 98 · -7% | 131 · -5% | 48 · -4% |
| D | 13 · -56%* | 49 · -14% | 77 · -8% | 106 · -10% | 138 · -5% | 41 · +2% |
| L | 15 · -36%* | 51 · -10% | 75 · -1% | 108 · -8% | 134 · -2% | 42 · -19% |
| D+conf | 2 · -4%* | 10 · +14%* | 21 · +9%* | 30 · +15% | 38 · +21% | 17 · +12%* |
| D+fade | 7 · -73%* | 22 · -39%* | 34 · -22% | 42 · -23% | 45 · -20% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 115. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.216 (n=74) | +0.032 (n=94) | +0.000 (n=95) | -0.057 (n=87) | -0.067 (n=15) | -0.098 (n=41) |
| spread · B | +0.183 (n=82) | -0.121 (n=91) | -0.042 (n=96) | -0.032 (n=93) | -0.188 (n=16) | -0.083 (n=36) |
| ml · A | -0.001 (n=72) | -0.003 (n=89) | -0.001 (n=93) | +0.000 (n=92) | +0.002 (n=16) | -0.003 (n=48) |
| ml · B | -0.004 (n=78) | -0.003 (n=103) | -0.003 (n=100) | -0.001 (n=92) | -0.004 (n=16) | -0.004 (n=47) |
| total · T | +1.156 (n=64) | +0.387 (n=75) | +0.078 (n=77) | -0.013 (n=75) | -0.143 (n=21) | +0.118 (n=34) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 155 | -0.698 (-1.66) | – | – | – |
| spread · A · D | 179 | -0.390 (-1.11) | – | – | – |
| spread · B · E | 155 | -0.822 (-2.16) | – | – | – |
| spread · B · D | 179 | -0.479 (-1.31) | – | – | – |
| ml · A · E | 155 | – | 0.2107 | 0.1960 | +0.0148 (2.93) |
| ml · A · D | 179 | – | 0.2072 | 0.1938 | +0.0134 (2.50) |
| ml · B · E | 155 | – | 0.2114 | 0.1960 | +0.0154 (2.72) |
| ml · B · D | 179 | – | 0.2053 | 0.1938 | +0.0114 (2.12) |
| total · T · E | 155 | +0.275 (0.69) | – | – | – |
| total · T · D | 179 | -0.158 (-0.42) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._