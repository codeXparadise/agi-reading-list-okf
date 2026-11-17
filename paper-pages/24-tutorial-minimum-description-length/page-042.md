---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 42
pages: [42]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "worst-case regret, where the worst-case is over all sequences. Formally, the maximum or worst-case regret of ¯P relative to M is defined as −log…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 42 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 42 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

worst-case regret, where the worst-case is over all sequences. Formally, the maximum or worst-case regret of ¯P relative to M is defined as

−log ¯P(xn) −{−log P(xn | ˆθ(xn))}

Rmax( ¯P):= max

.

xn∈X n

If we use Rmax as our quality measure, then the ‘optimal’ universal model relative to M, for given sample size n, is the distribution minimizing

−log ¯P(xn) −{−log P(xn | ˆθ(xn))}

¯P Rmax( ¯P) = min

min

¯P max xn∈X n

(2.16)

where the minimum is over all defective distributions on X n. The ¯P minimizing (2.16) corresponds to the code minimizing the additional number of bits compared to code in M that is best in hindsight in the worst-case over all possible xn. It turns out that we can solve for ¯P in (2.16). To this end, we first define the complexity of a given model M as

P(xn | ˆθ(xn)). (2.17)

X

COMPn(M):= log

xn∈X n

This quantity plays a fundamental role in refined MDL, Section 2.6. To get a first idea of why COMPn is called model complexity, note that the more sequences xn with large P(xn | ˆθ(xn)), the larger COMPn(M). In other words, the more sequences that can be fit well by an element of M, the larger M’s complexity.

Proposition 2.14 \[Shtarkov 1987\] Suppose that COMPn(M) is finite. Then the minimax regret (2.16) is uniquely achieved for the distribution ¯Pnml given by

¯Pnml(xn):= P(xn | ˆθ(xn))

. (2.18)

yn∈X n P(yn | ˆθ(yn))

P

The distribution ¯Pnml is known as the Shtarkov distribution or the normalized maximum likelihood (NML) distribution.

Proof Plug in ¯Pnml in (2.16) and notice that for all xn ∈X n,

−log ¯P(xn) −{−log P(xn | ˆθ(xn))} = Rmax( ¯P) = COMPn(M), (2.19)

so that ¯Pnml achieves the same regret, equal to COMPn(M), no matter what xn

actually obtains. Since every distribution P on X n with P̸ = ¯Pnml must satisfy P(zn) <

¯Pnml(zn) for at least one zn ∈X n, it follows that

Rmax(P) ≥−log P(zn) + log P(zn | ˆθ(zn)) >

−log ¯Pnml(zn) + log P(zn | ˆθ(zn)) = Rmax( ¯Pnml).

43

---

[previous page](page-041.md) · [next page](page-043.md) · [all pages](index.md)
