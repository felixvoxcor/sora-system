# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **119** · ventana E (24 h) **141**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 160 · capturados **119 (74%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 160 · capturados **141 (88%)** · sin cuotas 12 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 86 | -0.058 | [-0.214, +0.097] | -0.74 | 0.770 | -9.18% |
| A (A@D) | 2 | 64 | -0.125 | [-0.322, +0.072] | -1.27 | 0.896 | -4.74% |
| A (A@D) | 3 | 44 | -0.114 | [-0.378, +0.150] | -0.87 | 0.805 | -0.56% |
| B (B@D) | 1 | 88 | -0.125 | [-0.282, +0.032] | -1.58 | 0.942 | -6.77% |
| B (B@D) | 2 | 61 | -0.066 | [-0.205, +0.074] | -0.94 | 0.825 | -6.09% |
| B (B@D) | 3 | 47 | -0.021 | [-0.177, +0.135] | -0.27 | 0.608 | -10.54% |
| C (A@E) | 1 | 107 | +0.159 | [-0.212, +0.529] | 0.85 | 0.199 | -30.45% |
| C (A@E) | 2 | 77 | +0.000 | [-0.442, +0.442] | 0.00 | 0.500 | -18.15% |
| C (A@E) | 3 | 55 | +0.036 | [-0.517, +0.589] | 0.13 | 0.448 | -6.31% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (64/500)** · SD observada 0.79 -> efecto minimo detectable con n=500: 0.10 pts
- Brazo B (B@D): **EN CURSO (61/500)** · SD observada 0.54 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (77/500)** · SD observada 1.95 -> efecto minimo detectable con n=500: 0.26 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.009, t = -0.45
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.001, t = -0.03

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 12989 en 170 partidos · cambios de lesiones registrados: 1168

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._