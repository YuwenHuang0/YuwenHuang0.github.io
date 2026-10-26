"""Exact audit for the DQI--ML reliability sensitivity identities.

The script uses only rational arithmetic.  It verifies, on exhaustive small
binary codes, both the radial derivative identity and its asymmetric
directional-derivative extension.  It is deliberately independent of the
other theorem-certificate scripts in this workspace.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
import random


def bit_weight(x: int) -> int:
    return x.bit_count()


def syndrome(row_masks: tuple[int, ...], x: int) -> int:
    s = 0
    for j, row in enumerate(row_masks):
        s |= ((row & x).bit_count() & 1) << j
    return s


def gf2_rank(row_masks: tuple[int, ...], m: int) -> int:
    rows = list(row_masks)
    rank = 0
    for col in range(m - 1, -1, -1):
        pivot = next((j for j in range(rank, len(rows)) if (rows[j] >> col) & 1), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for j in range(len(rows)):
            if j != rank and ((rows[j] >> col) & 1):
                rows[j] ^= rows[rank]
        rank += 1
    return rank


def canonical_radial_section(row_masks: tuple[int, ...], m: int) -> dict[int, int]:
    leaders: dict[int, int] = {}
    for x in range(1 << m):
        s = syndrome(row_masks, x)
        key = (bit_weight(x), x)
        if s not in leaders or key < (bit_weight(leaders[s]), leaders[s]):
            leaders[s] = x
    return leaders


def verify_radial(row_masks: tuple[int, ...], m: int, p: Fraction) -> None:
    leaders = canonical_radial_section(row_masks, m)
    selected = set(leaders.values())
    n = [0] * (m + 1)
    for e in selected:
        n[bit_weight(e)] += 1

    q = p / (1 - p)
    w = sum(Fraction(n[k]) * q**k for k in range(m + 1))
    wp = sum(Fraction(k * n[k]) * q ** (k - 1) for k in range(1, m + 1))
    pair_poly = Fraction(0)
    for e in selected:
        for i in range(m):
            if (e >> i) & 1 and (e ^ (1 << i)) in selected:
                pair_poly += q ** (bit_weight(e) - 1)
    assert pair_poly == wp

    z = (1 - p) ** m * w
    zp = -m * (1 - p) ** (m - 1) * w + (1 - p) ** (m - 2) * wp

    # Divide the square-root identity by sqrt(q), leaving a rational equality.
    lhs = wp / (m * w)
    rhs = (1 - p) + (1 - p) ** 2 * zp / (m * z)
    assert lhs == rhs


def product_probability(x: int, ps: tuple[Fraction, ...]) -> Fraction:
    value = Fraction(1)
    for i, p in enumerate(ps):
        value *= p if ((x >> i) & 1) else (1 - p)
    return value


def verify_asymmetric(
    row_masks: tuple[int, ...],
    m: int,
    odds_roots: tuple[int, ...],
    gammas: tuple[Fraction, ...],
) -> None:
    # p_i=1/(1+r_i^2) makes r_i=sqrt((1-p_i)/p_i) rational.
    ps = tuple(Fraction(1, 1 + r * r) for r in odds_roots)
    probs = [product_probability(x, ps) for x in range(1 << m)]
    fibers: dict[int, list[int]] = {}
    for x in range(1 << m):
        fibers.setdefault(syndrome(row_masks, x), []).append(x)

    selected: dict[int, int] = {}
    z = Fraction(0)
    directional = Fraction(0)
    c = sum(gammas[i] * Fraction(odds_roots[i], 1 + odds_roots[i] ** 2) for i in range(m))
    for s, fiber in fibers.items():
        best_prob = max(probs[x] for x in fiber)
        active = [x for x in fiber if probs[x] == best_prob]

        def g_value(x: int) -> Fraction:
            return sum(
                gammas[i] * odds_roots[i]
                for i in range(m)
                if (x >> i) & 1
            )

        chosen = min(active, key=lambda x: (-g_value(x), bit_weight(x), x))
        selected[s] = chosen
        z += best_prob
        directional += best_prob * (g_value(chosen) - c)

    selected_set = set(selected.values())
    for e in selected_set:
        for i in range(m):
            if (e >> i) & 1:
                assert (e ^ (1 << i)) in selected_set

    edge_mass = Fraction(0)
    for e in selected_set:
        for i in range(m):
            if (e >> i) & 1 and (e ^ (1 << i)) in selected_set:
                # sqrt(pi(e)pi(e-e_i)) = pi(e) r_i for the rational family.
                edge_mass += gammas[i] * probs[e] * odds_roots[i]

    assert edge_mass == directional + c * z


def random_full_rank_rows(rng: random.Random, rho: int, m: int) -> tuple[int, ...]:
    while True:
        rows = tuple(rng.randrange(1 << m) for _ in range(rho))
        if gf2_rank(rows, m) == rho:
            return rows


def main() -> None:
    rng = random.Random(20260814)
    radial_count = 0
    asymmetric_count = 0

    fixed = [
        (1, 3, (0b101,)),
        (2, 4, (0b1011, 0b0110)),
        (2, 5, (0b00111, 0b11001)),
        # Full row rank with a zero column and with repeated columns.
        (2, 5, (0b00101, 0b01010)),
    ]
    cases = list(fixed)
    for m in range(3, 8):
        for rho in range(1, min(3, m) + 1):
            for _ in range(5):
                cases.append((rho, m, random_full_rank_rows(rng, rho, m)))

    for _, m, rows in cases:
        for p in (Fraction(1, 11), Fraction(1, 5), Fraction(2, 7)):
            verify_radial(rows, m, p)
            radial_count += 1

        roots = tuple(rng.choice((2, 3, 4)) for _ in range(m))
        gammas = tuple(Fraction(rng.randint(1, 5), rng.randint(1, 4)) for _ in range(m))
        verify_asymmetric(rows, m, roots, gammas)
        asymmetric_count += 1

    print(f"radial exact identities passed: {radial_count}")
    print(f"asymmetric directional identities passed: {asymmetric_count}")


if __name__ == "__main__":
    main()
