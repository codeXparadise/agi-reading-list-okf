---
type: Topic
title: Sequence to Sequence
description: Encoder-decoder models that map one sequence to another of arbitrary length.
tags: [sequence-modelling, topic, translation]
papers: ["/papers/01-attention-is-all-you-need.md", "/papers/10-sequence-to-sequence-learning.md", "/papers/12-pointer-networks.md", "/papers/13-order-matters-sequence-to-sequence-for-sets.md", "/papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md"]
status: stable
generated: { by: okf_builder/1.0, at: 2026-11-17T16:30:00Z }
verified: { by: process:okf-validator, at: 2026-11-17T16:30:00Z }
---

# Sequence to Sequence

Encoder-decoder models that map one sequence to another of arbitrary length.

## Why it matters in this list

Seq2seq plus attention is the direct lineage from recurrent translation systems to the Transformer.

## Papers

- [01 - Attention Is All You Need](/papers/01-attention-is-all-you-need.md) (2017) - Introduces the Transformer, an architecture built entirely from multi-head self-attention and positional encodings, with no recurrence or convolution.
- [10 - Sequence to Sequence Learning with Neural Networks](/papers/10-sequence-to-sequence-learning.md) (2014) - Encoder-decoder LSTMs for machine translation: one network reads a sentence into a fixed vector, another writes the translation.
- [12 - Pointer Networks](/papers/12-pointer-networks.md) (2015) - Outputs are pointers into the input sequence rather than indices into a fixed vocabulary, so the model can solve variable-size combinatorial problems such as sorting, convex hull and the travelling salesman..
- [13 - Order Matters: Sequence to Sequence for Sets](/papers/13-order-matters-sequence-to-sequence-for-sets.md) (2015) - Reads an unordered set in one order and decodes in another, showing how input ordering and attention interact - and when a set-to-sequence model can learn an order-invariant solution..
- [14 - Neural Machine Translation by Jointly Learning to Align and Translate](/papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md) (2014) - Introduces attention: instead of squeezing the source sentence into one vector, the decoder learns where to look at each step.

## Related topics

[Attention](/topics/attention.md), [Recurrent Neural Networks](/topics/recurrent-neural-networks.md), [Long Short-Term Memory](/topics/long-short-term-memory.md)