# BP+OSD as a DQI syndrome decoder: research audit

Date: 1 September 2026

## Bottom line

There is a precise, implementable **finite-code gain**.  Run ordinary real
belief propagation (BP), use ordered-statistics decoding (OSD) to produce
syndrome-valid candidates, retain the minimum-Hamming-weight candidates, and
replace the usual BP-metric tie rule by a fixed canonical lexicographic tie
rule.  On two loopy sparse codes for which order-two OSD contains every exact
minimum-weight candidate, this changes neither classical frame success nor
DQI postselection probability, but strictly improves both the conditional DQI
score and the acceptance-weighted DQI reward.

This is not yet a superpolynomial quantum speedup.  The strict result concerns
decoder choice at fixed finite length.  A speedup claim additionally needs an
asymptotic problem family, a polynomial-size coherent BP+OSD circuit, a
nonvanishing output-quality advantage, polynomial postselection/repetition
cost, and a classical hardness result at the same output quality.

## Decoder definitions used in the audit

Let `H=B^T`, let `s` be a syndrome, and use a BSC design prior.  Ordinary
sum-product BP produces real log-likelihood ratios.  OSD uses their absolute
values to choose a basis, enumerates free-bit test patterns of order at most
two, and solves the pivot bits so that every output satisfies `H e=s`.

The matched list comparison is:

1. **BP+OSD, conventional tie:** minimize Hamming weight in the OSD list, then
   use the BP posterior metric.
2. **DQI-aware BP+OSD:** use the same list and the same minimum-weight primary
   metric, then select the lexicographically first tied word under one fixed
   coordinate order.

Both decoders therefore select an error of the same weight for every syndrome
and have exactly the same BSC acceptance `Z`.  When the OSD list contains the
complete minimum-weight fiber, the second rule is the canonical DQI-optimal ML
tie rule, not a fitted heuristic.

For a decoder `D`, the audit records

```
Z = sum_e pi(e) 1{D(H e)=e},
E = sum_{accepted one-bit pairs {e,e'}} sqrt(pi(e) pi(e')),
J = 1/2 + E/(m Z),
R = Z(J-1/2) = E/m.
```

`J` is the conditional DQI solution score.  `R` retains the postselection
cost and is therefore the safer decoder-design objective.

## Exact finite results on loopy sparse graphs

All syndromes were enumerated, so the displayed `Z`, `J`, and `R` are exact
for these finite codes.

| code | decoder | Z | J | R | online BP edge updates | OSD trials | tie work |
|---|---|---:|---:|---:|---:|---:|---:|
| cycle incidence, m=9,r=6 | conventional BP+OSD | 0.854148239 | 0.768658081 | 0.229473827 | 384 | 7 | 0 |
| same | DQI-aware BP+OSD | 0.854148239 | 0.772595185 | 0.232836697 | 384 | 7 | about 63 bit inspections |
| cycle incidence, m=12,r=7 | conventional BP+OSD | 0.741454363 | 0.740333617 | 0.178196409 | 504 | 16 | 0 |
| same | DQI-aware BP+OSD | 0.741454363 | 0.744551089 | 0.181323472 | 504 | 16 | about 192 bit inspections |

Thus the exact same-`Z` gains are

| code | delta J | delta R |
|---|---:|---:|
| m=9,r=6 | +0.003937104 | +0.003362870 |
| m=12,r=7 | +0.004217472 | +0.003127063 |

For both cases, the OSD candidate lists contain every exact ML fiber and the
DQI-aware output equals the exact canonical ML ceiling.  Larger restricted
lists in the audit also produced strict same-`Z` gains, but their incomplete
ML fibers remove the global guarantee.

The unbiased paired estimator was also rerun.  With common random pairs, 8192
pairs (32768 decoder-map calls when comparing both decoders) gave RMSE about
0.0017--0.0018 for the approximately 0.004 increase in `J`.  This estimator
is scalable but not free: when actual BP+OSD calls replace table lookups, its
offline work is the sample count times the full decoder cost.

Machine-readable results and the implementation are in this directory and in
`../dqi_bp_osd_matched_cost_audit.py`.

## Online circuit cost

For a Tanner graph with `M` edges, `T` BP iterations, and `b`-bit messages, a
quantized soft-BP implementation requires at least order `T M b` reversible
arithmetic operations.  A straightforward reversible implementation retains
iteration history and can require order `T M b` work qubits; reversible
pebbling can trade qubits for additional gates.

Let `u` be the number of free reliability positions tested by OSD and `q` its
order.  The number of candidates is

```
N_q = sum_{j=0}^q binomial(u,j).
```

