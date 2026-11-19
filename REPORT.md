# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **176** · ventana E (24 h) **185**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 217 · capturados **176 (81%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 217 · capturados **185 (85%)** · sin cuotas 25 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 131 | +0.092 | [-0.078, +0.261] | 1.07 | 0.143 | -9.86% |
| A (A@D) | 2 | 94 | +0.043 | [-0.180, +0.265] | 0.38 | 0.353 | -4.87% |
| A (A@D) | 3 | 63 | +0.016 | [-0.238, +0.270] | 0.12 | 0.450 | -0.43% |
| B (B@D) | 1 | 132 | -0.083 | [-0.255, +0.088] | -0.96 | 0.831 | -9.04% |
| B (B@D) | 2 | 92 | -0.022 | [-0.221, +0.177] | -0.22 | 0.586 | -8.85% |
| B (B@D) | 3 | 65 | -0.015 | [-0.199, +0.168] | -0.17 | 0.566 | -6.22% |
| C (A@E) | 1 | 140 | +0.214 | [-0.097, +0.526] | 1.36 | 0.088 | -30.52% |
| C (A@E) | 2 | 94 | +0.160 | [-0.229, +0.548] | 0.82 | 0.208 | -16.71% |
| C (A@E) | 3 | 65 | +0.138 | [-0.333, +0.610] | 0.59 | 0.280 | -3.17% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (94/500)** · SD observada 1.09 -> efecto minimo detectable con n=500: 0.14 pts
- Brazo B (B@D): **EN CURSO (92/500)** · SD observada 0.96 -> efecto minimo detectable con n=500: 0.13 pts
- Brazo C (A@E): **EN CURSO (94/500)** · SD observada 1.90 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.002, t = -0.10
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.017, t = -0.71

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 19939 en 223 partidos · cambios de lesiones registrados: 1591

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._