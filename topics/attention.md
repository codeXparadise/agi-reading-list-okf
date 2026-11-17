---
type: Topic
title: Attention
description: "A mechanism that lets a model weight the parts of its input it should look at, instead of compressing everything into one state vector."
tags: [attention, sequence-modelling, topic]
papers: ["/papers/01-attention-is-all-you-need.md", "/papers/02-the-annotated-transformer.md", "/papers/12-pointer-networks.md", "/papers/13-order-matters-sequence-to-sequence-for-sets.md", "/papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md"]
status: stable
generated: { by: okf_builder/1.0, at: 2026-11-17T16:30:00Z }
verified: { by: process:okf-validator, at: 2026-11-17T16:30:00Z }
---

# Attention

A mechanism that lets a model weight the parts of its input it should look at, instead of compressing everything into one state vector.

## Why it matters in this list

Attention began as a fix for the fixed-size bottleneck in encoder-decoder translation and became the only mechanism the Transformer needs.

## Papers

- [01 - Attention Is All You Need](/papers/01-attention-is-all-you-need.md) (2017) - Introduces the Transformer, an architecture built entirely from multi-head self-attention and positional encodings, with no recurrence or convolution.
- [02 - The Annotated Transformer](/papers/02-the-annotated-transformer.md) (2018) - A line-by-line, runnable reimplementation of the Transformer paper in PyTorch, with commentary that ties every equation to code.
- [12 - Pointer Networks](/papers/12-pointer-networks.md) (2015) - Outputs are pointers into the input sequence rather than indices into a fixed vocabulary, so the model can solve variable-size combinatorial problems such as sorting, convex hull and the travelling salesman..
- [13 - Order Matters: Sequence to Sequence for Sets](/papers/13-order-matters-sequence-to-sequence-for-sets.md) (2015) - Reads an unordered set in one order and decodes in another, showing how input ordering and attention interact - and when a set-to-sequence model can learn an order-invariant solution..
- [14 - Neural Machine Translation by Jointly Learning to Align and Translate](/papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md) (2014) - Introduces attention: instead of squeezing the source sentence into one vector, the decoder learns where to look at each step.

## Related topics

[Recurrent Neural Networks](/topics/recurrent-neural-networks.md), [Long Short-Term Memory](/topics/long-short-term-memory.md), [Sequence to Sequence](/topics/sequence-to-sequence.md)