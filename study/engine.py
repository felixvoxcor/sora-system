"""Motor de estudio: 16 estrategias de entrada x 5 niveles de riesgo = 80 celdas, con prueba de azar (permutaciones)."""
import bisect, math, json
import numpy as np, pandas as pd
from scipy.stats import norm
import signals as sg

RNG = np.random.default_rng(7)
OOS_FROM = 2024                    # 2023 = calentamiento (ridge, percentiles). 2024 y 2025 = evaluacion.
MIN_PRIOR = 150                    # fuerzas previas necesarias para calcular el percentil de una senal
WIN110 = 100.0 / 110.0
LEVELS = {   # nivel: (rango 1-100, nombre, percentil minimo de confianza, % del bankroll por apuesta)
    1: ("1-20", "Temerario", 0, 3.0),
    2: ("21-40", "Agresivo", 40, 2.0),
    3: ("41-60", "Equilibrado", 60, 1.0),
    4: ("61-80", "Prudente", 80, 0.5),
    5: ("81-100", "Conservador", 95, 0.25)}
RUIN_LEVEL = 25.0                  # bankroll inicial 100; "ruina" = caer por debajo de 25


def am_to_dec_profit(px):
    px = np.asarray(px, float)
    return np.where(px > 0, px / 100.0, 100.0 / np.abs(px))


def am_to_prob(px):
    px = np.asarray(px, float)
    return np.where(px > 0, 100.0 / (px + 100.0), np.abs(px) / (np.abs(px) + 100.0))


# ------------------------------------------------------------------ estrategias
def build_strategies(df, S):
    n = len(df)
    line, lopen, tclose = df.line.values, df.line_open.values, df.total_close.values
    y_close, y_open = df.res_m.values, (df.margin - df.line_open).values
    ya_t = df.res_t.values
    base = dict(m0g_close=(S.m0 - df.line).values, m0g_open=(S.m0 - df.line_open).values)
    rest = np.c_[S.rest_b2b, S.rest_g4, S.rest_days]
    X_all_close = np.c_[base["m0g_close"], S.abs_diff, S.pl_gap, S.ff_gap, rest, S.ref_m]
    X_all_open = np.c_[base["m0g_open"], S.abs_diff, S.pl_gap, S.ff_gap, rest, S.ref_m]
    t_gap = (S.t0 - df.total_close).values
    st = {}

    def add(name, kind, yhat, desc, line_used=None, price=None, family=True):
        yhat = np.asarray(yhat, float)
        side = np.where(np.isnan(yhat), 0, np.sign(yhat)).astype(int)
        st[name] = dict(kind=kind, side=side, strength=np.abs(np.nan_to_num(yhat)), desc=desc,
                        line_used=line_used, price=price, family=family)

    add("ST_RATING", "S", sg.wf_ridge(base["m0g_close"], y_close), "Spread al cierre: ratings de margen", line)
    add("ST_ABS", "S", sg.wf_ridge(S.abs_diff.values, y_close), "Spread al cierre: ausencias de jugadores clave", line)
    add("ST_PLAYER", "S", sg.wf_ridge(S.pl_gap.values, y_close), "Spread al cierre: valor individual de jugadores (+/-)", line)
    add("ST_FF", "S", sg.wf_ridge(S.ff_gap.values, y_close), "Spread al cierre: four factors (tiro, perdidas, rebote, tiros libres)", line)
    add("ST_REF", "S", sg.wf_ridge(S.ref_m.values, y_close), "Spread al cierre: sesgo del trio arbitral", line)
    add("ST_REST", "S", sg.wf_ridge(rest, y_close), "Spread al cierre: descanso / back-to-back", line)
    add("ST_ENS", "S", sg.wf_ridge(X_all_close, y_close), "Spread al cierre: todas las senales combinadas", line)
    add("ST_ENS_OPEN", "S", sg.wf_ridge(X_all_open, y_open), "Spread a la APERTURA: todas las senales combinadas", lopen)
    add("TT_MODEL", "T", sg.wf_ridge(t_gap, ya_t), "Total: modelo ofensiva/defensiva por equipo", tclose)
    add("TT_REF", "T", sg.wf_ridge(S.ref_t.values, ya_t), "Total: efecto del trio arbitral", tclose)
    add("TT_ENS", "T", sg.wf_ridge(np.c_[t_gap, S.ref_t, S.ff_gap], ya_t), "Total: modelo + arbitros + four factors", tclose)
    # moneyline: valor = prob. del modelo - prob. implicita sin vig
    yh = sg.wf_ridge(X_all_close, y_close)
    pm = norm.cdf((line + np.nan_to_num(yh)) / 12.5)
    ph, pa = am_to_prob(df.h_ml_close.values), am_to_prob(df.a_ml_close.values)
    pimp = ph / (ph + pa)
    edge = np.where(np.isnan(yh), np.nan, pm - pimp)
    add("ML_ENS", "M", edge, "Moneyline: prob. del modelo vs prob. implicita sin vig", None,
        np.c_[df.h_ml_close.values, df.a_ml_close.values])
    mv = line - lopen
    add("STEAM_FOLLOW", "S", np.where(mv == 0, np.nan, mv), "Spread al cierre: seguir el movimiento de la linea (apertura->cierre)", line)
    add("STEAM_FADE", "S", np.where(mv == 0, np.nan, -mv), "Spread al cierre: ir contra el movimiento de la linea", line)
    # controles (no entran a la familia de hallazgos)
    add("CTRL_HOME", "S", RNG.uniform(0.1, 1, n), "CONTROL: siempre local al cierre", line, family=False)
    add("CTRL_RANDOM", "S", RNG.choice([-1, 1], n) * RNG.uniform(0.1, 1, n), "CONTROL: lado y confianza al azar", line, family=False)
    plant = 0.30 * df.res_m.values + RNG.normal(0, 13, n)
    add("PLANT", "S", plant, "VALIDACION: senal con ventaja real sembrada", line, family=False)
    return st


