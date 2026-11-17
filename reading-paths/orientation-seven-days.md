---
type: Reading Path
title: Orientation in Seven Days
description: "A one-week pass over the list for someone who wants the shape of modern AI quickly: what the Transformer is, what came before it, and what the theory underneath says."
tags: [reading-path, curriculum]
papers: ["/papers/01-attention-is-all-you-need.md", "/papers/02-the-annotated-transformer.md", "/papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md", "/papers/10-sequence-to-sequence-learning.md", "/papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md", "/papers/09-understanding-lstm-networks.md", "/papers/11-recurrent-neural-network-regularization.md", "/papers/04-imagenet-classification-alexnet.md", "/papers/05-deep-residual-learning-resnet.md", "/papers/06-identity-mappings-in-deep-residual-networks.md", "/papers/20-adam-stochastic-optimization.md", "/papers/21-dropout-regularization.md", "/papers/03-scaling-laws-for-neural-language-models.md", "/papers/16-neural-turing-machines.md", "/papers/17-simple-neural-network-module-for-relational-reasoning.md", "/papers/18-relational-recurrent-neural-networks.md", "/papers/22-first-law-of-complexodynamics.md", "/papers/24-tutorial-minimum-description-length.md", "/papers/26-kolmogorov-complexity-and-algorithmic-randomness.md"]
status: stable
generated: { by: okf_builder/1.0, at: 2026-11-17T16:30:00Z }
verified: { by: process:okf-validator, at: 2026-11-17T16:30:00Z }
---

# Orientation in Seven Days

A one-week pass over the list for someone who wants the shape of modern AI quickly: what the Transformer is, what came before it, and what the theory underneath says.

Read one sitting per day, in order. Each day is short enough to finish, and the order keeps every paper's prerequisites already read.

## Day 1 - Where it starts

- [01 - Attention Is All You Need](/papers/01-attention-is-all-you-need.md) (2017, NeurIPS 2017)
- [02 - The Annotated Transformer](/papers/02-the-annotated-transformer.md) (2018, Harvard NLP (web article))

The Transformer, then the annotated implementation. Do not skip paper 2: it is what turns the architecture from notation into code.

## Day 2 - How it was found

- [14 - Neural Machine Translation by Jointly Learning to Align and Translate](/papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md) (2014, arXiv / ICLR 2015)
- [10 - Sequence to Sequence Learning with Neural Networks](/papers/10-sequence-to-sequence-learning.md) (2014, NeurIPS 2014)

Attention before the Transformer, and the encoder-decoder template it was bolted onto.

## Day 3 - Sequences the old way

- [08 - The Unreasonable Effectiveness of Recurrent Neural Networks](/papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md) (2015, Personal blog (karpathy.github.io))
- [09 - Understanding LSTM Networks](/papers/09-understanding-lstm-networks.md) (2015, Personal blog (colah.github.io))
- [11 - Recurrent Neural Network Regularization](/papers/11-recurrent-neural-network-regularization.md) (2014, arXiv / ICLR 2015)

Why recurrence was the default, and the gating and regularisation tricks that made it work.

## Day 4 - Vision, and the ideas that leaked out

- [04 - ImageNet Classification with Deep Convolutional Neural Networks](/papers/04-imagenet-classification-alexnet.md) (2012, NeurIPS 2012 (AlexNet))
- [05 - Deep Residual Learning for Image Recognition](/papers/05-deep-residual-learning-resnet.md) (2015, arXiv / CVPR 2016 (ResNet))
- [06 - Identity Mappings in Deep Residual Networks](/papers/06-identity-mappings-in-deep-residual-networks.md) (2016, arXiv / ECCV 2016)

AlexNet, ResNet and pre-activation: where ReLU, dropout and residual streams came from.

## Day 5 - Training at scale

- [20 - Adam: A Method for Stochastic Optimization](/papers/20-adam-stochastic-optimization.md) (2014, arXiv / ICLR 2015)
- [21 - Dropout: A Simple Way to Prevent Neural Networks from Overfitting](/papers/21-dropout-regularization.md) (2014, JMLR 15 (2014))
- [03 - Scaling Laws for Neural Language Models](/papers/03-scaling-laws-for-neural-language-models.md) (2020, arXiv preprint)

Adam, dropout, and the scaling laws that justify the compute.

## Day 6 - Memory and reasoning

- [16 - Neural Turing Machines](/papers/16-neural-turing-machines.md) (2014, arXiv)
- [17 - A Simple Neural Network Module for Relational Reasoning](/papers/17-simple-neural-network-module-for-relational-reasoning.md) (2017, NeurIPS 2017)
- [18 - Relational Recurrent Neural Networks](/papers/18-relational-recurrent-neural-networks.md) (2018, NeurIPS 2018)

Giving a network somewhere to write, and something to reason over.

## Day 7 - The theory underneath

- [22 - The First Law of Complexodynamics](/papers/22-first-law-of-complexodynamics.md) (2011, Shtetl-Optimized (blog essay))
- [24 - A Tutorial Introduction to the Minimum Description Length Principle](/papers/24-tutorial-minimum-description-length.md) (2004, arXiv math/0406077)
- [26 - Kolmogorov Complexity and Algorithmic Randomness](/papers/26-kolmogorov-complexity-and-algorithmic-randomness.md) (2017, AMS Mathematical Surveys and Monographs 220)

Complexity, compression and why a shorter description generalises better. Read these slowly.

## Back to

- [All reading paths](/reading-paths/index.md)
- [Bundle index](/)