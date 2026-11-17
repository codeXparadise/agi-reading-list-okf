---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/03-scaling-laws-for-neural-language-models.md
source: ../../papers/03-scaling-laws-for-neural-language-models.md
paper_title: Scaling Laws for Neural Language Models
sequence: 3
section: B.2 Efficient Training
section_role: other
section_index: 33
pages: [20, 21]
topics: ["../../topics/scaling-laws.md", "../../topics/transformer-architecture.md", "../../topics/optimization.md"]
description: "Now we assemble the implications of (B.3) and (B.4). First, note that inserting (B.4) into (B.3) yields 1 + αN αS L (Neﬀ, ∞) , (B.5) L (Neﬀ(C) , C) =…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# B.2 Efficient Training

> Section 33 of 45 from [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md) · `other` · pages 20-21

Now we assemble the implications of (B.3) and (B.4). First, note that inserting (B.4) into (B.3) yields

1 + αN αS

L (Neﬀ, ∞) , (B.5)

L (Neﬀ(C) , C) =

which implies that for compute-efficient training, we should train to a fixed percentage αN

αS ≈10% above the converged loss. Next, let’s determine how the optimal loss depends on the compute budget. Eliminating N yields a power-law dependence of performance on compute:

αC

Cc

L (C) =

(B.6)

C

where we defined

αC = 1/ (1/αS + 1/αB + 1/αN) ≈0.052 (B.7)

1/αS+1/αN  αS

1/αS

1 + αN αS

Cc = 6NcB∗Sc

. (B.8)

αN

Similarly, we can eliminate L to find N (C):

 C

αC/αN 

1/αN

N (C)

1 + αN αS

=

(B.9)

Nc

Cc

and

−1/αN  C

αC/αS

S (C) = Cc 6NcB∗

1 + αN αS

(B.10)

Cc

9There is a slight ambiguity here: we can imagine training either at a constant batch size B (Ltarget), or we could instead train at a variable batch size ˜B (L), where ˜B is the instantaneous critical batch size (as opposed to B, which is the averaged version). These two prescriptions result in the same number of steps, so we can ignore this subtlety (see \[MKAT18\]).

---

Full document: [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md) · Page-level evidence: [paper-pages/03-scaling-laws-for-neural-language-models](../../paper-pages/03-scaling-laws-for-neural-language-models/index.md)
