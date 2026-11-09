# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **101** · ventana E (24 h) **123**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 142 · capturados **101 (71%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 142 · capturados **123 (87%)** · sin cuotas 12 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 71 | +0.000 | [-0.139, +0.139] | 0.00 | 0.500 | -6.16% |
| A (A@D) | 2 | 52 | -0.058 | [-0.227, +0.111] | -0.68 | 0.752 | -4.84% |
| A (A@D) | 3 | 37 | -0.081 | [-0.295, +0.132] | -0.77 | 0.777 | -2.32% |
| B (B@D) | 1 | 77 | -0.065 | [-0.204, +0.074] | -0.93 | 0.822 | -5.93% |
| B (B@D) | 2 | 51 | -0.039 | [-0.188, +0.109] | -0.53 | 0.701 | -6.52% |
| B (B@D) | 3 | 37 | +0.027 | [-0.139, +0.193] | 0.33 | 0.372 | -12.33% |
| C (A@E) | 1 | 91 | +0.154 | [-0.226, +0.534] | 0.80 | 0.212 | -28.72% |
| C (A@E) | 2 | 64 | +0.047 | [-0.429, +0.523] | 0.20 | 0.422 | -13.58% |
| C (A@E) | 3 | 47 | +0.128 | [-0.436, +0.691] | 0.46 | 0.325 | -6.78% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (52/500)** · SD observada 0.61 -> efecto minimo detectable con n=500: 0.08 pts
- Brazo B (B@D): **EN CURSO (51/500)** · SD observada 0.53 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (64/500)** · SD observada 1.91 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.004, t = -0.23
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.002, t = 0.10

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 10445 en 150 partidos · cambios de lesiones registrados: 1065

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._