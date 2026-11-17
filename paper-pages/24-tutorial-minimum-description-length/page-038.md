---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 38
pages: [38]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "Both L8(xn) and L9(xn) are linearly increasing in the number of 1s in xn. However, if the frequency n1/n is approximately 0.8, then minL∈L L(xn) will…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 38 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 38 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

Both L8(xn) and L9(xn) are linearly increasing in the number of 1s in xn. However, if the frequency n1/n is approximately 0.8, then minL∈L L(xn) will be achieved for L8. If n1/n ≈0.9 then minL∈L L(xn) is achieved for L9. More generally, if n1/n ≈j/10 then Lj achieves the minimum15. We would like to send xn using a code ¯L such that for all xn, we need at most ˆL(xn) bits, where ˆL(xn) is defined as ˆL(xn) := minL∈L L(xn). Since −log is monotonically decreasing, ˆL(xn) = −log P(xn | ˆθ(xn)). We already gave an informal explanation as to why a code with lengths ˆL does not exist. We can now explain this more formally as follows: if such a code were to exist, it would correspond to some distribution ¯P. Then we would have for all xn, ¯L(xn) = −log ¯P(xn). But, by definition, for all xn ∈X n, ¯L(xn) ≤ˆL(xn) = −log P(xn|ˆθ(xn)) where ˆθ(xn) ∈ {0.1, . . . , 0.9}. Thus we get for all xn, −log ¯P(xn) ≤−log P(xn | ˆθ(xn)) or ¯P(xn) ≥ P(xn | ˆθ(xn)), so that, since |L| > 1,

P(xn | ˆθ(xn)) =

θ P(xn | θ) > 1, (2.10)

¯P(xn) ≥

X

X

X

max

xn

xn

xn

where the last inequality follows because for any two θ1, θ2 with θ1̸ = θ2, there is at least one xn with P(xn | θ1) > P(xn | θ2). (2.10) says that ¯P is not a probability distribution. It follows that ¯L cannot be a codelength function. The argument can be extended beyond the Bernoulli model of the example above: as long as |L| > 1, and all codes in L correspond to a non-defective distribution, (2.10) must still hold, so that there exists no code ¯L with ¯L(xn) = ˆL(xn) for all xn. The underlying reason that no such code exists is the fact that probabilities must sum up to something ≤1; or equivalently, that there exists no coding scheme assigning short code words to many diﬀerent messages – see Example 2.2.

Since there exists no code which, no matter what xn is, always mimics the best code for xn, it may make sense to look for the next best thing: does there exist a code which, for all xn ∈X n, is ‘nearly’ (in some sense) as good as ˆL(xn)? It turns out that in many cases, the answer is yes: there typically exists codes ¯L such that no matter what xn arrives, ¯L(xn) is not much larger than ˆL(xn), which may be viewed as the code that is best ‘with hindsight’ (i.e., after seeing xn). Intuitively, codes which satisfy this property are called universal codes - a more precise definition follows below. The first (but perhaps not foremost) example of a universal code is the two-part code that we have encountered in Section 2.4.

2.5.1 Two-part Codes as simple Universal Codes

Example 2.10 \[finite L\] Let L be as in Example 2.9. We can devise a code ¯L2-p for all xn ∈X n as follows: to encode xn, we first encode the j ∈{1, . . . , 9} such that Lj(xn) = minL∈L L(xn), using a uniform code. This takes log 9 bits. We then encode xn itself using the code indexed by j. This takes Lj bits. Note that in contrast to the naive scheme discussed in Example 2.9, the resulting scheme properly defines a prefix code: a decoder can decode xn by first decoding j, and then decoding xn using Lj.

39

---

[previous page](page-037.md) · [next page](page-039.md) · [all pages](index.md)
