"""Matched-cost audit of BP, BP+OSD, and DQI-aware BP+OSD.

This is a finite-code diagnostic, not an asymptotic quantum-speedup claim.
For each small loopy sparse parity-check matrix, it enumerates all syndromes so
that Z, J, and R are exact.  All OSD candidates satisfy H e = s.  The two
BP+OSD maps use the same candidate list and the same minimum-Hamming-weight
primary metric; they differ only in the tie rule:

* conventional: use the BP posterior metric;
* DQI-aware: use a fixed 0<1 lexicographic key.

Consequently they have exactly the same BSC acceptance Z.  When the OSD list
contains every true minimum-weight coset leader, the DQI-aware rule is the
canonical coefficientwise-optimal ML tie rule.  Otherwise the comparison is
only a restricted-list experiment.

The paired Monte Carlo estimator uses two decoder calls per sample and is
cross-checked against exact enumeration.  Cost counters separate the online
decoder from the offline DQI evaluator.
"""

from __future__ import annotations

import csv
import json
import math
import random
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Sequence

import numpy as np

import dqi_ml_tie_codesign as ties
import dqi_transversal_codesign as base


OUT = Path(__file__).with_name("dqi_bp_osd_matched_cost_results")


@dataclass(frozen=True)
class ExactMetrics:
    Z: float
    J: float
    R: float
    E: float
    expected_retries: float


@dataclass(frozen=True)
class DecoderRow:
    case: str
    decoder: str
    m: int
    r: int
    p: float
    tanner_edges: int
    bp_iterations: int
    osd_order: int
    osd_test_bits: int
    mean_list_size: float
    online_edge_updates: int
    online_osd_trials: int
    online_rerank_bit_ops: int
    estimated_bp1_logical_qubits: int
    Z: float
    J: float
    R: float
    E: float
    delta_Z_vs_bp_osd: float
    delta_J_vs_bp_osd: float
    delta_R_vs_bp_osd: float
    runtime_seconds_all_syndromes: float
    complete_ml_fiber_fraction: float
    note: str


@dataclass(frozen=True)
class EstimatorRow:
    case: str
    decoder: str
    samples: int
    repetitions: int
    decoder_calls_per_repetition: int
    projected_edge_updates_per_repetition: int
    mean_Z: float
    rmse_Z: float
    mean_J: float
    rmse_J: float
    mean_R: float
    rmse_R: float
    runtime_seconds: float


@dataclass(frozen=True)
class DifferenceEstimatorRow:
    case: str
    samples: int
    repetitions: int
    decoder_calls_per_repetition: int
    exact_delta_J: float
    mean_delta_J: float
    rmse_delta_J: float
    exact_delta_R: float
    mean_delta_R: float
    rmse_delta_R: float


def probability(error: int, m: int, p: float) -> float:
    w = error.bit_count()
    return p**w * (1.0 - p) ** (m - w)


def exact_metrics(mapping: Sequence[int], columns: Sequence[int], p: float) -> ExactMetrics:
    m = len(columns)
    z = sum(probability(error, m, p) for error in mapping)
    directed = 0.0
    for s, error in enumerate(mapping):
        pe = probability(error, m, p)
        for bit, column in enumerate(columns):
            other = mapping[s ^ column]
            if other == (error ^ (1 << bit)):
                directed += math.sqrt(pe * probability(other, m, p))
    edge_mass = 0.5 * directed
    return ExactMetrics(
        Z=z,
        J=0.5 + edge_mass / (m * z),
        R=edge_mass / m,
        E=edge_mass,
        expected_retries=1.0 / z,
    )


def tanner_edge_count(columns: Sequence[int]) -> int:
    return sum(column.bit_count() for column in columns)


def max_check_degree(columns: Sequence[int], r: int) -> int:
    return max(sum((column >> check) & 1 for column in columns) for check in range(r))


def bp1_qubits(m: int, r: int, iterations: int, check_degree: int) -> int:
    # Eq. (71) of Sabater et al., with their syndrome-register size n replaced by r.
    return (
        (iterations + 1) * m
        + iterations * r
        + 2 * math.ceil(math.log2(check_degree + 1))
    )


