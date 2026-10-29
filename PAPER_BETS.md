# Apuestas ficticias con mercados reales (laboratorio exploratorio, p1.0)

**Qué es.** Para cada partido y en cada punto de entrada, el sistema registra con los precios reales de la casa (ESPN/DraftKings) qué habría apostado y cuánto borde tenía. Después se liquida con el resultado real. Sirve para ver cómo habría ido, qué tan eficiente es el mercado y qué ajustar.
**Qué NO es.** No toca el veredicto de `FALSIFICATION.md` v1.2 (que sigue decidiendo solo con CLV, umbral 2, brazos A/B/C). Aquí no hay umbral de "pasa": todo es exploratorio.

## Mercados y modelos
| Mercado | Modelo | Borde (puntos) | Precio usado |
|---|---|---|---|
| Spread | A (ratings) y B (A + lesiones) | modelo − línea | precio del spread del lado elegido |
| Moneyline | A y B | modelo − margen implícito del mercado sin vig (prob → margen con σ=13.8) | moneyline del lado elegido |
| Total (over/under) | T (ataque/defensa por equipo, K=0.05, carry 0.5) | total del modelo − total de la casa | overOdds / underOdds |

σ=13.8 viene del historial 2023-26 (desvío del margen contra la línea de cierre), no de datos del laboratorio. Todos los parámetros están congelados.

## Puntos de entrada (horas antes del tip)
`E` 20–26 · `H6` 5–7 · `D` 1–2 · `L` 0.1–0.5. La primera captura dentro de cada ventana fija la entrada. Derivadas: `D+conf` (en D solo si el mercado ya se movió hacia nuestro lado desde E) y `D+fade` (si se movió en contra).

## Niveles de riesgo
L1 muy selectivo … L5 casi todo. Umbral mínimo del borde en puntos: spread y ML 4·3·2·1·0.5; total 6·4·3·2·1. Unidad fija de 1u. Se guarda **la evaluación de todos los partidos, apostados o no**, en `paper_eval` (append-only con triggers); los niveles se aplican después sobre esas filas, así que no se pueden elegir a posteriori.

## Qué mide el reporte (`PAPER_REPORT.md`)
- Matriz entrada × nivel × mercado: apuestas y ROI. Celdas con menos de 30 apuestas llevan `*`.
- Corrección Benjamini-Hochberg (q=0.10) sobre todas las celdas evaluables: con decenas de celdas siempre habrá "ganadoras" por azar.
- CLV medio por entrada contra la última línea previa al tip (`line_path`).
- Eficiencia: pendiente del resultado sobre el borde (0 = mercado eficiente) y Brier del modelo vs mercado en moneyline.
- Grupo "sin apostar" (borde < L5): si ahí también hay ROI, algo está mal en la liquidación o en el modelo.

## Límites conocidos
Precios de un solo libro (DraftKings vía ESPN). Los cierres de moneyline y total son la última captura previa al tip, no un cierre oficial. Sin ajuste por límites de apuesta ni deslizamiento. Dinero real solo se prueba (ejecución) después de que un brazo de `FALSIFICATION.md` pase.
