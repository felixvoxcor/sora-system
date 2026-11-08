# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **72** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 12 · -5%* | 24 · -5%* | 34 · -4% | 46 · -17% | 52 · -12% | 12 · +28%* |
| H6 | 13 · -56%* | 24 · -13%* | 36 · -10% | 51 · -7% | 60 · -5% | 12 · -37%* |
| D | 15 · -37%* | 25 · -1%* | 35 · -2% | 51 · +1% | 65 · +3% | 7 · -19%* |
| L | 15 · -48%* | 24 · -20%* | 35 · -1% | 50 · +11% | 61 · +3% | 11 · -83%* |
| D+conf | 1 · -100%* | 4 · -4%* | 6 · +29%* | 9 · +8%* | 10 · -3%* | 2 · -100%* |
| D+fade | 11 · -13%* | 15 · +14%* | 18 · +16%* | 23 · +15%* | 23 · +15%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 14 · -45%* | 23 · -25%* | 38 · -4% | 49 · -6% | 56 · +2% | 8 · -76%* |
| H6 | 14 · -18%* | 23 · -9%* | 34 · -16% | 61 · -12% | 67 · -12% | 5 · -61%* |
| D | 14 · -31%* | 26 · -19%* | 37 · -7% | 59 · -9% | 66 · -7% | 6 · -36%* |
| L | 14 · -46%* | 27 · -29%* | 38 · -25% | 51 · -21% | 62 · -20% | 10 · -43%* |
| D+conf | 2 · -100%* | 5 · -61%* | 7 · -17%* | 15 · -23%* | 15 · -23%* | – |
| D+fade | 6 · -4%* | 11 · +4%* | 16 · +19%* | 20 · +14%* | 21 · +9%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 15 · -36%* | 24 · -36%* | 31 · -22% | 48 · -18% | 58 · -19% | 6 · +14%* |
| H6 | 15 · -100%* | 29 · -36%* | 37 · -36% | 54 · -20% | 58 · -18% | 14 · -6%* |
| D | 14 · -100%* | 30 · -38% | 36 · -34% | 52 · -16% | 61 · -15% | 11 · -37%* |
| L | 18 · -73%* | 29 · -41%* | 36 · -41% | 51 · -9% | 59 · -19% | 13 · -11%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 11 · +19%* | 13 · +34%* | 3 · -56%* |
| D+fade | 11 · -100%* | 17 · -36%* | 19 · -43%* | 23 · -23%* | 24 · -27%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 14 · -58%* | 26 · -58%* | 33 · -43% | 51 · -32% | 56 · -26% | 8 · +7%* |
| H6 | 16 · -70%* | 25 · -56%* | 42 · -37% | 60 · -39% | 67 · -36% | 5 · +3%* |
| D | 14 · -66%* | 28 · -64%* | 43 · -40% | 63 · -35% | 70 · -36% | 2 · -18%* |
| L | 16 · -58%* | 27 · -64%* | 41 · -59% | 57 · -41% | 64 · -40% | 8 · +24%* |
| D+conf | 1 · -100%* | 4 · -100%* | 10 · -53%* | 14 · -57%* | 15 · -48%* | – |
| D+fade | 9 · -67%* | 14 · -63%* | 19 · -43%* | 24 · -29%* | 24 · -29%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 9 · +6%* | 24 · +3%* | 28 · +9%* | 37 · -13% | 54 · -12% | 10 · -23%* |
| H6 | 8 · -5%* | 23 · -9%* | 35 · -2% | 42 · +4% | 52 · -5% | 20 · -42%* |
| D | 6 · -37%* | 22 · -4%* | 33 · +4% | 48 · -1% | 58 · -5% | 14 · -5%* |
| L | 4 · -53%* | 23 · -9%* | 35 · -2% | 50 · -4% | 55 · -3% | 17 · -21%* |
| D+conf | 2 · -4%* | 5 · -23%* | 8 · +20%* | 13 · +18%* | 16 · +8%* | 6 · +27%* |
| D+fade | 3 · -38%* | 10 · -5%* | 17 · +1%* | 22 · -5%* | 23 · -9%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 60. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | -0.029 (n=34) | -0.167 (n=36) | -0.029 (n=35) | -0.086 (n=35) | -0.333 (n=6) | +0.000 (n=18) |
| spread · B | +0.211 (n=38) | +0.029 (n=34) | +0.000 (n=37) | +0.079 (n=38) | +0.143 (n=7) | +0.000 (n=16) |
| ml · A | -0.006 (n=31) | -0.003 (n=37) | +0.001 (n=36) | +0.000 (n=36) | +0.000 (n=10) | +0.000 (n=19) |
| ml · B | +0.007 (n=33) | +0.002 (n=42) | +0.001 (n=43) | +0.000 (n=41) | +0.002 (n=10) | +0.001 (n=19) |
| total · T | +1.321 (n=28) | +0.457 (n=35) | +0.061 (n=33) | -0.171 (n=35) | +0.000 (n=8) | +0.059 (n=17) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 64 | -0.566 (-0.99) | – | – | – |
| spread · A · D | 72 | -0.360 (-0.70) | – | – | – |
| spread · B · E | 64 | -0.831 (-1.60) | – | – | – |
| spread · B · D | 72 | -0.752 (-1.41) | – | – | – |
| ml · A · E | 64 | – | 0.1988 | 0.1843 | +0.0145 (1.65) |
| ml · A · D | 72 | – | 0.2017 | 0.1846 | +0.0171 (2.04) |
| ml · B · E | 64 | – | 0.2094 | 0.1843 | +0.0251 (2.54) |
| ml · B · D | 72 | – | 0.2085 | 0.1846 | +0.0239 (2.70) |
| total · T · E | 64 | -0.121 (-0.18) | – | – | – |
| total · T · D | 72 | -0.300 (-0.48) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._