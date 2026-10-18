"""Motor v2. Cambios respecto a v1 (por la auditoria de 5 IAs):
- senales por dia de calendario (signals2); abs_diff/pl_gap en CUARENTENA (solo controles LEAK_*)
- ST_ENS_OPEN limpio: sin senales de jugadores del propio partido ni arbitros (asignados ~9AM, despues de la apertura)
- nula correcta: se baraja el residuo respecto a la MISMA linea con que apuesta cada estrategia
  (v1 barajaba el residuo vs cierre aunque la estrategia apostara contra la apertura)
- dos esquemas de nula: permutacion iid y desplazamiento circular en el tiempo (preserva dependencia entre
  partidos de un mismo periodo); el p reportado es el MAS conservador de los dos
- t con errores estandar agrupados por dia, binomial exacta, PLANT realista (+2%, +5%) y analisis de potencia"""
import bisect, math
import numpy as np, pandas as pd
from scipy.stats import norm, binom
import signals2 as sg

RNG = np.random.default_rng(11)
OOS_FROM = 2024
MIN_PRIOR = 150
PCT_WINDOW = 400
WIN110 = 100.0 / 110.0
BE110 = 110.0 / 210.0
LEVELS = {1: ("1-20", "Temerario", 0, 3.0), 2: ("21-40", "Agresivo", 40, 2.0),
          3: ("41-60", "Equilibrado", 60, 1.0), 4: ("61-80", "Prudente", 80, 0.5),
          5: ("81-100", "Conservador", 95, 0.25)}
RUIN_LEVEL = 25.0      # "ruina" aqui = perder mas del 75% del bankroll inicial (no es ruina literal)


def am_to_dec_profit(px):
    px = np.asarray(px, float)
    return np.where(px > 0, px / 100.0, 100.0 / np.abs(px))


def am_to_prob(px):
    px = np.asarray(px, float)
    return np.where(px > 0, 100.0 / (px + 100.0), np.abs(px) / (np.abs(px) + 100.0))


def plant_signal(res_m, target_roi, sd=13.1):
    """yhat = res_m + ruido, con ruido calibrado para que apostar SIEMPRE rinda ~target_roi a -110.
    P(acierto)=0.5+arcsin(rho)/pi ; ROI = 1.909*P-1."""
    p = (1 + target_roi) / (1 + WIN110)
    rho = math.sin(math.pi * (p - 0.5))
    s = sd * math.sqrt(1.0 / rho ** 2 - 1.0)
    return res_m + RNG.normal(0, s, len(res_m))


