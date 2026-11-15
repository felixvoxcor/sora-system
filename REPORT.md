# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **144** · ventana E (24 h) **160**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 185 · capturados **144 (78%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 185 · capturados **160 (86%)** · sin cuotas 18 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 108 | -0.037 | [-0.180, +0.106] | -0.51 | 0.696 | -8.35% |
| A (A@D) | 2 | 82 | -0.098 | [-0.276, +0.081] | -1.09 | 0.861 | -2.53% |
| A (A@D) | 3 | 56 | -0.089 | [-0.330, +0.152] | -0.74 | 0.769 | -1.49% |
| B (B@D) | 1 | 108 | -0.130 | [-0.275, +0.016] | -1.77 | 0.960 | -6.48% |
| B (B@D) | 2 | 75 | -0.067 | [-0.215, +0.081] | -0.90 | 0.814 | -3.39% |
| B (B@D) | 3 | 58 | -0.034 | [-0.205, +0.136] | -0.41 | 0.657 | -1.34% |
| C (A@E) | 1 | 122 | +0.180 | [-0.150, +0.511] | 1.08 | 0.141 | -28.07% |
| C (A@E) | 2 | 89 | +0.079 | [-0.309, +0.467] | 0.40 | 0.344 | -16.32% |
| C (A@E) | 3 | 64 | +0.125 | [-0.353, +0.603] | 0.52 | 0.302 | -4.64% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (82/500)** · SD observada 0.81 -> efecto minimo detectable con n=500: 0.11 pts
- Brazo B (B@D): **EN CURSO (75/500)** · SD observada 0.64 -> efecto minimo detectable con n=500: 0.09 pts
- Brazo C (A@E): **EN CURSO (89/500)** · SD observada 1.84 -> efecto minimo detectable con n=500: 0.24 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.021, t = -1.12
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.006, t = 0.31

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 15886 en 193 partidos · cambios de lesiones registrados: 1370

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._