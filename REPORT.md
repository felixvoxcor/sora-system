# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **77** · ventana E (24 h) **100**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 118 · capturados **77 (65%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 118 · capturados **100 (85%)** · sin cuotas 11 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 55 | +0.055 | [-0.113, +0.222] | 0.65 | 0.259 | -13.52% |
| A (A@D) | 2 | 39 | +0.000 | [-0.210, +0.210] | 0.00 | 0.500 | -12.27% |
| A (A@D) | 3 | 27 | +0.000 | [-0.269, +0.269] | 0.00 | 0.500 | -1.51% |
| B (B@D) | 1 | 56 | -0.054 | [-0.234, +0.126] | -0.60 | 0.723 | -11.92% |
| B (B@D) | 2 | 36 | -0.028 | [-0.217, +0.162] | -0.30 | 0.616 | -10.13% |
| B (B@D) | 3 | 25 | +0.040 | [-0.182, +0.262] | 0.37 | 0.357 | -8.73% |
| C (A@E) | 1 | 75 | +0.173 | [-0.222, +0.569] | 0.87 | 0.193 | -28.79% |
| C (A@E) | 2 | 52 | +0.173 | [-0.361, +0.707] | 0.65 | 0.259 | -15.67% |
| C (A@E) | 3 | 39 | +0.359 | [-0.270, +0.988] | 1.16 | 0.128 | -7.15% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (39/500)** · SD observada 0.65 -> efecto minimo detectable con n=500: 0.09 pts
- Brazo B (B@D): **EN CURSO (36/500)** · SD observada 0.56 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (52/500)** · SD observada 1.92 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente 0.013, t = 0.52
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.011, t = -0.42

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 7144 en 121 partidos · cambios de lesiones registrados: 890

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._