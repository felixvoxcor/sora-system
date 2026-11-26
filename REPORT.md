# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **223** · ventana E (24 h) **229**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 264 · capturados **223 (84%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 264 · capturados **229 (87%)** · sin cuotas 28 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 163 | +0.049 | [-0.125, +0.223] | 0.56 | 0.289 | -6.48% |
| A (A@D) | 2 | 119 | +0.050 | [-0.163, +0.264] | 0.47 | 0.321 | -4.00% |
| A (A@D) | 3 | 74 | -0.027 | [-0.251, +0.196] | -0.24 | 0.595 | -7.55% |
| B (B@D) | 1 | 168 | +0.024 | [-0.154, +0.202] | 0.26 | 0.396 | -2.43% |
| B (B@D) | 2 | 117 | +0.060 | [-0.133, +0.253] | 0.61 | 0.270 | +2.66% |
| B (B@D) | 3 | 76 | +0.026 | [-0.175, +0.227] | 0.26 | 0.397 | +0.27% |
| C (A@E) | 1 | 172 | +0.203 | [-0.084, +0.491] | 1.40 | 0.082 | -25.63% |
| C (A@E) | 2 | 114 | +0.219 | [-0.123, +0.561] | 1.27 | 0.103 | -11.18% |
| C (A@E) | 3 | 76 | +0.197 | [-0.215, +0.610] | 0.95 | 0.172 | -2.04% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (119/500)** · SD observada 1.18 -> efecto minimo detectable con n=500: 0.16 pts
- Brazo B (B@D): **EN CURSO (117/500)** · SD observada 1.05 -> efecto minimo detectable con n=500: 0.14 pts
- Brazo C (A@E): **EN CURSO (114/500)** · SD observada 1.84 -> efecto minimo detectable con n=500: 0.24 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.004, t = -0.18
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.006, t = 0.24

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 25905 en 270 partidos · cambios de lesiones registrados: 1895

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._