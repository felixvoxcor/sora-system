# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **49** · ventana E (24 h) **72**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 90 · capturados **49 (54%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 90 · capturados **72 (80%)** · sin cuotas 11 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 34 | +0.088 | [-0.111, +0.287] | 0.90 | 0.187 | -32.89% |
| A (A@D) | 2 | 26 | +0.077 | [-0.149, +0.303] | 0.70 | 0.245 | -26.72% |
| A (A@D) | 3 | 19 | +0.053 | [-0.200, +0.305] | 0.44 | 0.333 | -9.44% |
| B (B@D) | 1 | 35 | +0.086 | [-0.155, +0.327] | 0.72 | 0.237 | +3.01% |
| B (B@D) | 2 | 26 | +0.077 | [-0.118, +0.272] | 0.81 | 0.212 | -11.96% |
| B (B@D) | 3 | 20 | +0.150 | [-0.021, +0.321] | 1.83 | 0.041 | -4.73% |
| C (A@E) | 1 | 54 | +0.148 | [-0.362, +0.658] | 0.58 | 0.281 | -39.99% |
| C (A@E) | 2 | 39 | +0.205 | [-0.465, +0.875] | 0.62 | 0.270 | -26.71% |
| C (A@E) | 3 | 29 | +0.483 | [-0.296, +1.261] | 1.27 | 0.107 | -21.05% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (26/500)** · SD observada 0.56 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo B (B@D): **EN CURSO (26/500)** · SD observada 0.48 -> efecto minimo detectable con n=500: 0.06 pts
- Brazo C (A@E): **EN CURSO (39/500)** · SD observada 2.07 -> efecto minimo detectable con n=500: 0.27 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente 0.024, t = 0.89
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.005, t = 0.12

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 3334 en 105 partidos · cambios de lesiones registrados: 722

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._