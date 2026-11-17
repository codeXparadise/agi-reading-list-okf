---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/23-keeping-neural-networks-simple.md
source: ../../papers/23-keeping-neural-networks-simple.md
paper_title: Keeping Neural Networks Simple by Minimizing the Description Length of the Weights
sequence: 23
section: 6 Letting the data determine the prior
section_role: other
section_index: 9
pages: []
topics: ["../../topics/minimum-description-length.md", "../../topics/regularization.md"]
description: "So far, we have assumed that the “prior” distribution that is used for coding the weights is a single Gaussian. This coding-prior must be known to…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 6 Letting the data determine the prior

> Section 9 of 17 from [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](../../papers/23-keeping-neural-networks-simple.md) · `other` · pages n/a

So far, we have assumed that the “prior” distribution that is used for coding the weights is a single Gaussian. This coding-prior must be known to both the sender and the receiver before the weights are communicated. If we fix its mean and variance in advance we could pick inappropriate values that make it very expensive to code the actual weights. We therefore allow the mean and variance of the coding-prior to be determined during the optimization process, so the coding-prior depends on the data. This is a funny kind of prior! We could try to make sense of it in Bayesian terms by assuming that we start with a hyper-prior that specifies probability distributions for the mean and variance of the coding-prior and then we use the hyper-prior and the data to find the best coding-prior. This would automatically take into account the cost of communicating the coding-prior to a receiver who only knows the hyper-prior. In practice, we just ignore the cost of communicating the two parameters of the coding-prior so we do not need to invent hyper-priors.

---

Full document: [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](../../papers/23-keeping-neural-networks-simple.md) · Page-level evidence: [paper-pages/23-keeping-neural-networks-simple](../../paper-pages/23-keeping-neural-networks-simple/index.md)
