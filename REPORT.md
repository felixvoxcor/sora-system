# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **103** · ventana E (24 h) **125**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 144 · capturados **103 (72%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 144 · capturados **125 (87%)** · sin cuotas 12 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 73 | +0.000 | [-0.135, +0.135] | 0.00 | 0.500 | -8.73% |
| A (A@D) | 2 | 53 | -0.057 | [-0.222, +0.109] | -0.68 | 0.752 | -6.63% |
| A (A@D) | 3 | 38 | -0.079 | [-0.287, +0.129] | -0.77 | 0.777 | -4.89% |
| B (B@D) | 1 | 78 | -0.064 | [-0.202, +0.073] | -0.93 | 0.822 | -7.14% |
| B (B@D) | 2 | 52 | -0.038 | [-0.184, +0.107] | -0.53 | 0.701 | -8.32% |
| B (B@D) | 3 | 38 | +0.026 | [-0.136, +0.188] | 0.33 | 0.372 | -14.64% |
| C (A@E) | 1 | 93 | +0.151 | [-0.223, +0.524] | 0.80 | 0.212 | -30.25% |
| C (A@E) | 2 | 66 | +0.045 | [-0.418, +0.509] | 0.20 | 0.423 | -16.20% |
| C (A@E) | 3 | 48 | +0.104 | [-0.449, +0.657] | 0.38 | 0.353 | -8.72% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (53/500)** · SD observada 0.60 -> efecto minimo detectable con n=500: 0.08 pts
- Brazo B (B@D): **EN CURSO (52/500)** · SD observada 0.52 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (66/500)** · SD observada 1.88 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.004, t = -0.23
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.002, t = 0.10

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 10474 en 153 partidos · cambios de lesiones registrados: 1065

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._