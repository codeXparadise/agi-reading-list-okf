---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
section: 2.4 Crude MDL
section_role: other
section_index: 13
pages: [33, 34, 35, 36]
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "Based on the information-theoretic (Section 2.2) and statistical (Section 2.3) preliminaries discussed before, we now formalize a first, crude…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.4 Crude MDL

> Section 13 of 23 from [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · `other` · pages 33-36

Based on the information-theoretic (Section 2.2) and statistical (Section 2.3) preliminaries discussed before, we now formalize a first, crude version of MDL.

Let M be a class of probabilistic sources (not necessarily Markov chains). Suppose we observe a sample D = (x1, . . . , xn) ∈X n. Recall ‘the crude8 two-part code MDL Principle’ from Section 1.3, page 11:

Crude9, Two-part Version of MDL Principle Let H(1), H(2), . . . be a set of candidate models. The best point hypothesis H ∈ H(1) ∪H(2) ∪. . . to explain data D is the one which minimizes the sum L(H) + L(D|H), where

• L(H) is the length, in bits, of the description of the hypothesis; and

• L(D|H) is the length, in bits, of the description of the data when encoded with the help of the hypothesis.

The best model to explain D is the smallest model containing the selected H.

34

In this section, we implement this crude MDL Principle by giving a precise definition of the terms L(H) and L(D|H). To make the first term precise, we must design a code C1 for encoding hypotheses H such that L(H) = LC1(H). For the second term, we must design a set of codes C2,H (one for each H ∈M) such that for all D ∈X n, L(D|H) = LC2,H(D). We start by describing the codes C2,H.

2.4.1 Description Length of Data given Hypothesis

Given a sample of size n, each hypothesis H may be viewed as a probability distribution on X n. We denote the corresponding probability mass function by P(· | H). We need to associate with P(· | H) a code, or really, just a codelength function for X n. We already know that there exists a code with length function L such that for all xn ∈X n, L(xn) = −log P(xn | H). This is the code that we will pick. It is a natural choice for two reasons:

1. With this choice, the code length L(xn | H) is equal to minus the log-likelihood of xn according to H, which is a standard statistical notion of ‘goodness-of-fit’.

2. If the data turn out to be distributed according to P, then the code L(· | H) will uniquely minimize the expected code length (Section 2.2).

The second item implies that our choice is, in a sense, the only reasonable choice10. To see this, suppose M is a finite i.i.d. model containing, say, M distributions. Suppose we assign an arbitrary but finite code length L(H) to each H ∈M. Suppose X1, X2, . . . are actually distributed i.i.d. according to some ‘true’ H∗∈M. By the reasoning of Example 2.6, we see that MDL will select the true distribution P(· | H∗) for all large n, with probability 1. This means that MDL is consistent for finite M. If we were to assign codes to distributions in some other manner not satisfying L(D | H) = −log P(D | H), then there would exist distributions P(· | H) such that L(D|H)̸ = −log P(D|H). But by Figure 2.1, there must be some distribution P(· | H′) with L(·|H) = −log P(· | H′). Now let M = {H, H′} and suppose data are distributed according to P(· | H′). Then, by the reasoning of Example 2.6, MDL would select H rather than H′ for all large n! Thus, MDL would be inconsistent even in this simplest of all imaginable cases – there would then be no hope for good performance in the considerably more complex situations we intend to use it for11.

2.4.2 Description Length of Hypothesis

In its weakest and crudest form, the two-part code MDL Principle does not give any guidelines as to how to encode hypotheses (probability distributions). Every code for encoding hypotheses is allowed, as long as such a code does not change with the sample size n.

To see the danger in allowing codes to depend on n, consider the Markov chain example: if we were allowed to use diﬀerent codes for diﬀerent n, we could use, for each n, a code assigning a uniform distribution to all Markov chains of order n −1

35

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

where the θ(k) that is chosen will be equal to the ML estimator for M(k).

Why (not) this code? We may ask two questions about this code. First, why did we only reserve codewords for θ that are potentially ML estimators for the given data? The reason is that, given k′ = 2k, the codelength L(D | k, θ(k)) is minimized by ˆθ(k)(D), the ML estimator within θ(k). Reserving codewords for θ ∈\[0, 1\]k′ that cannot be ML estimates would only serve to lengthen L(D | k, θ(k)) and can never shorten L(k, θ(k)). Thus, the total description length needed to encode D will increase. Since our stated goal is to minimize description lengths, this is undesirable.

However, by the same logic we may also ask whether we have not reserved too many codewords for θ ∈\[0, 1\]k′. And in fact, it turns out that we have: the distance between two adjacent ML estimators is O(1/n). Indeed, if we had used a coarser precision, only reserving codewords for parameters with distances O(1/√

n), we would obtain smaller code lengths - (2.8) would become

L(k, θ(k)) + L(D | k, θ(k)) = −log P(D | k, ˆθ(k)) + k

2 log n + ck, (2.9)

where ck is a small constant depending on k, but not n \[Barron and Cover 1991\]. In Section 2.6 we show that (2.9) is in some sense ‘optimal’.

The Good News and the Bad News The good news is (1) we have found a principled, non-arbitrary manner to encode data D given a probability distribution H, namely, to use the code with lengths −log P(D | H); and (2), asymptotically, any code for hypotheses will lead to a consistent criterion. The bad news is that we have not found clear guidelines to design codes for hypotheses H ∈M. We found some intuitively reasonable codes for Markov chains, and we then reasoned that these could be somewhat ‘improved’, but what is conspicuously lacking is a sound theoretical principle for designing and improving codes.

We take the good news to mean that our idea may be worth pursing further. We take the bad news to mean that we do have to modify or extend the idea to get a meaningful, non-arbitrary and practically relevant model selection method. Such an extension was already suggested in Rissanen’s early works \[Rissanen 1978; Rissanen 1983\] and refined by Barron and Cover \[1991\]. However, in these works, the principle was still restricted to two-part codes. To get a fully satisfactory solution, we need to move to ‘universal codes’, of which the two-part codes are merely a special case.

---

Full document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · Page-level evidence: [paper-pages/24-tutorial-minimum-description-length](../../paper-pages/24-tutorial-minimum-description-length/index.md)
