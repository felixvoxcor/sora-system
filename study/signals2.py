"""Senales v2: walk-forward POR DIA DE CALENDARIO (ET).
Todas las senales de los partidos del dia D se calculan solo con partidos de dias < D
(un partido de las 19:30 ya no 've' el resultado del de las 19:00). El escalado del ridge usa solo
las filas previas a la primera prediccion. abs_diff / pl_gap usan quien jugo realmente EN ESE partido:
quedan en CUARENTENA (solo para el control de fuga LEAK_*), no entran a ninguna estrategia real."""
import numpy as np, pandas as pd
from collections import defaultdict, deque


def day_slices(days):
    """Lista de (inicio, fin) de bloques contiguos con el mismo dia. df debe estar ordenado por fecha."""
    out, s = [], 0
    for i in range(1, len(days) + 1):
        if i == len(days) or days[i] != days[s]:
            out.append((s, i)); s = i
    return out


def _num(x):
    try:
        return float(str(x).replace("+", ""))
    except Exception:
        return np.nan


# ---------------------------------------------------------------- ratings de margen
def rating_margin(df, k=0.05, carry=0.5, hca=2.5, cap=25):
    R, seas, out = defaultdict(float), None, np.zeros(len(df))
    H, A, M, SE = df.home.values, df.away.values, df.margin.values, df.season.values
    for a, b in day_slices(df.day_et.values):
        if SE[a] != seas:
            if seas is not None:
                for t in list(R): R[t] *= carry
            seas = SE[a]
        for i in range(a, b):
            out[i] = R[H[i]] - R[A[i]] + hca
        for i in range(a, b):                                   # actualizar DESPUES de predecir el dia entero
            err = max(-cap, min(cap, M[i])) - out[i]
            R[H[i]] += k * err; R[A[i]] -= k * err
    return out


# ---------------------------------------------------------------- jugadores (CUARENTENA)
def player_signals(df):
    mins = defaultdict(lambda: deque(maxlen=10))
    pm_sum, min_sum = defaultdict(float), defaultdict(float)
    abs_diff, pl_gap = np.zeros(len(df)), np.zeros(len(df))
    rows = list(df.itertuples())
    for a, b in day_slices(df.day_et.values):
        pending = []
        for i in range(a, b):
            r = rows[i]
            loss, strength = {r.home: 0.0, r.away: 0.0}, {r.home: 0.0, r.away: 0.0}
            played = []
            for p in r.players:
                if p["team"] not in loss or not p.get("id"):
                    continue
                st = p.get("stats") or {}
                m = _num(st.get("MIN")) if st else np.nan
                absent = bool(p.get("dnp")) or not (m > 0)
                hist = mins[p["id"]]
                em = float(np.mean(hist)) if len(hist) else 0.0
                if absent:
                    if em >= 10:
                        loss[p["team"]] += (em / 36.0) ** 2
                else:
                    ms = min_sum[p["id"]]
                    v = (pm_sum[p["id"]] / ms * 36.0) * (ms / (ms + 500.0)) if ms > 0 else 0.0
                    strength[p["team"]] += em * v / 48.0
                    played.append((p["id"], m, _num(st.get("+/-"))))
            abs_diff[i] = loss[r.away] - loss[r.home]
            pl_gap[i] = strength[r.home] - strength[r.away]
            pending.extend(played)
        for pid, m, pm in pending:                              # el dia entero se incorpora al terminar
            mins[pid].append(m)
            if not np.isnan(pm):
                pm_sum[pid] += pm; min_sum[pid] += m
    return abs_diff, pl_gap


# ---------------------------------------------------------------- four factors
def four_factors_gap(df, alpha=0.08, w=(0.40, -0.25, 0.20, 0.15)):
    def fac(a, b):
        poss = a["fga"] + 0.44 * a["fta"] + a["to"] - a["oreb"]
        return np.array([(a["fgm"] + 0.5 * a["tpm"]) / a["fga"], a["to"] / poss,
                         a["oreb"] / (a["oreb"] + b["dreb"]), a["ftm"] / a["fga"]])
    off, dfn, cnt = defaultdict(lambda: np.zeros(4)), defaultdict(lambda: np.zeros(4)), defaultdict(int)
    gap, w = np.zeros(len(df)), np.array(w)
    rows = list(df.itertuples())

    def strength(t):
        return float(w @ (off[t] - dfn[t])) if cnt[t] >= 5 else 0.0
    for a, b in day_slices(df.day_et.values):
        upd = []
        for i in range(a, b):
            r = rows[i]
            gap[i] = strength(r.home) - strength(r.away)
            try:
                fh, fa = fac(r.fh, r.fa), fac(r.fa, r.fh)
            except Exception:
                continue
            if np.isnan(fh).any() or np.isnan(fa).any():
                continue
            upd.append((r.home, r.away, fh, fa))
        for h, aw, fh, fa in upd:
            for t, mine, theirs in ((h, fh, fa), (aw, fa, fh)):
                if cnt[t] == 0:
                    off[t], dfn[t] = mine.copy(), theirs.copy()
                else:
                    off[t] += alpha * (mine - off[t]); dfn[t] += alpha * (theirs - dfn[t])
                cnt[t] += 1
    return gap * 100.0


