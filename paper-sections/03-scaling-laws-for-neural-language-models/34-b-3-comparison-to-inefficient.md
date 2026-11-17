---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/03-scaling-laws-for-neural-language-models.md
source: ../../papers/03-scaling-laws-for-neural-language-models.md
paper_title: Scaling Laws for Neural Language Models
sequence: 3
section: B.3 Comparison to Inefficient
section_role: other
section_index: 34
pages: [21]
topics: ["../../topics/scaling-laws.md", "../../topics/transformer-architecture.md", "../../topics/optimization.md"]
description: "Typically, researchers train models until they appear to be close to convergence. In this section, we compare the efficient training procedure…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# B.3 Comparison to Inefficient

> Section 34 of 45 from [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md) · `other` · pages 21-21

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

---

Full document: [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md) · Page-level evidence: [paper-pages/03-scaling-laws-for-neural-language-models](../../paper-pages/03-scaling-laws-for-neural-language-models/index.md)