def build_maps(
    columns: Sequence[int],
    r: int,
    p: float,
    iterations: int,
    osd_order: int,
    test_bits: int,
) -> tuple[dict[str, tuple[int, ...]], dict[str, int | float], ties.TieCatalogue]:
    start = time.perf_counter()
    llrs, edge_count = base.all_syndrome_bp_llrs(
        columns, r, p, iterations=iterations, damping=0.65
    )
    bp_runtime = time.perf_counter() - start
    states = 1 << r
    bp_projection: list[int] = []
    conventional: list[int] = []
    dqi_aware: list[int] = []
    list_sizes: list[int] = []
    lists: list[tuple[int, ...]] = []
    generation_start = time.perf_counter()
    for s in range(states):
        projected = base.osd_candidates(
            columns, r, s, llrs[s], order=0, test_bits=0
        )[0]
        group = base.osd_candidates(
            columns, r, s, llrs[s], order=osd_order, test_bits=test_bits
        )
        minimum = min(error.bit_count() for error in group)
        tied = tuple(error for error in group if error.bit_count() == minimum)
        # Same primary BSC metric, different secondary tie key.
        conventional_choice = min(
            tied,
            key=lambda error: (base.llr_metric(error, llrs[s]), -error),
        )
        dqi_choice = min(tied)  # fixed binary lex order, 0 < 1
        bp_projection.append(projected)
        conventional.append(conventional_choice)
        dqi_aware.append(dqi_choice)
        lists.append(group)
        list_sizes.append(len(group))
    osd_runtime = time.perf_counter() - generation_start

    # Exact minimum-weight fibers certify whether the restricted OSD list is complete.
    catalogue = ties.minimum_weight_ties(columns, r, cap=4096, selection_seed=0)
    complete = 0
    for s, exact_group in enumerate(catalogue.candidates):
        exact_set = set(exact_group)
        osd_min = min(error.bit_count() for error in lists[s])
        osd_min_set = {error for error in lists[s] if error.bit_count() == osd_min}
        if (
            osd_min == catalogue.minimum_weights[s]
            and catalogue.exact_tie_counts[s] == len(exact_group)
            and exact_set.issubset(osd_min_set)
        ):
            complete += 1
    exact_canonical = tuple(min(group) for group in catalogue.candidates)
    effective_test_bits = min(test_bits, len(columns) - r)
    trial_count = 1 + effective_test_bits
    if osd_order >= 2:
        trial_count += effective_test_bits * (effective_test_bits - 1) // 2
    stats: dict[str, int | float] = {
        "bp_runtime": bp_runtime,
        "osd_runtime": osd_runtime,
        "edge_count": edge_count,
        "mean_list_size": sum(list_sizes) / len(list_sizes),
        "osd_trials": trial_count,
        "complete_fraction": complete / states,
    }
    return {
        "BP + syndrome projection": tuple(bp_projection),
        "BP+OSD, conventional BP-metric tie": tuple(conventional),
        "DQI-aware BP+OSD, canonical tie": tuple(dqi_aware),
        "exact canonical ML ceiling": exact_canonical,
    }, stats, catalogue


def paired_estimate(
    mapping: Sequence[int],
    columns: Sequence[int],
    p: float,
    samples: int,
    seed: int,
) -> ExactMetrics:
    rng = random.Random(seed)
    m = len(columns)
    z_sum = 0.0
    pair_sum = 0.0
    for _ in range(samples):
        bit = rng.randrange(m)
        e0 = 0
        for j in range(m):
            if j != bit and rng.random() < p:
                e0 |= 1 << j
        e1 = e0 | (1 << bit)
        a0 = float(mapping[base.syndrome(e0, columns)] == e0)
        a1 = float(mapping[base.syndrome(e1, columns)] == e1)
        # Conditional averaging over the forced coordinate is an unbiased Z sample.
        z_sum += (1.0 - p) * a0 + p * a1
        pair_sum += a0 * a1
    z = z_sum / samples
    r_value = math.sqrt(p * (1.0 - p)) * pair_sum / samples
    j = 0.5 + r_value / z if z else float("nan")
    return ExactMetrics(z, j, r_value, r_value * m, 1.0 / z if z else float("inf"))


