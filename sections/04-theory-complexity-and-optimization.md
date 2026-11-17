---
type: Section
title: "Theory, Complexity & Optimization"
description: "How models are trained and why they generalise: optimisers, regularisation, scaling systems, minimum description length, Kolmogorov complexity and the theory of intelligence."
tags: [section, curriculum]
papers: ["/papers/19-gpipe-pipeline-parallelism.md", "/papers/20-adam-stochastic-optimization.md", "/papers/21-dropout-regularization.md", "/papers/22-first-law-of-complexodynamics.md", "/papers/23-keeping-neural-networks-simple.md", "/papers/24-tutorial-minimum-description-length.md", "/papers/25-coffee-automaton.md", "/papers/26-kolmogorov-complexity-and-algorithmic-randomness.md", "/papers/27-machine-super-intelligence.md"]
status: stable
generated: { by: okf_builder/1.0, at: 2026-11-17T16:30:00Z }
verified: { by: process:okf-validator, at: 2026-11-17T16:30:00Z }
---

# Theory, Complexity & Optimization

How models are trained and why they generalise: optimisers, regularisation, scaling systems, minimum description length, Kolmogorov complexity and the theory of intelligence.

## Papers

1. [19 - GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism](/papers/19-gpipe-pipeline-parallelism.md) - Yanping Huang, Youlong Cheng et al. (2018). Pipeline parallelism plus micro-batching, so a model too large for one accelerator can still be trained efficiently.
2. [20 - Adam: A Method for Stochastic Optimization](/papers/20-adam-stochastic-optimization.md) - Diederik P. Kingma, Jimmy Ba (2014). Adaptive moment estimation: per-parameter learning rates derived from running estimates of the first and second gradient moments, plus bias correction.
3. [21 - Dropout: A Simple Way to Prevent Neural Networks from Overfitting](/papers/21-dropout-regularization.md) - Nitish Srivastava, Geoffrey Hinton et al. (2014). Randomly dropping units during training, read as training an ensemble of thinned networks.
4. [22 - The First Law of Complexodynamics](/papers/22-first-law-of-complexodynamics.md) - Scott Aaronson (2011). An essay asking for a law that explains why the 'complexity' of a closed system rises, peaks and falls while entropy only rises - and proposing resource-bounded Kolmogorov complexity as the measure that would make such a law precise..
5. [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](/papers/23-keeping-neural-networks-simple.md) - Geoffrey E. Hinton, Drew van Camp (1993). Treats each weight as a distribution and penalises the number of bits needed to describe it, linking generalisation to compression.
6. [24 - A Tutorial Introduction to the Minimum Description Length Principle](/papers/24-tutorial-minimum-description-length.md) - Peter D. Grunwald (2004). A readable tutorial on MDL: learning as finding the model that compresses the data shortest, with the theory of why that controls overfitting.
7. [25 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton](/papers/25-coffee-automaton.md) - Scott Aaronson, Sean M. Carroll et al. (2014). Turns the coffee-and-milk thought experiment into a simulation, separating entropy from 'apparent complexity' and measuring how the latter rises and then falls as the two liquids mix..
8. [26 - Kolmogorov Complexity and Algorithmic Randomness](/papers/26-kolmogorov-complexity-and-algorithmic-randomness.md) - Alexander Shen, Vladimir A. Uspensky et al. (2017). The standard graduate text on Kolmogorov complexity, randomness deficiency and the two-part-code view of a good model.
9. [27 - Machine Super Intelligence](/papers/27-machine-super-intelligence.md) - Shane Legg (2008). Defines universal intelligence formally as expected performance across all computable environments, weighted by simplicity, and follows the consequences for agents, compression and safety.

## How to read this section

Read in the numbered order. Each paper links to what it builds on and what it enables, so you can follow the dependency arrows out of the section when a prerequisite sits elsewhere in the list.

## Related

- [All papers](/papers/index.md)
- [Bundle index](/)