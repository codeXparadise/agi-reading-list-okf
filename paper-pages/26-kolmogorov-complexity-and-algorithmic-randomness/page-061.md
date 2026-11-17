---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 61
pages: [61]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "62 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY inequalities for complexities that do not follow from basic inequalities were found fairly…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 61 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 61 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

62 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
inequalities for complexities that do not follow from basic inequalities were found
fairly recently (see [220, 221]) and they are rather complicated and not very intu-
itive. We discuss them in Section 10.13; we conclude this discussion by two simple
corollaries of basic inequalities.
Independent strings. We say that strings 𝑥 and 𝑦 are “independent” if
𝐼(𝑥 : 𝑦) ≈ 0. We need to specify what we mean by “≈”, but we always ignore the
terms of order 𝑂(log 𝑛) where 𝑛 is the maximal length (or complexity) of the strings
involved.
Independent strings could be considered as some counterpart of the notion of
independent random variables, which is central in the probability theory. There is
a simple observation: if a random variable 𝜉 is independent with the pair of random
variables ⟨𝛼, 𝛽⟩, then 𝜉 is independent with 𝛼 and with 𝛽 (separately).
The Kolmogorov complexity counterpart of this statement (if a string 𝑥 is
independent with a pair ⟨𝑦, 𝑧⟩, then 𝑥 is independent with 𝑦 and 𝑥 is independent
with 𝑧) can be expressed as an inequality:
𝐼(𝑥 : ⟨𝑦, 𝑧⟩) > 𝐼(𝑥 : 𝑦)
(and the similar inequality for 𝑧 instead of 𝑦). This inequality is indeed true (with
logarithmic precision), and it is easy to see if we rewrite it in terms of unconditional
complexities:
𝐶(𝑥) + 𝐶(𝑦, 𝑧) − 𝐶(𝑥, 𝑦, 𝑧) > 𝐶(𝑥) + 𝐶(𝑦) − 𝐶(𝑥, 𝑦),
which after cancellation of similar terms gives a basic inequality (Theorem 24). (In
classical probability theory one may also apply a similar inequality for Shannon
entropies.)
Complexity of pairs and triples. On the other hand, to prove the following
theorem (which we have already mentioned on p.22), it is convenient to replace
unconditional complexities by conditional ones:
Theorem 26.
2𝐶(𝑥, 𝑦, 𝑧) 6 𝐶(𝑥, 𝑦) + 𝐶(𝑥, 𝑧) + 𝐶(𝑦, 𝑧) + 𝑂(log 𝑛),
for all strings 𝑥, 𝑦, 𝑧 of complexity at most 𝑛.
Proof. Moving 𝐶(𝑥, 𝑦) and 𝐶(𝑥, 𝑧) to the left-hand side and replacing the
differences 𝐶(𝑥, 𝑦, 𝑧) − 𝐶(𝑥, 𝑦) and 𝐶(𝑥, 𝑦, 𝑧) − 𝐶(𝑥, 𝑧) by conditional complexities
𝐶(𝑧 | 𝑥, 𝑦) and 𝐶(𝑦 | 𝑥, 𝑧), we get the following inequality:
𝐶(𝑧 | 𝑥, 𝑦) + 𝐶(𝑦 | 𝑥, 𝑧) 6 𝐶(𝑦, 𝑧) + 𝑂(log 𝑛).
It remains to rewrite the right-hand side of this inequality as 𝐶(𝑦) + 𝐶(𝑧 | 𝑦), and
note that 𝐶(𝑧 | 𝑥, 𝑦) 6 𝐶(𝑧 | 𝑦) and 𝐶(𝑦 | 𝑥, 𝑧) 6 𝐶(𝑦). 
Instead we could just add two inequalities (the basic one and the inequality for
the complexity of a pair):
𝐶(𝑥, 𝑦, 𝑧) + 𝐶(𝑦) 6 𝐶(𝑥, 𝑦) + 𝐶(𝑦, 𝑧) + 𝑂(log 𝑛),
𝐶(𝑥, 𝑦, 𝑧) 6 𝐶(𝑦) + 𝐶(𝑥, 𝑧) + 𝑂(log 𝑛),
and then cancel 𝐶(𝑦) in both sides. (This proof, as well as the previous one, has
an important esthetic problem: both treat 𝑥, 𝑦, 𝑧 in a non-symmetric way while the
statement of the theorem is symmetric.)

---

[previous page](page-060.md) · [next page](page-062.md) · [all pages](index.md)
