# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **132** · ventana E (24 h) **150**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 173 · capturados **132 (76%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 173 · capturados **150 (87%)** · sin cuotas 16 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 98 | -0.041 | [-0.182, +0.100] | -0.58 | 0.717 | -10.60% |
| A (A@D) | 2 | 73 | -0.096 | [-0.275, +0.083] | -1.07 | 0.856 | -3.47% |
| A (A@D) | 3 | 49 | -0.082 | [-0.322, +0.159] | -0.68 | 0.751 | -2.86% |
| B (B@D) | 1 | 99 | -0.121 | [-0.264, +0.022] | -1.68 | 0.952 | -7.59% |
| B (B@D) | 2 | 68 | -0.044 | [-0.173, +0.084] | -0.69 | 0.752 | -4.60% |
| B (B@D) | 3 | 53 | -0.019 | [-0.157, +0.119] | -0.27 | 0.608 | -6.36% |
| C (A@E) | 1 | 114 | +0.149 | [-0.202, +0.500] | 0.84 | 0.201 | -29.76% |
| C (A@E) | 2 | 81 | +0.025 | [-0.396, +0.446] | 0.12 | 0.454 | -17.53% |
| C (A@E) | 3 | 59 | +0.068 | [-0.449, +0.584] | 0.26 | 0.397 | -6.26% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (73/500)** · SD observada 0.77 -> efecto minimo detectable con n=500: 0.10 pts
- Brazo B (B@D): **EN CURSO (68/500)** · SD observada 0.53 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (81/500)** · SD observada 1.90 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.007, t = -0.35
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.004, t = -0.19

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 14238 en 183 partidos · cambios de lesiones registrados: 1271

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._