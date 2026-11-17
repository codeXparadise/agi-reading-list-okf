---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/23-keeping-neural-networks-simple.md
source: ../../papers/23-keeping-neural-networks-simple.md
paper_title: Keeping Neural Networks Simple by Minimizing the Description Length of the Weights
sequence: 23
section: Abstract
section_role: abstract
section_index: 2
pages: []
topics: ["../../topics/minimum-description-length.md", "../../topics/regularization.md"]
description: "Supervised neural networks generalize well if there is much less information in the weights than there is in the output vectors of the training…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Abstract

> Section 2 of 17 from [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](../../papers/23-keeping-neural-networks-simple.md) · `abstract` · pages n/a

Supervised neural networks generalize well if there is much less information in the weights than there is in the output vectors of the training cases. So during learning, it is important to keep the weights simple by penalizing the amount of information they contain. The amount of information in a weight can be controlled by adding Gaussian noise and the noise level can be adapted during learning to optimize the trade-off between the expected squared error of the network and the amount of information in the weights. We describe a method of computing the derivatives of the expected squared error and of the amount of information in the noisy weights in a network that contains a layer of non-linear hidden units. Provided the output units are linear, the exact derivatives can be computed efficiently without time-consuming Monte Carlo simulations. The idea of minimizing the amount of information that is required to communicate the weights of a neural network leads to a number of interesting schemes for encoding the weights.

---

Full document: [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](../../papers/23-keeping-neural-networks-simple.md) · Page-level evidence: [paper-pages/23-keeping-neural-networks-simple](../../paper-pages/23-keeping-neural-networks-simple/index.md)
