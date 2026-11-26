# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **228** · ventana E (24 h) **234**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 269 · capturados **228 (85%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 269 · capturados **234 (87%)** · sin cuotas 28 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 166 | +0.054 | [-0.117, +0.226] | 0.62 | 0.267 | -7.03% |
| A (A@D) | 2 | 121 | +0.058 | [-0.153, +0.269] | 0.54 | 0.294 | -4.02% |
| A (A@D) | 3 | 75 | -0.013 | [-0.235, +0.209] | -0.12 | 0.547 | -8.78% |
| B (B@D) | 1 | 173 | +0.029 | [-0.144, +0.202] | 0.33 | 0.371 | -4.15% |
| B (B@D) | 2 | 122 | +0.066 | [-0.120, +0.251] | 0.70 | 0.243 | +0.01% |
| B (B@D) | 3 | 78 | +0.026 | [-0.170, +0.221] | 0.26 | 0.397 | +0.14% |
| C (A@E) | 1 | 177 | +0.215 | [-0.066, +0.496] | 1.51 | 0.067 | -24.52% |
| C (A@E) | 2 | 116 | +0.241 | [-0.098, +0.581] | 1.41 | 0.081 | -11.07% |
| C (A@E) | 3 | 76 | +0.197 | [-0.215, +0.610] | 0.95 | 0.172 | -2.04% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (121/500)** · SD observada 1.17 -> efecto minimo detectable con n=500: 0.16 pts
- Brazo B (B@D): **EN CURSO (122/500)** · SD observada 1.03 -> efecto minimo detectable con n=500: 0.14 pts
- Brazo C (A@E): **EN CURSO (116/500)** · SD observada 1.84 -> efecto minimo detectable con n=500: 0.24 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.002, t = -0.07
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.005, t = 0.21

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 25905 en 270 partidos · cambios de lesiones registrados: 1899

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._