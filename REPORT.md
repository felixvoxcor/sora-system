# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **99** · ventana E (24 h) **121**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 140 · capturados **99 (71%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 140 · capturados **121 (86%)** · sin cuotas 12 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 69 | +0.014 | [-0.125, +0.154] | 0.21 | 0.418 | -9.06% |
| A (A@D) | 2 | 50 | -0.040 | [-0.212, +0.132] | -0.47 | 0.679 | -8.79% |
| A (A@D) | 3 | 36 | -0.056 | [-0.269, +0.158] | -0.53 | 0.700 | -4.91% |
| B (B@D) | 1 | 75 | -0.053 | [-0.194, +0.088] | -0.75 | 0.773 | -8.60% |
| B (B@D) | 2 | 50 | -0.020 | [-0.166, +0.126] | -0.27 | 0.608 | -8.47% |
| B (B@D) | 3 | 37 | +0.027 | [-0.139, +0.193] | 0.33 | 0.372 | -12.33% |
| C (A@E) | 1 | 89 | +0.067 | [-0.296, +0.431] | 0.37 | 0.357 | -29.22% |
| C (A@E) | 2 | 63 | +0.016 | [-0.464, +0.496] | 0.07 | 0.474 | -15.19% |
| C (A@E) | 3 | 46 | +0.087 | [-0.483, +0.657] | 0.31 | 0.380 | -8.83% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (50/500)** · SD observada 0.60 -> efecto minimo detectable con n=500: 0.08 pts
- Brazo B (B@D): **EN CURSO (50/500)** · SD observada 0.51 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (63/500)** · SD observada 1.90 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.001, t = -0.05
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.001, t = 0.06

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 10388 en 148 partidos · cambios de lesiones registrados: 1058

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._