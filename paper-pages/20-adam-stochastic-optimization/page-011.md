---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/20-adam-stochastic-optimization.md
source: ../../papers/20-adam-stochastic-optimization.md
paper_title: "Adam: A Method for Stochastic Optimization"
sequence: 20
page: 11
pages: [11]
page_of: 15
topics: ["../../topics/optimization.md"]
description: "Published as a conference paper at ICLR 2015 10 APPENDIX 10.1 CONVERGENCE PROOF Definition 10.1. A function f : Rd →R is convex if for all x, y ∈Rd,…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 11 of 15 - Adam: A Method for Stochastic Optimization

> Page 11 of the source PDF, verbatim as extracted. Canonical document: [20 - Adam: A Method for Stochastic Optimization](../../papers/20-adam-stochastic-optimization.md)

Published as a conference paper at ICLR 2015

## 10 APPENDIX

10.1 CONVERGENCE PROOF

Definition 10.1. A function f : Rd →R is convex if for all x, y ∈Rd, for all λ ∈\[0, 1\],

λf(x) + (1 −λ)f(y) ≥f(λx + (1 −λ)y)

Also, notice that a convex function can be lower bounded by a hyperplane at its tangent. Lemma 10.2. If a function f : Rd →R is convex, then for all x, y ∈Rd,

f(y) ≥f(x) + ∇f(x)T (y −x)

The above lemma can be used to upper bound the regret and our proof for the main theorem is constructed by substituting the hyperplane with the Adam update rules.

The following two lemmas are used to support our main theorem. We also use some definitions simplify our notation, where gt ≜∇ft(θt) and gt,i as the ith element. We define g1:t,i ∈Rt as a vector that contains the ith dimension of the gradients over all iterations till t, g1:t,i = \[g1,i, g2,i, · · · , gt,i\] Lemma 10.3. Let gt = ∇ft(θt) and g1:t be defined as above and bounded, ∥gt∥2 ≤G, ∥gt∥∞≤ G∞. Then,

s

T X

g2

t,i t ≤2G∞∥g1:T,i∥2

t=1

Proof. We will prove the inequality using induction over T.

q

The base case for T = 1, we have

1,i ≤2G∞∥g1,i∥2.

g2

For the inductive step,

s

s

s

T −1 X

T X

g2

g2

g2

t,i t =

t,i t +

T,i T

t=1

t=1

s

g2

T,i T

≤2G∞∥g1:T −1,i∥2 +

s

q

g2

T,i T

∥g1:T,i∥2

2 −g2 T +

= 2G∞

g4

T,i 4∥g1:T,i∥2 2 ≥∥g1:T,i∥2 2 −g2 T,i, we can take square root of both side and have,

From, ∥g1:T,i∥2

2 −g2 T,i +

q

g2

T,i 2∥g1:T,i∥2

∥g1:T,i∥2

2 −g2 T,i ≤∥g1:T,i∥2 −

g2

T,i 2 p

≤∥g1:T,i∥2 −

TG2∞

q

Rearrange the inequality and substitute the

2 −g2 T,i term,

∥g1:T,i∥2

s

q

g2

T,i T ≤2G∞∥g1:T,i∥2

∥g1:T,i∥2

2 −g2 T +

G∞

12

---

[previous page](page-010.md) · [next page](page-012.md) · [all pages](index.md)
