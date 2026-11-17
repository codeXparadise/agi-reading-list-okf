---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/23-keeping-neural-networks-simple.md
source: ../../papers/23-keeping-neural-networks-simple.md
paper_title: Keeping Neural Networks Simple by Minimizing the Description Length of the Weights
sequence: 23
section: 5.1 The expected description length of the weights
section_role: other
section_index: 6
pages: []
topics: ["../../topics/minimum-description-length.md", "../../topics/regularization.md"]
description: "We assume that the sender and the receiver have an agreed Gaussian prior distribution, $P$, for a given weight. After learning, the sender has a…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 5.1 The expected description length of the weights

> Section 6 of 17 from [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](../../papers/23-keeping-neural-networks-simple.md) · `other` · pages n/a

We assume that the sender and the receiver have an agreed Gaussian prior distribution, $P$, for a given weight. After learning, the sender has a Gaussian posterior distribution, $Q$, for the weight. We describe a method of communicating both the weights and the data misfits and show that using this method the number of bits required to communicate the posterior distribution of a weight is equal to the asymmetric divergence (the Kullback-Liebler distance) from $P$ to $Q$.

$$G(P, Q) = \int Q(w) \log \frac{Q(w)}{P(w)} dw$$

---

Full document: [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](../../papers/23-keeping-neural-networks-simple.md) · Page-level evidence: [paper-pages/23-keeping-neural-networks-simple](../../paper-pages/23-keeping-neural-networks-simple/index.md)
