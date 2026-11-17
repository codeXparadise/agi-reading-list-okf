---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 29
pages: [29]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "30 1. PLAIN KOLMOGOROV COMPLEXITY As the optimal description mode is not worse than the identity function 𝑥 ↦ → 𝑥, we obtain the inequality 𝐶(𝑥) 6…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 29 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 29 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

30 1. PLAIN KOLMOGOROV COMPLEXITY
As the optimal description mode is not worse than the identity function 𝑥 ↦ → 𝑥,
we obtain the inequality 𝐶(𝑥) 6 𝑙(𝑥) + 𝑂(1) (Theorem 2, p. 15).
Let 𝐴 be a partial computable function. Comparing the optimal description
mode 𝐷 with the description mode 𝑦 ↦ → 𝐴(𝐷(𝑦)), we conclude that
𝐶(𝐴(𝑥)) 6 𝐶(𝑥) + 𝑂(1),
showing the non-growth of complexity under algorithmic transformations (Theo-
rem 3, p. 15).
Using this inequality, we can define Kolmogorov complexity of other “finite
objects” like natural numbers, graphs, permutations, finite sets of strings, etc.,
that can be naturally encoded by binary strings.
For example, let us define the complexity of natural numbers. A natural num-
ber 𝑛 can be written in binary notation. Another way to represent a number by a
string is as follows. Enumerate all the binary strings in the lexicographical order
Λ, 0, 1, 00, 01, 10, 11, 000, 001, 010, 011, 100, . . .
using the natural numbers 0, 1, 2, 3, . . . as indexes. This enumeration is more con-
venient compared to binary representation, as it is a bijection. Every string can be
considered as an encoding of its index in this enumeration. Finally, one can also
encode a natural number 𝑛 by a string consisting of 𝑛 ones.
Using either of these three encodings we can define the complexity of 𝑛 as
the complexity of the string encoding 𝑛. Three resulting complexities of 𝑛 differ
at most by an additive constant. Indeed, for every pair of these encodings there
is an algorithm translating the first encoding into the second one. Applying this
algorithm, we increase the complexity at most by a constant. Note that anyway
the Kolmogorov complexity of binary strings is defined up to an additive constant,
so the choice of a computable encoding does not matter.
As the length of the binary representation of a natural number 𝑛 is equal to
log 𝑛 + 𝑂(1), the Kolmogorov complexity of 𝑛 is at most log 𝑛 + 𝑂(1). (By log we
denote binary logarithms.)
Here is another application of the non-growth of complexity under algorithmic
transformations. Let us show that deleting the last bit of a string changes its
complexity at most by a constant. Indeed, all three functions 𝑥 ↦ → 𝑥0, 𝑥 ↦ → 𝑥1,
𝑥 ↦ → (𝑥 without the last bit) are computable.
The same is true for the first bit. However this does not apply to every bit of
the string. To show this, consider the string 𝑥 consisting of 2𝑛 zeros, its complexity
is at most 𝐶(𝑛) + 𝑂(1) 6 log 𝑛 + 𝑂(1). (By log we always mean binary logarithm.)
There are 2𝑛 different strings obtained from 𝑥 by flipping one bit. At least one of
them has complexity 𝑛 or more. (Recall that the number of strings of complexity
less than 𝑛 does not exceed the number of descriptions of length less than 𝑛, which
is less than 2𝑛, Theorem 5, p. 18.)
Incrementing a natural number 𝑛 by 1 changes 𝐶(𝑛) at most by a constant.
This implies that 𝐶(𝑛) satisfies “Lipschitz property”: for some 𝑐 and for all 𝑚, 𝑛
we have |𝐶(𝑚) − 𝐶(𝑛)| 6 𝑐|𝑚 − 𝑛|.
1 Prove a stronger inequality: |𝐶(𝑚) − 𝐶(𝑛)| 6 |𝑚 − 𝑛| + 𝑐 for some 𝑐 and for
all 𝑚, 𝑛 ∈ N, and, moreover, |𝐶(𝑚) − 𝐶(𝑛)| 6 2 log |𝑚 − 𝑛| + 𝑐 (the latter inequality
assumes that 𝑚̸ = 𝑛).

---

[previous page](page-028.md) · [next page](page-030.md) · [all pages](index.md)
