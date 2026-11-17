---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/16-neural-turing-machines.md
source: ../../papers/16-neural-turing-machines.md
paper_title: Neural Turing Machines
sequence: 16
page: 6
pages: [6]
page_of: 26
topics: ["../../topics/memory-augmented-networks.md", "../../topics/recurrent-neural-networks.md"]
description: "Figure 2: Flow Diagram of the Addressing Mechanism. The key vector, kt, and key strength, βt, are used to perform content-based addressing of the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 6 of 26 - Neural Turing Machines

> Page 6 of the source PDF, verbatim as extracted. Canonical document: [16 - Neural Turing Machines](../../papers/16-neural-turing-machines.md)

Figure 2: Flow Diagram of the Addressing Mechanism. The key vector, kt, and key strength, βt, are used to perform content-based addressing of the memory matrix, Mt. The resulting content-based weighting is interpolated with the weighting from the previous time step based on the value of the interpolation gate, gt. The shift weighting, st, determines whether and by how much the weighting is rotated. Finally, depending on γt, the weighting is sharpened and used for memory access.

## 3.3 Addressing Mechanisms

Although we have now shown the equations of reading and writing, we have not described how the weightings are produced. These weightings arise by combining two addressing mechanisms with complementary facilities. The first mechanism, “content-based addressing,” focuses attention on locations based on the similarity between their current values and values emitted by the controller. This is related to the content-addressing of Hopfield networks (Hopfield, 1982). The advantage of content-based addressing is that retrieval is simple, merely requiring the controller to produce an approximation to a part of the stored data, which is then compared to memory to yield the exact stored value.

However, not all problems are well-suited to content-based addressing. In certain tasks the content of a variable is arbitrary, but the variable still needs a recognisable name or address. Arithmetic problems fall into this category: the variable x and the variable y can take on any two values, but the procedure f(x, y) = x × y should still be defined. A controller for this task could take the values of the variables x and y, store them in different addresses, then retrieve them and perform a multiplication algorithm. In this case, the variables are addressed by location, not by content. We call this form of addressing “location-based addressing.” Content-based addressing is strictly more general than location-based addressing as the content of a memory location could include location information inside it. In our experiments however, providing location-based addressing as a primitive operation proved essential for some forms of generalisation, so we employ both mechanisms concurrently.

Figure 2 presents a flow diagram of the entire addressing system that shows the order of operations for constructing a weighting vector when reading or writing.

7

---

[previous page](page-005.md) · [next page](page-007.md) · [all pages](index.md)
