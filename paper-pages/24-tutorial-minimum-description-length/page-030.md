---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 30
pages: [30]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "The P that corresponds to L minimizes expected codelength Let P be a distribution on (finite, countable or continuous-valued) Z and let L be defined…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 30 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 30 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

The P that corresponds to L minimizes expected codelength Let P be a distribution on (finite, countable or continuous-valued) Z and let L be defined by

L:= arg min

EP \[L(Z)\]. (2.5)

L∈LZ

Then L exists, is unique, and is identical to the codelength function corresponding to P, with lengths L(z) = −log P(z).

Figure 2.3: The second most important observation of this tutorial.

Whenever in the following we make a general statement about sample spaces X and distributions P, X may be finite, countable or any subset of Rl, for any integer l ≥1, and P(x) represents the probability mass function or density of P, as the case may be. In the continuous case, all sums should be read as integrals. The correspondence between probability distributions and codes may be extended to distributions on continuous-valued X: we may think of L(xn) := −log P(xn) as a code-length function corresponding to Z = X n encoding the values in X n at unit precision; here P(xn) is the density of xn according to P. We refer to \[Cover and Thomas 1991\] for further details.

2.2.3 The Information Inequality - Codelengths & Probabilities, II

In the previous subsection, we established the first fundamental relation between probability distributions and codelength functions. We now discuss the second relation, which is nearly as important.

In the correspondence to codelength functions, probability distributions were treated as mathematical objects and nothing else. That is, if we decide to use a code C to encode our data, this definitely does not necessarily mean that we assume our data to be drawn according to the probability distribution corresponding to L: we may have no idea what distribution generates our data; or conceivably, such a distribution may not even exist6. Nevertheless, if the data are distributed according to some distribution P, then the code corresponding to P turns out to be the optimal code to use, in an expected sense – see Figure 2.3. This result may be recast as follows: for all distributions P and Q with Q̸ = P,

EP \[−log Q(X)\] > EP \[−log P(X)\].

In this form, the result is known as the information inequality. It is easily proved using concavity of the logarithm \[Cover and Thomas 1991\].

31

---

[previous page](page-029.md) · [next page](page-031.md) · [all pages](index.md)
