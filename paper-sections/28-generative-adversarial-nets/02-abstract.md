---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/28-generative-adversarial-nets.md
source: ../../papers/28-generative-adversarial-nets.md
paper_title: Generative Adversarial Nets
sequence: 28
section: Abstract
section_role: abstract
section_index: 2
pages: [1]
topics: ["../../topics/generative-models.md"]
description: "We propose a new framework for estimating generative models via an adversarial process, in which we simultaneously train two models: a generative…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Abstract

> Section 2 of 12 from [28 - Generative Adversarial Nets](../../papers/28-generative-adversarial-nets.md) · `abstract` · pages 1-1

We propose a new framework for estimating generative models via an adversarial process, in which we simultaneously train two models: a generative model G that captures the data distribution, and a discriminative model D that estimates the probability that a sample came from the training data rather than G. The training procedure for G is to maximize the probability of D making a mistake. This framework corresponds to a minimax two-player game. In the space of arbitrary functions G and D, a unique solution exists, with G recovering the training data distribution and D equal to 1

2 everywhere. In the case where G and D are defined by multilayer perceptrons, the entire system can be trained with backpropagation. There is no need for any Markov chains or unrolled approximate inference networks during either training or generation of samples. Experiments demonstrate the potential of the framework through qualitative and quantitative evaluation of the generated samples.

---

Full document: [28 - Generative Adversarial Nets](../../papers/28-generative-adversarial-nets.md) · Page-level evidence: [paper-pages/28-generative-adversarial-nets](../../paper-pages/28-generative-adversarial-nets/index.md)
