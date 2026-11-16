# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **154** · ventana E (24 h) **163**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 195 · capturados **154 (79%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 195 · capturados **163 (84%)** · sin cuotas 25 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 116 | +0.026 | [-0.128, +0.180] | 0.33 | 0.370 | -4.88% |
| A (A@D) | 2 | 86 | -0.012 | [-0.210, +0.187] | -0.12 | 0.546 | -0.46% |
| A (A@D) | 3 | 59 | +0.017 | [-0.255, +0.289] | 0.12 | 0.451 | -0.14% |
| B (B@D) | 1 | 116 | -0.095 | [-0.252, +0.062] | -1.20 | 0.883 | -6.43% |
| B (B@D) | 2 | 81 | -0.049 | [-0.209, +0.110] | -0.61 | 0.730 | -3.57% |
| B (B@D) | 3 | 60 | +0.017 | [-0.176, +0.210] | 0.17 | 0.432 | -1.53% |
| C (A@E) | 1 | 125 | +0.184 | [-0.139, +0.507] | 1.13 | 0.131 | -26.75% |
| C (A@E) | 2 | 90 | +0.089 | [-0.295, +0.473] | 0.46 | 0.323 | -15.12% |
| C (A@E) | 3 | 64 | +0.125 | [-0.353, +0.603] | 0.52 | 0.302 | -4.64% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (86/500)** · SD observada 0.93 -> efecto minimo detectable con n=500: 0.12 pts
- Brazo B (B@D): **EN CURSO (81/500)** · SD observada 0.72 -> efecto minimo detectable con n=500: 0.10 pts
- Brazo C (A@E): **EN CURSO (90/500)** · SD observada 1.83 -> efecto minimo detectable con n=500: 0.24 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.008, t = -0.40
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.005, t = -0.25

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 16856 en 203 partidos · cambios de lesiones registrados: 1436

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._