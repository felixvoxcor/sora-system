# Criterio de falsificacion — NBA CLV Lab (pre-registrado, v1.1)

**Registro v1.1:** 2026-10-17 (antes del primer partido rastreado, 2026-10-20) · **Modelo:** v1.1 (identico a v1.0).
La v1.0 queda en el historial de git. Este documento no se edita despues de que empiece la temporada.
Cualquier cambio de parametros o de protocolo crea una version nueva y reinicia el contador.

## Que cambio respecto a v1.0 y por que (auditoria independiente, 5 revisores, 2026-10-17)
| Cambio | Razon |
|---|---|
| **Un solo n = 500 por brazo** (antes 300 / 500 mezclados) | Potencia: con SD de CLV 1.5-2.0, n=300 detecta +0.2 pts con solo 41-64% de potencia |
| **Unica revision intermedia, solo de futilidad**, en n=250: se archiva si el limite superior (97.5%, 1 cola) del CLV < +0.05 | La regla vieja (CLV < -0.10 en n=150) casi nunca se activa con ventaja cero |
| **Nunca se declara exito antes de n=500** | Evita mirar-y-parar |
| **Ventana D = 1-2 h antes del tip** (antes 0.75-3 h) | Estandariza el momento de captura. Respaldo **DX** (30-60 min) se guarda pero NO entra al veredicto |
| **Cobertura minima 80%** de la ventana D, o el veredicto es INVALIDO | Un cron que pierde partidos no al azar sesga la muestra |
| Cron 2 veces por hora en horas de partido | Menos partidos perdidos por retrasos de GitHub Actions |
| Respuesta cruda de ESPN archivada con SHA-256 en cada snapshot | Re-auditar; detectar cambios silenciosos de formato |
| Reporte muestra IC 95% del CLV; el ROI es informativo | Reduce el sesgo de "celda bonita" |

## Estado de la evidencia previa (honestidad)
- El modelo y sus parametros se definieron con el backtest 2023-26. Este rastreador es la **primera prueba prospectiva**, pero
  no es una hipotesis generada a ciegas.
- Backtest 2023-26 (2.643 partidos): el modelo no supera al cierre (RMSE 14,45 vs 13,90). Contra la apertura de ESPN hubo CLV
  positivo (+0,48) que decae por temporada (+0,81 → +0,16); la "apertura" de ESPN no es un precio operable verificado.
- La prior de que H_A sea cierta es baja. H_B (lesiones) no tiene backtest y solo se prueba en vivo.
- El estudio amplio (rama `nba-study`) es **exploratorio y esta contaminado por fuga de informacion** en las senales de
  jugadores (ver `AUDIT_BRIEF.md`). Ninguna de sus celdas entra a este experimento.

## Hipotesis
- **H_A:** un modelo de ratings de margen (sin lesiones) obtiene CLV positivo respecto a la linea de cierre.
- **H_B:** el mismo modelo + capa de lesiones obtiene CLV positivo (el mercado tarda en incorporar noticias de lesiones).

## Parametros congelados (v1.1 = v1.0)
| Parametro | Valor |
|---|---|
| K de ratings | 0,05 |
| Regresion entre temporadas | 0,5 |
| Ventaja de local | 2,5 pts |
| Tope de margen | 25 |
| Beta de lesiones | 3,0 pts por jugador de 36 min fuera (cuadratico en minutos) |
| P(fuera) | Out = 1,0 · Day-To-Day = 0,25 |
| Minutos por jugador | promedio de sus ultimas 10 apariciones |

## Medicion
- Solo el snapshot **D** (1-2 h antes del tip). **E** (~24 h) y **DX** son exploratorios.
- `edge = prediccion − linea` (margen esperado del local). Apuesta hipotetica al lado del edge si `|edge| ≥ 2` (umbral primario unico).
- **CLV** = `lado × (linea de cierre − linea del snapshot)`, mismo proveedor cuando es posible. Convencion: `linea` = margen
  esperado del local = −spread del local (verificada por test).
- El ROI en papel usa el precio del snapshot; es informativo, no decide.

## Decision
- Prueba t de una cola sobre el CLV medio, **alfa = 0,025 por brazo** (A y B estan anidados; Bonferroni entre los dos).
- **Un unico analisis final en n = 500** apuestas hipoteticas con `|edge| ≥ 2` por brazo:
  - CLV medio > 0 **y** p < 0,025 **y** cobertura D ≥ 80% → el brazo **PASA** a fase 2.
  - Cualquier otro resultado → **ARCHIVAR**. No se reintenta con otros umbrales ni ventanas.
- **Revision intermedia (n = 250), solo futilidad:** limite superior (97.5%, 1 cola) del CLV < +0,05 → archivar.
- Los umbrales 1 y 3, la prueba de liderazgo y las etiquetas E/DX son exploratorios y no cambian el veredicto.
- **Cierre del programa:** si ambos brazos se archivan, no se abren brazos nuevos en 12 meses.

## Potencia (lo que este experimento puede y no puede decir)
Con n=500 y SD de CLV entre 1,5 y 2,0, el efecto minimo detectable (80% potencia) es ≈ 0,19-0,25 pts de CLV.
Un resultado "no significativo" significa **no hay ventaja grande**, no que no exista ninguna.

## Fase 2 (solo si un brazo pasa)
1. Replicar en una segunda ventana de n = 500 sin tocar parametros.
2. Contrastar el CLV con una referencia mas afilada (consenso de varios libros o Pinnacle) y con precios ejecutables.
3. Recien entonces, apuestas con dinero real minimo y precio verificable en el libro donde se apuesta.

## Prohibido
- Cambiar parametros, umbrales, ventanas o el brazo primario despues de ver resultados.
- Mirar resultados intermedios para declarar exito o para ajustar el diseno.
- Elegir el mejor umbral o brazo a posteriori.
- Apostar dinero real antes de cumplir la Fase 2.
