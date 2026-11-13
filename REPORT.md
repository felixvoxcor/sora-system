# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **133** · ventana E (24 h) **151**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 174 · capturados **133 (76%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 174 · capturados **151 (87%)** · sin cuotas 16 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 99 | -0.040 | [-0.180, +0.099] | -0.58 | 0.717 | -9.60% |
| A (A@D) | 2 | 74 | -0.095 | [-0.271, +0.082] | -1.07 | 0.856 | -2.22% |
| A (A@D) | 3 | 49 | -0.082 | [-0.322, +0.159] | -0.68 | 0.751 | -2.86% |
| B (B@D) | 1 | 100 | -0.120 | [-0.262, +0.022] | -1.68 | 0.952 | -8.52% |
| B (B@D) | 2 | 69 | -0.043 | [-0.170, +0.083] | -0.69 | 0.752 | -5.99% |
| B (B@D) | 3 | 53 | -0.019 | [-0.157, +0.119] | -0.27 | 0.608 | -6.36% |
| C (A@E) | 1 | 115 | +0.157 | [-0.192, +0.505] | 0.89 | 0.188 | -28.71% |
| C (A@E) | 2 | 82 | +0.037 | [-0.380, +0.453] | 0.17 | 0.431 | -16.21% |
| C (A@E) | 3 | 60 | +0.083 | [-0.425, +0.592] | 0.33 | 0.372 | -4.64% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (74/500)** · SD observada 0.76 -> efecto minimo detectable con n=500: 0.10 pts
- Brazo B (B@D): **EN CURSO (69/500)** · SD observada 0.53 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (82/500)** · SD observada 1.90 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.007, t = -0.35
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.004, t = -0.19

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 14708 en 183 partidos · cambios de lesiones registrados: 1272

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._