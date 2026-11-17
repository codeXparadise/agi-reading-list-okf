---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 51
pages: [51]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "52 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY 𝑡 𝐴𝑡 𝐴 𝑥 𝑦 Figure 1. The section 𝐴𝑡 of the set 𝐴 of all simple pairs. (Fig. 1). The sum of the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 51 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 51 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

52 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
𝑡
𝐴𝑡
𝐴
𝑥
𝑦
Figure 1. The section 𝐴𝑡 of the set 𝐴 of all simple pairs.
(Fig. 1). The sum of the cardinalities of all 𝐴𝑡 (over all strings 𝑡) is the cardinality
of 𝐴 and does not exceed 𝑂(2𝑎). Therefore there are few “large” sections 𝐴𝑡, and
this is the basic argument we need for the proof.
Let 𝑚 be equal to ⌊log2 |𝐴𝑥|⌋ where 𝑥 is the first component of the pair ⟨𝑥, 𝑦⟩
we started with. In other terms, assume that cardinality of 𝐴𝑥 is between 2𝑚 and
2𝑚+1. Let us prove that
(1) 𝐶(𝑦 | 𝑥) does not exceed 𝑚 significantly;
(2) 𝐶(𝑥) does not exceed 𝑎 − 𝑚 significantly.
We start with (1). Knowing 𝑎, we can enumerate the set 𝐴. If we know also 𝑥,
we can select only pairs whose first component equals 𝑥. In this way we get an
enumeration of 𝐴𝑥. To specify 𝑦, it is enough to tell the ordinal number of 𝑦 in
this enumeration (of 𝐴𝑥). This ordinal number takes 𝑚 + 𝑂(1) bits, and together
with 𝑎 we get 𝑚 + 𝑂(log 𝑛) bits for the conditional description of 𝑦 given 𝑥. Note
that 𝑎 = 𝐶(𝑥, 𝑦) does not exceed 𝑂(𝑛) for strings 𝑥 and 𝑦 of length 𝑛. Therefore,
we need only 𝑂(log 𝑛) to specify 𝑎 and 𝑛, and
𝐶(𝑦 | 𝑥) 6 𝑚 + 𝑂(log 𝑛).
Now let us prove (2). Consider the set 𝐵 of all strings 𝑡 such that cardinality
of 𝐴𝑡 is at least 2𝑚. The cardinality of 𝐵 does not exceed 2𝑎+1/2𝑚, otherwise the
sum |𝐴| =∑︀ |𝐴𝑡| would be greater than 2𝑎+1. We can enumerate 𝐵 if we know 𝑎
and 𝑚. Indeed, we should enumerate 𝐴 and group together the pairs with the same
first coordinate; if we find 2𝑚 pairs with the same value of the first coordinate, we
put this value into 𝐵. Therefore the string 𝑥 (as well as every element of 𝐵) can be
specified by (𝑎 − 𝑚) + 𝑂(log 𝑛) bits: 𝑎 − 𝑚 + 1 bits are needed for ordinal number
of 𝑥 in the enumeration of 𝐵, and 𝑂(log 𝑛) are used to specify 𝑎 and 𝑚. So we get
𝐶(𝑥) 6 (𝑎 − 𝑚) + 𝑂(log 𝑛),
and it remains to add this inequality and the preceding one. 
This theorem can be considered as the complexity counterpart of the following
combinatorial statement. Let 𝐴 be a finite set of pairs. Its cardinality is (obviously)
bounded by the product of the cardinality of 𝐴’s projection onto the first coordinate,
and the maximal cardinality of the sections 𝐴𝑥. This corresponds to the inequality
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + 𝑂(log 𝑛). The reverse inequality needs a more subtle
interpretation. Let 𝐴 be a set of pairs and let 𝑝 and 𝑞 be some numbers such that

---

[previous page](page-050.md) · [next page](page-052.md) · [all pages](index.md)
