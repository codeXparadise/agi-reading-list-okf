---
type: Section
title: Core Architecture & Transformers
description: "The Transformer and the convolutional architectures that preceded and surround it: attention, scaling behaviour, ResNets and dilated convolutions."
tags: [section, curriculum]
papers: ["/papers/01-attention-is-all-you-need.md", "/papers/02-the-annotated-transformer.md", "/papers/03-scaling-laws-for-neural-language-models.md", "/papers/04-imagenet-classification-alexnet.md", "/papers/05-deep-residual-learning-resnet.md", "/papers/06-identity-mappings-in-deep-residual-networks.md", "/papers/07-multi-scale-context-aggregation-dilated-convolutions.md"]
status: stable
generated: { by: okf_builder/1.0, at: 2026-11-17T16:30:00Z }
verified: { by: process:okf-validator, at: 2026-11-17T16:30:00Z }
---

# Core Architecture & Transformers

The Transformer and the convolutional architectures that preceded and surround it: attention, scaling behaviour, ResNets and dilated convolutions.

## Papers

1. [01 - Attention Is All You Need](/papers/01-attention-is-all-you-need.md) - Ashish Vaswani, Noam Shazeer et al. (2017). Introduces the Transformer, an architecture built entirely from multi-head self-attention and positional encodings, with no recurrence or convolution.
2. [02 - The Annotated Transformer](/papers/02-the-annotated-transformer.md) - Alexander M. Rush (2018). A line-by-line, runnable reimplementation of the Transformer paper in PyTorch, with commentary that ties every equation to code.
3. [03 - Scaling Laws for Neural Language Models](/papers/03-scaling-laws-for-neural-language-models.md) - Jared Kaplan, Sam McCandlish et al. (2020). Shows that language-model loss falls as a smooth power law in model size, dataset size and compute, across many orders of magnitude.
4. [04 - ImageNet Classification with Deep Convolutional Neural Networks](/papers/04-imagenet-classification-alexnet.md) - Alex Krizhevsky, Ilya Sutskever et al. (2012). AlexNet: the 2012 ImageNet winner that made deep convolutional networks the default in vision and set off the modern deep learning era.
5. [05 - Deep Residual Learning for Image Recognition](/papers/05-deep-residual-learning-resnet.md) - Kaiming He, Xiangyu Zhang et al. (2015). ResNet: reformulates a layer as learning a residual on top of an identity mapping, which lets networks train at 100+ layers.
6. [06 - Identity Mappings in Deep Residual Networks](/papers/06-identity-mappings-in-deep-residual-networks.md) - Kaiming He, Xiangyu Zhang et al. (2016). The pre-activation follow-up to ResNet: an analysis of why identity shortcuts keep gradients healthy, and a redesign that makes very deep residual networks easier to optimise..
7. [07 - Multi-Scale Context Aggregation by Dilated Convolutions](/papers/07-multi-scale-context-aggregation-dilated-convolutions.md) - Fisher Yu, Vladlen Koltun (2015). Dilated (atrous) convolutions widen the receptive field exponentially without losing resolution or adding parameters.

## How to read this section

Read in the numbered order. Each paper links to what it builds on and what it enables, so you can follow the dependency arrows out of the section when a prerequisite sits elsewhere in the list.

## Related

- [All papers](/papers/index.md)
- [Bundle index](/)