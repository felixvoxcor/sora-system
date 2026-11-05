# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **80** · ventana E (24 h) **103**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 121 · capturados **80 (66%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 121 · capturados **103 (85%)** · sin cuotas 11 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 58 | +0.034 | [-0.129, +0.198] | 0.42 | 0.337 | -11.35% |
| A (A@D) | 2 | 41 | -0.024 | [-0.230, +0.181] | -0.24 | 0.594 | -11.78% |
| A (A@D) | 3 | 29 | -0.034 | [-0.293, +0.224] | -0.27 | 0.607 | -1.57% |
| B (B@D) | 1 | 58 | -0.069 | [-0.246, +0.108] | -0.78 | 0.781 | -8.32% |
| B (B@D) | 2 | 38 | -0.053 | [-0.239, +0.134] | -0.57 | 0.715 | -4.72% |
| B (B@D) | 3 | 26 | +0.000 | [-0.228, +0.228] | 0.00 | 0.500 | -4.74% |
| C (A@E) | 1 | 77 | +0.130 | [-0.260, +0.520] | 0.66 | 0.255 | -28.16% |
| C (A@E) | 2 | 54 | +0.111 | [-0.410, +0.632] | 0.43 | 0.335 | -15.26% |
| C (A@E) | 3 | 41 | +0.268 | [-0.343, +0.880] | 0.89 | 0.190 | -7.03% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (41/500)** · SD observada 0.65 -> efecto minimo detectable con n=500: 0.09 pts
- Brazo B (B@D): **EN CURSO (38/500)** · SD observada 0.57 -> efecto minimo detectable con n=500: 0.08 pts
- Brazo C (A@E): **EN CURSO (54/500)** · SD observada 1.91 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente 0.004, t = 0.17
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.006, t = -0.23

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 7279 en 123 partidos · cambios de lesiones registrados: 906

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._