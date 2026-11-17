---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 58
pages: [58]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "2.3. COMPLEXITY AS THE AMOUNT OF INFORMATION 59 These properties of information can be described as “conservation laws” for information (about…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 58 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 58 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

2.3. COMPLEXITY AS THE AMOUNT OF INFORMATION 59
These properties of information can be described as “conservation laws” for
information (about something) in algorithmic or random processes. As Leonid
Levin once put it: “by torturing an uninformed person you do not get any evidence
about the crime”. He discusses this property (for different notion of information)
in [99].
Recall that
𝐶(𝑥, 𝑦) = 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + 𝑂(log 𝐶(𝑥, 𝑦)),
(Theorem 22, p. 53). This allows us to express conditional complexity in terms of
unconditional one: 𝐶(𝑦 | 𝑥) = 𝐶(𝑥, 𝑦) − 𝐶(𝑥) + 𝑂(log 𝐶(𝑥, 𝑦)). Then we get the
following expression for the information:
𝐼(𝑥 : 𝑦) = 𝐶(𝑦) − 𝐶(𝑦 | 𝑥) = 𝐶(𝑥) + 𝐶(𝑦) − 𝐶(𝑥, 𝑦) + 𝑂(log 𝐶(𝑥, 𝑦)).
This expression immediately implies the following theorem:
Theorem 23 (information symmetry).
𝐼(𝑥 : 𝑦) = 𝐼(𝑦 : 𝑥) + 𝑂(log 𝐶(𝑥, 𝑦))
So the difference between 𝐼(𝑥 : 𝑦) and 𝐼(𝑦 : 𝑥) is logarithmically small compared
to 𝐶(𝑥, 𝑦). The following problem shows that at the same time this difference could
be comparable with the values 𝐼(𝑥 : 𝑦) and 𝐼(𝑦 : 𝑥) if they are much less than 𝐶(𝑥, 𝑦).
60 Let 𝑥 be a string of length 𝑛 such that 𝐶(𝑥 | 𝑛) > 𝑛. Show that
𝐼(𝑥 : 𝑛) = 𝐶(𝑛) + 𝑂(1) and 𝐼(𝑛 : 𝑥) = 𝑂(1).
The property of information symmetry (up to a logarithmic term) explains
why 𝐼(𝑥 : 𝑦) (or 𝐼(𝑦 : 𝑥)) is sometimes called mutual information in two strings 𝑥
and 𝑦. The connection between mutual information, conditional and unconditional
complexities and pair complexity can be illustrated by a (rather symbolic) picture
(Fig. 2).
𝐶(𝑥 | 𝑦) 𝐶(𝑦 | 𝑥)
𝐼(𝑥 : 𝑦)
𝑥 𝑦
Figure 2. Mutual information and conditional complexity
It shows that strings 𝑥 and 𝑦 have 𝐼(𝑥 : 𝑦) ≈ 𝐼(𝑦 : 𝑥) bits of mutual information.
Adding 𝐶(𝑥 | 𝑦) bits (information that is present in 𝑥 but not in 𝑦, the left part),
we obtain
𝐼(𝑦 : 𝑥) + 𝐶(𝑥 | 𝑦) ≈ (𝐶(𝑥) − 𝐶(𝑥 | 𝑦)) + 𝐶(𝑥 | 𝑦) = 𝐶(𝑥)
bits (matching the complexity of 𝑥). Similarly, the central part together with
𝐶(𝑦 | 𝑥) (the right part) give 𝐶(𝑦). Finally, all three parts together give us
𝐶(𝑥 | 𝑦) + 𝐼(𝑥 : 𝑦) + 𝐶(𝑦 | 𝑥) = 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) = 𝐶(𝑥 | 𝑦) + 𝐶(𝑦) = 𝐶(𝑥, 𝑦)
bits (all equalities are true up to 𝑂(log 𝑛) for strings 𝑥 and 𝑦 of length at most 𝑛).
In some cases this picture can be understood quite literally. Consider, for
instance, an incompressible string 𝑟 = 𝑟1 . . . 𝑟𝑛 of length 𝑛, so 𝐶(𝑟1 . . . 𝑟𝑛) > 𝑛.

---

[previous page](page-057.md) · [next page](page-059.md) · [all pages](index.md)
