# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **82** · ventana E (24 h) **105**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 123 · capturados **82 (67%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 123 · capturados **105 (85%)** · sin cuotas 11 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 58 | +0.034 | [-0.129, +0.198] | 0.42 | 0.337 | -11.35% |
| A (A@D) | 2 | 41 | -0.024 | [-0.230, +0.181] | -0.24 | 0.594 | -11.78% |
| A (A@D) | 3 | 29 | -0.034 | [-0.293, +0.224] | -0.27 | 0.607 | -1.57% |
| B (B@D) | 1 | 60 | -0.067 | [-0.237, +0.104] | -0.78 | 0.781 | -8.07% |
| B (B@D) | 2 | 40 | -0.050 | [-0.227, +0.127] | -0.57 | 0.715 | -4.54% |
| B (B@D) | 3 | 28 | +0.000 | [-0.211, +0.211] | 0.00 | 0.500 | -4.47% |
| C (A@E) | 1 | 77 | +0.130 | [-0.260, +0.520] | 0.66 | 0.255 | -28.16% |
| C (A@E) | 2 | 54 | +0.111 | [-0.410, +0.632] | 0.43 | 0.335 | -15.26% |
| C (A@E) | 3 | 41 | +0.268 | [-0.343, +0.880] | 0.89 | 0.190 | -7.03% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (41/500)** · SD observada 0.65 -> efecto minimo detectable con n=500: 0.09 pts
- Brazo B (B@D): **EN CURSO (40/500)** · SD observada 0.55 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (54/500)** · SD observada 1.91 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente 0.004, t = 0.17
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.006, t = -0.22

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 8337 en 132 partidos · cambios de lesiones registrados: 937

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._