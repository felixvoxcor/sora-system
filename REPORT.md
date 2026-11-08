# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **95** · ventana E (24 h) **117**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 136 · capturados **95 (70%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 136 · capturados **117 (86%)** · sin cuotas 12 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 65 | +0.015 | [-0.133, +0.164] | 0.21 | 0.418 | -12.11% |
| A (A@D) | 2 | 46 | -0.043 | [-0.231, +0.144] | -0.47 | 0.679 | -13.07% |
| A (A@D) | 3 | 34 | -0.059 | [-0.285, +0.167] | -0.53 | 0.700 | -4.81% |
| B (B@D) | 1 | 71 | -0.056 | [-0.205, +0.093] | -0.75 | 0.773 | -8.74% |
| B (B@D) | 2 | 48 | -0.021 | [-0.173, +0.132] | -0.27 | 0.608 | -8.55% |
| B (B@D) | 3 | 35 | +0.029 | [-0.148, +0.205] | 0.33 | 0.372 | -12.66% |
| C (A@E) | 1 | 85 | +0.094 | [-0.285, +0.473] | 0.49 | 0.311 | -30.43% |
| C (A@E) | 2 | 60 | +0.033 | [-0.470, +0.537] | 0.13 | 0.448 | -17.37% |
| C (A@E) | 3 | 44 | +0.114 | [-0.481, +0.708] | 0.39 | 0.351 | -9.03% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (46/500)** · SD observada 0.63 -> efecto minimo detectable con n=500: 0.08 pts
- Brazo B (B@D): **EN CURSO (48/500)** · SD observada 0.53 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (60/500)** · SD observada 1.95 -> efecto minimo detectable con n=500: 0.26 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.001, t = -0.04
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.001, t = 0.06

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 9602 en 145 partidos · cambios de lesiones registrados: 1013

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._