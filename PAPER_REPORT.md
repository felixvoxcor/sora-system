# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **184** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 22 · +4%* | 50 · -1% | 77 · -11% | 118 · -26% | 135 · -19% | 25 · -16%* |
| H6 | 27 · -16%* | 57 · -10% | 97 · -4% | 139 · -10% | 154 · -7% | 30 · -11% |
| D | 33 · -14% | 60 · -5% | 98 · -3% | 136 · -6% | 162 · -6% | 22 · +4%* |
| L | 33 · -25% | 63 · -12% | 89 · -4% | 129 · +2% | 151 · -1% | 30 · -36% |
| D+conf | 3 · -38%* | 9 · -15%* | 16 · +32%* | 23 · +17%* | 29 · -1%* | 8 · -4%* |
| D+fade | 20 · -15%* | 30 · -5% | 42 · -1% | 52 · -5% | 53 · -7% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 32 · -28% | 53 · -21% | 83 · -10% | 121 · -12% | 140 · -5% | 20 · -33%* |
| H6 | 37 · -3% | 63 · -4% | 94 · -5% | 142 · -5% | 165 · -4% | 19 · -29%* |
| D | 35 · -13% | 61 · -3% | 99 · +2% | 143 · -3% | 170 · -4% | 14 · -18%* |
| L | 31 · -26% | 63 · -9% | 93 · -6% | 124 · +1% | 152 · -3% | 29 · -35%* |
| D+conf | 3 · -100%* | 9 · -16%* | 16 · +7%* | 30 · +2% | 37 · -2% | 1 · -100%* |
| D+fade | 15 · -11%* | 22 · -5%* | 38 · -0% | 48 · -5% | 49 · -7% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 27 · -37%* | 48 · -22% | 74 · -24% | 117 · -22% | 141 · -25% | 19 · +20%* |
| H6 | 34 · -49% | 67 · -19% | 90 · -20% | 143 · -14% | 159 · -16% | 25 · -1%* |
| D | 35 · -51% | 66 · -25% | 95 · -16% | 137 · -12% | 162 · -13% | 22 · -56%* |
| L | 41 · -45% | 64 · -28% | 93 · -10% | 130 · -6% | 153 · -13% | 27 · -19%* |
| D+conf | 2 · -100%* | 11 · -10%* | 17 · -3%* | 28 · -6%* | 35 · -2% | 5 · -74%* |
| D+fade | 25 · -49%* | 39 · -28% | 48 · -42% | 60 · -37% | 61 · -38% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 32 · -39% | 54 · -37% | 81 · -20% | 122 · -20% | 137 · -20% | 23 · -40%* |
| H6 | 40 · -54% | 68 · -23% | 106 · -14% | 145 · -17% | 164 · -12% | 20 · -45%* |
| D | 35 · -40% | 62 · -31% | 102 · -9% | 148 · -12% | 162 · -10% | 22 · -26%* |
| L | 37 · -21% | 59 · -30% | 93 · -24% | 131 · -16% | 155 · -17% | 25 · +39%* |
| D+conf | 1 · -100%* | 5 · -72%* | 16 · -35%* | 26 · -44%* | 29 · -27%* | 10 · -21%* |
| D+fade | 25 · -77%* | 34 · -48% | 49 · -32% | 61 · -30% | 61 · -30% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · -15%* | 51 · -10% | 67 · -9% | 93 · -12% | 128 · -5% | 32 · -28% |
| H6 | 16 · -29%* | 51 · -22% | 80 · -17% | 103 · -7% | 136 · -6% | 48 · -4% |
| D | 14 · -45%* | 52 · -15% | 80 · -9% | 110 · -11% | 142 · -6% | 42 · +4% |
| L | 16 · -28%* | 53 · -10% | 78 · -2% | 112 · -10% | 139 · -4% | 42 · -19% |
| D+conf | 2 · -4%* | 10 · +14%* | 21 · +9%* | 31 · +11% | 39 · +18% | 18 · +17%* |
| D+fade | 8 · -52%* | 25 · -39%* | 37 · -23% | 45 · -24% | 48 · -21% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 116. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.247 (n=77) | +0.062 (n=97) | +0.031 (n=98) | -0.056 (n=89) | -0.125 (n=16) | -0.095 (n=42) |
| spread · B | +0.181 (n=83) | -0.074 (n=94) | +0.010 (n=99) | -0.032 (n=93) | -0.188 (n=16) | -0.053 (n=38) |
| ml · A | +0.000 (n=74) | -0.003 (n=90) | -0.001 (n=95) | +0.000 (n=93) | +0.001 (n=17) | -0.003 (n=48) |
| ml · B | -0.003 (n=81) | -0.003 (n=106) | -0.003 (n=102) | -0.001 (n=93) | -0.004 (n=16) | -0.003 (n=49) |
| total · T | +1.194 (n=67) | +0.450 (n=80) | +0.100 (n=80) | -0.013 (n=78) | -0.143 (n=21) | +0.162 (n=37) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 160 | -0.598 (-1.44) | – | – | – |
| spread · A · D | 184 | -0.309 (-0.89) | – | – | – |
| spread · B · E | 160 | -0.728 (-1.95) | – | – | – |
| spread · B · D | 184 | -0.429 (-1.19) | – | – | – |
| ml · A · E | 160 | – | 0.2123 | 0.1992 | +0.0130 (2.59) |
| ml · A · D | 184 | – | 0.2085 | 0.1968 | +0.0117 (2.20) |
| ml · B · E | 160 | – | 0.2118 | 0.1992 | +0.0125 (2.19) |
| ml · B · D | 184 | – | 0.2069 | 0.1968 | +0.0101 (1.90) |
| total · T · E | 160 | +0.135 (0.34) | – | – | – |
| total · T · D | 184 | -0.224 (-0.59) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._