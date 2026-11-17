---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 40
pages: [40]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "1.2. ALGORITHMIC PROPERTIES 41 To prove the lower bound of 𝐶(𝑋𝑛) let 𝑛 − 𝑑 be the complexity of 𝑋𝑛. For some constant 𝑐 the string 𝛾𝑛−𝑐 can be…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 40 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 40 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

1.2. ALGORITHMIC PROPERTIES 41
To prove the lower bound of 𝐶(𝑋𝑛) let 𝑛 − 𝑑 be the complexity of 𝑋𝑛. For
some constant 𝑐 the string 𝛾𝑛−𝑐 can be obtained from the shortest description of
𝑋𝑛 of length 𝑛 − 𝑑 and from 𝑑 (note that 𝑛 can be retrieved from the length of
the shortest description and 𝑑). Thus, 𝑛 − 𝑐 6 𝐶(𝛾𝑛−𝑐) 6 (𝑛 − 𝑑) + 2 log 𝑑 + 𝑂(1).
Therefore 𝑑 6 2 log 𝑑 + 𝑐 + 𝑂(1) and hence 𝑑 = 𝑂(1). 
8 The objects in Theorem 15 depend on the choice of the optimal decompres-
sor. In the proof we assumed that the same optimal decompressor is used in all the
items (a)–(h). Prove that the statement of the theorem remains true if different
decompressors are used.
9 Prove that the complexity of all the objects in Theorem 15 becomes 𝑂(log 𝑛)
if we relativize the definition of Kolmogorov complexity by 0′, that is, if we allow
the decompressor to query the oracle for the halting problem.
We have seen that there exist a constant 𝑐 and an algorithm 𝐴 that given the
string 𝛾𝑛 solves the halting problem for the optimal decompressor on inputs of
length at most 𝑛 − 𝑐. This means that given an “oracle” that finds 𝛾𝑛 for every
given 𝑛 we can solve the halting problem. The same can be done given an oracle
deciding whether a given string 𝑥 is “incompressible”, that is, 𝐶(𝑥) > 𝑙(𝑥). Indeed,
using that oracle we can find 𝛾𝑛 by probing all strings of length 𝑛.
Using the terminology of computability theory, we can say that halting problem
is Turing reducible to the set of incompressible strings (or its complement, the set
of compressible strings). This implies that halting problem is also reducible to the
“upper graph” of 𝐶, that is, to the set {⟨𝑥, 𝑘⟩ | 𝐶(𝑥) < 𝑘}. Using the terminology
of computability theory, we say that the set of compressible strings (as well as the
upper graph of 𝐶) is Turing complete in the class of enumerable sets (this means
that it is enumerable and that the halting problem is Turing reducible to it).
10 Find some upper bound for the number of oracle queries for the set
{⟨𝑥, 𝑘⟩ | 𝐶(𝑥) < 𝑘}
needed to solve the halting problem for a fixed machine 𝑀 and for all strings of
length at most 𝑛.
11 Let 𝑓 be a computable partial function from N to N. Prove that there
is a constant 𝑐 such that for all 𝑛 such that 𝑓 (B (𝑛)) is defined the inequality
B (𝑛 + 𝑐) > 𝑓 (B (𝑛)) is true. [Hint: the complexity of 𝑓 (B (𝑛)) is at most 𝑛 + 𝑂(1).]
12 Call a set 𝑈 𝑟-separable [136] if every enumerable set 𝑉 disjoint with 𝑈
can be separated from 𝑈 by a decidable set, that is, there is a decidable set 𝑅 that
includes 𝑉 and is disjoint with 𝑈 .
(a) Prove that the the set {⟨𝑥, 𝑘⟩ | 𝐶(𝑥) < 𝑘} (the upper graph of 𝐶) is an
𝑟-separable set. The set of compressible strings is 𝑟-separable, too. [Hint: assume
that the upper graph of 𝐶 is disjoint with some enumerable set 𝑉 . The set of
the second components of pairs in 𝑉 is finite, otherwise we get an unbounded
computable lower bound for 𝐶. That is, 𝑉 is included in a horizontal strip of finite
height. The intersection of the strip with the upper graph is finite.]
(b) We say that a set 𝑈1 is 𝑚-reducible to a set 𝑈2 if there is a total computable
function 𝑓 such that 𝑈1 = 𝑓 −1(𝑈2). Prove that if 𝑈2 is 𝑟-separable and 𝑈1 is 𝑚-
reducible to 𝑈2 then 𝑈1 is 𝑟-separable as well. [Hint. If 𝑉 is an enumerable set
disjoint with 𝑈1 then 𝑓 (𝑉 ) is an enumerable set disjoint with 𝑈2. If 𝑅 is a decidable
set separating 𝑓 (𝑉 ) and 𝑈2 then 𝑓 −1(𝑅) is a decidable set separating 𝑉 and 𝑈1.]

---

[previous page](page-039.md) · [next page](page-041.md) · [all pages](index.md)
