# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **204** · ventana E (24 h) **210**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 245 · capturados **204 (83%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 245 · capturados **210 (86%)** · sin cuotas 28 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 149 | +0.074 | [-0.094, +0.241] | 0.87 | 0.192 | -11.82% |
| A (A@D) | 2 | 108 | +0.028 | [-0.193, +0.248] | 0.25 | 0.402 | -8.44% |
| A (A@D) | 3 | 68 | -0.029 | [-0.270, +0.211] | -0.24 | 0.596 | -7.75% |
| B (B@D) | 1 | 154 | -0.065 | [-0.230, +0.101] | -0.78 | 0.780 | -4.75% |
| B (B@D) | 2 | 108 | +0.000 | [-0.179, +0.179] | 0.00 | 0.500 | -1.27% |
| B (B@D) | 3 | 71 | +0.000 | [-0.179, +0.179] | 0.00 | 0.500 | -0.85% |
| C (A@E) | 1 | 155 | +0.239 | [-0.057, +0.534] | 1.60 | 0.056 | -32.33% |
| C (A@E) | 2 | 102 | +0.216 | [-0.154, +0.585] | 1.16 | 0.125 | -19.53% |
| C (A@E) | 3 | 70 | +0.200 | [-0.246, +0.646] | 0.89 | 0.187 | -7.40% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (108/500)** · SD observada 1.16 -> efecto minimo detectable con n=500: 0.15 pts
- Brazo B (B@D): **EN CURSO (108/500)** · SD observada 0.94 -> efecto minimo detectable con n=500: 0.12 pts
- Brazo C (A@E): **EN CURSO (102/500)** · SD observada 1.88 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.003, t = -0.16
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.008, t = -0.34

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 23050 en 256 partidos · cambios de lesiones registrados: 1789

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._