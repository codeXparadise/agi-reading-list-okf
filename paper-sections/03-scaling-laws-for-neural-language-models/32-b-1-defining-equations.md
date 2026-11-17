---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/03-scaling-laws-for-neural-language-models.md
source: ../../papers/03-scaling-laws-for-neural-language-models.md
paper_title: Scaling Laws for Neural Language Models
sequence: 3
section: B.1 Defining Equations
section_role: other
section_index: 32
pages: [19, 20]
topics: ["../../topics/scaling-laws.md", "../../topics/transformer-architecture.md", "../../topics/optimization.md"]
description: "The power-law fit to the learning curves implies a simple prescription for compute-efficient training. In this appendix, we will derive the optimal…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# B.1 Defining Equations

> Section 32 of 45 from [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md) · `other` · pages 19-20

The power-law fit to the learning curves implies a simple prescription for compute-efficient training. In this appendix, we will derive the optimal performance, model size, and number of training steps as a function of

the compute budget. We start with the Equation (1.6), repeated here for convenience:

αN

αS

Nc

Sc

L (N, S) =

+

. (B.1)

N

S

Here, S represents the number of parameter updates when training at the critical batch size \[MKAT18\], which was defined in Equation (5.2)9:

B (L) = B∗ L1/αB . (B.2)

We would like to determine optimal training parameters for a fixed compute budget, so we replace S = C/ (6NB (L)), where C is the number of FLOPs used in the training run:

αN

αS

Nc

6B∗Sc N L1/αBC

L (N, C) =

+

. (B.3)

N

Now, we set ∂NL

C = 0 to find the condition for optimality:

0 = ∂L ∂N

C

αN

αS 

1 −5N L ∂L ∂N

Nc

= −αN

+ αS

6B∗Sc N L1/αBC

C

N

N

N

αN

αS

Nc

=⇒αN

6B∗Sc N L1/αBC

=

(B.4)

αS

N

Equation (B.3) and (B.4) together determine the compute-efficient frontier.

---

Full document: [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md) · Page-level evidence: [paper-pages/03-scaling-laws-for-neural-language-models](../../paper-pages/03-scaling-laws-for-neural-language-models/index.md)
