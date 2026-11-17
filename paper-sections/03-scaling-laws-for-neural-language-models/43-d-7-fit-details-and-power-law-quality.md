---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/03-scaling-laws-for-neural-language-models.md
source: ../../papers/03-scaling-laws-for-neural-language-models.md
paper_title: Scaling Laws for Neural Language Models
sequence: 3
section: D.7 Fit Details and Power Law Quality
section_role: other
section_index: 43
pages: [25]
topics: ["../../topics/scaling-laws.md", "../../topics/transformer-architecture.md", "../../topics/optimization.md"]
description: "We experimented with a number of functional forms for the fits to L(N), L(C), and L(D); the power-law fits were qualitatively much more accurate than…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# D.7 Fit Details and Power Law Quality

> Section 43 of 45 from [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md) · `other` · pages 25-25

We experimented with a number of functional forms for the fits to L(N), L(C), and L(D); the power-law fits were qualitatively much more accurate than other functions such as logarithms (see Figure 23).

For L(C), we do not include small models with only 1 layer in the fit, as the transition from 1 to 2 layers causes a noticable lump in the data. For L(N) we also do not include very small models with only 1 layer in the fit, and we exclude the largest models that have not trained fully to convergence. Fit parameters change marginally if we do include them, and the trend extrapolates well in both directions regardless.

---

Full document: [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md) · Page-level evidence: [paper-pages/03-scaling-laws-for-neural-language-models](../../paper-pages/03-scaling-laws-for-neural-language-models/index.md)
