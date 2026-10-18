"""Senales walk-forward: cada valor del partido t usa SOLO informacion de partidos anteriores a t
(las ausencias/rotacion del propio partido son conocidas antes del tip salvo casos raros; ver README)."""
import numpy as np, pandas as pd
from collections import defaultdict, deque


def _num(x):
    try:
        return float(str(x).replace("+", ""))
    except Exception:
        return np.nan


# ---------------------------------------------------------------- ratings de margen
def rating_margin(df, k=0.05, carry=0.5, hca=2.5, cap=25):
    R, seas, out = defaultdict(float), None, np.zeros(len(df))
    for i, r in enumerate(df.itertuples()):
        if r.season != seas:
            if seas is not None:
                for t in list(R): R[t] *= carry
            seas = r.season
        pred = R[r.home] - R[r.away] + hca
        out[i] = pred
        err = max(-cap, min(cap, r.margin)) - pred
        R[r.home] += k * err; R[r.away] -= k * err
    return out


# ---------------------------------------------------------------- jugadores / ausencias
def player_signals(df):
    """abs_diff: perdida por ausencias (visitante - local, + favorece local).
    pl_gap: fuerza de plantilla disponible (local - visitante) con +/- por 36 min encogido."""
    mins = defaultdict(lambda: deque(maxlen=10))
    pm_sum, min_sum = defaultdict(float), defaultdict(float)
    abs_diff, pl_gap = np.zeros(len(df)), np.zeros(len(df))
    for i, r in enumerate(df.itertuples()):
        loss, strength = {r.home: 0.0, r.away: 0.0}, {r.home: 0.0, r.away: 0.0}
        played = []
        for p in r.players:
            if p["team"] not in loss or not p.get("id"):
                continue
            st = p.get("stats") or {}
            m = _num(st.get("MIN")) if st else np.nan
            absent = bool(p.get("dnp")) or not (m > 0)
            hist = mins[p["id"]]
            em = float(np.mean(hist)) if len(hist) else 0.0       # minutos esperados (solo pasado)
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
        for pid, m, pm in played:                                  # actualizar DESPUES de usar
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

    def strength(t):
        return float(w @ (off[t] - dfn[t])) if cnt[t] >= 5 else 0.0
    for i, r in enumerate(df.itertuples()):
        gap[i] = strength(r.home) - strength(r.away)
        try:
            fh, fa = fac(r.fh, r.fa), fac(r.fa, r.fh)
        except Exception:
            continue
        if np.isnan(fh).any() or np.isnan(fa).any():
            continue
        for t, mine, theirs in ((r.home, fh, fa), (r.away, fa, fh)):
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
    for i, r in enumerate(df.itertuples()):
        if r.season != seas:
            if seas is not None:
                for t in list(o): o[t] *= carry; d[t] *= carry
            seas = r.season
        ph = mu + o[r.home] + d[r.away]; pa = mu + o[r.away] + d[r.home]
        out[i] = ph + pa
        eh, ea = r.home_score - ph, r.away_score - pa
        o[r.home] += k * eh; d[r.away] += k * eh
        o[r.away] += k * ea; d[r.home] += k * ea
        mu += 0.01 * ((r.home_score + r.away_score) / 2 - mu)
    return out


# ---------------------------------------------------------------- arbitros
def referee_effects(df, k=40.0):
    sm, st, n = defaultdict(float), defaultdict(float), defaultdict(int)
    ref_m, ref_t = np.zeros(len(df)), np.zeros(len(df))
    for i, r in enumerate(df.itertuples()):
        refs = [x for x in (r.refs or []) if x]
        if refs:
            ref_m[i] = np.mean([sm[x] / (n[x] + k) for x in refs])
            ref_t[i] = np.mean([st[x] / (n[x] + k) for x in refs])
        for x in refs:
            sm[x] += r.res_m; st[x] += r.res_t; n[x] += 1
    return ref_m, ref_t


# ---------------------------------------------------------------- ridge walk-forward
def wf_ridge(X, y, lam=300.0, min_n=300, scale_rows=500):
    """yhat[t] = x_t . beta_t, con beta_t ajustado solo con filas < t. Escala fija de las primeras filas."""
    X = np.asarray(X, float).reshape(len(y), -1); y = np.asarray(y, float)
    s = X[:scale_rows].std(axis=0); s[s == 0] = 1.0
    Z = X / s
    p = Z.shape[1]
    XtX, Xty = np.zeros((p, p)), np.zeros(p)
    out = np.full(len(y), np.nan)
    for t in range(len(y)):
        if t >= min_n:
            beta = np.linalg.solve(XtX + lam * np.eye(p), Xty)
            out[t] = Z[t] @ beta
        XtX += np.outer(Z[t], Z[t]); Xty += Z[t] * y[t]
    return out


def build_all(df):
    S = pd.DataFrame(index=df.index)
    S["m0"] = rating_margin(df)
    S["abs_diff"], S["pl_gap"] = player_signals(df)
    S["ff_gap"] = four_factors_gap(df)
    S["t0"] = total_model(df)
    S["ref_m"], S["ref_t"] = referee_effects(df)
    S["rest_b2b"] = df.b2b_a - df.b2b_h
    S["rest_g4"] = df.g4_a - df.g4_h
    S["rest_days"] = df.rest_h.clip(upper=4) - df.rest_a.clip(upper=4)
    return S
