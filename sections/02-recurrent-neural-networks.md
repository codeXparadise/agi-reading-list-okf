---
type: Section
title: Recurrent Neural Networks
description: "Sequence modelling before and alongside attention: RNNs, LSTMs, regularisation, pointer networks, attention-based translation and end-to-end speech."
tags: [section, curriculum]
papers: ["/papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md", "/papers/09-understanding-lstm-networks.md", "/papers/10-sequence-to-sequence-learning.md", "/papers/11-recurrent-neural-network-regularization.md", "/papers/12-pointer-networks.md", "/papers/13-order-matters-sequence-to-sequence-for-sets.md", "/papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md", "/papers/15-deep-speech-2.md"]
status: stable
generated: { by: okf_builder/1.0, at: 2026-11-17T16:30:00Z }
verified: { by: process:okf-validator, at: 2026-11-17T16:30:00Z }
---

# Recurrent Neural Networks

Sequence modelling before and alongside attention: RNNs, LSTMs, regularisation, pointer networks, attention-based translation and end-to-end speech.

## Papers

1. [08 - The Unreasonable Effectiveness of Recurrent Neural Networks](/papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md) - Andrej Karpathy (2015). A hands-on essay: train character-level RNNs and watch them produce Shakespeare, LaTeX, C code and Wikipedia markup.
2. [09 - Understanding LSTM Networks](/papers/09-understanding-lstm-networks.md) - Christopher Olah (2015). The clearest visual walkthrough of LSTM gates - forget, input and output - and of why a cell state can carry information across long sequences where a plain RNN cannot..
3. [10 - Sequence to Sequence Learning with Neural Networks](/papers/10-sequence-to-sequence-learning.md) - Ilya Sutskever, Oriol Vinyals et al. (2014). Encoder-decoder LSTMs for machine translation: one network reads a sentence into a fixed vector, another writes the translation.
4. [11 - Recurrent Neural Network Regularization](/papers/11-recurrent-neural-network-regularization.md) - Wojciech Zaremba, Ilya Sutskever et al. (2014). Shows how to apply dropout to LSTMs correctly - on the non-recurrent connections only - which is what made regularised RNNs competitive on language modelling and translation..
5. [12 - Pointer Networks](/papers/12-pointer-networks.md) - Oriol Vinyals, Meir Fortunato et al. (2015). Outputs are pointers into the input sequence rather than indices into a fixed vocabulary, so the model can solve variable-size combinatorial problems such as sorting, convex hull and the travelling salesman..
6. [13 - Order Matters: Sequence to Sequence for Sets](/papers/13-order-matters-sequence-to-sequence-for-sets.md) - Oriol Vinyals, Samy Bengio et al. (2015). Reads an unordered set in one order and decodes in another, showing how input ordering and attention interact - and when a set-to-sequence model can learn an order-invariant solution..
7. [14 - Neural Machine Translation by Jointly Learning to Align and Translate](/papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md) - Dzmitry Bahdanau, Kyunghyun Cho et al. (2014). Introduces attention: instead of squeezing the source sentence into one vector, the decoder learns where to look at each step.
8. [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](/papers/15-deep-speech-2.md) - Dario Amodei, Rishita Anubhai et al. (2015). End-to-end deep learning for speech recognition: recurrent networks plus CTC, scaled into a production system that works in both English and Mandarin.

## How to read this section

Read in the numbered order. Each paper links to what it builds on and what it enables, so you can follow the dependency arrows out of the section when a prerequisite sits elsewhere in the list.

## Related

- [All papers](/papers/index.md)
- [Bundle index](/)