---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 59
pages: [59]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "60 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY Then any substring 𝑢 of 𝑥 has complexity 𝑙(𝑢) up to 𝑂(log 𝑛) terms. Indeed, since 𝑢 is a…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 59 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 59 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

60 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
Then any substring 𝑢 of 𝑥 has complexity 𝑙(𝑢) up to 𝑂(log 𝑛) terms. Indeed, since
𝑢 is a substring of 𝑟, we have 𝑟 = 𝑡𝑢𝑣 for some strings 𝑡, 𝑣. Then
𝑙(𝑟) = 𝐶(𝑟) 6 𝐶(𝑡) + 𝐶(𝑢) + 𝐶(𝑣) 6 𝑙(𝑡) + 𝑙(𝑢) + 𝑙(𝑣) = 𝑙(𝑟)
(up to a logarithmic error) and therefore all the inequalities are equalities (with the
same logarithmic precision).
Now take two overlapping substrings 𝑥 and 𝑦 (Fig. 3). Then 𝐶(𝑥) is the length
of 𝑥, 𝐶(𝑦) is the length of 𝑦 (up to 𝑂(log 𝑛)).
𝑥 : 𝑦	𝑥 | 𝑦 𝑦 | 𝑥
𝑥 𝑦
𝑥, 𝑦
Figure 3. Common information in overlapping substrings
The complexity 𝐶(𝑥, 𝑦) is equal to the length of the union of segments (since
the pair ⟨𝑥, 𝑦⟩ is equivalent to this union plus information about lengths requiring
𝑂(log 𝑛) bits).
Therefore, conditional complexities 𝐶(𝑥 | 𝑦), 𝐶(𝑦 | 𝑥) and the mutual informa-
tion 𝐼(𝑥 : 𝑦) are equal to the lengths of the corresponding segments (up to 𝑂(log 𝑛)).
However, not always the mutual information can be extracted in form of some
string (like it happened in our example, where this common information is just the
intersection of strings 𝑥 and 𝑦). As we will see in Chapter 11, there exist two strings
𝑥 and 𝑦 that have large mutual information 𝐼(𝑥 : 𝑦) but there is no string 𝑧 that
represents (“materializes”) this information in the following sense: 𝐶(𝑧 | 𝑥) ≈ 0,
𝐶(𝑧 | 𝑦) ≈ 0 (all information that is present in 𝑧 is also present both in 𝑥 and in 𝑦)
and 𝐶(𝑧) ≈ 𝐼(𝑥 : 𝑦) (all mutual information is extracted). In our last example we
can take the intersection substring for 𝑧, but in general this is not possible.
61 Prove that for any string 𝑥 of length at most 𝑛 the expected value of the
mutual information 𝐼(𝑥 : 𝑦) in 𝑥 and random string 𝑦 of length 𝑛 is 𝑂(log 𝑛).
Now we move to triples of strings instead of pairs. Here we have an important
tool that can be called relativization: most of the results proved for unconditional
complexities remain valid for conditional complexities (and proofs remain valid with
minimal changes). Let us give some example of this type.
A theorem about the complexity of pairs (p. 45) says that
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 2 log 𝐶(𝑥) + 𝐶(𝑦) + 𝑂(1).
Replacing all complexities by conditional ones (with the same condition 𝑧 in all
cases), we get the following inequality:
𝐶(𝑥, 𝑦 | 𝑧) 6 𝐶(𝑥 | 𝑧) + 2 log 𝐶(𝑥 | 𝑧) + 𝐶(𝑦 | 𝑧) + 𝑂(1),
By conditional complexity of a pair 𝑥, 𝑦 relative to 𝑧 we mean, as one can expect,
the conditional complexity of its encoding: 𝐶(𝑥, 𝑦 | 𝑧) = 𝐶([𝑥, 𝑦] | 𝑧). As for un-
conditional complexity, the choice of encoding is not important (the complexity
changes by 𝑂(1)).

---

[previous page](page-058.md) · [next page](page-060.md) · [all pages](index.md)
