# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **97** · ventana E (24 h) **119**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 138 · capturados **97 (70%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 138 · capturados **119 (86%)** · sin cuotas 12 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 67 | +0.015 | [-0.129, +0.159] | 0.21 | 0.418 | -9.14% |
| A (A@D) | 2 | 48 | -0.042 | [-0.221, +0.138] | -0.47 | 0.679 | -8.89% |
| A (A@D) | 3 | 34 | -0.059 | [-0.285, +0.167] | -0.53 | 0.700 | -4.81% |
| B (B@D) | 1 | 73 | -0.055 | [-0.200, +0.090] | -0.75 | 0.773 | -8.65% |
| B (B@D) | 2 | 48 | -0.021 | [-0.173, +0.132] | -0.27 | 0.608 | -8.55% |
| B (B@D) | 3 | 35 | +0.029 | [-0.148, +0.205] | 0.33 | 0.372 | -12.66% |
| C (A@E) | 1 | 87 | +0.080 | [-0.290, +0.451] | 0.43 | 0.334 | -29.79% |
| C (A@E) | 2 | 61 | +0.033 | [-0.462, +0.528] | 0.13 | 0.447 | -15.54% |
| C (A@E) | 3 | 44 | +0.114 | [-0.481, +0.708] | 0.39 | 0.351 | -9.03% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (48/500)** · SD observada 0.62 -> efecto minimo detectable con n=500: 0.08 pts
- Brazo B (B@D): **EN CURSO (48/500)** · SD observada 0.53 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (61/500)** · SD observada 1.93 -> efecto minimo detectable con n=500: 0.26 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.001, t = -0.04
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.001, t = 0.05

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 9666 en 146 partidos · cambios de lesiones registrados: 1017

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._