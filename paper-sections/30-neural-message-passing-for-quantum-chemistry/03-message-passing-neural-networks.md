---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
source: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
paper_title: Neural Message Passing for Quantum Chemistry
sequence: 30
section: 2. Message Passing Neural Networks
section_role: other
section_index: 3
pages: [1, 2, 3]
topics: ["../../topics/graph-neural-networks.md", "../../topics/relational-reasoning.md"]
description: "There are at least eight notable examples of models from the literature that we can describe using our Message Passing Neural Networks (MPNN)…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2. Message Passing Neural Networks

> Section 3 of 21 from [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md) · `other` · pages 1-3

There are at least eight notable examples of models from the literature that we can describe using our Message Passing Neural Networks (MPNN) framework. For simplicity we describe MPNNs which operate on undirected graphs G with node features xv and edge features evw. It is trivial to extend the formalism to directed multigraphs. The forward pass has two phases, a message passing phase and a readout phase. The message passing phase runs for T

1By comparison, the inference time of the neural networks discussed in this work is 300k times faster.

## Neural Message Passing for Quantum Chemistry

time steps and is defined in terms of message functions Mt and vertex update functions Ut. During the message passing phase, hidden states ht

Recurrent Unit introduced in Cho et al. (2014). This work used weight tying, so the same update function is used at each time step t. Finally,

v at each node in the graph are updated based on messages mt+1

v according to

X

i(h(T )

j(h(T )

v , h0

⊙

(4)

R =

σ

v)

v )

v∈V

X

mt+1

Mt(ht

v, ht

w, evw) (1)

v =

where i and j are neural networks, and ⊙denotes elementwise multiplication.

w∈N(v)

ht+1

v = Ut(ht

v, mt+1

v ) (2)

## Interaction Networks, Battaglia et al. (2016)

This work considered both the case where there is a target at each node in the graph, and where there is a graph level target. It also considered the case where there are node level effects applied at each time step, in such a case the update function takes as input the concatenation (hv, xv, mv) where xv is an external vector representing some outside influence on the vertex v. The message function M(hv, hw, evw) is a neural network which takes the concatenation (hv, hw, evw). The vertex update function U(hv, xv, mv) is a neural network which takes as input the concatenation (hv, xv, mv). Finally, in the case where there is a graph level output, R = f( P

where in the sum, N(v) denotes the neighbors of v in graph G. The readout phase computes a feature vector for the whole graph using some readout function R according to

ˆy = R({hT

v | v ∈G}). (3)

The message functions Mt, vertex update functions Ut, and readout function R are all learned differentiable functions. R operates on the set of node states and must be invariant to permutations of the node states in order for the MPNN to be invariant to graph isomorphism. In what follows, we define previous models in the literature by specifying the message function Mt, vertex update function Ut, and readout function R used. Note one could also learn edge features in an MPNN by introducing hidden states for all edges in the graph ht

hT

v ) where f is

v∈G

a neural network which takes the sum of the final hidden states hT

v . Note the original work only defined the model for T = 1.

evw and updating them analogously to equations 1 and 2. Of the existing MPNNs, only Kearnes et al. (2016) has used this idea.

## Molecular Graph Convolutions, Kearnes et al. (2016)

This work deviates slightly from other MPNNs in that it introduces edge representations et

## Convolutional Networks for Learning Molecular Fingerprints, Duvenaud et al. (2015)

vw which are updated during the message passing phase. The message function used for node messages is M(ht

The message function used is M(hv, hw, evw) = (hw, evw) where (., .) denotes concatenation. The vertex update function used is Ut(ht

v, ht

w, et

vw) = et

vw. The vertex update function is Ut(ht

v, mt+1

v ) = α(W1(α(W0ht

v), mt+1

v ) = σ(Hdeg(v)

v )) where (., .) denotes concatenation, α is the ReLU activation and W1, W0 are learned weight matrices. The edge state update is defined by et+1

v, mt+1

t mt+1

v ), where σ is the sigmoid function, deg(v) is the degree of vertex v and HN

