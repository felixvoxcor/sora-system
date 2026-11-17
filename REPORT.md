# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **164** · ventana E (24 h) **173**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 205 · capturados **164 (80%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 205 · capturados **173 (84%)** · sin cuotas 25 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 122 | +0.016 | [-0.131, +0.164] | 0.22 | 0.413 | -4.81% |
| A (A@D) | 2 | 89 | -0.022 | [-0.216, +0.171] | -0.23 | 0.591 | +0.47% |
| A (A@D) | 3 | 61 | +0.016 | [-0.246, +0.279] | 0.12 | 0.450 | +2.84% |
| B (B@D) | 1 | 122 | -0.107 | [-0.257, +0.044] | -1.40 | 0.918 | -7.91% |
| B (B@D) | 2 | 86 | -0.070 | [-0.223, +0.084] | -0.90 | 0.816 | -4.74% |
| B (B@D) | 3 | 64 | -0.016 | [-0.202, +0.171] | -0.17 | 0.566 | -4.76% |
| C (A@E) | 1 | 132 | +0.189 | [-0.123, +0.501] | 1.20 | 0.116 | -29.18% |
| C (A@E) | 2 | 91 | +0.099 | [-0.281, +0.479] | 0.52 | 0.303 | -13.96% |
| C (A@E) | 3 | 65 | +0.138 | [-0.333, +0.610] | 0.59 | 0.280 | -3.17% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (89/500)** · SD observada 0.92 -> efecto minimo detectable con n=500: 0.12 pts
- Brazo B (B@D): **EN CURSO (86/500)** · SD observada 0.72 -> efecto minimo detectable con n=500: 0.10 pts
- Brazo C (A@E): **EN CURSO (91/500)** · SD observada 1.83 -> efecto minimo detectable con n=500: 0.24 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.008, t = -0.42
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.011, t = -0.51

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 18268 en 210 partidos · cambios de lesiones registrados: 1509

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._