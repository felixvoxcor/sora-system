# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **147** · ventana E (24 h) **161**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 188 · capturados **147 (78%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 188 · capturados **161 (86%)** · sin cuotas 20 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 111 | -0.018 | [-0.168, +0.132] | -0.24 | 0.594 | -5.71% |
| A (A@D) | 2 | 83 | -0.060 | [-0.251, +0.131] | -0.63 | 0.734 | -1.42% |
| A (A@D) | 3 | 57 | -0.035 | [-0.295, +0.225] | -0.27 | 0.606 | +0.10% |
| B (B@D) | 1 | 111 | -0.108 | [-0.261, +0.045] | -1.40 | 0.918 | -3.89% |
| B (B@D) | 2 | 77 | -0.078 | [-0.224, +0.068] | -1.06 | 0.854 | -0.98% |
| B (B@D) | 3 | 58 | -0.034 | [-0.205, +0.136] | -0.41 | 0.657 | -1.34% |
| C (A@E) | 1 | 123 | +0.187 | [-0.141, +0.515] | 1.13 | 0.131 | -27.11% |
| C (A@E) | 2 | 90 | +0.089 | [-0.295, +0.473] | 0.46 | 0.323 | -15.12% |
| C (A@E) | 3 | 64 | +0.125 | [-0.353, +0.603] | 0.52 | 0.302 | -4.64% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (83/500)** · SD observada 0.87 -> efecto minimo detectable con n=500: 0.12 pts
- Brazo B (B@D): **EN CURSO (77/500)** · SD observada 0.64 -> efecto minimo detectable con n=500: 0.09 pts
- Brazo C (A@E): **EN CURSO (90/500)** · SD observada 1.83 -> efecto minimo detectable con n=500: 0.24 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.015, t = -0.79
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.001, t = -0.03

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 16638 en 197 partidos · cambios de lesiones registrados: 1398

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._