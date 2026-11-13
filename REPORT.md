# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **131** · ventana E (24 h) **149**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 172 · capturados **131 (76%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 172 · capturados **149 (87%)** · sin cuotas 16 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 97 | -0.041 | [-0.184, +0.101] | -0.58 | 0.717 | -11.62% |
| A (A@D) | 2 | 72 | -0.097 | [-0.279, +0.084] | -1.07 | 0.856 | -4.74% |
| A (A@D) | 3 | 49 | -0.082 | [-0.322, +0.159] | -0.68 | 0.751 | -2.86% |
| B (B@D) | 1 | 99 | -0.121 | [-0.264, +0.022] | -1.68 | 0.952 | -7.59% |
| B (B@D) | 2 | 68 | -0.044 | [-0.173, +0.084] | -0.69 | 0.752 | -4.60% |
| B (B@D) | 3 | 53 | -0.019 | [-0.157, +0.119] | -0.27 | 0.608 | -6.36% |
| C (A@E) | 1 | 113 | +0.142 | [-0.212, +0.495] | 0.79 | 0.215 | -30.80% |
| C (A@E) | 2 | 80 | +0.013 | [-0.413, +0.438] | 0.06 | 0.477 | -18.85% |
| C (A@E) | 3 | 58 | +0.052 | [-0.473, +0.576] | 0.20 | 0.422 | -7.88% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (72/500)** · SD observada 0.77 -> efecto minimo detectable con n=500: 0.10 pts
- Brazo B (B@D): **EN CURSO (68/500)** · SD observada 0.53 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (80/500)** · SD observada 1.91 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.007, t = -0.35
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.004, t = -0.19

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 14204 en 183 partidos · cambios de lesiones registrados: 1268

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._