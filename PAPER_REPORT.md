# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **68** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 12 · -5%* | 22 · -5%* | 31 · -8% | 42 · -18% | 48 · -12% | 12 · +28%* |
| H6 | 13 · -56%* | 22 · -14%* | 33 · -13% | 48 · -9% | 57 · -6% | 11 · -31%* |
| D | 14 · -32%* | 23 · -1%* | 31 · -8% | 47 · -3% | 61 · +0% | 7 · -19%* |
| L | 14 · -45%* | 22 · -21%* | 31 · -7% | 46 · +8% | 57 · +0% | 11 · -83%* |
| D+conf | 1 · -100%* | 4 · -4%* | 6 · +29%* | 9 · +8%* | 10 · -3%* | 2 · -100%* |
| D+fade | 10 · -5%* | 14 · +22%* | 16 · +19%* | 21 · +17%* | 21 · +17%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 13 · -41%* | 22 · -22%* | 36 · -4% | 46 · -9% | 53 · +1% | 7 · -72%* |
| H6 | 14 · -18%* | 21 · -9%* | 32 · -17% | 58 · -14% | 63 · -15% | 5 · -61%* |
| D | 13 · -26%* | 24 · -20%* | 35 · -7% | 55 · -10% | 62 · -7% | 6 · -36%* |
| L | 13 · -42%* | 25 · -31%* | 35 · -24% | 47 · -23% | 58 · -21% | 10 · -43%* |
| D+conf | 2 · -100%* | 5 · -61%* | 7 · -17%* | 15 · -23%* | 15 · -23%* | – |
| D+fade | 5 · +16%* | 10 · +15%* | 15 · +27%* | 19 · +20%* | 20 · +14%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 15 · -36%* | 23 · -33%* | 28 · -24%* | 44 · -18% | 54 · -19% | 6 · +14%* |
| H6 | 13 · -100%* | 26 · -41%* | 34 · -40% | 51 · -22% | 55 · -19% | 13 · +2%* |
| D | 12 · -100%* | 27 · -43%* | 32 · -35% | 48 · -16% | 57 · -15% | 11 · -37%* |
| L | 16 · -69%* | 25 · -44%* | 32 · -44% | 47 · -8% | 55 · -19% | 13 · -11%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 11 · +19%* | 13 · +34%* | 3 · -56%* |
| D+fade | 9 · -100%* | 14 · -45%* | 15 · -48%* | 19 · -24%* | 20 · -28%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 14 · -58%* | 25 · -56%* | 32 · -41% | 48 · -34% | 53 · -27% | 7 · +22%* |
| H6 | 14 · -66%* | 23 · -53%* | 39 · -40% | 57 · -41% | 63 · -40% | 5 · +3%* |
| D | 12 · -60%* | 26 · -62%* | 40 · -44% | 59 · -38% | 66 · -39% | 2 · -18%* |
| L | 14 · -52%* | 25 · -61%* | 39 · -57% | 53 · -45% | 60 · -43% | 8 · +24%* |
| D+conf | 1 · -100%* | 4 · -100%* | 10 · -53%* | 14 · -57%* | 15 · -48%* | – |
| D+fade | 7 · -58%* | 12 · -57%* | 16 · -52%* | 21 · -34%* | 21 · -34%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 8 · +20%* | 22 · +4%* | 26 · +10%* | 34 · -16% | 51 · -14% | 9 · -15%* |
| H6 | 7 · +9%* | 21 · -9%* | 33 · -2% | 40 · +5% | 50 · -5% | 18 · -57%* |
| D | 5 · -24%* | 20 · -4%* | 30 · +2% | 45 · -2% | 54 · -8% | 14 · -5%* |
| L | 3 · -37%* | 21 · -9%* | 33 · -2% | 47 · -6% | 52 · -4% | 16 · -29%* |
| D+conf | 2 · -4%* | 5 · -23%* | 8 · +20%* | 13 · +18%* | 16 · +8%* | 6 · +27%* |
| D+fade | 3 · -38%* | 9 · -15%* | 15 · -11%* | 20 · -14%* | 21 · -18%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 58. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.000 (n=31) | -0.152 (n=33) | -0.032 (n=31) | -0.097 (n=31) | -0.333 (n=6) | +0.000 (n=16) |
| spread · B | +0.250 (n=36) | +0.062 (n=32) | +0.000 (n=35) | +0.086 (n=35) | +0.143 (n=7) | +0.000 (n=15) |
| ml · A | -0.002 (n=28) | -0.003 (n=34) | +0.002 (n=32) | +0.000 (n=32) | +0.000 (n=10) | +0.001 (n=15) |
| ml · B | +0.008 (n=32) | +0.003 (n=39) | +0.001 (n=40) | -0.000 (n=39) | +0.002 (n=10) | +0.001 (n=16) |
| total · T | +1.423 (n=26) | +0.455 (n=33) | +0.000 (n=30) | -0.182 (n=33) | +0.000 (n=8) | -0.067 (n=15) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 60 | -0.542 (-0.91) | – | – | – |
| spread · A · D | 68 | -0.333 (-0.62) | – | – | – |
| spread · B · E | 60 | -0.778 (-1.45) | – | – | – |
| spread · B · D | 68 | -0.705 (-1.28) | – | – | – |
| ml · A · E | 60 | – | 0.1981 | 0.1833 | +0.0147 (1.61) |
| ml · A · D | 68 | – | 0.2013 | 0.1846 | +0.0167 (1.97) |
| ml · B · E | 60 | – | 0.2091 | 0.1833 | +0.0258 (2.49) |
| ml · B · D | 68 | – | 0.2092 | 0.1846 | +0.0246 (2.68) |
| total · T · E | 60 | -0.135 (-0.19) | – | – | – |
| total · T · D | 68 | -0.402 (-0.61) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._