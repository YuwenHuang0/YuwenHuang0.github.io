"""Reproduce the two aggregate rows in bp_osd_dqi_probe_confirm.csv."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from bp_osd_dqi_probe import run_probe


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("code/results/bp_osd_dqi_probe_confirm.reproduced.csv"),
    )
    args = parser.parse_args()
    rows = run_probe(
        seed=260902,
        matrices=3,
        trials=100,
        n_bits=72,
        n_checks=45,
        column_degrees=[5, 9],
        error_rates=[0.1],
        iterations=25,
        orders=[0, 1, 2],
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
