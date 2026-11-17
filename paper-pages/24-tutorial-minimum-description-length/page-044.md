---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 44
pages: [44]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "data D = (x1, . . . , xn) and two models M(1) and M(2) such that COMPn(M(1)) and COMPn(M(2)) (Equation 2.17) are both finite. For example, we could…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 44 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 44 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

data D = (x1, . . . , xn) and two models M(1) and M(2) such that COMPn(M(1)) and COMPn(M(2)) (Equation 2.17) are both finite. For example, we could have some binary data and M(1) and M(2) are the first- and second-order Markov models (Example 2.7), both considered possible explanations for the data. We show how to deal with an infinite number of models and/or models with infinite COMPn in Section 2.7.

Denote by ¯Pnml(· | M(j)) the NML distribution on X n corresponding to model M(j). Refined MDL tells us to pick the model M(j) maximizing the normalized maximum likelihood ¯Pnml(D | M(j)), or, by (2.18), equivalently, minimizing

−log ¯Pnml(D | M(j)) = −log P(D | ˆθ(j)(D)) + COMPn(M(j)) (2.20)

From a coding theoretic point of view, we associate with each M(j) a code with lengths

¯Pnml(· | M(j)), and we pick the model minimizing the codelength of the data. The codelength −log ¯Pnml(D | M(j)) has been called the stochastic complexity of the data D relative to model M(j) \[Rissanen 1987\], whereas COMPn(M(j)) is called the parametric complexity or model cost of M(j) (in this survey we simply call it ‘complexity’). We have already indicated in the previous section that COMPn(M(j)) measures something like the ‘complexity’ of model M(j). On the other hand, −log P(D | ˆθ(j)(D)) is minus the maximized log-likelihood of the data, so it measures something like (minus) fit or error – in the linear regression case, it can be directly related to the mean squared error, Section 2.8. Thus, (2.20) embodies a trade-oﬀbetween lack of fit (measured by minus log-likelihood) and complexity (measured by COMPn(M(j))). The confidence in the decision is given by the codelength diﬀerence

−log ¯Pnml(D | M(1)) −\[−log ¯Pnml(D | M(2))\]

.

In general, −log ¯Pnml(D | M) can only be evaluated numerically – the only exception this author is aware of is when M is the Gaussian family, Example 2.20. In many cases even numerical evaluation is computationally problematic. But the re-interpretations of ¯Pnml we provide below also indicate that in many cases, −log ¯P(D | M) is relatively easy to approximate.

Example 2.15 \[Refined MDL and GLRT\] Generalized likelihood ratio testing \[Casella and Berger 1990\] tells us to pick the M(j) maximizing log P(D | ˆθ(j)(D)) + c where c is determined by the desired type-I and type-II errors. In practice one often applies a naive variation17, simply picking the model M(j) maximizing log P(D |

ˆθ(j)(D)). This amounts to ignoring the complexity terms COMPn(M(j)) in (2.20): MDL tries to avoid overfitting by picking the model maximizing the normalized rather than the ordinary likelihood. The more distributions in M that fit the data well, the larger the normalization term.

The hope is that the normalization term COMPn(M(j)) strikes the right balance between complexity and fit. Whether it really does depends on whether COMPn is

45

---

[previous page](page-043.md) · [next page](page-045.md) · [all pages](index.md)
