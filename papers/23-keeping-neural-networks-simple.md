---
type: Research Paper
title: Keeping Neural Networks Simple by Minimizing the Description Length of the Weights
description: "Treats each weight as a distribution and penalises the number of bits needed to describe it, linking generalisation to compression."
resource: https://www.cs.toronto.edu/~hinton/absps/colt93.pdf
tags: [agi-reading-list, minimum-description-length, paper, regularization]
sequence: 23
section: /sections/04-theory-complexity-and-optimization.md
authors: [Geoffrey E. Hinton, Drew van Camp]
year: 1993
venue: COLT 1993
topics: ["/topics/minimum-description-length.md", "/topics/regularization.md"]
builds_on: []
enables: ["/papers/24-tutorial-minimum-description-length.md", "/papers/29-variational-lossy-autoencoder.md"]
sources:
  - id: reading-list
    resource: /references/the-30-papers-to-ai-mastery.md
    title: The 30 Papers to AI Mastery (curated by @rachit.speaks)
  - id: original
    resource: https://www.cs.toronto.edu/~hinton/absps/colt93.pdf
    title: Keeping Neural Networks Simple by Minimizing the Description Length of the Weights (COLT 1993)
status: stable
generated: { by: okf_builder/1.0, at: 2026-11-17T16:30:00Z }
verified: { by: process:okf-validator, at: 2026-11-17T16:30:00Z }
extraction:
  full_text: external-only
---

# Keeping Neural Networks Simple by Minimizing the Description Length of the Weights

**Authors:** Geoffrey E. Hinton, Drew van Camp  
**Year:** 1993 · **Venue:** COLT 1993 · **Position in the list:** 23 of 30  
**Read the original:** <https://www.cs.toronto.edu/~hinton/absps/colt93.pdf>

## Overview

Treats each weight as a distribution and penalises the number of bits needed to describe it, linking generalisation to compression. An early variational treatment of neural networks and an ancestor of the VAE and MDL-style regularisation.[^reading-list]

## Where it sits

This paper is part of [Theory, Complexity & Optimization](/sections/04-theory-complexity-and-optimization.md), the theory, complexity & optimization section of the list.

It is a prerequisite for: [24 - A Tutorial Introduction to the Minimum Description Length Principle](/papers/24-tutorial-minimum-description-length.md), [29 - Variational Lossy Autoencoder](/papers/29-variational-lossy-autoencoder.md).

## Full text

This item is a paper rather than an arXiv paper, and is not distributed as an open PDF that could be archived here. The overview above is the summary; the full text lives at the canonical link.[^original]

- **Read it:** <https://www.cs.toronto.edu/~hinton/absps/colt93.pdf>

## Relationships

- **Section:** [Theory, Complexity & Optimization](/sections/04-theory-complexity-and-optimization.md)
- **Previous in the list:** [22 - The First Law of Complexodynamics](/papers/22-first-law-of-complexodynamics.md)
- **Next in the list:** [24 - A Tutorial Introduction to the Minimum Description Length Principle](/papers/24-tutorial-minimum-description-length.md)
- **Enables:** [24 - A Tutorial Introduction to the Minimum Description Length Principle](/papers/24-tutorial-minimum-description-length.md), [29 - Variational Lossy Autoencoder](/papers/29-variational-lossy-autoencoder.md)
- **Alongside:** [19](/papers/19-gpipe-pipeline-parallelism.md), [20](/papers/20-adam-stochastic-optimization.md), [21](/papers/21-dropout-regularization.md), [22](/papers/22-first-law-of-complexodynamics.md), [24](/papers/24-tutorial-minimum-description-length.md), [25](/papers/25-coffee-automaton.md) …
- **Topics:** [Minimum Description Length](/topics/minimum-description-length.md), [Regularization](/topics/regularization.md)
- **People:** [Geoffrey E. Hinton](/people/geoffrey-hinton.md)
- **Reading paths:** [Theory and Compression](/reading-paths/theory-and-compression.md)

## Source and provenance

- Listed at position 23 of the 30-paper reading list compiled by @rachit.speaks, the list Ilya Sutskever is reported to have given John Carmack.[^reading-list]
- Original: <https://www.cs.toronto.edu/~hinton/absps/colt93.pdf>
- Full text not included in this bundle; follow the link above.

[^reading-list]: The 30 Papers to AI Mastery, curated by @rachit.speaks
[^original]: Keeping Neural Networks Simple by Minimizing the Description Length of the Weights - COLT 1993
