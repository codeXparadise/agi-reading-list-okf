---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/16-neural-turing-machines.md
source: ../../papers/16-neural-turing-machines.md
paper_title: Neural Turing Machines
sequence: 16
section: 5 Conclusion
section_role: conclusion
section_index: 22
pages: [21, 22]
topics: ["../../topics/memory-augmented-networks.md", "../../topics/recurrent-neural-networks.md"]
description: "We have introduced the Neural Turing Machine, a neural network architecture that takes inspiration from both models of biological working memory and…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 5 Conclusion

> Section 22 of 25 from [16 - Neural Turing Machines](../../papers/16-neural-turing-machines.md) · `conclusion` · pages 21-22

We have introduced the Neural Turing Machine, a neural network architecture that takes inspiration from both models of biological working memory and the design of digital computers. Like conventional neural networks, the architecture is differentiable end-to-end and can be trained with gradient descent. Our experiments demonstrate that it is capable of learning simple algorithms from example data and of using these algorithms to generalise well outside its training regime.

22

Task #Heads Controller Size Memory Size Learning Rate #Parameters

Copy 1 100 128 × 20 10−4 67, 561 Repeat Copy 1 100 128 × 20 10−4 66, 111 Associative 1 100 128 × 20 10−4 70, 330 N-Grams 1 100 128 × 20 3 × 10−5 61, 749 Priority Sort 5 2 × 100 128 × 20 3 × 10−5 269, 038

---

Full document: [16 - Neural Turing Machines](../../papers/16-neural-turing-machines.md) · Page-level evidence: [paper-pages/16-neural-turing-machines](../../paper-pages/16-neural-turing-machines/index.md)
