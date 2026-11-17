---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/12-pointer-networks.md
source: ../../papers/12-pointer-networks.md
paper_title: Pointer Networks
sequence: 12
page: 2
pages: [2]
page_of: 9
topics: ["../../topics/sequence-to-sequence.md", "../../topics/attention.md"]
description: "Here P = {P1, . . . , Pn} is a sequence of n vectors and CP = {C1, . . . , Cm(P)} is a sequence of m(P) indices, each between 1 and n. The parameters…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 2 of 9 - Pointer Networks

> Page 2 of the source PDF, verbatim as extracted. Canonical document: [12 - Pointer Networks](../../papers/12-pointer-networks.md)

Here P = {P1, . . . , Pn} is a sequence of n vectors and CP = {C1, . . . , Cm(P)} is a sequence of m(P) indices, each between 1 and n.

The parameters of the model are learnt by maximizing the conditional probabilities for the training set, i.e.

X

θ∗= arg max

log p(CP|P; θ), (2)

θ

P,CP

where the sum is over training examples.

As in \[1\], we use an Long Short Term Memory (LSTM) \[11\] to model pθ(Ci|C1, . . . , Ci−1, P; θ). The RNN is fed Pi at each time step, i, until the end of the input sequence is reached, at which time a special symbol, ⇒is input to the model. The model then switches to the generation mode until the network encounters the special symbol ⇐, which represents termination of the output sequence.

Note that this model makes no statistical independence assumptions. We use two separate RNNs (one to encode the sequence of vectors Pj, and another one to produce or decode the output symbols Ci). We call the former RNN the encoder and the latter the decoder or the generative RNN.

During inference, given a sequence P, the learnt parameters θ∗are used to select the sequence

ˆCP with the highest probability, i.e., ˆCP = arg max

CP p(CP|P; θ∗). Finding the optimal sequence ˆC

is computationally impractical because of the combinatorial number of possible output sequences. Instead we use a beam search procedure to find the best possible sequence given a beam size.

In this sequence-to-sequence model, the output dictionary size for all symbols Ci is fixed and equal to n, since the outputs are chosen from the input. Thus, we need to train a separate model for each n. This prevents us from learning solutions to problems that have an output dictionary with a size that depends on the input sequence length.

Under the assumption that the number of outputs is O(n) this model has computational complexity of O(n). However, exact algorithms for the problems we are dealing with are more costly. For example, the convex hull problem has complexity O(n log n). The attention mechanism (see Section 2.2) adds more “computational capacity” to this model.

## 2.2 Content Based Input Attention

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

---

[previous page](page-001.md) · [next page](page-003.md) · [all pages](index.md)
