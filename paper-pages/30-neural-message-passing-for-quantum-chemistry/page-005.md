---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
source: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
paper_title: Neural Message Passing for Quantum Chemistry
sequence: 30
page: 5
pages: [5]
page_of: 14
topics: ["../../topics/graph-neural-networks.md", "../../topics/relational-reasoning.md"]
description: "Neural Message Passing for Quantum Chemistry We also experimented with using a latent “master” node, which is connected to every input node in the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 5 of 14 - Neural Message Passing for Quantum Chemistry

> Page 5 of the source PDF, verbatim as extracted. Canonical document: [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md)

## Neural Message Passing for Quantum Chemistry

We also experimented with using a latent “master” node, which is connected to every input node in the graph with a special edge type. The master node serves as a global scratch space that each node both reads from and writes to in every step of message passing. We allow the master node to have a separate node dimension dmaster, as well as separate weights for the internal update function (in our case a GRU). This allows information to travel long distances during the propagation phase. It also, in theory, allows additional model capacity (e.g. large values of dmaster) without a substantial hit in performance, as the complexity of the master node model is O(|E|d2 + nd2

Table 1. Atom Features

Feature Description

Atom type H, C, N, O, F (one-hot) Atomic number Number of protons (integer) Acceptor Accepts electrons (binary) Donor Donates electrons (binary) Aromatic In an aromatic system (binary) Hybridization sp, sp2, sp3 (one-hot or null) Number of Hydrogens (integer)

master).

n2d2/k

overall time complexity is O

, with some additional overhead due to the mixing network. For k = 8, n = 9 and d = 200 we see a factor of 2 speedup in inference time over a k = 1, n = 9, and d = 200 architecture. This variation would be most useful for larger molecules, for instance molecules from GDB-17 (Ruddigkeit et al., 2012).

## 5.3. Readout Functions

We experimented with two readout functions. First is the readout function used in GG-NN, which is defined by equation 4. Second is a set2set model from Vinyals et al. (2015). The set2set model is specifically designed to operate on sets and should have more expressive power than simply summing the final node states. This model first applies a linear projection to each tuple (hT

v , xv) and then takes as input the set of projected tuples T = {(hT

## 6. Input Representation

v , xv)}. Then, after M steps of computation, the set2set model produces a graph level embedding q∗

There are a number of features available for each atom in a molecule which capture both properties of the electrons in the atom as well as the bonds that the atom participates in. For a list of all of the features see table 1. We experimented with making the hydrogen atoms explicit nodes in the graph (as opposed to simply including the count as a node feature), in which case graphs have up to 29 nodes. Note that having larger graphs significantly slows training time, in this case by a factor of roughly 10. For the adjacency matrix there are three edge representations used depending on the model.

t which is invariant to the order of the of the tuples T. We feed this embedding q∗

t through a neural network to produce the output.

## 5.4. Multiple Towers

One issue with MPNNs is scalability. In particular, a single step of the message passing phase for a dense graph requires O(n2d2) floating point multiplications. As n or d get large this can be computationally expensive. To address this issue we break the d dimensional node embeddings ht

v into k different d/k dimensional embeddings ht,k

v and run a propagation step on each of the k copies separately to get temporary embeddings {˜ht+1,k

Chemical Graph: In the abscence of distance information, adjacency matrix entries are discrete bond types: single, double, triple, or aromatic.

v , v ∈G}, using separate message and update functions for each copy. The k temporary embeddings of each node are then mixed together according to the equation

Distance bins: The matrix multiply message function assumes discrete edge types, so to include distance information we bin bond distances into 10 bins, the bins are obtained by uniformly partitioning the interval \[2, 6\] into 8 bins, followed by adding a bin \[0, 2\] and \[6, ∞\]. These bins were hand chosen by looking at a histogram of all distances. The adjacency matrix then has entries in an alphabet of size 14, indicating bond type for bonded atoms and distance bin for atoms that are not bonded. We found the distance for bonded atoms to be almost completely determined by bond type.

˜ht,1

v , ˜ht,2

v , . . . , ˜ht,k

ht,1

v , ht,2

v , . . . , ht,k

(5)

= g

v

v

where g denotes a neural network and (x, y, . . .) denotes concatenation, with g shared across all nodes in the graph. This mixing preserves the invariance to permutations of the nodes, while allowing the different copies of the graph to communicate with each other during the propagation phase. This can be advantageous in that it allows larger hidden states for the same number of parameters, which yields a computational speedup in practice. For example, when the message function is matrix multiplication (as in GG-NN) a propagation step of a single copy takes O

Raw distance feature: When using a message function which operates on vector valued edges, the entries of the adjacency matrix are then 5 dimensional, where the first dimension indicates the euclidean distance between the pair of atoms, and the remaining four are a one-hot encoding of

n2(d/k)2

time, and there are k copies, therefore the

---

[previous page](page-004.md) · [next page](page-006.md) · [all pages](index.md)
