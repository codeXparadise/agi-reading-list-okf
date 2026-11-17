---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 63
pages: [63]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "64 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY 𝑥 𝑦 𝑧 𝐶(𝑥 | 𝑦, 𝑧) 𝐼(𝑥 : 𝑦 | 𝑧) 𝐶(𝑦 | 𝑥, 𝑧) 𝐼(𝑥 : 𝑧 | 𝑦) 𝐼(𝑥 : 𝑦 : 𝑧) 𝐼(𝑦 : 𝑧 | 𝑥) 𝐶(𝑧 | 𝑥, 𝑦)…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 63 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 63 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

64 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
𝑥 𝑦
𝑧
𝐶(𝑥 | 𝑦, 𝑧)
𝐼(𝑥 : 𝑦 | 𝑧) 𝐶(𝑦 | 𝑥, 𝑧)
𝐼(𝑥 : 𝑧 | 𝑦)
𝐼(𝑥 : 𝑦 : 𝑧)
𝐼(𝑦 : 𝑧 | 𝑥)
𝐶(𝑧 | 𝑥, 𝑦)
Figure 5. The complexity interpretation of new coordinates.
notation 𝐼(𝑥 : 𝑦 : 𝑧) is used. However, the meaning of this expression is not quite
clear, especially if we take into accout that 𝑎5 can be negative.
Consider the following example where 𝑎5 < 0. Let 𝑥 and 𝑦 be two halves of
an incompressible strings of length 2𝑛. Then 𝐶(𝑥) = 𝑛, 𝐶(𝑦) = 𝑛, 𝐶(𝑥, 𝑦) = 2𝑛
and 𝐼(𝑥 : 𝑦) = 0 (up to 𝑂(log 𝑛)). Consider a string 𝑧 of length 𝑛 which is a bitwise
sum modulo 2 of 𝑥 and 𝑦 (XOR-operation). Then each of the strings 𝑥, 𝑦, 𝑧 can
be reconstructed if two others are known; therefore the complexities of all pairs
𝐶(𝑥, 𝑦), 𝐶(𝑦, 𝑧), 𝐶(𝑥, 𝑧) are equal to 2𝑛 (again up to 𝑂(log 𝑛)), and the complexity
𝐶(𝑥, 𝑦, 𝑧) is also 2𝑛. The complexity of 𝑧 is equal to 𝑛 (it can not be larger, since
the length is 𝑛; on the other hand, it cannot be smaller, since 𝑧 and 𝑦 form a pair
of complexity 2𝑛).
So we get the following values of 𝑎1, . . . , 𝑎7 for this example (Fig. 6):
0 𝑛 0
𝑛 −𝑛 𝑛
0
Figure 6. Two independent incompressible strings of length 𝑛
and their XOR.
Note that even if 𝑎5 is negative, the sums 𝑎5 + 𝑎2, 𝑎5 + 𝑎4 and 𝑎5 + 𝑎6, being
mutual informations for pairs, are non-negative. (In our examples these sums are
equal to 0.)
This example corresponds to the simple case of secret sharing of secret 𝑧 be-
tween two people: if one of them knows 𝑥 and the other one knows 𝑦, then none of

---

[previous page](page-062.md) · [next page](page-064.md) · [all pages](index.md)
