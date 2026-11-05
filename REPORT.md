# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **79** · ventana E (24 h) **102**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 120 · capturados **79 (66%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 120 · capturados **102 (85%)** · sin cuotas 11 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 57 | +0.053 | [-0.109, +0.215] | 0.65 | 0.259 | -13.22% |
| A (A@D) | 2 | 40 | +0.000 | [-0.205, +0.205] | 0.00 | 0.500 | -14.46% |
| A (A@D) | 3 | 28 | +0.000 | [-0.259, +0.259] | 0.00 | 0.500 | -5.02% |
| B (B@D) | 1 | 57 | -0.053 | [-0.229, +0.124] | -0.60 | 0.723 | -10.13% |
| B (B@D) | 2 | 37 | -0.027 | [-0.211, +0.157] | -0.30 | 0.616 | -7.42% |
| B (B@D) | 3 | 25 | +0.040 | [-0.182, +0.262] | 0.37 | 0.357 | -8.73% |
| C (A@E) | 1 | 76 | +0.158 | [-0.234, +0.549] | 0.80 | 0.212 | -29.72% |
| C (A@E) | 2 | 53 | +0.151 | [-0.374, +0.676] | 0.58 | 0.283 | -17.26% |
| C (A@E) | 3 | 40 | +0.325 | [-0.291, +0.941] | 1.07 | 0.146 | -9.48% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (40/500)** · SD observada 0.64 -> efecto minimo detectable con n=500: 0.09 pts
- Brazo B (B@D): **EN CURSO (37/500)** · SD observada 0.55 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (53/500)** · SD observada 1.91 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente 0.012, t = 0.52
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.011, t = -0.41

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 7153 en 123 partidos · cambios de lesiones registrados: 890

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._