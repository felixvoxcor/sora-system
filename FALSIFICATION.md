# Criterio de falsificación — NBA CLV Lab (pre-registrado)

**Fecha de registro:** 2026-10-17 · **Versión del modelo:** v1.0 · **Primer partido rastreado:** 2026-10-20

Este documento se escribió ANTES de ver un solo resultado en vivo. No se edita después de que
empiece la temporada. Cualquier cambio de parámetros crea una versión nueva (v1.1…) y reinicia el contador.

## Hipótesis
- **H_A:** un modelo de ratings de margen (sin lesiones) obtiene CLV positivo respecto a la línea de cierre.
- **H_B:** el mismo modelo + capa de lesiones obtiene CLV positivo (el mercado tarda en incorporar noticias de lesiones).

Antecedente (backtest 2023-26, 2.643 partidos): el modelo no supera a la línea de cierre en error de margen
(RMSE 14,45 vs 13,90); contra la apertura hay CLV positivo (+0,48 pts) pero decae por temporada
(+0,81 en 2024, +0,16 en 2025). La prior de que H_A sea cierta es baja. H_B no tiene backtest posible
(no hay lesiones históricas) y solo se puede probar en vivo.

## Parámetros congelados (v1.0)
| Parámetro | Valor |
|---|---|
| K de ratings | 0,05 |
| Regresión entre temporadas | 0,5 |
| Ventaja de local | 2,5 pts |
| Tope de margen | 25 |
| Beta de lesiones | 3,0 pts por jugador de 36 min fuera (cuadrático en minutos) |
| P(fuera) | Out = 1,0 · Day-To-Day = 0,25 |
| Minutos por jugador | promedio de sus últimas 10 apariciones |

## Medición
- Se usa solo el snapshot **D** (entre 3 h y 45 min antes del tip). El snapshot E (≈24 h antes) es exploratorio.
- `edge = predicción − línea` (en margen esperado del local). Apuesta hipotética al lado del edge si `|edge| ≥ 2` (umbral primario).
- **CLV** = `lado × (línea de cierre − línea del snapshot)`, mismo proveedor cuando es posible.
- El ROI en papel usa el precio del snapshot; es informativo, no es criterio de decisión.

## Decisión
- Prueba t de una cola sobre el CLV medio, **α = 0,025 por brazo** (Bonferroni entre A y B).
- **n = 300** apuestas hipotéticas con `|edge| ≥ 2` por brazo.
  - CLV medio > 0 **y** p < 0,025 → el brazo **PASA** a fase 2 (ver abajo).
  - Cualquier otro resultado → el brazo se **ARCHIVA**. No se reintenta con otros umbrales.
- **Futilidad:** en n = 150, si CLV medio < −0,10 → se archiva sin esperar.
- Los demás umbrales (1 y 3) y la prueba de liderazgo son exploratorios y no cambian el veredicto.

## Fase 2 (solo si un brazo pasa)
1. Replicar en una segunda ventana de 300 apuestas sin tocar parámetros.
2. Recién entonces, evaluar apuestas con dinero real mínimo, con precio verificable en el libro donde se apuesta.

## Prohibido
- Cambiar parámetros, umbrales o el brazo primario después de ver resultados.
- Elegir el mejor umbral o brazo a posteriori.
- Apostar dinero real antes de cumplir la Fase 2.
