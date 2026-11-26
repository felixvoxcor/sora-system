# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **226** · ventana E (24 h) **232**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 267 · capturados **226 (85%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 267 · capturados **232 (87%)** · sin cuotas 28 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 165 | +0.048 | [-0.124, +0.221] | 0.56 | 0.289 | -6.47% |
| A (A@D) | 2 | 120 | +0.050 | [-0.162, +0.262] | 0.47 | 0.321 | -3.22% |
| A (A@D) | 3 | 74 | -0.027 | [-0.251, +0.196] | -0.24 | 0.595 | -7.55% |
| B (B@D) | 1 | 171 | +0.023 | [-0.151, +0.198] | 0.26 | 0.396 | -3.03% |
| B (B@D) | 2 | 120 | +0.058 | [-0.130, +0.246] | 0.61 | 0.270 | +1.68% |
| B (B@D) | 3 | 78 | +0.026 | [-0.170, +0.221] | 0.26 | 0.397 | +0.14% |
| C (A@E) | 1 | 175 | +0.200 | [-0.083, +0.483] | 1.40 | 0.082 | -24.74% |
| C (A@E) | 2 | 114 | +0.219 | [-0.123, +0.561] | 1.27 | 0.103 | -11.18% |
| C (A@E) | 3 | 76 | +0.197 | [-0.215, +0.610] | 0.95 | 0.172 | -2.04% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (120/500)** · SD observada 1.17 -> efecto minimo detectable con n=500: 0.16 pts
- Brazo B (B@D): **EN CURSO (120/500)** · SD observada 1.04 -> efecto minimo detectable con n=500: 0.14 pts
- Brazo C (A@E): **EN CURSO (114/500)** · SD observada 1.84 -> efecto minimo detectable con n=500: 0.24 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.004, t = -0.17
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.006, t = 0.24

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 25905 en 270 partidos · cambios de lesiones registrados: 1896

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._