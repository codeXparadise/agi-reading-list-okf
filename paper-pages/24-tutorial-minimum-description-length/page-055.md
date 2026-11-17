---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 55
pages: [55]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "extended to sequences x1, . . . , xn by taking product densities. As is well-known [Casella and Berger 1990], the ML estimator ˆµ(xn) is equal to the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 55 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 55 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

extended to sequences x1, . . . , xn by taking product densities. As is well-known \[Casella and Berger 1990\], the ML estimator ˆµ(xn) is equal to the sample mean: ˆµ(xn) = n−1 Pn

i=1 xi. An easy calculation shows that

Z

xn P(xn | ˆµ(xn))dxn = ∞,

COMPn(M) =

where we abbreviated dx1 . . . dxn to dxn. Therefore, we cannot use basic MDL model selection. It also turns out that I(µ) = σ−2 so that

Z

Z

p

p

|I(θ)|dθ =

|I(µ)|dµ = ∞.

µ∈R

Θ

Thus, the Bayesian universal model approach with Jeﬀreys’ prior cannot be applied either. Does this mean that our MDL model selection and complexity definitions break down even in such a simple case? Luckily, it turns out that they can be repaired, as we now show. Barron, Rissanen, and Yu \[1998\] and Foster and Stine \[2001\] show that, for all intervals \[a, b\],

2πσ · √

P(xn | ˆµ(xn))dxn = b −a

Z

√

n. (2.33)

xn:ˆµ(xn)∈\[a,b\]

Suppose for the moment that it is known that ˆµ lies in some set \[−K, K\] for some fixed K. Let MK be the set of conditional distributions thus obtained: MK = {P ′(· | µ) | µ ∈R}, where P ′(xn | µ) is the density of xn according to the normal distribution with mean µ, conditioned on |n−1 P xi| ≤K. By (2.33), the ‘conditional’ minimax regret distribution ¯Pnml(· | MK) is well-defined for all K > 0. That is, for all xn with |ˆµ(xn)| ≤K,

¯Pnml(xn | MK) = P ′(xn | ˆµ(xn))

xn : |ˆµ(xn)|<K P ′(xn | ˆµ(xn))dxn,

R

with regret (or ‘conditional’ complexity),

P ′(xn | ˆµ(xn))dxn = log K + 1

2 log n

Z

COMPn(MK) = log

2π −log σ + 1.

|ˆµ(xn)|<K

This suggests to redefine the complexity of the full model M so that its regret depends on the area in which ˆµ falls. The most straightforward way of achieving this is to define a meta-universal model for M, combining the NML with a two-part code: we encode data by first encoding some value for K. We then encode the actual data xn using the code ¯Pnml(·|MK). The resulting code ¯Pmeta is a universal code for M with lengths

−log ¯Pmeta(xn | MK) + L(K)

−log ¯Pmeta(xn|M):= min

. (2.34)

K

The idea is now to base MDL model selection on ¯Pmeta(·|M) as in (2.34) rather than on the (undefined) ¯Pnml(·|M). To make this work, we need to choose L in a clever

56

---

[previous page](page-054.md) · [next page](page-056.md) · [all pages](index.md)
