---
type: Topic
title: Recurrent Neural Networks
description: Networks that process a sequence one step at a time while carrying a hidden state.
tags: [sequence-modelling, topic]
papers: ["/papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md", "/papers/09-understanding-lstm-networks.md", "/papers/10-sequence-to-sequence-learning.md", "/papers/11-recurrent-neural-network-regularization.md", "/papers/15-deep-speech-2.md", "/papers/16-neural-turing-machines.md", "/papers/18-relational-recurrent-neural-networks.md"]
status: stable
generated: { by: okf_builder/1.0, at: 2026-11-17T16:30:00Z }
verified: { by: process:okf-validator, at: 2026-11-17T16:30:00Z }
---

# Recurrent Neural Networks

Networks that process a sequence one step at a time while carrying a hidden state.

## Why it matters in this list

Recurrence was the default for sequences before attention, and the failure modes that motivated attention are best understood by reading these papers.

## Papers

- [08 - The Unreasonable Effectiveness of Recurrent Neural Networks](/papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md) (2015) - A hands-on essay: train character-level RNNs and watch them produce Shakespeare, LaTeX, C code and Wikipedia markup.
- [09 - Understanding LSTM Networks](/papers/09-understanding-lstm-networks.md) (2015) - The clearest visual walkthrough of LSTM gates - forget, input and output - and of why a cell state can carry information across long sequences where a plain RNN cannot..
- [10 - Sequence to Sequence Learning with Neural Networks](/papers/10-sequence-to-sequence-learning.md) (2014) - Encoder-decoder LSTMs for machine translation: one network reads a sentence into a fixed vector, another writes the translation.
- [11 - Recurrent Neural Network Regularization](/papers/11-recurrent-neural-network-regularization.md) (2014) - Shows how to apply dropout to LSTMs correctly - on the non-recurrent connections only - which is what made regularised RNNs competitive on language modelling and translation..
- [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](/papers/15-deep-speech-2.md) (2015) - End-to-end deep learning for speech recognition: recurrent networks plus CTC, scaled into a production system that works in both English and Mandarin.
- [16 - Neural Turing Machines](/papers/16-neural-turing-machines.md) (2014) - A neural network coupled to an external memory matrix that it learns to read from and write to with differentiable operations.
- [18 - Relational Recurrent Neural Networks](/papers/18-relational-recurrent-neural-networks.md) (2018) - Puts a relation-network memory inside a recurrent network so that separate facts in memory can interact with each other - relational reasoning carried across time rather than over a single snapshot..

## Related topics

[Attention](/topics/attention.md), [Long Short-Term Memory](/topics/long-short-term-memory.md), [Sequence to Sequence](/topics/sequence-to-sequence.md)