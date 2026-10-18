# NBA CLV Lab

Rastreador **en papel** que prueba, con datos reales y sin tocar dinero, si un modelo de NBA obtiene
*Closing Line Value* (CLV) positivo. Reemplaza los intentos anteriores (SENTINEL, SORA) que nunca se
validaron contra líneas reales.

> Resultado del backtest 2023-26: un modelo de ratings + descanso **no supera la línea de cierre**.
> Este laboratorio existe para averiguar, con evidencia y un criterio fijado de antemano, si una capa de
> lesiones sí aporta. Lee `FALSIFICATION.md` antes de interpretar cualquier número.

## Cómo funciona
| Pieza | Qué hace |
|---|---|
| `lab/ratings.py` | Ratings online de margen (brazo **A**). Nunca ve el partido que predice. |
| `lab/injury.py` | Ajuste por lesiones según minutos promedio de cada jugador (brazo **B** = A + lesiones). |
| `lab/tracker.py` | `settle` guarda resultados y líneas de cierre; `snapshot` registra predicción + línea actual. |
| `lab/store.py` | SQLite **append-only**: los snapshots no se pueden editar ni borrar. |
| `lab/report.py` | CLV medio, t, p, win%, ROI en papel y veredicto pre-registrado → `REPORT.md`. |

Snapshots: **E** (~24 h antes del tip, exploratorio), **D** (1-2 h antes, el único que cuenta) y **DX** (30-60 min, respaldo exploratorio). Brazos confirmatorios (v1.2): A y B en D, C (modelo A) en E. Se registra ademas la trayectoria de la línea (`line_path`) y los cambios de lesiones (`injury_log`) para el análisis de las 24 horas. Cada captura archiva la respuesta cruda de ESPN en `data/raw/` con su SHA-256.

## Uso local
```bash
pip install -r requirements.txt
python -m lab.tracker run        # settle + snapshot + report (la 1a vez siembra minutos de jugadores)
python -m pytest -q
```
Fuente de datos: APIs públicas de ESPN (sin API key). Datos históricos en `data/history.csv`;
`lab/fetch_history.py` baja temporadas con líneas open/close para re-hacer el backtest.

## Ejecución automática
`.github/workflows/tracker.yml` corre dos veces por hora en horas de partido (más una liquidación diaria), ejecuta los tests (sin bloquear la captura), actualiza `data/lab.db` y `REPORT.md`
y hace commit. **Los workflows programados solo corren desde la rama por defecto**: hay que fusionar esta
rama a `main` para activarlo. Costo estimado: ~1 min por corrida, ≈1.300 min/mes (el plan gratuito privado da 2.000).

## Limitaciones conocidas
- ESPN no publica lesiones históricas: la capa B **no tiene backtest**; solo se valida en vivo.
- Los minutos de los jugadores se siembran con los últimos 400 partidos (incluye playoffs, que sesgan hacia titulares).
  Jugadores nuevos o cambiados de equipo sin minutos no generan ajuste.
- La línea viene de un solo proveedor (ESPN BET / DraftKings); el CLV se mide contra el mismo proveedor cuando es posible.
- Es papel. Ninguna cifra autoriza apostar hasta cumplir la Fase 2 de `FALSIFICATION.md`.
