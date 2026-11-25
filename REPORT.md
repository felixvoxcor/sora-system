# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **219** · ventana E (24 h) **225**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 260 · capturados **219 (84%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 260 · capturados **225 (87%)** · sin cuotas 28 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 160 | +0.050 | [-0.127, +0.227] | 0.56 | 0.289 | -8.37% |
| A (A@D) | 2 | 117 | +0.043 | [-0.174, +0.260] | 0.39 | 0.349 | -5.67% |
| A (A@D) | 3 | 74 | -0.027 | [-0.251, +0.196] | -0.24 | 0.595 | -7.55% |
| B (B@D) | 1 | 166 | +0.024 | [-0.155, +0.203] | 0.27 | 0.396 | -3.57% |
| B (B@D) | 2 | 116 | +0.069 | [-0.125, +0.263] | 0.71 | 0.241 | +1.86% |
| B (B@D) | 3 | 75 | +0.040 | [-0.162, +0.242] | 0.40 | 0.347 | -0.99% |
| C (A@E) | 1 | 168 | +0.179 | [-0.111, +0.468] | 1.22 | 0.113 | -27.29% |
| C (A@E) | 2 | 112 | +0.205 | [-0.142, +0.553] | 1.17 | 0.122 | -13.04% |
| C (A@E) | 3 | 75 | +0.187 | [-0.231, +0.604] | 0.89 | 0.188 | -3.33% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (117/500)** · SD observada 1.18 -> efecto minimo detectable con n=500: 0.16 pts
- Brazo B (B@D): **EN CURSO (116/500)** · SD observada 1.05 -> efecto minimo detectable con n=500: 0.14 pts
- Brazo C (A@E): **EN CURSO (112/500)** · SD observada 1.86 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.007, t = -0.29
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.007, t = 0.30

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 24871 en 270 partidos · cambios de lesiones registrados: 1868

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._