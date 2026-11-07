# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **89** · ventana E (24 h) **111**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 130 · capturados **89 (68%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 130 · capturados **111 (85%)** · sin cuotas 12 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 61 | +0.033 | [-0.122, +0.188] | 0.42 | 0.337 | -9.48% |
| A (A@D) | 2 | 43 | -0.023 | [-0.219, +0.172] | -0.24 | 0.594 | -11.45% |
| A (A@D) | 3 | 31 | -0.032 | [-0.273, +0.209] | -0.27 | 0.607 | -1.76% |
| B (B@D) | 1 | 66 | -0.045 | [-0.203, +0.113] | -0.57 | 0.716 | -10.67% |
| B (B@D) | 2 | 46 | -0.022 | [-0.181, +0.138] | -0.27 | 0.608 | -8.72% |
| B (B@D) | 3 | 33 | +0.030 | [-0.157, +0.218] | 0.33 | 0.372 | -13.16% |
| C (A@E) | 1 | 81 | +0.160 | [-0.230, +0.551] | 0.82 | 0.208 | -29.35% |
| C (A@E) | 2 | 57 | +0.123 | [-0.396, +0.642] | 0.47 | 0.319 | -16.37% |
| C (A@E) | 3 | 42 | +0.214 | [-0.392, +0.820] | 0.71 | 0.240 | -9.24% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (43/500)** · SD observada 0.64 -> efecto minimo detectable con n=500: 0.08 pts
- Brazo B (B@D): **EN CURSO (46/500)** · SD observada 0.54 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (57/500)** · SD observada 1.96 -> efecto minimo detectable con n=500: 0.26 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente 0.002, t = 0.11
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.001, t = -0.04

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 8668 en 139 partidos · cambios de lesiones registrados: 962

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._