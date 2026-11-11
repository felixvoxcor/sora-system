# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **118** · ventana E (24 h) **140**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 159 · capturados **118 (74%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 159 · capturados **140 (88%)** · sin cuotas 12 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 86 | -0.058 | [-0.214, +0.097] | -0.74 | 0.770 | -9.18% |
| A (A@D) | 2 | 64 | -0.125 | [-0.322, +0.072] | -1.27 | 0.896 | -4.74% |
| A (A@D) | 3 | 44 | -0.114 | [-0.378, +0.150] | -0.87 | 0.805 | -0.56% |
| B (B@D) | 1 | 87 | -0.126 | [-0.285, +0.032] | -1.59 | 0.942 | -7.90% |
| B (B@D) | 2 | 60 | -0.067 | [-0.208, +0.075] | -0.94 | 0.825 | -7.72% |
| B (B@D) | 3 | 46 | -0.022 | [-0.181, +0.138] | -0.27 | 0.608 | -12.76% |
| C (A@E) | 1 | 107 | +0.159 | [-0.212, +0.529] | 0.85 | 0.199 | -30.45% |
| C (A@E) | 2 | 77 | +0.000 | [-0.442, +0.442] | 0.00 | 0.500 | -18.15% |
| C (A@E) | 3 | 55 | +0.036 | [-0.517, +0.589] | 0.13 | 0.448 | -6.31% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (64/500)** · SD observada 0.79 -> efecto minimo detectable con n=500: 0.10 pts
- Brazo B (B@D): **EN CURSO (60/500)** · SD observada 0.55 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (77/500)** · SD observada 1.95 -> efecto minimo detectable con n=500: 0.26 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.009, t = -0.45
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.001, t = -0.04

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 12513 en 170 partidos · cambios de lesiones registrados: 1162

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._