# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **26** · ventana E (24 h) **42**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 56 · capturados **26 (46%)** · sin cuotas 10 · perdidos por el cron 10 · respaldo DX 10
- Ventana E (~24 h antes): observados 56 · capturados **42 (75%)** · sin cuotas 7 · perdidos por el cron 0
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
| C (A@E) | 1 | 31 | +0.000 | [-0.599, +0.599] | 0.00 | 0.500 | -32.43% |
| C (A@E) | 2 | 22 | +0.000 | [-0.762, +0.762] | 0.00 | 0.500 | -13.67% |
| C (A@E) | 3 | 17 | +0.176 | [-0.485, +0.838] | 0.57 | 0.290 | +0.73% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (14/500)** · SD observada 0.47 -> efecto minimo detectable con n=500: 0.06 pts
- Brazo B (B@D): **EN CURSO (12/500)** · SD observada 0.29 -> efecto minimo detectable con n=500: 0.04 pts
- Brazo C (A@E): **EN CURSO (22/500)** · SD observada 1.72 -> efecto minimo detectable con n=500: 0.23 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.007, t = -0.18
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.060, t = 0.87

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 496 en 68 partidos · cambios de lesiones registrados: 531

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._