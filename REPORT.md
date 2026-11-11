# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **116** · ventana E (24 h) **138**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 157 · capturados **116 (74%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 157 · capturados **138 (88%)** · sin cuotas 12 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 84 | -0.071 | [-0.229, +0.086] | -0.90 | 0.816 | -9.24% |
| A (A@D) | 2 | 62 | -0.145 | [-0.345, +0.054] | -1.45 | 0.924 | -4.69% |
| A (A@D) | 3 | 43 | -0.140 | [-0.405, +0.126] | -1.06 | 0.853 | -2.60% |
| B (B@D) | 1 | 86 | -0.128 | [-0.288, +0.033] | -1.59 | 0.942 | -6.83% |
| B (B@D) | 2 | 59 | -0.068 | [-0.212, +0.076] | -0.94 | 0.825 | -6.16% |
| B (B@D) | 3 | 45 | -0.022 | [-0.185, +0.141] | -0.27 | 0.608 | -10.82% |
| C (A@E) | 1 | 105 | +0.143 | [-0.233, +0.519] | 0.75 | 0.227 | -30.95% |
| C (A@E) | 2 | 75 | -0.027 | [-0.477, +0.424] | -0.12 | 0.547 | -18.52% |
| C (A@E) | 3 | 54 | +0.000 | [-0.559, +0.559] | 0.00 | 0.500 | -8.11% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (62/500)** · SD observada 0.79 -> efecto minimo detectable con n=500: 0.10 pts
- Brazo B (B@D): **EN CURSO (59/500)** · SD observada 0.55 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (75/500)** · SD observada 1.96 -> efecto minimo detectable con n=500: 0.26 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.014, t = -0.66
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.005, t = 0.19

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 12433 en 169 partidos · cambios de lesiones registrados: 1161

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._