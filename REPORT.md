# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **139** · ventana E (24 h) **157**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 180 · capturados **139 (77%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 180 · capturados **157 (87%)** · sin cuotas 16 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 103 | -0.019 | [-0.156, +0.117] | -0.28 | 0.611 | -9.46% |
| A (A@D) | 2 | 77 | -0.078 | [-0.250, +0.094] | -0.90 | 0.815 | -3.63% |
| A (A@D) | 3 | 52 | -0.058 | [-0.288, +0.172] | -0.50 | 0.692 | -4.92% |
| B (B@D) | 1 | 106 | -0.113 | [-0.250, +0.023] | -1.65 | 0.949 | -8.32% |
| B (B@D) | 2 | 73 | -0.041 | [-0.167, +0.085] | -0.65 | 0.742 | -5.97% |
| B (B@D) | 3 | 56 | +0.000 | [-0.135, +0.135] | 0.00 | 0.500 | -4.64% |
| C (A@E) | 1 | 119 | +0.168 | [-0.171, +0.507] | 0.98 | 0.164 | -27.87% |
| C (A@E) | 2 | 86 | +0.058 | [-0.342, +0.459] | 0.29 | 0.387 | -15.62% |
| C (A@E) | 3 | 62 | +0.097 | [-0.396, +0.589] | 0.39 | 0.348 | -4.64% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (77/500)** · SD observada 0.76 -> efecto minimo detectable con n=500: 0.10 pts
- Brazo B (B@D): **EN CURSO (73/500)** · SD observada 0.54 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (86/500)** · SD observada 1.87 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.004, t = -0.23
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.007, t = -0.35

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 15312 en 185 partidos · cambios de lesiones registrados: 1302

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._