# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **26** · ventana E (24 h) **48**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 62 · capturados **26 (42%)** · sin cuotas 10 · perdidos por el cron 15 · respaldo DX 11
- Ventana E (~24 h antes): observados 62 · capturados **48 (77%)** · sin cuotas 7 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 17 | -0.118 | [-0.367, +0.132] | -1.00 | 0.834 | -44.42% |
| A (A@D) | 2 | 14 | -0.071 | [-0.345, +0.203] | -0.56 | 0.709 | -32.51% |
| A (A@D) | 3 | 10 | -0.100 | [-0.326, +0.126] | -1.00 | 0.828 | -23.99% |
| B (B@D) | 1 | 15 | +0.133 | [-0.328, +0.595] | 0.62 | 0.273 | -12.44% |
| B (B@D) | 2 | 12 | -0.083 | [-0.267, +0.100] | -1.00 | 0.831 | -21.40% |
| B (B@D) | 3 | 10 | +nan | [+nan, +nan] | nan | nan | -5.68% |
| C (A@E) | 1 | 37 | -0.108 | [-0.640, +0.424] | -0.41 | 0.659 | -38.34% |
| C (A@E) | 2 | 25 | -0.160 | [-0.872, +0.552] | -0.46 | 0.677 | -24.03% |
| C (A@E) | 3 | 19 | +0.000 | [-0.682, +0.682] | 0.00 | 0.500 | -9.87% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (14/500)** · SD observada 0.47 -> efecto minimo detectable con n=500: 0.06 pts
- Brazo B (B@D): **EN CURSO (12/500)** · SD observada 0.29 -> efecto minimo detectable con n=500: 0.04 pts
- Brazo C (A@E): **EN CURSO (25/500)** · SD observada 1.72 -> efecto minimo detectable con n=500: 0.23 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.007, t = -0.18
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.060, t = 0.87

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 545 en 71 partidos · cambios de lesiones registrados: 562

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._