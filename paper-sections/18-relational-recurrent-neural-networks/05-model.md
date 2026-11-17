---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/18-relational-recurrent-neural-networks.md
source: ../../papers/18-relational-recurrent-neural-networks.md
paper_title: Relational Recurrent Neural Networks
sequence: 18
section: 3 Model
section_role: method
section_index: 5
pages: [1]
topics: ["../../topics/relational-reasoning.md", "../../topics/memory-augmented-networks.md", "../../topics/recurrent-neural-networks.md"]
description: "Our guiding design principle is to provide an architectural backbone upon which a model can learn to compartmentalize information, and learn to…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3 Model

> Section 5 of 25 from [18 - Relational Recurrent Neural Networks](../../papers/18-relational-recurrent-neural-networks.md) · `method` · pages 1-1

Our guiding design principle is to provide an architectural backbone upon which a model can learn to compartmentalize information, and learn to compute interactions between compartmentalized information. To accomplish this we assemble building blocks from LSTMs, memory-augmented neural networks, and non-local networks (in particular, the Transformer seq2seq model \[22\]). Similar to memory-augmented architectures we consider a fixed set of memory slots; however, we allow for interactions between memory slots using an attention mechanism. As we will describe, in contrast to previous work we apply attention between memories at a single time step, and not across all previous representations computed from all previous observations.

---

Full document: [18 - Relational Recurrent Neural Networks](../../papers/18-relational-recurrent-neural-networks.md) · Page-level evidence: [paper-pages/18-relational-recurrent-neural-networks](../../paper-pages/18-relational-recurrent-neural-networks/index.md)
