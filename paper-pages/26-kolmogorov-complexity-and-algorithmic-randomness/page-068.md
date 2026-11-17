---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 68
pages: [68]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "3.2. THE STRONG LAW OF LARGE NUMBERS 69 ∙ The definition does not change if we restrict ourselves to rational values of 𝜀 (or even let 𝜀 = 2−𝑘 for…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 68 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 68 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

3.2. THE STRONG LAW OF LARGE NUMBERS 69
∙ The definition does not change if we restrict ourselves to rational values
of 𝜀 (or even let 𝜀 = 2−𝑘 for integer 𝑘).
∙ Any subset of a null set is a null set.
∙ A finite or countable union of null sets is a null set. (Indeed, to cover the
union by a family of intervals of total measure less than 𝜀, we combine
the covers of its parts that have measure less than 𝜀/2, 𝜀/4, 𝜀/8 etc.).
∙ Assume that 𝑝 is chosen in such a way that any singleton is a null set
(it is equivalent to the following property: for any infinite sequence 𝜔 =
𝜔0𝜔1𝜔2 . . . the limit of 𝑝(𝜔0 . . . 𝜔𝑛) (as 𝑛 → ∞) equals 0). Then every
finite or countable set is a null set.
A uniform measure on Ω assigns to each interval Ω𝑥 the number 2−𝑙(𝑥):
𝑝(𝑥) = 2−𝑛 for all strings 𝑥 of length 𝑛.
The uniform measure is closely related to the standard measure on R (or, more
precisely, on [0, 1]). Formally, the measure of a set 𝐴 ⊂ Ω is equal to the measure
of the set of reals whose binary expansions are elements of 𝐴. (In fact, the cor-
respondence between infinite binary fractions and reals in [0, 1] is not a bijection,
since numbers of the form 𝑘/2𝑙 for integer 𝑘 and 𝑙 have two representations: e.g.,
0.01111 . . . = 0.10000 . . . But this happens only for a countable family of reals and
measure theory easily ignores this.)
Indeed, the reals whose binary expansions start with 𝑥, form an interval, and
the length of this interval is 2−𝑛 where 𝑛 is the length of 𝑥. This implies that for
every interval 𝐼 ⊂ [0, 1] the uniform measure of the sequences that represent reals
in 𝐼 is equal to the length of the interval 𝐼.
Probability theory describes the uniform distribution as the probability distri-
bution for the outcomes of independent fair coin tossing. Indeed, for 𝑛 independent
fair coin tossings all 2𝑛 binary strings of length 𝑛 appear with the same probability
2−𝑛. The set Ω𝑥 is the event “a random sequence of zeros and ones starts with 𝑥”,
and this event has probability 2−𝑙(𝑥).
Similarly, we may consider a biased coin assuming that coin tossings are still in-
dependent. The corresponding measure (probability distribution) is called Bernoulli
measure (or Bernoulli distribution) with parameters 𝑞, 𝑝 (probabilities of 0 and 1
respectively; we assume that 𝑝, 𝑞 > 0, and 𝑝 + 𝑞 = 1).
With respect to this distribution, the event “sequence 𝜔 starts with a string
𝑥” has probability 𝑞𝑢𝑝𝑣 where 𝑢 and 𝑣 are the numbers of zeros and ones in 𝑥. In
other terms, we consider a function
𝑥 ↦ → 𝑞𝑢(𝑥)𝑝𝑣(𝑥)
where 𝑢(𝑥) and 𝑣(𝑥) stand for the numbers of zeros and ones in 𝑥, respectively. (It
is easy to check that this function has the additivity property.)
### 3.2. The Strong Law of Large Numbers
To see all these notions in action, let us state and prove the so-called Strong
Law of Large Numbers.
Fix some 𝑝, 𝑞 > 0 such that 𝑝 + 𝑞 = 1. Let 𝐴𝑝 be the set of all infinite sequences
𝜔0𝜔1𝜔2 . . . of zeros and ones such that limit frequency of ones exists and is equal
to 𝑝, i.e.,
lim
𝑛→∞
𝜔0 + 𝜔1 + . . . + 𝜔𝑛−1
𝑛 = 𝑝.

---

[previous page](page-067.md) · [next page](page-069.md) · [all pages](index.md)
