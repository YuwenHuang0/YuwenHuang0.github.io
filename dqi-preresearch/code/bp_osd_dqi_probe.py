"""Seeded finite-length probe of syndrome BP and BP+OSD for DQI.

This script studies the actual DQI decoding map

    syndrome = H @ error  (over GF(2)),

where the unknown error has a prescribed Hamming weight.  It is an
exploratory experiment, not an asymptotic theorem.
"""

from __future__ import annotations

import argparse
import csv
import itertools
import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np


def gf2_rank(a: np.ndarray) -> int:
    b = a.copy().astype(np.uint8)
    rank = 0
    for col in range(b.shape[1]):
        pivot = next((r for r in range(rank, b.shape[0]) if b[r, col]), None)
        if pivot is None:
            continue
        if pivot != rank:
            b[[rank, pivot]] = b[[pivot, rank]]
        for r in range(rank + 1, b.shape[0]):
            if b[r, col]:
                b[r] ^= b[rank]
        rank += 1
        if rank == b.shape[0]:
            break
    return rank


def gf2_inverse(a: np.ndarray) -> np.ndarray:
    n = a.shape[0]
    aug = np.concatenate([a.copy().astype(np.uint8), np.eye(n, dtype=np.uint8)], axis=1)
    row = 0
    for col in range(n):
        pivot = next((r for r in range(row, n) if aug[r, col]), None)
        if pivot is None:
            raise ValueError("matrix is singular over GF(2)")
        if pivot != row:
            aug[[row, pivot]] = aug[[pivot, row]]
        for r in range(n):
            if r != row and aug[r, col]:
                aug[r] ^= aug[row]
        row += 1
    return aug[:, n:]


def random_column_regular_h(
    n_checks: int, n_bits: int, column_degree: int, rng: np.random.Generator
) -> np.ndarray:
    for _ in range(500):
        h = np.zeros((n_checks, n_bits), dtype=np.uint8)
        for col in range(n_bits):
            h[rng.choice(n_checks, size=column_degree, replace=False), col] = 1
        if gf2_rank(h) == n_checks:
            return h
    raise RuntimeError("could not generate a full-row-rank matrix")


@dataclass
class TannerGraph:
    h: np.ndarray
    edge_checks: np.ndarray
    edge_bits: np.ndarray
    check_edges: list[np.ndarray]
    bit_edges: list[np.ndarray]


def make_graph(h: np.ndarray) -> TannerGraph:
    checks, bits = np.nonzero(h)
    edge_checks = checks.astype(np.int32)
    edge_bits = bits.astype(np.int32)
    check_edges = [np.flatnonzero(edge_checks == a) for a in range(h.shape[0])]
    bit_edges = [np.flatnonzero(edge_bits == i) for i in range(h.shape[1])]
    return TannerGraph(h, edge_checks, edge_bits, check_edges, bit_edges)


def syndrome_bp(
    graph: TannerGraph,
    syndrome: np.ndarray,
    prior_p: float,
    iterations: int,
    damping: float = 0.25,
) -> tuple[np.ndarray, np.ndarray]:
    """Sum-product decoding for a BSC prior, given syndrome only."""
    prior_p = min(max(prior_p, 1e-8), 1 - 1e-8)
    prior_llr = math.log((1 - prior_p) / prior_p)
    q = np.full(len(graph.edge_bits), prior_llr, dtype=float)
    r = np.zeros_like(q)

    for _ in range(iterations):
        new_r = np.zeros_like(r)
        for a, edges in enumerate(graph.check_edges):
            vals = np.tanh(np.clip(q[edges], -50.0, 50.0) / 2.0)
            sign = -1.0 if syndrome[a] else 1.0
            for local, edge in enumerate(edges):
                if len(edges) == 1:
                    product = sign
                else:
                    product = sign * float(np.prod(np.delete(vals, local)))
                product = float(np.clip(product, -1 + 1e-12, 1 - 1e-12))
                new_r[edge] = 2.0 * np.arctanh(product)
        r = damping * r + (1.0 - damping) * new_r

        new_q = np.zeros_like(q)
        for i, edges in enumerate(graph.bit_edges):
            total = prior_llr + float(np.sum(r[edges]))
            new_q[edges] = total - r[edges]
        q = damping * q + (1.0 - damping) * new_q

    posterior = np.full(graph.h.shape[1], prior_llr, dtype=float)
    for i, edges in enumerate(graph.bit_edges):
        posterior[i] += float(np.sum(r[edges]))
    hard = (posterior < 0).astype(np.uint8)
    return hard, posterior


