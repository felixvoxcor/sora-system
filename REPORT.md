# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **217** · ventana E (24 h) **223**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 258 · capturados **217 (84%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 258 · capturados **223 (86%)** · sin cuotas 28 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 158 | +0.082 | [-0.085, +0.250] | 0.97 | 0.166 | -8.39% |
| A (A@D) | 2 | 116 | +0.043 | [-0.176, +0.262] | 0.39 | 0.349 | -4.86% |
| A (A@D) | 3 | 73 | -0.027 | [-0.254, +0.199] | -0.24 | 0.595 | -6.29% |
| B (B@D) | 1 | 164 | -0.006 | [-0.177, +0.165] | -0.07 | 0.528 | -2.39% |
| B (B@D) | 2 | 116 | +0.069 | [-0.125, +0.263] | 0.71 | 0.241 | +1.86% |
| B (B@D) | 3 | 75 | +0.040 | [-0.162, +0.242] | 0.40 | 0.347 | -0.99% |
| C (A@E) | 1 | 166 | +0.211 | [-0.076, +0.498] | 1.45 | 0.074 | -27.59% |
| C (A@E) | 2 | 111 | +0.207 | [-0.143, +0.558] | 1.17 | 0.122 | -12.25% |
| C (A@E) | 3 | 74 | +0.189 | [-0.234, +0.612] | 0.89 | 0.188 | -2.03% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (116/500)** · SD observada 1.19 -> efecto minimo detectable con n=500: 0.16 pts
- Brazo B (B@D): **EN CURSO (116/500)** · SD observada 1.05 -> efecto minimo detectable con n=500: 0.14 pts
- Brazo C (A@E): **EN CURSO (111/500)** · SD observada 1.86 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.001, t = -0.04
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.000, t = 0.00

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 24395 en 261 partidos · cambios de lesiones registrados: 1853

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._