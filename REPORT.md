# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **186** · ventana E (24 h) **194**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 227 · capturados **186 (82%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 227 · capturados **194 (85%)** · sin cuotas 26 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 138 | +0.094 | [-0.070, +0.258] | 1.14 | 0.129 | -10.31% |
| A (A@D) | 2 | 101 | +0.050 | [-0.162, +0.261] | 0.46 | 0.322 | -5.83% |
| A (A@D) | 3 | 65 | +0.000 | [-0.248, +0.248] | 0.00 | 0.500 | -3.49% |
| B (B@D) | 1 | 139 | -0.058 | [-0.224, +0.109] | -0.68 | 0.753 | -5.37% |
| B (B@D) | 2 | 98 | +0.010 | [-0.182, +0.202] | 0.11 | 0.458 | -4.67% |
| B (B@D) | 3 | 67 | +0.015 | [-0.173, +0.202] | 0.16 | 0.437 | -3.37% |
| C (A@E) | 1 | 146 | +0.260 | [-0.046, +0.566] | 1.68 | 0.048 | -32.09% |
| C (A@E) | 2 | 98 | +0.204 | [-0.173, +0.582] | 1.07 | 0.143 | -18.19% |
| C (A@E) | 3 | 69 | +0.203 | [-0.249, +0.655] | 0.89 | 0.187 | -6.06% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (101/500)** · SD observada 1.07 -> efecto minimo detectable con n=500: 0.14 pts
- Brazo B (B@D): **EN CURSO (98/500)** · SD observada 0.96 -> efecto minimo detectable con n=500: 0.13 pts
- Brazo C (A@E): **EN CURSO (98/500)** · SD observada 1.88 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.003, t = -0.13
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.011, t = -0.50

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 21623 en 240 partidos · cambios de lesiones registrados: 1683

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._