# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **220** · ventana E (24 h) **226**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 261 · capturados **220 (84%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 261 · capturados **226 (87%)** · sin cuotas 28 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 161 | +0.056 | [-0.120, +0.232] | 0.63 | 0.266 | -7.77% |
| A (A@D) | 2 | 118 | +0.051 | [-0.165, +0.266] | 0.47 | 0.321 | -4.87% |
| A (A@D) | 3 | 74 | -0.027 | [-0.251, +0.196] | -0.24 | 0.595 | -7.55% |
| B (B@D) | 1 | 167 | +0.030 | [-0.149, +0.209] | 0.33 | 0.371 | -3.01% |
| B (B@D) | 2 | 116 | +0.069 | [-0.125, +0.263] | 0.71 | 0.241 | +1.86% |
| B (B@D) | 3 | 75 | +0.040 | [-0.162, +0.242] | 0.40 | 0.347 | -0.99% |
| C (A@E) | 1 | 169 | +0.183 | [-0.105, +0.472] | 1.26 | 0.105 | -26.59% |
| C (A@E) | 2 | 113 | +0.212 | [-0.132, +0.557] | 1.22 | 0.112 | -12.12% |
| C (A@E) | 3 | 75 | +0.187 | [-0.231, +0.604] | 0.89 | 0.188 | -3.33% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (118/500)** · SD observada 1.18 -> efecto minimo detectable con n=500: 0.16 pts
- Brazo B (B@D): **EN CURSO (116/500)** · SD observada 1.05 -> efecto minimo detectable con n=500: 0.14 pts
- Brazo C (A@E): **EN CURSO (113/500)** · SD observada 1.85 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.005, t = -0.21
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.007, t = 0.28

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 25779 en 270 partidos · cambios de lesiones registrados: 1878

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._