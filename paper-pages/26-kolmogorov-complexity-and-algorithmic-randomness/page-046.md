---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 46
pages: [46]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "2.1. COMPLEXITY OF PAIRS 47 17 Prove that there is no constant 𝑐 such that 𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + log 𝐶(𝑥) + 𝐶(𝑦) + 𝑐 for all 𝑥 and 𝑦. [Hint: Replace 𝐶 in…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 46 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 46 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

2.1. COMPLEXITY OF PAIRS 47
17 Prove that there is no constant 𝑐 such that
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + log 𝐶(𝑥) + 𝐶(𝑦) + 𝑐
for all 𝑥 and 𝑦. [Hint: Replace 𝐶 in the right hand side by 𝑙 and count the number
of corresponding pairs.]
18 (a) Prove that∑︁
𝑥∈Ξ
2−𝑙(^𝑥) 6 1
for any prefix-free encoding 𝑥 ↦ → ˆ𝑥 (here Ξ is the set of all binary strings).
(b) Prove that if a prefix-free encoding increases the length of a 𝑛-bit string at
most by 𝑓 (𝑛), i.e., if 𝑙(ˆ𝑥) 6 𝑙(𝑥) + 𝑓 (𝑙(𝑥)), then∑︀ 𝑛 2−𝑓 (𝑛) < ∞.
This problem explains why a coefficient 2 appears in the Theorem 16 (p. 45):
the series∑︁ 1
𝑛2 ,∑︁ 1
𝑛(log 𝑛)2 ,∑︁ 1
𝑛 log 𝑛(log log 𝑛)2 , . . .
converge, while the series∑︁	
1
𝑛 ,∑︁ 1
𝑛 log 𝑛 ,∑︁ 1
𝑛 log 𝑛 log log 𝑛 , . . .
diverge.
The following problem describes functions that can be used for bounds similar
to Theorem 16.
19 Let 𝑓 : N → N is a non-decreasing total computable function. Prove that
the following three properties are equivalent:
(a) 𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 𝐶(𝑦) + 𝑓 (𝐶(𝑥)) + 𝑂(1);
(b) 𝐶(𝑥, 𝑦) 6 𝑙(𝑥) + 𝑙(𝑦) + 𝑓 (𝑙(𝑥)) + 𝑂(1);
(c)∑︀ 𝑛 2−𝑓 (𝑛) < ∞. [Hint: (a) obviously implies (b); to get the reverse implica-
tion, consider the shortest descriptions. To derive (a) from (c), one can count pairs
with 𝑙(𝑥) + 𝑓 (𝑙(𝑥)) + 𝑙(𝑦) < 𝑛; one can also use results about prefix complexity (see
Chapter 4, Problem 107). Finally, to derive (c) from (b), note that the right hand
side in (b) is at most 𝑛 + 𝑂(1) if 𝑙(𝑥) = 𝑘 and 𝑙(𝑦) = 𝑛 − 𝑘 − 𝑓 (𝑘), for 𝑘 + 𝑓 (𝑘) 6 𝑛.
So the number of such pairs is at least∑︀ 2𝑘2𝑛−𝑘−𝑓 (𝑘) = 2𝑛∑︀ 𝑘 2−𝑓 (𝑘) where the
sum is taken over all 𝑘 such that 𝑘 + 𝑓 (𝑘) 6 𝑛. ]
20 Prove that all the inequalities of Theorem 16 become false if the coefficient
2 is replaced by 1, but remain true with the coefficient 1 + 𝜀 for any 𝜀 > 0. [Hint:
see the preceding problem.]
21 Prove that
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + log 𝐶(𝑥) + 𝐶(𝑦) + log 𝐶(𝑦) + 𝑂(1).
22 (Continued) Prove a stronger inequality:
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 𝐶(𝑦) + log(𝐶(𝑥) + 𝐶(𝑦)) + 𝑂(1).
(note that 𝐶(𝑥) + 𝐶(𝑦) can be replaced by max(𝐶(𝑥), 𝐶(𝑦)), this gives a factor at
most 2, which makes 𝑂(1) after taking logarithms).
23 Prove that 𝐶(𝑥, 𝐶(𝑥)) = 𝐶(𝑥) + 𝑂(1). [Hint: 𝐶(𝑥, 𝐶(𝑥)) > 𝐶(𝑥) + 𝑂(1)
for evident reasons; on the other hand, the shortest description of 𝑥 determines
both 𝑥 and 𝐶(𝑥).]
24 Prove that if 𝐶(𝑥) 6 𝑛 and 𝐶(𝑦) 6 𝑛, then 𝐶(𝑥, 𝑦) 6 2𝑛 + 𝑂(1).

---

[previous page](page-045.md) · [next page](page-047.md) · [all pages](index.md)
