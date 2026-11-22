# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **197** · ventana E (24 h) **204**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 238 · capturados **197 (83%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 238 · capturados **204 (86%)** · sin cuotas 27 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 145 | +0.090 | [-0.081, +0.260] | 1.04 | 0.151 | -12.03% |
| A (A@D) | 2 | 106 | +0.047 | [-0.176, +0.270] | 0.42 | 0.338 | -6.71% |
| A (A@D) | 3 | 66 | +0.000 | [-0.244, +0.244] | 0.00 | 0.500 | -4.95% |
| B (B@D) | 1 | 147 | -0.054 | [-0.226, +0.117] | -0.63 | 0.734 | -6.70% |
| B (B@D) | 2 | 103 | +0.019 | [-0.164, +0.203] | 0.21 | 0.417 | -3.85% |
| B (B@D) | 3 | 70 | +0.014 | [-0.165, +0.194] | 0.16 | 0.437 | -2.12% |
| C (A@E) | 1 | 150 | +0.267 | [-0.034, +0.567] | 1.75 | 0.041 | -32.60% |
| C (A@E) | 2 | 100 | +0.230 | [-0.144, +0.604] | 1.22 | 0.113 | -19.83% |
| C (A@E) | 3 | 70 | +0.200 | [-0.246, +0.646] | 0.89 | 0.187 | -7.40% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (106/500)** · SD observada 1.16 -> efecto minimo detectable con n=500: 0.15 pts
- Brazo B (B@D): **EN CURSO (103/500)** · SD observada 0.94 -> efecto minimo detectable con n=500: 0.12 pts
- Brazo C (A@E): **EN CURSO (100/500)** · SD observada 1.88 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente 0.001, t = 0.02
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.009, t = -0.39

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 22400 en 246 partidos · cambios de lesiones registrados: 1731

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._