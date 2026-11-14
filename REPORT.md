# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **141** · ventana E (24 h) **159**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 182 · capturados **141 (77%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 182 · capturados **159 (87%)** · sin cuotas 16 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 105 | -0.019 | [-0.153, +0.115] | -0.28 | 0.611 | -11.18% |
| A (A@D) | 2 | 79 | -0.076 | [-0.243, +0.091] | -0.90 | 0.815 | -6.07% |
| A (A@D) | 3 | 53 | -0.057 | [-0.282, +0.169] | -0.50 | 0.692 | -6.71% |
| B (B@D) | 1 | 106 | -0.113 | [-0.250, +0.023] | -1.65 | 0.949 | -8.32% |
| B (B@D) | 2 | 73 | -0.041 | [-0.167, +0.085] | -0.65 | 0.742 | -5.97% |
| B (B@D) | 3 | 56 | +0.000 | [-0.135, +0.135] | 0.00 | 0.500 | -4.64% |
| C (A@E) | 1 | 121 | +0.174 | [-0.160, +0.507] | 1.03 | 0.152 | -29.06% |
| C (A@E) | 2 | 88 | +0.068 | [-0.324, +0.460] | 0.35 | 0.365 | -17.53% |
| C (A@E) | 3 | 63 | +0.111 | [-0.374, +0.596] | 0.46 | 0.324 | -6.15% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (79/500)** · SD observada 0.75 -> efecto minimo detectable con n=500: 0.10 pts
- Brazo B (B@D): **EN CURSO (73/500)** · SD observada 0.54 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (88/500)** · SD observada 1.85 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.004, t = -0.23
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.007, t = -0.35

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 15322 en 187 partidos · cambios de lesiones registrados: 1302

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._