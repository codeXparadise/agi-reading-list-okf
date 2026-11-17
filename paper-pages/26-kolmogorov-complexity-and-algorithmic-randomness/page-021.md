---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 21
pages: [21]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "22 WHAT IS THIS BOOK ABOUT? (he called it in German “Kollektiv”) as a basis for probability theory (at that time the measure theory approach was not…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 21 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 21 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

22 WHAT IS THIS BOOK ABOUT?
(he called it in German “Kollektiv”) as a basis for probability theory (at that time
the measure theory approach was not developed yet). He considered the so-called
“frequency stability” as a main property of random sequences. We will consider
von Mises’ approach to the definition of a random sequence (and the subsequent
developments) in Chapter 9.
Lower bounds for computational complexity. Kolmogorov complexity
turned out to be a useful technical tool when proving lower bounds for computa-
tional complexity. Let us explain the idea using the following model example.
Consider the following problem: Initially a string 𝑥 of length 𝑛 is located in
the 𝑛 leftmost cells of the tape of a Turing machine. The machine has to copy 𝑥,
that is, to get 𝑥𝑥 on the tape (the string 𝑥 is intact and its copy is appended) and
halt.
Since the middle of 1960ies it is well known that (one-tape) Turing machine
needs time proportional to 𝑛2 to perform this task. More specifically, one can show
that for every Turing machine 𝑀 that can copying every string 𝑥 there exists some
𝜀 > 0 such that for all 𝑛 there is a string 𝑥 of length 𝑛 whose copying requires at
least 𝜀𝑛2 steps.
Consider the following intuitive argument supporting this claim. The number
of internal states of a Turing machine is a constant (depending on the machine).
That is, the machine can keep in its memory only a finite number of bits. The
speed of the head movement is also limited: one cell per step. Hence the rate of
information transfer (measured in bit·cell/step) is bounded by a constant depending
on the number of internal states. To copy a string 𝑥 of length 𝑛, we need to move 𝑛
bits by 𝑛 cells to the right, therefore the number of steps should be proportional
to 𝑛2 (or more).
Using Kolmogorov complexity, we can make this argument rigorous. A string
is hard to copy if it contains maximal amount of information, i.e., its complexity is
close to 𝑛. We consider this example in detail in Section 8.2 (p. 245).
A combinatorial interpretation of Kolmogorov complexity. We con-
sider here one example of this kind (see Chapter 10, p. 323, for more details).
One can prove the following inequality for complexity of three strings and their
combinations:
2𝐶(𝑥𝑦𝑧) 6 𝐶(𝑥𝑦) + 𝐶(𝑥𝑧) + 𝐶(𝑦𝑧) + 𝑂(log 𝑛)
for all strings 𝑥, 𝑦, 𝑧 of length at most 𝑛.
It turns out that this inequality has natural interpretations that are not related
to complexity at all. In particular, it implies (see [65]) the following geometrical
fact:
Consider a body 𝐵 in a three-dimensional Euclidean space with coordinate axes
𝑂𝑋, 𝑂𝑌 and 𝑂𝑍. Let 𝑉 be 𝐵’s volume. Consider 𝐵’s orthogonal projections onto
coordinate planes 𝑂𝑋𝑌 , 𝑂𝑋𝑍 and 𝑂𝑌 𝑍. Let 𝑆𝑥𝑦 , 𝑆𝑥𝑧 and 𝑆𝑦𝑧 be the areas of
these projections. Then
𝑉 2 6 𝑆𝑥𝑦 · 𝑆𝑥𝑧 · 𝑆𝑦𝑧 .
Here is an algebraic corollary of the same inequality. For every group 𝐺 and
its subgroups 𝑋, 𝑌 and 𝑍 we have
|𝑋 ∩ 𝑌 ∩ 𝑍|2 > |𝑋 ∩ 𝑌 | · |𝑋 ∩ 𝑍| · |𝑌 ∩ 𝑍|
|𝐺| ,
where |𝐻| denotes the number of elements in 𝐻.

---

[previous page](page-020.md) · [next page](page-022.md) · [all pages](index.md)
