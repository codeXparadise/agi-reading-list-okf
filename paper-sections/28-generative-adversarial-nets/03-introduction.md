---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/28-generative-adversarial-nets.md
source: ../../papers/28-generative-adversarial-nets.md
paper_title: Generative Adversarial Nets
sequence: 28
section: 1 Introduction
section_role: introduction
section_index: 3
pages: [1]
topics: ["../../topics/generative-models.md"]
description: "The promise of deep learning is to discover rich, hierarchical models [2] that represent probability distributions over the kinds of data encountered…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 1 Introduction

> Section 3 of 12 from [28 - Generative Adversarial Nets](../../papers/28-generative-adversarial-nets.md) · `introduction` · pages 1-1

The promise of deep learning is to discover rich, hierarchical models \[2\] that represent probability distributions over the kinds of data encountered in artificial intelligence applications, such as natural images, audio waveforms containing speech, and symbols in natural language corpora. So far, the most striking successes in deep learning have involved discriminative models, usually those that map a high-dimensional, rich sensory input to a class label \[14, 22\]. These striking successes have primarily been based on the backpropagation and dropout algorithms, using piecewise linear units \[19, 9, 10\] which have a particularly well-behaved gradient . Deep generative models have had less of an impact, due to the difficulty of approximating many intractable probabilistic computations that arise in maximum likelihood estimation and related strategies, and due to difficulty of leveraging the benefits of piecewise linear units in the generative context. We propose a new generative model estimation procedure that sidesteps these difficulties. 1

In the proposed adversarial nets framework, the generative model is pitted against an adversary: a discriminative model that learns to determine whether a sample is from the model distribution or the data distribution. The generative model can be thought of as analogous to a team of counterfeiters, trying to produce fake currency and use it without detection, while the discriminative model is analogous to the police, trying to detect the counterfeit currency. Competition in this game drives both teams to improve their methods until the counterfeits are indistiguishable from the genuine articles.

∗Jean Pouget-Abadie is visiting Universit´e de Montr´eal from Ecole Polytechnique. †Sherjil Ozair is visiting Universit´e de Montr´eal from Indian Institute of Technology Delhi ‡Yoshua Bengio is a CIFAR Senior Fellow. 1All code and hyperparameters available at http://www.github.com/goodfeli/adversarial

This framework can yield specific training algorithms for many kinds of model and optimization algorithm. In this article, we explore the special case when the generative model generates samples by passing random noise through a multilayer perceptron, and the discriminative model is also a multilayer perceptron. We refer to this special case as adversarial nets. In this case, we can train both models using only the highly successful backpropagation and dropout algorithms \[17\] and sample from the generative model using only forward propagation. No approximate inference or Markov chains are necessary.

---

Full document: [28 - Generative Adversarial Nets](../../papers/28-generative-adversarial-nets.md) · Page-level evidence: [paper-pages/28-generative-adversarial-nets](../../paper-pages/28-generative-adversarial-nets/index.md)
