---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/02-the-annotated-transformer.md
source: ../../papers/02-the-annotated-transformer.md
paper_title: The Annotated Transformer
sequence: 2
section: Background
section_role: background
section_index: 3
pages: []
topics: ["../../topics/transformer-architecture.md", "../../topics/attention.md"]
description: "The goal of reducing sequential computation also forms the foundation of the Extended Neural GPU, ByteNet and ConvS2S, all of which use convolutional…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Background

> Section 3 of 28 from [02 - The Annotated Transformer](../../papers/02-the-annotated-transformer.md) · `background` · pages n/a

The goal of reducing sequential computation also forms the foundation of the
Extended Neural GPU, ByteNet and ConvS2S, all of which use convolutional neural
networks as basic building block, computing hidden representations in parallel
for all input and output positions. In these models, the number of operations
required to relate signals from two arbitrary input or output positions grows in
the distance between positions, linearly for ConvS2S and logarithmically for
ByteNet. This makes it more difficult to learn dependencies between distant
positions. In the Transformer this is reduced to a constant number of
operations, albeit at the cost of reduced effective resolution due to averaging
attention-weighted positions, an effect we counteract with Multi-Head Attention.

Self-attention, sometimes called intra-attention is an attention mechanism
relating different positions of a single sequence in order to compute a
representation of the sequence. Self-attention has been used successfully in a
variety of tasks including reading comprehension, abstractive summarization,
textual entailment and learning task-independent sentence representations. End-
to-end memory networks are based on a recurrent attention mechanism instead of
sequencealigned recurrence and have been shown to perform well on simple-
language question answering and
language modeling tasks.

To the best of our knowledge, however, the Transformer is the first transduction
model relying entirely on self-attention to compute representations of its input
and output without using sequence aligned RNNs or convolution.

---

Full document: [02 - The Annotated Transformer](../../papers/02-the-annotated-transformer.md) · Page-level evidence: [paper-pages/02-the-annotated-transformer](../../paper-pages/02-the-annotated-transformer/index.md)
