# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **117** · ventana E (24 h) **139**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 158 · capturados **117 (74%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 158 · capturados **139 (88%)** · sin cuotas 12 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 85 | -0.059 | [-0.216, +0.099] | -0.74 | 0.770 | -8.11% |
| A (A@D) | 2 | 63 | -0.127 | [-0.327, +0.073] | -1.27 | 0.896 | -3.23% |
| A (A@D) | 3 | 44 | -0.114 | [-0.378, +0.150] | -0.87 | 0.805 | -0.56% |
| B (B@D) | 1 | 86 | -0.128 | [-0.288, +0.033] | -1.59 | 0.942 | -6.83% |
| B (B@D) | 2 | 59 | -0.068 | [-0.212, +0.076] | -0.94 | 0.825 | -6.16% |
| B (B@D) | 3 | 45 | -0.022 | [-0.185, +0.141] | -0.27 | 0.608 | -10.82% |
| C (A@E) | 1 | 106 | +0.160 | [-0.214, +0.535] | 0.85 | 0.199 | -29.80% |
| C (A@E) | 2 | 76 | +0.000 | [-0.448, +0.448] | 0.00 | 0.500 | -17.08% |
| C (A@E) | 3 | 55 | +0.036 | [-0.517, +0.589] | 0.13 | 0.448 | -6.31% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (63/500)** · SD observada 0.79 -> efecto minimo detectable con n=500: 0.11 pts
- Brazo B (B@D): **EN CURSO (59/500)** · SD observada 0.55 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (76/500)** · SD observada 1.96 -> efecto minimo detectable con n=500: 0.26 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.009, t = -0.45
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.001, t = -0.05

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 12466 en 169 partidos · cambios de lesiones registrados: 1161

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._