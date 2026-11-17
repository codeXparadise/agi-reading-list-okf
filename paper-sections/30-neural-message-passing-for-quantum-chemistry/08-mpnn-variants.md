---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
source: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
paper_title: Neural Message Passing for Quantum Chemistry
sequence: 30
section: 5. MPNN Variants
section_role: other
section_index: 8
pages: [4]
topics: ["../../topics/graph-neural-networks.md", "../../topics/relational-reasoning.md"]
description: "We began our exploration of MPNNs around the GG-NN model which we believe to be a strong baseline. We focused on trying different message functions,…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 5. MPNN Variants

> Section 8 of 21 from [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md) · `other` · pages 4-4

We began our exploration of MPNNs around the GG-NN model which we believe to be a strong baseline. We focused on trying different message functions, output functions, finding the appropriate input representation, and properly tuning hyperparameters.

When we apply the above message functions to directed graphs, there are two separate functions used, M in and an M out. Which function is applied to a particular edge evw depends on the direction of that edge.

For the rest of the paper we use d to denote the dimension of the internal hidden representation of each node in the graph, and n to denote the number of nodes in the graph. Our implementation of MPNNs in general operates on directed graphs with a separate message channel for incoming and outgoing edges, in which case the incoming message mv is the concatenation of min

---

Full document: [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md) · Page-level evidence: [paper-pages/30-neural-message-passing-for-quantum-chemistry](../../paper-pages/30-neural-message-passing-for-quantum-chemistry/index.md)
