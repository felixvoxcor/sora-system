# Estudio ampliado NBA (fase 1: backtest)

Motor que prueba **16 estrategias de entrada × 5 niveles de riesgo = 80 celdas** contra la línea de cierre,
con evaluación fuera de muestra (2024-25 y 2025-26; 2023-24 es solo calentamiento) y corrección por comparaciones múltiples.

```bash
pip install -r ../requirements.txt
python run_study.py 2000      # ~1 min; escribe REPORT_STUDY.md y cells.csv
```

| Archivo | Qué hace |
|---|---|
| `features.py` | Une cuotas, resultados, árbitros y box scores en una tabla ordenada por fecha. |
| `signals.py` | Señales walk-forward (ratings, ausencias, valor de jugadores, four factors, totales, árbitros, descanso) y ridge expansivo. |
| `engine.py` | Estrategias, niveles de riesgo (percentil de confianza + % del bankroll), simulación, bootstrap de ruina, permutaciones. |
| `run_study.py` | Genera el reporte: validación, ranking, matriz, riesgo, oportunidades no apostadas, diagnóstico de confianza. |
| `harvest_summaries.py` | Baja el summary de ESPN de cada partido (árbitros, box score, DNP). |

## Niveles de riesgo (1-100 dividido en 5)
| Nivel | Rango | Nombre | Apuesta solo si la confianza está en el percentil… | % del bankroll por apuesta |
|---|---|---|---|---|
| 1 | 1-20 | Temerario | 0+ (todo lo que tenga señal) | 3,0 |
| 2 | 21-40 | Agresivo | 40+ | 2,0 |
| 3 | 41-60 | Equilibrado | 60+ | 1,0 |
| 4 | 61-80 | Prudente | 80+ | 0,5 |
| 5 | 81-100 | Conservador | 95+ | 0,25 |

El percentil se mide contra las últimas 400 señales previas de la misma estrategia. Un nivel alto significa menos apuestas y más pequeñas, **no** apuestas seguras: en la NBA no existen.

## Garantías contra el autoengaño
- Controles (siempre local, lado al azar) deben perder ≈ el vig; una señal con ventaja sembrada (PLANT) debe detectarse.
- `p_azar` y `p_familia` salen de barajar miles de veces los resultados (min-p de Westfall-Young): solo cuenta lo que supere el techo de lo que 70 celdas producen por casualidad.
- Todo lo que aquí parezca prometedor es una **hipótesis** para confirmar en vivo, no un hallazgo.

## Limitaciones
- Spread y total se evalúan a -110 plano (ESPN no da el precio histórico fiable); el moneyline usa el precio real de cierre.
- Las entradas "al cierre" suponen que puedes apostar el número de cierre justo antes del tip.
- Las ausencias vienen del box score (DNP) del propio partido: prueban si el modelo valora bien a los jugadores, no si el mercado tarda en reaccionar a la noticia.
- Solo hay tres temporadas y las celdas comparten partidos (no son pruebas independientes).
