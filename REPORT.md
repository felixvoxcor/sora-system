# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **135** · ventana E (24 h) **153**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 176 · capturados **135 (77%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 176 · capturados **153 (87%)** · sin cuotas 16 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 100 | -0.030 | [-0.169, +0.109] | -0.43 | 0.665 | -8.59% |
| A (A@D) | 2 | 74 | -0.095 | [-0.271, +0.082] | -1.07 | 0.856 | -2.22% |
| A (A@D) | 3 | 49 | -0.082 | [-0.322, +0.159] | -0.68 | 0.751 | -2.86% |
| B (B@D) | 1 | 102 | -0.127 | [-0.267, +0.013] | -1.81 | 0.963 | -8.42% |
| B (B@D) | 2 | 71 | -0.056 | [-0.182, +0.069] | -0.89 | 0.813 | -5.92% |
| B (B@D) | 3 | 54 | -0.019 | [-0.154, +0.117] | -0.27 | 0.608 | -4.53% |
| C (A@E) | 1 | 115 | +0.157 | [-0.192, +0.505] | 0.89 | 0.188 | -28.71% |
| C (A@E) | 2 | 82 | +0.037 | [-0.380, +0.453] | 0.17 | 0.431 | -16.21% |
| C (A@E) | 3 | 60 | +0.083 | [-0.425, +0.592] | 0.33 | 0.372 | -4.64% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (74/500)** · SD observada 0.76 -> efecto minimo detectable con n=500: 0.10 pts
- Brazo B (B@D): **EN CURSO (71/500)** · SD observada 0.53 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (82/500)** · SD observada 1.90 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.006, t = -0.34
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.007, t = -0.34

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 15304 en 183 partidos · cambios de lesiones registrados: 1299

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._