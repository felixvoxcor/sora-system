# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **43** · ventana E (24 h) **68**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 84 · capturados **43 (51%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 84 · capturados **68 (81%)** · sin cuotas 9 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 29 | +0.000 | [-0.203, +0.203] | 0.00 | 0.500 | -27.91% |
| A (A@D) | 2 | 23 | +0.000 | [-0.226, +0.226] | 0.00 | 0.500 | -25.46% |
| A (A@D) | 3 | 16 | -0.062 | [-0.298, +0.173] | -0.56 | 0.710 | -4.39% |
| B (B@D) | 1 | 29 | +0.069 | [-0.199, +0.337] | 0.53 | 0.301 | -2.13% |
| B (B@D) | 2 | 22 | +0.045 | [-0.121, +0.212] | 0.57 | 0.288 | -13.39% |
| B (B@D) | 3 | 17 | +0.059 | [-0.066, +0.184] | 1.00 | 0.166 | +0.85% |
| C (A@E) | 1 | 51 | +0.098 | [-0.427, +0.623] | 0.37 | 0.355 | -40.29% |
| C (A@E) | 2 | 36 | +0.139 | [-0.567, +0.845] | 0.40 | 0.346 | -26.03% |
| C (A@E) | 3 | 26 | +0.423 | [-0.418, +1.264] | 1.04 | 0.155 | -19.45% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (23/500)** · SD observada 0.52 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo B (B@D): **EN CURSO (22/500)** · SD observada 0.38 -> efecto minimo detectable con n=500: 0.05 pts
- Brazo C (A@E): **EN CURSO (36/500)** · SD observada 2.09 -> efecto minimo detectable con n=500: 0.28 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente 0.005, t = 0.15
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.036, t = 0.84

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 2641 en 88 partidos · cambios de lesiones registrados: 675

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._