# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **109** · ventana E (24 h) **131**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 150 · capturados **109 (73%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 150 · capturados **131 (87%)** · sin cuotas 12 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 79 | -0.076 | [-0.239, +0.088] | -0.92 | 0.821 | -3.50% |
| A (A@D) | 2 | 59 | -0.153 | [-0.357, +0.052] | -1.49 | 0.930 | +0.16% |
| A (A@D) | 3 | 42 | -0.167 | [-0.432, +0.099] | -1.27 | 0.894 | -0.28% |
| B (B@D) | 1 | 82 | -0.134 | [-0.299, +0.031] | -1.62 | 0.945 | -4.67% |
| B (B@D) | 2 | 55 | -0.073 | [-0.219, +0.073] | -1.00 | 0.839 | -2.88% |
| B (B@D) | 3 | 41 | -0.024 | [-0.190, +0.141] | -0.30 | 0.616 | -6.89% |
| C (A@E) | 1 | 99 | +0.091 | [-0.295, +0.476] | 0.47 | 0.320 | -28.61% |
| C (A@E) | 2 | 70 | -0.071 | [-0.538, +0.396] | -0.31 | 0.619 | -12.70% |
| C (A@E) | 3 | 52 | -0.058 | [-0.616, +0.500] | -0.21 | 0.582 | -4.58% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (59/500)** · SD observada 0.78 -> efecto minimo detectable con n=500: 0.10 pts
- Brazo B (B@D): **EN CURSO (55/500)** · SD observada 0.54 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (70/500)** · SD observada 1.96 -> efecto minimo detectable con n=500: 0.26 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.019, t = -0.89
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.009, t = 0.37

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 11496 en 159 partidos · cambios de lesiones registrados: 1118

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._