---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 77
pages: [77]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "78 3. MARTIN-L ¨OF RANDOMNESS set, but just one ML-random (typical) sequence added is enough to destroy this property. For example, recall that any…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 77 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 77 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

78 3. MARTIN-L ¨OF RANDOMNESS
set, but just one ML-random (typical) sequence added is enough to destroy this
property.
For example, recall that any computable sequence forms an effectively null
singleton (with respect to uniform measure). We immediately get the following
corollary:
Theorem 30. The set of all computable sequences of zeros and ones is an
effectively null subset of Ω (with respect to the uniform measure).
It is interesting to note that this observation was made before Martin-L¨of gave
the definition of randomness, while developing the constructive version of calculus
(“Zaslavsky construction” [219] used for many counterexamples; it deals with real
numbers instead of bit sequences).
In the next section we explore the properties of ML-random sequences (with re-
spect to the uniform measure). We end this section with the following nice criterion
for ML-randomness which is attributed to R. Solovay in [34].
Theorem 31. A sequence 𝜔 is not ML-random with respect to a computable
measure 𝜇 if and only if there exists s computable sequence of intervals with finite
sum of measures that covers 𝜔 infinitely many times, i.e., a computable sequence
of binary strings 𝑥0, 𝑥1, 𝑥2, . . . such that∑︁
𝑖
𝜇(Ω𝑥𝑖 ) < ∞
and 𝜔 ∈ Ω𝑥𝑖 for infinitely many 𝑖.
Proof. Assume that 𝜔 is not ML-random. Then for each 𝜀 we can effectively
find a computable sequence of intervals that covers {𝜔} and has the sum of measures
less than 𝜀. Then we combine these sequences for 𝜀 = 1, 1/2, 1/4, 1/8, . . . and get a
computable sequence of intervals with sum of measures not exceeding 2 that covers
𝜔 infinitely many times (at least once for each 𝜀).
On the other hand, assume that there is a computable sequence 𝑥0, 𝑥1, 𝑥2 . . .
of strings such that the sum of measures of corresponding intervals Ω𝑥𝑖 does not
exceed some constant 𝑐 and infinitely many of them contain 𝜔. We may assume
without loss of generality that 𝑐 is a rational number. To find a covering for 𝜔 that
has sum of measures less than 𝜀, we consider the set 𝑀𝑁 of all sequences in Ω that
are covered at least 𝑁 times. Here 𝑁 is a positive integer such that 𝑐/𝑁 < 𝜀. It
is easy to see that 𝑀𝑁 can be represented as the union of a computable sequence
of disjoint intervals (while reading 𝑥0, 𝑥1, . . ., we discover more and more elements
of 𝑀𝑁 and add respective intervals as they appear). Therefore the set {𝜔} is an
effectively null set and the sequence 𝜔 is not ML-random. 
Remark. This result is a constructive version of Borel–Cantelli Lemma (if the
sum of measures of sets 𝐴0, 𝐴1, . . . is finite, then the set of all points that belong
to infinitely many 𝐴𝑖 is a null set), and our argument is an effective version of
a classical proof of Borel–Cantelli Lemma. However, we should be careful since
not any classical proof can be effectivized. The standard proof (since the series is
converging, its tails could be made as small is needed) does not work here, since
there is no way to find an appropriate tail given 𝜀.
Martin-L¨of randomness is defined for computable measures: we used com-
putability to prove that the largest effectively null set exists. One could refor-
mulate the definition and call a sequence random (for an arbitrary measure 𝜇 on

---

[previous page](page-076.md) · [next page](page-078.md) · [all pages](index.md)
