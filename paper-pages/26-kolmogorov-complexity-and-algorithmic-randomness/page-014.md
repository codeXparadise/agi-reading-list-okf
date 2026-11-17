---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 14
pages: [14]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "COMPLEXITY AND INFORMATION 15 strings. This situation is typical also for computational complexity: usually upper and lower bounds for complexity of…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 14 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 14 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

COMPLEXITY AND INFORMATION 15
strings. This situation is typical also for computational complexity: usually upper
and lower bounds for complexity of some computational problem are asymptotic
bounds.
Complexity and information
One can consider the Kolmogorov complexity of 𝑥 as the amount of informa-
tion in 𝑥. Indeed, a string of zeros, which has a very short description, has little
information, and a chaotic string, which cannot be compressed, has a lot of informa-
tion (although that information can be meaningless—we do not try to distinguish
between meaningful and meaningless information; so, in our view, any abracadabra
has much information unless it has a short description).
If the complexity of a string 𝑥 is equal to 𝑘, we say that 𝑥 has 𝑘 bits of
information. One can expect that the amount of information in a string does not
exceed its length, that is, 𝐶(𝑥) 6 𝑙(𝑥). This is true (up to an additive constant, as
we have already said).
Theorem 2. There is a constant 𝑐 such that
𝐶(𝑥) 6 𝑙(𝑥) + 𝑐
for all strings 𝑥.
Proof. Let 𝐷(𝑦) = 𝑦 for all 𝑦. Then 𝐶𝐷 (𝑥) = 𝑙(𝑥). By optimality, there
exists some 𝑐 such that
𝐶(𝑥) 6 𝐶𝐷 (𝑥) + 𝑐 = 𝑙(𝑥) + 𝑐
for all 𝑥. 
Usually this statement is written as follows: 𝐶(𝑥) 6 𝑙(𝑥) + 𝑂(1). Theorem 2
implies, in particular, that Kolmogorov complexity is always finite, that is, every
string has a description.
Here is another property of “amount of information” that one can expect: the
amount of information does not increase when algorithmic transformation is per-
formed. (More precisely, the increase is bounded by an additive constant depending
on the transformation algorithm.)
Theorem 3. For every algorithm 𝐴 there exists a constant 𝑐 such that
𝐶(𝐴(𝑥)) 6 𝐶(𝑥) + 𝑐
for all 𝑥 such that 𝐴(𝑥) is defined.
Proof. Let 𝐷 be an optimal decompressor that is used in the definition of the
Kolmogorov complexity. Consider another decompressor 𝐷′:
𝐷′(𝑝) = 𝐴(𝐷(𝑝)).
(We apply first 𝐷 and then 𝐴.) If 𝑝 is a description of a string 𝑥 with respect to 𝐷
and 𝐴(𝑥) is defined, then 𝑝 is a description of 𝐴(𝑥) with respect to 𝐷′. Let 𝑝 be a
shortest description of 𝑥 with respect to 𝐷. Then we have
𝐶𝐷′ (𝐴(𝑥)) 6 𝑙(𝑝) = 𝐶𝐷 (𝑥) = 𝐶(𝑥).
By optimality we obtain
𝐶(𝐴(𝑥)) 6 𝐶𝐷′ (𝐴(𝑥)) + 𝑐 6 𝐶(𝑥) + 𝑐
for some 𝑐 and all 𝑥. 

---

[previous page](page-013.md) · [next page](page-015.md) · [all pages](index.md)
