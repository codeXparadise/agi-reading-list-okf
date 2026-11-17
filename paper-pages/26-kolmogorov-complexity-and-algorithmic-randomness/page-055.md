---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 55
pages: [55]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "56 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY below or above the boundary). To find a block with big complexity increase we may use the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 55 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 55 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

56 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
below or above the boundary). To find a block with big complexity increase we
may use the previous problem, for a block with small increase we can use a block
or zeros. Note that (large enough) ℎ is fixed, so it is enough to control complexity
on the blocks’ boundaries.]
48 Prove that an infinite sequence 𝑥0𝑥1𝑥2 . . . of zeros and ones is computable
if and only if the values 𝐶(𝑥0 . . . 𝑥𝑛−1 | 𝑛) (the complexities of its prefixes conditional
to their lengths) remain bounded by a constant.
[Hint: Consider an infinite binary tree. Let 𝑆 be the enumerable set of vertices
(binary strings) that have conditional complexity (w.r.t. their length) less than
some constant 𝑐. The “horizontal” sections of 𝑆 have cardinality 𝑂(1). We need to
derive from this that each infinite path that lies entirely inside 𝑆, is computable.
We may assume that 𝑆 is a subtree (only strings whose prefixes are in 𝑆, remain
in 𝑆).
Let 𝜔 be an infinite path that goes through 𝑆 only. At each level 𝑛 we count
vertices in 𝑆 on the left of 𝜔 (𝑙𝑛 vertices) and on the right of 𝜔 (𝑟𝑛 vertices). Let
𝐿 = lim sup 𝑙𝑛 and 𝑅 = lim sup 𝑟𝑛. Let 𝑁 be the level such that 𝐿 and 𝑅 are never
exceeded after this level. Knowing 𝐿, 𝑅 and 𝑁 we can compute arbitrarily large
prefixes of 𝜔. We should look for a path 𝜋 in a tree such that at some level above
𝑁 there are at least 𝐿 elements of 𝑆 on the left of 𝜋, and at some (possibly other)
level above 𝑁 there are at least 𝑅 elements on the right of 𝜋. When such a path 𝜋
is found, we can be sure that its initial segment (up to the first of those two levels)
coincides with 𝜔.]
This result was published in [107] (attributed to A.R. Meyer).
49 Prove that in the previous problem a weaker assumption is sufficient:
instead of 𝐶(𝑥0 . . . 𝑥𝑛−1 | 𝑛) = 𝑂(1) we can require that 𝐶(𝑥0 . . . 𝑥𝑛−1) 6 log 𝑛 + 𝑐
for some 𝑐 and for all 𝑛. [Hint: In this case we get an enumerable set 𝑆 of strings
(=tree vertices) with the following property: the number of vertices below level 𝑁
is 𝑂(𝑁 ). This means that the average number of vertices per level is bounded by a
constant. To use the previous problem, we need a bound for all levels and not for
the average value. We can achieve this if we consider only vertices 𝑥 ∈ 𝑆 that have
a extension of length 2𝑙(𝑥) that goes entirely inside 𝑆.]
This result was published in [33].
Following Problem 48, we can suggest different definitions of the complexity
notion for computable bit sequences:
∙ a minimal complexity of a program that, given 𝑛, computes 𝑥0 . . . 𝑥𝑛−1.
We can also consider a program that computes 𝑥𝑛 for input 𝑛, it gives the
same (up to 𝑂(1)) complexity. We denote this complexity by 𝐶(𝑥).
∙ a minimal complexity of a program that, given 𝑛, computes 𝑥0 . . . 𝑥𝑛 for
all sufficiently large 𝑛. For other 𝑛 (finitely many of them) this program
may provide a wrong answer or never terminate. It is denoted by 𝐶∞(𝑥).
∙ max{𝐶(𝑥0 . . . 𝑥𝑛−1 | 𝑛) | 𝑛 = 0, 1, . . . }, denoted by 𝑀 (𝑥).
∙ lim sup𝑛→∞ 𝐶(𝑥0 . . . 𝑥𝑛−1 | 𝑛), denoted by 𝑀∞(𝑥).
There are evident relations between these notions:
𝑀∞(𝑥) 6 𝑀 (𝑥) 6 𝐶(𝑥)
(up to 𝑂(1) additive term) and
𝑀∞(𝑥) 6 𝐶∞(𝑥) 6 𝐶(𝑥)

---

[previous page](page-054.md) · [next page](page-056.md) · [all pages](index.md)
