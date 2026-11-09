# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **73** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 12 · -5%* | 24 · -5%* | 34 · -4% | 47 · -19% | 53 · -13% | 12 · +28%* |
| H6 | 13 · -56%* | 24 · -13%* | 36 · -10% | 51 · -7% | 60 · -5% | 13 · -26%* |
| D | 15 · -37%* | 26 · +2%* | 36 · +0% | 52 · +2% | 66 · +4% | 7 · -19%* |
| L | 16 · -40%* | 25 · -16%* | 36 · +1% | 51 · +12% | 62 · +5% | 11 · -83%* |
| D+conf | 1 · -100%* | 4 · -4%* | 6 · +29%* | 9 · +8%* | 10 · -3%* | 2 · -100%* |
| D+fade | 11 · -13%* | 15 · +14%* | 18 · +16%* | 23 · +15%* | 23 · +15%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 14 · -45%* | 23 · -25%* | 38 · -4% | 49 · -6% | 56 · +2% | 9 · -57%* |
| H6 | 14 · -18%* | 23 · -9%* | 34 · -16% | 62 · -11% | 68 · -10% | 5 · -61%* |
| D | 14 · -31%* | 26 · -19%* | 38 · -4% | 60 · -8% | 67 · -6% | 6 · -36%* |
| L | 14 · -46%* | 28 · -25%* | 39 · -22% | 52 · -19% | 63 · -18% | 10 · -43%* |
| D+conf | 2 · -100%* | 5 · -61%* | 7 · -17%* | 15 · -23%* | 15 · -23%* | – |
| D+fade | 6 · -4%* | 11 · +4%* | 17 · +23%* | 21 · +18%* | 22 · +12%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 15 · -36%* | 24 · -36%* | 32 · -24% | 49 · -20% | 59 · -21% | 6 · +14%* |
| H6 | 15 · -100%* | 29 · -36%* | 37 · -36% | 54 · -20% | 58 · -18% | 15 · +5%* |
| D | 14 · -100%* | 30 · -38% | 37 · -27% | 53 · -12% | 62 · -11% | 11 · -37%* |
| L | 18 · -73%* | 29 · -41%* | 37 · -34% | 52 · -5% | 60 · -15% | 13 · -11%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 11 · +19%* | 13 · +34%* | 3 · -56%* |
| D+fade | 11 · -100%* | 17 · -36%* | 19 · -43%* | 23 · -23%* | 24 · -27%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 14 · -58%* | 26 · -58%* | 33 · -43% | 51 · -32% | 57 · -27% | 8 · +7%* |
| H6 | 16 · -70%* | 25 · -56%* | 42 · -37% | 61 · -36% | 68 · -33% | 5 · +3%* |
| D | 14 · -66%* | 28 · -64%* | 43 · -40% | 64 · -31% | 71 · -32% | 2 · -18%* |
| L | 16 · -58%* | 27 · -64%* | 41 · -59% | 58 · -36% | 65 · -36% | 8 · +24%* |
| D+conf | 1 · -100%* | 4 · -100%* | 10 · -53%* | 14 · -57%* | 15 · -48%* | – |
| D+fade | 9 · -67%* | 14 · -63%* | 19 · -43%* | 24 · -29%* | 24 · -29%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 9 · +6%* | 24 · +3%* | 28 · +9%* | 38 · -15% | 55 · -14% | 10 · -23%* |
| H6 | 8 · -5%* | 23 · -9%* | 35 · -2% | 42 · +4% | 52 · -5% | 21 · -45%* |
| D | 6 · -37%* | 22 · -4%* | 34 · +7% | 49 · +1% | 59 · -3% | 14 · -5%* |
| L | 4 · -53%* | 24 · -5%* | 36 · +0% | 51 · -3% | 56 · -1% | 17 · -21%* |
| D+conf | 2 · -4%* | 5 · -23%* | 8 · +20%* | 13 · +18%* | 16 · +8%* | 6 · +27%* |
| D+fade | 3 · -38%* | 10 · -5%* | 17 · +1%* | 22 · -5%* | 23 · -9%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 60. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | -0.029 (n=34) | -0.167 (n=36) | -0.056 (n=36) | -0.083 (n=36) | -0.333 (n=6) | +0.000 (n=18) |
| spread · B | +0.211 (n=38) | +0.029 (n=34) | -0.026 (n=38) | +0.077 (n=39) | +0.143 (n=7) | -0.059 (n=17) |
| ml · A | -0.001 (n=32) | -0.003 (n=37) | +0.001 (n=37) | +0.000 (n=37) | +0.000 (n=10) | +0.000 (n=19) |
| ml · B | +0.007 (n=33) | +0.002 (n=42) | +0.001 (n=43) | +0.000 (n=41) | +0.002 (n=10) | +0.001 (n=19) |
| total · T | +1.321 (n=28) | +0.457 (n=35) | +0.029 (n=34) | -0.167 (n=36) | +0.000 (n=8) | +0.059 (n=17) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 65 | -0.581 (-1.03) | – | – | – |
| spread · A · D | 73 | -0.276 (-0.54) | – | – | – |
| spread · B · E | 65 | -0.818 (-1.58) | – | – | – |
| spread · B · D | 73 | -0.668 (-1.26) | – | – | – |
| ml · A · E | 65 | – | 0.2018 | 0.1861 | +0.0157 (1.80) |
| ml · A · D | 73 | – | 0.2043 | 0.1887 | +0.0156 (1.85) |
| ml · B · E | 65 | – | 0.2111 | 0.1861 | +0.0250 (2.58) |
| ml · B · D | 73 | – | 0.2113 | 0.1887 | +0.0226 (2.56) |
| total · T · E | 65 | -0.126 (-0.19) | – | – | – |
| total · T · D | 73 | -0.181 (-0.29) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._