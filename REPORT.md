# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **18** · ventana E (24 h) **24**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 24 · capturados **18 (75%)** · sin cuotas 0 · perdidos por el cron 6 · respaldo DX 0
- Ventana E (~24 h antes): observados 24 · capturados **24 (100%)** · sin cuotas 0 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 12 | -0.083 | [-0.267, +0.100] | -1.00 | 0.831 | -36.85% |
| A (A@D) | 2 | 11 | -0.091 | [-0.293, +0.112] | -1.00 | 0.830 | -31.10% |
| A (A@D) | 3 | 8 | +nan | [+nan, +nan] | nan | nan | -28.36% |
| B (B@D) | 1 | 11 | +nan | [+nan, +nan] | nan | nan | -14.26% |
| B (B@D) | 2 | 9 | +nan | [+nan, +nan] | nan | nan | -15.97% |
| B (B@D) | 3 | 8 | +nan | [+nan, +nan] | nan | nan | -5.47% |
| C (A@E) | 1 | 17 | +0.294 | [-0.573, +1.161] | 0.72 | 0.241 | -32.87% |
| C (A@E) | 2 | 13 | +0.385 | [-0.760, +1.530] | 0.73 | 0.239 | -12.21% |
| C (A@E) | 3 | 9 | +0.556 | [-0.539, +1.650] | 1.17 | 0.138 | +6.04% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (11/500)** · SD observada 0.30 -> efecto minimo detectable con n=500: 0.04 pts
- Brazo B (B@D): **EN CURSO (9/500)**
- Brazo C (A@E): **EN CURSO (13/500)** · SD observada 1.89 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.007, t = -0.36
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.020, t = 0.54

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 250 en 36 partidos · cambios de lesiones registrados: 309

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._