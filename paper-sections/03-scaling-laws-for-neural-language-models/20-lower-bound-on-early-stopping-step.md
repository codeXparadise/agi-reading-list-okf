---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/03-scaling-laws-for-neural-language-models.md
source: ../../papers/03-scaling-laws-for-neural-language-models.md
paper_title: Scaling Laws for Neural Language Models
sequence: 3
section: 5.3 Lower Bound on Early Stopping Step
section_role: other
section_index: 20
pages: [13]
topics: ["../../topics/scaling-laws.md", "../../topics/transformer-architecture.md", "../../topics/optimization.md"]
description: "The results for L(N, Smin) can be used to derive a lower-bound (and rough estimate) of the step at which early stopping should occur when training is…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 5.3 Lower Bound on Early Stopping Step

> Section 20 of 45 from [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md) · `other` · pages 13-13

The results for L(N, Smin) can be used to derive a lower-bound (and rough estimate) of the step at which early stopping should occur when training is data limited. It is motivated by the idea that finite and infinite D learning curves for a given model will be very similar until we reach Smin ≈Sstop. Thus overfitting should be proportional to the correction from simply ending training at Sstop. This will underestimate Sstop, because in reality the test loss will decrease more slowly when we have a finite D, and therefore we will require more training steps to reach the optimal test loss at finite D. This line of reasoning leads to the inequality

Sstop(N, D) ≳ Sc \[L(N, D) −L(N, ∞)\]1/αS (5.7)

where L(N, ∞) is the converged loss, evaluated with infinite available data. This inequality and its comparison to the empirical data is displayed in Figure 16 in the appendix. In that figure, the values of Sstop and L(N, D) are empirical (though Sstop is adjusted to mimic training at B ≫Bcrit), while L(N, ∞) is computed from the fit to L(N, D) evaluated at D = ∞.

---

Full document: [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md) · Page-level evidence: [paper-pages/03-scaling-laws-for-neural-language-models](../../paper-pages/03-scaling-laws-for-neural-language-models/index.md)
