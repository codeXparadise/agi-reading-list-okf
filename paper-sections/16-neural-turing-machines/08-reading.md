---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/16-neural-turing-machines.md
source: ../../papers/16-neural-turing-machines.md
paper_title: Neural Turing Machines
sequence: 16
section: 3.1 Reading
section_role: other
section_index: 8
pages: [5]
topics: ["../../topics/memory-augmented-networks.md", "../../topics/recurrent-neural-networks.md"]
description: "Let Mt be the contents of the N × M memory matrix at time t, where N is the number of memory locations, and M is the vector size at each location.…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.1 Reading

> Section 8 of 25 from [16 - Neural Turing Machines](../../papers/16-neural-turing-machines.md) · `other` · pages 5-5

Let Mt be the contents of the N × M memory matrix at time t, where N is the number of memory locations, and M is the vector size at each location. Let wt be a vector of weightings over the N locations emitted by a read head at time t. Since all weightings are normalised, the N elements wt(i) of wt obey the following constraints:

X

wt(i) = 1, 0 ≤wt(i) ≤1, ∀i. (1)

i

The length M read vector rt returned by the head is defined as a convex combination of the row-vectors Mt(i) in memory:

X

rt ←−

wt(i)Mt(i), (2)

i

which is clearly differentiable with respect to both the memory and the weighting.

---

Full document: [16 - Neural Turing Machines](../../papers/16-neural-turing-machines.md) · Page-level evidence: [paper-pages/16-neural-turing-machines](../../paper-pages/16-neural-turing-machines/index.md)
