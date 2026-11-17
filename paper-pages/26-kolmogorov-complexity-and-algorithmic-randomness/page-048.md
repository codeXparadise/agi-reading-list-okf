---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 48
pages: [48]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "2.2. CONDITIONAL COMPLEXITY 49 Proof. First inequality: any unconditional decompressor can be considered as a conditional one that ignores the second…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 48 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 48 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

2.2. CONDITIONAL COMPLEXITY 49
Proof. First inequality: any unconditional decompressor can be considered
as a conditional one that ignores the second argument.
Second inequality: consider 𝐷 such that 𝐷(𝑝, 𝑧) = 𝑧.
Third inequality: Let 𝐷 be the optimal conditional decompressor used to define
complexity. Consider another decompressor 𝐷′ such that
𝐷′(𝑝, 𝑦) = 𝑓 (𝐷(𝑝, 𝑦), 𝑦)
and apply the optimality property.
Similar argument works for the last inequality, but 𝐷′ should be defined in a
different way:
𝐷′(𝑝, 𝑦) = 𝐷(𝑝, 𝑔(𝑦)).
Theorem is proven. 
25 Prove that conditional complexity is “continuous as a function of its second
argument”: 𝐶(𝑥 | 𝑦0) = 𝐶(𝑥 | 𝑦) + 𝑂(1); 𝐶(𝑥 | 𝑦1) = 𝐶(𝑥 | 𝑦) + 𝑂(1). Using this
property, show that for every string 𝑥 and for every non-negative integer 𝑙 6 𝐶(𝑥)
there exists a string 𝑦 such that 𝐶(𝑥 | 𝑦) = 𝑙 + 𝑂(1).
Similar argument based on two-dimensional topology is used in [155].
26 Prove that for any fixed 𝑦 the function 𝑥 ↦ → 𝐶(𝑥 | 𝑦) differs from 𝐶 at most
by 2𝐶(𝑦) + 𝑂(1).
27 Prove that 𝐶([𝑥, 𝑧] | [𝑦, 𝑧]) 6 𝐶(𝑥 | 𝑦) + 𝑂(1) for any strings 𝑥, 𝑦, 𝑧 (here
[·, ·] stands for the computable encoding of pairs).
28 Fix some “reasonable” programming language. (Formally, we require the
corresponding universal function to be a G¨odel one; this means that translation
algorithm exists for any other programming language, see, e.g., [182].) Show that
conditional complexity 𝐶(𝑥 | 𝑦) is equal (up to 𝑂(1) additive term) to the minimal
complexity of a program that produces output 𝑥 on input 𝑦. [Hint: Let 𝐷 be an
optimal conditional decompressor. If we fix its first argument 𝑝, we get a program
of complexity at most 𝑙(𝑝) + 𝑂(1). On the other hand, if program 𝑝 maps 𝑦 to 𝑥,
then 𝐶(𝑥 | 𝑦) = 𝐶(𝑝(𝑦) | 𝑦) 6 𝐶(𝑝) + 𝑂(1).]
This interpretation of conditional complexity as a minimal complexity of a
program with some property will be considered in Chapter 13.
If we restrict ourselves to total programs (that terminate on all inputs), we
get an essentially different notion of conditional complexity that can be called total
conditional complexity.
29 Show that the notion of total conditional complexity CT(𝑥 | 𝑦), the minimal
(plain) complexity of a total program that maps 𝑦 to 𝑥, is well defined (i.e., changes
at most by 𝑂(1) when we change the programming language in a reasonable way).
Prove that
𝐶(𝑥 | 𝑦) 6 CT(𝑥 | 𝑦) 6 𝐶(𝑥)
with 𝑂(1)-precision.
30 Show that the total complexity sometimes exceeds significantly the usual
conditional complexity: for every 𝑛 there exist two 𝑛-bit strings 𝑥 and 𝑦 such that
𝐶(𝑥 | 𝑦) = 𝑂(1) while CT(𝑥 | 𝑦) > 𝑛.
[Hint: Let us enumerate all programs of complexity less than 𝑛 defined on all 𝑛-bit
strings, and maintain two 𝑛-bit strings 𝑥 and 𝑦 with the following property: none of
the programs found maps 𝑦 to 𝑥. When a new program is found that maps 𝑦 to 𝑥,

---

[previous page](page-047.md) · [next page](page-049.md) · [all pages](index.md)
