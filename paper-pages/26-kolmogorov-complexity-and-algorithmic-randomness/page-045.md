---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 45
pages: [45]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "46 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY (bin(𝑙(𝑥)) is the binary representation of the length 𝑙(𝑥) of the string 𝑥). Now 𝑙(ˆ𝑥) = 𝑙(𝑥) +…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 45 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 45 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

46 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
(bin(𝑙(𝑥)) is the binary representation of the length 𝑙(𝑥) of the string 𝑥). Now
𝑙(ˆ𝑥) = 𝑙(𝑥) + 2 log 𝑙(𝑥) + 𝑂(1).
This trick can be “iterated”: for any prefix-free encoding 𝑥 ↦ → ˆ𝑥 we can construct
another prefix-free encoding
𝑥 ↦ →	̂	 bin(𝑙(𝑥))𝑥.
Indeed, if	̂	 bin(𝑙(𝑥))𝑥 is a prefix of	̂	 bin(𝑙(𝑦))𝑦, then one of the strings	̂	 bin(𝑙(𝑥)) and
̂	
bin(𝑙(𝑦)) is a prefix of the other one, and therefore bin(𝑙(𝑥)) = bin(𝑙(𝑦)). Therefore
𝑥 is a prefix of 𝑦, and 𝑙(𝑥) = 𝑙(𝑦), so 𝑥 = 𝑦. (In other terms, we uniquely determine
the length of the string, since a prefix-free code is used for it, and then get the
string itself knowing where it ends.)
In this way we get a prefix-free encoding such that
𝑙(ˆ𝑥) = 𝑙(𝑥) + log 𝑙(𝑥) + 2 log log 𝑙(𝑥) + 𝑂(1),
then (one more iteration)
𝑙(ˆ𝑥) = 𝑙(𝑥) + log 𝑙(𝑥) + log log 𝑙(𝑥) + 2 log log log 𝑙(𝑥) + 𝑂(1),
etc.
Now we return to the proof. Let 𝐷 be the optimal decompressor used in
the definition of Kolmogorov complexity. Consider a decompressor 𝐷′ defined as
follows:
𝐷′(ˆ𝑝𝑞) = [𝐷(𝑝), 𝐷(𝑞)],
where ˆ𝑝 is a prefix-free encoding and [·, ·] is the encoding of pairs (used in the
definition of pairs complexity). Since ˆ𝑝 is a prefix-free encoding, 𝐷′ is well defined
(we can uniquely extract ˆ𝑝 out of ˆ𝑝𝑞).
Let 𝑝 and 𝑞 be the shortest descriptions of 𝑥 and 𝑦. Then ˆ𝑝𝑞 is a description
of [𝑥, 𝑦], and its length is exactly as we need in our theorem. (The more iterations
we use for the prefix-free encoding, the better bound we get.) 
Theorem 16 implies that
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 𝐶(𝑦) + 𝑂(log 𝑛)
for strings 𝑥 and 𝑦 of length at most 𝑛: one may say that the complexity of a
pair does not exceed the sum of the complexities of its component with logarithmic
precision.
16 Suggest a natural definition for the complexity of a triple. Show that
𝐶(𝑥, 𝑦, 𝑧) 6 𝐶(𝑥) + 𝐶(𝑦) + 𝐶(𝑧) + 𝑂(log 𝑛) for every three strings 𝑥, 𝑦, 𝑧 of length
at most 𝑛.
A natural question arises: is it true that 𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 𝐶(𝑦) + 𝑂(1)?
A simple argument shows that this is not the case. Indeed, this inequality would
imply 𝐶(𝑥, 𝑦) 6 𝑙(𝑥) + 𝑙(𝑦) + 𝑂(1). Consider some 𝑁 . For each 𝑛 = 0, 1, 2, . . . , 𝑁
we have 2𝑛 strings 𝑥 of length 𝑛 and 2𝑁 −𝑛 strings 𝑦 of length 𝑁 − 𝑛. Combining
them, we (for a given 𝑛) obtain 2𝑁 different pairs ⟨𝑥, 𝑦⟩. The total number of pairs
(all 𝑛 = 0, 1, . . . , 𝑁 give different pairs) is (𝑁 + 1)2𝑁 .
Assume that indeed 𝐾(𝑥, 𝑦) 6 𝑙(𝑥) + 𝑙(𝑦) + 𝑂(1) = 𝑁 + 𝑂(1) for all these pairs.
Then we get (𝑁 + 1)2𝑁 different strings [𝑥, 𝑦] of complexity at most 𝑁 + 𝑂(1), but
this is impossible (Theorem 7, p. 31, gives the upper bound 𝑂(2𝑁 )).

---

[previous page](page-044.md) · [next page](page-046.md) · [all pages](index.md)
