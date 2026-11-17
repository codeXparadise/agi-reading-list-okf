---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 36
pages: [36]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "1.2. ALGORITHMIC PROPERTIES 37 𝑚 𝐶(𝑚) 𝑛 − 1 𝐵(𝑛 − 1) 𝑛 𝐵(𝑛) = 𝐵(𝑛 + 1) 𝑛 + 1 Figure 1. The definition of B (𝑛): the value 𝐶(𝑚) does not exceed 𝑛−1…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 36 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 36 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

1.2. ALGORITHMIC PROPERTIES 37
𝑚
𝐶(𝑚)
𝑛 − 1
𝐵(𝑛 − 1)
𝑛
𝐵(𝑛) = 𝐵(𝑛 + 1)
𝑛 + 1
Figure 1. The definition of B (𝑛): the value 𝐶(𝑚) does not exceed
𝑛−1 for 𝑚 = B (𝑛−1) (the case when 𝐶(B (𝑛−1)) = 𝑛−1 is shown),
and 𝐶(𝑚) > 𝑛 for all 𝑚 > B (𝑛 − 1). At the point 𝑚 = B (𝑛)
the value of 𝐶 does not exceed 𝑛 (the case when 𝐶(B (𝑛)) = 𝑛
is shown), and 𝐶(𝑚) > 𝑛 for all 𝑚 > B (𝑛). The case when
𝐶(𝑚) is even greater than 𝑛 + 1 for all 𝑚 > B (𝑛) is shown, thus
B (𝑛 + 1) = B (𝑛). For 𝑚 ∈ (B (𝑛 − 1), B (𝑛)] the value of the
function 𝐶>(𝑚) is equal to 𝑛.
corresponds to the fast increase of B . The latter can be illustrated by the following
result.
Theorem 11. Let 𝑓 be a computable function from N to N. Then B (𝑛) > 𝑓 (𝑛)
for all but finitely many 𝑛.
Note that 𝑓 may be a partial function. In this case we claim that B (𝑛) > 𝑓 (𝑛)
for all sufficiently large 𝑛 that are in the domain of 𝑓 .
Proof. As algorithmic transformations do not increase complexity, for some
constant 𝑐 for all 𝑛 we have
𝐶(𝑓 (𝑛)) 6 𝐶(𝑛) + 𝑂(1) 6 log 𝑛 + 𝑐.
On the other hand, the definition of B and the inequality 𝑓 (𝑛) > B (𝑛) imply
𝐶(𝑓 (𝑛)) > 𝑛. Thus
𝑛 < 𝐶(𝑓 (𝑛)) 6 log 𝑛 + 𝑐
whenever 𝑓 (𝑛) > B (𝑛). This can happen only for finitely many 𝑛. 
Let us reformulate the definition of B (𝑛) as follows. Let 𝐷 be the optimal
description mode used in the definition of Kolmogorov complexity. Then B (𝑛) is
the maximal value of 𝐷 on strings of length at most 𝑛:
B (𝑛) = max{𝐷(𝑥) | 𝑙(𝑥) 6 𝑛}.
Recall that we identify natural numbers and binary strings and consider the values
of 𝐷 as natural numbers. The minimum of the empty set is defined as −1.
Consider now any partial computable function 𝑑 : Ξ → N in place of 𝐷 and let
B 𝑑(𝑛) = max{𝑑(𝑥) | 𝑙(𝑥) 6 𝑛 and 𝑑(𝑥) is defined}.
Next theorem shows that the function B is the largest function among all functions
B 𝑑, in the following sense:

---

[previous page](page-035.md) · [next page](page-037.md) · [all pages](index.md)
