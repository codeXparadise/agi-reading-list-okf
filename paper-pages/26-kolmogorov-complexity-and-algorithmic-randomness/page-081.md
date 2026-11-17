---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 81
pages: [81]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "82 3. MARTIN-L ¨OF RANDOMNESS each and choose one of them where the total measure of corresponding intervals does not exceed 1/8, and so on. In this…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 81 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 81 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

82 3. MARTIN-L ¨OF RANDOMNESS
each and choose one of them where the total measure of corresponding intervals
does not exceed 1/8, and so on.
In this way we get a 0′-computable sequence with the following property: each
its prefix is at most half-covered by our intervals. In particular, no prefix of this
sequence can appear in the sequence 𝑥𝑖, and this is what we need. 
A similar but more geometric argument can be given if we consider reals in [0, 1]
instead of binary sequences. A point 𝑥 ∈ [0, 1] is ML-random with respect to the
Lebesgue measure on [0, 1] if its binary representation is ML-random with respect to
the uniform measure on the Cantor space. (A point can have two representations
but in this case both are computable and non-random, so we may ignore this
problem.) One can also give an equivalent definition of randomness directly. A set
𝑋 ⊂ [0, 1] is called an effectively null subset of [0, 1] if there exists an algorithm
that for every rational 𝜀 > 0 enumerates a cover of 𝑋 that consists of intervals with
rational endpoints whose sum of measures is less than 𝜀. Then a ML-random real
is a real not contained in any effectively null subset of [0, 1]. All this is just a simple
reformulation of corresponding notions and results for Cantor space since the only
difference is that some numbers have two representations (but this happens only
for countably many computable reals), and that we consider intervals with rational
endpoints instead of intervals with dyadic-rational endpoints (this does not matter
since we can split an interval with rational endpoints into a computable sequence
of dyadic intervals). In particular, the following statement is true:
85 Prove that there exists the largest effectively null subset of [0, 1], and its
elements are reals whose binary representations are not ML-random with respect
to the uniform measure in the Cantor space.
Now we can point out an “explicit” ML-random point. Consider an enumerable
family of open intervals that have total length less than 1 and cover all non-ML-
random points. The union of this intervals is an open set which is a proper subset
of [0, 1]. Its complement is a closed set, and this closed set has a minimal point.
By construction this point is ML-random.
86 Prove that the minimal point that is not covered by enumerable family of
open intervals with rational endpoints is lower semicomputable, i.e., it is a limit of
an increasing computable sequence of rational numbers (and therefore is computable
with the oracle for halting problem, 0′).
(See Section 5.7 (p. 170) for more details about random reals and for an alter-
native construction of a lower semicomputable ML-random real.)
The proof of Theorem 37 given above is a relativized version of the following
result:
87 Assume that 𝑥0, 𝑥1, 𝑥2, . . . is a computable sequence of binary strings and
the sum	∑︁
𝑖
2−𝑙(𝑥𝑖)
is less than 1 and is a computable real number. Then there exists a computable
sequence of zeros and ones that has neither of 𝑥𝑖 as its prefix.
[Hint: Let this sum be less than some rational 𝑆 < 1. By induction construct
a computable sequence 𝜔0𝜔1𝜔2 . . . with the following property: the fraction of the
set 𝑈 = ∪Ω𝑥𝑖 among the sequences that have prefix 𝜔0 . . . 𝜔𝑘 is less than 𝑆.]

---

[previous page](page-080.md) · [next page](page-082.md) · [all pages](index.md)
