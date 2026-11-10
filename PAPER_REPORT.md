# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **86** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 16 · +7%* | 32 · -4% | 45 · -11% | 60 · -23% | 66 · -19% | 12 · +28%* |
| H6 | 17 · -44%* | 32 · -17% | 48 · -8% | 64 · -8% | 73 · -6% | 13 · -26%* |
| D | 20 · -33%* | 32 · +1% | 47 · +2% | 64 · +1% | 78 · +3% | 8 · -5%* |
| L | 21 · -36%* | 34 · -10% | 47 · +2% | 63 · +9% | 74 · +3% | 12 · -68%* |
| D+conf | 1 · -100%* | 4 · -4%* | 7 · +39%* | 11 · +6%* | 12 · -3%* | 2 · -100%* |
| D+fade | 15 · -24%* | 19 · +0%* | 23 · +7%* | 28 · +8%* | 28 · +8%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 16 · -52%* | 27 · -36%* | 43 · -16% | 57 · -16% | 66 · -5% | 12 · -52%* |
| H6 | 19 · -30%* | 30 · -11% | 42 · -19% | 70 · -13% | 78 · -10% | 8 · -52%* |
| D | 20 · -33%* | 34 · -15% | 46 · -4% | 70 · -7% | 78 · -4% | 8 · -28%* |
| L | 19 · -50%* | 34 · -27% | 45 · -24% | 60 · -20% | 72 · -18% | 14 · -59%* |
| D+conf | 2 · -100%* | 5 · -61%* | 7 · -17%* | 16 · -15%* | 16 · -15%* | – |
| D+fade | 10 · -4%* | 15 · +2%* | 21 · +18%* | 26 · +10%* | 27 · +6%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 20 · -35%* | 32 · -32% | 42 · -23% | 61 · -20% | 72 · -22% | 6 · +14%* |
| H6 | 21 · -82%* | 37 · -36% | 47 · -34% | 67 · -18% | 71 · -16% | 15 · +5%* |
| D | 19 · -81%* | 36 · -38% | 45 · -24% | 64 · -11% | 75 · -9% | 11 · -37%* |
| L | 24 · -64%* | 36 · -36% | 47 · -25% | 64 · -4% | 73 · -12% | 13 · -11%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 13 · +9%* | 16 · +23%* | 3 · -56%* |
| D+fade | 16 · -77%* | 23 · -36%* | 25 · -42%* | 29 · -27%* | 30 · -29% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 17 · -56%* | 30 · -54% | 39 · -44% | 58 · -36% | 66 · -31% | 12 · -12%* |
| H6 | 21 · -69%* | 31 · -53% | 50 · -37% | 70 · -37% | 79 · -32% | 7 · -10%* |
| D | 20 · -60%* | 34 · -61% | 52 · -38% | 73 · -31% | 82 · -29% | 4 · +3%* |
| L | 22 · -57%* | 33 · -62% | 47 · -59% | 65 · -39% | 76 · -38% | 10 · +28%* |
| D+conf | 1 · -100%* | 4 · -100%* | 11 · -46%* | 15 · -51%* | 16 · -44%* | – |
| D+fade | 14 · -68%* | 19 · -64%* | 25 · -50%* | 30 · -38% | 30 · -38% | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 9 · +6%* | 28 · +2%* | 33 · +4% | 48 · -9% | 66 · -8% | 12 · -4%* |
| H6 | 8 · -5%* | 27 · -16%* | 42 · -5% | 49 · +1% | 62 · -5% | 24 · -36%* |
| D | 7 · -46%* | 24 · -12%* | 39 · +3% | 54 · -1% | 69 · -3% | 17 · +1%* |
| L | 5 · -62%* | 27 · -15%* | 41 · -2% | 58 · -4% | 63 · -3% | 23 · -9%* |
| D+conf | 2 · -4%* | 5 · -23%* | 9 · +28%* | 14 · +23%* | 18 · +18%* | 9 · +27%* |
| D+fade | 4 · -53%* | 12 · -21%* | 20 · -5%* | 25 · -9%* | 26 · -12%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 78. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | -0.156 (n=45) | -0.271 (n=48) | -0.191 (n=47) | -0.043 (n=47) | -0.286 (n=7) | -0.217 (n=23) |
| spread · B | +0.047 (n=43) | -0.214 (n=42) | -0.065 (n=46) | +0.067 (n=45) | +0.143 (n=7) | -0.095 (n=21) |
| ml · A | -0.004 (n=42) | -0.004 (n=47) | -0.001 (n=45) | +0.000 (n=47) | +0.000 (n=10) | -0.004 (n=25) |
| ml · B | -0.000 (n=39) | -0.003 (n=50) | -0.002 (n=52) | +0.000 (n=47) | -0.001 (n=11) | -0.002 (n=25) |
| total · T | +1.606 (n=33) | +0.548 (n=42) | +0.128 (n=39) | -0.146 (n=41) | +0.000 (n=9) | +0.100 (n=20) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 78 | -0.851 (-1.62) | – | – | – |
| spread · A · D | 86 | -0.513 (-1.09) | – | – | – |
| spread · B · E | 78 | -1.349 (-2.79) | – | – | – |
| spread · B · D | 86 | -0.953 (-1.91) | – | – | – |
| ml · A · E | 78 | – | 0.1954 | 0.1802 | +0.0152 (1.86) |
| ml · A · D | 86 | – | 0.1979 | 0.1835 | +0.0144 (1.75) |
| ml · B · E | 78 | – | 0.2041 | 0.1802 | +0.0239 (2.80) |
| ml · B · D | 86 | – | 0.2041 | 0.1835 | +0.0205 (2.58) |
| total · T · E | 78 | +0.413 (0.74) | – | – | – |
| total · T · D | 86 | +0.092 (0.17) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._