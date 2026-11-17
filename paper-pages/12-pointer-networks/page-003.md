---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/12-pointer-networks.md
source: ../../papers/12-pointer-networks.md
paper_title: Pointer Networks
sequence: 12
page: 3
pages: [3]
page_of: 9
topics: ["../../topics/sequence-to-sequence.md", "../../topics/attention.md"]
description: "This model performs significantly better than the sequence-to-sequence model on the convex hull problem, but it is not applicable to problems where…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 3 of 9 - Pointer Networks

> Page 3 of the source PDF, verbatim as extracted. Canonical document: [12 - Pointer Networks](../../papers/12-pointer-networks.md)

This model performs significantly better than the sequence-to-sequence model on the convex hull problem, but it is not applicable to problems where the output dictionary size depends on the input.

Nevertheless, a very simple extension (or rather reduction) of the model allows us to do this easily.

## 2.3 Ptr-Net

We now describe a very simple modification of the attention model that allows us to apply the method to solve combinatorial optimization problems where the output dictionary size depends on the number of elements in the input sequence.

The sequence-to-sequence model of Section 2.1 uses a softmax distribution over a fixed sized output dictionary to compute p(Ci|C1, . . . , Ci−1, P) in Equation 1. Thus it cannot be used for our problems where the size of the output dictionary is equal to the length of the input sequence. To solve this problem we model p(Ci|C1, . . . , Ci−1, P) using the attention mechanism of Equation 3 as follows:

j = vT tanh(W1ej + W2di) j ∈(1, . . . , n)

ui

p(Ci|C1, . . . , Ci−1, P) = softmax(ui)

where softmax normalizes the vector ui (of length n) to be an output distribution over the dictionary of inputs, and v, W1, and W2 are learnable parameters of the output model. Here, we do not blend the encoder state ej to propagate extra information to the decoder, but instead, use ui

j as pointers to the input elements. In a similar way, to condition on Ci−1 as in Equation 1, we simply copy the corresponding PCi−1 as the input. Both our method and the attention model can be seen as an application of content-based attention mechanisms proposed in \[6, 5, 2\].

We also note that our approach specifically targets problems whose outputs are discrete and correspond to positions in the input. Such problems may be addressed artificially – for example we could learn to output the coordinates of the target point directly using an RNN. However, at inference, this solution does not respect the constraint that the outputs map back to the inputs exactly. Without the constraints, the predictions are bound to become blurry over longer sequences as shown in sequence-to-sequence models for videos \[12\].

## 3 Motivation and Datasets Structure

In the following sections, we review each of the three problems we considered, as well as our data generation protocol.1

In the training data, the inputs are planar point sets P = {P1, . . . , Pn} with n elements each, where Pj = (xj, yj) are the cartesian coordinates of the points over which we find the convex hull, the Delaunay triangulation or the solution to the corresponding Travelling Salesman Problem. In all cases, we sample from a uniform distribution in \[0, 1\] × \[0, 1\]. The outputs CP = {C1, . . . , Cm(P)} are sequences representing the solution associated to the point set P. In Figure 2, we find an illustration of an input/output pair (P, CP) for the convex hull and the Delaunay problems.

## 3.1 Convex Hull

We used this example as a baseline to develop our models and to understand the difficulty of solving combinatorial problems with data driven approaches. Finding the convex hull of a finite number of points is a well understood task in computational geometry, and there are several exact solutions available (see \[13, 14, 15\]). In general, finding the (generally unique) solution has complexity O(n log n), where n is the number of points considered.

The vectors Pj are uniformly sampled from \[0, 1\] × \[0, 1\]. The elements Ci are indices between 1 and n corresponding to positions in the sequence P, or special tokens representing beginning or end of sequence. See Figure 2 (a) for an illustration. To represent the output as a sequence, we start from the point with the lowest index, and go counter-clockwise – this is an arbitrary choice but helps reducing ambiguities during training.

1We release all the datasets at http://goo.gl/NDcOIG.

---

[previous page](page-002.md) · [next page](page-004.md) · [all pages](index.md)
