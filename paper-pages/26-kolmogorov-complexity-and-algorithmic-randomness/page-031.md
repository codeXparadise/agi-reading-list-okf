---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 31
pages: [31]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "32 1. PLAIN KOLMOGOROV COMPLEXITY Proof. Let us prove the theorem. First, we need to show that the set {⟨𝑛, 𝑥⟩ | 𝑥 ∈ 𝑆𝑛} = {⟨𝑛, 𝑥⟩ | 𝐶(𝑥) < 𝑛}, where…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 31 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 31 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

32 1. PLAIN KOLMOGOROV COMPLEXITY
Proof. Let us prove the theorem. First, we need to show that the set
{⟨𝑛, 𝑥⟩ | 𝑥 ∈ 𝑆𝑛} = {⟨𝑛, 𝑥⟩ | 𝐶(𝑥) < 𝑛},
where 𝑛 is a natural number and 𝑥 is a binary string, is enumerable.
Let 𝐷 be the optimal decompressor used in the definition of 𝐶. Perform in
parallel the computations of 𝐷 on all the inputs. (Say, for 𝑘 = 1, 2, . . . we make 𝑘
steps of 𝐷 on 𝑘 first inputs.) If we find that 𝐷 halts on some 𝑦 and returns 𝑥, the
generating algorithm outputs the pair ⟨𝑙(𝑦) + 1, 𝑥⟩. Indeed, this implies that the
complexity of 𝑥 is less than 𝑙(𝑦) + 1, as 𝑦 is a description of 𝑥. Also it outputs all
the pairs ⟨𝑙(𝑦) + 2, 𝑥⟩, ⟨𝑙(𝑦) + 3, 𝑥⟩ . . . in parallel to printing of other pairs.
For those familiar with computability theory, this proof can be compressed to
one line:
𝐶(𝑥) < 𝑛 ⇔ ∃𝑦 (𝑙(𝑦) < 𝑛 ∧ 𝐷(𝑦) = 𝑥).
(The set of pairs ⟨𝑥, 𝑦⟩ such that 𝐷(𝑦) = 𝑥 is enumerable, being the graph of
a computable function. The operations of intersection and projection preserve
enumerability.)
The converse implication is a bit harder. Assume that 𝑉𝑛 is an enumerable
family of finite sets of strings and |𝑉𝑛| < 2𝑛. Fix an algorithm generating the
set {⟨𝑛, 𝑥⟩ | 𝑥 ∈ 𝑉𝑛}. Consider the description mode 𝐷𝑉 that deals with strings
of length 𝑛 in the following way. Strings of length 𝑛 are used as descriptions of
strings in 𝑉𝑛. More specifically, let 𝑥𝑘 be the 𝑘th string in 𝑉𝑛 in the order the pairs
⟨𝑛, 𝑥⟩ appear while generating the set {⟨𝑛, 𝑥⟩ | 𝑥 ∈ 𝑉𝑛}. (We assume there are no
repetitions, so 𝑥0, 𝑥1, 𝑥2 . . . are distinct.) Let 𝑦𝑘 be the 𝑘th string of length 𝑛 in
the lexicographical order. Then 𝑦𝑘 is a description of 𝑥𝑘, that is, 𝐷(𝑦𝑘) = 𝑥𝑘. As
|𝑉𝑛| < 2𝑛, every string in 𝑉𝑛 gets a description of length 𝑛 with respect to 𝐷.
We need to verify that the description mode 𝐷𝑉 defined in this way is com-
putable. To compute 𝐷𝑉 (𝑦) we find the index 𝑘 of 𝑦 in the lexicographical ordering
of strings of length 𝑙(𝑦). Then we run the algorithm generating pairs ⟨𝑛, 𝑥⟩ such
that 𝑥 ∈ 𝑉𝑛 and wait until 𝑘 different pairs having the first component 𝑙(𝑦) appear.
The second component of the last of them is 𝐷𝑉 (𝑦).
By construction, for all 𝑥 ∈ 𝑉𝑛 we have 𝐶𝐷𝑉 (𝑥) 6 𝑛. Comparing 𝐷𝑉 with the
optimal description mode we see that there is a constant 𝑐 such that 𝐶(𝑥) < 𝑛 + 𝑐
for all 𝑥 ∈ 𝑉𝑛. Theorem 7 is proven. 
The intuitive meaning of Theorem 7 is as follows. The assertions “the number
of strings with certain property is small” (is less than 2𝑖) and “all the strings with
certain property are simple” (have complexity less than 𝑖) are equivalent provided
the property under consideration is enumerable and provided the complexity is
measured up to an additive constant (and the number of elements is measured up
to a multiplicative constant).
Theorem 7 can be reformulated as follows. Let 𝑓 (𝑥) be a function defined on
all binary strings and taking as values natural numbers and a special value +∞.
We call 𝑓 upper semicomputable, or enumerable from above, if there is a computable
function ⟨𝑥, 𝑘⟩ ↦ → 𝐹 (𝑥, 𝑘) defined on all strings 𝑥 and all natural numbers 𝑘 such
that
𝐹 (𝑥, 0) > 𝐹 (𝑥, 1) > 𝐹 (𝑥, 2) > . . .
and
𝑓 (𝑥) = lim
𝑘→∞ 𝐹 (𝑥, 𝑘),

---

[previous page](page-030.md) · [next page](page-032.md) · [all pages](index.md)
