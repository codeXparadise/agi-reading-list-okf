---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/03-scaling-laws-for-neural-language-models.md
source: ../../papers/03-scaling-laws-for-neural-language-models.md
paper_title: Scaling Laws for Neural Language Models
sequence: 3
page: 21
pages: [21]
page_of: 30
topics: ["../../topics/scaling-laws.md", "../../topics/transformer-architecture.md", "../../topics/optimization.md"]
description: "B.3 Comparison to Inefficient Typically, researchers train models until they appear to be close to convergence. In this section, we compare the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 21 of 30 - Scaling Laws for Neural Language Models

> Page 21 of the source PDF, verbatim as extracted. Canonical document: [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md)

## B.3 Comparison to Inefficient

Typically, researchers train models until they appear to be close to convergence. In this section, we compare the efficient training procedure described above to this more typical setup. We define a the convergence factor f as the percent deviation from the converged loss:

L (N, C) = (1 + f) L (N, ∞) . (B.11)

For compute-efficient training we have f = αN/αS ≈10% from the previous section, but researchers typically use a much smaller value. Here, we choose f ′ = 2% as an estimate. For a fixed value of the loss, we predict:

 1 + f

1/αN

Nf Nf ′ =

≈2.7 (B.12)

1 + f ′

!1/αS

1 + 1 f 1 + 1 f ′

Sf Sf ′ =

≈0.13 (B.13)

Cf Cf ′ = Nf

Sf Sf ′ ≈0.35 (B.14)

Nf ′

So that compute-efficient training uses 7.7x fewer parameter updates, 2.7x more parameters, and 65% less compute to reach the same loss.

## B.4 Suboptimal Model Sizes

We can solve A.1 to find an expression for the amount of compute needed to reach a given value of the loss L with a model of size N:

αN −1/αS

 

Nc

6B∗Sc N L1/αB

L −

C (N, L) =

. (B.15)

N

Using A.6 and A.9, we can eliminate L in favor of Neﬀ(L), the model size which reaches L most efficiently. From there, we find an expression for the excess compute needed as a consequence of using a suboptimal model size:

αN −1/αS

1 − Neﬀ

C (N, Neﬀ) C (Neﬀ, Neﬀ) = N Neﬀ

1 + αS αN

. (B.16)

N

The result is shown in Figure X. Models between 0.6x and 2.2x the optimal size can be used with only a 20% increase in compute budget. Using a smaller model is useful when accounting for the cost inference. A larger model can be trained the the same level of performance in fewer steps, allowing for more parallelism and faster training if sufficient harware is available (see Figure Y):

αN −1/αS

1 − Neﬀ

S (N, Neﬀ) S (Neﬀ, Neﬀ) =

1 + αS αN

. (B.17)

N

A 2.2x larger model requires 45% fewer steps at a cost of 20% more training compute. Note that this equation should not be trusted for very large models, as it is only valid in the power-law region of the learning curve after initial transient effects.

## C Caveats

In this section we list some potential caveats to our analysis.

• At present we do not have a solid theoretical understanding for any of our proposed scaling laws. The scaling relations with model size and compute are especially mysterious. It may be possible to understand scaling at very large D holding model size fixed \[AS17\], and also the shape of learning curves late in training, by modeling the loss with a noisy quadratic. But the scaling with D at very large model size still remains mysterious. Without a theory or a systematic understanding of the corrections to our scaling laws, it’s difficult to determine in what circumstances they can be trusted.

---

[previous page](page-020.md) · [next page](page-022.md) · [all pages](index.md)
