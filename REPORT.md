# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **100** · ventana E (24 h) **122**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 141 · capturados **100 (71%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 141 · capturados **122 (87%)** · sin cuotas 12 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 70 | +0.000 | [-0.141, +0.141] | 0.00 | 0.500 | -7.64% |
| A (A@D) | 2 | 51 | -0.059 | [-0.231, +0.114] | -0.68 | 0.752 | -6.84% |
| A (A@D) | 3 | 37 | -0.081 | [-0.295, +0.132] | -0.77 | 0.777 | -2.32% |
| B (B@D) | 1 | 76 | -0.066 | [-0.207, +0.075] | -0.93 | 0.822 | -7.29% |
| B (B@D) | 2 | 51 | -0.039 | [-0.188, +0.109] | -0.53 | 0.701 | -6.52% |
| B (B@D) | 3 | 37 | +0.027 | [-0.139, +0.193] | 0.33 | 0.372 | -12.33% |
| C (A@E) | 1 | 90 | +0.133 | [-0.249, +0.516] | 0.69 | 0.245 | -30.01% |
| C (A@E) | 2 | 63 | +0.016 | [-0.464, +0.496] | 0.07 | 0.474 | -15.19% |
| C (A@E) | 3 | 46 | +0.087 | [-0.483, +0.657] | 0.31 | 0.380 | -8.83% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (51/500)** · SD observada 0.61 -> efecto minimo detectable con n=500: 0.08 pts
- Brazo B (B@D): **EN CURSO (51/500)** · SD observada 0.53 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (63/500)** · SD observada 1.90 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.004, t = -0.22
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.002, t = 0.09

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 10429 en 149 partidos · cambios de lesiones registrados: 1064

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._