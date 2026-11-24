# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **216** · ventana E (24 h) **222**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 257 · capturados **216 (84%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 257 · capturados **222 (86%)** · sin cuotas 28 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 157 | +0.083 | [-0.086, +0.251] | 0.97 | 0.166 | -7.81% |
| A (A@D) | 2 | 115 | +0.043 | [-0.177, +0.264] | 0.39 | 0.349 | -4.03% |
| A (A@D) | 3 | 72 | -0.028 | [-0.258, +0.202] | -0.24 | 0.595 | -4.98% |
| B (B@D) | 1 | 163 | -0.006 | [-0.178, +0.166] | -0.07 | 0.528 | -1.79% |
| B (B@D) | 2 | 116 | +0.069 | [-0.125, +0.263] | 0.71 | 0.241 | +1.86% |
| B (B@D) | 3 | 75 | +0.040 | [-0.162, +0.242] | 0.40 | 0.347 | -0.99% |
| C (A@E) | 1 | 165 | +0.218 | [-0.070, +0.506] | 1.50 | 0.068 | -27.15% |
| C (A@E) | 2 | 110 | +0.218 | [-0.135, +0.571] | 1.22 | 0.112 | -11.46% |
| C (A@E) | 3 | 74 | +0.189 | [-0.234, +0.612] | 0.89 | 0.188 | -2.03% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (115/500)** · SD observada 1.19 -> efecto minimo detectable con n=500: 0.16 pts
- Brazo B (B@D): **EN CURSO (116/500)** · SD observada 1.05 -> efecto minimo detectable con n=500: 0.14 pts
- Brazo C (A@E): **EN CURSO (110/500)** · SD observada 1.87 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.001, t = -0.05
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.000, t = 0.01

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 24345 en 261 partidos · cambios de lesiones registrados: 1850

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._