---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 27
pages: [27]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "Probability Mass Functions correspond to Codelength Functions Let Z be a finite or countable set and let P be a probability distribution on Z. Then…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 27 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 27 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

Probability Mass Functions correspond to Codelength Functions Let Z be a finite or countable set and let P be a probability distribution on Z. Then there exists a prefix code C for Z such that for all z ∈Z, LC(z) = ⌈−log P(z)⌉. C is called the code corresponding to P. Similarly, let C′ be a prefix code for Z. Then there exists a (possibly defective) probability distribution P ′ such that for all z ∈Z, −log P ′(z) = LC′(z). P ′ is called the probability distribution corresponding to C′.

Moreover C′ is a complete prefix code iﬀP is proper (P

z P(z) = 1).

Thus, large probability according to P means small code length according to the code corresponding to P and vice versa. We are typically concerned with cases where Z represents sequences of n outcomes; that is, Z = X n (n ≥1) where X is the sample space for one observation.

Figure 2.1: The most important observation of this tutorial.

element. We can arrive at a code corresponding to PU as follows. First, order and number the elements in Z as 0, 1, . . . , M −1. Then, for each z with number j, set C(z) to be equal to j represented as a binary number with ⌈log M⌉bits. The resulting code has, for all z ∈Z, LC(z) = ⌈log M⌉= ⌈−log PU(z)⌉. This is a code corresponding to PU (Figure 2.1). In general, there exist several codes corresponding to PU, one for each ordering of Z. But all these codes share the same length function LU(z) := ⌈−log PU(z)⌉.; therefore, LU(z) is the unique codelength function corresponding to PU.

For example, if M = 4, Z = {a, b, c, d}, we can take C(a) = 00, C(b) = 01, C(c) = 10, C(d) = 11 and then LU(z) = 2 for all z ∈Z. In general, codes corresponding to uniform distributions assign fixed lengths to each z and are called fixed-length codes. To map a non-uniform distribution to a corresponding code, we have to use a more intricate construction \[Cover and Thomas 1991\].

In practical applications, we almost always deal with probability distributions P and strings xn such that P(xn) decreases exponentially in n; for example, this will typically be the case if data are i.i.d., such that P(xn) = Q P(xi). Then −log P(xn) increases linearly in n and the eﬀect of rounding oﬀ−log P(xn) becomes negligible. Note that the code corresponding to the product distribution of P on X n does not have to be the n-fold extension of the code for the original distribution P on X – if we were to require that, the eﬀect of rounding oﬀwould be on the order of n . Instead, we directly design a code for the distribution on the larger space Z = X n. In this way, the eﬀect of rounding changes the codelength by at most 1 bit, which is truly negligible. For this and other4

reasons, we henceforth simply neglect the integer requirement for codelengths. This simplification allows us to identify codelength functions and (defective) probability

28

---

[previous page](page-026.md) · [next page](page-028.md) · [all pages](index.md)
