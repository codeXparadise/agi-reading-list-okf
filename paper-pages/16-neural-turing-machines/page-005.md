---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/16-neural-turing-machines.md
source: ../../papers/16-neural-turing-machines.md
paper_title: Neural Turing Machines
sequence: 16
page: 5
pages: [5]
page_of: 26
topics: ["../../topics/memory-augmented-networks.md", "../../topics/recurrent-neural-networks.md"]
description: "at each location. A head can thereby attend sharply to the memory at a single location or weakly to the memory at many locations. 3.1 Reading Let Mt…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 5 of 26 - Neural Turing Machines

> Page 5 of the source PDF, verbatim as extracted. Canonical document: [16 - Neural Turing Machines](../../papers/16-neural-turing-machines.md)

at each location. A head can thereby attend sharply to the memory at a single location or weakly to the memory at many locations.

## 3.1 Reading

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

## 3.2 Writing

Taking inspiration from the input and forget gates in LSTM, we decompose each write into two parts: an erase followed by an add.

Given a weighting wt emitted by a write head at time t, along with an erase vector et whose M elements all lie in the range (0, 1), the memory vectors Mt−1(i) from the previous time-step are modified as follows:

˜ Mt(i) ←−Mt−1(i) \[1 −wt(i)et\] , (3)

where 1 is a row-vector of all 1-s, and the multiplication against the memory location acts point-wise. Therefore, the elements of a memory location are reset to zero only if both the weighting at the location and the erase element are one; if either the weighting or the erase is zero, the memory is left unchanged. When multiple write heads are present, the erasures can be performed in any order, as multiplication is commutative.

Each write head also produces a length M add vector at, which is added to the memory after the erase step has been performed:

Mt(i) ←−˜ Mt(i) + wt(i) at. (4)

Once again, the order in which the adds are performed by multiple heads is irrelevant. The combined erase and add operations of all the write heads produces the final content of the memory at time t. Since both erase and add are differentiable, the composite write operation is differentiable too. Note that both the erase and add vectors have M independent components, allowing fine-grained control over which elements in each memory location are modified.

6

---

[previous page](page-004.md) · [next page](page-006.md) · [all pages](index.md)
