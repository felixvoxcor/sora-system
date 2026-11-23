# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **206** · ventana E (24 h) **212**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 247 · capturados **206 (83%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 247 · capturados **212 (86%)** · sin cuotas 28 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 151 | +0.073 | [-0.093, +0.239] | 0.87 | 0.194 | -11.76% |
| A (A@D) | 2 | 110 | +0.027 | [-0.191, +0.245] | 0.25 | 0.402 | -8.42% |
| A (A@D) | 3 | 70 | -0.029 | [-0.265, +0.208] | -0.24 | 0.595 | -7.73% |
| B (B@D) | 1 | 156 | -0.064 | [-0.228, +0.100] | -0.77 | 0.779 | -4.78% |
| B (B@D) | 2 | 109 | -0.009 | [-0.187, +0.169] | -0.10 | 0.541 | -2.18% |
| B (B@D) | 3 | 72 | -0.014 | [-0.192, +0.165] | -0.16 | 0.561 | -2.22% |
| C (A@E) | 1 | 157 | +0.204 | [-0.093, +0.501] | 1.36 | 0.089 | -31.98% |
| C (A@E) | 2 | 103 | +0.204 | [-0.163, +0.570] | 1.10 | 0.136 | -18.45% |
| C (A@E) | 3 | 71 | +0.183 | [-0.258, +0.624] | 0.83 | 0.205 | -6.02% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (110/500)** · SD observada 1.15 -> efecto minimo detectable con n=500: 0.15 pts
- Brazo B (B@D): **EN CURSO (109/500)** · SD observada 0.94 -> efecto minimo detectable con n=500: 0.12 pts
- Brazo C (A@E): **EN CURSO (103/500)** · SD observada 1.88 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.002, t = -0.11
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.011, t = -0.49

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 23119 en 258 partidos · cambios de lesiones registrados: 1789

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._