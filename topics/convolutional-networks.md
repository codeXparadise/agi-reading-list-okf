---
type: Topic
title: Convolutional Networks
description: Weight-sharing architectures built for grid-structured data such as images.
tags: [architecture, topic, vision]
papers: ["/papers/04-imagenet-classification-alexnet.md", "/papers/05-deep-residual-learning-resnet.md", "/papers/06-identity-mappings-in-deep-residual-networks.md", "/papers/07-multi-scale-context-aggregation-dilated-convolutions.md"]
status: stable
generated: { by: okf_builder/1.0, at: 2026-11-17T16:30:00Z }
verified: { by: process:okf-validator, at: 2026-11-17T16:30:00Z }
---

# Convolutional Networks

Weight-sharing architectures built for grid-structured data such as images.

## Why it matters in this list

The CNN papers here are the ones that established deep learning empirically, and whose ideas (ReLU, dropout, residual streams) leaked into everything after.

## Papers

- [04 - ImageNet Classification with Deep Convolutional Neural Networks](/papers/04-imagenet-classification-alexnet.md) (2012) - AlexNet: the 2012 ImageNet winner that made deep convolutional networks the default in vision and set off the modern deep learning era.
- [05 - Deep Residual Learning for Image Recognition](/papers/05-deep-residual-learning-resnet.md) (2015) - ResNet: reformulates a layer as learning a residual on top of an identity mapping, which lets networks train at 100+ layers.
- [06 - Identity Mappings in Deep Residual Networks](/papers/06-identity-mappings-in-deep-residual-networks.md) (2016) - The pre-activation follow-up to ResNet: an analysis of why identity shortcuts keep gradients healthy, and a redesign that makes very deep residual networks easier to optimise..
- [07 - Multi-Scale Context Aggregation by Dilated Convolutions](/papers/07-multi-scale-context-aggregation-dilated-convolutions.md) (2015) - Dilated (atrous) convolutions widen the receptive field exponentially without losing resolution or adding parameters.

## Related topics

[Transformer Architecture](/topics/transformer-architecture.md), [Residual Connections](/topics/residual-connections.md), [Memory-Augmented Networks](/topics/memory-augmented-networks.md), [Graph Neural Networks](/topics/graph-neural-networks.md)