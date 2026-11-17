---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 36
pages: [36]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "where the θ(k) that is chosen will be equal to the ML estimator for M(k). Why (not) this code? We may ask two questions about this code. First, why…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 36 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 36 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

where the θ(k) that is chosen will be equal to the ML estimator for M(k).

Why (not) this code? We may ask two questions about this code. First, why did we only reserve codewords for θ that are potentially ML estimators for the given data? The reason is that, given k′ = 2k, the codelength L(D | k, θ(k)) is minimized by ˆθ(k)(D), the ML estimator within θ(k). Reserving codewords for θ ∈\[0, 1\]k′ that cannot be ML estimates would only serve to lengthen L(D | k, θ(k)) and can never shorten L(k, θ(k)). Thus, the total description length needed to encode D will increase. Since our stated goal is to minimize description lengths, this is undesirable.

However, by the same logic we may also ask whether we have not reserved too many codewords for θ ∈\[0, 1\]k′. And in fact, it turns out that we have: the distance between two adjacent ML estimators is O(1/n). Indeed, if we had used a coarser precision, only reserving codewords for parameters with distances O(1/√

n), we would obtain smaller code lengths - (2.8) would become

L(k, θ(k)) + L(D | k, θ(k)) = −log P(D | k, ˆθ(k)) + k

2 log n + ck, (2.9)

where ck is a small constant depending on k, but not n \[Barron and Cover 1991\]. In Section 2.6 we show that (2.9) is in some sense ‘optimal’.

The Good News and the Bad News The good news is (1) we have found a principled, non-arbitrary manner to encode data D given a probability distribution H, namely, to use the code with lengths −log P(D | H); and (2), asymptotically, any code for hypotheses will lead to a consistent criterion. The bad news is that we have not found clear guidelines to design codes for hypotheses H ∈M. We found some intuitively reasonable codes for Markov chains, and we then reasoned that these could be somewhat ‘improved’, but what is conspicuously lacking is a sound theoretical principle for designing and improving codes.

We take the good news to mean that our idea may be worth pursing further. We take the bad news to mean that we do have to modify or extend the idea to get a meaningful, non-arbitrary and practically relevant model selection method. Such an extension was already suggested in Rissanen’s early works \[Rissanen 1978; Rissanen 1983\] and refined by Barron and Cover \[1991\]. However, in these works, the principle was still restricted to two-part codes. To get a fully satisfactory solution, we need to move to ‘universal codes’, of which the two-part codes are merely a special case.

## 2.5 Information Theory II: Universal Codes and Models

We have just indicated why the two-part code formulation of MDL needs to be refined. It turns out that the key concept we need is that of universal coding. Broadly speaking, a code ¯L that is universal relative to a set of candidate codes L allows us to compress every sequence xn almost as well as the code in L that compresses that particular

37

---

[previous page](page-035.md) · [next page](page-037.md) · [all pages](index.md)
