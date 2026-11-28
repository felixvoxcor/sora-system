# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **213** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 25 · +7%* | 58 · +2% | 92 · -6% | 142 · -19% | 161 · -13% | 28 · -5%* |
| H6 | 30 · -18% | 65 · -12% | 111 · -2% | 163 · -8% | 179 · -6% | 34 · -5% |
| D | 37 · -13% | 69 · -9% | 112 · -1% | 156 · -5% | 187 · -4% | 26 · +3%* |
| L | 38 · -20% | 73 · -11% | 105 · -0% | 151 · +3% | 176 · -0% | 34 · -26% |
| D+conf | 5 · +14%* | 11 · +4%* | 20 · +45%* | 28 · +31%* | 36 · +12% | 10 · -3%* |
| D+fade | 21 · -19%* | 34 · -17% | 48 · -5% | 58 · -9% | 59 · -10% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 35 · -18% | 60 · -11% | 94 · -7% | 146 · -11% | 167 · -6% | 22 · -31%* |
| H6 | 43 · +1% | 73 · -1% | 112 · -7% | 166 · -7% | 192 · -7% | 21 · -26%* |
| D | 41 · -2% | 71 · -1% | 114 · +0% | 166 · -5% | 197 · -5% | 16 · -28%* |
| L | 37 · -12% | 70 · -5% | 108 · -7% | 146 · -1% | 179 · -5% | 31 · -27% |
| D+conf | 5 · -23%* | 11 · +4%* | 18 · +17%* | 32 · +8% | 40 · +5% | 2 · -100%* |
| D+fade | 19 · +0%* | 28 · -5%* | 48 · -9% | 60 · -15% | 62 · -18% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 31 · -32% | 57 · -15% | 89 · -13% | 140 · -14% | 168 · -16% | 21 · +9%* |
| H6 | 40 · -44% | 76 · -15% | 105 · -16% | 167 · -10% | 187 · -9% | 26 · +3%* |
| D | 40 · -47% | 77 · -22% | 110 · -12% | 159 · -6% | 187 · -7% | 26 · -53%* |
| L | 48 · -42% | 77 · -22% | 108 · -9% | 154 · -0% | 180 · -5% | 29 · -20%* |
| D+conf | 3 · +27%* | 15 · +36%* | 22 · +39%* | 34 · +23% | 42 · +23% | 7 · -62%* |
| D+fade | 27 · -53%* | 43 · -35% | 54 · -44% | 69 · -39% | 70 · -40% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 38 · -16% | 64 · -25% | 97 · -13% | 147 · -15% | 163 · -16% | 26 · -41%* |
| H6 | 46 · -33% | 81 · -17% | 124 · -11% | 172 · -16% | 192 · -11% | 21 · -39%* |
| D | 41 · -17% | 74 · -19% | 119 · -8% | 173 · -10% | 189 · -9% | 24 · -25%* |
| L | 44 · -4% | 69 · -19% | 110 · -19% | 156 · -14% | 184 · -16% | 25 · +39%* |
| D+conf | 2 · +91%* | 7 · -2%* | 18 · -12%* | 30 · -8% | 33 · +3% | 12 · -21%* |
| D+fade | 29 · -64%* | 41 · -46% | 58 · -35% | 73 · -34% | 74 · -34% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 19 · -19%* | 56 · -11% | 75 · -8% | 106 · -10% | 146 · -3% | 43 · -38% |
| H6 | 17 · -33%* | 59 · -26% | 94 · -19% | 123 · -7% | 163 · -9% | 50 · -4% |
| D | 17 · -32%* | 62 · -17% | 94 · -8% | 132 · -12% | 167 · -6% | 46 · -5% |
| L | 18 · -36%* | 64 · -11% | 95 · -4% | 134 · -12% | 164 · -7% | 46 · -26% |
| D+conf | 2 · -4%* | 10 · +14%* | 21 · +9%* | 32 · +14% | 40 · +20% | 18 · +17%* |
| D+fade | 11 · -31%* | 34 · -38% | 47 · -23% | 59 · -29% | 63 · -24% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 123. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.228 (n=92) | +0.018 (n=111) | +0.027 (n=112) | -0.057 (n=105) | -0.150 (n=20) | -0.083 (n=48) |
| spread · B | +0.106 (n=94) | -0.036 (n=112) | +0.035 (n=114) | +0.028 (n=108) | -0.167 (n=18) | +0.042 (n=48) |
| ml · A | +0.001 (n=89) | -0.001 (n=105) | -0.001 (n=110) | +0.000 (n=108) | +0.001 (n=22) | -0.003 (n=54) |
| ml · B | -0.004 (n=97) | -0.003 (n=124) | -0.002 (n=119) | -0.001 (n=110) | -0.005 (n=18) | -0.001 (n=58) |
| total · T | +0.973 (n=75) | +0.330 (n=94) | +0.117 (n=94) | +0.021 (n=95) | -0.143 (n=21) | +0.191 (n=47) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 189 | -0.186 (-0.50) | – | – | – |
| spread · A · D | 213 | -0.121 (-0.38) | – | – | – |
| spread · B · E | 189 | -0.436 (-1.28) | – | – | – |
| spread · B · D | 213 | -0.226 (-0.71) | – | – | – |
| ml · A · E | 189 | – | 0.2135 | 0.2038 | +0.0097 (2.03) |
| ml · A · D | 213 | – | 0.2101 | 0.2003 | +0.0098 (1.97) |
| ml · B · E | 189 | – | 0.2127 | 0.2038 | +0.0090 (1.66) |
| ml · B · D | 213 | – | 0.2080 | 0.2003 | +0.0077 (1.51) |
| total · T · E | 189 | +0.213 (0.56) | – | – | – |
| total · T · D | 213 | -0.134 (-0.38) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._