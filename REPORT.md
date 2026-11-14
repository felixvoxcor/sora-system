# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **142** · ventana E (24 h) **160**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 183 · capturados **142 (78%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 183 · capturados **160 (87%)** · sin cuotas 16 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 106 | -0.009 | [-0.144, +0.125] | -0.14 | 0.555 | -10.24% |
| A (A@D) | 2 | 80 | -0.062 | [-0.230, +0.105] | -0.74 | 0.770 | -4.88% |
| A (A@D) | 3 | 54 | -0.037 | [-0.262, +0.188] | -0.33 | 0.629 | -4.93% |
| B (B@D) | 1 | 107 | -0.103 | [-0.239, +0.034] | -1.49 | 0.931 | -7.41% |
| B (B@D) | 2 | 74 | -0.027 | [-0.154, +0.100] | -0.42 | 0.664 | -4.68% |
| B (B@D) | 3 | 57 | +0.018 | [-0.120, +0.155] | 0.26 | 0.399 | -2.99% |
| C (A@E) | 1 | 122 | +0.180 | [-0.150, +0.511] | 1.08 | 0.141 | -28.07% |
| C (A@E) | 2 | 89 | +0.079 | [-0.309, +0.467] | 0.40 | 0.344 | -16.32% |
| C (A@E) | 3 | 64 | +0.125 | [-0.353, +0.603] | 0.52 | 0.302 | -4.64% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (80/500)** · SD observada 0.75 -> efecto minimo detectable con n=500: 0.10 pts
- Brazo B (B@D): **EN CURSO (74/500)** · SD observada 0.55 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (89/500)** · SD observada 1.84 -> efecto minimo detectable con n=500: 0.24 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.003, t = -0.14
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.005, t = -0.25

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 15630 en 188 partidos · cambios de lesiones registrados: 1313

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._