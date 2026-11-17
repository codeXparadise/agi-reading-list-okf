---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 60
pages: [60]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "We give a very brief overview of these - for details we refer to [Barron, Rissanen, and Yu 1998; Hansen and Yu 2001] and, for the classification…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 60 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 60 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

We give a very brief overview of these - for details we refer to \[Barron, Rissanen, and Yu 1998; Hansen and Yu 2001\] and, for the classification case, \[Gr¨unwald and Langford 2004\].

Non-Parametric Inference Sometimes the model class M is so large that it cannot be finitely parameterized. For example, let X = \[0, 1\] be the unit interval and let M be the i.i.d. model consisting of all distributions on X with densities f such that −log f(x) is a continuous function on X. M is clearly ‘non-parametric’: it cannot be meaningfully parameterized by a connected finite-dimensional parameter set Θ(k) ⊆Rk. We may still try to learn a distribution from M in various ways, for example by histogram density estimation \[Rissanen, Speed, and Yu 1992\] or kernel density estimation \[Rissanen 1989\]. MDL is quite suitable for such applications, in which we typically select a density f from a class M(n) ⊂M, where M(n) grows with n, and every P ∗∈M can be arbitrarily well approximated by members of M(n), M(n+1), . . . in the sense that limn→∞infP ∈M(n) D(P ∗∥P) = 0 \[Barron, Rissanen, and Yu 1998\]. Here D is the Kullback-Leibler divergence \[Cover and Thomas 1991\] between P ∗and P.

MDL Parameter Estimation: Three Approaches The ‘crude’ MDL method (Section 2.4) was a means of doing model selection and parameter estimation at the same time. ‘Refined’ MDL only dealt with selection of models. If instead, or at the same time, parameter estimates are needed, they may be obtained in three diﬀerent ways. Historically the first way \[Rissanen 1989; Hansen and Yu 2001\] was to simply use the refined MDL Principle to pick a parametric model M(k), and then, within M(k), pick the ML estimator ˆθ(k). After all, we associate with M(k) the distribution ¯Pnml with codelengths ‘as close as possible’ to those achieved by the ML estimator. This suggests that within M(k), we should prefer the ML estimator. But upon closer inspection, Figure 2.4 suggests to use a two-part code also to select θ within M(k); namely, we should discretize the parameter space in such a way that the resulting 2-part code achieves the minimax regret among all two-part codes; we then pick the (quantized) θ minimizing the two-part code length. Essentially this approach has been worked out in detail by Barron and Cover \[1991\]. The resulting estimators may be called two-part code MDL estimators. A third possibility is to define predictive MDL estimators such as the Laplace and Jeﬀreys estimators of Example 2.19; once again, these can be understood as an extension of Figure 2.4 \[Barron, Rissanen, and Yu 1998\]. These second and third possibilities are more sophisticated than the first. However, if the model M is finitedimensional parametric and n is large, then both the two-part and the predictive MDL estimators will become indistinguishable from the maximum likelihood estimators. For this reason, it has sometimes been claimed that MDL parameter estimation is just ML parameter estimation. Since for small samples, the estimates can be quite diﬀerent, this statement is misleading.

61

---

[previous page](page-059.md) · [next page](page-061.md) · [all pages](index.md)
