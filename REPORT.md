# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **58** · ventana E (24 h) **81**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 99 · capturados **58 (59%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 99 · capturados **81 (82%)** · sin cuotas 11 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 41 | +0.073 | [-0.105, +0.252] | 0.83 | 0.206 | -21.37% |
| A (A@D) | 2 | 31 | +0.065 | [-0.146, +0.275] | 0.63 | 0.268 | -20.44% |
| A (A@D) | 3 | 23 | +0.043 | [-0.200, +0.287] | 0.37 | 0.357 | -0.80% |
| B (B@D) | 1 | 41 | +0.024 | [-0.193, +0.242] | 0.23 | 0.411 | -12.07% |
| B (B@D) | 2 | 26 | +0.077 | [-0.118, +0.272] | 0.81 | 0.212 | -11.96% |
| B (B@D) | 3 | 20 | +0.150 | [-0.021, +0.321] | 1.83 | 0.041 | -4.73% |
| C (A@E) | 1 | 61 | +0.098 | [-0.376, +0.572] | 0.42 | 0.340 | -37.41% |
| C (A@E) | 2 | 43 | +0.116 | [-0.522, +0.754] | 0.37 | 0.357 | -20.10% |
| C (A@E) | 3 | 32 | +0.344 | [-0.415, +1.102] | 0.92 | 0.181 | -16.51% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (31/500)** · SD observada 0.57 -> efecto minimo detectable con n=500: 0.08 pts
- Brazo B (B@D): **EN CURSO (26/500)** · SD observada 0.48 -> efecto minimo detectable con n=500: 0.06 pts
- Brazo C (A@E): **EN CURSO (43/500)** · SD observada 2.07 -> efecto minimo detectable con n=500: 0.28 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente 0.019, t = 0.77
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.000, t = -0.01

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 5089 en 107 partidos · cambios de lesiones registrados: 781

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._