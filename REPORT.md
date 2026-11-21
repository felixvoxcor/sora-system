# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **194** · ventana E (24 h) **202**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 235 · capturados **194 (83%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 235 · capturados **202 (86%)** · sin cuotas 26 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 144 | +0.118 | [-0.044, +0.280] | 1.44 | 0.076 | -11.42% |
| A (A@D) | 2 | 105 | +0.086 | [-0.126, +0.297] | 0.80 | 0.212 | -5.82% |
| A (A@D) | 3 | 66 | +0.000 | [-0.244, +0.244] | 0.00 | 0.500 | -4.95% |
| B (B@D) | 1 | 145 | -0.028 | [-0.193, +0.138] | -0.33 | 0.629 | -6.69% |
| B (B@D) | 2 | 102 | +0.020 | [-0.166, +0.205] | 0.21 | 0.417 | -4.71% |
| B (B@D) | 3 | 69 | +0.014 | [-0.167, +0.196] | 0.16 | 0.437 | -3.38% |
| C (A@E) | 1 | 150 | +0.267 | [-0.034, +0.567] | 1.75 | 0.041 | -32.60% |
| C (A@E) | 2 | 100 | +0.230 | [-0.144, +0.604] | 1.22 | 0.113 | -19.83% |
| C (A@E) | 3 | 70 | +0.200 | [-0.246, +0.646] | 0.89 | 0.187 | -7.40% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (105/500)** · SD observada 1.09 -> efecto minimo detectable con n=500: 0.15 pts
- Brazo B (B@D): **EN CURSO (102/500)** · SD observada 0.94 -> efecto minimo detectable con n=500: 0.13 pts
- Brazo C (A@E): **EN CURSO (100/500)** · SD observada 1.88 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente 0.003, t = 0.15
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.012, t = -0.53

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 21976 en 241 partidos · cambios de lesiones registrados: 1688

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._