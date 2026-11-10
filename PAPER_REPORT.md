# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **82** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 15 · +15%* | 30 · +2% | 41 · -2% | 56 · -18% | 62 · -14% | 12 · +28%* |
| H6 | 17 · -44%* | 29 · -8%* | 44 · -0% | 60 · -2% | 69 · -0% | 13 · -26%* |
| D | 19 · -30%* | 31 · +4% | 44 · +8% | 61 · +6% | 75 · +7% | 7 · -19%* |
| L | 20 · -33%* | 32 · -4% | 44 · +9% | 60 · +15% | 71 · +8% | 11 · -83%* |
| D+conf | 1 · -100%* | 4 · -4%* | 7 · +39%* | 11 · +6%* | 12 · -3%* | 2 · -100%* |
| D+fade | 14 · -19%* | 18 · +6%* | 22 · +12%* | 27 · +12%* | 27 · +12%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 14 · -45%* | 24 · -28%* | 40 · -9% | 54 · -11% | 63 · -0% | 11 · -47%* |
| H6 | 16 · -17%* | 27 · -1%* | 39 · -12% | 67 · -9% | 75 · -6% | 7 · -45%* |
| D | 17 · -21%* | 30 · -11% | 42 · +0% | 66 · -4% | 74 · -2% | 8 · -28%* |
| L | 16 · -40%* | 31 · -20% | 42 · -18% | 57 · -16% | 69 · -14% | 13 · -56%* |
| D+conf | 2 · -100%* | 5 · -61%* | 7 · -17%* | 16 · -15%* | 16 · -15%* | – |
| D+fade | 9 · +7%* | 14 · +9%* | 20 · +24%* | 25 · +14%* | 26 · +10%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 19 · -32%* | 29 · -31%* | 39 · -21% | 57 · -17% | 68 · -20% | 6 · +14%* |
| H6 | 19 · -81%* | 33 · -33% | 43 · -31% | 63 · -16% | 67 · -14% | 15 · +5%* |
| D | 18 · -79%* | 34 · -34% | 42 · -22% | 61 · -9% | 71 · -8% | 11 · -37%* |
| L | 22 · -60%* | 34 · -32% | 44 · -24% | 61 · -2% | 69 · -11% | 13 · -11%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 13 · +9%* | 16 · +23%* | 3 · -56%* |
| D+fade | 15 · -75%* | 21 · -30%* | 23 · -36%* | 27 · -21%* | 28 · -24%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 15 · -61%* | 28 · -57%* | 36 · -44% | 55 · -35% | 62 · -31% | 12 · -12%* |
| H6 | 18 · -73%* | 28 · -54%* | 47 · -37% | 66 · -36% | 75 · -30% | 7 · -10%* |
| D | 16 · -70%* | 30 · -67% | 48 · -40% | 69 · -31% | 78 · -30% | 4 · +3%* |
| L | 19 · -58%* | 30 · -64% | 44 · -59% | 62 · -38% | 73 · -38% | 9 · +25%* |
| D+conf | 1 · -100%* | 4 · -100%* | 11 · -46%* | 15 · -51%* | 16 · -44%* | – |
| D+fade | 11 · -73%* | 16 · -68%* | 22 · -51%* | 27 · -37%* | 27 · -37%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 9 · +6%* | 26 · +3%* | 31 · +4% | 44 · -9% | 62 · -8% | 12 · -4%* |
| H6 | 8 · -5%* | 26 · -12%* | 40 · -0% | 47 · +5% | 58 · -5% | 24 · -36%* |
| D | 6 · -37%* | 23 · -8%* | 38 · +6% | 53 · +1% | 67 · -3% | 15 · +1%* |
| L | 4 · -53%* | 26 · -12%* | 40 · +0% | 57 · -3% | 62 · -1% | 20 · -14%* |
| D+conf | 2 · -4%* | 5 · -23%* | 9 · +28%* | 14 · +23%* | 18 · +18%* | 7 · +36%* |
| D+fade | 3 · -38%* | 11 · -13%* | 19 · +0%* | 24 · -5%* | 25 · -9%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 70. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | -0.171 (n=41) | -0.295 (n=44) | -0.182 (n=44) | -0.045 (n=44) | -0.286 (n=7) | -0.227 (n=22) |
| spread · B | +0.125 (n=40) | -0.154 (n=39) | -0.071 (n=42) | +0.071 (n=42) | +0.143 (n=7) | -0.100 (n=20) |
| ml · A | -0.006 (n=39) | -0.006 (n=43) | -0.002 (n=42) | -0.000 (n=44) | +0.000 (n=10) | -0.004 (n=23) |
| ml · B | +0.002 (n=36) | -0.003 (n=47) | -0.003 (n=48) | +0.000 (n=44) | -0.001 (n=11) | -0.004 (n=22) |
| total · T | +1.323 (n=31) | +0.550 (n=40) | +0.132 (n=38) | -0.150 (n=40) | +0.000 (n=9) | +0.105 (n=19) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 74 | -0.502 (-0.94) | – | – | – |
| spread · A · D | 82 | -0.164 (-0.35) | – | – | – |
| spread · B · E | 74 | -0.915 (-1.76) | – | – | – |
| spread · B · D | 82 | -0.618 (-1.20) | – | – | – |
| ml · A · E | 74 | – | 0.1994 | 0.1847 | +0.0147 (1.72) |
| ml · A · D | 82 | – | 0.2019 | 0.1876 | +0.0143 (1.68) |
| ml · B · E | 74 | – | 0.2086 | 0.1847 | +0.0239 (2.78) |
| ml · B · D | 82 | – | 0.2091 | 0.1876 | +0.0215 (2.67) |
| total · T · E | 74 | +0.343 (0.58) | – | – | – |
| total · T · D | 82 | +0.087 (0.15) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._