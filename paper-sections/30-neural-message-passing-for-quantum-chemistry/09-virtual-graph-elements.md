---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
source: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
paper_title: Neural Message Passing for Quantum Chemistry
sequence: 30
section: 5.2. Virtual Graph Elements
section_role: other
section_index: 9
pages: [4, 5]
topics: ["../../topics/graph-neural-networks.md", "../../topics/relational-reasoning.md"]
description: "We explored two different ways to change how the messages are passed throughout the model. The simplest modification involves adding a separate…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 5.2. Virtual Graph Elements

> Section 9 of 21 from [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md) · `other` · pages 4-5

We explored two different ways to change how the messages are passed throughout the model. The simplest modification involves adding a separate “virtual” edge type for pairs of nodes that are not connected. This can be implemented as a data preprocessing step and allows information to travel long distances during the propagation phase.

v and mout

v , this was also used in Li et al. (2016). When we apply this to undirected

## Neural Message Passing for Quantum Chemistry

We also experimented with using a latent “master” node, which is connected to every input node in the graph with a special edge type. The master node serves as a global scratch space that each node both reads from and writes to in every step of message passing. We allow the master node to have a separate node dimension dmaster, as well as separate weights for the internal update function (in our case a GRU). This allows information to travel long distances during the propagation phase. It also, in theory, allows additional model capacity (e.g. large values of dmaster) without a substantial hit in performance, as the complexity of the master node model is O(|E|d2 + nd2

Table 1. Atom Features

Feature Description

Atom type H, C, N, O, F (one-hot) Atomic number Number of protons (integer) Acceptor Accepts electrons (binary) Donor Donates electrons (binary) Aromatic In an aromatic system (binary) Hybridization sp, sp2, sp3 (one-hot or null) Number of Hydrogens (integer)

master).

n2d2/k

overall time complexity is O

, with some additional overhead due to the mixing network. For k = 8, n = 9 and d = 200 we see a factor of 2 speedup in inference time over a k = 1, n = 9, and d = 200 architecture. This variation would be most useful for larger molecules, for instance molecules from GDB-17 (Ruddigkeit et al., 2012).

---

Full document: [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md) · Page-level evidence: [paper-pages/30-neural-message-passing-for-quantum-chemistry](../../paper-pages/30-neural-message-passing-for-quantum-chemistry/index.md)
