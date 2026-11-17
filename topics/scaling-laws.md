---
type: Topic
title: Scaling Laws
description: "Empirical power-law relationships between loss and model size, data size and compute."
tags: [compute, topic, training]
papers: ["/papers/03-scaling-laws-for-neural-language-models.md", "/papers/19-gpipe-pipeline-parallelism.md"]
status: stable
generated: { by: okf_builder/1.0, at: 2026-11-17T16:30:00Z }
verified: { by: process:okf-validator, at: 2026-11-17T16:30:00Z }
---

# Scaling Laws

Empirical power-law relationships between loss and model size, data size and compute.

## Why it matters in this list

Scaling laws are what make compute budgets a design decision rather than a gamble.

## Papers

- [03 - Scaling Laws for Neural Language Models](/papers/03-scaling-laws-for-neural-language-models.md) (2020) - Shows that language-model loss falls as a smooth power law in model size, dataset size and compute, across many orders of magnitude.
- [19 - GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism](/papers/19-gpipe-pipeline-parallelism.md) (2018) - Pipeline parallelism plus micro-batching, so a model too large for one accelerator can still be trained efficiently.

## Related topics

[Optimization](/topics/optimization.md), [Regularization](/topics/regularization.md), [Pipeline Parallelism](/topics/pipeline-parallelism.md)