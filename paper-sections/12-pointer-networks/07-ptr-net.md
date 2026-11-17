---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/12-pointer-networks.md
source: ../../papers/12-pointer-networks.md
paper_title: Pointer Networks
sequence: 12
section: 2.3 Ptr-Net
section_role: other
section_index: 7
pages: [3]
topics: ["../../topics/sequence-to-sequence.md", "../../topics/attention.md"]
description: "We now describe a very simple modification of the attention model that allows us to apply the method to solve combinatorial optimization problems…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.3 Ptr-Net

> Section 7 of 18 from [12 - Pointer Networks](../../papers/12-pointer-networks.md) · `other` · pages 3-3

We now describe a very simple modification of the attention model that allows us to apply the method to solve combinatorial optimization problems where the output dictionary size depends on the number of elements in the input sequence.

The sequence-to-sequence model of Section 2.1 uses a softmax distribution over a fixed sized output dictionary to compute p(Ci|C1, . . . , Ci−1, P) in Equation 1. Thus it cannot be used for our problems where the size of the output dictionary is equal to the length of the input sequence. To solve this problem we model p(Ci|C1, . . . , Ci−1, P) using the attention mechanism of Equation 3 as follows:

j = vT tanh(W1ej + W2di) j ∈(1, . . . , n)

ui

p(Ci|C1, . . . , Ci−1, P) = softmax(ui)

where softmax normalizes the vector ui (of length n) to be an output distribution over the dictionary of inputs, and v, W1, and W2 are learnable parameters of the output model. Here, we do not blend the encoder state ej to propagate extra information to the decoder, but instead, use ui

j as pointers to the input elements. In a similar way, to condition on Ci−1 as in Equation 1, we simply copy the corresponding PCi−1 as the input. Both our method and the attention model can be seen as an application of content-based attention mechanisms proposed in \[6, 5, 2\].

We also note that our approach specifically targets problems whose outputs are discrete and correspond to positions in the input. Such problems may be addressed artificially – for example we could learn to output the coordinates of the target point directly using an RNN. However, at inference, this solution does not respect the constraint that the outputs map back to the inputs exactly. Without the constraints, the predictions are bound to become blurry over longer sequences as shown in sequence-to-sequence models for videos \[12\].

---

Full document: [12 - Pointer Networks](../../papers/12-pointer-networks.md) · Page-level evidence: [paper-pages/12-pointer-networks](../../paper-pages/12-pointer-networks/index.md)
