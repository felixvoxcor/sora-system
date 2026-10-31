# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **31** · ventana E (24 h) **58**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 72 · capturados **31 (43%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 72 · capturados **58 (81%)** · sin cuotas 7 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 20 | -0.100 | [-0.309, +0.109] | -1.00 | 0.835 | -43.21% |
| A (A@D) | 2 | 16 | -0.062 | [-0.298, +0.173] | -0.56 | 0.710 | -29.02% |
| A (A@D) | 3 | 11 | -0.091 | [-0.293, +0.112] | -1.00 | 0.830 | -13.55% |
| B (B@D) | 1 | 18 | +0.111 | [-0.266, +0.488] | 0.62 | 0.271 | -5.72% |
| B (B@D) | 2 | 15 | -0.067 | [-0.210, +0.076] | -1.00 | 0.833 | -11.55% |
| B (B@D) | 3 | 12 | +nan | [+nan, +nan] | nan | nan | +10.56% |
| C (A@E) | 1 | 44 | +0.023 | [-0.532, +0.577] | 0.08 | 0.467 | -43.81% |
| C (A@E) | 2 | 30 | +0.067 | [-0.699, +0.832] | 0.18 | 0.430 | -30.32% |
| C (A@E) | 3 | 22 | +0.273 | [-0.616, +1.161] | 0.64 | 0.265 | -13.49% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (16/500)** · SD observada 0.44 -> efecto minimo detectable con n=500: 0.06 pts
- Brazo B (B@D): **EN CURSO (15/500)** · SD observada 0.26 -> efecto minimo detectable con n=500: 0.03 pts
- Brazo C (A@E): **EN CURSO (30/500)** · SD observada 2.05 -> efecto minimo detectable con n=500: 0.27 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.007, t = -0.19
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente 0.053, t = 0.90

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 1851 en 86 partidos · cambios de lesiones registrados: 639

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._