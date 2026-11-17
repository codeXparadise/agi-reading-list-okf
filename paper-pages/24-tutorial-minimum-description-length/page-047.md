---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 47
pages: [47]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "Asymptotic Expansion of ¯Pnml and COMPn Let M be a k-dimensional parametric model. Under regularity conditions on M and the parameterization Θ →M, to…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 47 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 47 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

Asymptotic Expansion of ¯Pnml and COMPn Let M be a k-dimensional parametric model. Under regularity conditions on M and the parameterization Θ →M, to be detailed below, we obtain the following asymptotic expansion of COMPn \[Rissanen 1996; Takeuchi and Barron 1997; Takeuchi and Barron 1998; Takeuchi 2000\]:

COMPn(M) = k

2 log n

2π + log Z

p

|I(θ)|dθ + o(1). (2.21)

θ∈Θ

Here k is the number of parameters (degrees of freedom) in model M, n is the sample size, and o(1) →0 as n →∞. |I(θ)| is the determinant of the k × k Fisher information matrix18 I evaluated at θ. In case M is an i.i.d. model, I is given by

− ∂2

Iij(θ∗):=Eθ∗

log P(X|θ)

θ=θ∗.

∂θi∂θj

This is generalized to non-i.i.d. models as follows:

− ∂2

1

log P(Xn|θ)

Iij(θ∗):= lim

nEθ∗

θ=θ∗.

∂θi∂θj

n→∞

(2.21) only holds if the model M, its parameterization Θ and the sequence x1, x2, . . . all satisfy certain conditions. Specifically, we require:

1. COMPn(M) < ∞and R p

|I(θ)|dθ < ∞;

2. ˆθ(xn) does not come arbitrarily close to the boundary of Θ: for some ǫ > 0, for all large n, ˆθ(xn) remains farther than ǫ from the boundary of Θ.

3. M and Θ satisfy certain further conditions. A simple suﬃcient condition is that M be an exponential family \[Casella and Berger 1990\]. Roughly, this is a family that can be parameterized so that for all x, P(x | β) = exp(βt(x))f(x)g(β), where t : X →R is a function of X. The Bernoulli model is an exponential family, as can be seen by setting β := ln(1 −θ) −ln θ and t(x) = x. Also the multinomial, Gaussian, Poisson, Gamma, exponential, Zipf and many other models are exponential families; but, for example, mixture models are not.

More general conditions are given by Takeuchi and Barron \[1997, 1998, 2000\]. Essentially, if M behaves ‘asymptotically’ like an exponential family, then (2.21) still holds. For example, (2.21) holds for the Markov models and for AR and ARMA processes.

Example 2.17 \[Complexity of the Bernoulli Model\] The Bernoulli model B(0)

can be parameterized in a 1-1 way by the unit interval (Example 2.7). Thus, k = 1. An easy calculation shows that the Fisher information is given by θ(1 −θ). Plugging this into (2.21) and calculating

R p

|θ(1 −θ)|dθ gives

COMPn(B(0)) = 1

2 log n + 1

2 log π

2 −3 + o(1) = 1

2 log n −2.674251935 + o(1).

Computing the integral of the Fisher determinant is not easy in general. Hanson and Fu \[2004\] compute it for several practically relevant models.

48

---

[previous page](page-046.md) · [next page](page-048.md) · [all pages](index.md)
