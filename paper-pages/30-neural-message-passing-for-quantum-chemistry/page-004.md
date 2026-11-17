---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
source: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
paper_title: Neural Message Passing for Quantum Chemistry
sequence: 30
page: 4
pages: [4]
page_of: 14
topics: ["../../topics/graph-neural-networks.md", "../../topics/relational-reasoning.md"]
description: "Neural Message Passing for Quantum Chemistry like organic molecules that span a wide range of chemistry. For each molecule DFT is used to find a…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 4 of 14 - Neural Message Passing for Quantum Chemistry

> Page 4 of the source PDF, verbatim as extracted. Canonical document: [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md)

## Neural Message Passing for Quantum Chemistry

like organic molecules that span a wide range of chemistry. For each molecule DFT is used to find a reasonable low energy structure and hence atom “positions” are available. Additionally a wide range of interesting and fundamental chemical properties are computed. Given how fundamental some of the QM9 properties are, it is hard to believe success on more challenging chemical tasks will be possible if we can’t make accurate statistical predictions for the properties computed in QM9.

chemical graphs we treat the graph as directed, where each original edge becomes both an incoming and outgoing edge with the same label. Note there is nothing special about the direction of the edge, it is only relevant for parameter tying. Treating undirected graphs as directed means that the size of the message channel is 2d instead of d.

The input to our MPNN model is a set of feature vectors for the nodes of the graph, xv, and an adjacency matrix A with vector valued entries to indicate different bonds in the molecule as well as pairwise spatial distance between two atoms. We experimented as well with the message function used in the GG-NN family, which assumes discrete edge labels, in which case the matrix A has entries in a discrete alphabet of size k. The initial hidden states h0

We can group the different properties we try to predict into four broad categories. First, we have four properties related to how tightly bound together the atoms in a molecule are. These measure the energy required to break up the molecule at different temperatures and pressures. These include the atomization energy at 0K, U0 (eV), atomization energy at room temperature, U (eV), enthalpy of atomization at room temperature, H (eV), and free energy of atomization, G (eV).

v are set to be the atom input feature vectors xv and are padded up to some larger dimension d. All of our experiments used weight tying at each time step t, and a GRU (Cho et al., 2014) for the update function as in the GG-NN family.

Next there are properties related to fundamental vibrations of the molecule, including the highest fundamental vibrational frequency ω1 (cm−1) and the zero point vibrational energy (ZPVE) (eV).

## 5.1. Message Functions

Matrix Multiplication: We started with the message function used in GG-NN which is defined by the equation M(hv, hw, evw) = Aevwhw.

Additionally, there are a number of properties that concern the states of the electrons in the molecule. They include the energy of the electron in the highest occupied molecular orbital (HOMO) εHOMO (eV), the energy of the lowest unoccupied molecular orbital (LUMO) εLUMO (eV), and the electron energy gap (∆ε (eV)). The electron energy gap is simply the difference εHOMO −εLUMO.

Edge Network: To allow vector valued edge features we propose the message function M(hv, hw, evw) = A(evw)hw where A(evw) is a neural network which maps the edge vector evw to a d × d matrix.

Pair Message: One property that the matrix multiplication rule has is that the message from node w to node v is a function only of the hidden state hw and the edge evw. In particular, it does not depend on the hidden state ht

Finally, there are several measures of the spatial distribution of electrons in the molecule. These include the electronic spatial extent ⟨R2⟩(Bohr2), the norm of the dipole moment µ (Debye), and the norm of static polarizability α (Bohr3). For a more detailed description of these properties, see the supplementary material.

v. In theory, a network may be able to use the message channel more efficiently if the node messages are allowed to depend on both the source and destination node. Thus we also tried using a variant on the message function as described in (Battaglia et al., 2016). Here the message from w to v along edge e is mwv = f (ht

w, ht

v, evw) where f is a neural network.

## 5. MPNN Variants

We began our exploration of MPNNs around the GG-NN model which we believe to be a strong baseline. We focused on trying different message functions, output functions, finding the appropriate input representation, and properly tuning hyperparameters.

When we apply the above message functions to directed graphs, there are two separate functions used, M in and an M out. Which function is applied to a particular edge evw depends on the direction of that edge.

For the rest of the paper we use d to denote the dimension of the internal hidden representation of each node in the graph, and n to denote the number of nodes in the graph. Our implementation of MPNNs in general operates on directed graphs with a separate message channel for incoming and outgoing edges, in which case the incoming message mv is the concatenation of min

## 5.2. Virtual Graph Elements

We explored two different ways to change how the messages are passed throughout the model. The simplest modification involves adding a separate “virtual” edge type for pairs of nodes that are not connected. This can be implemented as a data preprocessing step and allows information to travel long distances during the propagation phase.

v and mout

v , this was also used in Li et al. (2016). When we apply this to undirected

---

[previous page](page-003.md) · [next page](page-005.md) · [all pages](index.md)
