---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 34
pages: [34]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "In this section, we implement this crude MDL Principle by giving a precise definition of the terms L(H) and L(D|H). To make the first term precise,…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 34 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 34 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

In this section, we implement this crude MDL Principle by giving a precise definition of the terms L(H) and L(D|H). To make the first term precise, we must design a code C1 for encoding hypotheses H such that L(H) = LC1(H). For the second term, we must design a set of codes C2,H (one for each H ∈M) such that for all D ∈X n, L(D|H) = LC2,H(D). We start by describing the codes C2,H.

2.4.1 Description Length of Data given Hypothesis

Given a sample of size n, each hypothesis H may be viewed as a probability distribution on X n. We denote the corresponding probability mass function by P(· | H). We need to associate with P(· | H) a code, or really, just a codelength function for X n. We already know that there exists a code with length function L such that for all xn ∈X n, L(xn) = −log P(xn | H). This is the code that we will pick. It is a natural choice for two reasons:

1. With this choice, the code length L(xn | H) is equal to minus the log-likelihood of xn according to H, which is a standard statistical notion of ‘goodness-of-fit’.

2. If the data turn out to be distributed according to P, then the code L(· | H) will uniquely minimize the expected code length (Section 2.2).

The second item implies that our choice is, in a sense, the only reasonable choice10. To see this, suppose M is a finite i.i.d. model containing, say, M distributions. Suppose we assign an arbitrary but finite code length L(H) to each H ∈M. Suppose X1, X2, . . . are actually distributed i.i.d. according to some ‘true’ H∗∈M. By the reasoning of Example 2.6, we see that MDL will select the true distribution P(· | H∗) for all large n, with probability 1. This means that MDL is consistent for finite M. If we were to assign codes to distributions in some other manner not satisfying L(D | H) = −log P(D | H), then there would exist distributions P(· | H) such that L(D|H)̸ = −log P(D|H). But by Figure 2.1, there must be some distribution P(· | H′) with L(·|H) = −log P(· | H′). Now let M = {H, H′} and suppose data are distributed according to P(· | H′). Then, by the reasoning of Example 2.6, MDL would select H rather than H′ for all large n! Thus, MDL would be inconsistent even in this simplest of all imaginable cases – there would then be no hope for good performance in the considerably more complex situations we intend to use it for11.

2.4.2 Description Length of Hypothesis

In its weakest and crudest form, the two-part code MDL Principle does not give any guidelines as to how to encode hypotheses (probability distributions). Every code for encoding hypotheses is allowed, as long as such a code does not change with the sample size n.

To see the danger in allowing codes to depend on n, consider the Markov chain example: if we were allowed to use diﬀerent codes for diﬀerent n, we could use, for each n, a code assigning a uniform distribution to all Markov chains of order n −1

35

---

[previous page](page-033.md) · [next page](page-035.md) · [all pages](index.md)
