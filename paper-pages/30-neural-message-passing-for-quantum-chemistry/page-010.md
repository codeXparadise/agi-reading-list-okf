---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
source: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
paper_title: Neural Message Passing for Quantum Chemistry
sequence: 30
page: 10
pages: [10]
page_of: 14
topics: ["../../topics/graph-neural-networks.md", "../../topics/relational-reasoning.md"]
description: "Neural Message Passing for Quantum Chemistry Here ˜A = A + IN where A is the real valued adjacency matrix for an undirected graph G. Adding the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 10 of 14 - Neural Message Passing for Quantum Chemistry

> Page 10 of the source PDF, verbatim as extracted. Canonical document: [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md)

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

## 10.2. A More Detailed Description of the Quantum Properties

˜Lv,w,i,jxw,i

yv,j = σ





i=1,w=1

First there the four atomization energies.

N X

!

˜Lv,wxw

yv = σ

.

• Atomization energy at 0K U0 (eV): This is the energy required to break up the molecule into all of its constituent atoms if the molecule is at absolute zero. This calculation assumes that the molecules are held at fixed volume.

w=1

Relabelling yv as ht+1

v and xw as ht

w this last line can be interpreted as the message passing update in an MPNN where M(ht

w) = ˜Lv,wht

v, ht

w and U(ht

v, mt+1

v ) = σ(mt+1

v ).

• Atomization energy at room temperature U (eV): Like U0, this is the energy required to break up the molecule if it is at room temperature.

10.1.1. THE SPECIAL CASE OF KIPF AND WELLING (2016)

• Enthalpy of atomization at room temperature H (eV): The enthalpy of atomization is similar in spirit to the energy of atomization, U. However, unlike the energy this calculation assumes that the constituent molecules are held at fixed pressure.

Motivated as a first order approximation of the graph laplacian methods, Kipf & Welling (2016) propose the following layer-wise propagation rule:

˜D−1/2 ˜A ˜D−1/2HlW l

Hl+1 = σ

(7)

---

[previous page](page-009.md) · [next page](page-011.md) · [all pages](index.md)
