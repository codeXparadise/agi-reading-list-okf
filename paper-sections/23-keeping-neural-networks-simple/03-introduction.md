---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/23-keeping-neural-networks-simple.md
source: ../../papers/23-keeping-neural-networks-simple.md
paper_title: Keeping Neural Networks Simple by Minimizing the Description Length of the Weights
sequence: 23
section: 1 Introduction
section_role: introduction
section_index: 3
pages: []
topics: ["../../topics/minimum-description-length.md", "../../topics/regularization.md"]
description: "In many practical learning tasks there is little available training data so any reasonably complicated model will tend to overfit the data and give…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 1 Introduction

> Section 3 of 17 from [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](../../papers/23-keeping-neural-networks-simple.md) · `introduction` · pages n/a

In many practical learning tasks there is little available training data so any reasonably complicated model will tend to overfit the data and give poor generalization to new data. To avoid overfitting we need to ensure that there is less information in the weights than there is in the output vectors of the training cases. Researchers have considered many possible ways of limiting the information in the weights:

- Limit the number of connections in the network (and hope that each weight does not have too much information in it).
- Divide the connections into subsets, and force the weights within a subset to be identical. If this “weight-sharing” is based on an analysis of the natural symmetries of the task it can be very effective (Lang, Waibel and Hinton (1990); LeCun 1989).
- Quantize all the weights in the network so that a probability mass, $p$, can be assigned to each quantized value. The number of bits in a weight is then $-\log p$, provided we ignore the cost of defining the quantization. Unfortunately this method leads to a difficult search space because the cost of a weight does not have a smooth derivative.

---

Full document: [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](../../papers/23-keeping-neural-networks-simple.md) · Page-level evidence: [paper-pages/23-keeping-neural-networks-simple](../../paper-pages/23-keeping-neural-networks-simple/index.md)
