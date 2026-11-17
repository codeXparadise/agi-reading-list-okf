---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/03-scaling-laws-for-neural-language-models.md
source: ../../papers/03-scaling-laws-for-neural-language-models.md
paper_title: Scaling Laws for Neural Language Models
sequence: 3
section: Operation Parameters FLOPs per Token
section_role: other
section_index: 9
pages: [6]
topics: ["../../topics/scaling-laws.md", "../../topics/transformer-architecture.md", "../../topics/optimization.md"]
description: "Embed (nvocab + nctx) dmodel 4dmodel Attention: QKV nlayerdmodel3dattn 2nlayerdmodel3dattn Attention: Mask — 2nlayernctxdattn Attention: Project…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Operation Parameters FLOPs per Token

> Section 9 of 45 from [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md) · `other` · pages 6-6

Embed (nvocab + nctx) dmodel 4dmodel

Attention: QKV nlayerdmodel3dattn 2nlayerdmodel3dattn

Attention: Mask — 2nlayernctxdattn

Attention: Project nlayerdattndmodel 2nlayerdattndembd

Feedforward nlayer2dmodeldﬀ 2nlayer2dmodeldﬀ

De-embed — 2dmodelnvocab

Total (Non-Embedding) N = 2dmodelnlayer (2dattn + dﬀ) Cforward = 2N + 2nlayernctxdattn

Table 1 Parameter counts and compute (forward pass) estimates for a Transformer model. Sub-leading terms such as nonlinearities, biases, and layer normalization are omitted.

For contexts and models with dmodel > nctx/12, the context-dependent computational cost per token is a relatively small fraction of the total compute. Since we primarily study models where dmodel ≫nctx/12, we do not include context-dependent terms in our training compute estimate. Accounting for the backwards pass (approximately twice the compute as the forwards pass), we then define the estimated non-embedding compute as C ≈6N floating point operators per training token.

---

Full document: [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md) · Page-level evidence: [paper-pages/03-scaling-laws-for-neural-language-models](../../paper-pages/03-scaling-laws-for-neural-language-models/index.md)
