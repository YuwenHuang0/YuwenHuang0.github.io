"""Scalable classical decoder co-design for the accepted-pair DQI objective.

This is an independent research sandbox.  It does not edit the grant files.

For a full-row-rank binary parity-check matrix H, a deterministic syndrome
decoder chooses one representative e_s from every coset H e = s.  Under a
Bernoulli(p) error model, define

    Z(D) = sum_s P(e_s),

and let E(D) be the undirected probability-amplitude mass of accepted pairs
that differ in one physical bit.  The phase-averaged conditional DQI score and
the retry-adjusted excess bias per circuit attempt are

    S(D) = 1/2 + E(D)/(n Z(D)),
    R(D) = Z(D) (S(D)-1/2) = E(D)/n.

The script tests two entirely classical, real-valued routes.

1. Candidate/transversal co-design.  Exact k-best coset candidates, real BP,
   and OSD-1/2 candidates are generated for every syndrome.  Coordinate
   ascent maximizes E subject to Z >= eta Z_ML.  Small instances are checked
   against exhaustive optimization over the same candidate sets.

2. A compact implementable family.  The code and ML decoder are unchanged,
   while BP varies an invertible row representation H'=U H, a few redundant
   checks, input-LLR scale, damping, and an edge-update-matched iteration
   budget.  Selecting this low-dimensional family by E is compared with
   selecting it by frame success Z.

An optional zero-temperature Bethe/max-sum calculation is run on the same
candidate-label graph.  It is used only as an offline ranking heuristic.  No
complex-message gain, quantum measurement, or capacity claim is involved.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
import time
from dataclasses import asdict, dataclass
from itertools import product
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np


RESULT_DIR = Path(__file__).with_name("dqi_codesign_results")


def parity(value: int) -> int:
    return value.bit_count() & 1


def syndrome(error: int, columns: Sequence[int]) -> int:
    out = 0
    while error:
        low = error & -error
        out ^= columns[low.bit_length() - 1]
        error ^= low
    return out


def gf2_rank(vectors: Iterable[int]) -> int:
    basis: dict[int, int] = {}
    for value in vectors:
        x = value
        while x:
            pivot = x.bit_length() - 1
            if pivot in basis:
                x ^= basis[pivot]
            else:
                basis[pivot] = x
                break
    return len(basis)


def parity_check_columns_from_generator(n: int, generator_rows: Sequence[int]) -> tuple[int, ...]:
    orthogonal = [
        row
        for row in range(1, 1 << n)
        if all(parity(row & generator) == 0 for generator in generator_rows)
    ]
    chosen: list[int] = []
    rank = 0
    for row in orthogonal:
        new_rank = gf2_rank(chosen + [row])
        if new_rank > rank:
            chosen.append(row)
            rank = new_rank
    expected = n - gf2_rank(generator_rows)
    if rank != expected:
        raise RuntimeError("failed to construct a parity check")
    return tuple(
        sum((((row >> bit) & 1) << check) for check, row in enumerate(chosen))
        for bit in range(n)
    )


def random_sparse_columns(n: int, r: int, seed: int, column_weight: int = 3) -> tuple[int, ...]:
    rng = random.Random(seed)
    weight = min(column_weight, r)
    for _ in range(10_000):
        columns = tuple(
            sum(1 << check for check in rng.sample(range(r), weight)) for _ in range(n)
        )
        if gf2_rank(columns) == r and all(columns):
            return columns
    raise RuntimeError(f"could not generate a full-rank sparse H for n={n}, r={r}")


def binary_entropy(p: float) -> float:
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * math.log2(p) - (1.0 - p) * math.log2(1.0 - p)


def inverse_binary_entropy(target: float) -> float:
    lo, hi = 1e-8, 0.49999999
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if binary_entropy(mid) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def topk_coset_candidates(columns: Sequence[int], r: int, k: int) -> tuple[tuple[int, ...], ...]:
    """Exact k lightest representatives per syndrome by dynamic programming."""
    states = 1 << r
    table: list[list[tuple[int, int]]] = [[] for _ in range(states)]
    table[0] = [(0, 0)]
    for bit, column in enumerate(columns):
        bit_mask = 1 << bit
        updated: list[list[tuple[int, int]]] = [[] for _ in range(states)]
        for s in range(states):
            merged = list(table[s])
            merged.extend((weight + 1, mask | bit_mask) for weight, mask in table[s ^ column])
            merged.sort()
            seen: set[int] = set()
            for item in merged:
                if item[1] not in seen:
                    updated[s].append(item)
                    seen.add(item[1])
                    if len(updated[s]) == k:
                        break
        table = updated
    if any(not entries for entries in table):
        raise RuntimeError("H was not full row rank")
    return tuple(tuple(mask for _, mask in entries) for entries in table)


def exhaustive_topk_check(columns: Sequence[int], candidates: Sequence[Sequence[int]]) -> None:
    n = len(columns)
    if n > 16:
        return
    brute: list[list[int]] = [[] for _ in candidates]
    for error in range(1 << n):
        brute[syndrome(error, columns)].append(error)
    for group in brute:
        group.sort(key=lambda error: (error.bit_count(), error))
    for s, entries in enumerate(candidates):
        expected = tuple(brute[s][: len(entries)])
        if tuple(entries) != expected:
            raise AssertionError((s, tuple(entries), expected))


def probability_by_weight(n: int, p: float) -> tuple[float, ...]:
    return tuple((p**weight) * ((1.0 - p) ** (n - weight)) for weight in range(n + 1))


@dataclass(frozen=True)
class Metrics:
    acceptance: float
    conditional_score: float
    retry_adjusted_excess: float
    expected_retries: float
    pair_mass: float


def mapping_metrics(
    choice: Sequence[int],
    candidates: Sequence[Sequence[int]],
    probabilities: Sequence[Sequence[float]],
    columns: Sequence[int],
) -> Metrics:
    n = len(columns)
    z = sum(probabilities[s][choice[s]] for s in range(len(choice)))
    directed = 0.0
    for s in range(len(choice)):
        error = candidates[s][choice[s]]
        prob = probabilities[s][choice[s]]
        for bit, column in enumerate(columns):
            other_s = s ^ column
            other = candidates[other_s][choice[other_s]]
            if other == (error ^ (1 << bit)):
                directed += math.sqrt(prob * probabilities[other_s][choice[other_s]])
    pair_mass = 0.5 * directed
    score = 0.5 + pair_mass / (n * z)
    return Metrics(
        acceptance=z,
        conditional_score=score,
        retry_adjusted_excess=pair_mass / n,
        expected_retries=1.0 / z,
        pair_mass=pair_mass,
    )


def local_pair_mass(
    s: int,
    label: int,
    choice: Sequence[int],
    candidates: Sequence[Sequence[int]],
    probabilities: Sequence[Sequence[float]],
    columns: Sequence[int],
) -> float:
    error = candidates[s][label]
    prob = probabilities[s][label]
    value = 0.0
    for bit, column in enumerate(columns):
        other_s = s ^ column
        other_label = choice[other_s]
        if candidates[other_s][other_label] == (error ^ (1 << bit)):
            value += math.sqrt(prob * probabilities[other_s][other_label])
    return value


def coordinate_ascent(
    start: Sequence[int],
    candidates: Sequence[Sequence[int]],
    probabilities: Sequence[Sequence[float]],
    columns: Sequence[int],
    min_acceptance: float,
    seed: int,
    max_sweeps: int = 100,
) -> tuple[tuple[int, ...], Metrics, int]:
    """Monotone ascent of exact pair mass with a hard acceptance constraint."""
    rng = random.Random(seed)
    choice = list(start)
    current = mapping_metrics(choice, candidates, probabilities, columns)
    if current.acceptance + 1e-15 < min_acceptance:
        raise ValueError("infeasible coordinate-ascent start")
    z = current.acceptance
    pair_mass = current.pair_mass
    sweeps = 0
    for sweep in range(max_sweeps):
        sweeps = sweep + 1
        changed = False
        order = list(range(len(choice)))
        rng.shuffle(order)
        for s in order:
            old = choice[s]
            old_local = local_pair_mass(s, old, choice, candidates, probabilities, columns)
            old_prob = probabilities[s][old]
            best = old
            best_pair = pair_mass
            best_z = z
            for label in range(len(candidates[s])):
                if label == old:
                    continue
                trial_z = z - old_prob + probabilities[s][label]
                if trial_z + 1e-14 < min_acceptance:
                    continue
                trial_local = local_pair_mass(
                    s, label, choice, candidates, probabilities, columns
                )
                trial_pair = pair_mass - old_local + trial_local
                if trial_pair > best_pair + 1e-15 or (
                    abs(trial_pair - best_pair) <= 1e-15 and trial_z > best_z + 1e-15
                ):
                    best = label
                    best_pair = trial_pair
                    best_z = trial_z
            if best != old:
                choice[s] = best
                pair_mass = best_pair
                z = best_z
                changed = True
        if not changed:
            break
    result = mapping_metrics(choice, candidates, probabilities, columns)
    if abs(result.acceptance - z) > 2e-11 or abs(result.pair_mass - pair_mass) > 2e-11:
        raise AssertionError((result, z, pair_mass))
    return tuple(choice), result, sweeps


def random_feasible_start(
    ml_choice: Sequence[int],
    probabilities: Sequence[Sequence[float]],
    min_acceptance: float,
    seed: int,
    mutation_rate: float = 0.12,
) -> tuple[int, ...]:
    rng = random.Random(seed)
    choice = list(ml_choice)
    z = sum(probabilities[s][choice[s]] for s in range(len(choice)))
    order = list(range(len(choice)))
    rng.shuffle(order)
    for s in order:
        if len(probabilities[s]) <= 1 or rng.random() > mutation_rate:
            continue
        label = rng.randrange(1, len(probabilities[s]))
        trial_z = z - probabilities[s][choice[s]] + probabilities[s][label]
        if trial_z + 1e-14 >= min_acceptance:
            z = trial_z
            choice[s] = label
    return tuple(choice)


def multistart_coordinate_ascent(
    ml_choice: Sequence[int],
    candidates: Sequence[Sequence[int]],
    probabilities: Sequence[Sequence[float]],
    columns: Sequence[int],
    min_acceptance: float,
    seed: int,
    restarts: int,
) -> tuple[tuple[int, ...], Metrics, int]:
    best_choice: tuple[int, ...] | None = None
    best_metrics: Metrics | None = None
    total_sweeps = 0
    starts = [tuple(ml_choice)]
    starts.extend(
        random_feasible_start(ml_choice, probabilities, min_acceptance, seed + 7919 * j)
        for j in range(1, restarts)
    )
    for j, start in enumerate(starts):
        choice, metrics, sweeps = coordinate_ascent(
            start,
            candidates,
            probabilities,
            columns,
            min_acceptance,
            seed + 104729 * j,
        )
        total_sweeps += sweeps
        if best_metrics is None or metrics.pair_mass > best_metrics.pair_mass + 1e-15 or (
            abs(metrics.pair_mass - best_metrics.pair_mass) <= 1e-15
            and metrics.acceptance > best_metrics.acceptance
        ):
            best_choice, best_metrics = choice, metrics
    assert best_choice is not None and best_metrics is not None
    return best_choice, best_metrics, total_sweeps


def exhaustive_candidate_optimum(
    candidates: Sequence[Sequence[int]],
    probabilities: Sequence[Sequence[float]],
    columns: Sequence[int],
    min_acceptance: float,
    max_maps: int = 2_000_000,
) -> tuple[tuple[int, ...], Metrics] | None:
    count = math.prod(len(group) for group in candidates)
    if count > max_maps:
        return None
    best_choice: tuple[int, ...] | None = None
    best_metrics: Metrics | None = None
    for choice in product(*(range(len(group)) for group in candidates)):
        metrics = mapping_metrics(choice, candidates, probabilities, columns)
        if metrics.acceptance + 1e-14 < min_acceptance:
            continue
        if best_metrics is None or metrics.pair_mass > best_metrics.pair_mass + 1e-15 or (
            abs(metrics.pair_mass - best_metrics.pair_mass) <= 1e-15
            and metrics.acceptance > best_metrics.acceptance
        ):
            best_choice, best_metrics = tuple(choice), metrics
    if best_choice is None or best_metrics is None:
        return None
    return best_choice, best_metrics


def representation_graph(
    columns: Sequence[int], check_forms: Sequence[int]
) -> tuple[list[list[int]], list[list[int]], list[tuple[int, int]]]:
    check_edges: list[list[int]] = [[] for _ in check_forms]
    variable_edges: list[list[int]] = [[] for _ in columns]
    edge_pairs: list[tuple[int, int]] = []
    for check, form in enumerate(check_forms):
        for bit, column in enumerate(columns):
            if parity(form & column):
                edge = len(edge_pairs)
                edge_pairs.append((check, bit))
                check_edges[check].append(edge)
                variable_edges[bit].append(edge)
    if any(len(edges) < 2 for edges in check_edges):
        raise ValueError("degree-one or empty check in representation")
    return check_edges, variable_edges, edge_pairs


def all_syndrome_bp_llrs(
    columns: Sequence[int],
    r: int,
    p: float,
    check_forms: Sequence[int] | None = None,
    iterations: int = 15,
    input_scale: float = 1.0,
    damping: float = 0.7,
) -> tuple[np.ndarray, int]:
    """Flooding real sum-product for every original syndrome in parallel."""
    if check_forms is None:
        check_forms = tuple(1 << check for check in range(r))
    checks, variables, edge_pairs = representation_graph(columns, check_forms)
    states = 1 << r
    edge_count = len(edge_pairs)
    channel = input_scale * math.log((1.0 - p) / p)
    v2c = np.full((states, edge_count), channel, dtype=np.float64)
    c2v = np.zeros((states, edge_count), dtype=np.float64)
    syndrome_values = np.arange(states, dtype=np.uint32)
    check_signs = []
    for form in check_forms:
        bits = np.fromiter((parity(int(s) & form) for s in syndrome_values), dtype=np.int8)
        check_signs.append(1.0 - 2.0 * bits)
    edge_var = np.asarray([pair[1] for pair in edge_pairs], dtype=np.int32)

    for _ in range(iterations):
        raw_c2v = np.zeros_like(c2v)
        for check, edge_ids in enumerate(checks):
            ids = np.asarray(edge_ids, dtype=np.int32)
            tanh_values = np.tanh(0.5 * v2c[:, ids])
            near_zero = np.abs(tanh_values) < 1e-15
            zero_count = np.sum(near_zero, axis=1)
            product_nonzero = np.prod(np.where(near_zero, 1.0, tanh_values), axis=1)
            for local, edge in enumerate(edge_ids):
                current_zero = near_zero[:, local]
                product_other = np.zeros(states)
                no_zero = zero_count == 0
                product_other[no_zero] = product_nonzero[no_zero] / tanh_values[no_zero, local]
                sole_zero = (zero_count == 1) & current_zero
                product_other[sole_zero] = product_nonzero[sole_zero]
                value = check_signs[check] * product_other
                value = np.clip(value, -1.0 + 1e-14, 1.0 - 1e-14)
                raw_c2v[:, edge] = 2.0 * np.arctanh(value)
        c2v = (1.0 - damping) * c2v + damping * raw_c2v

        totals = np.full((states, len(columns)), channel, dtype=np.float64)
        for bit, edge_ids in enumerate(variables):
            totals[:, bit] += np.sum(c2v[:, edge_ids], axis=1)
        raw_v2c = totals[:, edge_var] - c2v
        v2c = (1.0 - damping) * v2c + damping * raw_v2c

    posterior = np.full((states, len(columns)), channel, dtype=np.float64)
    for bit, edge_ids in enumerate(variables):
        posterior[:, bit] += np.sum(c2v[:, edge_ids], axis=1)
    return posterior, edge_count


def build_basis_solver(columns: Sequence[int], order: Sequence[int], r: int):
    basis_vec = [0] * r
    basis_error = [0] * r
    selected: set[int] = set()
    for bit in order:
        value = columns[bit]
        representation = 1 << bit
        for pivot in range(r - 1, -1, -1):
            if not ((value >> pivot) & 1):
                continue
            if basis_vec[pivot]:
                value ^= basis_vec[pivot]
                representation ^= basis_error[pivot]
            else:
                basis_vec[pivot] = value
                basis_error[pivot] = representation
                selected.add(bit)
                break
        if len(selected) == r:
            break
    if len(selected) != r:
        raise RuntimeError("could not form an OSD basis")

    def solve(target: int) -> int:
        value = target
        error = 0
        for pivot in range(r - 1, -1, -1):
            if (value >> pivot) & 1:
                value ^= basis_vec[pivot]
                error ^= basis_error[pivot]
        if value:
            raise RuntimeError("basis solve failed")
        return error

    return solve, selected


def llr_metric(error: int, llr: np.ndarray) -> float:
    value = 0.0
    while error:
        low = error & -error
        value += float(llr[low.bit_length() - 1])
        error ^= low
    return value


def osd_candidates(
    columns: Sequence[int],
    r: int,
    target: int,
    llr: np.ndarray,
    order: int = 1,
    test_bits: int = 7,
) -> tuple[int, ...]:
    hard = 0
    for bit, value in enumerate(llr):
        if value < 0.0:
            hard |= 1 << bit
    residual = target ^ syndrome(hard, columns)
    reliability_order = sorted(range(len(columns)), key=lambda bit: (abs(float(llr[bit])), bit))
    solve, basis_bits = build_basis_solver(columns, reliability_order, r)
    nonbasis = [bit for bit in reliability_order if bit not in basis_bits][:test_bits]
    trial_flips = [0]
    trial_flips.extend(1 << bit for bit in nonbasis)
    if order >= 2:
        for a in range(len(nonbasis)):
            for b in range(a + 1, len(nonbasis)):
                trial_flips.append((1 << nonbasis[a]) | (1 << nonbasis[b]))
    candidates: set[int] = set()
    for flips in trial_flips:
        target_repair = residual ^ syndrome(flips, columns)
        candidate = hard ^ flips ^ solve(target_repair)
        if syndrome(candidate, columns) != target:
            raise AssertionError("OSD emitted an invalid coset representative")
        candidates.add(candidate)
    return tuple(sorted(candidates, key=lambda error: (llr_metric(error, llr), error)))


@dataclass(frozen=True)
class BPConfig:
    label: str
    input_scale: float
    damping: float
    base_iterations: int


def bp_osd_maps_and_pool(
    columns: Sequence[int],
    r: int,
    p: float,
    base_candidates: Sequence[Sequence[int]],
    configs: Sequence[BPConfig],
    check_forms: Sequence[int] | None = None,
    update_budget: int | None = None,
    osd_order: int = 1,
) -> tuple[dict[str, tuple[int, ...]], tuple[tuple[int, ...], ...], dict[str, int]]:
    states = 1 << r
    pool = [list(group) for group in base_candidates]
    maps: dict[str, tuple[int, ...]] = {}
    costs: dict[str, int] = {}
    for config in configs:
        probe_forms = check_forms or tuple(1 << check for check in range(r))
        _, _, edge_pairs = representation_graph(columns, probe_forms)
        iterations = config.base_iterations
        if update_budget is not None:
            iterations = max(1, update_budget // len(edge_pairs))
        llrs, edge_count = all_syndrome_bp_llrs(
            columns,
            r,
            p,
            check_forms=check_forms,
            iterations=iterations,
            input_scale=config.input_scale,
            damping=config.damping,
        )
        mapping: list[int] = []
        for s in range(states):
            osd = osd_candidates(columns, r, s, llrs[s], order=osd_order)
            selected = osd[0]
            mapping.append(selected)
            for candidate in osd[:4]:
                if candidate not in pool[s]:
                    pool[s].append(candidate)
        label = f"{config.label}[it={iterations},edges={edge_count}]"
        maps[label] = tuple(mapping)
        costs[label] = iterations * edge_count
    return maps, tuple(tuple(group) for group in pool), costs


def choice_for_mapping(mapping: Sequence[int], candidates: Sequence[Sequence[int]]) -> tuple[int, ...]:
    return tuple(candidates[s].index(error) for s, error in enumerate(mapping))


def max_sum_bethe(
    candidates: Sequence[Sequence[int]],
    probabilities: Sequence[Sequence[float]],
    columns: Sequence[int],
    unary_weight: float,
    iterations: int = 30,
    damping: float = 0.6,
) -> tuple[tuple[int, ...], list[np.ndarray]]:
    """Zero-temperature Bethe/max-sum on the syndrome candidate graph."""
    edges: list[tuple[int, int, int]] = []
    for s in range(len(candidates)):
        for bit, column in enumerate(columns):
            other = s ^ column
            if s < other:
                edges.append((s, other, bit))
    adjacency: list[list[tuple[int, bool]]] = [[] for _ in candidates]
    uv: list[np.ndarray] = []  # message u -> v, indexed by labels at v
    vu: list[np.ndarray] = []  # message v -> u, indexed by labels at u
    candidate_index = [{value: label for label, value in enumerate(group)} for group in candidates]
    for edge, (u, v, _) in enumerate(edges):
        adjacency[u].append((edge, True))
        adjacency[v].append((edge, False))
        uv.append(np.zeros(len(candidates[v])))
        vu.append(np.zeros(len(candidates[u])))

    beliefs: list[np.ndarray] = []
    for _ in range(iterations):
        totals = [unary_weight * np.asarray(probabilities[s], dtype=float) for s in range(len(candidates))]
        for edge, (u, v, _) in enumerate(edges):
            totals[u] = totals[u] + vu[edge]
            totals[v] = totals[v] + uv[edge]
        new_uv: list[np.ndarray] = []
        new_vu: list[np.ndarray] = []
        for edge, (u, v, bit) in enumerate(edges):
            base_u = totals[u] - vu[edge]
            base_v = totals[v] - uv[edge]
            out_uv = np.full(len(candidates[v]), float(np.max(base_u)))
            out_vu = np.full(len(candidates[u]), float(np.max(base_v)))
            flip = 1 << bit
            for lu, error_u in enumerate(candidates[u]):
                lv = candidate_index[v].get(error_u ^ flip)
                if lv is None:
                    continue
                reward = math.sqrt(probabilities[u][lu] * probabilities[v][lv])
                out_uv[lv] = max(out_uv[lv], base_u[lu] + reward)
                out_vu[lu] = max(out_vu[lu], base_v[lv] + reward)
            out_uv -= np.max(out_uv)
            out_vu -= np.max(out_vu)
            new_uv.append((1.0 - damping) * uv[edge] + damping * out_uv)
            new_vu.append((1.0 - damping) * vu[edge] + damping * out_vu)
        uv, vu = new_uv, new_vu

    beliefs = [unary_weight * np.asarray(probabilities[s], dtype=float) for s in range(len(candidates))]
    for edge, (u, v, _) in enumerate(edges):
        beliefs[u] = beliefs[u] + vu[edge]
        beliefs[v] = beliefs[v] + uv[edge]
    choice = tuple(int(np.argmax(belief)) for belief in beliefs)
    return choice, beliefs


def rankdata(values: np.ndarray) -> np.ndarray:
    order = np.argsort(values, kind="mergesort")
    ranks = np.empty(len(values), dtype=float)
    start = 0
    while start < len(values):
        stop = start + 1
        while stop < len(values) and values[order[stop]] == values[order[start]]:
            stop += 1
        rank = 0.5 * (start + stop - 1)
        ranks[order[start:stop]] = rank
        start = stop
    return ranks


def bethe_local_rank_correlation(
    beliefs: Sequence[np.ndarray],
    reference: Sequence[int],
    candidates: Sequence[Sequence[int]],
    probabilities: Sequence[Sequence[float]],
    columns: Sequence[int],
    unary_weight: float,
) -> float:
    predicted: list[float] = []
    exact_local: list[float] = []
    for s in range(len(candidates)):
        centered = beliefs[s] - np.mean(beliefs[s])
        for label in range(len(candidates[s])):
            predicted.append(float(centered[label]))
            exact_local.append(
                local_pair_mass(s, label, reference, candidates, probabilities, columns)
                + unary_weight * probabilities[s][label]
            )
    x = rankdata(np.asarray(predicted))
    y = rankdata(np.asarray(exact_local))
    x -= np.mean(x)
    y -= np.mean(y)
    denominator = math.sqrt(float(np.dot(x, x) * np.dot(y, y)))
    return float(np.dot(x, y) / denominator) if denominator else float("nan")


def random_invertible_forms(r: int, seed: int, operations: int) -> tuple[int, ...]:
    rng = random.Random(seed)
    rows = [1 << check for check in range(r)]
    for _ in range(operations):
        target, source = rng.sample(range(r), 2)
        rows[target] ^= rows[source]
    if gf2_rank(rows) != r:
        raise AssertionError("row operations lost rank")
    return tuple(rows)


def redundant_forms(r: int, seed: int, count: int) -> tuple[int, ...]:
    rng = random.Random(seed)
    forms = [1 << check for check in range(r)]
    seen = set(forms)
    while len(forms) < r + count:
        weight = 2 if rng.random() < 0.7 else min(3, r)
        form = sum(1 << check for check in rng.sample(range(r), weight))
        if form not in seen:
            forms.append(form)
            seen.add(form)
    return tuple(forms)


@dataclass(frozen=True)
class ResultRow:
    experiment: str
    n: int
    r: int
    p: float
    code_seed: int
    decoder: str
    eta: float
    acceptance: float
    conditional_score: float
    retry_adjusted_excess: float
    expected_retries: float
    pair_mass: float
    runtime_seconds: float
    cost: int
    note: str = ""


def probability_table(
    candidates: Sequence[Sequence[int]], n: int, p: float
) -> tuple[tuple[float, ...], ...]:
    by_weight = probability_by_weight(n, p)
    return tuple(tuple(by_weight[error.bit_count()] for error in group) for group in candidates)


def append_row(
    rows: list[ResultRow],
    experiment: str,
    n: int,
    r: int,
    p: float,
    code_seed: int,
    decoder: str,
    eta: float,
    metrics: Metrics,
    runtime: float,
    cost: int,
    note: str = "",
) -> None:
    rows.append(
        ResultRow(
            experiment,
            n,
            r,
            p,
            code_seed,
            decoder,
            eta,
            metrics.acceptance,
            metrics.conditional_score,
            metrics.retry_adjusted_excess,
            metrics.expected_retries,
            metrics.pair_mass,
            runtime,
            cost,
            note,
        )
    )


def run_candidate_experiment(
    name: str,
    columns: Sequence[int],
    r: int,
    p: float,
    code_seed: int,
    topk: int,
    etas: Sequence[float],
    restarts: int,
    use_bp: bool,
    use_bethe: bool,
) -> tuple[list[ResultRow], dict]:
    n = len(columns)
    rows: list[ResultRow] = []
    start_time = time.perf_counter()
    base_candidates = topk_coset_candidates(columns, r, topk)
    exhaustive_topk_check(columns, base_candidates)
    candidate_seconds = time.perf_counter() - start_time

    configs = (
        BPConfig("BP-nominal", 1.0, 1.0, 16),
        BPConfig("BP-damped", 1.0, 0.55, 20),
        BPConfig("BP-temperature", 0.65, 0.70, 20),
    )
    bp_maps: dict[str, tuple[int, ...]] = {}
    costs: dict[str, int] = {}
    candidates = base_candidates
    if use_bp:
        bp_start = time.perf_counter()
        bp_maps, candidates, costs = bp_osd_maps_and_pool(
            columns, r, p, base_candidates, configs, osd_order=2
        )
        bp_seconds = time.perf_counter() - bp_start
    else:
        bp_seconds = 0.0
    probabilities = probability_table(candidates, n, p)
    ml_choice = tuple(group.index(base_candidates[s][0]) for s, group in enumerate(candidates))
    ml = mapping_metrics(ml_choice, candidates, probabilities, columns)
    append_row(
        rows, name, n, r, p, code_seed, "ML/coset-leader", 1.0, ml,
        candidate_seconds, 0, f"top-k DP candidate construction; k={topk}"
    )

    for label, mapping in bp_maps.items():
        choice = choice_for_mapping(mapping, candidates)
        metrics = mapping_metrics(choice, candidates, probabilities, columns)
        append_row(
            rows, name, n, r, p, code_seed, label + "+OSD2", 0.0, metrics,
            bp_seconds / max(1, len(bp_maps)), costs[label], "real-valued matched baseline"
        )

    validation: dict[str, object] = {
        "name": name,
        "n": n,
        "r": r,
        "p": p,
        "seed": code_seed,
        "candidate_pool_sizes": {
            "min": min(map(len, candidates)),
            "max": max(map(len, candidates)),
            "mean": sum(map(len, candidates)) / len(candidates),
        },
        "etas": {},
    }

    for eta in etas:
        threshold = eta * ml.acceptance
        coord_start = time.perf_counter()
        choice, metrics, sweeps = multistart_coordinate_ascent(
            ml_choice,
            candidates,
            probabilities,
            columns,
            threshold,
            seed=code_seed + int(10_000 * eta),
            restarts=restarts,
        )
        coord_seconds = time.perf_counter() - coord_start
        append_row(
            rows,
            name,
            n,
            r,
            p,
            code_seed,
            "exact-objective coordinate ascent",
            eta,
            metrics,
            coord_seconds,
            sweeps * len(columns) * (1 << r),
            f"Z >= {eta:.2f} Z_ML; {restarts} starts; {sweeps} total sweeps",
        )
        exact = exhaustive_candidate_optimum(candidates, probabilities, columns, threshold)
        if exact is not None:
            exact_choice, exact_metrics = exact
            append_row(
                rows,
                name,
                n,
                r,
                p,
                code_seed,
                "exhaustive candidate optimum",
                eta,
                exact_metrics,
                0.0,
                math.prod(len(group) for group in candidates),
                "exact validation on the identical candidate pool",
            )
            exhaustive_gap = exact_metrics.pair_mass - metrics.pair_mass
        else:
            exact_choice = None
            exhaustive_gap = None

        bethe_info = None
        if use_bethe:
            best_bethe = None
            for multiplier in (0.0, 0.25, 0.5, 1.0, 2.0, 5.0):
                unary_weight = multiplier * n
                bethe_start = time.perf_counter()
                raw_choice, beliefs = max_sum_bethe(
                    candidates, probabilities, columns, unary_weight, iterations=25
                )
                raw_metrics = mapping_metrics(raw_choice, candidates, probabilities, columns)
                elapsed = time.perf_counter() - bethe_start
                if raw_metrics.acceptance + 1e-14 < threshold:
                    continue
                polished_choice, polished_metrics, polished_sweeps = coordinate_ascent(
                    raw_choice,
                    candidates,
                    probabilities,
                    columns,
                    threshold,
                    seed=code_seed + int(multiplier * 1000) + 17,
                )
                correlation = bethe_local_rank_correlation(
                    beliefs,
                    polished_choice,
                    candidates,
                    probabilities,
                    columns,
                    unary_weight,
                )
                record = (
                    polished_metrics.pair_mass,
                    polished_metrics,
                    elapsed,
                    multiplier,
                    correlation,
                    polished_sweeps,
                )
                if best_bethe is None or record[0] > best_bethe[0]:
                    best_bethe = record
            if best_bethe is not None:
                _, bmetrics, elapsed, multiplier, correlation, polished_sweeps = best_bethe
                append_row(
                    rows,
                    name,
                    n,
                    r,
                    p,
                    code_seed,
                    "Bethe/max-sum + coordinate polish",
                    eta,
                    bmetrics,
                    elapsed,
                    25 * len(columns) * (1 << r),
                    f"lambda/n={multiplier:.2f}; local-rank Spearman={correlation:.4f}",
                )
                bethe_info = {
                    "lambda_over_n": multiplier,
                    "local_rank_spearman": correlation,
                    "acceptance": bmetrics.acceptance,
                    "pair_mass": bmetrics.pair_mass,
                }

        validation["etas"][str(eta)] = {
            "coordinate_acceptance": metrics.acceptance,
            "coordinate_pair_mass": metrics.pair_mass,
            "coordinate_gain_over_ml": metrics.pair_mass - ml.pair_mass,
            "exhaustive_gap": exhaustive_gap,
            "bethe": bethe_info,
        }
    return rows, validation


def run_representation_search(
    name: str,
    columns: Sequence[int],
    r: int,
    p: float,
    code_seed: int,
    eta: float,
    topk: int,
    representation_count: int,
) -> tuple[list[ResultRow], dict]:
    """Matched-edge-update search over a compact equivalent-factor-graph family."""
    n = len(columns)
    base_candidates = topk_coset_candidates(columns, r, topk)
    probabilities = probability_table(base_candidates, n, p)
    ml_choice = tuple(0 for _ in base_candidates)
    ml = mapping_metrics(ml_choice, base_candidates, probabilities, columns)
    identity = tuple(1 << check for check in range(r))
    _, _, identity_edges = representation_graph(columns, identity)
    update_budget = len(identity_edges) * 20
    configs = (
        BPConfig("nominal", 1.0, 1.0, 20),
        BPConfig("damped", 1.0, 0.55, 20),
        BPConfig("temperature", 0.65, 0.70, 20),
    )
    representations: list[tuple[str, tuple[int, ...]]] = [("identity", identity)]
    for index in range(representation_count):
        if index % 2 == 0:
            forms = random_invertible_forms(r, 100003 * code_seed + index, operations=2 * r)
            representations.append((f"row-transform-{index}", forms))
        else:
            forms = redundant_forms(r, 100003 * code_seed + index, count=max(1, r // 3))
            representations.append((f"redundant-{index}", forms))

    records = []
    rows: list[ResultRow] = []
    for rep_label, forms in representations:
        for config in configs:
            begin = time.perf_counter()
            maps, pool, costs = bp_osd_maps_and_pool(
                columns,
                r,
                p,
                base_candidates,
                (config,),
                check_forms=forms,
                update_budget=update_budget,
                osd_order=1,
            )
            elapsed = time.perf_counter() - begin
            map_label, mapping = next(iter(maps.items()))
            pool_prob = probability_table(pool, n, p)
            choice = choice_for_mapping(mapping, pool)
            metrics = mapping_metrics(choice, pool, pool_prob, columns)
            cost = next(iter(costs.values()))
            label = f"{rep_label}/{map_label}+OSD1"
            records.append((label, metrics, elapsed, cost, len(forms)))

    best_fer = max(records, key=lambda item: (item[1].acceptance, item[1].pair_mass))
    feasible = [item for item in records if item[1].acceptance + 1e-14 >= eta * best_fer[1].acceptance]
    best_dqi = max(feasible, key=lambda item: (item[1].pair_mass, item[1].acceptance))
    for selector, record in (("FER-selected representation", best_fer), ("DQI-selected representation", best_dqi)):
        label, metrics, elapsed, cost, form_count = record
        append_row(
            rows,
            name,
            n,
            r,
            p,
            code_seed,
            selector,
            eta,
            metrics,
            elapsed,
            cost,
            f"{label}; checks={form_count}; common edge-update budget={update_budget}",
        )
    info = {
        "name": name,
        "n": n,
        "r": r,
        "p": p,
        "seed": code_seed,
        "eta": eta,
        "family_size": len(records),
        "update_budget": update_budget,
        "fer_selected": {"label": best_fer[0], **asdict(best_fer[1])},
        "dqi_selected": {"label": best_dqi[0], **asdict(best_dqi[1])},
        "pair_mass_gain": best_dqi[1].pair_mass - best_fer[1].pair_mass,
    }
    return rows, info


def write_results(rows: Sequence[ResultRow], audit: dict) -> None:
    RESULT_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = RESULT_DIR / "decoder_codesign_results.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(rows[0]).keys()))
        writer.writeheader()
        writer.writerows(asdict(row) for row in rows)
    (RESULT_DIR / "decoder_codesign_audit.json").write_text(
        json.dumps(audit, indent=2, sort_keys=True), encoding="utf-8"
    )

    lines = [
        "# DQI-aware classical decoder co-design: reproducible results",
        "",
        "`retry_adjusted_excess = Z * (conditional_score - 1/2) = pair_mass / n`.",
        "All BP and OSD computations are real-valued and classical.",
        "",
        "| experiment | decoder | eta | Z | conditional S | retry-adjusted excess | retries | pair mass | seconds |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row.experiment} | {row.decoder} | {row.eta:.2f} | "
            f"{row.acceptance:.9f} | {row.conditional_score:.9f} | "
            f"{row.retry_adjusted_excess:.9f} | {row.expected_retries:.4f} | "
            f"{row.pair_mass:.9f} | {row.runtime_seconds:.3f} |"
        )
    (RESULT_DIR / "decoder_codesign_results.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--full", action="store_true", help="include n=40 and n=100 stress tests")
    parser.add_argument("--seeds", type=int, default=1, help="number of random codes per size")
    args = parser.parse_args()

    all_rows: list[ResultRow] = []
    audit: dict[str, object] = {"candidate_experiments": [], "representation_searches": []}

    small_columns = parity_check_columns_from_generator(5, (0b00111, 0b11100))
    rows, info = run_candidate_experiment(
        "exact-[5,2]", small_columns, 3, 0.32, 0, 4,
        etas=(0.95, 0.90, 0.80), restarts=12, use_bp=True, use_bethe=True
    )
    all_rows.extend(rows)
    audit["candidate_experiments"].append(info)
    rows, info = run_candidate_experiment(
        "exact-[5,2]-p0.40", small_columns, 3, 0.40, 0, 4,
        etas=(0.95, 0.90, 0.80), restarts=20, use_bp=True, use_bethe=True
    )
    all_rows.extend(rows)
    audit["candidate_experiments"].append(info)

    sizes = [(12, 5), (20, 8)]
    if args.full:
        sizes.extend([(40, 10), (100, 12)])
    for n, r in sizes:
        p = inverse_binary_entropy(r / n)
        for seed in range(args.seeds):
            columns = random_sparse_columns(n, r, seed=10_000 * n + seed)
            rows, info = run_candidate_experiment(
                f"random-sparse-{n}-{r}",
                columns,
                r,
                p,
                seed,
                topk=6 if n <= 20 else 4,
                etas=(0.95, 0.90, 0.80),
                restarts=8 if n <= 20 else 4,
                use_bp=n <= 40,
                use_bethe=n <= 20,
            )
            all_rows.extend(rows)
            audit["candidate_experiments"].append(info)

            if n in (20, 40) and seed == 0:
                rep_rows, rep_info = run_representation_search(
                    f"factor-graph-family-{n}-{r}",
                    columns,
                    r,
                    p,
                    seed,
                    eta=0.95,
                    topk=8,
                    representation_count=12,
                )
                all_rows.extend(rep_rows)
                audit["representation_searches"].append(rep_info)

    write_results(all_rows, audit)
    print(RESULT_DIR / "decoder_codesign_results.md")
    print(RESULT_DIR / "decoder_codesign_audit.json")


if __name__ == "__main__":
    main()
