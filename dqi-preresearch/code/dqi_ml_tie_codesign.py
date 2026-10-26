"""DQI-aware tie-breaking among exactly ML-equivalent coset leaders.

For a BSC with p < 1/2, every minimum-weight representative of one syndrome
coset has the same posterior probability.  Choosing among these ties cannot
change frame-error probability or postselection probability Z.  It can change
the accepted one-bit pair mass E and hence the DQI score

    S = 1/2 + E/(n Z).

This script computes all minimum-weight ties (with an explicit cap only on
stored representatives), then coordinates their selection on the syndrome
graph.  It tests Hamming, extended-Hamming, BCH, cycle-rich incidence, and
random sparse parity-check matrices up to n=100.  Small candidate spaces are
exhausted exactly.  Real BP on edge-update-matched equivalent factor graphs is
also used as a compact tie-breaking family; FER cannot rank that family because
every output remains ML, while the DQI pair metric can.

No BPQM, complex-message advantage, or capacity claim is involved.
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

import dqi_transversal_codesign as base


RESULT_DIR = Path(__file__).with_name("dqi_codesign_results")


@dataclass(frozen=True)
class TieCatalogue:
    candidates: tuple[tuple[int, ...], ...]
    minimum_weights: tuple[int, ...]
    exact_tie_counts: tuple[int, ...]
    cap: int


def minimum_weight_ties(
    columns: Sequence[int], r: int, cap: int, selection_seed: int = 0
) -> TieCatalogue:
    """Dynamic program for exact min weights/counts and up to cap witnesses."""
    states = 1 << r
    infinity = len(columns) + 1
    weights = [infinity] * states
    counts = [0] * states
    witnesses: list[list[int]] = [[] for _ in range(states)]
    weights[0] = 0
    counts[0] = 1
    witnesses[0] = [0]
    rng = random.Random(selection_seed)
    for bit, column in enumerate(columns):
        bit_mask = 1 << bit
        new_weights = [infinity] * states
        new_counts = [0] * states
        new_witnesses: list[list[int]] = [[] for _ in range(states)]
        for s in range(states):
            no_weight = weights[s]
            yes_weight = weights[s ^ column] + 1
            best = min(no_weight, yes_weight)
            new_weights[s] = best
            values: list[int] = []
            if no_weight == best:
                new_counts[s] += counts[s]
                values.extend(witnesses[s])
            if yes_weight == best:
                new_counts[s] += counts[s ^ column]
                values.extend(mask | bit_mask for mask in witnesses[s ^ column])
            values = sorted(set(values))
            if len(values) > cap:
                # Retain the lexicographic endpoints and a reproducible sample;
                # exact_tie_counts still records the full number of minimizers.
                keep = {values[0], values[-1]}
                interior = values[1:-1]
                rng.shuffle(interior)
                keep.update(interior[: max(0, cap - len(keep))])
                values = sorted(keep)[:cap]
            new_witnesses[s] = values
        weights, counts, witnesses = new_weights, new_counts, new_witnesses
    if any(weight == infinity for weight in weights):
        raise RuntimeError("H is not full row rank")
    for s, group in enumerate(witnesses):
        for error in group:
            if base.syndrome(error, columns) != s or error.bit_count() != weights[s]:
                raise AssertionError("invalid minimum-weight witness")
    return TieCatalogue(
        tuple(tuple(group) for group in witnesses),
        tuple(weights),
        tuple(counts),
        cap,
    )


def hamming_columns(r: int) -> tuple[int, ...]:
    return tuple(range(1, 1 << r))


def extended_hamming_8_columns() -> tuple[int, ...]:
    return tuple((1 << 3) | label for label in range(8))


def bch_15_7_5_columns() -> tuple[int, ...]:
    # g(x)=1+x^4+x^6+x^7+x^8, the primitive narrow-sense BCH(15,7,5)
    generator = sum(1 << degree for degree in (0, 4, 6, 7, 8))
    rows = tuple(generator << shift for shift in range(7))
    return base.parity_check_columns_from_generator(15, rows)


def incidence_columns(vertices: int, edges: Sequence[tuple[int, int]]) -> tuple[int, ...]:
    """Delete the final incidence row; connected graphs then have full rank."""
    r = vertices - 1
    columns = []
    for left, right in edges:
        value = 0
        if left < r:
            value ^= 1 << left
        if right < r:
            value ^= 1 << right
        columns.append(value)
    if base.gf2_rank(columns) != r:
        raise ValueError("incidence graph is not connected")
    return tuple(columns)


def grid_3_by_3_columns() -> tuple[int, ...]:
    edges = []
    for row in range(3):
        for col in range(3):
            vertex = 3 * row + col
            if row + 1 < 3:
                edges.append((vertex, vertex + 3))
            if col + 1 < 3:
                edges.append((vertex, vertex + 1))
    return incidence_columns(9, edges)


def cycle_rich_columns(vertices: int, edge_count: int, seed: int) -> tuple[int, ...]:
    rng = random.Random(seed)
    edges = [(vertex, vertex + 1) for vertex in range(vertices - 1)]
    possible = [
        (left, right)
        for left in range(vertices)
        for right in range(left + 1, vertices)
        if (left, right) not in edges
    ]
    rng.shuffle(possible)
    edges.extend(possible[: max(0, edge_count - len(edges))])
    return incidence_columns(vertices, edges)


@dataclass(frozen=True)
class TieResult:
    experiment: str
    family: str
    n: int
    r: int
    p: float
    decoder: str
    acceptance: float
    conditional_score: float
    retry_adjusted_excess: float
    pair_mass: float
    score_gain: float
    retry_gain: float
    tied_syndrome_fraction: float
    tied_acceptance_fraction: float
    mean_tie_count: float
    max_tie_count: int
    truncated_syndrome_fraction: float
    runtime_seconds: float
    note: str


def tie_statistics(
    catalogue: TieCatalogue,
    probabilities: Sequence[Sequence[float]],
    ml_acceptance: float,
) -> tuple[float, float, float, int, float]:
    tied = [count > 1 for count in catalogue.exact_tie_counts]
    tied_fraction = sum(tied) / len(tied)
    tied_mass = sum(
        probabilities[s][0] for s, is_tied in enumerate(tied) if is_tied
    ) / ml_acceptance
    mean_count = sum(catalogue.exact_tie_counts) / len(catalogue.exact_tie_counts)
    max_count = max(catalogue.exact_tie_counts)
    truncated = sum(
        count > len(catalogue.candidates[s])
        for s, count in enumerate(catalogue.exact_tie_counts)
    ) / len(catalogue.candidates)
    return tied_fraction, tied_mass, mean_count, max_count, truncated


def append_tie_result(
    rows: list[TieResult],
    experiment: str,
    family: str,
    n: int,
    r: int,
    p: float,
    decoder: str,
    metrics: base.Metrics,
    baseline: base.Metrics,
    stats: tuple[float, float, float, int, float],
    runtime: float,
    note: str,
) -> None:
    rows.append(
        TieResult(
            experiment,
            family,
            n,
            r,
            p,
            decoder,
            metrics.acceptance,
            metrics.conditional_score,
            metrics.retry_adjusted_excess,
            metrics.pair_mass,
            metrics.conditional_score - baseline.conditional_score,
            metrics.retry_adjusted_excess - baseline.retry_adjusted_excess,
            *stats,
            runtime,
            note,
        )
    )


def bp_tie_mapping(
    llrs: np.ndarray, candidates: Sequence[Sequence[int]]
) -> tuple[int, ...]:
    choice = []
    for s, group in enumerate(candidates):
        choice.append(
            min(
                range(len(group)),
                key=lambda label: (base.llr_metric(group[label], llrs[s]), group[label]),
            )
        )
    return tuple(choice)


def tie_representation_search(
    columns: Sequence[int],
    r: int,
    p: float,
    catalogue: TieCatalogue,
    representation_count: int,
    seed: int,
) -> dict:
    candidates = catalogue.candidates
    probabilities = base.probability_table(candidates, len(columns), p)
    identity = tuple(1 << check for check in range(r))
    _, _, identity_edges = base.representation_graph(columns, identity)
    update_budget = 20 * len(identity_edges)
    representations: list[tuple[str, tuple[int, ...]]] = [("identity", identity)]
    for index in range(representation_count):
        if index % 2 == 0:
            representations.append(
                (
                    f"row-{index}",
                    base.random_invertible_forms(r, seed * 1009 + index, 2 * r),
                )
            )
        else:
            representations.append(
                (
                    f"redundant-{index}",
                    base.redundant_forms(r, seed * 1009 + index, max(1, r // 3)),
                )
            )
    configs = (
        base.BPConfig("nominal", 1.0, 1.0, 20),
        base.BPConfig("damped", 1.0, 0.55, 20),
        base.BPConfig("temperature", 0.65, 0.70, 20),
    )
    records = []
    for rep_label, forms in representations:
        _, _, edges = base.representation_graph(columns, forms)
        iterations = max(1, update_budget // len(edges))
        for config in configs:
            begin = time.perf_counter()
            llrs, edge_count = base.all_syndrome_bp_llrs(
                columns,
                r,
                p,
                check_forms=forms,
                iterations=iterations,
                input_scale=config.input_scale,
                damping=config.damping,
            )
            choice = bp_tie_mapping(llrs, candidates)
            metrics = base.mapping_metrics(choice, candidates, probabilities, columns)
            records.append(
                {
                    "label": f"{rep_label}/{config.label}",
                    "choice": choice,
                    "metrics": metrics,
                    "runtime": time.perf_counter() - begin,
                    "cost": iterations * edge_count,
                    "checks": len(forms),
                    "iterations": iterations,
                }
            )
    nominal_reference = records[0]
    identity_records = [record for record in records if record["label"].startswith("identity/")]
    tuned_reference = max(
        identity_records,
        key=lambda item: (item["metrics"].pair_mass, item["metrics"].conditional_score),
    )
    best = max(records, key=lambda item: (item["metrics"].pair_mass, item["metrics"].conditional_score))
    acceptances = [record["metrics"].acceptance for record in records]
    return {
        "family_size": len(records),
        "update_budget": update_budget,
        "acceptance_range": max(acceptances) - min(acceptances),
        "nominal_reference": nominal_reference,
        "reference": tuned_reference,
        "best": best,
        "pair_mass_gain": best["metrics"].pair_mass - tuned_reference["metrics"].pair_mass,
        "score_gain": best["metrics"].conditional_score - tuned_reference["metrics"].conditional_score,
        "nominal_pair_mass_gain": best["metrics"].pair_mass - nominal_reference["metrics"].pair_mass,
        "nominal_score_gain": best["metrics"].conditional_score - nominal_reference["metrics"].conditional_score,
    }


def run_one(
    experiment: str,
    family: str,
    columns: Sequence[int],
    r: int,
    p: float,
    cap: int,
    restarts: int,
    use_bethe: bool,
    use_representation_search: bool,
    seed: int,
) -> tuple[list[TieResult], dict]:
    n = len(columns)
    begin = time.perf_counter()
    catalogue = minimum_weight_ties(columns, r, cap, selection_seed=seed)
    catalogue_seconds = time.perf_counter() - begin
    probabilities = base.probability_table(catalogue.candidates, n, p)
    lex_choice = tuple(0 for _ in catalogue.candidates)
    lex = base.mapping_metrics(lex_choice, catalogue.candidates, probabilities, columns)
    stats = tie_statistics(catalogue, probabilities, lex.acceptance)
    rows: list[TieResult] = []
    append_tie_result(
        rows,
        experiment,
        family,
        n,
        r,
        p,
        "lexicographic ML tie-break",
        lex,
        lex,
        stats,
        catalogue_seconds,
        "exact ML; baseline tie rule",
    )

    coord_start = time.perf_counter()
    coord_choice, coord, sweeps = base.multistart_coordinate_ascent(
        lex_choice,
        catalogue.candidates,
        probabilities,
        columns,
        lex.acceptance - 1e-13,
        seed=seed,
        restarts=restarts,
    )
    coord_seconds = time.perf_counter() - coord_start
    if abs(coord.acceptance - lex.acceptance) > 2e-11:
        raise AssertionError("ML tie optimization changed acceptance")
    append_tie_result(
        rows,
        experiment,
        family,
        n,
        r,
        p,
        "DQI-aware ML tie coordinate ascent",
        coord,
        lex,
        stats,
        coord_seconds,
        f"{restarts} starts; {sweeps} total sweeps; same Z by construction",
    )

    exact = base.exhaustive_candidate_optimum(
        catalogue.candidates,
        probabilities,
        columns,
        lex.acceptance - 1e-13,
    )
    exact_gap = None
    if exact is not None:
        _, exact_metrics = exact
        exact_gap = exact_metrics.pair_mass - coord.pair_mass
        append_tie_result(
            rows,
            experiment,
            family,
            n,
            r,
            p,
            "exhaustive ML-tie optimum",
            exact_metrics,
            lex,
            stats,
            0.0,
            "global validation on all stored ML ties",
        )

    bethe_correlation = None
    if use_bethe and max(map(len, catalogue.candidates)) > 1:
        bethe_start = time.perf_counter()
        bethe_choice, beliefs = base.max_sum_bethe(
            catalogue.candidates, probabilities, columns, unary_weight=0.0, iterations=30
        )
        bethe_choice, bethe_metrics, _ = base.coordinate_ascent(
            bethe_choice,
            catalogue.candidates,
            probabilities,
            columns,
            lex.acceptance - 1e-13,
            seed=seed + 17,
        )
        bethe_correlation = base.bethe_local_rank_correlation(
            beliefs,
            bethe_choice,
            catalogue.candidates,
            probabilities,
            columns,
            unary_weight=0.0,
        )
        append_tie_result(
            rows,
            experiment,
            family,
            n,
            r,
            p,
            "Bethe/max-sum ML tie-break + polish",
            bethe_metrics,
            lex,
            stats,
            time.perf_counter() - bethe_start,
            f"offline local-rank Spearman={bethe_correlation:.4f}",
        )

    representation = None
    if use_representation_search and max(map(len, catalogue.candidates)) > 1:
        representation = tie_representation_search(
            columns, r, p, catalogue, representation_count=16, seed=seed
        )
        for decoder, record in (
            ("best tuned identity-graph BP ML tie-break", representation["reference"]),
            ("DQI-selected equivalent-graph BP tie-break", representation["best"]),
        ):
            append_tie_result(
                rows,
                experiment,
                family,
                n,
                r,
                p,
                decoder,
                record["metrics"],
                lex,
                stats,
                record["runtime"],
                f"{record['label']}; matched edge-update cost={record['cost']}",
            )
        representation = {
            "family_size": representation["family_size"],
            "update_budget": representation["update_budget"],
            "acceptance_range": representation["acceptance_range"],
            "reference_label": representation["reference"]["label"],
            "nominal_reference_label": representation["nominal_reference"]["label"],
            "best_label": representation["best"]["label"],
            "pair_mass_gain": representation["pair_mass_gain"],
            "score_gain": representation["score_gain"],
            "nominal_pair_mass_gain": representation["nominal_pair_mass_gain"],
            "nominal_score_gain": representation["nominal_score_gain"],
        }

    audit = {
        "experiment": experiment,
        "family": family,
        "n": n,
        "r": r,
        "p": p,
        "r_over_n": r / n,
        "binary_entropy_p": base.binary_entropy(p),
        "tie_statistics": {
            "tied_syndrome_fraction": stats[0],
            "tied_acceptance_fraction": stats[1],
            "mean_tie_count": stats[2],
            "max_tie_count": stats[3],
            "truncated_syndrome_fraction": stats[4],
        },
        "lex": asdict(lex),
        "coordinate": asdict(coord),
        "coordinate_score_gain": coord.conditional_score - lex.conditional_score,
        "coordinate_retry_gain": coord.retry_adjusted_excess - lex.retry_adjusted_excess,
        "exhaustive_pair_mass_gap": exact_gap,
        "bethe_local_rank_spearman": bethe_correlation,
        "representation_search": representation,
    }
    return rows, audit


def write_results(rows: Sequence[TieResult], audits: Sequence[dict]) -> None:
    RESULT_DIR.mkdir(parents=True, exist_ok=True)
    with (RESULT_DIR / "ml_tie_codesign_results.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(rows[0]).keys()))
        writer.writeheader()
        writer.writerows(asdict(row) for row in rows)
    (RESULT_DIR / "ml_tie_codesign_audit.json").write_text(
        json.dumps(list(audits), indent=2, sort_keys=True), encoding="utf-8"
    )
    lines = [
        "# DQI-aware exact-ML tie-breaking",
        "",
        "Every decoder in one experiment has the same ML frame success and postselection Z.",
        "",
        "| experiment | family | n | decoder | Z | S | score gain | retry gain | tied mass | max ties | trunc. | seconds |",
        "|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row.experiment} | {row.family} | {row.n} | {row.decoder} | "
            f"{row.acceptance:.9f} | {row.conditional_score:.9f} | "
            f"{row.score_gain:+.9f} | {row.retry_gain:+.9f} | "
            f"{row.tied_acceptance_fraction:.4f} | {row.max_tie_count} | "
            f"{row.truncated_syndrome_fraction:.4f} | {row.runtime_seconds:.3f} |"
        )
    (RESULT_DIR / "ml_tie_codesign_results.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )


def main() -> None:
    experiments = [
        ("hamming-7-4", "Hamming", hamming_columns(3), 3, 32, 8, True, False, 1),
        ("extended-hamming-8-4", "extended Hamming", extended_hamming_8_columns(), 4, 32, 12, True, True, 2),
        ("bch-15-7-5", "BCH", bch_15_7_5_columns(), 8, 32, 10, True, True, 3),
        ("grid-3x3-cycle", "cycle/incidence", grid_3_by_3_columns(), 8, 48, 12, True, True, 4),
        ("cycle-rich-20-12", "cycle/incidence", cycle_rich_columns(9, 20, 5), 8, 48, 10, True, True, 5),
        ("random-ldpc-20-8", "random LDPC", base.random_sparse_columns(20, 8, 20008), 8, 48, 10, True, True, 6),
        ("random-ldpc-40-10", "random LDPC", base.random_sparse_columns(40, 10, 40010), 10, 32, 6, False, False, 7),
        ("random-ldpc-100-12", "random LDPC", base.random_sparse_columns(100, 12, 100012), 12, 24, 4, False, False, 8),
    ]
    rows: list[TieResult] = []
    audits: list[dict] = []
    for name, family, columns, r, cap, restarts, bethe, representation, seed in experiments:
        p = base.inverse_binary_entropy(r / len(columns))
        result_rows, audit = run_one(
            name,
            family,
            columns,
            r,
            p,
            cap,
            restarts,
            bethe,
            representation,
            seed,
        )
        rows.extend(result_rows)
        audits.append(audit)
        print(
            name,
            f"gain={audit['coordinate_score_gain']:+.9f}",
            f"tie_mass={audit['tie_statistics']['tied_acceptance_fraction']:.4f}",
        )
    write_results(rows, audits)
    print(RESULT_DIR / "ml_tie_codesign_results.md")
    print(RESULT_DIR / "ml_tie_codesign_audit.json")


if __name__ == "__main__":
    main()
