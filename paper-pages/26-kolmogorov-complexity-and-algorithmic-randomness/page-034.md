---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 34
pages: [34]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "1.2. ALGORITHMIC PROPERTIES 35 satisfies the inequality 𝐶(𝑦) 6 𝑛 − log 𝑛 + 𝑐. [Hint. For a given natural 𝑘 consider a Boolean matrix of size 𝑘 × (2𝑘…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 34 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 34 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

1.2. ALGORITHMIC PROPERTIES 35
satisfies the inequality 𝐶(𝑦) 6 𝑛 − log 𝑛 + 𝑐. [Hint. For a given natural 𝑘 consider
a Boolean matrix of size 𝑘 × (2𝑘 − 1) whose columns are all nonzero strings of
length 𝑘. (Such matrix is used for Hamming codes.) Consider the linear mapping
B2𝑘 −1 → B𝑘 defined by this matrix, where B denotes the field {0, 1}. It is easy to
verify that for every vector 𝑥 one can flip one bit in 𝑥 so that the resulting string 𝑦
is in the kernel of this mapping, and the elements of the kernel have complexity at
most 2𝑘 − 𝑘 + 𝑂(1). This gives the desired result for 𝑛 = 2𝑘 − 1; if 𝑛 has not the
form 2𝑘 − 1, we can flip one of the first 2𝑘 − 1 bits for an appropriate 𝑘.]
### 1.2. Algorithmic properties
The function 𝐶 is upper semicomputable. On the other hand, it is not com-
putable and, moreover, it has no unbounded computable lower bounds (Theorem 6,
p. 19).
This implies that all optimal description modes are necessarily non-total, that
is, some strings describe nothing. Indeed, if a description mode 𝐷 is total then we
can compute 𝐶𝐷 (𝑥) just by trying all descriptions in the lexicographical order until
we find the shortest one.
At first glance, this contradicts to our intuition: the bigger the domain of 𝐷
is, the better 𝐷 is. If optimal decompressor 𝐷 is undefined on some string 𝑦 then
we can define another description mode 𝐷′ as follows. Let 𝐷′(𝑦) be equal to a
string 𝑧 of complexity (with respect to 𝐷) greater than 𝑙(𝑦) and let 𝐷′ coincide
with 𝐷 on all other strings. The description mode 𝐷′ is a bit better than 𝐷, as the
complexity of all strings except 𝑧 remains the same while the complexity of 𝑧 has
been decreased.
There is no formal contradiction here, as 𝐷 is still not worse than 𝐷′ (they differ
only at one point, the difference between the complexities is bounded by a constant,
and both 𝐷 and 𝐷′ are optimal). However, this is still a bit strange. This observa-
tion was made by Yu. Manin in his book “Computable and non-computable” [113]
(by the way, in this book he also discussed the computational power of quantum
mechanics long before quantum computing became fashionable).
A similar argument shows that the domain of every optimal description mode
is undecidable. (The set of strings is called decidable, or computable, if there is an
algorithm that for any given string decides whether it belongs to the set or not.)
Indeed, if there were an algorithm deciding whether 𝐷(𝑥) is defined or not, then
there would be a total computable extension of 𝐷 (for example, let 𝐷(𝑥) = 0 for all
𝑥 outside the domain of 𝐷). This extension would be a total optimal description
mode, but this is impossible as we have seen.
As a byproduct we get an algorithm whose domain is undecidable. This is one
of the central theorems in computability theory (see, for example, [182]).
In general the notion of Kolmogorov complexity has a lot of connections with
computability theory. Recently many interesting facts were discovered, see [146,
49]. We consider here only two basic examples (a simple set of simple strings, and
the complexity of large numbers).
1.2.1. Simple strings and simple sets. In this section, the word “simple”
has two unrelated meanings. First, when applied to strings, it means that the
Kolmogorov complexity of the string is small. Second, it is applied to sets of

---

[previous page](page-033.md) · [next page](page-035.md) · [all pages](index.md)
