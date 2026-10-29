# Registro de ingeniería (no son cambios de protocolo)

## 2026-10-29 · v1.3 de infraestructura
**Problema.** En 11 días GitHub ejecutó 89 corridas programadas de ~500 esperadas. La ventana D (1–2 h antes del tip) quedó en 40% de cobertura (mínimo exigido: 80%); 17 de 68 partidos se perdieron por el cron.
**Cambio.** Comando `watch`: sondeo cada 3 min durante ~5.5 h por sesión, con liquidación cada 20 min y publicación a git cada 45 min. El workflow se encadena solo (dispatch al terminar) y el cron horario es respaldo. En repo privado se mantiene una pasada por corrida (el plan gratuito no alcanza para sondeo continuo).
**Efecto sobre el protocolo.** Ninguno en modelo, umbrales, brazos ni ventanas. Sí cambia *cuándo* dentro de la ventana D se toma la captura: con sondeo continuo es la primera dentro de 1–2 h (cerca de 2 h), antes caía en un punto aleatorio. Es la misma ventana pre-registrada; se anota por transparencia.
**Añadido.** `poll_log` (latido de cada sondeo, para atribuir capturas perdidas), `line_path` con moneyline y over/under, `paper_eval` y modelo de totales (ver `PAPER_BETS.md`). Los snapshots A/B/C no cambian.
