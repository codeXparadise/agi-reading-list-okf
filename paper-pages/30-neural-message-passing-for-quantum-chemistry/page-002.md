---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
source: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
paper_title: Neural Message Passing for Quantum Chemistry
sequence: 30
page: 2
pages: [2]
page_of: 14
topics: ["../../topics/graph-neural-networks.md", "../../topics/relational-reasoning.md"]
description: "Neural Message Passing for Quantum Chemistry time steps and is defined in terms of message functions Mt and vertex update functions Ut. During the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 2 of 14 - Neural Message Passing for Quantum Chemistry

> Page 2 of the source PDF, verbatim as extracted. Canonical document: [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md)

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

---

[previous page](page-001.md) · [next page](page-003.md) · [all pages](index.md)
