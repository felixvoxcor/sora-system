# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **155** · ventana E (24 h) **164**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 196 · capturados **155 (79%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 196 · capturados **164 (84%)** · sin cuotas 25 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 117 | +0.026 | [-0.127, +0.179] | 0.33 | 0.370 | -4.10% |
| A (A@D) | 2 | 87 | -0.011 | [-0.208, +0.185] | -0.12 | 0.546 | +0.55% |
| A (A@D) | 3 | 60 | +0.017 | [-0.250, +0.284] | 0.12 | 0.450 | +1.31% |
| B (B@D) | 1 | 117 | -0.094 | [-0.250, +0.062] | -1.20 | 0.883 | -5.63% |
| B (B@D) | 2 | 82 | -0.049 | [-0.207, +0.109] | -0.61 | 0.730 | -2.46% |
| B (B@D) | 3 | 61 | +0.016 | [-0.173, +0.206] | 0.17 | 0.432 | -0.08% |
| C (A@E) | 1 | 126 | +0.167 | [-0.156, +0.489] | 1.02 | 0.154 | -27.33% |
| C (A@E) | 2 | 90 | +0.089 | [-0.295, +0.473] | 0.46 | 0.323 | -15.12% |
| C (A@E) | 3 | 64 | +0.125 | [-0.353, +0.603] | 0.52 | 0.302 | -4.64% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (87/500)** · SD observada 0.92 -> efecto minimo detectable con n=500: 0.12 pts
- Brazo B (B@D): **EN CURSO (82/500)** · SD observada 0.72 -> efecto minimo detectable con n=500: 0.10 pts
- Brazo C (A@E): **EN CURSO (90/500)** · SD observada 1.83 -> efecto minimo detectable con n=500: 0.24 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.008, t = -0.40
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.005, t = -0.25

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 16903 en 205 partidos · cambios de lesiones registrados: 1437

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._