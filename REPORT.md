# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **98** · ventana E (24 h) **120**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 139 · capturados **98 (71%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 139 · capturados **120 (86%)** · sin cuotas 12 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 68 | +0.015 | [-0.127, +0.156] | 0.21 | 0.418 | -10.48% |
| A (A@D) | 2 | 49 | -0.041 | [-0.216, +0.135] | -0.47 | 0.679 | -10.75% |
| A (A@D) | 3 | 35 | -0.057 | [-0.277, +0.162] | -0.53 | 0.700 | -7.53% |
| B (B@D) | 1 | 74 | -0.054 | [-0.197, +0.089] | -0.75 | 0.773 | -9.89% |
| B (B@D) | 2 | 49 | -0.020 | [-0.170, +0.129] | -0.27 | 0.608 | -10.41% |
| B (B@D) | 3 | 36 | +0.028 | [-0.144, +0.199] | 0.33 | 0.372 | -15.09% |
| C (A@E) | 1 | 88 | +0.068 | [-0.299, +0.436] | 0.37 | 0.357 | -30.59% |
| C (A@E) | 2 | 62 | +0.016 | [-0.472, +0.504] | 0.07 | 0.474 | -16.90% |
| C (A@E) | 3 | 45 | +0.089 | [-0.494, +0.672] | 0.31 | 0.380 | -11.05% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (49/500)** · SD observada 0.61 -> efecto minimo detectable con n=500: 0.08 pts
- Brazo B (B@D): **EN CURSO (49/500)** · SD observada 0.52 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (62/500)** · SD observada 1.92 -> efecto minimo detectable con n=500: 0.26 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.001, t = -0.04
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.001, t = 0.05

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 10030 en 146 partidos · cambios de lesiones registrados: 1017

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._