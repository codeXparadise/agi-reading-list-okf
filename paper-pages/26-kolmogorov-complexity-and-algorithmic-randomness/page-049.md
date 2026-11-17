---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 49
pages: [49]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "50 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY we choose a fresh value of 𝑦 and then choose appropriate 𝑥. This process is effective if 𝑛…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 49 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 49 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

50 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
we choose a fresh value of 𝑦 and then choose appropriate 𝑥. This process is effective
if 𝑛 (=length of 𝑦) is given, it defines a partial function 𝑦 ↦ → 𝑥, so 𝐶(𝑥 | 𝑦) = 𝑂(1)
for every pair selected.]
31 Let 𝑥 and 𝑦 be two bit strings such that CT(𝑥 | 𝑦) 6 𝑛 and CT(𝑦 | 𝑥) 6 𝑛.
Prove that there exists a program of a computable permutation of the set of bit
strings that maps 𝑥 to 𝑦 and has complexity at most 2𝑛 + 𝑂(1). [Hint: it is easy
to construct a string 𝑣 of length 2𝑛 + 𝑂(1) that encodes a pair of total programs
𝑓 that maps 𝑥 to 𝑦 and 𝑔 that maps 𝑦 to 𝑥. We may assume without loss of
generality that 𝑥 and 𝑦 have 0 as their first bits. Consider a binary relation on
binary strings that starts with 0, defined as 𝑅(𝑢, 𝑣) : (𝑓 (𝑢) = 𝑣) and (𝑔(𝑣) = 𝑢)).
This is a decidable one-to-one correspondence between decidable sets of strings with
infinite complements, and it can be easily extended to a computable permutation.]
32 Show that the upper bound in the preceding problem cannot be improved
significantly: for every 𝑘 there are two strings 𝑥 and 𝑦 of length 𝑛 = 2𝑘 + 𝑂(1)
such that 𝐶(𝑥), 𝐶(𝑦) 6 𝑘 + 𝑂(1) (and therefore CT(𝑥 | 𝑦), CT(𝑦 | 𝑥) 6 𝑘 + 𝑂(1)),
but every permutation of 𝑛-bit strings that maps 𝑥 to 𝑦 has complexity at least
2𝑘. [Hint: Let us first select (arbitrarily) 2𝑘 strings 𝑦 and pair them with some
string 𝑥. Let us enumerate computable permutations of 𝑛-bit strings that have
complexity less than 2𝑘. If and when all selected pairs are served by some of these
permutations, choose a new string 𝑥 that is connected (by existing permutation)
with at most half of the selected 𝑦-strings. After that Ω(2𝑘) new permutations are
needed to connect new 𝑥 to all 𝑦-strings. Therefore at most 22𝑘/Ω(2𝑘) = 𝑂(2𝑘)
𝑥-strings will be used, so the final 𝑥 and 𝑦 have complexity at most 𝑘 + 𝑂(1). The
selection of 𝑥 connected with at most half of selected 𝑦-strings is always possible,
since each of 𝑦-strings is connected with a small fraction of 𝑥-strings, and we can
change the order of summation in the double sum. Note that this argument may
be used to guarantee that one of the strings 𝑥 and 𝑦 belongs to a given set of 2𝑘
strings.]
See [135] for the detailed proofs of these results about total conditional com-
plexity.
Many properties of unconditional complexity have conditional counterparts
with essentially the same proofs. Here are some of these counterparts:
∙ Function 𝐶(· | ·) is upper semicomputable (this means that the set of triples
⟨𝑥, 𝑦, 𝑛⟩ such that 𝐶(𝑥 | 𝑦) < 𝑛 is enumerable).
∙ For any 𝑦 and 𝑛 the set of all strings 𝑥 such that 𝐶(𝑥 | 𝑦) < 𝑛 has cardi-
nality less then 2𝑛.
∙ For any 𝑦 and 𝑛 there exists a string 𝑥 of length 𝑛 such that 𝐶(𝑥 | 𝑦) > 𝑛.
33 Prove that for any strings 𝑦 and 𝑧 and for any number 𝑛 there exists a
string 𝑥 of length 𝑛 such that 𝐶(𝑥 | 𝑦) > 𝑛 − 1 and 𝐶(𝑥 | 𝑧) > 𝑛 − 1. [Hint: both
requirements are violated by a minority of strings.]
Theorem 19. Let ⟨𝑥, 𝑦⟩ ↦ → 𝑘(𝑥, 𝑦) be an upper semicomputable function such
that the set {𝑥 | 𝑘(𝑥, 𝑦) < 𝑛} has cardinality less than 2𝑛 for any string 𝑦 and
integer 𝑛. Then 𝐶(𝑥 | 𝑦) 6 𝑘(𝑥, 𝑦) + 𝑐 for some 𝑐 and for all 𝑥 and 𝑦.
The proof repeats the proof of Theorem simple-upper-reformulated.
Using conditional complexity, we get a stronger inequality for the complexity
of pairs (compared with Theorem 16, p. 45):

---

[previous page](page-048.md) · [next page](page-050.md) · [all pages](index.md)
