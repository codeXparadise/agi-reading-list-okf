---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 5.2. Prediction of computable sequences
section_role: other
section_index: 44
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "The most elementary result is that every computable sequence can be predicted by at least one predictor, and that this predictor need not be…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 5.2. Prediction of computable sequences

> Section 44 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

The most elementary result is that every computable sequence can be predicted
by at least one predictor, and that this predictor need not be significantly more
complex than the sequence to be predicted.

5.2.1 Lemma. ∀ω ∈C, ∃p ∈P (ω) : K(p) < K(ω).+

$$
\forall\omega\in\mathcal{C},\exists p\in\mathcal{P}(\omega):K(p)\leq K(\omega)
$$

Proof. As the sequence ω is computable, there must exist at least one
algorithm that generates ω. Let q be the shortest such algorithm and construct
an algorithm p that “predicts” ω as follows: Firstly the algorithm p reads x1:n
to find the value of n, then it runs q to generate x1:n+1 and returns xn+1 as its
prediction. Clearly p perfectly predicts ω and ℓ(p) < ℓ(q) + c, for some small
constant c that is independent of ω and q.

$$
\omega
$$

$$
q
$$

$$
x_{1:n}
$$

$$
n,
$$

$$
x_{1:n+1}
$$

$$
q
$$

$$
x_{n+1}
$$

$$
\omega
$$

$$
p
$$

$$
\ell(p)<\ell(q)+c,
$$

$$
\omega
$$

$$
q
$$

Not only can any computable sequence be predicted, there also exist very
simple predictors able to predict arbitrarily complex sequences:

5.2.2 Lemma. There exists a predictor p such that ∀n ∈ N, ∃ ω ∈ C : p ∈
P (ω) and K(ω) > n.

$$
\mathcal{P}(\omega)
$$

$$
\forall n\in\mathbb{N},\exists\omega\in\mathcal{C}:p\in
$$

$$
K(\omega)>n
$$

Proof. Take a string x such that K(x) = ℓ(x) ≥ 2n, and from this define a
sequence ω := x0000.... Clearly K(ω) > n and yet a simple predictor p that
always predicts 0 can learn to predict ω.

$$
K(x)=\ell(x)\geq2n
$$

$$
\omega:=x0000\ldots
$$

$$
K(\omega)>n
$$

$$
\omega
$$

The predictor used in the above proof is very simple and can only “learn”
sequences that end with all 0’s, albeit where the initial string can have arbitrarily high Kolmogorov complexity. It may seem that this is due to sequences that are initially complex but where the “tail complexity”, defined
lim infi→∞K(ωi:∞), is zero. This is not the case:

$$
0^{\prime}\mathrm{s}
$$

$$
\operatorname{nf}_{i\to\infty}K(\omega_{i:\infty})
$$

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
