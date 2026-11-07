# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **87** · ventana E (24 h) **109**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 128 · capturados **87 (68%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 128 · capturados **109 (85%)** · sin cuotas 12 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 61 | +0.033 | [-0.122, +0.188] | 0.42 | 0.337 | -9.48% |
| A (A@D) | 2 | 43 | -0.023 | [-0.219, +0.172] | -0.24 | 0.594 | -11.45% |
| A (A@D) | 3 | 31 | -0.032 | [-0.273, +0.209] | -0.27 | 0.607 | -1.76% |
| B (B@D) | 1 | 64 | -0.062 | [-0.222, +0.097] | -0.78 | 0.781 | -7.88% |
| B (B@D) | 2 | 44 | -0.045 | [-0.205, +0.115] | -0.57 | 0.715 | -4.57% |
| B (B@D) | 3 | 31 | +0.000 | [-0.189, +0.189] | 0.00 | 0.500 | -7.55% |
| C (A@E) | 1 | 79 | +0.089 | [-0.296, +0.474] | 0.46 | 0.324 | -27.56% |
| C (A@E) | 2 | 56 | +0.054 | [-0.456, +0.563] | 0.21 | 0.417 | -14.88% |
| C (A@E) | 3 | 42 | +0.214 | [-0.392, +0.820] | 0.71 | 0.240 | -9.24% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (43/500)** · SD observada 0.64 -> efecto minimo detectable con n=500: 0.08 pts
- Brazo B (B@D): **EN CURSO (44/500)** · SD observada 0.53 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (56/500)** · SD observada 1.90 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente 0.004, t = 0.17
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.005, t = -0.23

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 8629 en 139 partidos · cambios de lesiones registrados: 962

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._