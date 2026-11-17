---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/12-pointer-networks.md
source: ../../papers/12-pointer-networks.md
paper_title: Pointer Networks
sequence: 12
section: 5 Conclusions
section_role: conclusion
section_index: 16
pages: [7]
topics: ["../../topics/sequence-to-sequence.md", "../../topics/attention.md"]
description: "In this paper we described Ptr-Net, a new architecture that allows us to learn a conditional probability of one sequence CP given another sequence P,…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 5 Conclusions

> Section 16 of 18 from [12 - Pointer Networks](../../papers/12-pointer-networks.md) · `conclusion` · pages 7-7

In this paper we described Ptr-Net, a new architecture that allows us to learn a conditional probability of one sequence CP given another sequence P, where CP is a sequence of discrete tokens corresponding to positions in P. We show that Ptr-Nets can be used to learn solutions to three different combinatorial optimization problems. Our method works on variable sized inputs (yielding variable sized output dictionaries), something the baseline models (sequence-to-sequence with or without attention) cannot do directly. Even more impressively, they outperform the baselines on fixed input size problems - to which both the models can be applied.

Previous methods such as RNNSearch, Memory Networks and Neural Turing Machines \[5, 6, 2\] have used attention mechanisms to process inputs. However these methods do not directly address problems that arise with variable output dictionaries. We have shown that an attention mechanism can be applied to the output to solve such problems. In so doing, we have opened up a new class of problems to which neural networks can be applied without artificial assumptions. In this paper, we have applied this extension to RNNSearch, but the methods are equally applicable to Memory Networks and Neural Turing Machines.

Future work will try and show its applicability to other problems such as sorting where the outputs are chosen from the inputs. We are also excited about the possibility of using this approach to other combinatorial optimization problems.

---

Full document: [12 - Pointer Networks](../../papers/12-pointer-networks.md) · Page-level evidence: [paper-pages/12-pointer-networks](../../paper-pages/12-pointer-networks/index.md)
