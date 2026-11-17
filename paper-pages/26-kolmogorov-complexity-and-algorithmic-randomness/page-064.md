---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 64
pages: [64]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "2.3. COMPLEXITY AS THE AMOUNT OF INFORMATION 65 them has any information about 𝑧 in isolation (since 𝐼(𝑥 : 𝑧) ≈ 0 and 𝐼(𝑦 : 𝑧) ≈ 0)), but together…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 64 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 64 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

2.3. COMPLEXITY AS THE AMOUNT OF INFORMATION 65
them has any information about 𝑧 in isolation (since 𝐼(𝑥 : 𝑧) ≈ 0 and 𝐼(𝑦 : 𝑧) ≈ 0)),
but together they can reconstruct 𝑧 as a bitwise sum of 𝑥 and 𝑦.
One can check that we have already given a full list of inequalities that are true
for complexities of three strings and their combinations (all 𝑎𝑖, except for 𝑎5, are
non-negative, as well as three sums mentioned above). We return to this question
in Chapter 10.
Our diagram is a good mnenonic tool. For example, consider again the inequal-
ity
𝐶(𝑥, 𝑦, 𝑧) 6 𝐶(𝑥, 𝑦) + 𝐶(𝑥, 𝑧) + 𝐶(𝑦, 𝑧).
In our new variables it can be rewritten as 𝑎2 + 𝑎4 + 𝑎5 + 𝑎6 > 0 (you can easily
check it by counting the multiplicity of each 𝑎𝑖 in both sides of the inequality). It
remains to note that 𝑎2 + 𝑎5 > 0, 𝑎4 > 0 and 𝑎6 > 0. (Alas, the symmetry is broken
again!)
63 Prove that 𝐼(𝑥𝑦 : 𝑧) = 𝐼(𝑥 : 𝑧) + 𝐼(𝑦 : 𝑧 | 𝑥) + 𝑂(log 𝑛) for strings 𝑥, 𝑦, 𝑧 of
complexity at most 𝑛. [Hint: Use the diagram.]
This problem shows that information in 𝑥𝑦 about 𝑧 can be somehow split into
two parts: information in 𝑥 about 𝑧 and information in 𝑦 about 𝑧 (when 𝑥 is
known). This is somehow similar to the equality 𝐶(𝑥, 𝑦) = 𝐶(𝑥) + 𝐶(𝑦 | 𝑥), but now
complexity is replaced by the quantity of information about 𝑧. As a corollary we
immediately get that if 𝑥𝑦 is independent with 𝑧 then 𝑥 in independent with 𝑧 and,
at the same time 𝑦 is independent with 𝑧 when 𝑥 is known. (Here independence
means that mutual information is negligible.) A symmetric argument shows that 𝑦
is independent with 𝑧 and 𝑥 is independent with 𝑧 when 𝑦 is known.
64 Show that properties “𝑥 is independent with 𝑦” and “𝑥 is independent
with 𝑦 when 𝑧 is known” are quite different: each of them can be true when the
other one is false.
65 We say that strings 𝑥, 𝑦, 𝑧, 𝑡 form a Markov chain (a well known notion
in the probability theory now transferred to the algorithmic information theory) if
𝐼(𝑥 : 𝑧 | 𝑦) and 𝐼(⟨𝑥, 𝑦⟩ : 𝑡 | 𝑧) are negligible. (Of course, we need to specify what is
“negligible” to get a formal definition.) Show that the reversed sequence of strings
also forms a Markov chain, i.e., that 𝐼(𝑡 : 𝑦 | 𝑧) and 𝐼(⟨𝑡, 𝑧⟩ : 𝑥 | 𝑦) are negligible. [Hint:
Since 𝐼(⟨𝑥, 𝑦⟩ : 𝑡 | 𝑧) = 𝐼(𝑦 : 𝑡 | 𝑧) + 𝐼(𝑥 : 𝑡 | 𝑦, 𝑧), the left hand side in this equality is
zero if and only if both terms in the right hand side are zero; and the second term
in the right-hand side does not change when the order of 𝑥, 𝑦, 𝑧, 𝑡 is reversed.]

---

[previous page](page-063.md) · [next page](page-065.md) · [all pages](index.md)
