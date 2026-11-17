---
type: Topic
title: Transformer Architecture
description: "The self-attention stack - multi-head attention, positional encodings, residual streams and layer norm - that underpins modern language models."
tags: [architecture, language-models, topic]
papers: ["/papers/01-attention-is-all-you-need.md", "/papers/02-the-annotated-transformer.md", "/papers/03-scaling-laws-for-neural-language-models.md"]
status: stable
generated: { by: okf_builder/1.0, at: 2026-11-17T16:30:00Z }
verified: { by: process:okf-validator, at: 2026-11-17T16:30:00Z }
---

# Transformer Architecture

The self-attention stack - multi-head attention, positional encodings, residual streams and layer norm - that underpins modern language models.

## Why it matters in this list

Every large language model in use today is a Transformer or a close relative, which is why this list puts the paper first and annotates it second.

## Papers

- [01 - Attention Is All You Need](/papers/01-attention-is-all-you-need.md) (2017) - Introduces the Transformer, an architecture built entirely from multi-head self-attention and positional encodings, with no recurrence or convolution.
- [02 - The Annotated Transformer](/papers/02-the-annotated-transformer.md) (2018) - A line-by-line, runnable reimplementation of the Transformer paper in PyTorch, with commentary that ties every equation to code.
- [03 - Scaling Laws for Neural Language Models](/papers/03-scaling-laws-for-neural-language-models.md) (2020) - Shows that language-model loss falls as a smooth power law in model size, dataset size and compute, across many orders of magnitude.

## Related topics

[Convolutional Networks](/topics/convolutional-networks.md), [Residual Connections](/topics/residual-connections.md), [Memory-Augmented Networks](/topics/memory-augmented-networks.md), [Graph Neural Networks](/topics/graph-neural-networks.md)