"""NBA CLV Lab: rastreador de CLV con criterio de falsificacion pre-registrado."""
MODEL_VERSION = "v1.1"   # v1.1 = mismo modelo que v1.0; cambia solo el protocolo (ver FALSIFICATION.md)

# ---- PARAMETROS CONGELADOS (ver FALSIFICATION.md). Cambiarlos reinicia el contador. ----
RATING_K = 0.05        # ajustado en la temporada 2023-24 solamente
RATING_CARRY = 0.5     # regresion a la media entre temporadas
HOME_ADV = 2.5
MARGIN_CAP = 25
INJ_BETA = 3.0         # puntos por jugador de 36 min fuera (cuadratico en minutos)
P_OUT = {"Out": 1.0, "Day-To-Day": 0.25}
NON_NBA = {"CAN", "CHK", "KEN", "SHQ"}   # equipos de All-Star / exhibicion
