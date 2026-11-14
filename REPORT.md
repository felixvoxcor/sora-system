# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **138** · ventana E (24 h) **156**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 179 · capturados **138 (77%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 179 · capturados **156 (87%)** · sin cuotas 16 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 103 | -0.019 | [-0.156, +0.117] | -0.28 | 0.611 | -9.46% |
| A (A@D) | 2 | 77 | -0.078 | [-0.250, +0.094] | -0.90 | 0.815 | -3.63% |
| A (A@D) | 3 | 52 | -0.058 | [-0.288, +0.172] | -0.50 | 0.692 | -4.92% |
| B (B@D) | 1 | 105 | -0.114 | [-0.252, +0.023] | -1.65 | 0.949 | -7.45% |
| B (B@D) | 2 | 72 | -0.042 | [-0.169, +0.086] | -0.65 | 0.742 | -4.66% |
| B (B@D) | 3 | 55 | +0.000 | [-0.138, +0.138] | 0.00 | 0.500 | -2.90% |
| C (A@E) | 1 | 118 | +0.153 | [-0.188, +0.493] | 0.89 | 0.188 | -28.91% |
| C (A@E) | 2 | 85 | +0.035 | [-0.367, +0.438] | 0.17 | 0.431 | -16.92% |
| C (A@E) | 3 | 62 | +0.097 | [-0.396, +0.589] | 0.39 | 0.348 | -4.64% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (77/500)** · SD observada 0.76 -> efecto minimo detectable con n=500: 0.10 pts
- Brazo B (B@D): **EN CURSO (72/500)** · SD observada 0.54 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (85/500)** · SD observada 1.87 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.004, t = -0.23
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.007, t = -0.35

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 15306 en 183 partidos · cambios de lesiones registrados: 1302

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._