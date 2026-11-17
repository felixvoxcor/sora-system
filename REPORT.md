# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **159** · ventana E (24 h) **168**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 200 · capturados **159 (80%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 200 · capturados **168 (84%)** · sin cuotas 25 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 119 | +0.017 | [-0.134, +0.168] | 0.22 | 0.413 | -5.71% |
| A (A@D) | 2 | 88 | -0.023 | [-0.218, +0.173] | -0.23 | 0.591 | -0.59% |
| A (A@D) | 3 | 60 | +0.017 | [-0.250, +0.284] | 0.12 | 0.450 | +1.31% |
| B (B@D) | 1 | 120 | -0.100 | [-0.253, +0.053] | -1.30 | 0.902 | -7.99% |
| B (B@D) | 2 | 84 | -0.060 | [-0.215, +0.096] | -0.76 | 0.775 | -4.78% |
| B (B@D) | 3 | 63 | +0.000 | [-0.187, +0.187] | 0.00 | 0.500 | -3.25% |
| C (A@E) | 1 | 129 | +0.178 | [-0.141, +0.497] | 1.11 | 0.135 | -29.02% |
| C (A@E) | 2 | 90 | +0.089 | [-0.295, +0.473] | 0.46 | 0.323 | -15.12% |
| C (A@E) | 3 | 64 | +0.125 | [-0.353, +0.603] | 0.52 | 0.302 | -4.64% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (88/500)** · SD observada 0.92 -> efecto minimo detectable con n=500: 0.12 pts
- Brazo B (B@D): **EN CURSO (84/500)** · SD observada 0.72 -> efecto minimo detectable con n=500: 0.10 pts
- Brazo C (A@E): **EN CURSO (90/500)** · SD observada 1.83 -> efecto minimo detectable con n=500: 0.24 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.008, t = -0.44
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.008, t = -0.38

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 17826 en 209 partidos · cambios de lesiones registrados: 1487

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._