# ------------------------------------------------------------------ niveles
PCT_WINDOW = 400                   # los percentiles se miden contra las ultimas 400 fuerzas (las senales cambian de escala con el tiempo)


def percentiles(strength, side, start=0):
    """Percentil (0-100) de la fuerza de cada partido respecto a las fuerzas PREVIAS recientes de la misma estrategia."""
    from collections import deque
    pct = np.full(len(strength), np.nan)
    win, srt = deque(), []
    for i in range(len(strength)):
        if side[i] == 0:
            continue
        x = strength[i]
        if len(srt) >= MIN_PRIOR:
            pct[i] = 100.0 * (bisect.bisect_left(srt, x) + bisect.bisect_right(srt, x)) / 2.0 / len(srt)
        bisect.insort(srt, x); win.append(x)
        if len(win) > PCT_WINDOW:
            srt.pop(bisect.bisect_left(srt, win.popleft()))
    return pct


def profits(s, idx, margin, total, line_close, tclose):
    """Ganancia en unidades por apuesta de 1u para las filas idx, dados resultados (margin, total)."""
    side = s["side"][idx]
    if s["kind"] == "S":
        d = margin[idx] - s["line_used"][idx]
        win, push = (side * d) > 0, d == 0
        return np.where(push, 0.0, np.where(win, WIN110, -1.0))
    if s["kind"] == "T":
        d = total[idx] - tclose[idx]
        win, push = (side * d) > 0, d == 0
        return np.where(push, 0.0, np.where(win, WIN110, -1.0))
    home_win = margin[idx] > 0
    win = np.where(side == 1, home_win, ~home_win)
    px = np.where(side == 1, s["price"][idx, 0], s["price"][idx, 1])
    return np.where(win, am_to_dec_profit(px), -1.0)


def bankroll_path(p, frac):
    return 100.0 * np.cumprod(1.0 + frac * p)


def cell_metrics(p, frac):
    n = len(p)
    out = dict(n=n)
    if n < 5:
        return out
    out["win"] = float((p > 0).sum() / max(1, (p != 0).sum()))
    out["roi"] = float(p.mean())
    sd = p.std(ddof=1)
    out["t"] = float(p.mean() / (sd / math.sqrt(n))) if sd > 0 else 0.0
    path = bankroll_path(p, frac)
    out["final"] = float(path[-1])
    out["maxdd"] = float((1 - path / np.maximum.accumulate(np.r_[100.0, path])[1:]).max())
    reps = 600
    ii = RNG.integers(0, n, (reps, n))
    paths = np.cumprod(1.0 + frac * p[ii], axis=1) * 100.0
    out["ruin"] = float((paths.min(axis=1) < RUIN_LEVEL).mean())
    out["p_end_profit"] = float((paths[:, -1] > 100.0).mean())
    return out


