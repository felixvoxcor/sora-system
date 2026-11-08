# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **92** · ventana E (24 h) **114**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 133 · capturados **92 (69%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 133 · capturados **114 (86%)** · sin cuotas 12 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 63 | +0.016 | [-0.137, +0.169] | 0.21 | 0.418 | -9.32% |
| A (A@D) | 2 | 45 | -0.044 | [-0.236, +0.147] | -0.47 | 0.679 | -11.14% |
| A (A@D) | 3 | 33 | -0.061 | [-0.294, +0.173] | -0.53 | 0.700 | -1.93% |
| B (B@D) | 1 | 68 | -0.044 | [-0.197, +0.109] | -0.57 | 0.716 | -7.60% |
| B (B@D) | 2 | 47 | -0.021 | [-0.177, +0.135] | -0.27 | 0.608 | -6.60% |
| B (B@D) | 3 | 34 | +0.029 | [-0.153, +0.211] | 0.33 | 0.372 | -10.10% |
| C (A@E) | 1 | 83 | +0.108 | [-0.279, +0.496] | 0.56 | 0.290 | -28.75% |
| C (A@E) | 2 | 59 | +0.051 | [-0.460, +0.562] | 0.20 | 0.421 | -15.97% |
| C (A@E) | 3 | 44 | +0.114 | [-0.481, +0.708] | 0.39 | 0.351 | -9.03% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (45/500)** · SD observada 0.64 -> efecto minimo detectable con n=500: 0.08 pts
- Brazo B (B@D): **EN CURSO (47/500)** · SD observada 0.53 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (59/500)** · SD observada 1.96 -> efecto minimo detectable con n=500: 0.26 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.001, t = -0.05
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.003, t = 0.15

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 9581 en 145 partidos · cambios de lesiones registrados: 1012

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._