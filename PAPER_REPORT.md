# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **88** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 16 · +7%* | 32 · -4% | 45 · -11% | 61 · -22% | 68 · -16% | 12 · +28%* |
| H6 | 17 · -44%* | 32 · -17% | 48 · -8% | 65 · -9% | 75 · -6% | 13 · -26%* |
| D | 20 · -33%* | 32 · +1% | 47 · +2% | 65 · -0% | 80 · +3% | 8 · -5%* |
| L | 21 · -36%* | 34 · -10% | 47 · +2% | 64 · +7% | 76 · +3% | 12 · -68%* |
| D+conf | 1 · -100%* | 4 · -4%* | 7 · +39%* | 11 · +6%* | 12 · -3%* | 2 · -100%* |
| D+fade | 15 · -24%* | 19 · +0%* | 23 · +7%* | 28 · +8%* | 28 · +8%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 16 · -52%* | 27 · -36%* | 44 · -13% | 58 · -14% | 68 · -2% | 12 · -52%* |
| H6 | 19 · -30%* | 30 · -11% | 42 · -19% | 70 · -13% | 79 · -8% | 9 · -57%* |
| D | 20 · -33%* | 34 · -15% | 46 · -4% | 70 · -7% | 79 · -3% | 9 · -36%* |
| L | 19 · -50%* | 34 · -27% | 45 · -24% | 60 · -20% | 72 · -18% | 16 · -53%* |
| D+conf | 2 · -100%* | 5 · -61%* | 7 · -17%* | 16 · -15%* | 16 · -15%* | – |
| D+fade | 10 · -4%* | 15 · +2%* | 21 · +18%* | 26 · +10%* | 27 · +6%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 20 · -35%* | 32 · -32% | 42 · -23% | 61 · -20% | 73 · -23% | 7 · +25%* |
| H6 | 21 · -82%* | 37 · -36% | 47 · -34% | 67 · -18% | 71 · -16% | 17 · -1%* |
| D | 19 · -81%* | 36 · -38% | 45 · -24% | 64 · -11% | 75 · -9% | 13 · -38%* |
| L | 24 · -64%* | 36 · -36% | 47 · -25% | 64 · -4% | 74 · -13% | 14 · -17%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 13 · +9%* | 16 · +23%* | 3 · -56%* |
| D+fade | 16 · -77%* | 23 · -36%* | 25 · -42%* | 29 · -27%* | 30 · -29% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 17 · -56%* | 30 · -54% | 39 · -44% | 59 · -34% | 68 · -30% | 12 · -12%* |
| H6 | 21 · -69%* | 31 · -53% | 50 · -37% | 70 · -37% | 80 · -30% | 8 · -8%* |
| D | 20 · -60%* | 34 · -61% | 52 · -38% | 73 · -31% | 83 · -28% | 5 · +4%* |
| L | 22 · -57%* | 33 · -62% | 47 · -59% | 65 · -39% | 77 · -39% | 11 · +33%* |
| D+conf | 1 · -100%* | 4 · -100%* | 11 · -46%* | 15 · -51%* | 17 · -37%* | – |
| D+fade | 14 · -68%* | 19 · -64%* | 25 · -50%* | 30 · -38% | 30 · -38% | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 9 · +6%* | 28 · +2%* | 33 · +4% | 48 · -9% | 67 · -6% | 13 · +4%* |
| H6 | 8 · -5%* | 27 · -16%* | 42 · -5% | 49 · +1% | 63 · -3% | 25 · -38%* |
| D | 7 · -46%* | 24 · -12%* | 39 · +3% | 55 · +1% | 70 · -2% | 18 · -5%* |
| L | 5 · -62%* | 27 · -15%* | 41 · -2% | 58 · -4% | 64 · -2% | 24 · -13%* |
| D+conf | 2 · -4%* | 5 · -23%* | 9 · +28%* | 14 · +23%* | 18 · +18%* | 9 · +27%* |
| D+fade | 4 · -53%* | 12 · -21%* | 20 · -5%* | 26 · -5%* | 27 · -8%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 78. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | -0.156 (n=45) | -0.271 (n=48) | -0.191 (n=47) | -0.043 (n=47) | -0.286 (n=7) | -0.217 (n=23) |
| spread · B | +0.114 (n=44) | -0.214 (n=42) | -0.065 (n=46) | +0.067 (n=45) | +0.143 (n=7) | -0.095 (n=21) |
| ml · A | -0.004 (n=42) | -0.004 (n=47) | -0.001 (n=45) | +0.000 (n=47) | +0.000 (n=10) | -0.004 (n=25) |
| ml · B | -0.000 (n=39) | -0.003 (n=50) | -0.002 (n=52) | +0.000 (n=47) | -0.001 (n=11) | -0.002 (n=25) |
| total · T | +1.606 (n=33) | +0.548 (n=42) | +0.128 (n=39) | -0.146 (n=41) | +0.000 (n=9) | +0.100 (n=20) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 80 | -0.751 (-1.41) | – | – | – |
| spread · A · D | 88 | -0.520 (-1.09) | – | – | – |
| spread · B · E | 80 | -1.218 (-2.48) | – | – | – |
| spread · B · D | 88 | -0.936 (-1.86) | – | – | – |
| ml · A · E | 80 | – | 0.1937 | 0.1789 | +0.0147 (1.84) |
| ml · A · D | 88 | – | 0.1963 | 0.1822 | +0.0141 (1.76) |
| ml · B · E | 80 | – | 0.2019 | 0.1789 | +0.0229 (2.74) |
| ml · B · D | 88 | – | 0.2020 | 0.1822 | +0.0198 (2.54) |
| total · T · E | 80 | +0.421 (0.77) | – | – | – |
| total · T · D | 88 | +0.133 (0.24) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._