# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **235** · ventana E (24 h) **241**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 276 · capturados **235 (85%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 276 · capturados **241 (87%)** · sin cuotas 28 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 173 | +0.052 | [-0.112, +0.216] | 0.62 | 0.267 | -7.53% |
| A (A@D) | 2 | 126 | +0.056 | [-0.147, +0.258] | 0.54 | 0.294 | -3.35% |
| A (A@D) | 3 | 79 | -0.013 | [-0.223, +0.198] | -0.12 | 0.547 | -8.66% |
| B (B@D) | 1 | 178 | +0.028 | [-0.140, +0.196] | 0.33 | 0.371 | -4.72% |
| B (B@D) | 2 | 125 | +0.064 | [-0.117, +0.245] | 0.70 | 0.243 | -0.88% |
| B (B@D) | 3 | 80 | +0.025 | [-0.166, +0.216] | 0.26 | 0.397 | +0.00% |
| C (A@E) | 1 | 182 | +0.198 | [-0.077, +0.472] | 1.42 | 0.078 | -23.46% |
| C (A@E) | 2 | 120 | +0.225 | [-0.104, +0.554] | 1.35 | 0.089 | -10.90% |
| C (A@E) | 3 | 79 | +0.190 | [-0.208, +0.588] | 0.95 | 0.173 | -0.99% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (126/500)** · SD observada 1.15 -> efecto minimo detectable con n=500: 0.15 pts
- Brazo B (B@D): **EN CURSO (125/500)** · SD observada 1.02 -> efecto minimo detectable con n=500: 0.14 pts
- Brazo C (A@E): **EN CURSO (120/500)** · SD observada 1.82 -> efecto minimo detectable con n=500: 0.24 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.002, t = -0.08
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.005, t = 0.22

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 27617 en 285 partidos · cambios de lesiones registrados: 1943

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._