---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 32
pages: [32]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "1.1. THE DEFINITION AND MAIN PROPERTIES 33 for all 𝑥. The values of 𝐹 are natural numbers as well as the special constant +∞. The requirements imply…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 32 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 32 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

1.1. THE DEFINITION AND MAIN PROPERTIES 33
for all 𝑥. The values of 𝐹 are natural numbers as well as the special constant +∞.
The requirements imply that for every 𝑘 the value 𝐹 (𝑥, 𝑘) is an upper bound of
𝑓 (𝑥). This upper bound becomes more precise as 𝑘 increases. For every 𝑥 there
is a 𝑘 for which this upper bound is tight. However, we do not know the value of
that 𝑘. (If there is an algorithm that given any 𝑥 finds such 𝑘, then the function 𝑓
is computable.) Evidently, any computable function is upper semicomputable.
A function 𝑓 is upper semicomputable if and only if the set
𝐺𝑓 = {⟨𝑥, 𝑛⟩ | 𝑓 (𝑥) < 𝑛}
is enumerable. This set is sometimes called the “upper graph of 𝑓 ”, which explains
the strange names “upper semicomputable” and “enumerable from above”.
Let us verify this. Assume that a function 𝑓 is upper semicomputable. Let
𝐹 (𝑥, 𝑘) be the function from the definition of semicomputability. Then we have
𝑓 (𝑥) < 𝑛 ⇔ ∃𝑘 𝐹 (𝑥, 𝑘) < 𝑛.
Thus, performing in parallel the computations of 𝐹 (𝑥, 𝑘) for all 𝑥 and 𝑘, we can
generate all the pairs in the upper graph of 𝑓 .
Assume now that the set 𝐺𝑓 is enumerable. Fix an algorithm enumerating this
set. Then define 𝐹 (𝑥, 𝑘) as the best upper bound of 𝑓 obtained after 𝑘 steps of
generating elements in 𝐺𝑓 . That is, 𝐹 (𝑥, 𝑘) is equal to the minimal 𝑛 such that
the pair ⟨𝑥, 𝑛 + 1⟩ has been printed after 𝑘 steps. If there is no such pair, let
𝐹 (𝑥, 𝑘) = +∞.
Using the notion of an upper semicomputable function we can reformulate
Theorem 7 as follows.
Theorem 8. (a) The function 𝐶 is upper semicomputable and
|{𝑥 | 𝐶(𝑥) < 𝑛}| < 2𝑛
for all 𝑛.
(b) If a function 𝐶′ is upper semicomputable and |{𝑥 | 𝐶′(𝑥) < 𝑛}| < 2𝑛 for
all 𝑛, then 𝐶(𝑥) 6 𝐶′(𝑥) + 𝑐 for some 𝑐 and for all 𝑥.
Note that the upper bound 2𝑛 of the cardinality of |{𝑥 | 𝐶′(𝑥) < 𝑛}| in item
(b) can be replaced by a weaker upper bound 𝑂(2𝑛).
Theorem 8 allows to define Kolmogorov complexity as a minimal (up to an
additive constant) upper semicomputable function 𝑘 that satisfies the inequality
|{𝑥 | 𝑘(𝑥) < 𝑛}| = 𝑂(2𝑛).
One can replace the requirement of minimality in this definition by some other
properties of 𝐶. In this way we obtain the following “axiomatic” definition of
Kolmogorov complexity [172]:
Theorem 9. Let 𝑘 be a function defined on binary strings and taking natural
values. Assume that 𝑘 satisfies the following properties:
(a) 𝑘 is upper semicomputable; [enumerability axiom]
(b) for every partial computable function 𝐴 from Ξ to Ξ the inequality
𝑘(𝐴(𝑥)) 6 𝑘(𝑥) + 𝑐
is valid for some 𝑐 and all 𝑥 in the domain of 𝐴; [complexity non-increase axiom]
(c) the number of strings 𝑥 such that 𝑘(𝑥) < 𝑛 is in the range [2𝑛−𝑐1 ; 2𝑛+𝑐2 ]
for some 𝑐1, 𝑐2 and for any 𝑛. [calibration axiom]

---

[previous page](page-031.md) · [next page](page-033.md) · [all pages](index.md)
