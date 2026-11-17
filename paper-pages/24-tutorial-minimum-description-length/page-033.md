---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 33
pages: [33]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "Taking the derivative of (2.7) with respect to θ, we see that for fixed xn, the loglikelihood is maximized by setting the probability of 1 equal to…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 33 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 33 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

Taking the derivative of (2.7) with respect to θ, we see that for fixed xn, the loglikelihood is maximized by setting the probability of 1 equal to the observed frequency. Since the logarithm is a monotonically increasing function, the likelihood is maximized at the same value: the ML estimator is given by ˆθ(xn) = n\[1\]/n.

Similarly, the first-order Markov model B(1) can be parameterized by a vector θ = (θ\[1|0\], θ\[1|1\]) ∈\[0, 1\]2 together with a starting state in {0, 1}. Here θ\[1|j\] represents the probability of observing a 1 following the symbol j. The log-likelihood is given by

log P(xn | θ) = n\[1|1\] log θ\[1|1\] + n\[0|1\] log(1 −θ\[1|1\]) + n\[1|0\] log θ\[1|0\] + n\[0|0\] log(1 −θ\[1|0\]),

n\[i|j\] denoting the number of times outcome i is observed in state (previous outcome) j. This is maximized by setting ˆθ = (ˆθ\[1|0\], ˆθ\[1|1\]), with ˆθ\[i|j\] = n\[i|j\] = n\[ji\]/n\[j\] set to the conditional frequency of i preceded by j. In general, a k-th order Markov chain has 2k parameters and the corresponding likelihood is maximized by setting the parameter θ\[i|j\] equal to the number of times i was observed in state j divided by the number of times the chain was in state j.

Suppose now we are given data D = xn and we want to find the Markov chain that best explains D. Since we do not want to restrict ourselves to chains of fixed order, we run a large risk of overfitting: simply picking, among all Markov chains of each order, the ML Markov chain that maximizes the probability of the data, we typically end up with a chain of order n −1 with starting state given by the sequence x1, . . . , xn−1, and P(Xn = xn | Xn−1 = xn−1) = 1. Such a chain will assign probability 1 to xn. Below we show that MDL makes a more reasonable choice.

## 2.4 Crude MDL

Based on the information-theoretic (Section 2.2) and statistical (Section 2.3) preliminaries discussed before, we now formalize a first, crude version of MDL.

Let M be a class of probabilistic sources (not necessarily Markov chains). Suppose we observe a sample D = (x1, . . . , xn) ∈X n. Recall ‘the crude8 two-part code MDL Principle’ from Section 1.3, page 11:

Crude9, Two-part Version of MDL Principle Let H(1), H(2), . . . be a set of candidate models. The best point hypothesis H ∈ H(1) ∪H(2) ∪. . . to explain data D is the one which minimizes the sum L(H) + L(D|H), where

• L(H) is the length, in bits, of the description of the hypothesis; and

• L(D|H) is the length, in bits, of the description of the data when encoded with the help of the hypothesis.

The best model to explain D is the smallest model containing the selected H.

34

---

[previous page](page-032.md) · [next page](page-034.md) · [all pages](index.md)
