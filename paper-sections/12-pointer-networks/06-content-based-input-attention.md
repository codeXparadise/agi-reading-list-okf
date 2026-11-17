---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/12-pointer-networks.md
source: ../../papers/12-pointer-networks.md
paper_title: Pointer Networks
sequence: 12
section: 2.2 Content Based Input Attention
section_role: other
section_index: 6
pages: [2, 3]
topics: ["../../topics/sequence-to-sequence.md", "../../topics/attention.md"]
description: "The vanilla sequence-to-sequence model produces the entire output sequence CP using the fixed dimensional state of the recognition RNN at the end of…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.2 Content Based Input Attention

> Section 6 of 18 from [12 - Pointer Networks](../../papers/12-pointer-networks.md) · `other` · pages 2-3

The vanilla sequence-to-sequence model produces the entire output sequence CP using the fixed dimensional state of the recognition RNN at the end of the input sequence P. This constrains the amount of information and computation that can flow through to the generative model. The attention model of \[5\] ameliorates this problem by augmenting the encoder and decoder RNNs with an additional neural network that uses an attention mechanism over the entire sequence of encoder RNN states.

For notation purposes, let us define the encoder and decoder hidden states as (e1, . . . , en) and (d1, . . . , dm(P)), respectively. For the LSTM RNNs, we use the state after the output gate has been component-wise multiplied by the cell activations. We compute the attention vector at each output time i as follows:

j = vT tanh(W1ej + W2di) j ∈(1, . . . , n)

ui

ai

j = softmax(ui

j) j ∈(1, . . . , n) (3)

n X

d′

ai

i =

jej

j=1

where softmax normalizes the vector ui (of length n) to be the “attention” mask over the inputs, and v, W1, and W2 are learnable parameters of the model. In all our experiments, we use the same hidden dimensionality at the encoder and decoder (typically 512), so v is a vector and W1 and W2 are square matrices. Lastly, d′

i and di are concatenated and used as the hidden states from which we make predictions and which we feed to the next time step in the recurrent model.

Note that for each output we have to perform n operations, so the computational complexity at inference time becomes O(n2).

This model performs significantly better than the sequence-to-sequence model on the convex hull problem, but it is not applicable to problems where the output dictionary size depends on the input.

Nevertheless, a very simple extension (or rather reduction) of the model allows us to do this easily.

---

Full document: [12 - Pointer Networks](../../papers/12-pointer-networks.md) · Page-level evidence: [paper-pages/12-pointer-networks](../../paper-pages/12-pointer-networks/index.md)
