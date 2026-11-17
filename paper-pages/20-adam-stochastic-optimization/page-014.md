---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/20-adam-stochastic-optimization.md
source: ../../papers/20-adam-stochastic-optimization.md
paper_title: "Adam: A Method for Stochastic Optimization"
sequence: 20
page: 14
pages: [14]
page_of: 15
topics: ["../../topics/optimization.md"]
description: "Published as a conference paper at ICLR 2015 From the assumption, ∥θt −θ∗∥2 ≤D, ∥θm −θn∥∞≤D∞, we have: d X d X d X t X p p R(T) ≤ D2 ∥g1:T,i∥2 + D2…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 14 of 15 - Adam: A Method for Stochastic Optimization

> Page 14 of the source PDF, verbatim as extracted. Canonical document: [20 - Adam: A Method for Stochastic Optimization](../../papers/20-adam-stochastic-optimization.md)

Published as a conference paper at ICLR 2015

From the assumption, ∥θt −θ∗∥2 ≤D, ∥θm −θn∥∞≤D∞, we have:

d X

d X

d X

t X

p

p

R(T) ≤ D2

∥g1:T,i∥2 + D2

TbvT,i + α(1 + β1)G∞ (1 −β1)√1 −β2(1 −γ)2

β1,t (1 −β1,t)

∞ 2α

tbvt,i

2α(1 −β1)

t=1

i=1

i=1

i=1

d X

d X

p

≤ D2

TbvT,i + α(1 + β1)G∞ (1 −β1)√1 −β2(1 −γ)2

∥g1:T,i∥2

2α(1 −β1)

i=1

i=1

√1 −β2 2α

d X

t X

√

+ D2

∞G∞

β1,t (1 −β1,t)

t

t=1

i=1

We can use arithmetic geometric series upper bound for the last term:

t X

t X

√

1 (1 −β1)λt−1√

β1,t (1 −β1,t)

t ≤

t

t=1

t=1

t X

1 (1 −β1)λt−1t

≤

t=1

≤ 1 (1 −β1)(1 −λ)2

Therefore, we have the following regret bound:

√1 −β2 2αβ1(1 −λ)2

d X

d X

d X

p

R(T) ≤ D2

D2

TbvT,i + α(1 + β1)G∞ (1 −β1)√1 −β2(1 −γ)2

∞G∞

∥g1:T,i∥2 +

2α(1 −β1)

i=1

i=1

i=1

15

---

[previous page](page-013.md) · [next page](page-015.md) · [all pages](index.md)
