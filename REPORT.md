# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **52** · ventana E (24 h) **75**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 93 · capturados **52 (56%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 93 · capturados **75 (81%)** · sin cuotas 11 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 36 | +0.083 | [-0.104, +0.271] | 0.90 | 0.187 | -26.26% |
| A (A@D) | 2 | 27 | +0.074 | [-0.143, +0.291] | 0.70 | 0.245 | -22.53% |
| A (A@D) | 3 | 20 | +0.050 | [-0.189, +0.289] | 0.44 | 0.333 | -4.66% |
| B (B@D) | 1 | 37 | +0.081 | [-0.146, +0.309] | 0.72 | 0.237 | -2.56% |
| B (B@D) | 2 | 26 | +0.077 | [-0.118, +0.272] | 0.81 | 0.212 | -11.96% |
| B (B@D) | 3 | 20 | +0.150 | [-0.021, +0.321] | 1.83 | 0.041 | -4.73% |
| C (A@E) | 1 | 56 | +0.161 | [-0.331, +0.653] | 0.65 | 0.258 | -38.65% |
| C (A@E) | 2 | 40 | +0.200 | [-0.453, +0.853] | 0.62 | 0.269 | -23.66% |
| C (A@E) | 3 | 30 | +0.467 | [-0.285, +1.218] | 1.27 | 0.107 | -17.18% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (27/500)** · SD observada 0.55 -> efecto minimo detectable con n=500: 0.07 pts
- Brazo B (B@D): **EN CURSO (26/500)** · SD observada 0.48 -> efecto minimo detectable con n=500: 0.06 pts
- Brazo C (A@E): **EN CURSO (40/500)** · SD observada 2.04 -> efecto minimo detectable con n=500: 0.27 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente 0.024, t = 0.89
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.005, t = 0.13

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 5086 en 107 partidos · cambios de lesiones registrados: 781

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._