t is a learned matrix for each time step t and vertex degree N. R has skip connections to all previous

vw = U ′

t(et

vw, ht

v, ht

w) = α(W4(α(W2, et

vw), α(W3(ht

v, ht

w)))) where the Wi are also learned weight matrices.

!

hidden states ht

softmax(Wtht

P

v and is equal to f

v)

,

v,t

## Deep Tensor Neural Networks, Sch¨utt et al. (2017)

where f is a neural network and Wt are learned readout matrices, one for each time step t. This message passing scheme may be problematic since the resulting message vector is mt+1

The message from w to v is computed by

w, P evw) , which separately sums over connected nodes and connected edges. It follows that the message passing implemented in Duvenaud et al. (2015) is unable to identify correlations between edge states and node states.

v = (P ht

W fc((W cfht

w + b1) ⊙(W dfevw + b2))

Mt = tanh

where W fc, W cf, W df are matrices and b1, b2 are bias vectors. The update function used is Ut(ht

v, mt+1

v ) = ht

v + mt+1

v . The readout function passes each node independently through a single hidden layer neural network and sums the outputs, in particular

## Gated Graph Neural Networks (GG-NN), Li et al. (2016)

X

NN(hT

R =

v ).

The message function used is Mt(ht

v, ht

w, evw) = Aevwht

w, where Aevw is a learned matrix, one for each edge label e (the model assumes discrete edge types). The update function is Ut = GRU(ht

v

### Laplacian Based Methods, Bruna et al. (2013); Defferrard et al. (2016); Kipf & Welling (2016)

v, mt+1

v ), where GRU is the Gated

## Neural Message Passing for Quantum Chemistry

These methods generalize the notion of the convolution operation typically applied to image datasets to an operation that operates on an arbitrary graph G with a real valued adjacency matrix A. The operations defined in Bruna et al. (2013); Defferrard et al. (2016) result in message functions of the form Mt(ht

up to 8 hours. Empirical potentials have been developed, such as the Stillinger-Weber potential (Stillinger & Weber, 1985), that are fast and accurate but must be created from scratch, from first principles, for every new composition of atoms.

v, ht

w) = Ct

vwht

w, where the matrices Ct

Hu et al. (2003) used neural networks to approximate a particularly troublesome term in DFT called the exchange correlation potential to improve the accuracy of DFT. However, their method fails to improve upon the efficiency of DFT and relies on a large set of ad hoc atomic descriptors.

vw are parameterized by the eigenvectors of the graph laplacian L, and the learned parameters of the model. The vertex update function used is Ut(ht

v, mt+1

v ) = σ(mt+1

v ) where σ is some pointwise non-linearity (such as ReLU).

The Kipf & Welling (2016) model results in a message function Mt(ht

Two more recent approaches by Behler & Parrinello (2007) and Rupp et al. (2012) attempt to approximate solutions to quantum mechanics directly without appealing to DFT. In the first case single-hidden-layer neural networks were used to approximate the energy and forces for configurations of a Silicon melt with the goal of speeding up molecular dynamics simulations. The second paper used Kernel Ridge Regression (KRR) to infer atomization energies over a wide range of molecules. In both cases hand engineered features were used (symmetry functions and the Coulomb matrix, respectively) that built physical symmetries into the input representation. Subsequent papers have replaced KRR by a neural network.

v, ht

w) = cvwht

w where cvw = (deg(v)deg(w))−1/2 Avw. The vertex update function is U t

v(ht

v, mt+1

v ) = ReLU(W tmt+1

v ). For the exact expressions for the Ct

vw and the derivation of the reformulation of these models as MPNNs, see the supplementary material.

---

Full document: [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md) · Page-level evidence: [paper-pages/30-neural-message-passing-for-quantum-chemistry](../../paper-pages/30-neural-message-passing-for-quantum-chemistry/index.md)
