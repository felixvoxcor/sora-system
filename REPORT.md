# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **51** · ventana E (24 h) **74**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 92 · capturados **51 (55%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 92 · capturados **74 (80%)** · sin cuotas 11 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 35 | +0.086 | [-0.107, +0.279] | 0.90 | 0.187 | -29.47% |
| A (A@D) | 2 | 26 | +0.077 | [-0.149, +0.303] | 0.70 | 0.245 | -26.72% |
| A (A@D) | 3 | 19 | +0.053 | [-0.200, +0.305] | 0.44 | 0.333 | -9.44% |
| B (B@D) | 1 | 36 | +0.083 | [-0.151, +0.317] | 0.72 | 0.237 | +0.15% |
| B (B@D) | 2 | 26 | +0.077 | [-0.118, +0.272] | 0.81 | 0.212 | -11.96% |
| B (B@D) | 3 | 20 | +0.150 | [-0.021, +0.321] | 1.83 | 0.041 | -4.73% |
| C (A@E) | 1 | 55 | +0.164 | [-0.337, +0.665] | 0.65 | 0.258 | -41.08% |
| C (A@E) | 2 | 39 | +0.205 | [-0.465, +0.875] | 0.62 | 0.270 | -26.71% |
| C (A@E) | 3 | 29 | +0.483 | [-0.296, +1.261] | 1.27 | 0.107 | -21.05% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (26/500)** · SD observada 0.56 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo B (B@D): **EN CURSO (26/500)** · SD observada 0.48 -> efecto minimo detectable con n=500: 0.06 pts
- Brazo C (A@E): **EN CURSO (39/500)** · SD observada 2.07 -> efecto minimo detectable con n=500: 0.27 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente 0.024, t = 0.88
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.006, t = 0.16

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 4478 en 107 partidos · cambios de lesiones registrados: 733

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._