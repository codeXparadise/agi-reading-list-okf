---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
source: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
paper_title: Neural Message Passing for Quantum Chemistry
sequence: 30
section: 10.1. Interpretation of Laplacian based models as MPNNs
section_role: other
section_index: 18
pages: [9, 10]
topics: ["../../topics/graph-neural-networks.md", "../../topics/relational-reasoning.md"]
description: "Ramakrishnan, Raghunathan, Dral, Pavlo O, Rupp, Matthias, and Von Lilienfeld, O Anatole. Quantum chemistry structures and properties of 134 kilo…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 10.1. Interpretation of Laplacian based models as MPNNs

> Section 18 of 21 from [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md) · `other` · pages 9-10

Ramakrishnan, Raghunathan, Dral, Pavlo O, Rupp, Matthias, and Von Lilienfeld, O Anatole. Quantum chemistry structures and properties of 134 kilo molecules. Scientific data, 1, 2014.

Another family of models defined in Defferrard et al. (2016), Bruna et al. (2013), Kipf & Welling (2016) can be interpreted as MPNNs. These models generalize the notion of convolutions a general graph G with N nodes. In the language of MPNNs, these models tend to have very simple message functions and are typically applied to much larger graphs such as social network data. We closely follow the notation defined in Bruna et al. (2013) equation (3.2). The model discussed in Defferrard et al. (2016) (equation 5)

Rogers, David and Hahn, Mathew. Extended-connectivity

fingerprints. Journal of chemical information and modeling, 50(5):742–754, 2010.

Ruddigkeit, Lars, Van Deursen, Ruud, Blum, Lorenz C,

and Reymond, Jean-Louis. Enumeration of 166 billion organic small molecules in the chemical universe

## Neural Message Passing for Quantum Chemistry

Here ˜A = A + IN where A is the real valued adjacency matrix for an undirected graph G. Adding the identity matrix IN corresponds to adding self loops to the graph. Also

and Kipf & Welling (2016) can be viewed as special cases. Given an adjacency matrix W ∈RN×N we define the graph Laplacian to be L = In −D−1/2WD−1/2 where D is the diagonal degree matrix with Dii = deg(vi). Let V denote the eigenvectors of L, ordered by eigenvalue. Let σ be a real valued nonlinearity (such as ReLU). We now define an operation which transforms an input vector x of size N × d1 to a vector y of size N × d2 (the full model can defined as stacking these operations).

j ˜Aij denotes the degree matrix for the graph with self loops, W l ∈RD×D is a layer-specific trainable weight matrix, and σ(·) denotes a real valued nonlinearity. Each Hl is a RN×D dimensional matrix indicating the D dimensional node states for the N nodes in the graph.

˜Dii = P

In what follows, given a matrix M we use M(v) to denote the row in M indexed by v (v will always correspond to a node in the graph G). Let L = ˜D−1/2 ˜A ˜D−1/2. To get the updated node state for node v we have

d1 X

!

V Fi,jV T xi

(j = 1 . . . d2) (6)

yj = σ

i=1

Hl+1

L(v)HlW l

Here yj and xi are all N dimensional vectors corresponding to a scalar feature at each node. The matrices Fi,j are all diagonal N × N matrices and contain all of the learned parameters in the layer. We now expand equation 6 in terms of the full N × d1 vector x and N × d2 vector y, using v and w to index nodes in the graph G and i, j to index the dimensions of the node states. In this way xw,i denotes the i’th dimension of node w, and yv,j denotes the j’th dimension of node v, furthermore we use xw to denote the d1 dimensional vector for node state w, and yv to denote the d2 dimensional vector for node v. Define the rank 4 tensor ˜L of dimension N × N × d1 × d2 where

(v) = σ

X

!

LvwHl

(w)W l

= σ

w

Relabelling the row vector Hl+1

(v) as an N dimensional column vector ht+1

v the above equation is equivalent to

!

(W l)T X

ht+1

Lvwht

(8)

v = σ

w

w

˜Lv,w,i,j = (V Fi,jV T )v,w. We will use ˜Li,j to denote the N × N dimensional matrix where (˜Li,j)v,w = ˜Lv,w,i,j and ˜Lv,w to denote the d1 × d2 dimensional matrix where (˜Lv,w)i,j = ˜Lv,w,i,j. Writing equation 6 in this notation we have

which is equivalent to a message function

w = ˜Avw(deg(v)deg(w))−1/2ht

Mt(ht

v, ht

w) = Lvwht

w,

and update function

v ) = σ((W t)T mt+1).

Ut(ht

v, mt+1

Note that the Lvw are all scalar valued, so this model corresponds to taking a certain weighted average of neighboring nodes at each time step.

d1 X

!

˜Li,jxi

yj = σ

i=1





d1,N X

---

Full document: [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md) · Page-level evidence: [paper-pages/30-neural-message-passing-for-quantum-chemistry](../../paper-pages/30-neural-message-passing-for-quantum-chemistry/index.md)
