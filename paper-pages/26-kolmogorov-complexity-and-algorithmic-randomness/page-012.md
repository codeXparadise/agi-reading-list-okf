---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 12
pages: [12]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "OPTIMAL DESCRIPTION MODES 13 them. Indeed, let 𝐷(0𝑦) = 𝐷1(𝑦), 𝐷(1𝑦) = 𝐷2(𝑦). In other words, we consider the first bit of a description as the index…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 12 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 12 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

OPTIMAL DESCRIPTION MODES 13
them. Indeed, let
𝐷(0𝑦) = 𝐷1(𝑦),
𝐷(1𝑦) = 𝐷2(𝑦).
In other words, we consider the first bit of a description as the index of a description
mode and the rest as the description (for this mode).
If 𝑦 is a description of 𝑥 with respect to 𝐷1 (or 𝐷2), then 0𝑦 (respectively, 1𝑦)
is a description of 𝑥 with respect to 𝐷 as well. This description is only one bit
longer, therefore we have
𝐶𝐷 (𝑥) 6 𝐶𝐷1 (𝑥) + 1,
𝐶𝐷 (𝑥) 6 𝐶𝐷2 (𝑥) + 1
for all 𝑥. Thus the mode 𝐷 is not worse than both 𝐷1 and 𝐷2.
This idea is often used in practice. For instance, a zip-archive has a preamble;
the preamble says (among other things) which mode was used to compress this
particular file, and the compressed file follows the preamble.
If we want to use 𝑁 different compression modes, we need to reserve initial
log2 𝑁 bits for the index of the compression mode.
Using a generalization of this idea, we can prove the following theorem:
Theorem 1 (Solomonoff–Kolmogorov). There is a description mode 𝐷 that is
not worse than any other one: for every description mode 𝐷′ there is a constant 𝑐
such that
𝐶𝐷 (𝑥) 6 𝐶𝐷′ (𝑥) + 𝑐
for every string 𝑥.
A description mode 𝐷 having this property is called optimal.
Proof. Recall that a description mode by definition is a computable function.
Every computable function has a program. We assume that programs are binary
strings. Moreover, we assume that reading the program bits from left to right we
can determine uniquely where it ends, that is, programs are “self-delimiting”. Note
that every programming language can be modified in such a way that programs are
self-delimiting. For instance, we can double every bit of a given program (changing
0 to 00 and 1 to 11) and append the pattern 01 to its end.
Define now a new description mode 𝐷 as follows:
𝐷(𝑃 𝑦) = 𝑃 (𝑦)
where 𝑃 is a program (in the chosen self-delimiting programming language) and
𝑦 is any binary string. That is, the algorithm 𝐷 scans the input string from the
left to the right and extracts a program 𝑃 from the input. (If the input does not
start with a valid program, 𝐷 does whatever it wants, say, goes into an infinite
loop. The self-delimiting property guarantees that the decomposition of input is
unique: if 𝑃 𝑦 = 𝑃 ′𝑦′ for two programs 𝑃 and 𝑃 ′, then one of the programs is a
prefix of the other one.) Then 𝐷 applies the extracted program 𝑃 to the rest of the
input (𝑦) and returns the obtained result. (So 𝐷 is just an “universal algorithm”,
or “interpreter”; the only difference is that program and input are not separated
and therefore we need to use a self-delimiting programming language.)
Let us show that indeed 𝐷 is not worse than any other description mode 𝑃 . We
assume that the program 𝑃 is written in the chosen self-delimiting programming

---

[previous page](page-006.md) · [next page](page-013.md) · [all pages](index.md)
