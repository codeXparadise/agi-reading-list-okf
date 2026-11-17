---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 35
pages: [35]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "36 1. PLAIN KOLMOGOROV COMPLEXITY strings. The notion of a simple set was introduced by an American logician Emil Post and has no relation to…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 35 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 35 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

36 1. PLAIN KOLMOGOROV COMPLEXITY
strings. The notion of a simple set was introduced by an American logician Emil
Post and has no relation to Kolmogorov complexity.
Definition. An enumerable set 𝐴 is simple (according to Post) if its comple-
ment is infinite but has no infinite enumerable subset.
Call a string 𝑥 “simple” if 𝐶(𝑥) < 𝑙(𝑥)/2.
Theorem 10. The set of all “simple” strings is simple in the sense of Post.
Proof. That set 𝑆 of all “simple” strings is enumerable. Indeed, the function
𝐶 is upper semicomputable, and if 𝐶(𝑥) is less than |𝑥|/2, this can be seen while
approximating 𝐶(𝑥) from above.
The number of strings of complexity less than 𝑛/2 does not exceed 2𝑛/2. There-
fore the fraction of “simple” strings among strings of length 𝑛 is negligible, and the
complement of 𝑆 is infinite.
Assume now that the complement of 𝑆 has an infinite enumerable subset 𝑈 . We
can use 𝑈 to obtain a computable unbounded lower bound of 𝐶. To find a string of
complexity greater than 𝑡 we can generate elements of 𝑈 until we find a string 𝑢𝑡 of
length greater than 2𝑡. As 𝑈 is infinite, there is such a string. The complexity of 𝑢𝑡
is greater than 𝑡, otherwise 𝑢𝑡 is simple. Without loss of generality we can assume
that the strings 𝑢𝑡, 𝑡 = 1, 2, . . . are pairwise different. Thus the function 𝑢𝑡 ↦ → 𝑡
is a computable unbounded lower bound for 𝐶. This contradicts to Theorem 6
(page 19). 
Note that the choice of the threshold 𝑙(𝑥)/2 in the definition of a simple string
was not essential. The proof of Theorem 10 would work as well with 𝑙(𝑥) − 1 or
log log 𝑙(𝑥) in place of 𝑙(𝑥)/2.
1.2.2. Complexity of large numbers. Let us identify a natural number 𝑚
with the binary string having index 𝑚 in the standard enumeration of binary strings.
In this way 𝐶 becomes a function of a natural argument. The function 𝐶(𝑚) goes
to infinity as 𝑚 → ∞. Indeed, for all 𝑛 there are only finitely many integers of
complexity less than 𝑛. However, the convergence is not effective. That is, there
is no algorithm that for every given 𝑛 finds a number 𝑁 such that the complexity
of 𝑁 and of all larger numbers is bigger than 𝑛. Indeed, such an algorithm would
provide an effective way to describe the number 𝑁 , whose complexity is at least 𝑛,
by log 𝑛 + 𝑂(1) bits. We have seen this in the proof of Theorem 6 (p. 19).
In this section, we study in detail the rate of convergence of 𝐶 to infinity.
Following Chaitin [31], we consider for every natural 𝑛 the largest number B (𝑛)
whose complexity is at most 𝑛:
B (𝑛) = max{𝑚 ∈ N | 𝐶(𝑚) 6 𝑛}
The function 𝑛 ↦ → B (𝑛) may be called the modulus of the convergence of 𝐶(𝑚) to
infinity. Indeed, 𝐾(𝑥) > 𝑛 for all 𝑥 > B (𝑛) (and B (𝑛) is the minimal number with
this property). Note also that it can happen (for small values of 𝑛) that 𝐶(𝑚) > 𝑛
for all 𝑚. In this case we let B (𝑛) = −1.
The function B can be considered as an inverse function to the function
𝐶>(𝑁 ) = min{𝐶(𝑚) | 𝑚 > 𝑁 }.
The function 𝐶> grows very slowly. It takes the value 𝑛 between 𝐵(𝑛 − 1) and
𝐵(𝑛), more precisely, on the interval (B (𝑛 − 1), B (𝑛)]. The slow increase of 𝐶>

---

[previous page](page-034.md) · [next page](page-036.md) · [all pages](index.md)