def paired_audit(
    case: str,
    decoder: str,
    mapping: Sequence[int],
    columns: Sequence[int],
    p: float,
    exact: ExactMetrics,
    online_edge_updates: int,
    budgets: Sequence[int],
    repetitions: int,
) -> list[EstimatorRow]:
    rows: list[EstimatorRow] = []
    for samples in budgets:
        start = time.perf_counter()
        estimates = [
            paired_estimate(mapping, columns, p, samples, 1000003 * samples + rep)
            for rep in range(repetitions)
        ]
        elapsed = time.perf_counter() - start

        def mean(name: str) -> float:
            return sum(getattr(item, name) for item in estimates) / repetitions

        def rmse(name: str, target: float) -> float:
            return math.sqrt(
                sum((getattr(item, name) - target) ** 2 for item in estimates)
                / repetitions
            )

        rows.append(
            EstimatorRow(
                case=case,
                decoder=decoder,
                samples=samples,
                repetitions=repetitions,
                decoder_calls_per_repetition=2 * samples,
                projected_edge_updates_per_repetition=2 * samples * online_edge_updates,
                mean_Z=mean("Z"),
                rmse_Z=rmse("Z", exact.Z),
                mean_J=mean("J"),
                rmse_J=rmse("J", exact.J),
                mean_R=mean("R"),
                rmse_R=rmse("R", exact.R),
                runtime_seconds=elapsed,
            )
        )
    return rows


def paired_difference_audit(
    case: str,
    conventional: Sequence[int],
    dqi_aware: Sequence[int],
    columns: Sequence[int],
    p: float,
    conventional_exact: ExactMetrics,
    dqi_exact: ExactMetrics,
    budgets: Sequence[int],
    repetitions: int,
) -> list[DifferenceEstimatorRow]:
    """Common-random-number estimate of the small DQI-aware gain."""
    out: list[DifferenceEstimatorRow] = []
    m = len(columns)
    for samples in budgets:
        delta_j: list[float] = []
        delta_r: list[float] = []
        for rep in range(repetitions):
            rng = random.Random(9000011 * samples + rep)
            z = [0.0, 0.0]
            pair = [0.0, 0.0]
            maps = (conventional, dqi_aware)
            for _ in range(samples):
                bit = rng.randrange(m)
                e0 = 0
                for j in range(m):
                    if j != bit and rng.random() < p:
                        e0 |= 1 << j
                e1 = e0 | (1 << bit)
                s0 = base.syndrome(e0, columns)
                s1 = s0 ^ columns[bit]
                for index, mapping in enumerate(maps):
                    a0 = float(mapping[s0] == e0)
                    a1 = float(mapping[s1] == e1)
                    z[index] += (1.0 - p) * a0 + p * a1
                    pair[index] += a0 * a1
            estimate = []
            for index in range(2):
                zi = z[index] / samples
                ri = math.sqrt(p * (1.0 - p)) * pair[index] / samples
                ji = 0.5 + ri / zi if zi else float("nan")
                estimate.append((ji, ri))
            delta_j.append(estimate[1][0] - estimate[0][0])
            delta_r.append(estimate[1][1] - estimate[0][1])
        exact_dj = dqi_exact.J - conventional_exact.J
        exact_dr = dqi_exact.R - conventional_exact.R
        mean_dj = sum(delta_j) / repetitions
        mean_dr = sum(delta_r) / repetitions
        out.append(
            DifferenceEstimatorRow(
                case=case,
                samples=samples,
                repetitions=repetitions,
                # Both mappings are evaluated at both endpoints: four calls.
                decoder_calls_per_repetition=4 * samples,
                exact_delta_J=exact_dj,
                mean_delta_J=mean_dj,
                rmse_delta_J=math.sqrt(
                    sum((value - exact_dj) ** 2 for value in delta_j) / repetitions
                ),
                exact_delta_R=exact_dr,
                mean_delta_R=mean_dr,
                rmse_delta_R=math.sqrt(
                    sum((value - exact_dr) ** 2 for value in delta_r) / repetitions
                ),
            )
        )
    return out


