# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **169** · ventana E (24 h) **178**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 210 · capturados **169 (80%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 210 · capturados **178 (85%)** · sin cuotas 25 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 127 | +0.047 | [-0.101, +0.195] | 0.63 | 0.265 | -7.02% |
| A (A@D) | 2 | 91 | -0.022 | [-0.211, +0.167] | -0.23 | 0.591 | -1.74% |
| A (A@D) | 3 | 62 | +0.016 | [-0.242, +0.274] | 0.12 | 0.450 | +1.18% |
| B (B@D) | 1 | 127 | -0.134 | [-0.285, +0.017] | -1.76 | 0.959 | -8.48% |
| B (B@D) | 2 | 89 | -0.090 | [-0.244, +0.065] | -1.16 | 0.875 | -5.78% |
| B (B@D) | 3 | 65 | -0.015 | [-0.199, +0.168] | -0.17 | 0.566 | -6.22% |
| C (A@E) | 1 | 135 | +0.185 | [-0.123, +0.493] | 1.19 | 0.118 | -30.76% |
| C (A@E) | 2 | 92 | +0.098 | [-0.278, +0.474] | 0.52 | 0.303 | -14.89% |
| C (A@E) | 3 | 65 | +0.138 | [-0.333, +0.610] | 0.59 | 0.280 | -3.17% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (91/500)** · SD observada 0.91 -> efecto minimo detectable con n=500: 0.12 pts
- Brazo B (B@D): **EN CURSO (89/500)** · SD observada 0.73 -> efecto minimo detectable con n=500: 0.10 pts
- Brazo C (A@E): **EN CURSO (92/500)** · SD observada 1.82 -> efecto minimo detectable con n=500: 0.24 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.007, t = -0.37
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.019, t = -0.90

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 19250 en 222 partidos · cambios de lesiones registrados: 1537

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._