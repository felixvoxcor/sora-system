# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **63** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 12 · -5%* | 21 · -0%* | 29 · -1%* | 39 · -12% | 45 · -7% | 10 · +34%* |
| H6 | 11 · -48%* | 20 · -5%* | 31 · -8% | 46 · -5% | 53 · +1% | 10 · -24%* |
| D | 12 · -21%* | 21 · +9%* | 29 · -1%* | 44 · +4% | 56 · +6% | 7 · -19%* |
| L | 12 · -36%* | 20 · -13%* | 29 · -0%* | 43 · +15% | 53 · +8% | 10 · -81%* |
| D+conf | 1 · -100%* | 4 · -4%* | 6 · +29%* | 9 · +8%* | 10 · -3%* | 2 · -100%* |
| D+fade | 8 · +19%* | 12 · +43%* | 14 · +36%* | 19 · +30%* | 19 · +30%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 13 · -41%* | 22 · -22%* | 34 · -10% | 43 · -11% | 49 · -3% | 6 · -67%* |
| H6 | 13 · -12%* | 20 · -5%* | 31 · -14% | 54 · -15% | 59 · -16% | 4 · -51%* |
| D | 13 · -26%* | 23 · -16%* | 34 · -4% | 51 · -10% | 58 · -8% | 5 · -23%* |
| L | 13 · -42%* | 24 · -28%* | 34 · -21% | 44 · -22% | 55 · -20% | 8 · -29%* |
| D+conf | 2 · -100%* | 5 · -61%* | 7 · -17%* | 14 · -31%* | 14 · -31%* | – |
| D+fade | 5 · +16%* | 9 · +28%* | 14 · +36%* | 18 · +27%* | 19 · +20%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 15 · -36%* | 23 · -33%* | 26 · -24%* | 40 · -17% | 50 · -19% | 5 · +36%* |
| H6 | 12 · -100%* | 24 · -36%* | 32 · -36% | 48 · -20% | 52 · -17% | 11 · +20%* |
| D | 10 · -100%* | 25 · -38%* | 30 · -31% | 46 · -12% | 54 · -13% | 9 · -36%* |
| L | 14 · -65%* | 23 · -39%* | 30 · -40% | 44 · -5% | 51 · -16% | 12 · -4%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 11 · +19%* | 12 · +34%* | 3 · -56%* |
| D+fade | 7 · -100%* | 12 · -36%* | 13 · -40%* | 17 · -15%* | 18 · -20%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 14 · -58%* | 24 · -62%* | 31 · -45% | 45 · -34% | 49 · -28% | 6 · +42%* |
| H6 | 13 · -63%* | 22 · -50%* | 38 · -39% | 53 · -40% | 59 · -38% | 4 · +29%* |
| D | 12 · -60%* | 24 · -58%* | 37 · -44% | 54 · -36% | 61 · -36% | 2 · -18%* |
| L | 14 · -52%* | 24 · -60%* | 36 · -58% | 50 · -45% | 56 · -42% | 7 · +41%* |
| D+conf | 1 · -100%* | 4 · -100%* | 9 · -66%* | 13 · -66%* | 14 · -57%* | – |
| D+fade | 7 · -58%* | 10 · -48%* | 14 · -45%* | 18 · -23%* | 18 · -23%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 7 · +37%* | 20 · +14%* | 24 · +19%* | 32 · -11% | 47 · -11% | 8 · -4%* |
| H6 | 7 · +9%* | 20 · -5%* | 30 · +8% | 37 · +13% | 47 · +1% | 16 · -52%* |
| D | 5 · -24%* | 19 · +1%* | 29 · +6%* | 42 · +5% | 51 · -3% | 12 · -5%* |
| L | 3 · -37%* | 20 · -4%* | 32 · +1% | 44 · -0% | 49 · +1% | 14 · -19%* |
| D+conf | 2 · -4%* | 4 · -4%* | 7 · +37%* | 11 · +40%* | 14 · +24%* | 4 · +43%* |
| D+fade | 3 · -38%* | 9 · -15%* | 15 · -11%* | 19 · -10%* | 20 · -14%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 54. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.103 (n=29) | -0.161 (n=31) | +0.000 (n=29) | -0.069 (n=29) | -0.333 (n=6) | +0.071 (n=14) |
| spread · B | +0.235 (n=34) | +0.032 (n=31) | +0.000 (n=34) | +0.088 (n=34) | +0.143 (n=7) | +0.000 (n=14) |
| ml · A | -0.001 (n=26) | -0.003 (n=32) | +0.002 (n=30) | +0.000 (n=30) | +0.000 (n=10) | +0.001 (n=13) |
| ml · B | +0.007 (n=31) | +0.003 (n=38) | +0.001 (n=37) | -0.000 (n=36) | +0.002 (n=9) | +0.001 (n=14) |
| total · T | +1.333 (n=24) | +0.433 (n=30) | +0.000 (n=29) | -0.188 (n=32) | +0.000 (n=7) | -0.067 (n=15) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 55 | -0.447 (-0.74) | – | – | – |
| spread · A · D | 63 | -0.265 (-0.48) | – | – | – |
| spread · B · E | 55 | -0.780 (-1.43) | – | – | – |
| spread · B · D | 63 | -0.625 (-1.11) | – | – | – |
| ml · A · E | 55 | – | 0.2039 | 0.1886 | +0.0154 (1.56) |
| ml · A · D | 63 | – | 0.2063 | 0.1914 | +0.0150 (1.67) |
| ml · B · E | 55 | – | 0.2172 | 0.1886 | +0.0286 (2.58) |
| ml · B · D | 63 | – | 0.2157 | 0.1914 | +0.0244 (2.50) |
| total · T · E | 55 | +0.302 (0.40) | – | – | – |
| total · T · D | 63 | -0.115 (-0.17) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._