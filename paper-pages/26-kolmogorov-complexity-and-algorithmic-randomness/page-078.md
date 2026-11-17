---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 78
pages: [78]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "3.4. PROPERTIES OF MARTIN-L ¨OF RANDOMNESS 79 Ω) if it does not belong to any effectively null set. For this notion B. Kjos-Hansen suggested the name…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 78 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 78 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

3.4. PROPERTIES OF MARTIN-L ¨OF RANDOMNESS 79
Ω) if it does not belong to any effectively null set. For this notion B. Kjos-Hansen
suggested the name Hippocratic randomness (and P. G´acs suggested more neutral
name blind randomness). This is not the only existing notion of randomness with
respect to non-computable measures; we do not go into details here and mention
only that one can use uniform tests of randomness (following Levin and G´acs, see
[13]).
78 Prove that for an upper semicomputable measure there exists the largest
effectively null set. (We do not assume here that the measure of the entire Ω equals
1, otherwise all upper semicomputable measures would be computable.)
79 Construct an example of a (non-computable) measure for which there is no
largest effectively null set. [Hint: Construct a measure that has two properties at
the same time: (1) every computable sequence forms a singleton that is an effective
null set (moreover, some prefix already has measure zero); (2) every algorithm that
pretends to generate an effectively null set, either gives an interval whose measure
is too big, or does not cover some computable sequence. This can be done by a
diagonal argument where we consider one by one all the computable sequences and
all possible algorithms.]
80 Show that there is a non-computable measure for which there exists the
largest effectively null set. [Hint: consider a non-computable measure that is very
close to the uniform one (say, at most twice bigger and at most twice smaller for
all sets).]
### 3.4. Properties of Martin-L¨of randomness
The Strong Law of Large Numbers also provides an example of an effective null
set (with respect to the uniform measure).
Theorem 32. A set of all bit sequences that do no have limit frequency 1/2 is
an effectively null set with respect to the uniform measure.
Proof. It is enough to prove that for every rational 𝜀 > 0 the set of all
sequences such that frequency of ones is greater than 1/2 + 𝜀 infinitely many times
(or less than 1/2 − 𝜀 infinitely many times) is an effective null set.
Indeed, the upper bound for the measure of this set achieved in the proof of
the Strong Law of Large Numbers in the previous section (Theorem 27, p. 70) is
effective: the set of intervals was the set of all sufficiently long strings with large
frequency deviation, and its total measure was effectively bounded by a tail of the
converging geometric series. 
The statement of this theorem can be reformulated as the property of individual
ML-random sequences:
Theorem 33. Let 𝜔 = 𝜔0𝜔1 . . . be a ML-random sequence with respect to the
uniform measure. Then
lim
𝑛→∞
𝜔0 + 𝜔1 + . . . + 𝜔𝑛−1
𝑛 = 1
2 .
The similar statement is true for arbitrary Bernoulli measure. Let 𝑝 and 𝑞 be
computable positive reals such that 𝑝 + 𝑞 = 1. Consider the Bernoulli measure
with parameters 𝑞 and 𝑝 (the sequence of independent coin tossing with success
probability 𝑝). It is easy to check that this is a computable measure (since 𝑝 and 𝑞
are computable).

---

[previous page](page-077.md) · [next page](page-079.md) · [all pages](index.md)
