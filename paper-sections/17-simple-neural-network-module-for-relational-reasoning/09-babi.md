---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/17-simple-neural-network-module-for-relational-reasoning.md
source: ../../papers/17-simple-neural-network-module-for-relational-reasoning.md
paper_title: A Simple Neural Network Module for Relational Reasoning
sequence: 17
section: 3.3 bAbI
section_role: other
section_index: 9
pages: [3, 4]
topics: ["../../topics/relational-reasoning.md", "../../topics/graph-neural-networks.md"]
description: "bAbI is a pure text-based QA dataset [41]. There are 20 tasks, each corresponding to a particular type of reasoning, such as deduction, induction, or…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.3 bAbI

> Section 9 of 22 from [17 - A Simple Neural Network Module for Relational Reasoning](../../papers/17-simple-neural-network-module-for-relational-reasoning.md) · `other` · pages 3-4

bAbI is a pure text-based QA dataset \[41\]. There are 20 tasks, each corresponding to a particular type of reasoning, such as deduction, induction, or counting. Each question is associated with a set of supporting facts. For example, the facts “Sandra picked up the football” and “Sandra went to the oﬃce” support the question “Where is the football?” (answer: “oﬃce”). A model succeeds on

a task if its performance surpasses 95%. Many memory-augmented neural networks have reported impressive results on bAbI. When training jointly on all tasks using 10K examples per task, Memory Networks pass 14/20, DNC 18/20, Sparse DNC 19/20, and EntNet 16/20 (the authors of EntNets report state-of-the-art at 20/20; however, unlike previously reported results this was not done with joint training on all tasks, where they instead achieve 16/20) \[42, 9, 34, 13\].

1The “Sort-of-CLEVR” dataset will be made publicly available online.

4

---

Full document: [17 - A Simple Neural Network Module for Relational Reasoning](../../papers/17-simple-neural-network-module-for-relational-reasoning.md) · Page-level evidence: [paper-pages/17-simple-neural-network-module-for-relational-reasoning](../../paper-pages/17-simple-neural-network-module-for-relational-reasoning/index.md)
