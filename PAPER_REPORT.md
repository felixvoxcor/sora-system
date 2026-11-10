# Apuestas ficticias (laboratorio exploratorio, precios reales de ESPN/DraftKings)

Partidos liquidados con evaluacion: **85** · version p1.0 · unidad fija 1u por apuesta · `*` = menos de 30 apuestas (no interpretable).

Niveles de riesgo L1 (muy selectivo) a L5 (casi todo): umbral del borde en puntos. Spread/ML: 4·3·2·1·0.5. Total: 6·4·3·2·1. Cada celda: apuestas · ROI.

### SPREAD · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 15 · +15%* | 31 · -1% | 44 · -9% | 59 · -22% | 65 · -18% | 12 · +28%* |
| H6 | 17 · -44%* | 31 · -14% | 47 · -7% | 63 · -6% | 72 · -5% | 13 · -26%* |
| D | 19 · -30%* | 31 · +4% | 46 · +4% | 63 · +3% | 77 · +4% | 8 · -5%* |
| L | 20 · -33%* | 33 · -7% | 46 · +4% | 62 · +11% | 73 · +5% | 12 · -68%* |
| D+conf | 1 · -100%* | 4 · -4%* | 7 · +39%* | 11 · +6%* | 12 · -3%* | 2 · -100%* |
| D+fade | 14 · -19%* | 18 · +6%* | 22 · +12%* | 27 · +12%* | 27 · +12%* | – |

### SPREAD · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 15 · -49%* | 26 · -34%* | 42 · -14% | 56 · -15% | 65 · -3% | 12 · -52%* |
| H6 | 18 · -26%* | 29 · -8%* | 41 · -17% | 69 · -11% | 77 · -8% | 8 · -52%* |
| D | 19 · -29%* | 33 · -13% | 45 · -2% | 69 · -6% | 77 · -3% | 8 · -28%* |
| L | 18 · -47%* | 33 · -25% | 44 · -22% | 59 · -19% | 71 · -16% | 14 · -59%* |
| D+conf | 2 · -100%* | 5 · -61%* | 7 · -17%* | 16 · -15%* | 16 · -15%* | – |
| D+fade | 9 · +7%* | 14 · +9%* | 20 · +24%* | 25 · +14%* | 26 · +10%* | – |

### ML · modelo A

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 19 · -32%* | 31 · -30% | 41 · -21% | 60 · -19% | 71 · -21% | 6 · +14%* |
| H6 | 20 · -82%* | 36 · -34% | 46 · -32% | 66 · -17% | 70 · -15% | 15 · +5%* |
| D | 18 · -79%* | 35 · -36% | 44 · -22% | 63 · -9% | 74 · -8% | 11 · -37%* |
| L | 23 · -62%* | 35 · -34% | 46 · -24% | 63 · -2% | 72 · -11% | 13 · -11%* |
| D+conf | – | 6 · +4%* | 10 · +14%* | 13 · +9%* | 16 · +23%* | 3 · -56%* |
| D+fade | 15 · -75%* | 22 · -34%* | 24 · -39%* | 28 · -24%* | 29 · -27%* | – |

### ML · modelo B

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 16 · -54%* | 29 · -53%* | 38 · -43% | 57 · -35% | 65 · -30% | 12 · -12%* |
| H6 | 20 · -68%* | 30 · -51% | 49 · -36% | 69 · -36% | 78 · -31% | 7 · -10%* |
| D | 19 · -58%* | 33 · -60% | 51 · -37% | 72 · -30% | 81 · -28% | 4 · +3%* |
| L | 21 · -55%* | 32 · -61% | 46 · -58% | 64 · -38% | 75 · -38% | 10 · +28%* |
| D+conf | 1 · -100%* | 4 · -100%* | 11 · -46%* | 15 · -51%* | 16 · -44%* | – |
| D+fade | 13 · -65%* | 18 · -62%* | 24 · -48%* | 29 · -36%* | 29 · -36%* | 1 · +65%* |

