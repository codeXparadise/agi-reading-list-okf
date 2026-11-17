---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/17-simple-neural-network-module-for-relational-reasoning.md
source: ../../papers/17-simple-neural-network-module-for-relational-reasoning.md
paper_title: A Simple Neural Network Module for Relational Reasoning
sequence: 17
section: 5.3 Sort-of-CLEVR from pixels
section_role: other
section_index: 14
pages: [7]
topics: ["../../topics/relational-reasoning.md", "../../topics/graph-neural-networks.md"]
description: "The results so far led us to hypothesize that the diﬃculty in solving CLEVR lies in its heavy emphasis on relational reasoning, contrary to previous…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 5.3 Sort-of-CLEVR from pixels

> Section 14 of 22 from [17 - A Simple Neural Network Module for Relational Reasoning](../../papers/17-simple-neural-network-module-for-relational-reasoning.md) · `other` · pages 7-7

The results so far led us to hypothesize that the diﬃculty in solving CLEVR lies in its heavy emphasis on relational reasoning, contrary to previous claims that the diﬃculty lies in question parsing \[17\]. However, the questions in the CLEVR dataset are not categorized based on the degree to which they may be relational, making it hard to assess our hypothesis. Therefore, we use the Sort-of-CLEVR dataset which we explicitly designed to seperate out relational and non-relational questions (see Section 3.2).

We find that a CNN augmented with an RN achieves an accuracy above 94% for both relational and non-relational questions. However, a CNN augmented with an MLP only reached this performance on the non-relational questions, plateauing at 63% on the relational questions. This strongly indicates that models lacking a dedicated relational reasoning component struggle, or may even be completely incapable of solving tasks that require very simple relational reasoning. Augmenting these models with a relational module, like the RN, is suﬃcient to overcome this hurdle.

A simple “closest-to” or “furthest-from” relation is particularly revealing of a CNN+MLP’s lack of general reasoning capabilities (52.3% success). For these relations a model must gauge the distances between each object, and then compare each of these distances. Moreover, depending on the images, the relevant distance could be quite small in magnitude, or quite large, further increasing the combinatoric diﬃculty of this task.

---

Full document: [17 - A Simple Neural Network Module for Relational Reasoning](../../papers/17-simple-neural-network-module-for-relational-reasoning.md) · Page-level evidence: [paper-pages/17-simple-neural-network-module-for-relational-reasoning](../../paper-pages/17-simple-neural-network-module-for-relational-reasoning/index.md)
