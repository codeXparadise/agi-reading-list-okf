---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/20-adam-stochastic-optimization.md
source: ../../papers/20-adam-stochastic-optimization.md
paper_title: "Adam: A Method for Stochastic Optimization"
sequence: 20
page: 13
pages: [13]
page_of: 15
topics: ["../../topics/optimization.md"]
description: "Published as a conference paper at ICLR 2015 ∥θm −θn∥∞≤D∞for any m, n ∈{1, ..., T}, and β1, β2 ∈[0, 1) satisfy β2 1 √β2 < 1. Let αt = α √ t and β1,t…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 13 of 15 - Adam: A Method for Stochastic Optimization

> Page 13 of the source PDF, verbatim as extracted. Canonical document: [20 - Adam: A Method for Stochastic Optimization](../../papers/20-adam-stochastic-optimization.md)

Published as a conference paper at ICLR 2015

∥θm −θn∥∞≤D∞for any m, n ∈{1, ..., T}, and β1, β2 ∈\[0, 1) satisfy β2

1 √β2 < 1. Let αt = α √

t and β1,t = β1λt−1, λ ∈(0, 1). Adam achieves the following guarantee, for all T ≥1.

√1 −β2 2α(1 −β1)(1 −λ)2

d X

d X

d X

p

R(T) ≤ D2

D2

TbvT,i+ α(β1 + 1)G∞ (1 −β1)√1 −β2(1 −γ)2

∞G∞

∥g1:T,i∥2+

2α(1 −β1)

i=1

i=1

i=1

Proof. Using Lemma 10.2, we have,

d X

ft(θt) −ft(θ∗) ≤gT

t (θt −θ∗) =

gt,i(θt,i −θ∗

,i)

i=1

From the update rules presented in algorithm 1,

p

θt+1 = θt −αt bmt/

bvt

 β1,t √bvt

mt−1 + (1 −β1,t) √bvt

= θt − αt 1 −βt 1

gt

We focus on the ith dimension of the parameter vector θt ∈Rd. Subtract the scalar θ∗

,i and square both sides of the above update rule, we have,

t( bmt,i p

,i)2 − 2αt 1 −βt 1 ( β1,t p

mt−1,i + (1 −β1,t) p

,i)2 =(θt,i −θ∗

(θt+1,i −θ∗

gt,i)(θt,i −θ∗

,i) + α2

)2

bvt,i

bvt,i

bvt,i

We can rearrange the above equation and use Young’s inequality, ab ≤a2/2 + b2/2. Also, it can be

qPt

p

p

j=1(1 −β2)βt−j

shown that

1 −βt 2 ≤∥g1:t,i∥2 and β1,t ≤β1. Then

2 g2

bvt,i =

j,i/

1) p

,i) =(1 −βt

bvt,i 2αt(1 −β1,t)

,t)2 −(θt+1,i −θ∗

gt,i(θt,i −θ∗

(θt,i −θ∗

,i)2

1) p

1 4 t−1,i √αt−1

+ αt(1 −βt

bv

bvt,i 2(1 −β1,t) ( bmt,i p

+ β1,t (1 −β1,t)

,i −θt,i)√αt−1

mt−1,i

(θ∗

)2

1 4 t−1,i

bvt,i

bv

p

bvt,i + β1,t 2αt−1(1 −β1,t)(θ∗ ,i −θt,i)2p

≤ 1 2αt(1 −β1)

,t)2 −(θt+1,i −θ∗

(θt,i −θ∗

,i)2

bvt−1,i

+ β1αt−1 2(1 −β1) m2

+ αt 2(1 −β1) bm2

t−1,i p

t,i p

bvt−1,i

bvt,i

We apply Lemma 10.4 to the above inequality and derive the regret bound by summing across all the dimensions for i ∈1, ..., d in the upper bound of ft(θt) −ft(θ∗) and the sequence of convex functions for t ∈1, ..., T:

p

p

d X

d X

T X

1 2α1(1 −β1)(θ1,i −θ∗ ,i)2p

bvt,i αt

bvt−1,i αt−1

1 2(1 −β1)(θt,i −θ∗ ,i)2(

R(T) ≤

−

bv1,i +

)

t=2

i=1

i=1

d X

d X

+ β1αG∞ (1 −β1)√1 −β2(1 −γ)2

∥g1:T,i∥2 + αG∞ (1 −β1)√1 −β2(1 −γ)2

∥g1:T,i∥2

i=1

i=1

d X

T X

β1,t 2αt(1 −β1,t)(θ∗ ,i −θt,i)2p

bvt,i

+

t=1

i=1

14

---

[previous page](page-012.md) · [next page](page-014.md) · [all pages](index.md)
