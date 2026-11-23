# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **202** · ventana E (24 h) **209**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 243 · capturados **202 (83%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 243 · capturados **209 (86%)** · sin cuotas 27 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 147 | +0.075 | [-0.095, +0.244] | 0.87 | 0.192 | -13.23% |
| A (A@D) | 2 | 108 | +0.028 | [-0.193, +0.248] | 0.25 | 0.402 | -8.44% |
| A (A@D) | 3 | 68 | -0.029 | [-0.270, +0.211] | -0.24 | 0.596 | -7.75% |
| B (B@D) | 1 | 152 | -0.066 | [-0.233, +0.102] | -0.78 | 0.780 | -4.78% |
| B (B@D) | 2 | 108 | +0.000 | [-0.179, +0.179] | 0.00 | 0.500 | -1.27% |
| B (B@D) | 3 | 71 | +0.000 | [-0.179, +0.179] | 0.00 | 0.500 | -0.85% |
| C (A@E) | 1 | 154 | +0.234 | [-0.064, +0.531] | 1.55 | 0.061 | -33.13% |
| C (A@E) | 2 | 101 | +0.208 | [-0.165, +0.581] | 1.11 | 0.136 | -20.62% |
| C (A@E) | 3 | 70 | +0.200 | [-0.246, +0.646] | 0.89 | 0.187 | -7.40% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (108/500)** · SD observada 1.16 -> efecto minimo detectable con n=500: 0.15 pts
- Brazo B (B@D): **EN CURSO (108/500)** · SD observada 0.94 -> efecto minimo detectable con n=500: 0.12 pts
- Brazo C (A@E): **EN CURSO (101/500)** · SD observada 1.89 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.003, t = -0.16
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.008, t = -0.35

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 23030 en 255 partidos · cambios de lesiones registrados: 1789

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._