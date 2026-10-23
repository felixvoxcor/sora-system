# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **12** · ventana E (24 h) **16**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 16 · capturados **12 (75%)** · sin cuotas 0 · perdidos por el cron 4 · respaldo DX 0
- Ventana E (~24 h antes): observados 16 · capturados **16 (100%)** · sin cuotas 0 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 7 | +nan | [+nan, +nan] | nan | nan | -44.84% |
| A (A@D) | 2 | 6 | +nan | [+nan, +nan] | nan | nan | -35.64% |
| A (A@D) | 3 | 5 | +nan | [+nan, +nan] | nan | nan | -22.77% |
| B (B@D) | 1 | 6 | +nan | [+nan, +nan] | nan | nan | -35.91% |
| B (B@D) | 2 | 5 | +nan | [+nan, +nan] | nan | nan | -23.10% |
| B (B@D) | 3 | 4 | +nan | [+nan, +nan] | nan | nan | -3.87% |
| C (A@E) | 1 | 11 | +0.182 | [-1.086, +1.450] | 0.32 | 0.378 | -30.75% |
| C (A@E) | 2 | 8 | +0.250 | [-1.579, +2.079] | 0.32 | 0.378 | -4.78% |
| C (A@E) | 3 | 5 | +1.000 | [-1.151, +3.151] | 1.29 | 0.133 | +14.96% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (6/500)**
- Brazo B (B@D): **EN CURSO (5/500)**
- Brazo C (A@E): **EN CURSO (8/500)** · SD observada 2.19 -> efecto minimo detectable con n=500: 0.29 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente 0.001, t = 0.04
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.017, t = -0.44

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 177 en 28 partidos · cambios de lesiones registrados: 259

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._