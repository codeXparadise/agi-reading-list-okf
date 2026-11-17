---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 32
pages: [32]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "write P as P(· | θ), and M as M = {P(· | θ) | θ ∈Θ}, for some parameter space Θ. If M can be parameterized by some connected Θ ⊆Rk for some k ≥1 and…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 32 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 32 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

write P as P(· | θ), and M as M = {P(· | θ) | θ ∈Θ}, for some parameter space Θ. If M can be parameterized by some connected Θ ⊆Rk for some k ≥1 and the mapping θ →P(· | θ) is smooth (appropriately defined), we call M a parametric model or family. For example, the model M of all normal distributions on X = R is a parametric model that can be parameterized by θ = (µ, σ2) where µ is the mean and σ2 is the variance of the distribution indexed by θ. The family of all Markov chains of all orders is a model, but not a parametric model. We call a model M an i.i.d. model if, according to all P ∈M, X1, X2, . . . are i.i.d. We call M k-dimensional if k is the smallest integer k so that M can be smoothly parameterized by some Θ ⊆Rk.

For a given model M and sample D = xn, the maximum likelihood (ML) P is the P ∈M maximizing P(xn). For a parametric model with parameter space Θ, the maximum likelihood estimator ˆθ is the function that, for each n, maps xn to the θ ∈Θ that maximizes the likelihood P(xn | θ). The ML estimator may be viewed as a ‘learning algorithm’. This is a procedure that, when input a sample xn of arbitrary length, outputs a parameter or hypothesis Pn ∈M. We say a learning algorithm is consistent relative to distance measure d if for all P ∗∈M, if data are distributed according to P ∗, then the output Pn converges to P ∗in the sense that d(P ∗, Pn) →0 with P ∗-probability 1. Thus, if P ∗is the ‘true’ state of nature, then given enough data, the learning algorithm will learn a good approximation of P ∗with very high probability.

Example 2.7 \[Markov and Bernoulli models\] Recall that a k-th order Markov chain on X = {0, 1} is a probabilistic source such that for every n > k,

P(Xn = 1 | Xn−1 = xn−1, . . . , Xn−k = xn−k) =

P(Xn = 1 | Xn−1 = xn−1, . . . , Xn−k = xn−k, . . . , X1 = x1). (2.6)

That is, the probability distribution on Xn depends only on the k symbols preceding n. Thus, there are 2k possible distributions of Xn, and each such distribution is identified with a state of the Markov chain. To fully identify the chain, we also need to specify the starting state, defining the first k outcomes X1, . . . , Xk. The k-th order Markov model is the set of all k-th order Markov chains, i.e. all sources satisfying (2.6) equipped with a starting state.

The special case of the 0-th order Markov model is the Bernoulli or biased coin model, which we denote by B(0) We can parameterize the Bernoulli model by a parameter θ ∈\[0, 1\] representing the probability of observing a 1. Thus, B(0) = {P(· | θ) | θ ∈ \[0, 1\]}, with P(xn | θ) by definition equal to

n Y

P(xn | θ) =

P(xi | θ) = θn\[1\](1 −θ)n\[0\],

i=1

where n\[1\] stands for the number of 1s, and n\[0\] for the number of 0s in the sample. Note that the Bernoulli model is i.i.d. The log-likelihood is given by

log P(xn | θ) = n\[1\] log θ + n\[0\] log(1 −θ). (2.7)

33

---

[previous page](page-031.md) · [next page](page-033.md) · [all pages](index.md)
