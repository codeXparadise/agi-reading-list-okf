---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 29
pages: [29]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "calculation gives 2−2 log x−1 = 1 x−2 < 1 2 + 1 1 X X X X P(x) = x(x −1) = 1, 2 2 x∈1,2,... x∈1,2,... x∈1,2,... x=2,3,... so that P is a (defective)…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 29 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 29 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

calculation gives

2−2 log x−1 = 1

x−2 < 1

2 + 1

1

X

X

X

X

P(x) =

x(x −1) = 1,

2

2

x∈1,2,...

x∈1,2,...

x∈1,2,...

x=2,3,...

so that P is a (defective) probability distribution. Thus, by our new definition (Figure 2.2), there exists a prefix code with, for all k, L(k) = −log P(k) = 2 log k + 1. We call the resulting code the ‘simple standard code for the integers’. In Section 2.5 we will see that it is an instance of a so-called ‘universal’ code.

The idea can be refined to lead to codes with lengths log k + O(log log k); the ‘best’ possible refinement, with code lengths L(k) increasing monotonically but as slowly as possible in k, is known as ‘the universal code for the integers’ \[Rissanen 1983\]. However, for our purposes in this tutorial, it is good enough to encode integers k with 2 log k + 1 bits.

Example 2.5 \[Example 1.2 and 2.2, Continued.\] We are now also in a position to prove the third and final claim of Examples 1.2 and 2.2. Consider the three sequences (2.1), (2.2) and (2.3) on page 26 again. It remains to investigate how much the third sequence can be compressed. Assume for concreteness that, before seeing the sequence, we are told that the sequence contains a fraction of 1s equal to 1/5 + ǫ for some small unknown ǫ. By the Kraft inequality, Figure 2.1, for all distributions P, there exists some code on sequences of length n such that for all xn ∈X n, L(xn) = ⌈−log P(xn)⌉. The fact that the fraction of 1s is approximately equal to 1/5 suggests to model xn as independent outcomes of a coin with bias 1/5-th. The corresponding distribution P0 satisfies

n\[1\]4

n\[0\]

1

1

log 1

5 − 4

log 4

−log P0(xn) = log

5 + ǫ 

5 −ǫ 

5 

= n

−

=

5

5

n\[log 5 −8

5 + 2ǫ\],

where n\[j\] denotes the number of occurrences of symbol j in xn. For small enough ǫ, the part between brackets is smaller than 1, so that, using the code L0 with lengths −log P0, the sequence can be encoded using αn bits were α satisfies 0 < α < 1. Thus, using the code L0, the sequence can be compressed by a linear amount, if we use a specially designed code that assigns short codelengths to sequences with about four times as many 0s than 1s.

We note that after the data (2.3) has been observed, it is always possible to design a code which uses arbitrarily few bits to encode xn - the actually observed sequence may be encoded as ‘1’ for example, and no other sequence is assigned a codeword. The point is that with a code that has been designed before seeing the actual sequence, given only the knowledge that the sequence will contain approximately four times as many 0s than 1s, the sequence is guaranteed to be compressed by an amount linear in n.

Continuous Sample Spaces How does the correspondence work for continuousvalued X? In this tutorial we only consider P on X such that P admits a density5.

30

---

[previous page](page-028.md) · [next page](page-030.md) · [all pages](index.md)
