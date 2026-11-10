# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **112** · ventana E (24 h) **134**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 153 · capturados **112 (73%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 153 · capturados **134 (88%)** · sin cuotas 12 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 81 | -0.086 | [-0.247, +0.075] | -1.07 | 0.856 | -5.88% |
| A (A@D) | 2 | 61 | -0.164 | [-0.363, +0.035] | -1.64 | 0.947 | -3.12% |
| A (A@D) | 3 | 42 | -0.167 | [-0.432, +0.099] | -1.27 | 0.894 | -0.28% |
| B (B@D) | 1 | 85 | -0.141 | [-0.301, +0.019] | -1.75 | 0.958 | -5.73% |
| B (B@D) | 2 | 58 | -0.086 | [-0.228, +0.056] | -1.22 | 0.886 | -4.54% |
| B (B@D) | 3 | 44 | -0.045 | [-0.205, +0.115] | -0.57 | 0.715 | -8.80% |
| C (A@E) | 1 | 102 | +0.118 | [-0.265, +0.500] | 0.61 | 0.271 | -30.71% |
| C (A@E) | 2 | 73 | -0.027 | [-0.489, +0.434] | -0.12 | 0.547 | -16.29% |
| C (A@E) | 3 | 53 | +0.019 | [-0.549, +0.587] | 0.07 | 0.474 | -6.38% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (61/500)** · SD observada 0.78 -> efecto minimo detectable con n=500: 0.10 pts
- Brazo B (B@D): **EN CURSO (58/500)** · SD observada 0.54 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (73/500)** · SD observada 1.98 -> efecto minimo detectable con n=500: 0.26 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.020, t = -0.96
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.006, t = 0.26

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 11533 en 159 partidos · cambios de lesiones registrados: 1128

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._