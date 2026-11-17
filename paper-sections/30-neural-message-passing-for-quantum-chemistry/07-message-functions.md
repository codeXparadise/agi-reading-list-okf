---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
source: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
paper_title: Neural Message Passing for Quantum Chemistry
sequence: 30
section: 5.1. Message Functions
section_role: other
section_index: 7
pages: [4]
topics: ["../../topics/graph-neural-networks.md", "../../topics/relational-reasoning.md"]
description: "Matrix Multiplication: We started with the message function used in GG-NN which is defined by the equation M(hv, hw, evw) = Aevwhw. Additionally,…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 5.1. Message Functions

> Section 7 of 21 from [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md) · `other` · pages 4-4

Matrix Multiplication: We started with the message function used in GG-NN which is defined by the equation M(hv, hw, evw) = Aevwhw.

Additionally, there are a number of properties that concern the states of the electrons in the molecule. They include the energy of the electron in the highest occupied molecular orbital (HOMO) εHOMO (eV), the energy of the lowest unoccupied molecular orbital (LUMO) εLUMO (eV), and the electron energy gap (∆ε (eV)). The electron energy gap is simply the difference εHOMO −εLUMO.

Edge Network: To allow vector valued edge features we propose the message function M(hv, hw, evw) = A(evw)hw where A(evw) is a neural network which maps the edge vector evw to a d × d matrix.

Pair Message: One property that the matrix multiplication rule has is that the message from node w to node v is a function only of the hidden state hw and the edge evw. In particular, it does not depend on the hidden state ht

Finally, there are several measures of the spatial distribution of electrons in the molecule. These include the electronic spatial extent ⟨R2⟩(Bohr2), the norm of the dipole moment µ (Debye), and the norm of static polarizability α (Bohr3). For a more detailed description of these properties, see the supplementary material.

v. In theory, a network may be able to use the message channel more efficiently if the node messages are allowed to depend on both the source and destination node. Thus we also tried using a variant on the message function as described in (Battaglia et al., 2016). Here the message from w to v along edge e is mwv = f (ht

w, ht

v, evw) where f is a neural network.

---

Full document: [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md) · Page-level evidence: [paper-pages/30-neural-message-passing-for-quantum-chemistry](../../paper-pages/30-neural-message-passing-for-quantum-chemistry/index.md)
