# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **210** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 25 · +7%* | 58 · +2% | 92 · -6% | 141 · -19% | 159 · -14% | 27 · -8%* |
| H6 | 30 · -18% | 65 · -12% | 111 · -2% | 161 · -8% | 176 · -6% | 34 · -5% |
| D | 37 · -13% | 69 · -9% | 112 · -1% | 156 · -5% | 184 · -4% | 26 · +3%* |
| L | 38 · -20% | 73 · -11% | 105 · -0% | 151 · +3% | 173 · +0% | 34 · -26% |
| D+conf | 5 · +14%* | 11 · +4%* | 20 · +45%* | 28 · +31%* | 35 · +16% | 10 · -3%* |
| D+fade | 21 · -19%* | 34 · -17% | 48 · -5% | 58 · -9% | 59 · -10% | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 35 · -18% | 59 · -12% | 92 · -7% | 144 · -11% | 165 · -6% | 21 · -37%* |
| H6 | 43 · +1% | 71 · -1% | 109 · -8% | 163 · -8% | 189 · -7% | 21 · -26%* |
| D | 40 · -4% | 69 · -0% | 112 · +1% | 163 · -5% | 194 · -6% | 16 · -28%* |
| L | 36 · -15% | 69 · -6% | 106 · -7% | 143 · -2% | 176 · -6% | 31 · -27% |
| D+conf | 5 · -23%* | 11 · +4%* | 18 · +17%* | 32 · +8% | 40 · +5% | 2 · -100%* |
| D+fade | 18 · -4%* | 26 · -5%* | 46 · -9% | 58 · -15% | 60 · -18% | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 31 · -32% | 57 · -15% | 88 · -14% | 139 · -14% | 167 · -17% | 19 · +20%* |
| H6 | 40 · -44% | 76 · -15% | 105 · -16% | 164 · -10% | 184 · -9% | 26 · +3%* |
| D | 40 · -47% | 77 · -22% | 110 · -12% | 157 · -6% | 185 · -6% | 25 · -56%* |
| L | 48 · -42% | 77 · -22% | 108 · -9% | 152 · +0% | 178 · -5% | 28 · -22%* |
| D+conf | 3 · +27%* | 15 · +36%* | 22 · +39%* | 33 · +23% | 41 · +22% | 7 · -62%* |
| D+fade | 27 · -53%* | 43 · -35% | 54 · -44% | 68 · -38% | 69 · -39% | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 38 · -16% | 63 · -26% | 95 · -12% | 145 · -15% | 161 · -15% | 25 · -38%* |
| H6 | 46 · -33% | 79 · -15% | 121 · -10% | 169 · -16% | 189 · -10% | 21 · -39%* |
| D | 41 · -17% | 72 · -17% | 117 · -6% | 170 · -9% | 186 · -8% | 24 · -25%* |
| L | 43 · -2% | 67 · -17% | 108 · -18% | 153 · -13% | 181 · -15% | 25 · +39%* |
| D+conf | 2 · +91%* | 7 · -2%* | 18 · -12%* | 30 · -8% | 33 · +3% | 12 · -21%* |
| D+fade | 29 · -64%* | 39 · -43% | 56 · -33% | 70 · -33% | 71 · -34% | 2 · -18%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 19 · -19%* | 56 · -11% | 75 · -8% | 105 · -11% | 145 · -4% | 41 · -35% |
| H6 | 17 · -33%* | 59 · -26% | 92 · -19% | 121 · -7% | 160 · -8% | 50 · -4% |
| D | 17 · -32%* | 61 · -15% | 93 · -7% | 129 · -11% | 164 · -6% | 46 · -5% |
| L | 18 · -36%* | 62 · -11% | 93 · -4% | 132 · -12% | 161 · -6% | 46 · -26% |
| D+conf | 2 · -4%* | 10 · +14%* | 21 · +9%* | 32 · +14% | 40 · +20% | 18 · +17%* |
| D+fade | 11 · -31%* | 33 · -36% | 46 · -21% | 57 · -26% | 61 · -22% | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 123. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | +0.228 (n=92) | +0.018 (n=111) | +0.027 (n=112) | -0.057 (n=105) | -0.150 (n=20) | -0.083 (n=48) |
| spread · B | +0.120 (n=92) | -0.037 (n=109) | +0.036 (n=112) | +0.028 (n=106) | -0.167 (n=18) | +0.043 (n=46) |
| ml · A | +0.000 (n=88) | -0.001 (n=105) | -0.001 (n=110) | +0.000 (n=108) | +0.001 (n=22) | -0.003 (n=54) |
| ml · B | -0.004 (n=95) | -0.003 (n=121) | -0.002 (n=117) | -0.001 (n=108) | -0.005 (n=18) | -0.001 (n=56) |
| total · T | +0.973 (n=75) | +0.359 (n=92) | +0.118 (n=93) | +0.022 (n=93) | -0.143 (n=21) | +0.196 (n=46) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 186 | -0.185 (-0.49) | – | – | – |
| spread · A · D | 210 | -0.118 (-0.37) | – | – | – |
| spread · B · E | 186 | -0.464 (-1.35) | – | – | – |
| spread · B · D | 210 | -0.244 (-0.75) | – | – | – |
| ml · A · E | 186 | – | 0.2142 | 0.2041 | +0.0100 (2.07) |
| ml · A · D | 210 | – | 0.2107 | 0.2008 | +0.0098 (1.96) |
| ml · B · E | 186 | – | 0.2130 | 0.2041 | +0.0088 (1.61) |
| ml · B · D | 210 | – | 0.2078 | 0.2008 | +0.0069 (1.36) |
| total · T · E | 186 | +0.189 (0.50) | – | – | – |
| total · T · D | 210 | -0.147 (-0.42) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._