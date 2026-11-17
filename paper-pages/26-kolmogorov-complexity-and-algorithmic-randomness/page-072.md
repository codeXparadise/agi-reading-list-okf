---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 72
pages: [72]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "3.3. EFFECTIVELY NULL SETS 73 We say that a set 𝐴 ⊂ Ω is an effectively null set (with respect to the given measure) if for every 𝜀 0 one can…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 72 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 72 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

3.3. EFFECTIVELY NULL SETS 73
We say that a set 𝐴 ⊂ Ω is an effectively null set (with respect to the given
measure) if for every 𝜀 > 0 one can effectively find a family of intervals that cover
𝐴 and whose total measure does not exceed 𝜀.
Some details should be specified in this definition. First, we consider only
rational values of 𝜀 (otherwise it is not clear how 𝜀 could be given to an algorithm).
Second, we need to specify how the sequence of intervals (that cover 𝐴) is generated.
We do this as follows:
Definition. A set 𝐴 ⊂ Ω is called an effectively null set (with respect to a
given measure) if there exists a computable function 𝑥(·, ·) whose first argument is
a positive rational number, second argument is a natural number and values are
binary strings, such that:
(1) 𝐴 ⊂ Ω𝑥(𝜀,0) ∪ Ω𝑥(𝜀,1) ∪ Ω𝑥(𝜀,2) . . .;
(2) 𝑝(𝑥(𝜀, 0)) + 𝑝(𝑥(𝜀, 1)) + 𝑝(𝑥(𝜀, 2)) + . . . 6 𝜀
for any rational 𝜀 > 0. Note that we do not require the function 𝑥 to be total; if
𝑥(𝜀, 𝑖) is undefined, the corresponding term (in both conditions) is omitted.
68 Show that we get an equivalent version of the definition if we consider an
algorithm that gets 𝜀 > 0 as an input and enumerates a set of binary strings (by
printing its elements with arbitrary delays between elements) such that intervals
Ω𝑥 for generated 𝑥 cover 𝐴 and have total measure (the measure of the union of
the intervals) at most 𝜀. (Note that the total measure can be much smaller than
the sum of measures, if the intervals are not disjoint.)
69 Show that we get an equivalent definition if we consider only rational
numbers of the form 2−𝑘 (for integer 𝑘) instead of all rational 𝜀. Show that the
definition does not change if we replace the sign 6 by < in the second inequality.
[Hint: subtract from each interval its part covered by previous intervals, possibly
splitting it into several intervals.]
70 Show that we get an equivalent definition if we require that for each 𝜀 > 0
the domain of the function 𝑖 ↦ → 𝑥(𝜀, 𝑖) is an initial segment of N (or N itself).
71 Show that we get an equivalent definition if we require that the family
of intervals is decidable (instead of being enumerable). [Hint: An interval can
be split into small parts, so we may assume that intervals in the sequence have
non-increasing length, and the family of intervals becomes decicable.]
Let us give some examples of effectively null subsets of Ω (with respect to the
uniform measure).
A singleton whose only element is a sequence of zeros, is an effectively null
set. Indeed, for every 𝜀 > 0 we find an integer 𝑘 such that 2−𝑘 < 𝜀, and consider a
covering that consists of one interval Ω00...0 (corresponding to the string of 𝑘 zeros).
Formally speaking, 𝑥(𝜀, 0) = 0𝑘, where 0𝑘 stands for the sequence formed by
𝑘 zeros, and 𝑘 is the smallest integer such that 2−𝑘 < 𝜀. The values 𝑥(𝜀, 𝑖) are
undefined for 𝑖 > 0.
In this example the sequence 0000 . . . can be replaced by arbitrary computable
sequence of zeros and ones; we need only to consider its prefix of length 𝑘 instead
of 0𝑘.
However, for noncomputable sequences the situation could be different:
72 Prove that there exists a sequence 𝜔 ∈ Ω such that singleton {𝜔} is not
an effectively null set. [Hint: Consider all computable functions 𝑥 that satisfy

---

[previous page](page-071.md) · [next page](page-073.md) · [all pages](index.md)
