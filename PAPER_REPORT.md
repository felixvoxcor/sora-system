# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **174** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · +0%* | 48 · -5% | 71 · -17% | 110 · -29% | 127 · -22% | 24 · -12%* |
| H6 | 25 · -17%* | 53 · -11% | 90 · -7% | 131 · -13% | 145 · -9% | 29 · -8%* |
| D | 31 · -14% | 56 · -5% | 92 · -5% | 128 · -9% | 152 · -8% | 22 · +4%* |
| L | 31 · -26% | 58 · -14% | 84 · -5% | 121 · -1% | 142 · -3% | 29 · -34%* |
| D+conf | 3 · -38%* | 9 · -15%* | 15 · +28%* | 21 · +10%* | 26 · -4%* | 8 · -4%* |
| D+fade | 18 · -16%* | 26 · -5%* | 38 · -0% | 48 · -5% | 49 · -7% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 30 · -30% | 49 · -26% | 78 · -14% | 113 · -17% | 131 · -8% | 20 · -33%* |
| H6 | 35 · -3% | 61 · -4% | 89 · -8% | 133 · -8% | 155 · -7% | 19 · -29%* |
| D | 34 · -10% | 60 · -2% | 94 · -1% | 135 · -5% | 161 · -5% | 13 · -26%* |
| L | 30 · -24% | 62 · -8% | 90 · -7% | 117 · -2% | 145 · -7% | 26 · -42%* |
| D+conf | 3 · -100%* | 9 · -16%* | 15 · +2%* | 28 · -4%* | 35 · -7% | 1 · -100%* |
| D+fade | 14 · -4%* | 21 · -0%* | 35 · -2% | 44 · -10% | 45 · -12% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 25 · -48%* | 46 · -27% | 68 · -32% | 109 · -27% | 133 · -29% | 18 · +27%* |
| H6 | 32 · -58% | 63 · -22% | 85 · -24% | 135 · -19% | 150 · -19% | 24 · -7%* |
| D | 32 · -50% | 62 · -29% | 89 · -21% | 129 · -17% | 152 · -16% | 22 · -56%* |
| L | 38 · -50% | 60 · -32% | 88 · -13% | 124 · -9% | 144 · -15% | 26 · -26%* |
| D+conf | 2 · -100%* | 10 · -38%* | 16 · -19%* | 27 · -16%* | 33 · -7% | 5 · -74%* |
| D+fade | 22 · -49%* | 36 · -26% | 45 · -41% | 57 · -36% | 58 · -37% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 29 · -52%* | 50 · -43% | 74 · -31% | 113 · -28% | 128 · -27% | 23 · -40%* |
| H6 | 38 · -60% | 66 · -25% | 98 · -19% | 136 · -21% | 155 · -16% | 19 · -42%* |
| D | 34 · -42% | 61 · -32% | 95 · -15% | 139 · -17% | 153 · -14% | 21 · -39%* |
| L | 36 · -22% | 58 · -31% | 89 · -28% | 124 · -19% | 146 · -22% | 24 · +29%* |
| D+conf | 1 · -100%* | 5 · -72%* | 15 · -42%* | 25 · -48%* | 28 · -30%* | 9 · -52%* |
| D+fade | 24 · -81%* | 33 · -51% | 45 · -39% | 57 · -35% | 57 · -35% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · -15%* | 47 · -7% | 62 · -8% | 88 · -11% | 121 · -4% | 30 · -30% |
| H6 | 15 · -36%* | 47 · -19% | 74 · -15% | 94 · -9% | 126 · -8% | 48 · -4% |
| D | 13 · -56%* | 47 · -15% | 75 · -8% | 103 · -11% | 134 · -6% | 40 · +5% |
| L | 14 · -45%* | 49 · -10% | 72 · -2% | 105 · -9% | 129 · -2% | 42 · -19% |
| D+conf | 2 · -4%* | 10 · +14%* | 21 · +9%* | 30 · +15% | 38 · +21% | 16 · +19%* |
| D+fade | 7 · -73%* | 20 · -43%* | 32 · -22% | 40 · -24% | 43 · -20% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 113. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.254 (n=71) | +0.011 (n=90) | +0.011 (n=92) | -0.048 (n=84) | -0.067 (n=15) | -0.079 (n=38) |
| spread · B | +0.218 (n=78) | -0.146 (n=89) | -0.043 (n=94) | -0.022 (n=90) | -0.267 (n=15) | -0.057 (n=35) |
| ml · A | +0.002 (n=68) | -0.002 (n=85) | -0.001 (n=89) | +0.001 (n=88) | +0.002 (n=16) | -0.002 (n=45) |
| ml · B | -0.003 (n=74) | -0.004 (n=98) | -0.003 (n=95) | -0.001 (n=89) | -0.006 (n=15) | -0.003 (n=45) |
| total · T | +1.323 (n=62) | +0.405 (n=74) | +0.067 (n=75) | -0.028 (n=72) | -0.143 (n=21) | +0.094 (n=32) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 151 | -0.754 (-1.76) | – | – | – |
| spread · A · D | 174 | -0.414 (-1.15) | – | – | – |
| spread · B · E | 151 | -0.892 (-2.32) | – | – | – |
| spread · B · D | 174 | -0.502 (-1.35) | – | – | – |
| ml · A · E | 151 | – | 0.2111 | 0.1963 | +0.0148 (2.91) |
| ml · A · D | 174 | – | 0.2074 | 0.1943 | +0.0131 (2.42) |
| ml · B · E | 151 | – | 0.2132 | 0.1963 | +0.0169 (2.95) |
| ml · B · D | 174 | – | 0.2072 | 0.1943 | +0.0129 (2.34) |
| total · T · E | 151 | +0.298 (0.76) | – | – | – |
| total · T · D | 174 | -0.133 (-0.35) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._