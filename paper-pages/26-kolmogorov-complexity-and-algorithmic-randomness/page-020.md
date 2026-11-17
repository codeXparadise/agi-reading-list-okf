---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 20
pages: [20]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "SOME APPLICATIONS OF KOLMOGOROV COMPLEXITY 21 only zeros or equals 0101010101 . . . (zeros and ones alternate), then we definitely will conclude that…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 20 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 20 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

SOME APPLICATIONS OF KOLMOGOROV COMPLEXITY 21
only zeros or equals 0101010101 . . . (zeros and ones alternate), then we definitely
will conclude that the generator is bad. Why?
Usual explanation: the probability of obtaining thousand zeros is negligible
(2−1000) provided the coin is fair. Therefore the conjecture of a fair coin is refuted
by the experiment.
The problem with this explanation is that we do not always reject the generator:
there should be some sequence 𝛼 of thousand zeros and ones which is consistent
with this conjecture. Note, however, that the probability of obtaining the sequence
𝛼 as a result of fair coin tossing is also 2−1000. So what is the reason behind our
complaints? What is the difference between the sequence of thousand zeros and
the sequence 𝛼?
The reason is revealed when we compare Kolmogorov complexities of these
sequences.
Proving theorems of probability theory. As an example, consider the
Strong Law of Large Numbers. It claims that for almost all (according to the the
uniform Bernoulli probability distribution) infinite binary sequences the limit of
frequencies of 1s in their initial segments equals 1/2.
More formally, let Ω be the set of all infinite sequences of zeros and ones.
The uniform Bernoulli measure on Ω is defined as follows. For every finite binary
string 𝑥 consider the set Ω𝑥 consisting of all infinite sequences that start with 𝑥.
For example, ΩΛ = Ω. The measure of Ω𝑥 is equal to 2−𝑙(𝑥). For example, the
measure of the set Ω01 that consists of all sequences starting with 01, equals 1/4.
For each sequence 𝜔 = 𝜔0𝜔1𝜔2 . . . consider the limit of the frequencies of 1s in
the prefixes of 𝜔, that is,
lim
𝑛→∞
𝜔0 + 𝜔1 + . . . + 𝜔𝑛−1
𝑛
We say that 𝜔 satisfies the Strong Law of Large Numbers (SLLN) if this limit exists
and is equal to 1/2. For instance, the sequence 010101 . . . , having period 2, satisfies
the SLLN and the sequence 011011011 . . ., having period 3, does not.
The Strong Law of Large Numbers says that the set of sequences that do not
satisfy SLLN has measure 0. Recall that a set 𝐴 ⊂ Ω has measure 0 if for all 𝜀 > 0
there is a sequence of strings 𝑥0, 𝑥1, 𝑥2, . . . such that
𝐴 ⊂ Ω𝑥0 ∪ Ω𝑥1 ∪ Ω𝑥2 ∪ . . .
and the sum of the series
2−𝑙(𝑥0) + 2−𝑙(𝑥1) + 2−𝑙(𝑥2) + . . .
(the sum of the measures of Ω𝑥𝑖 ) is less than 𝜀.
One can prove SLLN using the notion of a Martin-L¨of random sequence men-
tioned above. The proof consists of two parts. First, we show that every Martin-L¨of
random sequence satisfies SLLN. This can be done using Levin–Schnorr random-
ness criterion (if the limit does not exist or differs from 1/2, then the complexity
of some prefix is less than it should be for a random sequence).
The second part is rather general and does not depend on the specific law of
probability theory. We prove that the set of all Martin-L¨of non-random sequences
has measure zero. This implies that the set of sequences that do not satisfy SLLN
is included in a set of measure 0 and hence has measure 0 itself.
The notion of a random sequence is philosophically interesting in its own right.
In the beginning of XXth century Richard von Mises suggested to use this notion

---

[previous page](page-019.md) · [next page](page-021.md) · [all pages](index.md)
