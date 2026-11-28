# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **240** · ventana E (24 h) **246**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 281 · capturados **240 (85%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 281 · capturados **246 (88%)** · sin cuotas 28 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 174 | +0.052 | [-0.112, +0.215] | 0.62 | 0.267 | -8.06% |
| A (A@D) | 2 | 127 | +0.055 | [-0.146, +0.256] | 0.54 | 0.294 | -4.11% |
| A (A@D) | 3 | 80 | -0.013 | [-0.220, +0.195] | -0.12 | 0.547 | -9.80% |
| B (B@D) | 1 | 182 | +0.022 | [-0.143, +0.187] | 0.26 | 0.396 | -4.72% |
| B (B@D) | 2 | 127 | +0.055 | [-0.124, +0.234] | 0.61 | 0.271 | -0.98% |
| B (B@D) | 3 | 82 | +0.012 | [-0.175, +0.200] | 0.13 | 0.449 | -0.19% |
| C (A@E) | 1 | 185 | +0.216 | [-0.055, +0.488] | 1.57 | 0.059 | -24.70% |
| C (A@E) | 2 | 121 | +0.223 | [-0.103, +0.550] | 1.35 | 0.089 | -11.63% |
| C (A@E) | 3 | 80 | +0.188 | [-0.205, +0.580] | 0.95 | 0.173 | -2.23% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (127/500)** · SD observada 1.14 -> efecto minimo detectable con n=500: 0.15 pts
- Brazo B (B@D): **EN CURSO (127/500)** · SD observada 1.02 -> efecto minimo detectable con n=500: 0.14 pts
- Brazo C (A@E): **EN CURSO (121/500)** · SD observada 1.81 -> efecto minimo detectable con n=500: 0.24 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.002, t = -0.11
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.004, t = 0.18

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 27770 en 286 partidos · cambios de lesiones registrados: 1948

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._