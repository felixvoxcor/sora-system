# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **150** · ventana E (24 h) **161**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 191 · capturados **150 (79%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 191 · capturados **161 (84%)** · sin cuotas 23 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 112 | +0.009 | [-0.149, +0.167] | 0.11 | 0.456 | -4.89% |
| A (A@D) | 2 | 84 | -0.024 | [-0.226, +0.178] | -0.23 | 0.592 | -0.38% |
| A (A@D) | 3 | 58 | +0.017 | [-0.259, +0.294] | 0.12 | 0.451 | +1.58% |
| B (B@D) | 1 | 113 | -0.080 | [-0.239, +0.080] | -0.99 | 0.837 | -3.94% |
| B (B@D) | 2 | 79 | -0.038 | [-0.200, +0.124] | -0.47 | 0.679 | -1.13% |
| B (B@D) | 3 | 59 | +0.017 | [-0.180, +0.213] | 0.17 | 0.432 | +0.14% |
| C (A@E) | 1 | 123 | +0.187 | [-0.141, +0.515] | 1.13 | 0.131 | -27.11% |
| C (A@E) | 2 | 90 | +0.089 | [-0.295, +0.473] | 0.46 | 0.323 | -15.12% |
| C (A@E) | 3 | 64 | +0.125 | [-0.353, +0.603] | 0.52 | 0.302 | -4.64% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (84/500)** · SD observada 0.93 -> efecto minimo detectable con n=500: 0.12 pts
- Brazo B (B@D): **EN CURSO (79/500)** · SD observada 0.72 -> efecto minimo detectable con n=500: 0.10 pts
- Brazo C (A@E): **EN CURSO (90/500)** · SD observada 1.83 -> efecto minimo detectable con n=500: 0.24 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.009, t = -0.46
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.000, t = -0.01

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 16804 en 197 partidos · cambios de lesiones registrados: 1431

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._