def build_strategies(df, S):
    n, days = len(df), df.day_et.values
    line, lopen, tclose = df.line.values, df.line_open.values, df.total_close.values
    y_close, y_open, y_t = df.res_m.values, (df.margin - df.line_open).values, df.res_t.values
    g_close, g_open = (S.m0 - df.line).values, (S.m0 - df.line_open).values
    rest = np.c_[S.rest_b2b, S.rest_g4, S.rest_days]
    t_gap = (S.t0 - df.total_close).values
    W = lambda X, y: sg.wf_ridge(X, y, days)
    st = {}

    def add(name, kind, yhat, desc, key, group="real", price=None):
        yhat = np.asarray(yhat, float)
        st[name] = dict(kind=kind, side=np.where(np.isnan(yhat), 0, np.sign(yhat)).astype(int),
                        strength=np.abs(np.nan_to_num(yhat)), desc=desc, key=key, group=group,
                        family=(group == "real"), price=price)

    # ---- estrategias reales (informacion disponible antes de la linea que usan)
    X_close = np.c_[g_close, S.ff_gap, rest, S.ref_m]
    X_open = np.c_[g_open, S.ff_gap, rest]                       # sin arbitros ni jugadores
    add("ST_RATING", "S", W(g_close, y_close), "Spread al cierre: ratings de margen", "close")
    add("ST_FF", "S", W(S.ff_gap.values, y_close), "Spread al cierre: four factors", "close")
    add("ST_REF", "S", W(S.ref_m.values, y_close), "Spread al cierre: sesgo del trio arbitral", "close")
    add("ST_REST", "S", W(rest, y_close), "Spread al cierre: descanso / back-to-back", "close")
    add("ST_ENS", "S", W(X_close, y_close), "Spread al cierre: ratings+four factors+descanso+arbitros", "close")
    add("ST_ENS_OPEN", "S", W(X_open, y_open), "Spread a la APERTURA: ratings+four factors+descanso (limpio)", "open")
    add("TT_MODEL", "T", W(t_gap, y_t), "Total: modelo ofensiva/defensiva", "total")
    add("TT_REF", "T", W(S.ref_t.values, y_t), "Total: efecto del trio arbitral", "total")
    add("TT_ENS", "T", W(np.c_[t_gap, S.ref_t, S.ff_gap], y_t), "Total: modelo + arbitros + four factors", "total")
    yh = W(X_close, y_close)
    pm = norm.cdf((line + np.nan_to_num(yh)) / 12.5)
    ph, pa = am_to_prob(df.h_ml_close.values), am_to_prob(df.a_ml_close.values)
    edge = np.where(np.isnan(yh), np.nan, pm - ph / (ph + pa))
    add("ML_ENS", "M", edge, "Moneyline: prob. del modelo vs implicita sin vig", "close",
        price=np.c_[df.h_ml_close.values, df.a_ml_close.values])
    mv = line - lopen
    add("STEAM_FOLLOW", "S", np.where(mv == 0, np.nan, mv), "Al cierre: seguir el movimiento apertura->cierre (operabilidad sin verificar)", "close")
    add("STEAM_FADE", "S", np.where(mv == 0, np.nan, -mv), "Al cierre: ir contra el movimiento", "close")
    # ---- controles de FUGA CONOCIDA (positivos de fuga: deben verse 'buenos' si la fuga existe)
    X_leak_o = np.c_[g_open, S.abs_diff, S.pl_gap, S.ff_gap, rest, S.ref_m]
    X_leak_c = np.c_[g_close, S.abs_diff, S.pl_gap, S.ff_gap, rest, S.ref_m]
    add("LEAK_ENS_OPEN", "S", W(X_leak_o, y_open), "FUGA: ensemble v1 a la apertura (jugadores del propio partido)", "open", "leak")
    add("LEAK_ENS", "S", W(X_leak_c, y_close), "FUGA: ensemble v1 al cierre", "close", "leak")
    add("LEAK_ABS", "S", W(S.abs_diff.values, y_close), "FUGA: ausencias reales del partido", "close", "leak")
    add("LEAK_PLAYER", "S", W(S.pl_gap.values, y_close), "FUGA: plantilla que realmente jugo", "close", "leak")
    # ---- controles y plantas
    add("CTRL_HOME", "S", RNG.uniform(0.1, 1, n), "CONTROL: siempre local", "close", "ctrl")
    add("CTRL_RANDOM", "S", RNG.choice([-1, 1], n) * RNG.uniform(0.1, 1, n), "CONTROL: azar", "close", "ctrl")
    add("PLANT2", "S", plant_signal(y_close, 0.02), "PLANTA: ventaja real de +2% ROI (siempre apostando)", "close", "plant")
    add("PLANT5", "S", plant_signal(y_close, 0.05), "PLANTA: ventaja real de +5% ROI", "close", "plant")
    return st


def percentiles(strength, side):
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


def profits(s, idx, resid):
    """Ganancia por apuesta de 1u. resid = diccionario key->array de residuos (resultado menos la linea usada)."""
    side = s["side"][idx]
    if s["kind"] in ("S", "T"):
        d = resid[s["key"]][idx]
        win, push = (side * d) > 0, d == 0
        return np.where(push, 0.0, np.where(win, WIN110, -1.0))
    home_win = resid["ml_margin"][idx] > 0
    win = np.where(side == 1, home_win, ~home_win)
    px = np.where(side == 1, s["price"][idx, 0], s["price"][idx, 1])
    return np.where(win, am_to_dec_profit(px), -1.0)


def real_resid(df):
    return dict(close=df.res_m.values.astype(float), open=(df.margin - df.line_open).values.astype(float),
                total=df.res_t.values.astype(float), ml_margin=df.margin.values.astype(float))


