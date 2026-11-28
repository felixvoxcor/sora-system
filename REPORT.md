# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **234** · ventana E (24 h) **240**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 275 · capturados **234 (85%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 275 · capturados **240 (87%)** · sin cuotas 28 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 172 | +0.052 | [-0.113, +0.218] | 0.62 | 0.267 | -6.99% |
| A (A@D) | 2 | 125 | +0.056 | [-0.148, +0.260] | 0.54 | 0.294 | -2.58% |
| A (A@D) | 3 | 78 | -0.013 | [-0.226, +0.201] | -0.12 | 0.547 | -7.49% |
| B (B@D) | 1 | 177 | +0.028 | [-0.141, +0.197] | 0.33 | 0.371 | -4.18% |
| B (B@D) | 2 | 125 | +0.064 | [-0.117, +0.245] | 0.70 | 0.243 | -0.88% |
| B (B@D) | 3 | 80 | +0.025 | [-0.166, +0.216] | 0.26 | 0.397 | +0.00% |
| C (A@E) | 1 | 181 | +0.204 | [-0.071, +0.480] | 1.46 | 0.073 | -23.04% |
| C (A@E) | 2 | 119 | +0.235 | [-0.096, +0.567] | 1.41 | 0.081 | -10.15% |
| C (A@E) | 3 | 79 | +0.190 | [-0.208, +0.588] | 0.95 | 0.173 | -0.99% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (125/500)** · SD observada 1.15 -> efecto minimo detectable con n=500: 0.15 pts
- Brazo B (B@D): **EN CURSO (125/500)** · SD observada 1.02 -> efecto minimo detectable con n=500: 0.14 pts
- Brazo C (A@E): **EN CURSO (119/500)** · SD observada 1.83 -> efecto minimo detectable con n=500: 0.24 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.002, t = -0.08
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.005, t = 0.22

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 27604 en 285 partidos · cambios de lesiones registrados: 1943

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._