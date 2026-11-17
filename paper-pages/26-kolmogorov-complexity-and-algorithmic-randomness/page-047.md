---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 47
pages: [47]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "48 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY 2.2. Conditional complexity When transmitting a file, one could try to save communication…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 47 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 47 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

48 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
### 2.2. Conditional complexity
When transmitting a file, one could try to save communication charges by
compressing it. The transmission could be made even more effective if and old
version of the same file already exists at the other side. In this case we need only
to describe the changes made. This could be considered as a kind of motivation
for the definition of conditional complexity of a given string 𝑥 relative to (known)
string 𝑦.
A conditional decompressor is a computable function 𝐷 of two arguments,
the description and the condition (both arguments and the value of 𝐷 are binary
strings). If 𝐷(𝑦, 𝑧) = 𝑥 we say that 𝑦 is a (conditional) description of 𝑥 when 𝑧 is
known (or relative to 𝑧) The complexity 𝐶𝐷 (𝑥 | 𝑧) is then defined as the length of
the shortest conditional description:
𝐶𝐷 (𝑥 | 𝑧) = min{𝑙(𝑦) | 𝐷(𝑦, 𝑧) = 𝑥}.
We say that (conditional) decompressor 𝐷1 is not worse than 𝐷2 if
𝐶𝐷1 (𝑥 | 𝑧) 6 𝐶𝐷2 (𝑥 | 𝑧) + 𝑐
for some constant 𝑐 and for all 𝑥 and 𝑧. A conditional decompressor is optimal if
it is not worse than any other conditional decompressor.
Theorem 17. There exist optimal conditional decompressors.
Proof. This “conditional” version of Kolmogorov–Solomonoff theorem can be
proved in the same way as the unconditional one (Theorem 1, p. 13).
Fix some programming language where one can write programs for computable
functions of two arguments, and let
𝐷(ˆ𝑝𝑦, 𝑧) = 𝑝(𝑦, 𝑧),
where 𝑝(𝑦, 𝑧) is the output of program 𝑝 on inputs 𝑦 and 𝑧, and ˆ𝑝 is the prefix-free
encoding of 𝑝.
It is easy to see now that if 𝐷′ is a conditional decompressor and 𝑝 is a program
for 𝐷′, then
𝐶𝐷 (𝑥 | 𝑧) 6 𝐶𝐷′ (𝑥 | 𝑧) + 𝑙(ˆ𝑝).
Theorem is proved. 
Again, we fix some optimal conditional decompressor 𝐷 and omit index 𝐷 in
the notation.
Let us start with some simple properties of conditional complexity.
Theorem 18.
𝐶(𝑥 | 𝑦) 6 𝐶(𝑥) + 𝑂(1);
𝐶(𝑥 | 𝑥) = 𝑂(1);
𝐶(𝑓 (𝑥, 𝑦) | 𝑦) 6 𝐶(𝑥 | 𝑦) + 𝑂(1);
𝐶(𝑥 | 𝑦) 6 𝐶(𝑥 | 𝑔(𝑦)) + 𝑂(1).
Here 𝑔 and 𝑓 are arbitrary computable functions (of one and two arguments,
respectively); the inequalities are valid if 𝑓 (𝑥, 𝑦) and 𝑔(𝑦) are defined.

---

[previous page](page-046.md) · [next page](page-048.md) · [all pages](index.md)
