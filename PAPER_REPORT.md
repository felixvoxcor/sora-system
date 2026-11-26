# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **200** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 23 · +8%* | 54 · +3% | 86 · -7% | 133 · -20% | 150 · -15% | 26 · -12%* |
| H6 | 28 · -12%* | 62 · -11% | 105 · -2% | 151 · -7% | 166 · -5% | 34 · -5% |
| D | 34 · -11% | 64 · -8% | 106 · -1% | 148 · -3% | 175 · -3% | 25 · +7%* |
| L | 35 · -18% | 68 · -10% | 99 · +0% | 142 · +5% | 164 · +1% | 33 · -24% |
| D+conf | 4 · -4%* | 10 · -4%* | 19 · +42%* | 27 · +28%* | 34 · +13% | 10 · -3%* |
| D+fade | 20 · -15%* | 32 · -11% | 45 · -3% | 55 · -7% | 56 · -9% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 34 · -21% | 58 · -14% | 89 · -6% | 135 · -9% | 155 · -4% | 21 · -37%* |
| H6 | 40 · +4% | 68 · +0% | 104 · -5% | 156 · -5% | 180 · -4% | 20 · -32%* |
| D | 38 · -4% | 67 · -0% | 108 · +2% | 156 · -3% | 184 · -4% | 16 · -28%* |
| L | 34 · -16% | 67 · -6% | 102 · -5% | 137 · +1% | 168 · -2% | 29 · -35%* |
| D+conf | 5 · -23%* | 11 · +4%* | 18 · +17%* | 32 · +8% | 40 · +5% | 2 · -100%* |
| D+fade | 16 · -4%* | 24 · -5%* | 42 · -5% | 53 · -11% | 54 · -12% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 30 · -30% | 53 · -19% | 83 · -16% | 130 · -15% | 157 · -17% | 19 · +20%* |
| H6 | 39 · -42% | 72 · -17% | 98 · -17% | 154 · -10% | 174 · -9% | 26 · +3%* |
| D | 38 · -44% | 72 · -24% | 103 · -14% | 149 · -6% | 177 · -7% | 23 · -58%* |
| L | 46 · -40% | 71 · -26% | 101 · -10% | 144 · +0% | 169 · -6% | 27 · -19%* |
| D+conf | 3 · +27%* | 13 · +17%* | 20 · +26%* | 31 · +14% | 39 · +15% | 5 · -74%* |
| D+fade | 26 · -51%* | 41 · -32% | 50 · -44% | 63 · -37% | 64 · -38% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 35 · -15% | 59 · -24% | 90 · -10% | 137 · -15% | 153 · -15% | 23 · -40%* |
| H6 | 43 · -34% | 75 · -14% | 116 · -8% | 160 · -12% | 179 · -9% | 21 · -39%* |
| D | 38 · -17% | 69 · -17% | 112 · -4% | 162 · -9% | 177 · -7% | 23 · -22%* |
| L | 40 · -1% | 64 · -17% | 104 · -17% | 145 · -13% | 171 · -14% | 25 · +39%* |
| D+conf | 2 · +91%* | 7 · -2%* | 18 · -12%* | 29 · -19%* | 32 · -6% | 11 · -14%* |
| D+fade | 26 · -69%* | 36 · -45% | 52 · -32% | 65 · -31% | 65 · -31% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 18 · -15%* | 54 · -12% | 71 · -11% | 100 · -14% | 137 · -7% | 39 · -31% |
| H6 | 17 · -33%* | 56 · -29% | 87 · -21% | 114 · -10% | 151 · -9% | 49 · -6% |
| D | 15 · -49%* | 57 · -23% | 87 · -14% | 121 · -15% | 155 · -8% | 45 · -3% |
| L | 17 · -32%* | 57 · -16% | 86 · -7% | 124 · -14% | 152 · -7% | 45 · -24% |
| D+conf | 2 · -4%* | 10 · +14%* | 21 · +9%* | 32 · +14% | 40 · +20% | 18 · +17%* |
| D+fade | 9 · -58%* | 30 · -49% | 42 · -32% | 52 · -34% | 56 · -29% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 121. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.221 (n=86) | +0.048 (n=105) | +0.028 (n=106) | -0.061 (n=99) | -0.158 (n=19) | -0.089 (n=45) |
| spread · B | +0.169 (n=89) | -0.029 (n=104) | +0.037 (n=108) | +0.029 (n=102) | -0.167 (n=18) | +0.048 (n=42) |
| ml · A | +0.001 (n=83) | -0.002 (n=98) | -0.000 (n=103) | +0.000 (n=101) | +0.002 (n=20) | -0.003 (n=50) |
| ml · B | -0.003 (n=90) | -0.003 (n=116) | -0.002 (n=112) | -0.001 (n=104) | -0.005 (n=18) | -0.001 (n=52) |
| total · T | +1.056 (n=71) | +0.368 (n=87) | +0.092 (n=87) | -0.023 (n=86) | -0.143 (n=21) | +0.167 (n=42) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 176 | -0.246 (-0.63) | – | – | – |
| spread · A · D | 200 | -0.103 (-0.31) | – | – | – |
| spread · B · E | 176 | -0.456 (-1.29) | – | – | – |
| spread · B · D | 200 | -0.219 (-0.65) | – | – | – |
| ml · A · E | 176 | – | 0.2119 | 0.2021 | +0.0098 (1.99) |
| ml · A · D | 200 | – | 0.2085 | 0.1994 | +0.0091 (1.78) |
| ml · B · E | 176 | – | 0.2107 | 0.2021 | +0.0087 (1.53) |
| ml · B · D | 200 | – | 0.2063 | 0.1994 | +0.0069 (1.31) |
| total · T · E | 176 | +0.062 (0.16) | – | – | – |
| total · T · D | 200 | -0.296 (-0.82) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._