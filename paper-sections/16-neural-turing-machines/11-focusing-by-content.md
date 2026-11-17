---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/16-neural-turing-machines.md
source: ../../papers/16-neural-turing-machines.md
paper_title: Neural Turing Machines
sequence: 16
section: 3.3.1 Focusing by Content
section_role: other
section_index: 11
pages: [7]
topics: ["../../topics/memory-augmented-networks.md", "../../topics/recurrent-neural-networks.md"]
description: "For content-addressing, each head (whether employed for reading or writing) first produces a length M key vector kt that is compared to each vector…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.3.1 Focusing by Content

> Section 11 of 25 from [16 - Neural Turing Machines](../../papers/16-neural-turing-machines.md) · `other` · pages 7-7

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

---

Full document: [16 - Neural Turing Machines](../../papers/16-neural-turing-machines.md) · Page-level evidence: [paper-pages/16-neural-turing-machines](../../paper-pages/16-neural-turing-machines/index.md)
