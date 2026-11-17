---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 41
pages: [41]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "Bayes is Better than Two-part The Bayesian model is in a sense superior to the two-part code. Namely, in the two-part code we first encode an element…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 41 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 41 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

Bayes is Better than Two-part The Bayesian model is in a sense superior to the two-part code. Namely, in the two-part code we first encode an element of M or its parameter set Θ using some code L0. Such a code must correspond to some ‘prior’ distribution W on M so that the two-part code gives codelengths

¯L2-p(xn) = min

θ∈Θ −log P(xn|θ) −log W(θ) (2.14)

where W depends on the specific code L0 that was used. Using the Bayes code with prior W, we get as in (2.13),

P(xn | θ)W(θ) ≤min

−log ¯PBayes(xn) = −log

X

θ∈Θ −log P(xn|θ) −log W(θ).

θ∈Θ

The inequality becomes strict whenever P(xn|θ) > 0 for more than one value of θ. Comparing to (2.14), we see that in general the Bayesian code is preferable over the two-part code: for all xn it never assigns codelengths larger than ¯L2-p(xn), and in many cases it assigns strictly shorter codelengths for some xn. But this raises two important issues: (1) what exactly do we mean by ‘better’ anyway? (2) can we say that ‘some prior distributions are better than others’? These questions are answered below.

2.5.3 NML as an Optimal Universal Model

We can measure the performance of universal models relative to a set of candidate sources M using the regret:

Definition 2.13 \[Regret\] Let M be a class of probabilistic sources. Let ¯P be a probability distribution on X n ( ¯P is not necessarily in M). For given xn, the regret of ¯P relative to M is defined as

−log ¯P(xn) −min

P ∈M{−log P(xn)}. (2.15)

The regret of ¯P relative to M for xn is the additional number of bits needed to encode xn using the code/distribution ¯P, as compared to the number of bits that had been needed if we had used code/distribution in M that was optimal (‘best-fitting’) with hind-sight. For simplicity, from now on we tacitly assume that for all the models M we work with, there is a single ˆθ(xn) maximizing the likelihood for every xn ∈X n. In that case (2.15) simplifies to

−log ¯P(xn) −{−log P(xn | ˆθ(xn))}.

We would like to measure the quality of a universal model ¯P in terms of its regret. However, ¯P may have small (even < 0) regret for some xn, and very large regret for other xn. We must somehow find a measure of quality that takes into account all xn ∈X n. We take a worst-case approach, and look for universal models ¯P with small

42

---

[previous page](page-040.md) · [next page](page-042.md) · [all pages](index.md)
