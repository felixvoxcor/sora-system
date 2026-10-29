# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **27** · ventana E (24 h) **54**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 68 · capturados **27 (40%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 68 · capturados **54 (79%)** · sin cuotas 7 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 18 | -0.111 | [-0.346, +0.123] | -1.00 | 0.834 | -36.90% |
| A (A@D) | 2 | 15 | -0.067 | [-0.320, +0.187] | -0.56 | 0.709 | -24.29% |
| A (A@D) | 3 | 11 | -0.091 | [-0.293, +0.112] | -1.00 | 0.830 | -13.55% |
| B (B@D) | 1 | 16 | +0.125 | [-0.305, +0.555] | 0.62 | 0.272 | -5.98% |
| B (B@D) | 2 | 13 | -0.077 | [-0.245, +0.091] | -1.00 | 0.831 | -12.76% |
| B (B@D) | 3 | 11 | +nan | [+nan, +nan] | nan | nan | +3.10% |
| C (A@E) | 1 | 42 | +0.024 | [-0.558, +0.606] | 0.08 | 0.467 | -41.13% |
| C (A@E) | 2 | 29 | +0.069 | [-0.725, +0.863] | 0.18 | 0.430 | -27.92% |
| C (A@E) | 3 | 22 | +0.273 | [-0.616, +1.161] | 0.64 | 0.265 | -13.49% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (15/500)** · SD observada 0.46 -> efecto minimo detectable con n=500: 0.06 pts
- Brazo B (B@D): **EN CURSO (13/500)** · SD observada 0.28 -> efecto minimo detectable con n=500: 0.04 pts
- Brazo C (A@E): **EN CURSO (29/500)** · SD observada 2.09 -> efecto minimo detectable con n=500: 0.28 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.007, t = -0.18
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.060, t = 0.89

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 713 en 79 partidos · cambios de lesiones registrados: 584

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._