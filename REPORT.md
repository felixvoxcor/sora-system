# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **30** · ventana E (24 h) **57**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 71 · capturados **30 (42%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 71 · capturados **57 (80%)** · sin cuotas 7 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 19 | -0.105 | [-0.326, +0.116] | -1.00 | 0.835 | -40.23% |
| A (A@D) | 2 | 15 | -0.067 | [-0.320, +0.187] | -0.56 | 0.709 | -24.29% |
| A (A@D) | 3 | 11 | -0.091 | [-0.293, +0.112] | -1.00 | 0.830 | -13.55% |
| B (B@D) | 1 | 17 | +0.118 | [-0.284, +0.519] | 0.62 | 0.272 | -0.18% |
| B (B@D) | 2 | 14 | -0.071 | [-0.226, +0.083] | -1.00 | 0.832 | -5.24% |
| B (B@D) | 3 | 12 | +nan | [+nan, +nan] | nan | nan | +10.56% |
| C (A@E) | 1 | 43 | +0.023 | [-0.545, +0.591] | 0.08 | 0.467 | -42.50% |
| C (A@E) | 2 | 29 | +0.069 | [-0.725, +0.863] | 0.18 | 0.430 | -27.92% |
| C (A@E) | 3 | 22 | +0.273 | [-0.616, +1.161] | 0.64 | 0.265 | -13.49% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (15/500)** · SD observada 0.46 -> efecto minimo detectable con n=500: 0.06 pts
- Brazo B (B@D): **EN CURSO (14/500)** · SD observada 0.27 -> efecto minimo detectable con n=500: 0.04 pts
- Brazo C (A@E): **EN CURSO (29/500)** · SD observada 2.09 -> efecto minimo detectable con n=500: 0.28 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.007, t = -0.19
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.053, t = 0.88

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 1803 en 81 partidos · cambios de lesiones registrados: 636

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._