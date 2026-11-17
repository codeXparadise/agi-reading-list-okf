---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 44
pages: [44]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "CHAPTER 2 Complexity of pairs and conditional complexity 2.1. Complexity of pairs As we have discussed, we can define complexity of any constructive…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 44 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 44 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

CHAPTER 2
Complexity of pairs and conditional complexity
### 2.1. Complexity of pairs
As we have discussed, we can define complexity of any constructive object using
(computable) encodings by strings. In this section we deal with pairs of strings.
A pair 𝑥, 𝑦 can be encoded, e.g., by a string [𝑥, 𝑦] = 𝑥01𝑦; here 𝑥 stands for 𝑥
with doubled bits. Any other computable encoding 𝑥, 𝑦 ↦ → [𝑥, 𝑦] could be used (of
course, we need that [𝑥, 𝑦]̸ = [𝑥′, 𝑦′] if 𝑥̸ = 𝑥′ or 𝑦̸ = 𝑦′). Any two encodings of
this type are equivalent (there are translation algorithms in both directions), so
Theorem 3 (p. 15) guarantees that complexities of the different encodings of the
same pair differ by 𝑂(1).
So let us fix some encoding [𝑥, 𝑦]. Kolmogorov complexity of a pair 𝑥, 𝑦 is
defined as 𝐶([𝑥, 𝑦]) and denoted by 𝐶(𝑥, 𝑦). Here are some evident properties:
∙ 𝐶(𝑥, 𝑥) = 𝐶(𝑥) + 𝑂(1);
∙ 𝐶(𝑥, 𝑦) = 𝐶(𝑦, 𝑥) + 𝑂(1);
∙ 𝐶(𝑥) 6 𝐶(𝑥, 𝑦) + 𝑂(1); 𝐶(𝑦) 6 𝐶(𝑥, 𝑦) + 𝑂(1).
The following theorem gives an upper bound for the complexity of a pair in
terms of complexities of its components:
Theorem 16.
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 2 log 𝐶(𝑥) + 𝐶(𝑦) + 𝑂(1);
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + log 𝐶(𝑥) + 2 log log 𝐶(𝑥) + 𝐶(𝑦) + 𝑂(1);
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + log 𝐶(𝑥) + log log 𝐶(𝑥) + 2 log log log 𝐶(𝑥) + 𝐶(𝑦) + 𝑂(1);
. . .
(We can continue this sequence of inequalities indefinitely. Also, one can ex-
change 𝑥 and 𝑦.)
Proof. This proof (for the first inequality) was already explained in the In-
troduction (Theorem 4, p. 16). The only difference is that we considered the con-
catenation 𝑥𝑦 instead of a pair. Let us repeat the argument for pairs.
A computable mapping 𝑥 ↦ → ˆ𝑥 (here 𝑥 and ˆ𝑥 are binary strings) is called a
prefix-free encoding, if for any two different strings 𝑥 and 𝑦 the string ˆ𝑥 is not a
prefix of the string ˆ𝑦. (In particular, ˆ𝑥̸ = ˆ𝑦 if 𝑥̸ = 𝑦.) This guarantees that both 𝑢
and 𝑣 can be uniquely reconstructed from ˆ𝑢𝑣.
An example of a prefix-free encoding: 𝑥 ↦ → 𝑥01, where 𝑥 stands for 𝑥 with
doubled bits. Here the block 01 are used as a delimiter. However, this encoding is
not the most space-efficient one, since it doubles the length. A better prefix-free
encoding:
𝑥 ↦ → ˆ𝑥 = bin(𝑙(𝑥)) 01𝑥
45

---

[previous page](page-043.md) · [next page](page-045.md) · [all pages](index.md)
