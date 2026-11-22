# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **172** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · +0%* | 48 · -5% | 71 · -17% | 109 · -30% | 125 · -24% | 24 · -12%* |
| H6 | 25 · -17%* | 53 · -11% | 89 · -8% | 130 · -14% | 144 · -10% | 28 · -12%* |
| D | 31 · -14% | 56 · -5% | 92 · -5% | 128 · -9% | 152 · -8% | 20 · -5%* |
| L | 31 · -26% | 58 · -14% | 84 · -5% | 120 · -1% | 141 · -4% | 28 · -38%* |
| D+conf | 3 · -38%* | 9 · -15%* | 15 · +28%* | 21 · +10%* | 26 · -4%* | 6 · -36%* |
| D+fade | 18 · -16%* | 26 · -5%* | 38 · -0% | 48 · -5% | 49 · -7% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 29 · -34%* | 48 · -28% | 77 · -16% | 111 · -17% | 129 · -8% | 20 · -33%* |
| H6 | 35 · -3% | 60 · -5% | 88 · -9% | 132 · -9% | 153 · -8% | 19 · -29%* |
| D | 34 · -10% | 59 · -3% | 92 · -3% | 133 · -7% | 159 · -7% | 13 · -26%* |
| L | 29 · -28%* | 60 · -11% | 88 · -9% | 115 · -4% | 143 · -8% | 26 · -42%* |
| D+conf | 3 · -100%* | 8 · -29%* | 14 · -4%* | 27 · -7%* | 34 · -10% | 1 · -100%* |
| D+fade | 14 · -4%* | 21 · -0%* | 35 · -2% | 44 · -10% | 45 · -12% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 25 · -48%* | 46 · -27% | 68 · -32% | 108 · -31% | 132 · -33% | 17 · +22%* |
| H6 | 32 · -58% | 62 · -31% | 84 · -31% | 134 · -23% | 149 · -23% | 23 · -12%* |
| D | 32 · -50% | 62 · -29% | 89 · -21% | 128 · -21% | 151 · -20% | 21 · -54%* |
| L | 38 · -50% | 60 · -32% | 87 · -19% | 123 · -13% | 143 · -19% | 25 · -23%* |
| D+conf | 2 · -100%* | 10 · -38%* | 16 · -19%* | 26 · -33%* | 32 · -21% | 5 · -74%* |
| D+fade | 22 · -49%* | 36 · -26% | 45 · -41% | 57 · -36% | 58 · -37% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 29 · -52%* | 50 · -43% | 73 · -33% | 112 · -30% | 126 · -27% | 23 · -40%* |
| H6 | 38 · -60% | 65 · -27% | 97 · -21% | 134 · -27% | 153 · -21% | 19 · -42%* |
| D | 33 · -57% | 60 · -40% | 93 · -21% | 137 · -21% | 151 · -18% | 21 · -39%* |
| L | 35 · -36% | 56 · -43% | 87 · -36% | 122 · -24% | 144 · -26% | 24 · +29%* |
| D+conf | 1 · -100%* | 5 · -72%* | 15 · -42%* | 25 · -48%* | 28 · -30%* | 9 · -52%* |
| D+fade | 24 · -81%* | 33 · -51% | 45 · -39% | 57 · -35% | 57 · -35% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · -15%* | 47 · -7% | 61 · -6% | 87 · -10% | 120 · -3% | 29 · -27%* |
| H6 | 15 · -36%* | 47 · -19% | 74 · -15% | 92 · -7% | 124 · -6% | 48 · -4% |
| D | 13 · -56%* | 46 · -13% | 74 · -7% | 101 · -9% | 132 · -5% | 40 · +5% |
| L | 14 · -45%* | 49 · -10% | 72 · -2% | 103 · -7% | 127 · -1% | 42 · -19% |
| D+conf | 2 · -4%* | 10 · +14%* | 21 · +9%* | 30 · +15% | 38 · +21% | 16 · +19%* |
| D+fade | 7 · -73%* | 19 · -40%* | 31 · -20% | 38 · -20% | 41 · -16% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 111. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.254 (n=71) | +0.000 (n=89) | +0.011 (n=92) | -0.048 (n=84) | -0.067 (n=15) | -0.079 (n=38) |
| spread · B | +0.221 (n=77) | -0.136 (n=88) | -0.022 (n=92) | -0.011 (n=88) | -0.214 (n=14) | -0.057 (n=35) |
| ml · A | +0.002 (n=68) | -0.002 (n=84) | -0.001 (n=89) | +0.001 (n=87) | +0.002 (n=16) | -0.002 (n=45) |
| ml · B | -0.003 (n=73) | -0.004 (n=97) | -0.003 (n=93) | -0.000 (n=87) | -0.006 (n=15) | -0.003 (n=45) |
| total · T | +1.344 (n=61) | +0.405 (n=74) | +0.041 (n=74) | -0.028 (n=72) | -0.143 (n=21) | +0.032 (n=31) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 149 | -0.761 (-1.78) | – | – | – |
| spread · A · D | 172 | -0.401 (-1.11) | – | – | – |
| spread · B · E | 149 | -0.908 (-2.34) | – | – | – |
| spread · B · D | 172 | -0.535 (-1.44) | – | – | – |
| ml · A · E | 149 | – | 0.2077 | 0.1923 | +0.0154 (3.00) |
| ml · A · D | 172 | – | 0.2045 | 0.1910 | +0.0136 (2.48) |
| ml · B · E | 149 | – | 0.2098 | 0.1923 | +0.0175 (3.04) |
| ml · B · D | 172 | – | 0.2053 | 0.1910 | +0.0143 (2.62) |
| total · T · E | 149 | +0.338 (0.87) | – | – | – |
| total · T · D | 172 | -0.072 (-0.19) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._