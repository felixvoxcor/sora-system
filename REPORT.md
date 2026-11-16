# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **152** · ventana E (24 h) **161**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 193 · capturados **152 (79%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 193 · capturados **161 (83%)** · sin cuotas 25 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 114 | +0.018 | [-0.139, +0.174] | 0.22 | 0.412 | -4.90% |
| A (A@D) | 2 | 85 | -0.024 | [-0.223, +0.176] | -0.23 | 0.592 | -1.55% |
| A (A@D) | 3 | 59 | +0.017 | [-0.255, +0.289] | 0.12 | 0.451 | -0.14% |
| B (B@D) | 1 | 115 | -0.087 | [-0.245, +0.071] | -1.09 | 0.861 | -5.62% |
| B (B@D) | 2 | 80 | -0.037 | [-0.198, +0.123] | -0.47 | 0.679 | -2.36% |
| B (B@D) | 3 | 60 | +0.017 | [-0.176, +0.210] | 0.17 | 0.432 | -1.53% |
| C (A@E) | 1 | 123 | +0.187 | [-0.141, +0.515] | 1.13 | 0.131 | -27.11% |
| C (A@E) | 2 | 90 | +0.089 | [-0.295, +0.473] | 0.46 | 0.323 | -15.12% |
| C (A@E) | 3 | 64 | +0.125 | [-0.353, +0.603] | 0.52 | 0.302 | -4.64% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (85/500)** · SD observada 0.93 -> efecto minimo detectable con n=500: 0.12 pts
- Brazo B (B@D): **EN CURSO (80/500)** · SD observada 0.72 -> efecto minimo detectable con n=500: 0.10 pts
- Brazo C (A@E): **EN CURSO (90/500)** · SD observada 1.83 -> efecto minimo detectable con n=500: 0.24 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.009, t = -0.44
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.002, t = -0.09

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 16827 en 199 partidos · cambios de lesiones registrados: 1436

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._