### TOTAL · modelo T

| Entrada | L1 | L2 | L3 | L4 | L5 | sin apostar (<L5) |
|---|---|---|---|---|---|---|
| E | 9 · +6%* | 28 · +2%* | 33 · +4% | 47 · -7% | 65 · -6% | 12 · -4%* |
| H6 | 8 · -5%* | 27 · -16%* | 41 · -3% | 48 · +3% | 61 · -3% | 24 · -36%* |
| D | 6 · -37%* | 23 · -8%* | 38 · +6% | 53 · +1% | 68 · -2% | 17 · +1%* |
| L | 4 · -53%* | 26 · -12%* | 40 · +0% | 57 · -3% | 62 · -1% | 23 · -9%* |
| D+conf | 2 · -4%* | 5 · -23%* | 9 · +28%* | 14 · +23%* | 18 · +18%* | 9 · +27%* |
| D+fade | 3 · -38%* | 11 · -13%* | 19 · +0%* | 24 · -5%* | 25 · -9%* | – |

## Celdas que sobreviven a la correccion por multiples comparaciones

Celdas evaluables: 73. Con tantas celdas, aparecen 'ganadoras' por azar: solo cuenta lo que pasa BH (q=0.10).

**Ninguna.** Las celdas positivas son compatibles con ruido.

## CLV medio por entrada (apuestas nivel L3 o mas; positivo = el mercado se movio hacia nuestro lado)

| Mercado · modelo | E | H6 | D | L | D+conf | D+fade |
|---|---|---|---|---|---|---|
| spread · A | -0.114 (n=44) | -0.213 (n=47) | -0.196 (n=46) | -0.043 (n=46) | -0.286 (n=7) | -0.227 (n=22) |
| spread · B | +0.095 (n=42) | -0.146 (n=41) | -0.067 (n=45) | +0.068 (n=44) | +0.143 (n=7) | -0.100 (n=20) |
| ml · A | -0.003 (n=41) | -0.003 (n=46) | -0.001 (n=44) | -0.000 (n=46) | +0.000 (n=10) | -0.004 (n=24) |
| ml · B | +0.001 (n=38) | -0.002 (n=49) | -0.002 (n=51) | +0.000 (n=46) | -0.001 (n=11) | -0.003 (n=24) |
| total · T | +1.606 (n=33) | +0.659 (n=41) | +0.132 (n=38) | -0.150 (n=40) | +0.000 (n=9) | +0.105 (n=19) |

## Eficiencia del mercado (todos los partidos, sin umbral)

Pendiente de (resultado - linea) sobre (modelo - linea): 0 = el mercado ya lo incorpora todo; 1 = el modelo acierta cuanto se desvia. En moneyline: Brier del modelo vs el del mercado (menor = mejor).

| Mercado · modelo · entrada | n | pendiente (t) | Brier modelo | Brier mercado | dif (t) |
|---|---|---|---|---|---|
| spread · A · E | 77 | -0.535 (-1.03) | – | – | – |
| spread · A · D | 85 | -0.198 (-0.42) | – | – | – |
| spread · B · E | 77 | -0.953 (-1.89) | – | – | – |
| spread · B · D | 85 | -0.679 (-1.37) | – | – | – |
| ml · A · E | 77 | – | 0.1961 | 0.1818 | +0.0144 (1.74) |
| ml · A · D | 85 | – | 0.1988 | 0.1853 | +0.0135 (1.63) |
| ml · B · E | 77 | – | 0.2037 | 0.1818 | +0.0220 (2.61) |
| ml · B · D | 85 | – | 0.2053 | 0.1853 | +0.0200 (2.48) |
| total · T · E | 77 | +0.433 (0.77) | – | – | – |
| total · T · D | 85 | +0.112 (0.20) | – | – | – |

_Papel, no dinero. Nada aqui modifica el protocolo ni autoriza apostar (ver FALSIFICATION.md y PAPER_BETS.md)._