# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **69** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 12 · -5%* | 22 · -5%* | 32 · -4% | 43 · -15% | 49 · -10% | 12 · +28%* |
| H6 | 13 · -56%* | 22 · -14%* | 34 · -10% | 49 · -7% | 58 · -5% | 11 · -31%* |
| D | 14 · -32%* | 23 · -1%* | 32 · -5% | 48 · -1% | 62 · +2% | 7 · -19%* |
| L | 14 · -45%* | 22 · -21%* | 32 · -4% | 47 · +10% | 58 · +2% | 11 · -83%* |
| D+conf | 1 · -100%* | 4 · -4%* | 6 · +29%* | 9 · +8%* | 10 · -3%* | 2 · -100%* |
| D+fade | 10 · -5%* | 14 · +22%* | 16 · +19%* | 21 · +17%* | 21 · +17%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 13 · -41%* | 22 · -22%* | 36 · -4% | 47 · -6% | 54 · +2% | 7 · -72%* |
| H6 | 14 · -18%* | 21 · -9%* | 32 · -17% | 59 · -13% | 64 · -14% | 5 · -61%* |
| D | 13 · -26%* | 24 · -20%* | 35 · -7% | 56 · -8% | 63 · -6% | 6 · -36%* |
| L | 13 · -42%* | 25 · -31%* | 35 · -24% | 48 · -20% | 59 · -19% | 10 · -43%* |
| D+conf | 2 · -100%* | 5 · -61%* | 7 · -17%* | 15 · -23%* | 15 · -23%* | – |
| D+fade | 5 · +16%* | 10 · +15%* | 15 · +27%* | 19 · +20%* | 20 · +14%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 15 · -36%* | 23 · -33%* | 29 · -17%* | 45 · -13% | 55 · -15% | 6 · +14%* |
| H6 | 13 · -100%* | 27 · -32%* | 35 · -32% | 52 · -17% | 56 · -15% | 13 · +2%* |
| D | 12 · -100%* | 28 · -33%* | 33 · -28% | 49 · -11% | 58 · -11% | 11 · -37%* |
| L | 16 · -69%* | 26 · -34%* | 33 · -36% | 48 · -3% | 56 · -15% | 13 · -11%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 11 · +19%* | 13 · +34%* | 3 · -56%* |
| D+fade | 9 · -100%* | 15 · -27%* | 16 · -32%* | 20 · -12%* | 21 · -16%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 14 · -58%* | 25 · -56%* | 32 · -41% | 49 · -30% | 54 · -23% | 7 · +22%* |
| H6 | 14 · -66%* | 23 · -53%* | 40 · -34% | 58 · -37% | 64 · -36% | 5 · +3%* |
| D | 12 · -60%* | 26 · -62%* | 41 · -37% | 60 · -34% | 67 · -35% | 2 · -18%* |
| L | 14 · -52%* | 25 · -61%* | 39 · -57% | 54 · -40% | 61 · -39% | 8 · +24%* |
| D+conf | 1 · -100%* | 4 · -100%* | 10 · -53%* | 14 · -57%* | 15 · -48%* | – |
| D+fade | 7 · -58%* | 12 · -57%* | 17 · -36%* | 22 · -22%* | 22 · -22%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 8 · +20%* | 22 · +4%* | 26 · +10%* | 34 · -16% | 51 · -14% | 10 · -23%* |
| H6 | 7 · +9%* | 21 · -9%* | 33 · -2% | 40 · +5% | 50 · -5% | 19 · -49%* |
| D | 5 · -24%* | 20 · -4%* | 30 · +2% | 45 · -2% | 55 · -6% | 14 · -5%* |
| L | 3 · -37%* | 21 · -9%* | 33 · -2% | 47 · -6% | 52 · -4% | 17 · -21%* |
| D+conf | 2 · -4%* | 5 · -23%* | 8 · +20%* | 13 · +18%* | 16 · +8%* | 6 · +27%* |
| D+fade | 3 · -38%* | 9 · -15%* | 15 · -11%* | 20 · -14%* | 21 · -18%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 58. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.000 (n=32) | -0.147 (n=34) | -0.031 (n=32) | -0.094 (n=32) | -0.333 (n=6) | +0.000 (n=16) |
| spread · B | +0.250 (n=36) | +0.062 (n=32) | +0.000 (n=35) | +0.086 (n=35) | +0.143 (n=7) | +0.000 (n=15) |
| ml · A | -0.003 (n=29) | -0.003 (n=35) | +0.002 (n=33) | +0.000 (n=33) | +0.000 (n=10) | +0.001 (n=16) |
| ml · B | +0.008 (n=32) | +0.003 (n=40) | +0.001 (n=41) | -0.000 (n=39) | +0.002 (n=10) | +0.001 (n=17) |
| total · T | +1.423 (n=26) | +0.455 (n=33) | +0.000 (n=30) | -0.182 (n=33) | +0.000 (n=8) | -0.067 (n=15) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 61 | -0.501 (-0.85) | – | – | – |
| spread · A · D | 69 | -0.309 (-0.58) | – | – | – |
| spread · B · E | 61 | -0.763 (-1.43) | – | – | – |
| spread · B · D | 69 | -0.695 (-1.27) | – | – | – |
| ml · A · E | 61 | – | 0.2008 | 0.1879 | +0.0129 (1.41) |
| ml · A · D | 69 | – | 0.2037 | 0.1890 | +0.0147 (1.71) |
| ml · B · E | 61 | – | 0.2123 | 0.1879 | +0.0244 (2.38) |
| ml · B · D | 69 | – | 0.2120 | 0.1890 | +0.0230 (2.52) |
| total · T · E | 61 | -0.192 (-0.28) | – | – | – |
| total · T · D | 69 | -0.393 (-0.60) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._