# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **211** · ventana E (24 h) **217**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 252 · capturados **211 (84%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 252 · capturados **217 (86%)** · sin cuotas 28 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 154 | +0.091 | [-0.080, +0.262] | 1.05 | 0.148 | -9.78% |
| A (A@D) | 2 | 113 | +0.053 | [-0.171, +0.277] | 0.47 | 0.320 | -5.80% |
| A (A@D) | 3 | 71 | -0.028 | [-0.261, +0.205] | -0.24 | 0.595 | -6.42% |
| B (B@D) | 1 | 159 | -0.031 | [-0.201, +0.138] | -0.37 | 0.643 | -2.98% |
| B (B@D) | 2 | 112 | +0.036 | [-0.152, +0.224] | 0.38 | 0.354 | +0.31% |
| B (B@D) | 3 | 72 | -0.014 | [-0.192, +0.165] | -0.16 | 0.561 | -2.22% |
| C (A@E) | 1 | 161 | +0.224 | [-0.070, +0.517] | 1.50 | 0.067 | -30.08% |
| C (A@E) | 2 | 106 | +0.226 | [-0.137, +0.590] | 1.23 | 0.110 | -15.32% |
| C (A@E) | 3 | 72 | +0.181 | [-0.254, +0.615] | 0.83 | 0.205 | -4.61% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (113/500)** · SD observada 1.20 -> efecto minimo detectable con n=500: 0.16 pts
- Brazo B (B@D): **EN CURSO (112/500)** · SD observada 1.00 -> efecto minimo detectable con n=500: 0.13 pts
- Brazo C (A@E): **EN CURSO (106/500)** · SD observada 1.89 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente 0.004, t = 0.17
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.009, t = -0.38

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 24304 en 261 partidos · cambios de lesiones registrados: 1843

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._