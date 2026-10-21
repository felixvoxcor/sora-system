# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **3** · ventana E (24 h) **3**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 3 · capturados **3 (100%)** · sin cuotas 0 · perdidos por el cron 0 · respaldo DX 0
- Ventana E (~24 h antes): observados 3 · capturados **3 (100%)** · sin cuotas 0 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 3 | +nan | [+nan, +nan] | nan | nan | -34.92% |
| A (A@D) | 2 | 3 | +nan | [+nan, +nan] | nan | nan | -34.92% |
| A (A@D) | 3 | 3 | +nan | [+nan, +nan] | nan | nan | -34.92% |
| B (B@D) | 1 | 3 | +nan | [+nan, +nan] | nan | nan | -34.92% |
| B (B@D) | 2 | 3 | +nan | [+nan, +nan] | nan | nan | -34.92% |
| B (B@D) | 3 | 2 | +nan | [+nan, +nan] | nan | nan | -2.38% |
| C (A@E) | 1 | 3 | -1.333 | [-7.070, +4.404] | -1.00 | 0.789 | -37.68% |
| C (A@E) | 2 | 3 | -1.333 | [-7.070, +4.404] | -1.00 | 0.789 | -37.68% |
| C (A@E) | 3 | 2 | +nan | [+nan, +nan] | nan | nan | -6.52% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (3/500)**
- Brazo B (B@D): **EN CURSO (3/500)**
- Brazo C (A@E): **EN CURSO (3/500)** · SD observada 2.31 -> efecto minimo detectable con n=500: 0.31 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente nan, t = nan
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente nan, t = nan

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 91 en 14 partidos · cambios de lesiones registrados: 173

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._