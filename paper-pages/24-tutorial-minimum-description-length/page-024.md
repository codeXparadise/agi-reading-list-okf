---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 24
pages: [24]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "distributed according to P, then the code with lengths −log P achieves the minimum expected codelength. Throughout the section we give examples…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 24 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 24 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

distributed according to P, then the code with lengths −log P achieves the minimum expected codelength. Throughout the section we give examples relating our findings to our discussion of regularity and compression in Section 1.2 of Chapter 1.

Preliminaries and Notational Conventions - Codes We use log to denote logarithm to base 2. For real-valued x we use ⌈x⌉to denote the ceiling of x, that is, x rounded up to the nearest integer. We often abbreviate x1, . . . , xn to xn. Let X be a finite or countable set. A code for X is defined as a 1-to-1 mapping from X to ∪n≥1{0, 1}n. ∪n≥1{0, 1}n is the set of binary strings (sequences of 0s and 1s) of length 1 or larger. For a given code C, we use C(x) to denote the encoding of x. Every code C induces a function LC : X →N called the codelength function. LC(x) is the number of bits (symbols) needed to encode x using code C.

Our definition of code implies that we only consider lossless encoding in MDL1: for any description z it is always possible to retrieve the unique x that gave rise to it. More precisely, because the code C must be 1-to-1, there is at most one x with C(x) = z. Then x = C−1(z), where the inverse C−1 of C is sometimes called a ‘decoding function’ or ‘description method’.

Preliminaries and Notational Conventions - Probability Let P be a probability distribution defined on a finite or countable set X. We use P(x) to denote the probability of x, and we denote the corresponding random variable by X. If P is a function on finite or countable X such that P

x P(x) < 1, we call P a defective distribution. A defective distribution may be thought of as a probability distribution that puts some of its mass on an imagined outcome that in reality will never appear.

A probabilistic source P is a sequence of probability distributions P (1), P (2), . . . on X 1, X 2, . . . such that for all n, P (n) and P (n+1) are compatible: P (n) is equal to the ‘marginal’ distribution of P (n+1) restricted to n outcomes. That is, for all xn ∈X n, P (n)(xn) = P

y∈X P (n+1)(xn, y). Whenever this cannot cause any confusion, we write P(xn) rather than P (n)(xn). A probabilistic source may be thought of as a probability distribution on infinite sequences2. We say that the data are i.i.d. (independently and identically distributed) under source P if for each n, xn ∈X n, P(xn) = Qn

i=1 P(xi).

2.2.1 Prefix Codes

In MDL we only work with a subset of all possible codes, the so-called prefix codes. A prefix code3 is a code such that no codeword is a prefix of any other codeword. For example, let X = {a, b, c}. Then the code C1 defined by C1(a) = 0, C1(b) = 10, C1(c) = 11 is prefix. The code C2 with C2(a) = 0, C2(b) = 10 and C2(c) = 01, while allowing for lossless decoding, is not a prefix code since 0 is a prefix of 01. The prefix requirement is natural, and nearly ubiquitous in the data compression literature. We now explain why.

Example 2.1 Suppose we plan to encode a sequence of symbols (x1, . . . , xn) ∈X n.

25

---

[previous page](page-023.md) · [next page](page-025.md) · [all pages](index.md)
