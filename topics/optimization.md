---
type: Topic
title: Optimization
description: The algorithms that decide how weights move in response to gradients.
tags: [topic, training]
papers: ["/papers/03-scaling-laws-for-neural-language-models.md", "/papers/20-adam-stochastic-optimization.md"]
status: stable
generated: { by: okf_builder/1.0, at: 2026-11-17T16:30:00Z }
verified: { by: process:okf-validator, at: 2026-11-17T16:30:00Z }
---

# Optimization

The algorithms that decide how weights move in response to gradients.

## Why it matters in this list

Adam is the default optimiser of the field, and reading the paper explains both why it works and where its assumptions bite.

## Papers

- [03 - Scaling Laws for Neural Language Models](/papers/03-scaling-laws-for-neural-language-models.md) (2020) - Shows that language-model loss falls as a smooth power law in model size, dataset size and compute, across many orders of magnitude.
- [20 - Adam: A Method for Stochastic Optimization](/papers/20-adam-stochastic-optimization.md) (2014) - Adaptive moment estimation: per-parameter learning rates derived from running estimates of the first and second gradient moments, plus bias correction.

## Related topics

[Scaling Laws](/topics/scaling-laws.md), [Regularization](/topics/regularization.md), [Pipeline Parallelism](/topics/pipeline-parallelism.md)