# ------------------------------------------------------------------ corrida completa
def run(df, S, n_perm=1000):
    st = build_strategies(df, S)
    margin, total = df.margin.values.astype(float), df.total.values.astype(float)
    line, tclose = df.line.values, df.total_close.values
    oos = (df.season.values >= OOS_FROM)
    seasons = df.season.values
    cells, perm_sets = [], {}
    for name, s in st.items():
        pct = percentiles(s["strength"], s["side"])
        s["pct"] = pct
        for lv, (rng_, lname, cut, stake) in LEVELS.items():
            elig = oos & ~np.isnan(pct)
            bet = elig & (pct >= cut)
            skip = elig & (pct < cut)
            ib, isk = np.where(bet)[0], np.where(skip)[0]
            p = profits(s, ib, margin, total, line, tclose)
            m = cell_metrics(p, stake / 100.0)
            row = dict(strategy=name, level=lv, level_name=lname, range=rng_, stake_pct=stake,
                       family=s["family"], **m)
            for sy in (2024, 2025):
                q = p[seasons[ib] == sy]
                row[f"roi_{sy}"], row[f"n_{sy}"] = (float(q.mean()) if len(q) else np.nan), len(q)
            if len(isk):
                ps = profits(s, isk, margin, total, line, tclose)
                row.update(skip_n=len(isk), skip_win=float((ps > 0).sum() / max(1, (ps != 0).sum())),
                           skip_roi=float(ps.mean()), skip_net=float(ps.sum()),
                           skip_won=float(ps[ps > 0].sum()), skip_lost=float(-ps[ps < 0].sum()))
            if name == "ST_ENS_OPEN" and len(ib):
                row["clv_pts"] = float((s["side"][ib] * (df.line.values[ib] - df.line_open.values[ib])).mean())
            cells.append(row)
            perm_sets[(name, lv)] = ib
    res = pd.DataFrame(cells)
    # ---------- permutaciones: se baraja el residuo (resultado vs linea) entre los partidos de evaluacion
    ioos = np.where(oos)[0]
    rm, rt = df.res_m.values[ioos], df.res_t.values[ioos]
    keys = [k for k, ib in perm_sets.items() if len(ib) >= 50]
    tmat = np.full((n_perm, len(keys)), np.nan)
    for b in range(n_perm):
        perm = RNG.permutation(len(ioos))
        m_b, t_b = margin.copy(), total.copy()
        m_b[ioos] = line[ioos] + rm[perm]
        t_b[ioos] = tclose[ioos] + rt[perm]
        for j, (name, lv) in enumerate(keys):
            p = profits(st[name], perm_sets[(name, lv)], m_b, t_b, line, tclose)
            sd = p.std(ddof=1)
            tmat[b, j] = p.mean() / (sd / math.sqrt(len(p))) if sd > 0 else 0.0
    kidx = {k: j for j, k in enumerate(keys)}
    n_ = tmat.shape[0]
    pnull = np.empty_like(tmat)
    for j in range(tmat.shape[1]):
        v = tmat[:, j]; sv = np.sort(v)
        pnull[:, j] = (1 + (n_ - np.searchsorted(sv, v, side="left"))) / (1 + n_)
    fam_cols = [j for (k, j) in kidx.items() if st[k[0]]["family"]]
    minp_null = pnull[:, fam_cols].min(axis=1)
    res["p_raw"] = np.nan; res["p_fwer"] = np.nan; res["q_bh"] = np.nan
    for i, r in res.iterrows():
        k = (r.strategy, r.level)
        if k in kidx and not np.isnan(r.get("t", np.nan)):
            j = kidx[k]
            pr = (1 + (tmat[:, j] >= r.t).sum()) / (1 + n_perm)
            res.at[i, "p_raw"] = pr
            res.at[i, "p_fwer"] = (1 + (minp_null <= pr).sum()) / (1 + n_perm)
    fam = res[res.family & res.p_raw.notna()].sort_values("p_raw")
    m = len(fam); prev = 1.0
    qs = {}
    for rank, (i, r) in reversed(list(enumerate(fam.iterrows(), 1))):
        prev = min(prev, r.p_raw * m / rank); qs[i] = prev
    for i, q in qs.items():
        res.at[i, "q_bh"] = q
    null_info = dict(minp_q05=float(np.quantile(minp_null, .05)), minp_q50=float(np.quantile(minp_null, .5)),
                     n_family_cells=len(fam_cols), n_perm=n_perm)
    return res, st, null_info
