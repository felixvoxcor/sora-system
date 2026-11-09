# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **105** · ventana E (24 h) **127**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 146 · capturados **105 (72%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 146 · capturados **127 (87%)** · sin cuotas 12 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 75 | +0.000 | [-0.131, +0.131] | 0.00 | 0.500 | -6.13% |
| A (A@D) | 2 | 55 | -0.055 | [-0.214, +0.105] | -0.68 | 0.752 | -3.16% |
| A (A@D) | 3 | 40 | -0.075 | [-0.272, +0.122] | -0.77 | 0.777 | -0.20% |
| B (B@D) | 1 | 79 | -0.063 | [-0.199, +0.073] | -0.93 | 0.822 | -5.95% |
| B (B@D) | 2 | 53 | -0.038 | [-0.180, +0.105] | -0.53 | 0.701 | -6.52% |
| B (B@D) | 3 | 39 | +0.026 | [-0.132, +0.183] | 0.33 | 0.372 | -12.03% |
| C (A@E) | 1 | 95 | +0.116 | [-0.255, +0.487] | 0.62 | 0.268 | -27.66% |
| C (A@E) | 2 | 68 | +0.000 | [-0.458, +0.458] | 0.00 | 0.500 | -13.00% |
| C (A@E) | 3 | 50 | +0.040 | [-0.505, +0.585] | 0.15 | 0.442 | -4.67% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (55/500)** · SD observada 0.59 -> efecto minimo detectable con n=500: 0.08 pts
- Brazo B (B@D): **EN CURSO (53/500)** · SD observada 0.52 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (68/500)** · SD observada 1.89 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.004, t = -0.23
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.002, t = 0.10

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 11274 en 155 partidos · cambios de lesiones registrados: 1088

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._