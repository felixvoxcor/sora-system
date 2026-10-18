# Criterio de falsificacion — NBA CLV Lab (pre-registrado, v1.2)

**Registro v1.2:** 2026-10-18 (antes del primer partido rastreado, 2026-10-20) · **Modelo:** v1.2 (identico a v1.0).
Las versiones v1.0 y v1.1 quedan en el historial de git. Este documento no se edita despues de que empiece la temporada.
Cualquier cambio de parametros o de protocolo crea una version nueva y reinicia el contador.

## Que cambio en v1.2 respecto a v1.1 y por que
| Cambio | Razon |
|---|---|
| **Nuevo brazo confirmatorio C** = modelo A contra la captura **E** (20-26 h antes del tip, primera captura dentro de la ventana) | La reconstruccion v2 del estudio (`study/REPORT_STUDY_V2.md`) mostro que la unica pista con algo de senal es "ratings contra una linea temprana". La captura E es una cotizacion real con hora real, no la "apertura" de ESPN |
| **Alfa por brazo = 0,05 / 3 = 0,0167** (antes 0,025 con dos brazos) | Bonferroni entre A, B y C |
| Trayectoria de la linea (`line_path`) y cambios de lesiones (`injury_log`) | Datos para el analisis posterior de las 24 horas. **Exploratorios: no deciden nada** |
| Cron: una corrida por hora tambien fuera de horario de partidos | Completar la trayectoria de 24 h y la cobertura de E |

Brazo C usa exactamente las mismas reglas que A y B: umbral primario |prediccion − linea_E| ≥ 2, CLV = lado × (cierre − linea_E),
n = 500, un unico analisis final, futilidad en n = 250 (limite superior del IC < +0,05), cobertura minima 80% de la ventana E.
El analisis de trayectoria y de factores se hace sobre datos exploratorios y **no cambia ningun veredicto ni puede abrir brazos nuevos**.

## Que cambio en v1.1 respecto a v1.0 y por que (auditoria independiente, 5 revisores, 2026-10-17)
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
- **H_A:** un modelo de ratings de margen (sin lesiones) obtiene CLV positivo respecto a la linea de cierre, entrando 1-2 h antes del tip (captura D).
- **H_B:** el mismo modelo + capa de lesiones obtiene CLV positivo en la captura D (el mercado tarda en incorporar noticias de lesiones).
- **H_C:** el modelo A obtiene CLV positivo respecto al cierre entrando ~24 h antes del tip (captura E): una linea temprana todavia no incorpora lo que los ratings saben.

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
- Brazos A y B: snapshot **D** (1-2 h antes del tip). Brazo C: snapshot **E** (~24 h). **DX** (respaldo) es exploratorio.
- `edge = prediccion − linea` (margen esperado del local). Apuesta hipotetica al lado del edge si `|edge| ≥ 2` (umbral primario unico).
- **CLV** = `lado × (linea de cierre − linea del snapshot)`, mismo proveedor cuando es posible. Convencion: `linea` = margen
  esperado del local = −spread del local (verificada por test).
- El ROI en papel usa el precio del snapshot; es informativo, no decide.

## Decision
- Prueba t de una cola sobre el CLV medio, **alfa = 0,05 / 3 = 0,0167 por brazo** (Bonferroni entre A, B y C).
- **Un unico analisis final en n = 500** apuestas hipoteticas con `|edge| ≥ 2` por brazo:
  - CLV medio > 0 **y** p < 0,0167 **y** cobertura de su ventana ≥ 80% → el brazo **PASA** a fase 2.
  - Cualquier otro resultado → **ARCHIVAR**. No se reintenta con otros umbrales ni ventanas.
- **Revision intermedia (n = 250), solo futilidad:** limite superior (97.5%, 1 cola) del CLV < +0,05 → archivar.
- Los umbrales 1 y 3, la prueba de liderazgo, DX, `line_path` e `injury_log` son exploratorios y no cambian el veredicto.
- **Cierre del programa:** si los tres brazos se archivan, no se abren brazos nuevos en 12 meses.

## Potencia (lo que este experimento puede y no puede decir)
Con n=500 y SD de CLV entre 1,5 y 2,0, el efecto minimo detectable (80% potencia, alfa 0,025) es ≈ 0,19-0,25 pts de CLV; con alfa 0,0167 (v1.2) es ≈ 0,20-0,27.
Un resultado "no significativo" significa **no hay ventaja grande**, no que no exista ninguna.

## Fase 2 (solo si un brazo pasa)
1. Replicar en una segunda ventana de n = 500 sin tocar parametros.
2. Contrastar el CLV con una referencia mas afilada (consenso de varios libros o Pinnacle) y con precios ejecutables.
3. Recien entonces, apuestas con dinero real minimo y precio verificable en el libro donde se apuesta. El proposito de ese dinero es **probar la ejecucion** (precio disponible, limites, deslizamiento), no demostrar rentabilidad: con presupuestos de unas decenas de dolares la ganancia observada no tiene valor estadistico.

## Prohibido
- Cambiar parametros, umbrales, ventanas o el brazo primario despues de ver resultados.
- Mirar resultados intermedios para declarar exito o para ajustar el diseno.
- Elegir el mejor umbral o brazo a posteriori.
- Apostar dinero real antes de cumplir la Fase 2.
