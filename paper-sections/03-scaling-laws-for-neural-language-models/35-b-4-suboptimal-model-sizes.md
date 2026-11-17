---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/03-scaling-laws-for-neural-language-models.md
source: ../../papers/03-scaling-laws-for-neural-language-models.md
paper_title: Scaling Laws for Neural Language Models
sequence: 3
section: B.4 Suboptimal Model Sizes
section_role: other
section_index: 35
pages: [21]
topics: ["../../topics/scaling-laws.md", "../../topics/transformer-architecture.md", "../../topics/optimization.md"]
description: "We can solve A.1 to find an expression for the amount of compute needed to reach a given value of the loss L with a model of size N: αN −1/αS Nc…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# B.4 Suboptimal Model Sizes

> Section 35 of 45 from [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md) · `other` · pages 21-21

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

---

Full document: [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md) · Page-level evidence: [paper-pages/03-scaling-laws-for-neural-language-models](../../paper-pages/03-scaling-laws-for-neural-language-models/index.md)
