---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/23-keeping-neural-networks-simple.md
source: ../../papers/23-keeping-neural-networks-simple.md
paper_title: Keeping Neural Networks Simple by Minimizing the Description Length of the Weights
sequence: 23
section: 7 A coding scheme that uses a mixture of Gaussians
section_role: other
section_index: 11
pages: []
topics: ["../../topics/minimum-description-length.md", "../../topics/regularization.md"]
description: "Suppose that a sender and a receiver have already agreed on a particular mixture of Gaussians distribution. The sender can now send a sample from the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 7 A coding scheme that uses a mixture of Gaussians

> Section 11 of 17 from [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](../../papers/23-keeping-neural-networks-simple.md) · `other` · pages n/a

Suppose that a sender and a receiver have already agreed on a particular mixture of Gaussians distribution. The sender can now send a sample from the posterior Gaussian distribution of a weight using the following coding scheme:

1. Randomly pick one of the Gaussians in the mixture with probability $r_i$ given by

$$r_i = \frac{\pi_i e^{-G_i}}{\sum_j \pi_j e^{-G_j}}$$

2. Communicate the choice of Gaussian to the receiver. If we use the mixing proportions as a prior for communicating the choice, the expected code cost is

$$\sum_i r_i \log \frac{1}{\pi_i}$$

3. Communicate the sample value to the receiver using the chosen Gaussian. If we take into account the random bits that we get back when the receiver reconstructs the posterior distribution from which the sample was chosen, the expected cost of communicating the sample is

$$\sum_i r_i G_i$$

So the expected cost of communicating both the choice of Gaussian and the sample value given that choice is

$$\sum_i r_i G_i + \sum_i r_i \log \frac{1}{\pi_i} = \sum_i r_i (-\log \pi_i e^{-G_i})$$

4. After receiving samples from all the posterior weight distributions and also receiving the errors on the training cases with these sampled weights, the receiver can run the learning algorithm and reconstruct the posterior distributions from which the weights are sampled. This allows the receiver to reconstruct all of the $G_i$ and hence to reconstruct the random bits used to choose a Gaussian from the mixture. So the number of “bits back” that must be subtracted from the expected cost in equation 21 is

$$H = \sum_i r_i \log \frac{1}{r_i}$$

We now use a lemma from statistical mechanics to get a simple expression for the expected code cost minus the bits back.

---

Full document: [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](../../papers/23-keeping-neural-networks-simple.md) · Page-level evidence: [paper-pages/23-keeping-neural-networks-simple](../../paper-pages/23-keeping-neural-networks-simple/index.md)
