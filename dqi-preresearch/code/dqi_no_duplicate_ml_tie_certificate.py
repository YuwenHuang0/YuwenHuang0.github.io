"""Deterministic certificate for an indecomposable ML-tie separation family.

For fixed t >= 2 and odd n >= 2t-1, let d=2t, N=d+n, and

    g = (1^d, 0^n),       c = (e_1, 1^n),
    C_{t,n} = span{g,c}.

The program checks, without random sampling,

* the advertised sparse parity-check matrix and its rank;
* connectedness, distinct nonzero columns, and minimum distance;
* two syndrome-by-syndrome pointwise-weight-equivalent ML sections;
* exact equality of their BSC acceptance probabilities;
* their exact DQI accepted-edge score gap at p=1/5; and
* convergence to the closed-form nonzero asymptotic gap.

At p=1/5 every vertex probability and every adjacent-pair geometric mean
is rational, so all decoder and score assertions below use Fraction.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb


P = Fraction(1, 5)


def parity(value: int) -> int:
    return value.bit_count() & 1


def gf2_rank(rows: list[int]) -> int:
    basis: dict[int, int] = {}
    for row in rows:
        value = row
        while value:
            pivot = value.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = value
                break
            value ^= basis[pivot]
    return len(basis)


def generators(t: int, n: int) -> tuple[int, int]:
    d = 2 * t
    g = (1 << d) - 1
    c = 1 | (((1 << n) - 1) << d)
    return g, c


def codewords(t: int, n: int) -> tuple[int, int, int, int]:
    g, c = generators(t, n)
    return 0, g, c, g ^ c


def check_rows(t: int, n: int) -> list[int]:
    """Rows for x_j+x_{j+1}=0, z_j+z_{j+1}=0, x_1+x_2+z_1=0."""
    d = 2 * t
    inner = [(1 << j) | (1 << (j + 1)) for j in range(1, d - 1)]
    outer = [
        (1 << (d + j)) | (1 << (d + j + 1))
        for j in range(n - 1)
    ]
    bridge = 1 | (1 << 1) | (1 << d)
    return inner + outer + [bridge]


def syndrome(word: int, rows: list[int]) -> int:
    return sum((parity(word & row) << index) for index, row in enumerate(rows))


def columns(rows: list[int], length: int) -> tuple[int, ...]:
    return tuple(
        sum((((row >> coordinate) & 1) << check) for check, row in enumerate(rows))
        for coordinate in range(length)
    )


def tanner_connected(rows: list[int], length: int) -> bool:
    adjacency = [set() for _ in range(length + len(rows))]
    for check, row in enumerate(rows):
        check_vertex = length + check
        for coordinate in range(length):
            if (row >> coordinate) & 1:
                adjacency[coordinate].add(check_vertex)
                adjacency[check_vertex].add(coordinate)
    seen = {0}
    frontier = [0]
    while frontier:
        vertex = frontier.pop()
        for neighbor in adjacency[vertex] - seen:
            seen.add(neighbor)
            frontier.append(neighbor)
    return len(seen) == len(adjacency)


def structural_checks(t: int, n: int) -> dict[str, int]:
    d = 2 * t
    length = d + n
    rows = check_rows(t, n)
    code = codewords(t, n)
    assert len(rows) == length - 2
    assert gf2_rank(rows) == length - 2
    assert all(syndrome(word, rows) == 0 for word in code)
    assert len({word for word in range(1 << length) if syndrome(word, rows) == 0}) == 4
    assert max(row.bit_count() for row in rows) == 3
    assert tanner_connected(rows, length)
    cols = columns(rows, length)
    assert all(cols)
    assert len(set(cols)) == length
    nonzero_weights = sorted(word.bit_count() for word in code if word)
    assert nonzero_weights == sorted((d, n + 1, n + d - 1))
    assert min(nonzero_weights) == d
    assert min(nonzero_weights) >= 4

    # A binary dimension-two code is coordinate-decomposable only if some
    # pair of its three nonzero words has disjoint support.  None does here.
    nonzero = code[1:]
    assert all((left & right) != 0 for i, left in enumerate(nonzero) for right in nonzero[i + 1 :])
    return {
        "N": length,
        "rank": gf2_rank(rows),
        "dmin": min(nonzero_weights),
        "max_check_degree": max(row.bit_count() for row in rows),
    }


def choose_sections(t: int, n: int) -> tuple[dict[int, int], dict[int, int]]:
    """Construct the constant and parity-oriented exact ML sections.

    Each C-coset consists of two g-pairs.  First choose a g-pair with the
    smallest attainable Hamming weight; if both pairs tie, choose the one
    with the numerically smaller outer block.  Within that pair, the ML word
    is unique unless its d-bit block lies in the middle layer.  On a middle
    tie, the constant section chooses x_1=0, whereas the parity section
    chooses x_1=parity(z) for the selected outer block z.
    """
    d = 2 * t
    length = d + n
    outer_mask = (1 << n) - 1
    code = codewords(t, n)
    rows = check_rows(t, n)
    good: dict[int, int] = {}
    bad: dict[int, int] = {}

    for seed in range(1 << length):
        orbit = tuple(sorted(seed ^ codeword for codeword in code))
        if seed != orbit[0]:
            continue
        syndromes = {syndrome(word, rows) for word in orbit}
        assert len(syndromes) == 1
        key = next(iter(syndromes))

        pairs: dict[int, list[int]] = {}
        for word in orbit:
            z = (word >> d) & outer_mask
            pairs.setdefault(z, []).append(word)
        assert len(pairs) == 2 and all(len(pair) == 2 for pair in pairs.values())
        pair_minimum = {
            z: min(word.bit_count() for word in pair)
            for z, pair in pairs.items()
        }
        global_minimum = min(pair_minimum.values())
        winning_z = min(z for z, value in pair_minimum.items() if value == global_minimum)
        winners = [word for word in pairs[winning_z] if word.bit_count() == global_minimum]
        assert len(winners) in (1, 2)
        if len(winners) == 1:
            chosen_good = chosen_bad = winners[0]
        else:
            assert winners[0] ^ winners[1] == code[1]
            chosen_good = next(word for word in winners if (word & 1) == 0)
            target = parity(winning_z)
            chosen_bad = next(word for word in winners if (word & 1) == target)

        assert chosen_good.bit_count() == min(word.bit_count() for word in orbit)
        assert chosen_bad.bit_count() == min(word.bit_count() for word in orbit)
        assert chosen_good.bit_count() == chosen_bad.bit_count()
        good[key] = chosen_good
        bad[key] = chosen_bad

    assert len(good) == len(bad) == 1 << (length - 2)
    return good, bad


def direct_product_sections(t: int, n: int) -> tuple[set[int], set[int]]:
    """Reference sections for span{(1^d,0),(0,1^n)}."""
    d = 2 * t
    radius = (n - 1) // 2
    inner_mask = (1 << d) - 1
    good: set[int] = set()
    bad: set[int] = set()
    for canonical in range(1 << d):
        pair = (canonical, canonical ^ inner_mask)
        if canonical != min(pair):
            continue
        minimum = min(word.bit_count() for word in pair)
        winners = [word for word in pair if word.bit_count() == minimum]
        for z in range(1 << n):
            if z.bit_count() > radius:
                continue
            if len(winners) == 1:
                inner_good = inner_bad = winners[0]
            else:
                inner_good = next(word for word in winners if (word & 1) == 0)
                inner_bad = next(word for word in winners if (word & 1) == parity(z))
            good.add(inner_good | (z << d))
            bad.add(inner_bad | (z << d))
    assert len(good) == len(bad) == 1 << (d + n - 2)
    return good, bad


def vertex_probability(word: int, length: int) -> Fraction:
    weight = word.bit_count()
    return Fraction(4 ** (length - weight), 5**length)


def edge_probability(lower_weight: int, length: int) -> Fraction:
    """sqrt(pi_w*pi_{w+1}) at p=1/5."""
    return Fraction(2 * 4 ** (length - lower_weight - 1), 5**length)


def acceptance(section: set[int], length: int) -> Fraction:
    return sum((vertex_probability(word, length) for word in section), Fraction())


def edge_mass(section: set[int], length: int) -> Fraction:
    total = Fraction()
    for word in section:
        for coordinate in range(length):
            neighbor = word ^ (1 << coordinate)
            if word < neighbor and neighbor in section:
                total += edge_probability(min(word.bit_count(), neighbor.bit_count()), length)
    return total


def is_downset(section: set[int], length: int) -> bool:
    return all(
        (word ^ (1 << coordinate)) in section
        for word in section
        for coordinate in range(length)
        if (word >> coordinate) & 1
    )


def zeta_beta(t: int) -> tuple[Fraction, Fraction]:
    d = 2 * t
    zeta = sum(
        (Fraction(comb(d, weight)) * P**weight * (1 - P) ** (d - weight)
         for weight in range(t)),
        Fraction(),
    )
    beta = Fraction(comb(d, t), 2) * (P * (1 - P)) ** t
    return zeta + beta, beta


def exact_instance(t: int, n: int) -> dict[str, Fraction | int]:
    d = 2 * t
    length = d + n
    structure = structural_checks(t, n)
    good_map, bad_map = choose_sections(t, n)
    good = set(good_map.values())
    bad = set(bad_map.values())
    assert len(good) == len(bad) == 1 << (length - 2)
    assert all(good_map[key].bit_count() == bad_map[key].bit_count() for key in good_map)
    assert is_downset(good, length)
    assert not is_downset(bad, length)

    z_good = acceptance(good, length)
    z_bad = acceptance(bad, length)
    assert z_good == z_bad
    p_good = edge_mass(good, length)
    p_bad = edge_mass(bad, length)
    gap = (p_good - p_bad) / (length * z_good)
    assert gap > 0

    # The perturbation from the direct-product reference is confined to the
    # two central outer layers.  This is checked exactly as a set statement.
    reference_good, reference_bad = direct_product_sections(t, n)
    central = {(n - 1) // 2, (n + 1) // 2}
    for section, reference in ((good, reference_good), (bad, reference_bad)):
        assert all(((word >> d).bit_count() in central) for word in section ^ reference)

    return {
        **structure,
        "Z": z_good,
        "P_good": p_good,
        "P_bad": p_bad,
        "gap": gap,
    }


def product_identity(t: int, n: int) -> None:
    d = 2 * t
    length = d + n
    good, bad = direct_product_sections(t, n)
    zeta, beta = zeta_beta(t)
    radius = (n - 1) // 2
    z_outer = sum(
        (Fraction(comb(n, weight)) * P**weight * (1 - P) ** (n - weight)
         for weight in range(radius + 1)),
        Fraction(),
    )
    e_outer = sum(
        (Fraction((n - weight) * comb(n, weight))
         * P ** weight * (1 - P) ** (n - weight)
         * Fraction(1, 2)
         for weight in range(radius)),
        Fraction(),
    )
    # At p=1/5, sqrt(p/(1-p))=1/2, giving the expression above.
    assert acceptance(good, length) == acceptance(bad, length) == zeta * z_outer
    assert edge_mass(good, length) - edge_mass(bad, length) == beta * e_outer


def main() -> None:
    t = 2
    zeta, beta = zeta_beta(t)
    limit = beta * Fraction(2, 5) / zeta
    retry_limit = beta * Fraction(2, 5)
    print("C_{t,n}=span{(1^{2t},0^n),(e_1,1^n)} exact certificate")
    print(f"p=1/5, t={t}, zeta={zeta}={float(zeta):.9f}, beta={beta}={float(beta):.9f}")
    print(f"conditional-gap limit={limit}={float(limit):.12f}")
    print(f"retry-adjusted-gap limit={retry_limit}={float(retry_limit):.12f}")
    print(" n   N rank dmin  Z(exact)       score gap       residual to limit")
    residuals: list[Fraction] = []
    for n in range(3, 16, 2):
        result = exact_instance(t, n)
        product_identity(t, n)
        residual = limit - result["gap"]
        assert isinstance(residual, Fraction) and residual > 0
        residuals.append(residual)
        print(
            f"{n:2d} {result['N']:3d} {result['rank']:4d} {result['dmin']:4d}  "
            f"{float(result['Z']):.9f}   {float(result['gap']):.12f}   {float(residual):.12f}"
        )
    assert all(right < left for left, right in zip(residuals, residuals[1:]))
    print("PASS: all structural, ML, down-set, pointwise-weight, equal-Z, boundary, and score checks succeeded.")


if __name__ == "__main__":
    main()
