---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 61
pages: [61]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "Regression In regression problems we are interested in learning how the values y1, . . . , yn of a regression variable Y depend on the values x1, . .…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 61 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 61 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

Regression In regression problems we are interested in learning how the values y1, . . . , yn of a regression variable Y depend on the values x1, . . . , xn of the regressor variable X. We assume or hope that there exists some function h : X →Y so that h(X) predicts the value Y reasonably well, and we want to learn such an h from data. To this end, we assume a set of candidate predictors (functions) H. In Example 1.2, we took H to be the set of all polynomials. In the standard formulation of this problem, we take h to express that

Yi = h(Xi) + Zi, (2.38)

where the Zi are i.i.d. Gaussian random variables with mean 0 and some variance σ2, independent of Xi. That is, we assume Gaussian noise: (2.38) implies that the conditional density of y1, . . . , yn, given x1, . . . , xn, is equal to the product of n Gaussian densities:

n

Pn

i=1(yi −h(xi))2

 1

P(yn | xn, σ, h) =

√

exp

−

. (2.39)

2σ2

2πσ

With this choice, the log-likelihood becomes a linear function of the squared error:

n X

−log P(yn | xn, σ, h) = 1

(yi −h(xi))2 + n

2 log 2πσ2. (2.40)

2σ2

i=1

Let us now assume that H = ∪k≥1H(k) where for each k, H(k) is a set of functions h : X →Y. For example, H(k) may be the set of k-th degree polynomials.

With each model H(k) we can associate a set of densities (2.39), one for each (h, σ2) with h ∈H(k) and σ2 ∈R+. Let M(k) be the resulting set of conditional distributions. Each P(· | h, σ2) ∈M(k) is identified by the parameter vector (α0, . . . , αk, σ2) so that h(x):= Pk

j=0 αjxj. By Section 2.7.1, (2.8) MDL tells us to select the model minimizing

−log ¯P(yn | M(k), xn) + L(k) (2.41)

where we may take L(k) = 2 log k + 1, and ¯P(· | M(k), ·) is now a conditional universal model with small minimax regret. (2.41) ignores the codelength of x1, . . . , xn. Intuitively, this is because we are only interested in learning how y depends on x; therefore, we do not care how many bits are needed to encode x. Formally, this may be understood as follows: we really are encoding the x-values as well, but we do so using a fixed code that does not depend on the hypothesis h under consideration. Thus, we are really trying to find the model M(k) minimizing

−log ¯P(yn | M(k), xn) + L(k) + L′(xn)

where L′ represents some code for X n. Since this codelength does not involve k, it can be dropped from the minimization; see Figure 2.5. We will not go into the precise definition of ¯P(yn | M(k), xn). Ideally, it should be an NML distribution, but just as in Example 2.20, this NML distribution is not well-defined. We can get reasonable alternative universal models after all using any of the methods described in Section 2.7.2; see \[Barron, Rissanen, and Yu 1998\] and \[Rissanen 2000\] for details.

62

---

[previous page](page-060.md) · [next page](page-062.md) · [all pages](index.md)
