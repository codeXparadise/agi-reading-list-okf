---
type: Topic
title: Machine Translation
description: "Translating text between languages; historically the benchmark that drove sequence modelling."
tags: [application, language, topic]
papers: ["/papers/01-attention-is-all-you-need.md", "/papers/10-sequence-to-sequence-learning.md", "/papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md"]
status: stable
generated: { by: okf_builder/1.0, at: 2026-11-17T16:30:00Z }
verified: { by: process:okf-validator, at: 2026-11-17T16:30:00Z }
---

# Machine Translation

Translating text between languages; historically the benchmark that drove sequence modelling.

## Why it matters in this list

Translation was the task on which attention, seq2seq and the Transformer were all demonstrated first.

## Papers

- [01 - Attention Is All You Need](/papers/01-attention-is-all-you-need.md) (2017) - Introduces the Transformer, an architecture built entirely from multi-head self-attention and positional encodings, with no recurrence or convolution.
- [10 - Sequence to Sequence Learning with Neural Networks](/papers/10-sequence-to-sequence-learning.md) (2014) - Encoder-decoder LSTMs for machine translation: one network reads a sentence into a fixed vector, another writes the translation.
- [14 - Neural Machine Translation by Jointly Learning to Align and Translate](/papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md) (2014) - Introduces attention: instead of squeezing the source sentence into one vector, the decoder learns where to look at each step.

## Related topics

[Speech Recognition](/topics/speech-recognition.md)