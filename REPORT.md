# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **91** · ventana E (24 h) **113**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 132 · capturados **91 (69%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 132 · capturados **113 (86%)** · sin cuotas 12 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 62 | +0.032 | [-0.120, +0.185] | 0.42 | 0.337 | -7.86% |
| A (A@D) | 2 | 44 | -0.023 | [-0.214, +0.168] | -0.24 | 0.594 | -9.12% |
| A (A@D) | 3 | 32 | -0.031 | [-0.264, +0.202] | -0.27 | 0.607 | +1.14% |
| B (B@D) | 1 | 68 | -0.044 | [-0.197, +0.109] | -0.57 | 0.716 | -7.60% |
| B (B@D) | 2 | 47 | -0.021 | [-0.177, +0.135] | -0.27 | 0.608 | -6.60% |
| B (B@D) | 3 | 34 | +0.029 | [-0.153, +0.211] | 0.33 | 0.372 | -10.10% |
| C (A@E) | 1 | 82 | +0.134 | [-0.255, +0.523] | 0.69 | 0.247 | -27.88% |
| C (A@E) | 2 | 58 | +0.086 | [-0.429, +0.601] | 0.34 | 0.369 | -14.52% |
| C (A@E) | 3 | 43 | +0.163 | [-0.438, +0.763] | 0.55 | 0.294 | -6.91% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (44/500)** · SD observada 0.63 -> efecto minimo detectable con n=500: 0.08 pts
- Brazo B (B@D): **EN CURSO (47/500)** · SD observada 0.53 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (58/500)** · SD observada 1.96 -> efecto minimo detectable con n=500: 0.26 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente 0.002, t = 0.11
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.001, t = -0.04

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 9243 en 139 partidos · cambios de lesiones registrados: 986

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._