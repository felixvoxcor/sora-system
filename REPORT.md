# Reporte NBA CLV Lab (protocolo v1.2)

Partidos con snapshot + cierre + resultado: ventana D **191** · ventana E (24 h) **199**

## Cobertura de las ventanas (control de sesgo de seleccion)

- Ventana D (1-2 h antes): observados 232 · capturados **191 (82%)** · sin cuotas 10 · perdidos por el cron 17 · respaldo DX 14
- Ventana E (~24 h antes): observados 232 · capturados **199 (86%)** · sin cuotas 26 · perdidos por el cron 0
- Minimo exigido: 80% en cada ventana usada.

## CLV por brazo (puntos; positivo = la linea se movio hacia nuestro lado)

| Brazo | Umbral | n | CLV medio | IC 95% | t | p (1 cola) | ROI papel (informativo) |
|---|---|---|---|---|---|---|---|
| A (A@D) | 1 | 142 | +0.099 | [-0.061, +0.258] | 1.22 | 0.112 | -10.17% |
| A (A@D) | 2 | 104 | +0.058 | [-0.148, +0.264] | 0.56 | 0.290 | -4.91% |
| A (A@D) | 3 | 66 | +0.000 | [-0.244, +0.244] | 0.00 | 0.500 | -4.95% |
| B (B@D) | 1 | 143 | -0.049 | [-0.211, +0.113] | -0.60 | 0.724 | -5.38% |
| B (B@D) | 2 | 102 | +0.020 | [-0.166, +0.205] | 0.21 | 0.417 | -4.71% |
| B (B@D) | 3 | 69 | +0.014 | [-0.167, +0.196] | 0.16 | 0.437 | -3.38% |
| C (A@E) | 1 | 148 | +0.250 | [-0.053, +0.553] | 1.63 | 0.052 | -31.69% |
| C (A@E) | 2 | 99 | +0.202 | [-0.172, +0.576] | 1.07 | 0.143 | -19.02% |
| C (A@E) | 3 | 70 | +0.200 | [-0.246, +0.646] | 0.89 | 0.187 | -7.40% |

Decide SOLO el umbral 2 y el CLV; el ROI en papel no decide nada.

## Veredicto pre-registrado (umbral primario = 2 pts, alfa por brazo = 0.0167)

- Brazo A (A@D): **EN CURSO (104/500)** · SD observada 1.06 -> efecto minimo detectable con n=500: 0.14 pts
- Brazo B (B@D): **EN CURSO (102/500)** · SD observada 0.94 -> efecto minimo detectable con n=500: 0.13 pts
- Brazo C (A@E): **EN CURSO (99/500)** · SD observada 1.87 -> efecto minimo detectable con n=500: 0.25 pts

## Prueba de liderazgo en la ventana D (exploratoria)

- Movimiento snapshot->cierre ~ (modelo A - linea): pendiente -0.002, t = -0.10
- Movimiento snapshot->cierre ~ ajuste de lesiones: pendiente -0.011, t = -0.51

## Datos para el analisis de las 24 horas (exploratorio, no decide nada)

- Puntos de trayectoria de linea: 21655 en 240 partidos · cambios de lesiones registrados: 1685

_Esto es papel, no dinero. Ninguna cifra aqui autoriza apostar hasta cumplir FALSIFICATION.md._