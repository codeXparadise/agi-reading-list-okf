---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
source: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
paper_title: Neural Message Passing for Quantum Chemistry
sequence: 30
section: 5.4. Multiple Towers
section_role: other
section_index: 12
pages: [5, 6]
topics: ["../../topics/graph-neural-networks.md", "../../topics/relational-reasoning.md"]
description: "One issue with MPNNs is scalability. In particular, a single step of the message passing phase for a dense graph requires O(n2d2) floating point…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 5.4. Multiple Towers

> Section 12 of 21 from [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md) · `other` · pages 5-6

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

## Neural Message Passing for Quantum Chemistry

the bond type.

In table 2 we compare the performance of our best MPNN variant (denoted with enn-s2s) and the corresponding ensemble (denoted with enn-s2s-ens5) with the previous state of the art on this dataset as reported in Faber et al. (2017). For clarity the error ratios of the best non-ensemble models are shown in bold. This previous work performed a comparison study of several existing ML models for QM9 and we have taken care to use the same train, validation, and test split. These baselines include 5 different hand engineered molecular representations, which then get fed through a standard, off-the-shelf classifier. These input representations include the Coulomb Matrix (CM, Rupp et al. (2012)), Bag of Bonds (BoB, Hansen et al. (2015)), Bonds Angles, Machine Learning (BAML, Huang & von Lilienfeld (2016)), Extended Connectivity Fingerprints (ECPF4, Rogers & Hahn (2010)), and “Projected Histograms” (HDAD, Faber et al. (2017)) representations. In addition to these hand engineered features we include two existing baseline MPNNs, the Molecular Graph Convolutions model (GC) from Kearnes et al. (2016), and the original GG-NN model Li et al. (2016) trained with distance bins. Overall, our new MPNN achieves chemical accuracy on 11 out of 13 targets and state of the art on all 13 targets.

---

Full document: [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md) · Page-level evidence: [paper-pages/30-neural-message-passing-for-quantum-chemistry](../../paper-pages/30-neural-message-passing-for-quantum-chemistry/index.md)
