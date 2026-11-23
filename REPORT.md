# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **205** · ventana E (24 h) **211**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 246 · capturados **205 (83%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 246 · capturados **211 (86%)** · sin cuotas 28 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 150 | +0.080 | [-0.087, +0.247] | 0.95 | 0.172 | -11.18% |
| A (A@D) | 2 | 109 | +0.037 | [-0.182, +0.256] | 0.33 | 0.370 | -7.57% |
| A (A@D) | 3 | 69 | -0.014 | [-0.253, +0.224] | -0.12 | 0.548 | -6.40% |
| B (B@D) | 1 | 155 | -0.058 | [-0.223, +0.107] | -0.70 | 0.756 | -4.17% |
| B (B@D) | 2 | 108 | +0.000 | [-0.179, +0.179] | 0.00 | 0.500 | -1.27% |
| B (B@D) | 3 | 71 | +0.000 | [-0.179, +0.179] | 0.00 | 0.500 | -0.85% |
| C (A@E) | 1 | 156 | +0.231 | [-0.063, +0.525] | 1.55 | 0.062 | -31.54% |
| C (A@E) | 2 | 103 | +0.204 | [-0.163, +0.570] | 1.10 | 0.136 | -18.45% |
| C (A@E) | 3 | 71 | +0.183 | [-0.258, +0.624] | 0.83 | 0.205 | -6.02% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (109/500)** · SD observada 1.15 -> efecto minimo detectable con n=500: 0.15 pts
- Brazo B (B@D): **EN CURSO (108/500)** · SD observada 0.94 -> efecto minimo detectable con n=500: 0.12 pts
- Brazo C (A@E): **EN CURSO (103/500)** · SD observada 1.88 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.000, t = -0.02
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.010, t = -0.47

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 23080 en 257 partidos · cambios de lesiones registrados: 1789

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._