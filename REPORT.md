# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **200** · ventana E (24 h) **207**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 241 · capturados **200 (83%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 241 · capturados **207 (86%)** · sin cuotas 27 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 146 | +0.082 | [-0.088, +0.252] | 0.95 | 0.171 | -12.64% |
| A (A@D) | 2 | 107 | +0.037 | [-0.184, +0.259] | 0.33 | 0.369 | -7.58% |
| A (A@D) | 3 | 67 | -0.015 | [-0.257, +0.227] | -0.12 | 0.549 | -6.37% |
| B (B@D) | 1 | 150 | -0.067 | [-0.236, +0.102] | -0.78 | 0.782 | -6.01% |
| B (B@D) | 2 | 106 | +0.000 | [-0.180, +0.180] | 0.00 | 0.500 | -2.95% |
| B (B@D) | 3 | 70 | +0.014 | [-0.165, +0.194] | 0.16 | 0.437 | -2.12% |
| C (A@E) | 1 | 152 | +0.250 | [-0.050, +0.550] | 1.65 | 0.051 | -33.49% |
| C (A@E) | 2 | 100 | +0.230 | [-0.144, +0.604] | 1.22 | 0.113 | -19.83% |
| C (A@E) | 3 | 70 | +0.200 | [-0.246, +0.646] | 0.89 | 0.187 | -7.40% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (107/500)** · SD observada 1.16 -> efecto minimo detectable con n=500: 0.15 pts
- Brazo B (B@D): **EN CURSO (106/500)** · SD observada 0.94 -> efecto minimo detectable con n=500: 0.12 pts
- Brazo C (A@E): **EN CURSO (100/500)** · SD observada 1.88 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.002, t = -0.07
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.010, t = -0.43

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 22691 en 248 partidos · cambios de lesiones registrados: 1746

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._