# ---------------------------------------------------------------- modelo de totales
def total_model(df, k=0.05, carry=0.5):
    o, d = defaultdict(float), defaultdict(float)
    mu, seas, out = 112.0, None, np.zeros(len(df))
    H, A, HS, AS, SE = df.home.values, df.away.values, df.home_score.values, df.away_score.values, df.season.values
    for a, b in day_slices(df.day_et.values):
        if SE[a] != seas:
            if seas is not None:
                for t in list(o): o[t] *= carry; d[t] *= carry
            seas = SE[a]
        ph, pa = {}, {}
        for i in range(a, b):
            ph[i] = mu + o[H[i]] + d[A[i]]; pa[i] = mu + o[A[i]] + d[H[i]]
            out[i] = ph[i] + pa[i]
        for i in range(a, b):
            eh, ea = HS[i] - ph[i], AS[i] - pa[i]
            o[H[i]] += k * eh; d[A[i]] += k * eh
            o[A[i]] += k * ea; d[H[i]] += k * ea
            mu += 0.01 * ((HS[i] + AS[i]) / 2 - mu)
    return out


# ---------------------------------------------------------------- arbitros (efecto estimado solo con dias previos)
def referee_effects(df, k=40.0):
    sm, st, n = defaultdict(float), defaultdict(float), defaultdict(int)
    ref_m, ref_t = np.zeros(len(df)), np.zeros(len(df))
    refs, RM, RT = df.refs.values, df.res_m.values, df.res_t.values
    for a, b in day_slices(df.day_et.values):
        for i in range(a, b):
            rs = [x for x in (refs[i] or []) if x]
            if rs:
                ref_m[i] = np.mean([sm[x] / (n[x] + k) for x in rs])
                ref_t[i] = np.mean([st[x] / (n[x] + k) for x in rs])
        for i in range(a, b):
            for x in [x for x in (refs[i] or []) if x]:
                sm[x] += RM[i]; st[x] += RT[i]; n[x] += 1
    return ref_m, ref_t


# ---------------------------------------------------------------- ridge walk-forward por dia
def wf_ridge(X, y, days, lam=300.0, min_n=300):
    """yhat de las filas del dia D usa beta ajustado SOLO con filas de dias < D.
    La escala sale de las primeras min_n filas (todas previas a la primera prediccion)."""
    X = np.asarray(X, float).reshape(len(y), -1); y = np.asarray(y, float)
    s = X[:min_n].std(axis=0); s[s == 0] = 1.0
    Z = X / s
    p = Z.shape[1]
    XtX, Xty = np.zeros((p, p)), np.zeros(p)
    out = np.full(len(y), np.nan)
    for a, b in day_slices(days):
        if a >= min_n:
            beta = np.linalg.solve(XtX + lam * np.eye(p), Xty)
            out[a:b] = Z[a:b] @ beta
        for t in range(a, b):
            XtX += np.outer(Z[t], Z[t]); Xty += Z[t] * y[t]
    return out


def build_all(df):
    S = pd.DataFrame(index=df.index)
    S["m0"] = rating_margin(df)
    S["abs_diff"], S["pl_gap"] = player_signals(df)           # CUARENTENA
    S["ff_gap"] = four_factors_gap(df)
    S["t0"] = total_model(df)
    S["ref_m"], S["ref_t"] = referee_effects(df)
    S["rest_b2b"] = df.b2b_a - df.b2b_h
    S["rest_g4"] = df.g4_a - df.g4_h
    S["rest_days"] = df.rest_h.clip(upper=4) - df.rest_a.clip(upper=4)
    return S