def independent_pivots(h: np.ndarray, order: np.ndarray) -> tuple[list[int], list[int]]:
    selected: list[int] = []
    current = np.zeros((h.shape[0], 0), dtype=np.uint8)
    rank = 0
    for col in order:
        trial = np.column_stack([current, h[:, col]])
        trial_rank = gf2_rank(trial)
        if trial_rank > rank:
            selected.append(int(col))
            current = trial
            rank = trial_rank
            if rank == h.shape[0]:
                break
    if rank != h.shape[0]:
        raise ValueError("full pivot set not found")
    selected_set = set(selected)
    nonpivots = [int(c) for c in order if int(c) not in selected_set]
    return selected, nonpivots


def bp_osd(
    h: np.ndarray,
    syndrome: np.ndarray,
    hard: np.ndarray,
    posterior_llr: np.ndarray,
    osd_order: int,
    window: int | None = None,
) -> tuple[np.ndarray, int]:
    """Reliability-ordered syndrome OSD with an exact BSC-prior score."""
    reliabilities = np.abs(posterior_llr)
    reliability_order = np.argsort(reliabilities)  # least reliable first
    pivots, nonpivots = independent_pivots(h, reliability_order)
    if window is not None:
        nonpivots = nonpivots[:window]

    hp = h[:, pivots]
    hp_inv = gf2_inverse(hp)
    residual = syndrome ^ ((h @ hard) & 1)

    best: np.ndarray | None = None
    best_key: tuple[float, float, bytes] | None = None
    tested = 0
    max_order = min(osd_order, len(nonpivots))
    for weight in range(max_order + 1):
        for subset in itertools.combinations(nonpivots, weight):
            z = np.zeros(h.shape[1], dtype=np.uint8)
            if subset:
                z[list(subset)] = 1
            rhs = residual ^ ((h @ z) & 1)
            z[pivots] = (hp_inv @ rhs) & 1
            candidate = hard ^ z
            tested += 1
            # Under the uniform BSC prior, MAP means minimum Hamming weight.
            # BP reliabilities only break equal-weight ties in the finite list.
            key = (
                float(np.sum(candidate)),
                float(np.sum(reliabilities[candidate != hard])),
                candidate.tobytes(),
            )
            if best_key is None or key < best_key:
                best_key = key
                best = candidate.copy()
    assert best is not None
    assert np.array_equal((h @ best) & 1, syndrome)
    return best, tested


def run_probe(
    seed: int,
    matrices: int,
    trials: int,
    n_bits: int,
    n_checks: int,
    column_degrees: list[int],
    error_rates: list[float],
    iterations: int,
    orders: list[int],
) -> list[dict[str, float | int]]:
    rng = np.random.default_rng(seed)
    rows: list[dict[str, float | int]] = []
    for degree in column_degrees:
        for p in error_rates:
            ell = max(1, round(p * n_bits))
            counts = {"bp": 0, **{f"osd{o}": 0 for o in orders}}
            candidate_totals = {o: 0 for o in orders}
            total = matrices * trials
            for _ in range(matrices):
                h = random_column_regular_h(n_checks, n_bits, degree, rng)
                graph = make_graph(h)
                for _ in range(trials):
                    support = rng.choice(n_bits, size=ell, replace=False)
                    error = np.zeros(n_bits, dtype=np.uint8)
                    error[support] = 1
                    syndrome = (h @ error) & 1
                    hard, llr = syndrome_bp(graph, syndrome, ell / n_bits, iterations)
                    counts["bp"] += int(np.array_equal(hard, error))
                    for order in orders:
                        estimate, tested = bp_osd(h, syndrome, hard, llr, order)
                        candidate_totals[order] += tested
                        counts[f"osd{order}"] += int(np.array_equal(estimate, error))
            base = {
                "n_bits": n_bits,
                "n_checks": n_checks,
                "column_degree": degree,
                "mean_row_degree": degree * n_bits / n_checks,
                "error_weight": ell,
                "error_rate": ell / n_bits,
                "trials": total,
                "bp_success": counts["bp"] / total,
            }
            for order in orders:
                base[f"osd{order}_success"] = counts[f"osd{order}"] / total
                base[f"osd{order}_mean_candidates"] = candidate_totals[order] / total
            rows.append(base)
            print(base, flush=True)
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=260901)
    parser.add_argument("--matrices", type=int, default=4)
    parser.add_argument("--trials", type=int, default=100)
    parser.add_argument("--bits", type=int, default=96)
    parser.add_argument("--checks", type=int, default=60)
    parser.add_argument("--iterations", type=int, default=30)
    parser.add_argument("--output", type=Path, default=Path("audit/bp_osd_dqi_probe.csv"))
    args = parser.parse_args()

    rows = run_probe(
        seed=args.seed,
        matrices=args.matrices,
        trials=args.trials,
        n_bits=args.bits,
        n_checks=args.checks,
        column_degrees=[3, 5, 9],
        error_rates=[0.04, 0.06, 0.08, 0.10, 0.12],
        iterations=args.iterations,
        orders=[0, 1, 2],
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
