# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **90** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 17 · +12%* | 33 · -2% | 47 · -10% | 63 · -21% | 70 · -15% | 12 · +28%* |
| H6 | 18 · -37%* | 33 · -14% | 49 · -6% | 67 · -9% | 77 · -6% | 13 · -26%* |
| D | 21 · -27%* | 33 · +4% | 48 · +3% | 67 · -0% | 82 · +2% | 8 · -5%* |
| L | 22 · -30%* | 35 · -7% | 48 · +4% | 66 · +7% | 78 · +3% | 12 · -68%* |
| D+conf | 2 · -7%* | 5 · +14%* | 8 · +45%* | 13 · +4%* | 14 · -3%* | 2 · -100%* |
| D+fade | 15 · -24%* | 19 · +0%* | 23 · +7%* | 28 · +8%* | 28 · +8%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 16 · -52%* | 28 · -32%* | 45 · -11% | 60 · -14% | 70 · -2% | 12 · -52%* |
| H6 | 19 · -30%* | 30 · -11% | 42 · -19% | 70 · -13% | 80 · -7% | 10 · -61%* |
| D | 20 · -33%* | 34 · -15% | 46 · -4% | 70 · -7% | 81 · -1% | 9 · -36%* |
| L | 19 · -50%* | 34 · -27% | 45 · -24% | 60 · -20% | 74 · -17% | 16 · -53%* |
| D+conf | 2 · -100%* | 5 · -61%* | 7 · -17%* | 16 · -15%* | 17 · -9%* | – |
| D+fade | 10 · -4%* | 15 · +2%* | 21 · +18%* | 26 · +10%* | 27 · +6%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 21 · -38%* | 33 · -35% | 43 · -25% | 63 · -23% | 75 · -25% | 7 · +25%* |
| H6 | 22 · -83%* | 38 · -37% | 48 · -35% | 69 · -21% | 73 · -18% | 17 · -1%* |
| D | 20 · -82%* | 37 · -40% | 47 · -27% | 66 · -13% | 77 · -11% | 13 · -38%* |
| L | 25 · -65%* | 37 · -37% | 49 · -28% | 66 · -7% | 76 · -15% | 14 · -17%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 13 · +9%* | 16 · +23%* | 3 · -56%* |
| D+fade | 17 · -78%* | 24 · -39%* | 26 · -44%* | 30 · -29% | 31 · -31% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 17 · -56%* | 30 · -54% | 40 · -46% | 60 · -35% | 69 · -31% | 13 · -19%* |
| H6 | 21 · -69%* | 31 · -53% | 50 · -37% | 71 · -38% | 81 · -31% | 9 · -18%* |
| D | 20 · -60%* | 34 · -61% | 52 · -38% | 74 · -32% | 84 · -29% | 6 · +13%* |
| L | 22 · -57%* | 33 · -62% | 47 · -59% | 65 · -39% | 77 · -39% | 13 · +34%* |
| D+conf | 1 · -100%* | 4 · -100%* | 11 · -46%* | 15 · -51%* | 17 · -37%* | – |
| D+fade | 14 · -68%* | 19 · -64%* | 25 · -50%* | 31 · -40% | 31 · -40% | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 10 · -4%* | 29 · -1%* | 34 · +1% | 49 · -11% | 68 · -8% | 14 · +10%* |
| H6 | 9 · -15%* | 28 · -19%* | 43 · -7% | 50 · -1% | 65 · -3% | 25 · -38%* |
| D | 8 · -53%* | 25 · -16%* | 40 · +1% | 56 · -1% | 72 · -2% | 18 · -5%* |
| L | 6 · -69%* | 28 · -18%* | 42 · -5% | 59 · -6% | 66 · -2% | 24 · -13%* |
| D+conf | 2 · -4%* | 5 · -23%* | 9 · +28%* | 14 · +23%* | 18 · +18%* | 9 · +27%* |
| D+fade | 4 · -53%* | 12 · -21%* | 20 · -5%* | 26 · -5%* | 28 · -5%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 79. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | -0.085 (n=47) | -0.245 (n=49) | -0.167 (n=48) | -0.042 (n=48) | -0.125 (n=8) | -0.217 (n=23) |
| spread · B | +0.156 (n=45) | -0.214 (n=42) | -0.065 (n=46) | +0.067 (n=45) | +0.143 (n=7) | -0.095 (n=21) |
| ml · A | -0.004 (n=43) | -0.003 (n=48) | -0.001 (n=47) | +0.000 (n=49) | +0.000 (n=10) | -0.003 (n=26) |
| ml · B | -0.000 (n=40) | -0.003 (n=50) | -0.002 (n=52) | +0.000 (n=47) | -0.001 (n=11) | -0.002 (n=25) |
| total · T | +1.559 (n=34) | +0.535 (n=43) | +0.125 (n=40) | -0.143 (n=42) | +0.000 (n=9) | +0.100 (n=20) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 82 | -0.753 (-1.47) | – | – | – |
| spread · A · D | 90 | -0.549 (-1.18) | – | – | – |
| spread · B · E | 82 | -1.235 (-2.54) | – | – | – |
| spread · B · D | 90 | -0.950 (-1.89) | – | – | – |
| ml · A · E | 82 | – | 0.1935 | 0.1773 | +0.0162 (2.05) |
| ml · A · D | 90 | – | 0.1961 | 0.1804 | +0.0156 (1.97) |
| ml · B · E | 82 | – | 0.2001 | 0.1773 | +0.0228 (2.80) |
| ml · B · D | 90 | – | 0.1999 | 0.1804 | +0.0195 (2.56) |
| total · T · E | 82 | +0.400 (0.77) | – | – | – |
| total · T · D | 90 | +0.142 (0.27) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._