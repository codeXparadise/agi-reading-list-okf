---
type: Reading Path
title: Sequence Models to Transformers
description: "A focused track through the sequence-modelling lineage: RNNs and LSTMs, seq2seq, attention, and the Transformer that removed recurrence entirely."
tags: [reading-path, curriculum]
papers: ["/papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md", "/papers/09-understanding-lstm-networks.md", "/papers/11-recurrent-neural-network-regularization.md", "/papers/10-sequence-to-sequence-learning.md", "/papers/12-pointer-networks.md", "/papers/13-order-matters-sequence-to-sequence-for-sets.md", "/papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md", "/papers/15-deep-speech-2.md", "/papers/01-attention-is-all-you-need.md", "/papers/02-the-annotated-transformer.md"]
status: stable
generated: { by: okf_builder/1.0, at: 2026-11-17T16:30:00Z }
verified: { by: process:okf-validator, at: 2026-11-17T16:30:00Z }
---

# Sequence Models to Transformers

A focused track through the sequence-modelling lineage: RNNs and LSTMs, seq2seq, attention, and the Transformer that removed recurrence entirely.

Follow the arrows. Every paper in this track either fixes a specific failure of the previous one or explains why the fix was unnecessary.

## The recurrence era

- [08 - The Unreasonable Effectiveness of Recurrent Neural Networks](/papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md) (2015, Personal blog (karpathy.github.io))
- [09 - Understanding LSTM Networks](/papers/09-understanding-lstm-networks.md) (2015, Personal blog (colah.github.io))
- [11 - Recurrent Neural Network Regularization](/papers/11-recurrent-neural-network-regularization.md) (2014, arXiv / ICLR 2015)

Start with the essay for intuition, then the LSTM mechanics, then the regularisation that made them practical.

## Encoder-decoder

- [10 - Sequence to Sequence Learning with Neural Networks](/papers/10-sequence-to-sequence-learning.md) (2014, NeurIPS 2014)
- [12 - Pointer Networks](/papers/12-pointer-networks.md) (2015, NeurIPS 2015)
- [13 - Order Matters: Sequence to Sequence for Sets](/papers/13-order-matters-sequence-to-sequence-for-sets.md) (2015, arXiv / ICLR 2016)

Seq2seq fixes variable-length output; pointer networks and set-to-sequence push on what the output can be.

## Attention

- [14 - Neural Machine Translation by Jointly Learning to Align and Translate](/papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md) (2014, arXiv / ICLR 2015)
- [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](/papers/15-deep-speech-2.md) (2015, arXiv / ICML 2016)

The alignment model that became attention, and a scaled production system built on recurrent sequence models.

## The Transformer

- [01 - Attention Is All You Need](/papers/01-attention-is-all-you-need.md) (2017, NeurIPS 2017)
- [02 - The Annotated Transformer](/papers/02-the-annotated-transformer.md) (2018, Harvard NLP (web article))

The paper and its annotated implementation.

## Back to

- [All reading paths](/reading-paths/index.md)
- [Bundle index](/)