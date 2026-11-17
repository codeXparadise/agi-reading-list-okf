---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 2.7. Solomonoff induction
section_role: other
section_index: 19
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "Given a prior distribution ξ over B∞, it is straightforward to predict the continuation of a binary sequence using the same approach as we used in…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.7. Solomonoff induction

> Section 19 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

Given a prior distribution ξ over B∞, it is straightforward to predict the continuation of a binary sequence using the same approach as we used in Section 2.3.
∞
Given prior distribution ξ and the observed string ω1:t ∈ B from a sequence
ω ∈ B∞ that has been sampled from an unknown computable distribution
µ ∈Mc, our estimate of the probability that the next bit will be 0 is,

$$
\xi over\mathbb{B}^{\infty}
$$

$$
\xi
$$

$$
\omega_{1:t}\in\mathbb{B}^{\infty}
$$

$$
\omega\in\mathbb{B}^{\infty}
$$

$$
\mu\in\mathcal{M}_{c},
$$

$$
\xi(\omega_{1:t}\underline{0})=\frac{\xi(\underline{\omega}_{1:t}\underline{0})}{\xi(\underline{\omega}_{1:t})}.
$$

Is this predictor based on ξ any good? By definition, the best possible
predictor would be based on the unknown true distribution µ that ω has been
sampled from. That is, the true probability that the next bit is a 0 given an
observed initial string ω1:t is,

$$
\xi
$$

$$
\mu
$$

$$
\omega
$$

$$
\omega_{1:t}
$$

$$
\mu(\omega_{1:t}\underline{0})=\frac{\mu(\underline{\omega}_{1:t}\underline{0})}{\mu(\underline{\omega}_{1:t})}.
$$

As this predictor is optimal by construction, it can be used to quantify the
relative performance of the predictor based on ξ. For example, consider the
expected squared error in the estimated probability that the tth bit will be a
0: ∑
()2
S = µ(x) ξ(x0) − µ(x0).

$$
\xi
$$

$$
t^{th}
$$

$$
0;
$$

$$
S_{t}=\sum_{\underline{x}\in\mathbb{B}^{t-1}}\mu(\underline{x})\big(\xi(x\underline{0})-\mu(x\underline{0})\big)^{2}.
$$

If ξ is a good predictor, then its predictions should be close to those made by
the optimal predictor µ, and thus St will be small.

$$
\mathrm {I f} \xi
$$

$$
\mu,
$$

$$
S_{t}
$$

Solomonoff (1978) was able to prove the following remarkable convergence
theorem:

2.7.1 Theorem. For any computable probability measure µ ∈Mc,

$$
\mu\in\mathcal{M}_{c}
$$

$$
\sum_{t=1}^{\infty}S_{t}\;\leq\;\frac{\ln2}{2}\thinspace K(\mu).
$$

That is, the total of all the prediction errors over the length of the infinite sequence ω is bounded by a constant. This implies rapid convergence for
any unknown hypothesis that can be described by a computable distribution
(for a precise analysis see Hutter, 2007a). This set includes all computable

$$
\omega
$$ hypotheses over binary strings, which is essentially the set of all well defined
hypotheses. If it were not for the fact that the universal prior ξ is not computable, Solomonoff induction would be the ultimate all purpose universal
predictor.

$$
\xi
$$

Although we will not present Solomonoff’s proof, the following highlights
the key step required to obtaining the convergence result. For any probability
measure µ the following relation can be proven,

$$
\mu
$$

$$
\sum_{t=1}^{n}S_{t}\;\leq\;\frac{1}{2}\sum_{\underline{{x}}\in\mathbb{B}^{n}}\mu(\underline{{x}})\ln\frac{\mu(\underline{{x}})}{\xi(\underline{{x}})}.
$$

This in fact holds for any semi-measure ξ, thus no special properties of the
universal distribution have been used up to this point in the proof. Now, by the
universal dominance property of ξ, we know that ∀x ∈ B∗: ξ(x)≥2−K(µ)µ(x).
Substituting this into the above equation,

$$
\xi,
$$

$$
\xi
$$

$$
\forall x\in\mathbb{B}^*:\xi(\underline{x})\geq2^{-K(\mu)}\mu(\underline{x})
$$

$$
\sum_{t=1}^{n}S_{t}\;\leq\;\frac{1}{2}\sum_{\underline{{x}}\in\mathbb{B}^{n}}\mu(\underline{{x}})\ln\frac{\mu(\underline{{x}})}{2^{-K(\mu)}\mu(\underline{{x}})}\;=\;\frac{\ln2}{2}K(\mu)\sum_{\underline{{x}}\in\mathbb{B}^{n}}\mu(\underline{{x}})\;=\;\frac{\ln2}{2}K(\mu).
$$

As this holds for all n ∈ N, the result follows. It is this application of
dominance to obtain powerful convergence results that lies at the heart of
Solomonoff induction, and indeed universal artificial intelligence in general.

$$
n\in\mathbb{N}
$$

Although Solomonoff induction is not computable and is thus impractical,
it nevertheless has many connections to practical principles and methods that
are used for inductive inference. Clearly, if we define a computable prior rather
than ξ, we recover normal Bayesian inference. If we define our prior to be uniform, for example by assuming that all models have the same complexity, then
the result is maximum a posteriori (MAP) estimation, which in turn is related
to maximum likelihood (ML) estimation. Relations can also be established to
Minimum Message Length (MML), Minimum Description Length (MDL), and
Maximum entropy (ME) based prediction (see Chapter 5 of Li and Vit´anyi,
1997). Thus, although Solomonoff induction does not yield a prediction algorithm itself, it does provide a theoretical framework that can be used to
understand various practical inductive inference methods. It is a kind of ideal,
but unattainable, model of optimal inductive inference.

$$
\xi,
$$

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
