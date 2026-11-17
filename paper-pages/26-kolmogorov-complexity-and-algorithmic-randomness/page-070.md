---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 70
pages: [70]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "3.2. THE STRONG LAW OF LARGE NUMBERS 71 0 1 1/2 𝑢 1 𝐻(𝑢, 1 − 𝑢) Figure 1. Shannon entropy as a function of 𝑢. Lemma. The fraction of strings of…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 70 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 70 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

3.2. THE STRONG LAW OF LARGE NUMBERS 71
0 1	1/2 𝑢
1
𝐻(𝑢, 1 − 𝑢)
Figure 1. Shannon entropy as a function of 𝑢.
Lemma. The fraction of strings of length 𝑛 where frequency of ones differs
from 1/2 at least by 𝜀 (among all strings of length 𝑛) does not exceed some 𝛿𝑛 that
decreases exponentially as 𝑛 increases.
This lemma (without any specific claims for the fast convergence 𝛿𝑛 → 0) is
called the Law of Large Numbers. To prove the Strong Law of Large Numbers we
need to know that the series∑︀ 𝑛 𝛿𝑛 is convergent.
We need to prove that the set 𝐴1/2 of all sequences that have limit frequency
of ones equal to 1/2 has measure 1. In other terms, we need to prove that the
complement of this set (we denote this complement by 𝐵) is a null set.
According to the definition of limit the set 𝐵 is the union (over all 𝜀 > 0) of
the sets 𝐵𝜀. Here 𝐵𝜀 is the set of all sequences such that frequency of ones in their
prefixes exceeds 1/2 + 𝜀 (or is less than 1/2 − 𝜀) infinitely many times.
Evidently, we can consider only a countable set of different 𝜀 (e.g., only rational
values), and the countable union of null sets is a null set. Therefore it remains to
prove that the set 𝐵𝜀 is a null set for each 𝜀.
The set 𝐵𝜀 consists of the sequences that have arbitrarily long “bad” prefixes.
Here “bad” prefix is a string where the frequency of ones differs from 1/2 more
than by 𝜀. Therefore, for each 𝑁 the set 𝐵𝜀 is covered by the family of intervals
Ω𝑥 where 𝑥 ranges over all bad strings of length at least 𝑁 . The total (uniform)
measure of all this intervals does not exceed
𝛿𝑁 + 𝛿𝑁 +1 + 𝛿𝑁 +2 + . . . ,
and this sum can be made small since the series∑︀ 𝑖 𝛿𝑖 is convergent.
(Probability theorists call this argument Borel–Cantelli lemma. In its general
form this lemma says that if the sum of measures of some sets 𝐴0, 𝐴1, . . . is finite,
then the set of all points that belong to infinitely many 𝐴𝑖 is a null set.) 
One can get a bound for the number of bad strings of length 𝑛 without Stirling’s
approximation. We do it separately for bad strings that have too many and too few
ones. For example, let us consider the set of all “bad” strings that have frequency
of ones greater than 1/2 + 𝜀. To get a bound for the cardinality of this set, consider
two distributions (measures) on the set of all strings of length 𝑛. The first one,
called 𝐿, is the uniform distribution: all strings have probability 2−𝑛. The second
one, called 𝑆, is biased (ones are more likely than zeros) and corresponds to 𝑛
independent coin tossing where 1 appears with probability 𝑝 = 1/2 + 𝜀. In other

---

[previous page](page-069.md) · [next page](page-071.md) · [all pages](index.md)
