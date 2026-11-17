---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 49
pages: [49]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "2.6.3 Bayesian Interpretation The Bayesian method of statistical inference provides several alternative approaches to model selection. The most…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 49 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 49 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

2.6.3 Bayesian Interpretation

The Bayesian method of statistical inference provides several alternative approaches to model selection. The most popular of these is based on Bayes factors \[Kass and Raftery 1995\]. The Bayes factor method is very closely related to the refined MDL approach. Assuming uniform priors on models M(1) and M(2), it tells us to select the model with largest marginal likelihood ¯PBayes(xn | M(j)), where ¯PBayes is as in (2.12), with the sum replaced by an integral, and w(j) is the density of the prior distribution on M(j):

Z

¯PBayes(xn | M(j)) =

P(xn | θ)w(j)(θ)dθ. (2.22)

M is Exponential Family Let now ¯PBayes = ¯PBayes(· | M) for some fixed model M. Under regularity conditions on M, we can perform a Laplace approximation of the integral in (2.12). For the special case that M is an exponential family, we obtain the following expression for the regret \[Jeﬀreys 1961; Schwarz 1978; Kass and Raftery 1995; Balasubramanian 1997\]:

−log ¯PBayes(xn) −\[−log P(xn | ˆθ(xn))\] = k

2 log n

2π −log w(ˆθ) + log q

|I(ˆθ)| + o(1).

(2.23)

Let us compare this with (2.21). Under the regularity conditions needed for (2.21), the quantity on the right of (2.23) is within O(1) of COMPn(M). Thus, the code length achieved with ¯PBayes is within a constant of the minimax optimal −log ¯Pnml(xn). Since −log P(xn | ˆθ(xn)) increases linearly in n, this means that if we compare two models M(1) and M(2), then for large enough n, Bayes and refined MDL select the same model. If we equip the Bayesian universal model with a special prior known as the Jeﬀreys-Bernardo prior \[Jeﬀreys 1946; Bernardo and Smith 1994\],

p

|I(θ)|

wJeﬀreys(θ) =

, (2.24)

p

R

|I(θ)|dθ

θ∈Θ

then Bayes and refined NML become even more closely related: plugging in (2.24) into (2.23), we find that the right-hand side of (2.23) now simply coincides with (2.21). A concrete example of Jeﬀreys’ prior is given in Example 2.19. Jeﬀreys introduced his prior as a ‘least informative prior’, to be used when no useful prior knowledge about the parameters is available \[Jeﬀreys 1946\]. As one may expect from such a prior, it is invariant under continuous 1-to-1 reparameterizations of the parameter space. The present analysis shows that, when M is an exponential family, then it also leads to asymptotically minimax codelength regret: for large n, refined NML model selection becomes indistinguishable from Bayes factor model selection with Jeﬀreys’ prior.

50

---

[previous page](page-048.md) · [next page](page-050.md) · [all pages](index.md)
