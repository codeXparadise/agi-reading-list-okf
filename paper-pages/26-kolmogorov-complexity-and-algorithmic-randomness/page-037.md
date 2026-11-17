---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 37
pages: [37]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "38 1. PLAIN KOLMOGOROV COMPLEXITY Theorem 12. For every function 𝑑 there is a constant 𝑐 such that B 𝑑(𝑛) 6 B (𝑛 + 𝑐) for all 𝑛. Proof. For every 𝑥…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 37 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 37 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

38 1. PLAIN KOLMOGOROV COMPLEXITY
Theorem 12. For every function 𝑑 there is a constant 𝑐 such that
B 𝑑(𝑛) 6 B (𝑛 + 𝑐)
for all 𝑛.
Proof. For every 𝑥 of length at most 𝑛 the complexity of 𝑑(𝑥) is less than
𝑛 + 𝑐 for some constant 𝑐. Indeed, the complexity of 𝑑(𝑥) exceeds at most by a
constant the complexity of 𝑥, which is less than 𝑛 + 𝑂(1). Hence 𝑑(𝑥) does not
exceed the largest number of complexity 𝑛 + 𝑐 or less, i.e., B (𝑛 + 𝑐). 
This (trivial) observation is useful in the following special case. Let 𝑀 be an
algorithm and let 𝑋 be a set of binary strings. A halting problem for 𝑀 restricted
to 𝑋 is the following problem: given a string 𝑥 ∈ 𝑋, find out whether 𝑀 terminates
on 𝑥 or not.
A classical result in computability theory states that for some algorithm 𝑀 the
unrestricted halting problem (𝑋 = Ξ) for 𝑀 is undecidable.
We are interested now in the case when 𝑋 is the set of all strings of bounded
length. Fix some algorithm 𝑀 and consider the running time 𝑡(𝑥) of 𝑀 for some
input 𝑥. If 𝑀 does not halt on 𝑥, then 𝑡(𝑥) is undefined. Thus the domains of 𝑡
and 𝑀 coincide. By definition, B 𝑡(𝑛) is the maximal running time of 𝑀 on inputs
of length at most 𝑛. If we know B 𝑡(𝑛) or any larger number 𝑚, we can solve the
halting problem for 𝑀 and every input 𝑥 of length at most 𝑛: Run 𝑀 on input 𝑥;
if the computation does not terminate after 𝑚 steps, it never terminates.
We have seen that B 𝑡(𝑛) 6 B (𝑛 + 𝑐) for some constant 𝑐 (depending on 𝑀 ).
Therefore the knowledge of B (𝑛 + 𝑐) or any greater number is enough to solve the
halting problem of 𝑀 on inputs of length at most 𝑛. In other words, the following
holds:
Theorem 13. For every algorithm 𝑀 there is a constant 𝑐 and another al-
gorithm 𝐴 having the following property. For every 𝑛 and for every number 𝑡 >
B (𝑛 + 𝑐) the algorithm 𝐴, given 𝑛 and 𝑡, produces the list of all strings 𝑥 of length
at most 𝑛 such that 𝑀 halts on input 𝑥.
This theorem says that the halting problem for inputs of length at most 𝑛 is
reducible to the problem of finding a number greater than B (𝑛 + 𝑐).
If 𝑀 is the optimal decompressor 𝐷 then the converse is also true: given 𝑛 and
the list of all strings 𝑥 of length at most 𝑛 in the domain of 𝐷 we can find B (𝑛).
Continuing this argument, we can prove the following result:
Theorem 14. Let BB (𝑛) denote the maximal running time of the optimal
decompressor 𝐷 on strings of length at most 𝑛 (in the domain of 𝐷). Then
BB (𝑛) 6 B (𝑛 + 𝑐) and B (𝑛) 6 BB (𝑛 + 𝑐)
for some 𝑐 and all 𝑛.
Proof. Let 𝛼𝑛 be the most time-consuming description of length at most 𝑛,
that is, the string 𝑥 of length at most 𝑛 in the domain of 𝐷 that maximizes the
running time of 𝐷 on 𝑥. Knowing 𝑛 and 𝛼𝑛, one can generate the list of all strings
of length at most 𝑛 in the domain of 𝐷, and hence the number BB (𝑛). Both 𝑛 and
𝛼𝑛 can be encoded in one string of length 𝑛 + 1, the string 0 . . . 01𝛼𝑛 (there are
𝑛 − 𝑙(𝛼𝑛) zeros in the beginning). Therefore, the Kolmogorov complexity of BB (𝑛)
is at most 𝑛 + 𝑂(1), and BB (𝑛) 6 B (𝑛 + 𝑐) for some 𝑐 and all 𝑛.

---

[previous page](page-036.md) · [next page](page-038.md) · [all pages](index.md)
