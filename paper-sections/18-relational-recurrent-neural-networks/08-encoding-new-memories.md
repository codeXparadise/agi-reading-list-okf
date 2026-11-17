---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/18-relational-recurrent-neural-networks.md
source: ../../papers/18-relational-recurrent-neural-networks.md
paper_title: Relational Recurrent Neural Networks
sequence: 18
section: 3.2 Encoding new memories
section_role: other
section_index: 8
pages: [3]
topics: ["../../topics/relational-reasoning.md", "../../topics/memory-augmented-networks.md", "../../topics/recurrent-neural-networks.md"]
description: "We assumed that we already had a matrix of memories M. Of course, memories instead need to be encoded as new inputs are received. Suppose then that M…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.2 Encoding new memories

> Section 8 of 25 from [18 - Relational Recurrent Neural Networks](../../papers/18-relational-recurrent-neural-networks.md) · `other` · pages 3-3

We assumed that we already had a matrix of memories M. Of course, memories instead need to be encoded as new inputs are received. Suppose then that M is some randomly initialised memory. We can efficiently incorporate new information x into M with a simple modification to equation 1:

MW q(\[M; x\]W k)T

\[M; x\]W v, (2)

√

f M = softmax

dk

where we use \[M; x\] to denote the row-wise concatenation of M and x. Since we use \[M; x\] when computing the keys and values, and only M when computing the queries, f M is a matrix with same dimensionality as M. Thus, equation 2 is a memory-size preserving attention operation that includes attention over the memories and the new observations. Notably, we use the same attention operation to efficiently compute memory interactions and to incorporate new information.

We also note the possible utility of this operation when the memory consists of a single vector rather than a matrix. In this case the model may learn to pick and choose which information from the input should be written into the vector memory state by learning how to attend to the input, conditioned on what is contained in the memory already. This is possible in LSTMs via the gates, though at a different granularity. We return to this idea, and the possible compartmentalization that can occur via the heads even in the single-memory-slot case, in the discussion.

---

Full document: [18 - Relational Recurrent Neural Networks](../../papers/18-relational-recurrent-neural-networks.md) · Page-level evidence: [paper-pages/18-relational-recurrent-neural-networks](../../paper-pages/18-relational-recurrent-neural-networks/index.md)
