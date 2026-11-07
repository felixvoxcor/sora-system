# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **84** · ventana E (24 h) **106**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 125 · capturados **84 (67%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 125 · capturados **106 (85%)** · sin cuotas 12 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 59 | +0.034 | [-0.126, +0.194] | 0.42 | 0.337 | -12.85% |
| A (A@D) | 2 | 42 | -0.024 | [-0.224, +0.177] | -0.24 | 0.594 | -13.88% |
| A (A@D) | 3 | 30 | -0.033 | [-0.283, +0.216] | -0.27 | 0.607 | -4.85% |
| B (B@D) | 1 | 61 | -0.066 | [-0.233, +0.102] | -0.78 | 0.781 | -9.58% |
| B (B@D) | 2 | 41 | -0.049 | [-0.221, +0.123] | -0.57 | 0.715 | -6.86% |
| B (B@D) | 3 | 29 | +0.000 | [-0.203, +0.203] | 0.00 | 0.500 | -7.76% |
| C (A@E) | 1 | 78 | +0.103 | [-0.286, +0.492] | 0.53 | 0.301 | -29.08% |
| C (A@E) | 2 | 55 | +0.073 | [-0.445, +0.590] | 0.28 | 0.390 | -16.80% |
| C (A@E) | 3 | 42 | +0.214 | [-0.392, +0.820] | 0.71 | 0.240 | -9.24% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (42/500)** · SD observada 0.64 -> efecto minimo detectable con n=500: 0.09 pts
- Brazo B (B@D): **EN CURSO (41/500)** · SD observada 0.55 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (55/500)** · SD observada 1.91 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente 0.004, t = 0.17
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.005, t = -0.22

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 8609 en 135 partidos · cambios de lesiones registrados: 962

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._