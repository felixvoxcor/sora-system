# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **22** · ventana E (24 h) **33**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 43 · capturados **22 (51%)** · sin cuotas 5 · perdidos por el cron 10 · respaldo DX 6
- Ventana E (~24 h antes): observados 43 · capturados **33 (77%)** · sin cuotas 6 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 15 | +0.000 | [-0.209, +0.209] | 0.00 | 0.500 | -37.01% |
| A (A@D) | 2 | 13 | +0.000 | [-0.247, +0.247] | 0.00 | 0.500 | -27.32% |
| A (A@D) | 3 | 9 | +nan | [+nan, +nan] | nan | nan | -15.55% |
| B (B@D) | 1 | 12 | +nan | [+nan, +nan] | nan | nan | -5.82% |
| B (B@D) | 2 | 10 | +nan | [+nan, +nan] | nan | nan | -5.68% |
| B (B@D) | 3 | 9 | +nan | [+nan, +nan] | nan | nan | +4.80% |
| C (A@E) | 1 | 24 | +0.000 | [-0.747, +0.747] | 0.00 | 0.500 | -28.47% |
| C (A@E) | 2 | 18 | +0.111 | [-0.821, +1.044] | 0.25 | 0.402 | -15.47% |
| C (A@E) | 3 | 13 | +0.385 | [-0.453, +1.223] | 1.00 | 0.169 | +2.66% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (13/500)** · SD observada 0.41 -> efecto minimo detectable con n=500: 0.05 pts
- Brazo B (B@D): **EN CURSO (10/500)**
- Brazo C (A@E): **EN CURSO (18/500)** · SD observada 1.88 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.000, t = -0.01
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.006, t = 0.16

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 411 en 52 partidos · cambios de lesiones registrados: 444

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._