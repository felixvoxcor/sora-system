# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **207** · ventana E (24 h) **213**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 248 · capturados **207 (83%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 248 · capturados **213 (86%)** · sin cuotas 28 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 152 | +0.066 | [-0.100, +0.231] | 0.78 | 0.217 | -11.07% |
| A (A@D) | 2 | 111 | +0.018 | [-0.199, +0.235] | 0.16 | 0.435 | -7.49% |
| A (A@D) | 3 | 70 | -0.029 | [-0.265, +0.208] | -0.24 | 0.595 | -7.73% |
| B (B@D) | 1 | 156 | -0.064 | [-0.228, +0.100] | -0.77 | 0.779 | -4.78% |
| B (B@D) | 2 | 109 | -0.009 | [-0.187, +0.169] | -0.10 | 0.541 | -2.18% |
| B (B@D) | 3 | 72 | -0.014 | [-0.192, +0.165] | -0.16 | 0.561 | -2.22% |
| C (A@E) | 1 | 158 | +0.203 | [-0.093, +0.498] | 1.36 | 0.089 | -31.17% |
| C (A@E) | 2 | 104 | +0.202 | [-0.161, +0.565] | 1.10 | 0.136 | -17.36% |
| C (A@E) | 3 | 72 | +0.181 | [-0.254, +0.615] | 0.83 | 0.205 | -4.61% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (111/500)** · SD observada 1.15 -> efecto minimo detectable con n=500: 0.15 pts
- Brazo B (B@D): **EN CURSO (109/500)** · SD observada 0.94 -> efecto minimo detectable con n=500: 0.12 pts
- Brazo C (A@E): **EN CURSO (104/500)** · SD observada 1.87 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.003, t = -0.16
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.009, t = -0.39

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 24024 en 258 partidos · cambios de lesiones registrados: 1820

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._