def shuffled_resid(df, R, ioos, src):
    """Residuos 'nulos': la fila i de evaluacion recibe el resultado de la fila src[i]; las 3 lineas se mueven juntas."""
    out = {k: v.copy() for k, v in R.items()}
    for k in ("close", "open", "total"):
        out[k][ioos] = R[k][ioos][src]
    out["ml_margin"][ioos] = df.line.values[ioos] + R["close"][ioos][src]      # el ML usa el residuo vs cierre
    return out


def day_cluster_t(p, day_ids):
    """t con errores estandar agrupados por dia: sum(p)/sqrt(sum_dias(sum_p_dia^2))."""
    if len(p) < 5:
        return float("nan")
    mu = p.mean()
    sums_c = pd.Series(p - mu).groupby(day_ids).sum().values
    se = math.sqrt((sums_c ** 2).sum())
    return float(p.sum() / se) if se > 0 else float("nan")


def cell_metrics(p, frac, day_ids):
    n = len(p); out = dict(n=n)
    if n < 5:
        return out
    out["win"] = float((p > 0).sum() / max(1, (p != 0).sum()))
    out["roi"] = float(p.mean())
    sd = p.std(ddof=1)
    out["t"] = float(p.mean() / (sd / math.sqrt(n))) if sd > 0 else 0.0
    out["t_dia"] = day_cluster_t(p, day_ids)
    nb, wins = int((p != 0).sum()), int((p > 0).sum())
    out["p_binom"] = float(binom.sf(wins - 1, nb, BE110)) if nb else float("nan")
    path = 100.0 * np.cumprod(1.0 + frac * p)
    out["final"] = float(path[-1])
    out["maxdd"] = float((1 - path / np.maximum.accumulate(np.r_[100.0, path])[1:]).max())
    ii = RNG.integers(0, n, (400, n))
    paths = np.cumprod(1.0 + frac * p[ii], axis=1) * 100.0
    out["ruin"] = float((paths.min(axis=1) < RUIN_LEVEL).mean())
    out["p_end_profit"] = float((paths[:, -1] > 100.0).mean())
    return out


def null_tmat(df, st, perm_sets, keys, n_perm, scheme):
    oos = (df.season.values >= OOS_FROM); ioos = np.where(oos)[0]; m = len(ioos)
    R = real_resid(df)
    tmat = np.full((n_perm, len(keys)), np.nan)
    for b in range(n_perm):
        if scheme == "perm":
            src = RNG.permutation(m)
        else:                                                   # desplazamiento circular
            off = RNG.integers(60, m - 60)
            src = (np.arange(m) + off) % m
        Rb = shuffled_resid(df, R, ioos, src)
        for j, (name, lv) in enumerate(keys):
            p = profits(st[name], perm_sets[(name, lv)], Rb)
            sd = p.std(ddof=1)
            tmat[b, j] = p.mean() / (sd / math.sqrt(len(p))) if sd > 0 else 0.0
    return tmat


def pvals_from_null(res, keys, tmat, st):
    n_ = tmat.shape[0]
    kidx = {k: j for j, k in enumerate(keys)}
    pnull = np.empty_like(tmat)
    for j in range(tmat.shape[1]):
        v = tmat[:, j]; sv = np.sort(v)
        pnull[:, j] = (1 + (n_ - np.searchsorted(sv, v, side="left"))) / (1 + n_)
    fam_cols = [j for (k, j) in kidx.items() if st[k[0]]["family"]]
    minp_null = pnull[:, fam_cols].min(axis=1)
    p_raw, p_fwer = {}, {}
    for i, r in res.iterrows():
        k = (r.strategy, r.level)
        if k in kidx and not np.isnan(r.get("t", np.nan)):
            pr = (1 + (tmat[:, kidx[k]] >= r.t).sum()) / (1 + n_)
            p_raw[i] = pr; p_fwer[i] = (1 + (minp_null <= pr).sum()) / (1 + n_)
    maxt = tmat[:, fam_cols].max(axis=1)
    return p_raw, p_fwer, dict(minp_q05=float(np.quantile(minp_null, .05)), crit_t95=float(np.quantile(maxt, .95)),
                               n_family_cells=len(fam_cols))


