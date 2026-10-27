# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **24** · ventana E (24 h) **39**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 52 · capturados **24 (46%)** · sin cuotas 10 · perdidos por el cron 10 · respaldo DX 8
- Ventana E (~24 h antes): observados 52 · capturados **39 (75%)** · sin cuotas 7 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 15 | +0.000 | [-0.209, +0.209] | 0.00 | 0.500 | -37.01% |
| A (A@D) | 2 | 13 | +0.000 | [-0.247, +0.247] | 0.00 | 0.500 | -27.32% |
| A (A@D) | 3 | 9 | +nan | [+nan, +nan] | nan | nan | -15.55% |
| B (B@D) | 1 | 14 | +0.214 | [-0.249, +0.677] | 1.00 | 0.168 | -6.18% |
| B (B@D) | 2 | 11 | +nan | [+nan, +nan] | nan | nan | -14.26% |
| B (B@D) | 3 | 10 | +nan | [+nan, +nan] | nan | nan | -5.68% |
| C (A@E) | 1 | 28 | +0.000 | [-0.642, +0.642] | 0.00 | 0.500 | -25.19% |
| C (A@E) | 2 | 21 | +0.048 | [-0.747, +0.842] | 0.12 | 0.451 | -9.55% |
| C (A@E) | 3 | 16 | +0.250 | [-0.438, +0.938] | 0.77 | 0.225 | +7.02% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (13/500)** · SD observada 0.41 -> efecto minimo detectable con n=500: 0.05 pts
- Brazo B (B@D): **EN CURSO (11/500)**
- Brazo C (A@E): **EN CURSO (21/500)** · SD observada 1.75 -> efecto minimo detectable con n=500: 0.23 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente 0.010, t = 0.26
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.016, t = 0.22

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 459 en 61 partidos · cambios de lesiones registrados: 522

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._