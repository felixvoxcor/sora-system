# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **41** · ventana E (24 h) **67**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 82 · capturados **41 (50%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 82 · capturados **67 (82%)** · sin cuotas 8 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 27 | +0.037 | [-0.168, +0.242] | 0.37 | 0.356 | -29.64% |
| A (A@D) | 2 | 21 | +0.048 | [-0.179, +0.274] | 0.44 | 0.333 | -27.45% |
| A (A@D) | 3 | 15 | +0.000 | [-0.209, +0.209] | 0.00 | 0.500 | -10.75% |
| B (B@D) | 1 | 27 | +0.111 | [-0.165, +0.387] | 0.83 | 0.208 | -1.95% |
| B (B@D) | 2 | 21 | +0.048 | [-0.127, +0.223] | 0.57 | 0.288 | -9.27% |
| B (B@D) | 3 | 16 | +0.062 | [-0.071, +0.196] | 1.00 | 0.167 | +7.16% |
| C (A@E) | 1 | 50 | +0.140 | [-0.389, +0.669] | 0.53 | 0.299 | -42.91% |
| C (A@E) | 2 | 35 | +0.200 | [-0.516, +0.916] | 0.57 | 0.287 | -29.37% |
| C (A@E) | 3 | 26 | +0.423 | [-0.418, +1.264] | 1.04 | 0.155 | -19.45% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (21/500)** · SD observada 0.50 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo B (B@D): **EN CURSO (21/500)** · SD observada 0.38 -> efecto minimo detectable con n=500: 0.05 pts
- Brazo C (A@E): **EN CURSO (35/500)** · SD observada 2.08 -> efecto minimo detectable con n=500: 0.28 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente 0.013, t = 0.41
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.029, t = 0.66

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 2625 en 88 partidos · cambios de lesiones registrados: 669

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._