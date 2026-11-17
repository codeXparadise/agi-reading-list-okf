---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/23-keeping-neural-networks-simple.md
source: ../../papers/23-keeping-neural-networks-simple.md
paper_title: Keeping Neural Networks Simple by Minimizing the Description Length of the Weights
sequence: 23
section: 8 Implementation
section_role: experiments
section_index: 13
pages: []
topics: ["../../topics/minimum-description-length.md", "../../topics/regularization.md"]
description: "With an adaptive mixture of Gaussians coding-prior, the derivatives of the cost function are moderately complicated so it is easy to make an error in…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 8 Implementation

> Section 13 of 17 from [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](../../papers/23-keeping-neural-networks-simple.md) · `experiments` · pages n/a

With an adaptive mixture of Gaussians coding-prior, the derivatives of the cost function are moderately complicated so it is easy to make an error in implementing them. This is worrying because gradient descent algorithms are quite robust against minor errors. Also, it is hard to know how large to make the tables that are used for propagating Gaussian distributions through logistic functions or for backpropagating derivatives. To demonstrate that the implementation was correct and to decide the table sizes we used the following semantic check. We change each parameter by a small step and check that the cost function changes by the product of the gradient and step size. Using this method we found that a $300 \times 300$ table with linear interpolation gives reasonably accurate derivatives.

---

Full document: [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](../../papers/23-keeping-neural-networks-simple.md) · Page-level evidence: [paper-pages/23-keeping-neural-networks-simple](../../paper-pages/23-keeping-neural-networks-simple/index.md)
