---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 69
pages: [69]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "70 3. MARTIN-L ¨OF RANDOMNESS Theorem 27. The set 𝐴𝑝 has measure 1 with respect to Bernoulli distribution with parameters 𝑝 and 𝑞. In other terms,…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 69 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 69 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

70 3. MARTIN-L ¨OF RANDOMNESS
Theorem 27. The set 𝐴𝑝 has measure 1 with respect to Bernoulli distribution
with parameters 𝑝 and 𝑞.
In other terms, the complement of 𝐴𝑝, i.e., the set of all sequences that either
do not have limit frequency at all or have a limit frequency different from 𝑝, is a
null set (according to this distribution).
Proof. We prove this theorem for the uniform case (i.e., for 𝑝 = 𝑞 = 1/2) by
an explicit calculation. The general case is left as an exercise (see also Section 9.6).
Let us consider first a finite number of coin tossings and fix some 𝑛. All
binary strings of length 𝑛 have the same probability. We claim that most of them
have approximately 𝑛/2 ones. Assume that some threshold 𝜀 is fixed. How many
sequences have more than (1/2 + 𝜀)𝑛 ones? The answer can be found using the
Pascal triangle: we have to sum up all the terms in the 𝑛th row starting from some
point that is slightly on the right of the midpoint. In this part we have a decreasing
sequence of less than 𝑛 terms, so the sum in question is bounded by the first term
multiplied by 𝑛. (We do not need to be very accurate in our bounds and ignore
factors that are polynomial in 𝑛. So we can omit the factor 𝑛 in our bound.)
The first term of the sum is the binomial coefficient
𝑛!
𝑘!(𝑛 − 𝑘)! ,
where 𝑘 is the smallest integer not less than (1/2 + 𝜀)𝑛. We use the Stirling’s
approximation:
𝑚! =√︀ (2𝜋 + 𝑜(1))𝑚
(︁
 
𝑚
𝑒
)︁
𝑚
,
where 𝑒 is the base of natural logarithms. Ignoring polynomial (in 𝑛) factors and
using the notation 𝑢 = 𝑘/𝑛, 𝑣 = (𝑛 − 𝑘)/𝑛, we get
𝑛!
𝑘!(𝑛 − 𝑘)! ≈ (𝑛/𝑒)𝑛
(𝑘/𝑒)𝑘((𝑛 − 𝑘)/𝑒)𝑛−𝑘 = 𝑛𝑛
𝑘𝑘(𝑛 − 𝑘)𝑛−𝑘 =
= 𝑛𝑛
(𝑢𝑛)𝑢𝑛(𝑣𝑛)𝑣𝑛 = 1
𝑢𝑢𝑛𝑣𝑣𝑛 = 2𝐻(𝑢,𝑣)𝑛,
where
𝐻(𝑢, 𝑣) = −𝑢 log 𝑢 − 𝑣 log 𝑣.
The value 𝐻(𝑢, 𝑣) is called the Shannon entropy of the random variable that has
two values whose probabilities are 𝑢 and 𝑣. (We study the Shannon entropy in
Chapter 7.) Figure 1 shows the corresponding graph (note that 𝑣 = 1 − 𝑢). It
is easy to check that 𝐻(𝑢, 1 − 𝑢) achieves its maximal value (equal to 1) only
at 𝑢 = 1/2.
Now we see that the number of binary strings of length 𝑛 that have frequency of
ones greater than (1/2 + 𝜀) does not exceed poly(𝑛)2𝐻(1/2+𝜀,1/2−𝜀)𝑛 and therefore
is bounded by 2𝑐𝑛+𝑜(𝑛), where 𝑐 is some constant less than 1 (depending on 𝜀).
Therefore, the fraction of these strings (among all strings of length 𝑛) exponentially
decreases as 𝑛 increases. The same is true for the strings that have frequency of
ones less than (1/2 − 𝜀).
Let us see where we are. For each fixed 𝜀 > 0 we have proved the following
statement:

---

[previous page](page-068.md) · [next page](page-070.md) · [all pages](index.md)
