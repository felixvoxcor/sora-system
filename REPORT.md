# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **36** · ventana E (24 h) **63**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 77 · capturados **36 (47%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 77 · capturados **63 (82%)** · sin cuotas 7 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 22 | -0.091 | [-0.280, +0.098] | -1.00 | 0.836 | -31.00% |
| A (A@D) | 2 | 17 | -0.059 | [-0.279, +0.162] | -0.57 | 0.710 | -21.71% |
| A (A@D) | 3 | 12 | -0.083 | [-0.267, +0.100] | -1.00 | 0.831 | -4.48% |
| B (B@D) | 1 | 22 | +0.091 | [-0.212, +0.394] | 0.62 | 0.270 | +2.91% |
| B (B@D) | 2 | 17 | -0.059 | [-0.184, +0.066] | -1.00 | 0.834 | -10.48% |
| B (B@D) | 3 | 14 | +nan | [+nan, +nan] | nan | nan | +8.71% |
| C (A@E) | 1 | 47 | +0.170 | [-0.392, +0.732] | 0.61 | 0.273 | -43.33% |
| C (A@E) | 2 | 32 | +0.250 | [-0.532, +1.032] | 0.65 | 0.260 | -28.71% |
| C (A@E) | 3 | 24 | +0.500 | [-0.407, +1.407] | 1.14 | 0.133 | -12.74% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (17/500)** · SD observada 0.43 -> efecto minimo detectable con n=500: 0.06 pts
- Brazo B (B@D): **EN CURSO (17/500)** · SD observada 0.24 -> efecto minimo detectable con n=500: 0.03 pts
- Brazo C (A@E): **EN CURSO (32/500)** · SD observada 2.17 -> efecto minimo detectable con n=500: 0.29 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.005, t = -0.14
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.041, t = 0.78

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 1874 en 87 partidos · cambios de lesiones registrados: 639

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._