# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **161** · ventana E (24 h) **170**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 202 · capturados **161 (80%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 202 · capturados **170 (84%)** · sin cuotas 25 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 120 | +0.017 | [-0.133, +0.167] | 0.22 | 0.413 | -6.49% |
| A (A@D) | 2 | 88 | -0.023 | [-0.218, +0.173] | -0.23 | 0.591 | -0.59% |
| A (A@D) | 3 | 60 | +0.017 | [-0.250, +0.284] | 0.12 | 0.450 | +1.31% |
| B (B@D) | 1 | 121 | -0.107 | [-0.259, +0.045] | -1.40 | 0.918 | -8.75% |
| B (B@D) | 2 | 85 | -0.071 | [-0.226, +0.085] | -0.90 | 0.816 | -5.90% |
| B (B@D) | 3 | 64 | -0.016 | [-0.202, +0.171] | -0.17 | 0.566 | -4.76% |
| C (A@E) | 1 | 130 | +0.177 | [-0.140, +0.493] | 1.11 | 0.135 | -29.56% |
| C (A@E) | 2 | 90 | +0.089 | [-0.295, +0.473] | 0.46 | 0.323 | -15.12% |
| C (A@E) | 3 | 64 | +0.125 | [-0.353, +0.603] | 0.52 | 0.302 | -4.64% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (88/500)** · SD observada 0.92 -> efecto minimo detectable con n=500: 0.12 pts
- Brazo B (B@D): **EN CURSO (85/500)** · SD observada 0.72 -> efecto minimo detectable con n=500: 0.10 pts
- Brazo C (A@E): **EN CURSO (90/500)** · SD observada 1.83 -> efecto minimo detectable con n=500: 0.24 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.008, t = -0.42
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.011, t = -0.51

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 17840 en 209 partidos · cambios de lesiones registrados: 1493

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._