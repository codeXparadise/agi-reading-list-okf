---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/16-neural-turing-machines.md
source: ../../papers/16-neural-turing-machines.md
paper_title: Neural Turing Machines
sequence: 16
page: 7
pages: [7]
page_of: 26
topics: ["../../topics/memory-augmented-networks.md", "../../topics/recurrent-neural-networks.md"]
description: "3.3.1 Focusing by Content For content-addressing, each head (whether employed for reading or writing) first produces a length M key vector kt that is…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 7 of 26 - Neural Turing Machines

> Page 7 of the source PDF, verbatim as extracted. Canonical document: [16 - Neural Turing Machines](../../papers/16-neural-turing-machines.md)

## 3.3.1 Focusing by Content

For content-addressing, each head (whether employed for reading or writing) first produces a length M key vector kt that is compared to each vector Mt(i) by a similarity measure K

. The content-based system produces a normalised weighting wc

·, · 

t based on the similarity and a positive key strength, βt, which can amplify or attenuate the precision of the focus:

exp

βtK

kt, Mt(i)

wc

t(i) ←−

. (5)

P

j exp

βtK

kt, Mt(j)

In our current implementation, the similarity measure is cosine similarity:

= u · v ||u|| · ||v||. (6)

K

u, v

## 3.3.2 Focusing by Location

The location-based addressing mechanism is designed to facilitate both simple iteration across the locations of the memory and random-access jumps. It does so by implementing a rotational shift of a weighting. For example, if the current weighting focuses entirely on a single location, a rotation of 1 would shift the focus to the next location. A negative shift would move the weighting in the opposite direction.

Prior to rotation, each head emits a scalar interpolation gate gt in the range (0, 1). The value of g is used to blend between the weighting wt−1 produced by the head at the previous time-step and the weighting wc

t produced by the content system at the current time-step, yielding the gated weighting wg

t :

wg

t ←−gtwc

t + (1 −gt)wt−1. (7)

If the gate is zero, then the content weighting is entirely ignored, and the weighting from the previous time step is used. Conversely, if the gate is one, the weighting from the previous iteration is ignored, and the system applies content-based addressing.

After interpolation, each head emits a shift weighting st that defines a normalised distribution over the allowed integer shifts. For example, if shifts between -1 and 1 are allowed, st has three elements corresponding to the degree to which shifts of -1, 0 and 1 are performed. The simplest way to define the shift weightings is to use a softmax layer of the appropriate size attached to the controller. We also experimented with another technique, where the controller emits a single scalar that is interpreted as the lower bound of a width one uniform distribution over shifts. For example, if the shift scalar is 6.7, then st(6) = 0.3, st(7) = 0.7, and the rest of st is zero.

8

---

[previous page](page-006.md) · [next page](page-008.md) · [all pages](index.md)