def run(df, S, n_perm=2000):
    st = build_strategies(df, S)
    R = real_resid(df)
    seasons, oos = df.season.values, (df.season.values >= OOS_FROM)
    day_codes = pd.factorize(df.day_et.values)[0]
    cells, perm_sets = [], {}
    for name, s in st.items():
        s["pct"] = percentiles(s["strength"], s["side"])
        for lv, (rng_, lname, cut, stake) in LEVELS.items():
            elig = oos & ~np.isnan(s["pct"])
            ib, isk = np.where(elig & (s["pct"] >= cut))[0], np.where(elig & (s["pct"] < cut))[0]
            p = profits(s, ib, R)
            row = dict(strategy=name, level=lv, level_name=lname, range=rng_, stake_pct=stake,
                       group=s["group"], family=s["family"], **cell_metrics(p, stake / 100.0, day_codes[ib]))
            for sy in (2024, 2025):
                q = p[seasons[ib] == sy]
                row[f"roi_{sy}"], row[f"n_{sy}"] = (float(q.mean()) if len(q) else np.nan), len(q)
            if len(isk):
                ps = profits(s, isk, R)
                row.update(skip_n=len(isk), skip_win=float((ps > 0).sum() / max(1, (ps != 0).sum())),
                           skip_roi=float(ps.mean()), skip_net=float(ps.sum()),
                           skip_won=float(ps[ps > 0].sum()), skip_lost=float(-ps[ps < 0].sum()))
            cells.append(row); perm_sets[(name, lv)] = ib
    res = pd.DataFrame(cells)
    keys = [k for k, ib in perm_sets.items() if len(ib) >= 50]
    out = {}
    for scheme in ("perm", "shift"):
        tm = null_tmat(df, st, perm_sets, keys, n_perm, scheme)
        out[scheme] = (tm,) + pvals_from_null(res, keys, tm, st)
    res["p_raw_perm"] = pd.Series(out["perm"][1]); res["p_raw_shift"] = pd.Series(out["shift"][1])
    res["p_fwer_perm"] = pd.Series(out["perm"][2]); res["p_fwer_shift"] = pd.Series(out["shift"][2])
    res["p_raw"] = res[["p_raw_perm", "p_raw_shift"]].max(axis=1)         # el mas conservador
    res["p_fwer"] = res[["p_fwer_perm", "p_fwer_shift"]].max(axis=1)
    fam = res[res.family & res.p_raw.notna()].sort_values("p_raw")
    m, prev, qs = len(fam), 1.0, {}
    for rank, (i, r) in reversed(list(enumerate(fam.iterrows(), 1))):
        prev = min(prev, r.p_raw * m / rank); qs[i] = prev
    res["q_bh"] = np.nan
    for i, q in qs.items():
        res.at[i, "q_bh"] = q
    null_info = dict(n_perm=n_perm, perm=out["perm"][3], shift=out["shift"][3],
                     tmat_shift=out["shift"][0], keys=keys)
    return res, st, null_info


def plant_power(df, target_roi, crit_t, n_sim=150):
    """Potencia: en n_sim plantas independientes, fraccion de veces que la celda de cada nivel supera el t critico
    familiar (max-t al 95% de la nula) y fraccion con p_celda_sola < 0.05 (t > 1.645)."""
    R = real_resid(df); oos = df.season.values >= OOS_FROM
    out = {lv: [] for lv in LEVELS}
    for _ in range(n_sim):
        yh = plant_signal(R["close"], target_roi)
        side = np.sign(yh).astype(int); strength = np.abs(yh)
        pct = percentiles(strength, side)
        s = dict(kind="S", side=side, key="close")
        for lv, (_, _, cut, _) in LEVELS.items():
            ib = np.where(oos & ~np.isnan(pct) & (pct >= cut))[0]
            p = profits(s, ib, R)
            sd = p.std(ddof=1)
            out[lv].append(p.mean() / (sd / math.sqrt(len(p))) if sd > 0 else 0.0)
    return {lv: dict(power_family=float((np.array(v) > crit_t).mean()), power_single=float((np.array(v) > 1.645).mean()),
                     t_mean=float(np.mean(v))) for lv, v in out.items()}
