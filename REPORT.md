# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **178** · ventana E (24 h) **187**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 219 · capturados **178 (81%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 219 · capturados **187 (85%)** · sin cuotas 25 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 133 | +0.083 | [-0.085, +0.250] | 0.98 | 0.165 | -9.78% |
| A (A@D) | 2 | 96 | +0.031 | [-0.188, +0.250] | 0.28 | 0.389 | -4.86% |
| A (A@D) | 3 | 64 | +0.000 | [-0.252, +0.252] | 0.00 | 0.500 | -1.98% |
| B (B@D) | 1 | 134 | -0.075 | [-0.244, +0.095] | -0.87 | 0.807 | -7.56% |
| B (B@D) | 2 | 93 | -0.011 | [-0.209, +0.187] | -0.11 | 0.543 | -7.79% |
| B (B@D) | 3 | 65 | -0.015 | [-0.199, +0.168] | -0.17 | 0.566 | -6.22% |
| C (A@E) | 1 | 142 | +0.246 | [-0.065, +0.558] | 1.56 | 0.060 | -31.50% |
| C (A@E) | 2 | 95 | +0.168 | [-0.216, +0.553] | 0.87 | 0.193 | -17.58% |
| C (A@E) | 3 | 66 | +0.152 | [-0.313, +0.616] | 0.65 | 0.259 | -4.63% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (96/500)** · SD observada 1.08 -> efecto minimo detectable con n=500: 0.14 pts
- Brazo B (B@D): **EN CURSO (93/500)** · SD observada 0.96 -> efecto minimo detectable con n=500: 0.13 pts
- Brazo C (A@E): **EN CURSO (95/500)** · SD observada 1.89 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.005, t = -0.22
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.013, t = -0.55

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 19942 en 223 partidos · cambios de lesiones registrados: 1591

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._