def run_case(
    case: str,
    columns: Sequence[int],
    r: int,
    p: float,
    iterations: int = 12,
    osd_order: int = 2,
    test_bits: int = 7,
) -> tuple[list[DecoderRow], list[EstimatorRow], list[DifferenceEstimatorRow], dict]:
    m = len(columns)
    maps, stats, catalogue = build_maps(
        columns, r, p, iterations, osd_order, test_bits
    )
    edges = tanner_edge_count(columns)
    bp_updates = 2 * iterations * edges
    osd_trials = int(stats["osd_trials"])
    mean_list = float(stats["mean_list_size"])
    conventional_metrics = exact_metrics(
        maps["BP+OSD, conventional BP-metric tie"], columns, p
    )
    rows: list[DecoderRow] = []
    exact_by_name: dict[str, ExactMetrics] = {}
    for name, mapping in maps.items():
        begin = time.perf_counter()
        metric = exact_metrics(mapping, columns, p)
        elapsed = time.perf_counter() - begin
        exact_by_name[name] = metric
        uses_osd = "OSD" in name
        is_exact = name.startswith("exact")
        online_trials = osd_trials if uses_osd else 0
        rerank = int(round(mean_list * m)) if "DQI-aware" in name else 0
        note = ""
        if "DQI-aware" in name:
            note = (
                "same OSD list and same minimum-weight primary metric as conventional; "
                "only the tie key changes"
            )
        elif is_exact:
            note = "exponential-table ceiling; not an online scalable decoder"
        rows.append(
            DecoderRow(
                case=case,
                decoder=name,
                m=m,
                r=r,
                p=p,
                tanner_edges=edges,
                bp_iterations=iterations if not is_exact else 0,
                osd_order=osd_order if uses_osd else 0,
                osd_test_bits=test_bits if uses_osd else 0,
                mean_list_size=mean_list if uses_osd else 1.0,
                online_edge_updates=bp_updates if not is_exact else 0,
                online_osd_trials=online_trials,
                online_rerank_bit_ops=rerank,
                estimated_bp1_logical_qubits=(
                    bp1_qubits(m, r, iterations, max_check_degree(columns, r))
                    if not is_exact
                    else 0
                ),
                Z=metric.Z,
                J=metric.J,
                R=metric.R,
                E=metric.E,
                delta_Z_vs_bp_osd=metric.Z - conventional_metrics.Z,
                delta_J_vs_bp_osd=metric.J - conventional_metrics.J,
                delta_R_vs_bp_osd=metric.R - conventional_metrics.R,
                runtime_seconds_all_syndromes=(
                    float(stats["bp_runtime"]) + float(stats["osd_runtime"]) + elapsed
                    if not is_exact
                    else elapsed
                ),
                complete_ml_fiber_fraction=float(stats["complete_fraction"]),
                note=note,
            )
        )

    estimator_rows: list[EstimatorRow] = []
    for name in (
        "BP+OSD, conventional BP-metric tie",
        "DQI-aware BP+OSD, canonical tie",
    ):
        estimator_rows.extend(
            paired_audit(
                case,
                name,
                maps[name],
                columns,
                p,
                exact_by_name[name],
                bp_updates,
                budgets=(128, 512, 2048, 8192),
                repetitions=24,
            )
        )

    difference_rows = paired_difference_audit(
        case,
        maps["BP+OSD, conventional BP-metric tie"],
        maps["DQI-aware BP+OSD, canonical tie"],
        columns,
        p,
        exact_by_name["BP+OSD, conventional BP-metric tie"],
        exact_by_name["DQI-aware BP+OSD, canonical tie"],
        budgets=(128, 512, 2048, 8192),
        repetitions=24,
    )

    audit = {
        "case": case,
        "columns": list(columns),
        "minimum_weight_tied_syndrome_fraction": sum(
            count > 1 for count in catalogue.exact_tie_counts
        )
        / len(catalogue.exact_tie_counts),
        "maximum_exact_tie_count": max(catalogue.exact_tie_counts),
        "osd_complete_ml_fiber_fraction": stats["complete_fraction"],
        "strict_same_Z_gain": (
            abs(
                exact_by_name["DQI-aware BP+OSD, canonical tie"].Z
                - conventional_metrics.Z
            )
            < 1e-12
            and exact_by_name["DQI-aware BP+OSD, canonical tie"].J
            > conventional_metrics.J + 1e-12
        ),
    }
    return rows, estimator_rows, difference_rows, audit


