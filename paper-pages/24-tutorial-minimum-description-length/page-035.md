---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 35
pages: [35]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "with all parameters equal to 0 or 1. Since there are only a finite number (2n−1) of these, this is possible. But then, for each n, xn ∈X n, MDL would…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 35 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 35 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

with all parameters equal to 0 or 1. Since there are only a finite number (2n−1) of these, this is possible. But then, for each n, xn ∈X n, MDL would select the ML Markov chain of order n −1. Thus, MDL would coincide with ML and, no matter how large n, we would overfit.

Consistency of Two-part MDL Remarkably, if we fix an arbitrary code for all hypotheses, identical for all sample sizes n, this is suﬃcient to make MDL consistent12

for a wide variety of models, including the Markov chains. For example, let L be the length function corresponding to some code for the Markov chains. Suppose some Markov chain P ∗generates the data such that L(P ∗) < ∞under our coding scheme. Then, broadly speaking, for every P ∗of every order, with probability 1 there exists some n0 such that for all samples larger than n0, two-part MDL will select P ∗– here n0 may depend on P ∗and L.

While this results indicates that MDL may be doing something sensible, it certainly does not justify the use of arbitrary codes - diﬀerent codes will lead to preferences of diﬀerent hypotheses, and it is not at all clear how a code should be designed that leads to good inferences with small, practically relevant sample sizes.

Barron and Cover \[1991\] have developed a precise theory of how to design codes C1 in a ‘clever’ way, anticipating the developments of ‘refined MDL’. Practitioners have often simply used ‘reasonable’ coding schemes, based on the following idea. Usually there exists some ‘natural’ decomposition of the models under consideration, M = S

k>0 M(k) where the dimension of M(k) grows with k but is not necessarily equal to k. In the Markov chain example, we have B = S B(k) where B(k) is the k-th order, 2k-parameter Markov model. Then within each submodel M(k), we may use a fixedlength code for θ ∈Θ(k). Since the set Θ(k) is typically a continuum, we somehow need to discretize it to achieve this.

Example 2.8 \[a Very Crude Code for the Markov Chains\] We can describe a Markov chain of order k by first describing k, and then describing a parameter vector θ ∈\[0, 1\]k′ with k′ = 2k. We describe k using our simple code for the integers (Example 2.4). This takes 2 log k + 1 bits. We now have to describe the k′-component parameter vector. We saw in Example 2.7 that for any xn, the best-fitting (ML) kth order Markov chain can be identified with k′ frequencies. It is not hard to see that these frequencies are uniquely determined by the counts n\[1|0...00\], n\[1|0...01\], . . . , n\[1|1...11\]. Each individual count must be in the (n+1)-element set {0, 1, . . . , n}. Since we assume n is given in advance13, we may use a simple fixed-length code to encode this count, taking log(n + 1) bits (Example 2.3). Thus, once k is fixed, we can describe such a Markov chain by a uniform code using k′ log(n + 1) bits. With the code just defined we get for any P ∈B, indexed by parameter Θ(k),

L(P) = L(k, Θ(k)) = 2 log k + 1 + k log(n + 1),

so that with these codes, MDL tells us to pick the k, θ(k) minimizing

L(k, θ(k)) + L(D | k, θ(k)) = 2 log k + 1 + k log(n + 1) −log P(D | k, θ(k)), (2.8)

36

---

[previous page](page-034.md) · [next page](page-036.md) · [all pages](index.md)
