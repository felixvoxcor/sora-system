# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **218** · ventana E (24 h) **224**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 259 · capturados **218 (84%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 259 · capturados **224 (86%)** · sin cuotas 28 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 159 | +0.050 | [-0.127, +0.228] | 0.56 | 0.289 | -7.80% |
| A (A@D) | 2 | 116 | +0.043 | [-0.176, +0.262] | 0.39 | 0.349 | -4.86% |
| A (A@D) | 3 | 73 | -0.027 | [-0.254, +0.199] | -0.24 | 0.595 | -6.29% |
| B (B@D) | 1 | 165 | +0.024 | [-0.156, +0.205] | 0.27 | 0.396 | -2.98% |
| B (B@D) | 2 | 116 | +0.069 | [-0.125, +0.263] | 0.71 | 0.241 | +1.86% |
| B (B@D) | 3 | 75 | +0.040 | [-0.162, +0.242] | 0.40 | 0.347 | -0.99% |
| C (A@E) | 1 | 167 | +0.180 | [-0.112, +0.471] | 1.22 | 0.113 | -26.86% |
| C (A@E) | 2 | 111 | +0.207 | [-0.143, +0.558] | 1.17 | 0.122 | -12.25% |
| C (A@E) | 3 | 74 | +0.189 | [-0.234, +0.612] | 0.89 | 0.188 | -2.03% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (116/500)** · SD observada 1.19 -> efecto minimo detectable con n=500: 0.16 pts
- Brazo B (B@D): **EN CURSO (116/500)** · SD observada 1.05 -> efecto minimo detectable con n=500: 0.14 pts
- Brazo C (A@E): **EN CURSO (111/500)** · SD observada 1.86 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.007, t = -0.28
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.007, t = 0.29

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 24804 en 269 partidos · cambios de lesiones registrados: 1867

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._