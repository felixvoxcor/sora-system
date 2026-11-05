# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **72** · ventana E (24 h) **95**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 113 · capturados **72 (64%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 113 · capturados **95 (84%)** · sin cuotas 11 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 50 | +0.040 | [-0.141, +0.221] | 0.44 | 0.330 | -16.30% |
| A (A@D) | 2 | 36 | -0.028 | [-0.249, +0.194] | -0.25 | 0.600 | -15.45% |
| A (A@D) | 3 | 25 | -0.040 | [-0.319, +0.239] | -0.30 | 0.615 | -8.74% |
| B (B@D) | 1 | 52 | -0.077 | [-0.267, +0.113] | -0.81 | 0.790 | -8.76% |
| B (B@D) | 2 | 33 | -0.061 | [-0.258, +0.136] | -0.63 | 0.732 | -7.65% |
| B (B@D) | 3 | 24 | +0.000 | [-0.216, +0.216] | 0.00 | 0.500 | -12.75% |
| C (A@E) | 1 | 70 | +0.129 | [-0.291, +0.548] | 0.61 | 0.272 | -31.81% |
| C (A@E) | 2 | 47 | +0.106 | [-0.478, +0.691] | 0.37 | 0.358 | -18.78% |
| C (A@E) | 3 | 36 | +0.306 | [-0.370, +0.981] | 0.92 | 0.182 | -15.18% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (36/500)** · SD observada 0.65 -> efecto minimo detectable con n=500: 0.09 pts
- Brazo B (B@D): **EN CURSO (33/500)** · SD observada 0.56 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (47/500)** · SD observada 1.99 -> efecto minimo detectable con n=500: 0.26 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente 0.009, t = 0.35
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.011, t = -0.41

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 7144 en 121 partidos · cambios de lesiones registrados: 889

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._