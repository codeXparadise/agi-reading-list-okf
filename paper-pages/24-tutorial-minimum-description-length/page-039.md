---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 39
pages: [39]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "Thus, for every possible xn ∈X n, we obtain ¯L2-p(xn) = min L∈L L(xn) + log 9. For all L ∈L, minxn L(xn) grows linearly in n: minθ,xn −log P(xn | θ)…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 39 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 39 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

Thus, for every possible xn ∈X n, we obtain

¯L2-p(xn) = min

L∈L L(xn) + log 9.

For all L ∈L, minxn L(xn) grows linearly in n: minθ,xn −log P(xn | θ) = −n log 0.9 ≈ 0.15n. Unless n is very small, no matter what xn arises, the extra number of bits we need using ¯L2-p compared to ˆL(xn) is negligible.

More generally, let L = {L1, . . . , LM} where M can be arbitrarily large, and the Lj can be any codelength functions we like; they do not necessarily represent Bernoulli distributions any more. By the reasoning of Example 2.10, there exists a (two-part) code such that for all xn ∈X n,

¯L2-p(xn) = min

L∈L L(xn) + log M. (2.11)

In most applications min L(xn) grows linearly in n, and we see from (2.11) that, as soon as n becomes substantially larger than log M, the relative diﬀerence in performance between our universal code and ˆL(xn) becomes negligible. In general, we do not always want to use a uniform code for the elements in L; note that any arbitrary code on L will give us an analogue of (2.11), but with a worst-case overhead larger than log M corresponding to the largest codelength of any of the elements in L.

Example 2.11 \[Countably Infinite L\] We can also construct a 2-part code for arbitrary countably infinite sets of codes L = {L1, L2, . . . }: we first encode some k using our simple code for the integers (Example 2.4). With this code we need 2 log k + 1 bits to encode integer k. We then encode xn using the code Lk. ¯L2-p is now defined as the code we get if, for any xn, we encode xn using the Lk minimizing the total two-part description length 2 log k + 1 + Lk(xn).

In contrast to the case of finite L, there does not exist a constant c any more such that for all n, xn ∈X n, ¯L2-p(xn) ≤infL∈L L(xn) + c. Instead we have the following weaker, but still remarkable property: for all k, all n, all xn, ¯L2-p(xn) ≤Lk(xn) + 2 log k + 1, so that also,

¯L2-p(xn) ≤ inf L∈{L1,... ,Lk} L(xn) + 2 log k + 1.

For any k, as n grows larger, the code ¯L2-p starts to mimic whatever L ∈{L1, . . . , Lk} compresses the data most. However, the larger k, the larger n has to be before this happens.

2.5.2 From Universal Codes to Universal Models

Instead of postulating a set of candidate codes L, we may equivalently postulate a set M of candidate probabilistic sources, such that L is the set of codes corresponding to M. We already implicitly did this in Example 2.9.

40

---

[previous page](page-038.md) · [next page](page-040.md) · [all pages](index.md)
