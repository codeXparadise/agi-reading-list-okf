---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 48
pages: [48]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "Whereas for finite M, COMPn(M) remains finite, for parametric models it generally grows logarithmically in n. Since typically −log P(xn | ˆθ(xn))…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 48 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 48 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

Whereas for finite M, COMPn(M) remains finite, for parametric models it generally grows logarithmically in n. Since typically −log P(xn | ˆθ(xn)) grows linearly in n, it is still the case that for fixed dimensionality k (i.e. for a fixed M that is k-dimensional) and large n, the part of the codelength −log ¯Pnml(xn | M) due to the complexity of M is very small compared to the part needed to encode data xn with ˆθ(xn). The term R

p

|I(θ)|dθ may be interpreted as the contribution of the functional form of M to the model complexity \[Balasubramanian 2004\]. It does not grow with n so that, when selecting between two models, it becomes irrelevant and can be ignored for very large n. But for small n, it can be important, as can be seen from Example 1.4, Fechner’s and Stevens’ model. Both models have two parameters, yet the

Θ

p

R

|I(θ)|dθ-term is much larger for Fechner’s than for Stevens’ model. In the experiments of Myung, Balasubramanian, and Pitt \[2000\], the parameter set was restricted to 0 < a < ∞, 0 < b < 3 for Stevens’ model and 0 < a < ∞, 0 < b < ∞for Fechner’s model. The variance of the error Z was set to 1 in both models. With these values, the diﬀerence in

Θ

p

R

|I(θ)|dθ is 3.804, which is non-negligible for small samples. Thus, Stevens’ model contains more distinguishable distributions than Fechner’s, and is better able to capture random noise in the data – as Townsend \[1975\] already speculated almost 30 years ago. Experiments suggest that for regression models such as Stevens’ and Fechner’s’, as well as for Markov models and general exponential families, the approximation (2.21) is reasonably accurate already for small samples. But this is certainly not true for general models:

Θ

The Asymptotic Expansion of COMPn Should Be Used with Care! (2.21) does not hold for all parametric models; and for some models for which it does hold, the o(1) term may only converge to 0 only for quite large sample sizes. Foster and Stine \[1999, 2004\] show that the approximation (2.21) is, in general, only valid if k is much smaller than n.

Two-part codes and COMPn(M) We now have a clear guiding principle (minimax regret) which we can use to construct ‘optimal’ two-part codes, that achieve the minimax regret among all two-part codes. How do such optimal two-part codes compare to the NML codelength? Let M be a k-dimensional model. By slightly adjusting the arguments of \[Barron and Cover 1991, Appendix\], one can show that, under regularity conditions, the minimax optimal two-part code ¯P2-p achieves regret

−log ¯P2-p(xn | M) + log P(xn | ˆθ(xn)) = k

2 log n

2π + log Z

p

|I(θ)|dθ + f(k) + o(1),

θ∈Θ

where f : N →R is a bounded positive function satisfying limk→∞f(k) = 0. Thus, for large k, optimally designed two-part codes are about as good as NML. The problem with two-part code MDL is that in practice, people often use much cruder codes with much larger minimax regret.

49

---

[previous page](page-047.md) · [next page](page-049.md) · [all pages](index.md)
