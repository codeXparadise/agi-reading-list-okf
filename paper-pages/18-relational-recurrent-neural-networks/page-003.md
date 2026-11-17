---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/18-relational-recurrent-neural-networks.md
source: ../../papers/18-relational-recurrent-neural-networks.md
paper_title: Relational Recurrent Neural Networks
sequence: 18
page: 3
pages: [3]
page_of: 18
topics: ["../../topics/relational-reasoning.md", "../../topics/memory-augmented-networks.md", "../../topics/recurrent-neural-networks.md"]
description: "3.2 Encoding new memories We assumed that we already had a matrix of memories M. Of course, memories instead need to be encoded as new inputs are…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 3 of 18 - Relational Recurrent Neural Networks

> Page 3 of the source PDF, verbatim as extracted. Canonical document: [18 - Relational Recurrent Neural Networks](../../papers/18-relational-recurrent-neural-networks.md)

## 3.2 Encoding new memories

We assumed that we already had a matrix of memories M. Of course, memories instead need to be encoded as new inputs are received. Suppose then that M is some randomly initialised memory. We can efficiently incorporate new information x into M with a simple modification to equation 1:

MW q(\[M; x\]W k)T

\[M; x\]W v, (2)

√

f M = softmax

dk

where we use \[M; x\] to denote the row-wise concatenation of M and x. Since we use \[M; x\] when computing the keys and values, and only M when computing the queries, f M is a matrix with same dimensionality as M. Thus, equation 2 is a memory-size preserving attention operation that includes attention over the memories and the new observations. Notably, we use the same attention operation to efficiently compute memory interactions and to incorporate new information.

We also note the possible utility of this operation when the memory consists of a single vector rather than a matrix. In this case the model may learn to pick and choose which information from the input should be written into the vector memory state by learning how to attend to the input, conditioned on what is contained in the memory already. This is possible in LSTMs via the gates, though at a different granularity. We return to this idea, and the possible compartmentalization that can occur via the heads even in the single-memory-slot case, in the discussion.

## 3.3 Introducing recurrence and embedding into an LSTM

Suppose we have a temporal dimension with new observations at each timestep, xt. Since M and f M are the same dimensionality, we can naively introduce recurrence by first randomly initialising M, and then updating it with f M at each timestep. We chose to do this by embedding this update into an LSTM. Suppose memory matrix M can be interpreted as a matrix of cell states, usually denoted as C, for a 2-dimensional LSTM. We can make the operations of individual memories mi nearly identical to those in a normal LSTM cell state as follows (subscripts are overloaded to denote the row from a matrix, and timestep; e.g., mi,t is the ith row from M at time t).

si,t = (hi,t−1, mi,t−1) (3)

fi,t = W fxt + U fhi,t−1 + bf (4)

ii,t = W ixt + U ihi,t−1 + bi (5) oi,t = W oxt + U ohi,t−1 + bo (6)

mi,t = σ(fi,t + ˜bf) ◦mi,t−1 + σ(ii,t) ◦gψ( emi,t) | {z } (7)

hi,t = σ(oi,t) ◦tanh(mi,t) (8) si,t+1 = (mi,t, hi,t) (9)

The underbrace denotes the modification to a standard LSTM. In practice we did not find output gates necessary – please see the url in the footnote for our Tensorflow implementation of this model in the Sonnet library 2, and for the exact formulation we used, including our choice for the gψ function (briefly, we found a row/memory-wise MLP with layer normalisation to work best). There is also an interesting opportunity to introduce a different kind of gating, which we call ‘memory’ gating, which resembles previous gating ideas \[24, 3\]. Instead of producing scalar gates for each individual unit (‘unit’ gating), we can produce scalar gates for each memory row by converting W f, W i, W o, U f, U i, and U o from weight matrices into weight vectors, and by replacing the element-wise product in the gating equations with scalar-vector multiplication.

Since parameters W f, W i, W o, U f, U i, U o, and ψ are shared for each mi, we can modify the number of memories without affecting the number of parameters. Thus, tuning the number of memories and the size of each memory can be used to balance the overall storage capacity (equal to the total number of units, or elements, in M) and the number of parameters (proportional to the dimensionality of mi). We find in our experiments that some tasks require more, but not necessarily larger, memories, and others such as language modeling require fewer, larger memories.

2https://github.com/deepmind/sonnet/blob/master/sonnet/python/modules/ relational\_memory.py

---

[previous page](page-002.md) · [next page](page-004.md) · [all pages](index.md)
