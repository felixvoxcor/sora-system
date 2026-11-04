# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **66** · ventana E (24 h) **89**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 107 · capturados **66 (62%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 107 · capturados **89 (83%)** · sin cuotas 11 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 46 | +0.000 | [-0.188, +0.188] | 0.00 | 0.500 | -13.26% |
| A (A@D) | 2 | 35 | -0.029 | [-0.257, +0.199] | -0.25 | 0.600 | -13.03% |
| A (A@D) | 3 | 24 | -0.042 | [-0.333, +0.250] | -0.30 | 0.615 | -4.94% |
| B (B@D) | 1 | 47 | -0.021 | [-0.220, +0.177] | -0.22 | 0.585 | -11.16% |
| B (B@D) | 2 | 31 | +0.000 | [-0.189, +0.189] | 0.00 | 0.500 | -7.77% |
| B (B@D) | 3 | 22 | +0.091 | [-0.098, +0.280] | 1.00 | 0.164 | -13.39% |
| C (A@E) | 1 | 67 | +0.119 | [-0.319, +0.558] | 0.54 | 0.294 | -31.55% |
| C (A@E) | 2 | 46 | +0.109 | [-0.489, +0.707] | 0.37 | 0.358 | -17.01% |
| C (A@E) | 3 | 35 | +0.314 | [-0.382, +1.010] | 0.92 | 0.183 | -12.76% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (35/500)** · SD observada 0.66 -> efecto minimo detectable con n=500: 0.09 pts
- Brazo B (B@D): **EN CURSO (31/500)** · SD observada 0.52 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (46/500)** · SD observada 2.01 -> efecto minimo detectable con n=500: 0.27 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente 0.006, t = 0.24
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.008, t = 0.29

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 6268 en 121 partidos · cambios de lesiones registrados: 837

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._