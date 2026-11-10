# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **106** · ventana E (24 h) **128**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 147 · capturados **106 (72%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 147 · capturados **128 (87%)** · sin cuotas 12 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 76 | +0.000 | [-0.129, +0.129] | 0.00 | 0.500 | -4.78% |
| A (A@D) | 2 | 56 | -0.054 | [-0.210, +0.103] | -0.68 | 0.752 | -1.39% |
| A (A@D) | 3 | 41 | -0.073 | [-0.265, +0.119] | -0.77 | 0.777 | +2.15% |
| B (B@D) | 1 | 79 | -0.063 | [-0.199, +0.073] | -0.93 | 0.822 | -5.95% |
| B (B@D) | 2 | 53 | -0.038 | [-0.180, +0.105] | -0.53 | 0.701 | -6.52% |
| B (B@D) | 3 | 39 | +0.026 | [-0.132, +0.183] | 0.33 | 0.372 | -12.03% |
| C (A@E) | 1 | 96 | +0.115 | [-0.252, +0.482] | 0.62 | 0.268 | -26.38% |
| C (A@E) | 2 | 69 | +0.000 | [-0.451, +0.451] | 0.00 | 0.500 | -11.43% |
| C (A@E) | 3 | 51 | +0.039 | [-0.494, +0.573] | 0.15 | 0.442 | -2.71% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (56/500)** · SD observada 0.59 -> efecto minimo detectable con n=500: 0.08 pts
- Brazo B (B@D): **EN CURSO (53/500)** · SD observada 0.52 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (69/500)** · SD observada 1.88 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.004, t = -0.24
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.002, t = 0.11

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 11474 en 159 partidos · cambios de lesiones registrados: 1115

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._