The coherent OSD stage additionally needs reliability sorting, pivot/basis
selection, binary elimination, `N_q` syndrome-valid repairs, metric
calculation, minimum selection, and uncomputation.  For fixed `q`, this can
remain polynomial.  If the required `q` grows linearly with blocklength,
`N_q` is exponential and any DQI speedup is lost.  The canonical tie rule adds
only an `O(Lm)` comparison over an `L`-candidate list; it does not remove the
dominant BP or OSD circuit cost.

The closest existing coherent-DQI decoder work is:

* Sabater et al., *Towards solving industrial integer linear programs with
  Decoded Quantum Interferometry*, arXiv:2509.08328.  It implements a hard
  Gallager-style bit-flipping algorithm called BP1.  Its logical-qubit count is
  `(T+1)m + Tn + 2 ceil(log2(t+1))`.  The paper also reports that conventional
  soft BP (BP2) decodes better, but explicitly leaves an efficient BP2 quantum
  circuit as future work.  It contains no OSD circuit.
* Patamawisut et al., *Quantum Circuit Design for Decoded Quantum
  Interferometry*, arXiv:2504.18334.  It gives Gauss--Jordan and lookup-table
  decoder circuits; it does not implement the soft BP+OSD decoder studied
  here.
* Jordan et al., *Optimization by Decoded Quantum Interferometry*, Nature 646,
  2025.  It states a preparation cost `O(T_dec+m^2)` when the decoder has a
  coherent circuit of cost `T_dec`.  Its large sparse max-XORSAT BP runtime is
  classical and explicitly excludes coherent decoder and quantum-error-
  correction overhead.

Targeted searches found no published coherent BP+OSD implementation inside
DQI as of the date above.

## What DE-NFG contributes

The double-edge normal factor graph (DE-NFG) exposes `E`, the accepted
one-bit-pair term, and proves why `Z` or frame-error rate alone cannot rank
decoders for DQI.  It is useful as an exact evaluator on small or bounded-width
graphs and as a source of the pair objective.

For large graphs, direct paired sampling already gives an unbiased estimate
using two decoder calls per sample.  A loopy DE-NFG/Bethe evaluator has net
value only if it supplies a calibrated ranking at lower matched cost or lower
variance.  No such theorem or stable numerical advantage is presently
established.  Complex-valued DE-NFG messages are not required for the
phase-averaged binary accepted-pair statistic.

## No-go cases

The tie route gives no gain in any of the following regimes:

1. every relevant syndrome has a unique minimum-cost representative;
2. the baseline already uses a canonical downward-closed ML section;
3. DQI remains entirely inside a guaranteed unique-decoding radius;
4. generic continuous soft reliabilities remove exact ML ties;
5. decoder acceptance tends to one and the tie-sensitive boundary mass
   vanishes;
6. OSD needs exponentially many test patterns or its coherent implementation
   dominates the DQI circuit.

## Theorems required before claiming an end-to-end superpolynomial speedup

For an explicit growing family, one needs all of the following.

1. **Decoder performance:** `Z_m >= 1/poly(m)` and a target-quality probability
   at least `1/poly(m)`, together with a nonvanishing DQI-aware improvement in
   `J` or `R`.
2. **Coherent cost:** fixed precision, iteration count, list size, and OSD
   order with a proved polynomial gate, depth, and logical-qubit bound,
   including uncomputation.
3. **End-to-end cost:** polynomial state preparation, syndrome encoding,
   Fourier transform, postselection/repetitions, and fault-tolerant overhead.
4. **Matched quantum baseline:** the complete DQI algorithm beats the same
   classical routine used with quantum amplitude amplification at the same
   target quality.
5. **Classical barrier:** a proved lower bound, oracle separation, or clearly
   stated conditional hardness result showing that specialized classical
   optimization algorithms cannot reach that quality in polynomial time.

The Nature sparse max-XORSAT experiment does not meet item 5: its tailored
classical heuristic reaches a better satisfaction fraction than DQI+BP, and
the authors do not present that example as an exponential advantage.  Its OPI
claim uses an algebraic Reed--Solomon decoder, not BP+OSD.  Therefore the
finite strict gains above support a decoder-theory result, but not yet a
superpolynomial quantum-advantage result.

## Recommended claim

The defensible immediate claim is:

> A DQI-oriented tie rule can be added to BP+OSD at negligible classical
> reranking cost.  On explicit loopy sparse codes it strictly improves the DQI
> accepted-pair objective while preserving the entire syndrome-wise classical
> ML performance.  Establishing a scalable coherent OSD circuit and a
> nonvanishing asymptotic advantage remains open.

