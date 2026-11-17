---
type: Topic
title: Regularization
description: Techniques that trade training fit for generalisation.
tags: [generalization, topic, training]
papers: ["/papers/04-imagenet-classification-alexnet.md", "/papers/11-recurrent-neural-network-regularization.md", "/papers/21-dropout-regularization.md", "/papers/23-keeping-neural-networks-simple.md"]
status: stable
generated: { by: okf_builder/1.0, at: 2026-11-17T16:30:00Z }
verified: { by: process:okf-validator, at: 2026-11-17T16:30:00Z }
---

# Regularization

Techniques that trade training fit for generalisation.

## Why it matters in this list

Dropout, weight noise and description-length penalties are three views of the same instinct: prefer the simpler explanation.

## Papers

- [04 - ImageNet Classification with Deep Convolutional Neural Networks](/papers/04-imagenet-classification-alexnet.md) (2012) - AlexNet: the 2012 ImageNet winner that made deep convolutional networks the default in vision and set off the modern deep learning era.
- [11 - Recurrent Neural Network Regularization](/papers/11-recurrent-neural-network-regularization.md) (2014) - Shows how to apply dropout to LSTMs correctly - on the non-recurrent connections only - which is what made regularised RNNs competitive on language modelling and translation..
- [21 - Dropout: A Simple Way to Prevent Neural Networks from Overfitting](/papers/21-dropout-regularization.md) (2014) - Randomly dropping units during training, read as training an ensemble of thinned networks.
- [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](/papers/23-keeping-neural-networks-simple.md) (1993) - Treats each weight as a distribution and penalises the number of bits needed to describe it, linking generalisation to compression.

## Related topics

[Scaling Laws](/topics/scaling-laws.md), [Optimization](/topics/optimization.md), [Minimum Description Length](/topics/minimum-description-length.md), [Pipeline Parallelism](/topics/pipeline-parallelism.md)