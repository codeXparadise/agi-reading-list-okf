---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/16-neural-turing-machines.md
source: ../../papers/16-neural-turing-machines.md
paper_title: Neural Turing Machines
sequence: 16
section: 3.2 Writing
section_role: other
section_index: 9
pages: [5, 6]
topics: ["../../topics/memory-augmented-networks.md", "../../topics/recurrent-neural-networks.md"]
description: "Taking inspiration from the input and forget gates in LSTM, we decompose each write into two parts: an erase followed by an add. Given a weighting wt…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.2 Writing

> Section 9 of 25 from [16 - Neural Turing Machines](../../papers/16-neural-turing-machines.md) · `other` · pages 5-6

Taking inspiration from the input and forget gates in LSTM, we decompose each write into two parts: an erase followed by an add.

Given a weighting wt emitted by a write head at time t, along with an erase vector et whose M elements all lie in the range (0, 1), the memory vectors Mt−1(i) from the previous time-step are modified as follows:

˜ Mt(i) ←−Mt−1(i) \[1 −wt(i)et\] , (3)

where 1 is a row-vector of all 1-s, and the multiplication against the memory location acts point-wise. Therefore, the elements of a memory location are reset to zero only if both the weighting at the location and the erase element are one; if either the weighting or the erase is zero, the memory is left unchanged. When multiple write heads are present, the erasures can be performed in any order, as multiplication is commutative.

Each write head also produces a length M add vector at, which is added to the memory after the erase step has been performed:

Mt(i) ←−˜ Mt(i) + wt(i) at. (4)

Once again, the order in which the adds are performed by multiple heads is irrelevant. The combined erase and add operations of all the write heads produces the final content of the memory at time t. Since both erase and add are differentiable, the composite write operation is differentiable too. Note that both the erase and add vectors have M independent components, allowing fine-grained control over which elements in each memory location are modified.

6

Figure 2: Flow Diagram of the Addressing Mechanism. The key vector, kt, and key strength, βt, are used to perform content-based addressing of the memory matrix, Mt. The resulting content-based weighting is interpolated with the weighting from the previous time step based on the value of the interpolation gate, gt. The shift weighting, st, determines whether and by how much the weighting is rotated. Finally, depending on γt, the weighting is sharpened and used for memory access.

---

Full document: [16 - Neural Turing Machines](../../papers/16-neural-turing-machines.md) · Page-level evidence: [paper-pages/16-neural-turing-machines](../../paper-pages/16-neural-turing-machines/index.md)
