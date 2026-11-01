# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **47** · ventana E (24 h) **71**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 88 · capturados **47 (53%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 88 · capturados **71 (81%)** · sin cuotas 10 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 32 | +0.062 | [-0.141, +0.266] | 0.63 | 0.268 | -28.70% |
| A (A@D) | 2 | 25 | +0.040 | [-0.182, +0.262] | 0.37 | 0.357 | -23.79% |
| A (A@D) | 3 | 18 | +0.000 | [-0.241, +0.241] | 0.00 | 0.500 | -4.41% |
| B (B@D) | 1 | 33 | +0.061 | [-0.189, +0.310] | 0.49 | 0.312 | +3.42% |
| B (B@D) | 2 | 25 | +0.040 | [-0.148, +0.228] | 0.44 | 0.332 | -8.44% |
| B (B@D) | 3 | 19 | +0.105 | [-0.047, +0.257] | 1.46 | 0.081 | +0.29% |
| C (A@E) | 1 | 54 | +0.148 | [-0.362, +0.658] | 0.58 | 0.281 | -39.99% |
| C (A@E) | 2 | 39 | +0.205 | [-0.465, +0.875] | 0.62 | 0.270 | -26.71% |
| C (A@E) | 3 | 29 | +0.483 | [-0.296, +1.261] | 1.27 | 0.107 | -21.05% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (25/500)** · SD observada 0.54 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo B (B@D): **EN CURSO (25/500)** · SD observada 0.45 -> efecto minimo detectable con n=500: 0.06 pts
- Brazo C (A@E): **EN CURSO (39/500)** · SD observada 2.07 -> efecto minimo detectable con n=500: 0.27 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente 0.015, t = 0.54
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.020, t = 0.47

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 2784 en 92 partidos · cambios de lesiones registrados: 687

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._