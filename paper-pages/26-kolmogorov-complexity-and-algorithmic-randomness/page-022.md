---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 22
pages: [22]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "SOME APPLICATIONS OF KOLMOGOROV COMPLEXITY 23 G¨odel incompleteness theorem. Following G. Chaitin, let us explain how to use Theorem 6 in order to…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 22 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 22 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

SOME APPLICATIONS OF KOLMOGOROV COMPLEXITY 23
G¨odel incompleteness theorem. Following G. Chaitin, let us explain how
to use Theorem 6 in order to prove the famous G¨odel incompleteness theorem. This
theorem states that not all true statements of a formal theory that is “rich enough”
(the formal arithmetic and the axiomatic set theory are two examples of such a
theory) are provable in the theory.
Assume that for every string 𝑥 and every natural number 𝑛, one can express
the statement 𝐶(𝑥) > 𝑛 as a formula in the language of our theory. (This statement
says that the chosen optimal decompressor 𝐷 does not output 𝑥 on any input of
length at most 𝑛; one can easily write this statement in the formal arithmetic and
therefore in the set theory.)
Let us generate all the proofs (derivations) in our theory and select those of
them who prove some statement of the form 𝐶(𝑥) > 𝑛 where 𝑥 is some string
and 𝑛 is some integer (statements of this type have no free variables). Once we
have found a new theorem of this type, we compare 𝑛 with all previously found 𝑛’s.
If the new 𝑛 is greater than all previous 𝑛’s we write the new 𝑛 into the “records
table” together with the corresponding 𝑥𝑛.
There are two possibilities: either (1) the table will grow infinitely, or (2) there
is the last statement 𝐶(𝑋) > 𝑁 in the table which remains unbeaten forever. If (2)
happens, there is an entire class of true statements that have no proof. Namely, all
true statements of the form 𝐶(𝑥) > 𝑛 with 𝑛 > 𝑁 have no proofs. (Recall that by
Theorem 5 there are infinitely many such statements.)
In the first case we have infinite computable sequences of strings 𝑥0, 𝑥1, 𝑥2 . . .
and numbers 𝑛0 < 𝑛1 < 𝑛2 < . . . such that all statements 𝐶(𝑥𝑖) > 𝑛𝑖 are provable.
We assume that the theory proves only true statements, thus all the inequalities
𝐶(𝑥𝑖) > 𝑛𝑖 are true. Without loss of generality we can assume that all 𝑥𝑖 are
pairwise different (we can omit 𝑥𝑖 if there exists 𝑗 < 𝑖 such that 𝑥𝑗 = 𝑥𝑖; every string
can occur only finitely many times in the sequence 𝑥0, 𝑥1, 𝑥2 . . . since 𝑛𝑖 → ∞ as
𝑖 → ∞). The computable function 𝑘, defined by the equation 𝑘(𝑥𝑖) = 𝑛𝑖, is then an
unbounded lower bound for Kolmogorov complexity. This contradicts Theorem 6.

---

[previous page](page-021.md) · [next page](page-023.md) · [all pages](index.md)
