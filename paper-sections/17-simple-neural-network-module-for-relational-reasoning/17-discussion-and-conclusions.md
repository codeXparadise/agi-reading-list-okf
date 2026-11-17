---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/17-simple-neural-network-module-for-relational-reasoning.md
source: ../../papers/17-simple-neural-network-module-for-relational-reasoning.md
paper_title: A Simple Neural Network Module for Relational Reasoning
sequence: 17
section: 6 Discussion and Conclusions
section_role: results
section_index: 17
pages: [8]
topics: ["../../topics/relational-reasoning.md", "../../topics/graph-neural-networks.md"]
description: "This work showed how the RN, a dedicated module for computing inter-entity relations, can be plugged into broader deep learning architectures to…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 6 Discussion and Conclusions

> Section 17 of 22 from [17 - A Simple Neural Network Module for Relational Reasoning](../../papers/17-simple-neural-network-module-for-relational-reasoning.md) · `results` · pages 8-8

This work showed how the RN, a dedicated module for computing inter-entity relations, can be plugged into broader deep learning architectures to substantially improve performance on tasks that demand rich relational reasoning. Our CLEVR results included super-human performance at 95.5% overall. Our bAbI results demonstrated broad reasoning capabilities, solving 18/20 tasks with no catastrophic failures. Together these results demonstrate the flexibility and power of this simple neural network building block.

One of the most interesting aspects of the work is that RN module inclusion in relatively simple CNN- and LSTM-based VQA architectures raised the performance on CLEVR from 68.5% to 95.5% and achieved state-of-the-art, super-human performance. We speculate that the RN provided a more powerful mechanism for flexible relational reasoning, and freed up the CNN to focus more exclusively on processing local spatial structure. This distinction between processing and reasoning is important. Powerful deep learning architectures, such as ResNets, are highly capable visual processors, but they may not be the most appropriate choice for reasoning about arbitrary relations.

A key contribution of this work is that the RN was able to induce, through the learning process, upstream processing to provide a set of useful object-like representations. Note, the input data and target objective functions did not specify any particular form or semantics of the internal object representations. This demonstrates the RN’s rich capacity for structured reasoning even with unstructured inputs and outputs.

Future work should apply RNs to a variety of problems that can benefit from structure learning and exploitation, such as rich scene understanding in RL agents, modeling social networks, and abstract problem solving. Future work could also improve the eﬃciency of RN computations. Though our results show that no knowledge about the particular relations among objects are necessary, RNs can exploit such knowledge if available or useful. For example, if two objects are known to have no actual relation, the RN’s computation of their relation can be omitted. An important direction is exercising this option in circumstances with strict computational constraints, where, for instance, attentional mechanisms could be used to filter unimportant relations and thus bound the otherwise quadratic complexity of the number of considered pairwise relations.

Relation Networks are a simple and powerful approach for learning to perform rich, structured reasoning in complex, real-world domains.

---

Full document: [17 - A Simple Neural Network Module for Relational Reasoning](../../papers/17-simple-neural-network-module-for-relational-reasoning.md) · Page-level evidence: [paper-pages/17-simple-neural-network-module-for-relational-reasoning](../../paper-pages/17-simple-neural-network-module-for-relational-reasoning/index.md)
