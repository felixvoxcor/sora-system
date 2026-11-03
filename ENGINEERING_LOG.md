# Registro de ingeniería (no son cambios de protocolo)

## 2026-10-29 · v1.3 de infraestructura
**Problema.** En 11 días GitHub ejecutó 89 corridas programadas de ~500 esperadas. La ventana D (1–2 h antes del tip) quedó en 40% de cobertura (mínimo exigido: 80%); 17 de 68 partidos se perdieron por el cron.
**Cambio.** Comando `watch`: sondeo cada 3 min durante ~5.5 h por sesión, con liquidación cada 20 min y publicación a git cada 45 min. El workflow se encadena solo (dispatch al terminar) y el cron horario es respaldo. En repo privado se mantiene una pasada por corrida (el plan gratuito no alcanza para sondeo continuo).
**Efecto sobre el protocolo.** Ninguno en modelo, umbrales, brazos ni ventanas. Sí cambia *cuándo* dentro de la ventana D se toma la captura: con sondeo continuo es la primera dentro de 1–2 h (cerca de 2 h), antes caía en un punto aleatorio. Es la misma ventana pre-registrada; se anota por transparencia.
**Añadido.** `poll_log` (latido de cada sondeo, para atribuir capturas perdidas), `line_path` con moneyline y over/under, `paper_eval` y modelo de totales (ver `PAPER_BETS.md`). Los snapshots A/B/C no cambian.

## 2026-11-02 · hueco del 30-oct (corregido)
**Qué pasó.** Una corrida programada quedó en cola detrás de la sesión en curso. GitHub hace `checkout` del commit del momento del disparo, así que arrancó con una `lab.db` vieja (de las 06:41 UTC). Su primer `git pull --rebase` reemplazó el archivo bajo la conexión abierta: la base quedó "readonly" y la sesión no pudo escribir durante ~5.6 h, y esa primera publicación pisó los datos de 06:41–08:14 UTC.
**Datos perdidos.** Sondeos y trayectoria de línea de 06:41 a 13:55 UTC del 30-oct (sin partidos en juego a esa hora; ninguna captura D ni E, ni evaluación de apuestas ficticias, cae en esa franja). No se recuperan: restaurarlos por PR chocaría con las publicaciones del bot.
**Arreglo.** (1) `checkout` de la punta actual de la rama, no del commit del disparo. (2) Tras cada publicación a git la conexión a SQLite se reabre. (3) Si un sondeo falla con "readonly"/"disk I/O" la conexión se reabre sola. (4) Salida sin buffer en los logs. Dos pruebas nuevas.
