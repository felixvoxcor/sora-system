# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **79** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 15 · +15%* | 29 · +5%* | 40 · +1% | 53 · -13% | 59 · -9% | 12 · +28%* |
| H6 | 16 · -41%* | 28 · -5%* | 41 · -2% | 57 · -3% | 66 · -2% | 13 · -26%* |
| D | 18 · -26%* | 30 · +8% | 41 · +7% | 58 · +5% | 72 · +6% | 7 · -19%* |
| L | 19 · -29%* | 29 · -7%* | 41 · +7% | 57 · +14% | 68 · +7% | 11 · -83%* |
| D+conf | 1 · -100%* | 4 · -4%* | 7 · +39%* | 11 · +6%* | 12 · -3%* | 2 · -100%* |
| D+fade | 13 · -12%* | 17 · +12%* | 20 · +14%* | 25 · +14%* | 25 · +14%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 14 · -45%* | 24 · -28%* | 39 · -7% | 51 · -6% | 60 · +5% | 11 · -47%* |
| H6 | 15 · -24%* | 25 · -9%* | 36 · -16% | 64 · -11% | 72 · -7% | 7 · -45%* |
| D | 16 · -28%* | 28 · -18%* | 40 · -4% | 63 · -6% | 71 · -3% | 8 · -28%* |
| L | 15 · -49%* | 30 · -24% | 41 · -21% | 54 · -19% | 66 · -16% | 13 · -56%* |
| D+conf | 2 · -100%* | 5 · -61%* | 7 · -17%* | 16 · -15%* | 16 · -15%* | – |
| D+fade | 8 · -4%* | 13 · +3%* | 19 · +20%* | 23 · +16%* | 24 · +11%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · -28%* | 28 · -28%* | 38 · -19% | 55 · -17% | 65 · -18% | 6 · +14%* |
| H6 | 18 · -79%* | 32 · -31% | 42 · -30% | 60 · -17% | 64 · -15% | 15 · +5%* |
| D | 17 · -78%* | 33 · -32% | 41 · -20% | 59 · -9% | 68 · -9% | 11 · -37%* |
| L | 21 · -58%* | 32 · -35% | 41 · -27% | 58 · -2% | 66 · -12% | 13 · -11%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 13 · +9%* | 15 · +24%* | 3 · -56%* |
| D+fade | 14 · -74%* | 20 · -27%* | 22 · -34%* | 26 · -18%* | 27 · -21%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 15 · -61%* | 27 · -60%* | 34 · -45% | 52 · -34% | 59 · -30% | 12 · -12%* |
| H6 | 18 · -73%* | 27 · -60%* | 44 · -40% | 63 · -38% | 72 · -32% | 7 · -10%* |
| D | 16 · -70%* | 30 · -67% | 45 · -43% | 66 · -33% | 75 · -31% | 4 · +3%* |
| L | 18 · -63%* | 29 · -67%* | 43 · -61% | 61 · -39% | 70 · -40% | 9 · +25%* |
| D+conf | 1 · -100%* | 4 · -100%* | 10 · -53%* | 14 · -57%* | 15 · -48%* | – |
| D+fade | 11 · -73%* | 16 · -68%* | 21 · -48%* | 26 · -34%* | 26 · -34%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 9 · +6%* | 26 · +3%* | 30 · +8% | 42 · -9% | 60 · -8% | 11 · -13%* |
| H6 | 8 · -5%* | 25 · -9%* | 38 · +0% | 45 · +6% | 55 · -3% | 24 · -36%* |
| D | 6 · -37%* | 23 · -8%* | 37 · +9% | 52 · +3% | 64 · -1% | 15 · +1%* |
| L | 4 · -53%* | 25 · -8%* | 39 · +3% | 55 · -3% | 60 · -1% | 19 · -10%* |
| D+conf | 2 · -4%* | 5 · -23%* | 9 · +28%* | 14 · +23%* | 17 · +13%* | 7 · +36%* |
| D+fade | 3 · -38%* | 11 · -13%* | 19 · +0%* | 24 · -5%* | 25 · -9%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 66. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | -0.050 (n=40) | -0.171 (n=41) | -0.049 (n=41) | -0.049 (n=41) | -0.286 (n=7) | +0.000 (n=20) |
| spread · B | +0.179 (n=39) | +0.000 (n=36) | -0.025 (n=40) | +0.073 (n=41) | +0.143 (n=7) | -0.053 (n=19) |
| ml · A | -0.004 (n=38) | -0.004 (n=42) | -0.000 (n=41) | -0.000 (n=41) | +0.000 (n=10) | -0.001 (n=22) |
| ml · B | +0.006 (n=34) | +0.001 (n=44) | +0.001 (n=45) | +0.000 (n=43) | +0.002 (n=10) | -0.000 (n=21) |
| total · T | +1.267 (n=30) | +0.447 (n=38) | +0.054 (n=37) | -0.154 (n=39) | +0.000 (n=9) | +0.105 (n=19) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 71 | -0.426 (-0.79) | – | – | – |
| spread · A · D | 79 | -0.158 (-0.33) | – | – | – |
| spread · B · E | 71 | -0.899 (-1.72) | – | – | – |
| spread · B · D | 79 | -0.704 (-1.34) | – | – | – |
| ml · A · E | 71 | – | 0.1976 | 0.1845 | +0.0131 (1.51) |
| ml · A · D | 79 | – | 0.2003 | 0.1869 | +0.0134 (1.57) |
| ml · B · E | 71 | – | 0.2083 | 0.1845 | +0.0238 (2.68) |
| ml · B · D | 79 | – | 0.2093 | 0.1869 | +0.0223 (2.72) |
| total · T · E | 71 | +0.298 (0.49) | – | – | – |
| total · T · D | 79 | +0.076 (0.13) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._