# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **122** · ventana E (24 h) **143**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 163 · capturados **122 (75%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 163 · capturados **143 (88%)** · sin cuotas 13 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 88 | -0.045 | [-0.199, +0.108] | -0.59 | 0.721 | -9.06% |
| A (A@D) | 2 | 66 | -0.106 | [-0.300, +0.087] | -1.09 | 0.861 | -4.71% |
| A (A@D) | 3 | 45 | -0.111 | [-0.369, +0.147] | -0.87 | 0.805 | -2.77% |
| B (B@D) | 1 | 90 | -0.133 | [-0.288, +0.021] | -1.72 | 0.955 | -8.84% |
| B (B@D) | 2 | 61 | -0.066 | [-0.205, +0.074] | -0.94 | 0.825 | -6.09% |
| B (B@D) | 3 | 47 | -0.021 | [-0.177, +0.135] | -0.27 | 0.608 | -10.54% |
| C (A@E) | 1 | 109 | +0.165 | [-0.199, +0.529] | 0.90 | 0.185 | -31.73% |
| C (A@E) | 2 | 78 | +0.000 | [-0.436, +0.436] | 0.00 | 0.500 | -19.20% |
| C (A@E) | 3 | 56 | +0.036 | [-0.507, +0.578] | 0.13 | 0.448 | -7.99% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (66/500)** · SD observada 0.79 -> efecto minimo detectable con n=500: 0.10 pts
- Brazo B (B@D): **EN CURSO (61/500)** · SD observada 0.54 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo C (A@E): **EN CURSO (78/500)** · SD observada 1.93 -> efecto minimo detectable con n=500: 0.26 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.008, t = -0.39
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.004, t = -0.20

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 13567 en 173 partidos · cambios de lesiones registrados: 1213

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._