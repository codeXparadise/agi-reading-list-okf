---
type: Topic
title: Minimum Description Length
description: The principle that the best model is the one that compresses the data shortest.
tags: [generalization, information-theory, topic]
papers: ["/papers/23-keeping-neural-networks-simple.md", "/papers/24-tutorial-minimum-description-length.md", "/papers/26-kolmogorov-complexity-and-algorithmic-randomness.md", "/papers/29-variational-lossy-autoencoder.md"]
status: stable
generated: { by: okf_builder/1.0, at: 2026-11-17T16:30:00Z }
verified: { by: process:okf-validator, at: 2026-11-17T16:30:00Z }
---

# Minimum Description Length

The principle that the best model is the one that compresses the data shortest.

## Why it matters in this list

MDL is the formal statement of Occam's razor, and the cleanest bridge between compression and generalisation in this list.

## Papers

- [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](/papers/23-keeping-neural-networks-simple.md) (1993) - Treats each weight as a distribution and penalises the number of bits needed to describe it, linking generalisation to compression.
- [24 - A Tutorial Introduction to the Minimum Description Length Principle](/papers/24-tutorial-minimum-description-length.md) (2004) - A readable tutorial on MDL: learning as finding the model that compresses the data shortest, with the theory of why that controls overfitting.
- [26 - Kolmogorov Complexity and Algorithmic Randomness](/papers/26-kolmogorov-complexity-and-algorithmic-randomness.md) (2017) - The standard graduate text on Kolmogorov complexity, randomness deficiency and the two-part-code view of a good model.
- [29 - Variational Lossy Autoencoder](/papers/29-variational-lossy-autoencoder.md) (2016) - Combines variational autoencoders with expressive autoregressive decoders and explicit control over what the latent code is allowed to keep, giving much sharper generative models and a clean information-theoretic reading of why..

## Related topics

[Regularization](/topics/regularization.md), [Kolmogorov Complexity](/topics/kolmogorov-complexity.md)