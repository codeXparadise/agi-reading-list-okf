---
type: Topic
title: Pipeline Parallelism
description: Splitting a model across devices by layer and streaming micro-batches through the split.
tags: [compute, systems, topic, training]
papers: ["/papers/19-gpipe-pipeline-parallelism.md"]
status: stable
generated: { by: okf_builder/1.0, at: 2026-11-17T16:30:00Z }
verified: { by: process:okf-validator, at: 2026-11-17T16:30:00Z }
---

# Pipeline Parallelism

Splitting a model across devices by layer and streaming micro-batches through the split.

## Why it matters in this list

Training runs that produce frontier models are systems problems as much as modelling problems.

## Papers

- [19 - GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism](/papers/19-gpipe-pipeline-parallelism.md) (2018) - Pipeline parallelism plus micro-batching, so a model too large for one accelerator can still be trained efficiently.

## Related topics

[Scaling Laws](/topics/scaling-laws.md), [Optimization](/topics/optimization.md), [Regularization](/topics/regularization.md)