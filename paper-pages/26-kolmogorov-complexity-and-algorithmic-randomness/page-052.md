---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 52
pages: [52]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "2.2. CONDITIONAL COMPLEXITY 53 cardinality of 𝐴 does not exceed 𝑝𝑞. Then we can split 𝐴 into parts 𝑃 and 𝑄 with the following properties: the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 52 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 52 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

2.2. CONDITIONAL COMPLEXITY 53
cardinality of 𝐴 does not exceed 𝑝𝑞. Then we can split 𝐴 into parts 𝑃 and 𝑄 with
the following properties: the projection of 𝑃 onto the first coordinate has at most 𝑝
elements, while all the sections 𝑄𝑥 of 𝑄 (for element in 𝑄𝑥 the first coordinate equals
𝑥) have at most 𝑞 elements. (Indeed, let 𝑃 be the union of all sections that have
more than 𝑞 elements. The number of such sections do not exceed 𝑝. Remaining
elements form 𝑄.) We return to this combinatorial translation in Chapter 10.
Note that in fact we have not used the lengths of 𝑥 and 𝑦, only their complex-
ities. So we have proved the following statement:
Theorem 22 (Kolmogorov–Levin, complexity version).
𝐶(𝑥, 𝑦) = 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + 𝑂(log 𝐶(𝑥, 𝑦))
for all strings 𝑥 and 𝑦.
35 Give a more detailed analysis of the additive terms in the proof and show
that
𝐶(𝑥) + 𝐶(𝑦 | 𝑥) 6 𝐶(𝑥, 𝑦) + 3 log 𝐶(𝑥, 𝑦) + 𝑂(log log 𝐶(𝑥, 𝑦)).
36 Show that if 𝐶(𝑥, 𝑦 | 𝑘, 𝑙) < 𝑘+𝑙, then 𝐶(𝑥 | 𝑘, 𝑙) < 𝑘+𝑂(1) or 𝐶(𝑦 | 𝑥, 𝑘, 𝑙) <
𝑙 + 𝑂(1). [Hint: This is what we proved actually in the proof of Theorem 22.]
37 Show that 𝑂(log 𝑛) terms are unavoidable in Kolmogorov–Levin theorem
in both directions: for each 𝑛 there exist strings 𝑥 and 𝑦 of length at most 𝑛 such
that
𝐶(𝑥, 𝑦) > 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + log 𝑛 − 𝑂(1),
as well as strings 𝑥 and 𝑦 of length at most 𝑛 such that
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) − log 𝑛 + 𝑂(1).
[Hint: For the first inequality we can refer to the remark after Theorem 16 (p. 45).
For the second note that 𝐶(𝑥, 𝑙(𝑥)) = 𝐶(𝑥) for every 𝑥, while 𝐶(𝑥|𝑙(𝑥)) can be
equal to 𝑙(𝑥) + 𝑂(1) and 𝐶(𝑥) + 𝑂(1). Then we can take a random length between
𝑛/2 and 𝑛 and a random string of this length.]
38 Prove that changing one bit in a string of length 𝑛 changes its complexity
at most by log 𝑛 + 𝑂(log log 𝑛). Prove the same for the conditional complexity
𝐶(𝑥 | 𝑛).
As we have seen in Problem 7 (p. 34), for every 𝑛-bit string 𝑥 there exists
another string 𝑥′ of the same length that differs from 𝑥 in one position only such
that 𝐶(𝑥′) < 𝑛 − log 𝑛 + 𝑂(1) (and therefore 𝐶(𝑥′ | 𝑛) < 𝑛 − log 𝑛 + 𝑂(1)). In
particular, if 𝑥 is incompressible (given 𝑛), one can change one bit in 𝑥 and decrease
𝐶(𝑥 | 𝑛).
One can move also in the other direction: if 𝐶(𝑥 | 𝑛) is small enough (this means
that 𝐶(𝑥 | 𝑛) 6 𝛼𝑛 for some positive constant 𝛼), we can increase this complexity
by changing one bit in 𝑛: there exists some 𝛼 > 0 such that for each 𝑛-bit string
𝑥 with 𝐶(𝑥 | 𝑛) 6 𝛼𝑛 one can change one bit in 𝑥 and get another 𝑛-bit string 𝑥′
such that 𝐶(𝑥′ | 𝑛) > 𝐶(𝑥 | 𝑛). (The proof of this statement requires more involved
combinatorial argument [24] than the decrease in complexity.)
39 Fix some unconditional decompressor 𝐷. Prove that for some constant 𝑐
and for all integers 𝑛 and 𝑘 the following statement is true: if some string 𝑥 has
at least 2𝑘 descriptions of length at most 𝑛, then 𝐶(𝑥 | 𝑘) 6 𝑛 − 𝑘 + 𝑐. [Hint: Fix
some 𝑘. For each 𝑛 consider all strings 𝑥 that have at least 2𝑘 descriptions of length

---

[previous page](page-051.md) · [next page](page-053.md) · [all pages](index.md)
