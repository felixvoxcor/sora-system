# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **38** · ventana E (24 h) **65**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 79 · capturados **38 (48%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 79 · capturados **65 (82%)** · sin cuotas 7 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 24 | -0.042 | [-0.238, +0.154] | -0.44 | 0.668 | -28.73% |
| A (A@D) | 2 | 19 | +0.000 | [-0.227, +0.227] | 0.00 | 0.500 | -19.81% |
| A (A@D) | 3 | 14 | +0.000 | [-0.226, +0.226] | 0.00 | 0.500 | -4.37% |
| B (B@D) | 1 | 24 | +0.125 | [-0.162, +0.412] | 0.90 | 0.188 | +10.31% |
| B (B@D) | 2 | 19 | +0.000 | [-0.161, +0.161] | 0.00 | 0.500 | +0.29% |
| B (B@D) | 3 | 15 | +0.067 | [-0.076, +0.210] | 1.00 | 0.167 | +14.30% |
| C (A@E) | 1 | 49 | +0.143 | [-0.398, +0.683] | 0.53 | 0.299 | -41.75% |
| C (A@E) | 2 | 34 | +0.206 | [-0.532, +0.944] | 0.57 | 0.287 | -27.29% |
| C (A@E) | 3 | 25 | +0.440 | [-0.436, +1.316] | 1.04 | 0.155 | -16.23% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (19/500)** · SD observada 0.47 -> efecto minimo detectable con n=500: 0.06 pts
- Brazo B (B@D): **EN CURSO (19/500)** · SD observada 0.33 -> efecto minimo detectable con n=500: 0.04 pts
- Brazo C (A@E): **EN CURSO (34/500)** · SD observada 2.11 -> efecto minimo detectable con n=500: 0.28 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente 0.004, t = 0.12
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.050, t = 1.12

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 1930 en 87 partidos · cambios de lesiones registrados: 639

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._