# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **19** · ventana E (24 h) **28**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 28 · capturados **19 (68%)** · sin cuotas 0 · perdidos por el cron 9 · respaldo DX 0
- Ventana E (~24 h antes): observados 28 · capturados **28 (100%)** · sin cuotas 0 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 13 | -0.077 | [-0.245, +0.091] | -1.00 | 0.831 | -41.70% |
| A (A@D) | 2 | 11 | -0.091 | [-0.293, +0.112] | -1.00 | 0.830 | -31.10% |
| A (A@D) | 3 | 8 | +nan | [+nan, +nan] | nan | nan | -28.36% |
| B (B@D) | 1 | 11 | +nan | [+nan, +nan] | nan | nan | -14.26% |
| B (B@D) | 2 | 9 | +nan | [+nan, +nan] | nan | nan | -15.97% |
| B (B@D) | 3 | 8 | +nan | [+nan, +nan] | nan | nan | -5.47% |
| C (A@E) | 1 | 19 | +0.211 | [-0.602, +1.023] | 0.54 | 0.296 | -29.97% |
| C (A@E) | 2 | 15 | +0.267 | [-0.769, +1.302] | 0.55 | 0.295 | -11.29% |
| C (A@E) | 3 | 11 | +0.364 | [-0.645, +1.372] | 0.80 | 0.220 | +3.97% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (11/500)** · SD observada 0.30 -> efecto minimo detectable con n=500: 0.04 pts
- Brazo B (B@D): **EN CURSO (9/500)**
- Brazo C (A@E): **EN CURSO (15/500)** · SD observada 1.87 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.007, t = -0.37
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.019, t = 0.54

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 266 en 36 partidos · cambios de lesiones registrados: 309

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._