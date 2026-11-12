# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **127** · ventana E (24 h) **147**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 168 · capturados **127 (76%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 168 · capturados **147 (88%)** · sin cuotas 14 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 93 | -0.043 | [-0.192, +0.105] | -0.58 | 0.717 | -9.81% |
| A (A@D) | 2 | 70 | -0.100 | [-0.287, +0.087] | -1.07 | 0.856 | -4.66% |
| A (A@D) | 3 | 48 | -0.083 | [-0.329, +0.162] | -0.68 | 0.751 | -0.84% |
| B (B@D) | 1 | 95 | -0.126 | [-0.276, +0.023] | -1.68 | 0.952 | -9.59% |
| B (B@D) | 2 | 65 | -0.046 | [-0.181, +0.088] | -0.69 | 0.752 | -5.95% |
| B (B@D) | 3 | 50 | -0.020 | [-0.166, +0.126] | -0.27 | 0.608 | -8.22% |
| C (A@E) | 1 | 112 | +0.152 | [-0.205, +0.508] | 0.84 | 0.200 | -31.86% |
| C (A@E) | 2 | 80 | +0.013 | [-0.413, +0.438] | 0.06 | 0.477 | -18.85% |
| C (A@E) | 3 | 58 | +0.052 | [-0.473, +0.576] | 0.20 | 0.422 | -7.88% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (70/500)** · SD observada 0.78 -> efecto minimo detectable con n=500: 0.10 pts
- Brazo B (B@D): **EN CURSO (65/500)** · SD observada 0.54 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (80/500)** · SD observada 1.91 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.007, t = -0.34
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.004, t = -0.20

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 13601 en 174 partidos · cambios de lesiones registrados: 1220

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._