def write_outputs(
    decoder_rows: Sequence[DecoderRow],
    estimator_rows: Sequence[EstimatorRow],
    difference_rows: Sequence[DifferenceEstimatorRow],
    audits: Sequence[dict],
) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / "decoder_metrics.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(asdict(decoder_rows[0]).keys()))
        writer.writeheader()
        writer.writerows(asdict(row) for row in decoder_rows)
    with (OUT / "paired_estimator.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(asdict(estimator_rows[0]).keys()))
        writer.writeheader()
        writer.writerows(asdict(row) for row in estimator_rows)
    with (OUT / "paired_difference_estimator.csv").open(
        "w", newline="", encoding="utf-8"
    ) as f:
        writer = csv.DictWriter(f, fieldnames=list(asdict(difference_rows[0]).keys()))
        writer.writeheader()
        writer.writerows(asdict(row) for row in difference_rows)
    (OUT / "audit.json").write_text(
        json.dumps(list(audits), indent=2, sort_keys=True), encoding="utf-8"
    )

    lines = [
        "# BP+OSD for DQI: matched-cost finite-code audit",
        "",
        "## Exact decoder metrics",
        "",
        "| case | decoder | Z | J | R | dZ | dJ | dR | edge updates | OSD trials | rerank bit ops | complete ML fibers |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in decoder_rows:
        lines.append(
            f"| {row.case} | {row.decoder} | {row.Z:.9f} | {row.J:.9f} | "
            f"{row.R:.9f} | {row.delta_Z_vs_bp_osd:+.3e} | "
            f"{row.delta_J_vs_bp_osd:+.3e} | {row.delta_R_vs_bp_osd:+.3e} | "
            f"{row.online_edge_updates} | {row.online_osd_trials} | "
            f"{row.online_rerank_bit_ops} | {row.complete_ml_fiber_fraction:.3f} |"
        )
    lines.extend(
        [
            "",
            "## Paired-estimator accuracy",
            "",
            "| case | decoder | pairs | calls | RMSE(Z) | RMSE(J) | RMSE(R) |",
            "|---|---|---:|---:|---:|---:|---:|",
        ]
    )
    for row in estimator_rows:
        lines.append(
            f"| {row.case} | {row.decoder} | {row.samples} | "
            f"{row.decoder_calls_per_repetition} | {row.rmse_Z:.3e} | "
            f"{row.rmse_J:.3e} | {row.rmse_R:.3e} |"
        )
    lines.extend(
        [
            "",
            "## Common-random-number estimate of the DQI-aware gain",
            "",
            "| case | pairs | calls | exact dJ | mean dJ | RMSE(dJ) | exact dR | mean dR | RMSE(dR) |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in difference_rows:
        lines.append(
            f"| {row.case} | {row.samples} | {row.decoder_calls_per_repetition} | "
            f"{row.exact_delta_J:+.3e} | {row.mean_delta_J:+.3e} | "
            f"{row.rmse_delta_J:.3e} | {row.exact_delta_R:+.3e} | "
            f"{row.mean_delta_R:+.3e} | {row.rmse_delta_R:.3e} |"
        )
    lines.extend(
        [
            "",
            "## Scope",
            "",
            "The exact metrics enumerate all syndromes and are ground truth only for these small codes. "
            "The paired estimator remains scalable because it uses two decoder calls per pair. "
            "The BP1 qubit count is a comparator only: soft BP+OSD needs fixed-precision arithmetic, "
            "sorting, elimination, list storage, and uncomputation that are not included in that formula.",
        ]
    )
    (OUT / "REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    cases = [
        (
            "cycle-complete-9x6",
            ties.cycle_rich_columns(vertices=7, edge_count=9, seed=173),
            6,
            0.14,
        ),
        (
            "cycle-complete-12x7",
            ties.cycle_rich_columns(vertices=8, edge_count=12, seed=185),
            7,
            0.14,
        ),
        (
            "cycle-rich-16x7",
            ties.cycle_rich_columns(vertices=8, edge_count=16, seed=91),
            7,
            0.14,
        ),
        (
            "random-sparse-18x8",
            base.random_sparse_columns(18, 8, seed=1808, column_weight=3),
            8,
            0.13,
        ),
        (
            "random-sparse-22x9",
            base.random_sparse_columns(22, 9, seed=2209, column_weight=3),
            9,
            0.12,
        ),
    ]
    decoder_rows: list[DecoderRow] = []
    estimator_rows: list[EstimatorRow] = []
    difference_rows: list[DifferenceEstimatorRow] = []
    audits: list[dict] = []
    for case, columns, r, p in cases:
        rows, estimates, differences, audit = run_case(case, columns, r, p)
        decoder_rows.extend(rows)
        estimator_rows.extend(estimates)
        difference_rows.extend(differences)
        audits.append(audit)
        print(
            case,
            "strict_same_Z_gain=",
            audit["strict_same_Z_gain"],
            "complete=",
            f"{audit['osd_complete_ml_fiber_fraction']:.3f}",
        )
    write_outputs(decoder_rows, estimator_rows, difference_rows, audits)
    print(OUT / "REPORT.md")


if __name__ == "__main__":
    main()
