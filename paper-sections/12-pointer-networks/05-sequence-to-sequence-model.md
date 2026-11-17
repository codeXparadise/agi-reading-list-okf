---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/12-pointer-networks.md
source: ../../papers/12-pointer-networks.md
paper_title: Pointer Networks
sequence: 12
section: 2.1 Sequence-to-Sequence Model
section_role: other
section_index: 5
pages: [1, 2]
topics: ["../../topics/sequence-to-sequence.md", "../../topics/attention.md"]
description: "Given a training pair, (P, CP), the sequence-to-sequence model computes the conditional probability p(CP|P; θ) using a parametric model (an RNN with…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.1 Sequence-to-Sequence Model

> Section 5 of 18 from [12 - Pointer Networks](../../papers/12-pointer-networks.md) · `other` · pages 1-2

Given a training pair, (P, CP), the sequence-to-sequence model computes the conditional probability p(CP|P; θ) using a parametric model (an RNN with parameters θ) to estimate the terms of the probability chain rule (also see Figure 1), i.e.

m(P) Y

p(CP|P; θ) =

pθ(Ci|C1, . . . , Ci−1, P; θ). (1)

i=1

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

---

Full document: [12 - Pointer Networks](../../papers/12-pointer-networks.md) · Page-level evidence: [paper-pages/12-pointer-networks](../../paper-pages/12-pointer-networks/index.md)
