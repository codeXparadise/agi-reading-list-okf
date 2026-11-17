---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/03-scaling-laws-for-neural-language-models.md
source: ../../papers/03-scaling-laws-for-neural-language-models.md
paper_title: Scaling Laws for Neural Language Models
sequence: 3
section: 2.1 Parameter and Compute Scaling of Transformers
section_role: other
section_index: 8
pages: [5, 6]
topics: ["../../topics/scaling-laws.md", "../../topics/transformer-architecture.md", "../../topics/optimization.md"]
description: "We parameterize the Transformer architecture using hyperparameters nlayer (number of layers), dmodel (dimension of the residual stream), dﬀ(dimension…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.1 Parameter and Compute Scaling of Transformers

> Section 8 of 45 from [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md) · `other` · pages 5-6

We parameterize the Transformer architecture using hyperparameters nlayer (number of layers), dmodel (dimension of the residual stream), dﬀ(dimension of the intermediate feed-forward layer), dattn (dimension of the attention output), and nheads (number of attention heads per layer). We include nctx tokens in the input context, with nctx = 1024 except where otherwise noted.

We use N to denote the model size, which we define as the number of non-embedding parameters

N ≈2dmodelnlayer (2dattn + dﬀ)

= 12nlayerd2

model with the standard dattn = dﬀ/4 = dmodel (2.1)

where we have excluded biases and other sub-leading terms. Our models also have nvocabdmodel parameters in an embedding matrix, and use nctxdmodel parameters for positional embeddings, but we do not include these when discussing the ‘model size’ N; we will see that this produces significantly cleaner scaling laws.

Evaluating a forward pass of the Transformer involves roughly

Cforward ≈2N + 2nlayernctxdmodel (2.2)

add-multiply operations, where the factor of two comes from the multiply-accumulate operation used in matrix multiplication. A more detailed per-operation parameter and compute count is included in Table 1.

---

Full document: [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md) · Page-level evidence: [paper-pages/03-scaling-laws-for-neural-language-models](../../paper-pages/03-scaling-laws-for-neural-language-models/index.md)
