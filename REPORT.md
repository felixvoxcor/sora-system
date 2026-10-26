# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **21** · ventana E (24 h) **31**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 37 · capturados **21 (57%)** · sin cuotas 4 · perdidos por el cron 10 · respaldo DX 2
- Ventana E (~24 h antes): observados 37 · capturados **31 (84%)** · sin cuotas 5 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 14 | -0.071 | [-0.226, +0.083] | -1.00 | 0.832 | -32.51% |
| A (A@D) | 2 | 12 | -0.083 | [-0.267, +0.100] | -1.00 | 0.831 | -21.27% |
| A (A@D) | 3 | 9 | +nan | [+nan, +nan] | nan | nan | -15.55% |
| B (B@D) | 1 | 12 | +nan | [+nan, +nan] | nan | nan | -5.82% |
| B (B@D) | 2 | 10 | +nan | [+nan, +nan] | nan | nan | -5.68% |
| B (B@D) | 3 | 9 | +nan | [+nan, +nan] | nan | nan | +4.80% |
| C (A@E) | 1 | 22 | -0.091 | [-0.899, +0.718] | -0.23 | 0.591 | -30.84% |
| C (A@E) | 2 | 17 | +0.059 | [-0.928, +1.046] | 0.13 | 0.451 | -10.50% |
| C (A@E) | 3 | 12 | +0.333 | [-0.579, +1.245] | 0.80 | 0.219 | +11.21% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (12/500)** · SD observada 0.29 -> efecto minimo detectable con n=500: 0.04 pts
- Brazo B (B@D): **EN CURSO (10/500)**
- Brazo C (A@E): **EN CURSO (17/500)** · SD observada 1.92 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.007, t = -0.38
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.018, t = 0.56

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 366 en 46 partidos · cambios de lesiones registrados: 423

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._