---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 73
pages: [73]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "74 3. MARTIN-L ¨OF RANDOMNESS the second condition of the definition of effectively null set. There are countably many such functions. For each of…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 73 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 73 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

74 3. MARTIN-L ¨OF RANDOMNESS
the second condition of the definition of effectively null set. There are countably
many such functions. For each of them consider the largest set 𝐴 that satisfies the
requirement (1) of the definition (i.e., the intersection of the unions of coverings
over all 𝜀). This set is an (effectively) null set, and the union of a countable family
of those sets is a null set. Therefore, there exists a sequence 𝜔 which does not
belong to this union.]
Let us note that the statement of this problem is a straightforward corollary
of the Martin-L¨of theorem on the existence of the largest effectively null set (The-
orem 28, p. 75) proved later in this section, and the hint just follows its proof. As
we will see later, the set {𝜔} is an effectively null set if and only if the sequence 𝜔
is not “Martin-L¨of random”.
It is easy to construct a non-computable sequence 𝜔 such that the singleton {𝜔}
is an effective null set. Indeed, consider any sequence of the form 𝜔 = 0?0?0?0 . . .
(each second term is zero, the rest is arbitrary). Let us show that {𝜔} is indeed an
effectively null set. To find a covering with total measure 2−𝑛, consider all strings
of length 2𝑛 that are formed by 𝑛 arbitrary bits interleaved with 𝑛 zeros (as in 𝜔).
There are 2𝑛 strings of this form, and each corresponds to an interval of length
2−2𝑛, so the total measure is 2−𝑛.
In fact we have proved a bit more: the set of all sequences that have only
zeros at even positions, is an effectively null set. Therefore, each of its subsets (in
particular, every singleton) is an effectively null set.
Let us now return to the definition of an effectively null set and separate the
requirements used in this definition. We say that a computable function 𝑥 is “regu-
lar” if is satisfies the requirement (2). The requirement (1) then says that for every
rational 𝜀 > 0 the set 𝐴 is a subset of the union
Ω𝑥(𝜀,0) ∪ Ω𝑥(𝜀,1) ∪ Ω𝑥(𝜀,2) . . .
Therefore, a regular function “serves” all the subsets of the set⋂︁
𝜀>0
(Ω𝑥(𝜀,0) ∪ Ω𝑥(𝜀,1) ∪ Ω𝑥(𝜀,2) . . .) =⋂︁
𝜀>0
⋃︁
 𝑖
Ω𝑥(𝜀,𝑖)
So for each (computable) regular function 𝑥 we get an effectively null set (defined
by the formula above), and effectively null sets are all these sets (for all regular
functions) and all their subsets, and that’s all.
Before we formulate Martin-L¨of theorem, let us give the definition of a com-
putable measure on the set Ω.
A real number 𝛼 is called computable if there exists an algorithm that computes
rational approximations to 𝛼 with any given precision. Formally, 𝛼 is a computable
real if there exists a computable function 𝜀 ↦ → 𝑎(𝜀) defined on all positive rational
numbers and having rational values such that
|𝛼 − 𝑎(𝜀)| < 𝜀
for all rational 𝜀 > 0.
73 Show that we get an equivalent definition if we additionally require that
all approximation given by 𝑎 are approximations from below, i.e., 𝑎(𝜀) < 𝛼 for all
𝜀. [Hint: we can transform any approximation to the approximation from below
losing only factor 2 in precision.]
74 Prove that the sum, difference, product and quotient of two computable
reals are computable reals.

---

[previous page](page-072.md) · [next page](page-074.md) · [all pages](index.md)
