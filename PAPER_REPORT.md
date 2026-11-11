# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **89** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 16 · +7%* | 32 · -4% | 46 · -13% | 62 · -23% | 69 · -17% | 12 · +28%* |
| H6 | 17 · -44%* | 32 · -17% | 48 · -8% | 66 · -11% | 76 · -7% | 13 · -26%* |
| D | 20 · -33%* | 32 · +1% | 47 · +2% | 66 · -2% | 81 · +1% | 8 · -5%* |
| L | 21 · -36%* | 34 · -10% | 47 · +2% | 65 · +6% | 77 · +2% | 12 · -68%* |
| D+conf | 1 · -100%* | 4 · -4%* | 7 · +39%* | 12 · -3%* | 13 · -10%* | 2 · -100%* |
| D+fade | 15 · -24%* | 19 · +0%* | 23 · +7%* | 28 · +8%* | 28 · +8%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 16 · -52%* | 27 · -36%* | 44 · -13% | 59 · -16% | 69 · -3% | 12 · -52%* |
| H6 | 19 · -30%* | 30 · -11% | 42 · -19% | 70 · -13% | 79 · -8% | 10 · -61%* |
| D | 20 · -33%* | 34 · -15% | 46 · -4% | 70 · -7% | 80 · -2% | 9 · -36%* |
| L | 19 · -50%* | 34 · -27% | 45 · -24% | 60 · -20% | 73 · -16% | 16 · -53%* |
| D+conf | 2 · -100%* | 5 · -61%* | 7 · -17%* | 16 · -15%* | 16 · -15%* | – |
| D+fade | 10 · -4%* | 15 · +2%* | 21 · +18%* | 26 · +10%* | 27 · +6%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 20 · -35%* | 32 · -32% | 42 · -23% | 62 · -22% | 74 · -24% | 7 · +25%* |
| H6 | 21 · -82%* | 37 · -36% | 47 · -34% | 68 · -19% | 72 · -17% | 17 · -1%* |
| D | 19 · -81%* | 36 · -38% | 46 · -25% | 65 · -12% | 76 · -10% | 13 · -38%* |
| L | 24 · -64%* | 36 · -36% | 48 · -27% | 65 · -5% | 75 · -14% | 14 · -17%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 13 · +9%* | 16 · +23%* | 3 · -56%* |
| D+fade | 16 · -77%* | 23 · -36%* | 25 · -42%* | 29 · -27%* | 30 · -29% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 17 · -56%* | 30 · -54% | 39 · -44% | 59 · -34% | 68 · -30% | 13 · -19%* |
| H6 | 21 · -69%* | 31 · -53% | 50 · -37% | 70 · -37% | 80 · -30% | 9 · -18%* |
| D | 20 · -60%* | 34 · -61% | 52 · -38% | 73 · -31% | 83 · -28% | 6 · +13%* |
| L | 22 · -57%* | 33 · -62% | 47 · -59% | 65 · -39% | 77 · -39% | 12 · +35%* |
| D+conf | 1 · -100%* | 4 · -100%* | 11 · -46%* | 15 · -51%* | 17 · -37%* | – |
| D+fade | 14 · -68%* | 19 · -64%* | 25 · -50%* | 30 · -38% | 30 · -38% | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 9 · +6%* | 28 · +2%* | 33 · +4% | 48 · -9% | 67 · -6% | 14 · +10%* |
| H6 | 8 · -5%* | 27 · -16%* | 42 · -5% | 49 · +1% | 64 · -2% | 25 · -38%* |
| D | 7 · -46%* | 24 · -12%* | 39 · +3% | 55 · +1% | 71 · -0% | 18 · -5%* |
| L | 5 · -62%* | 27 · -15%* | 41 · -2% | 58 · -4% | 65 · -0% | 24 · -13%* |
| D+conf | 2 · -4%* | 5 · -23%* | 9 · +28%* | 14 · +23%* | 18 · +18%* | 9 · +27%* |
| D+fade | 4 · -53%* | 12 · -21%* | 20 · -5%* | 26 · -5%* | 28 · -5%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 78. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | -0.130 (n=46) | -0.271 (n=48) | -0.191 (n=47) | -0.043 (n=47) | -0.286 (n=7) | -0.217 (n=23) |
| spread · B | +0.114 (n=44) | -0.214 (n=42) | -0.065 (n=46) | +0.067 (n=45) | +0.143 (n=7) | -0.095 (n=21) |
| ml · A | -0.004 (n=42) | -0.004 (n=47) | -0.001 (n=46) | +0.000 (n=48) | +0.000 (n=10) | -0.004 (n=25) |
| ml · B | -0.000 (n=39) | -0.003 (n=50) | -0.002 (n=52) | +0.000 (n=47) | -0.001 (n=11) | -0.002 (n=25) |
| total · T | +1.606 (n=33) | +0.548 (n=42) | +0.128 (n=39) | -0.146 (n=41) | +0.000 (n=9) | +0.100 (n=20) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 81 | -0.827 (-1.57) | – | – | – |
| spread · A · D | 89 | -0.579 (-1.22) | – | – | – |
| spread · B · E | 81 | -1.258 (-2.56) | – | – | – |
| spread · B · D | 89 | -0.949 (-1.88) | – | – | – |
| ml · A · E | 81 | – | 0.1938 | 0.1787 | +0.0151 (1.91) |
| ml · A · D | 89 | – | 0.1964 | 0.1819 | +0.0145 (1.83) |
| ml · B · E | 81 | – | 0.2014 | 0.1787 | +0.0227 (2.75) |
| ml · B · D | 89 | – | 0.2014 | 0.1819 | +0.0195 (2.53) |
| total · T · E | 81 | +0.452 (0.82) | – | – | – |
| total · T · D | 89 | +0.172 (0.32) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._