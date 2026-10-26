# 初步数值实验：DQI 求解 Max-3-XORSAT 时的 BP 伴随式译码
# 约束矩阵 B (m x n)：每个约束含 3 个变量、每个变量出现在 6 个约束中，
# 因而 H = B^T 是 (3,6) 正则 LDPC 校验矩阵（码长 m，码率约 1/2）。
# DQI 需要从伴随式 s = B^T y 恢复重量为 l 的 y；本脚本统计 BP 的精确恢复概率，
# 并按 Jordan 等 (Nature 2025) 的半圆律把“可译码半径”换算成 DQI 期望满足比例。
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams["font.sans-serif"] = ["SimHei"]
rcParams["axes.unicode_minus"] = False
rcParams["font.size"] = 10.5

rng = np.random.default_rng(2026)


def regular_B(n, dv=6, k=3):
    """随机 (k, dv) 正则二部图：m = n*dv/k 个约束，每个约束 k 个变量（避免重边）。"""
    m = n * dv // k
    while True:
        sockets = np.repeat(np.arange(n), dv)
        rng.shuffle(sockets)
        rows = sockets.reshape(m, k)
        if all(len(set(r)) == k for r in rows):
            return rows  # rows[i] = 第 i 个约束涉及的变量


def bp_syndrome(rows, n, s, p, iters=60):
    """对数域和积算法。变量节点 = y 的 m 个分量（约束），校验节点 = B 的 n 列。"""
    m, k = rows.shape
    # 边：约束 i 的第 j 个槽 <-> 校验 rows[i, j]
    edge_chk = rows.ravel()
    L0 = np.log((1 - p) / p)
    v2c = np.full(m * k, L0)
    sign_s = 1 - 2 * s  # 伴随式比特为 1 时翻转符号
    order = np.argsort(edge_chk, kind="stable")
    chk_sorted = edge_chk[order]
    starts = np.r_[0, np.flatnonzero(np.diff(chk_sorted)) + 1]
    for _ in range(iters):
        t = np.tanh(np.clip(v2c, -30, 30) / 2)
        t = np.where(np.abs(t) < 1e-12, 1e-12, t)
        logabs = np.log(np.abs(t))
        neg = (t < 0).astype(int)
        sum_log = np.add.reduceat(logabs[order], starts)
        sum_neg = np.add.reduceat(neg[order], starts)
        tot_log = np.empty(n); tot_log[chk_sorted[starts]] = sum_log
        tot_neg = np.empty(n, dtype=int); tot_neg[chk_sorted[starts]] = sum_neg
        ex_log = tot_log[edge_chk] - logabs
        ex_neg = (tot_neg[edge_chk] - neg) % 2
        mag = np.clip(np.exp(ex_log), 0, 1 - 1e-12)
        c2v = 2 * np.arctanh(mag) * (1 - 2 * ex_neg) * sign_s[edge_chk]
        c2v = c2v.reshape(m, k)
        post = L0 + c2v.sum(axis=1)
        yhat = (post < 0).astype(int)
        syn = np.zeros(n, dtype=int)
        np.add.at(syn, rows.ravel(), np.repeat(yhat, k))
        if np.array_equal(syn % 2, s):
            return yhat
        v2c = (post[:, None] - c2v).ravel()
    return yhat


def success_rate(n, fracs, trials):
    rows = regular_B(n)
    m = rows.shape[0]
    out = []
    for f in fracs:
        l = int(round(f * m))
        ok = 0
        for _ in range(trials):
            y = np.zeros(m, dtype=int)
            y[rng.choice(m, l, replace=False)] = 1
            s = np.zeros(n, dtype=int)
            np.add.at(s, rows.ravel(), np.repeat(y, 3))
            s %= 2
            yhat = bp_syndrome(rows, n, s, max(f, 1e-3))
            ok += np.array_equal(yhat, y)
        out.append(ok / trials)
        print(f"n={n} m={m} l/m={f:.3f} success={out[-1]:.3f}", flush=True)
    return np.array(out)


fracs = np.round(np.arange(0.03, 0.111, 0.005), 3)
res = {}
for n, trials in [(300, 300), (1200, 200), (4800, 100)]:
    res[n] = success_rate(n, fracs, trials)
np.savez("prelim_bp.npz", fracs=fracs, **{f"n{n}": v for n, v in res.items()})

