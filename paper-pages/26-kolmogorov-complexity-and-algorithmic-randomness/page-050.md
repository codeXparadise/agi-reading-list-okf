---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 50
pages: [50]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "2.2. CONDITIONAL COMPLEXITY 51 Theorem 20. 𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 2 log 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + 𝑂(1) Proof. Let 𝐷1 be an optimal unconditional decompressor and…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 50 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 50 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

2.2. CONDITIONAL COMPLEXITY 51
Theorem 20.
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 2 log 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + 𝑂(1)
Proof. Let 𝐷1 be an optimal unconditional decompressor and let 𝐷2 be an
optimal conditional decompressor. Construct a new unconditional decompressor
𝐷′ as follows:
𝐷′(ˆ𝑝𝑞) = [𝐷1(𝑝), 𝐷2(𝑞, 𝐷1(𝑝))].
Here ˆ𝑝 stands for the prefix-free encoding of 𝑝, and [·, ·] is a computable encoding
of pairs used in the definition of the complexity of pairs. Let 𝑝 be the shortest 𝐷1-
description of 𝑥 and 𝑞 be the shortest 𝐷2-description of 𝑦 conditional to 𝑥. Then
the string ˆ𝑝𝑞 is a 𝐷3-description of [𝑥, 𝑦]. Therefore,
𝐶(𝑥, 𝑦) 6 𝐶𝐷′ (𝑥, 𝑦) + 𝑂(1) 6 𝑙(ˆ𝑝) + 𝑙(𝑞) + 𝑂(1).
As we have seen, one can choose a prefix-free encoding in such a way that 𝑙(ˆ𝑝) is
bounded by 𝑙(𝑝) + 2 log 𝑙(𝑝) + 𝑂(1) (see the proof of Theorem 16, p. 45), and we
get a desired inequality. 
As before, we may replace 2 log 𝐶(𝑥) by log 𝐶(𝑥) + 2 log log 𝐶(𝑥) etc., getting a
better bound. We also can use conditional complexity in the logarithmic term and
write
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + 2 log 𝐶(𝑦 | 𝑥) + 𝑂(1).
(In the proof we should then replace 𝐷′(ˆ𝑝𝑞) by 𝐷′(ˆ𝑞𝑝).)
34 Prove that
𝐶(𝑥 | 𝑧) 6 𝐶(𝑥 | 𝑦) + 2 log 𝐶(𝑥 | 𝑦) + 𝐶(𝑦 | 𝑧) + 𝑂(1)
for all 𝑥, 𝑦, 𝑧 (a sort of a “triangle inequality”).
If we are not interested in the exact form of the additional logarithmic term,
the statement of Theorem 20 can be reformulated as follows:
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + 𝑂(log 𝑛).
for all strings 𝑥, 𝑦 of length at most 𝑛.
It turns out (and this is the first nontrivial statement in this chapter, and
probably the first non-trivial result about Kolmogorov complexity; it was proven
independently by Kolmogorov and Levin and published in [78, 223]) that this
inequality is in fact an equality.
Theorem 21 (Kolmogorov–Levin).
𝐶(𝑥, 𝑦) = 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + 𝑂(log 𝑛).
for all strings 𝑥, 𝑦 of length at most 𝑛.
Proof. Since we already have one inequality, we need to prove only that
𝐶(𝑥, 𝑦) > 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + 𝑂(log 𝑛)
for all 𝑥 and 𝑦 of length at most 𝑛.
Let 𝑥 and 𝑦 be some strings of length at most 𝑛. Let 𝑎 be the complexity
𝐶(𝑥, 𝑦) of the pair ⟨𝑥, 𝑦⟩. Consider the set 𝐴 of all pairs whose complexity does not
exceed 𝑎. Then 𝐴 is a set of cardinality 𝑂(2𝑎) (in fact, at most 2𝑎+1) and ⟨𝑥, 𝑦⟩ is
one of its elements.
For each string 𝑡 consider the “vertical section” 𝐴𝑡 of 𝐴:
𝐴𝑡 = {𝑢 | ⟨𝑡, 𝑢⟩ ∈ 𝐴}

---

[previous page](page-049.md) · [next page](page-051.md) · [all pages](index.md)
