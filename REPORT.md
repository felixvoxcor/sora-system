# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **215** · ventana E (24 h) **221**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 256 · capturados **215 (84%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 256 · capturados **221 (86%)** · sin cuotas 28 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 157 | +0.083 | [-0.086, +0.251] | 0.97 | 0.166 | -7.81% |
| A (A@D) | 2 | 115 | +0.043 | [-0.177, +0.264] | 0.39 | 0.349 | -4.03% |
| A (A@D) | 3 | 72 | -0.028 | [-0.258, +0.202] | -0.24 | 0.595 | -4.98% |
| B (B@D) | 1 | 162 | -0.031 | [-0.197, +0.135] | -0.37 | 0.643 | -1.19% |
| B (B@D) | 2 | 115 | +0.035 | [-0.148, +0.218] | 0.38 | 0.354 | +2.75% |
| B (B@D) | 3 | 74 | -0.014 | [-0.187, +0.160] | -0.16 | 0.561 | +0.34% |
| C (A@E) | 1 | 164 | +0.232 | [-0.057, +0.520] | 1.59 | 0.057 | -27.87% |
| C (A@E) | 2 | 109 | +0.239 | [-0.116, +0.593] | 1.34 | 0.092 | -12.39% |
| C (A@E) | 3 | 74 | +0.189 | [-0.234, +0.612] | 0.89 | 0.188 | -2.03% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (115/500)** · SD observada 1.19 -> efecto minimo detectable con n=500: 0.16 pts
- Brazo B (B@D): **EN CURSO (115/500)** · SD observada 0.99 -> efecto minimo detectable con n=500: 0.13 pts
- Brazo C (A@E): **EN CURSO (109/500)** · SD observada 1.87 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente 0.002, t = 0.10
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.008, t = -0.34

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 24334 en 261 partidos · cambios de lesiones registrados: 1848

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._