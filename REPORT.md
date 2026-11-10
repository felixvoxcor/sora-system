# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **110** · ventana E (24 h) **132**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 151 · capturados **110 (73%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 151 · capturados **132 (87%)** · sin cuotas 12 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 80 | -0.075 | [-0.236, +0.086] | -0.92 | 0.821 | -4.70% |
| A (A@D) | 2 | 60 | -0.150 | [-0.351, +0.051] | -1.49 | 0.930 | -1.51% |
| A (A@D) | 3 | 42 | -0.167 | [-0.432, +0.099] | -1.27 | 0.894 | -0.28% |
| B (B@D) | 1 | 83 | -0.133 | [-0.295, +0.030] | -1.62 | 0.945 | -5.81% |
| B (B@D) | 2 | 56 | -0.071 | [-0.215, +0.072] | -1.00 | 0.839 | -4.61% |
| B (B@D) | 3 | 42 | -0.024 | [-0.185, +0.137] | -0.30 | 0.616 | -9.10% |
| C (A@E) | 1 | 100 | +0.090 | [-0.292, +0.472] | 0.47 | 0.320 | -29.33% |
| C (A@E) | 2 | 71 | -0.070 | [-0.531, +0.390] | -0.31 | 0.619 | -13.93% |
| C (A@E) | 3 | 52 | -0.058 | [-0.616, +0.500] | -0.21 | 0.582 | -4.58% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (60/500)** · SD observada 0.78 -> efecto minimo detectable con n=500: 0.10 pts
- Brazo B (B@D): **EN CURSO (56/500)** · SD observada 0.53 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (71/500)** · SD observada 1.94 -> efecto minimo detectable con n=500: 0.26 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.019, t = -0.90
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.009, t = 0.37

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 11514 en 159 partidos · cambios de lesiones registrados: 1125

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._