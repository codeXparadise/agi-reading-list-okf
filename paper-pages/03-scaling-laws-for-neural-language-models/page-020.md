---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/03-scaling-laws-for-neural-language-models.md
source: ../../papers/03-scaling-laws-for-neural-language-models.md
paper_title: Scaling Laws for Neural Language Models
sequence: 3
page: 20
pages: [20]
page_of: 30
topics: ["../../topics/scaling-laws.md", "../../topics/transformer-architecture.md", "../../topics/optimization.md"]
description: "the compute budget. We start with the Equation (1.6), repeated here for convenience: αN αS Nc Sc L (N, S) = + . (B.1) N S Here, S represents the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 20 of 30 - Scaling Laws for Neural Language Models

> Page 20 of the source PDF, verbatim as extracted. Canonical document: [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md)

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

## B.2 Efficient Training

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

[previous page](page-019.md) · [next page](page-021.md) · [all pages](index.md)
