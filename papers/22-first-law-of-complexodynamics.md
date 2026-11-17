---
type: Web Article
title: The First Law of Complexodynamics
description: "An essay asking for a law that explains why the 'complexity' of a closed system rises, peaks and falls while entropy only rises - and proposing resource-bounded Kolmogorov complexity as the measure that would."
resource: https://scottaaronson.blog/?p=762
tags: [agi-reading-list, article, kolmogorov-complexity]
sequence: 22
section: /sections/04-theory-complexity-and-optimization.md
authors: [Scott Aaronson]
year: 2011
venue: Shtetl-Optimized (blog essay)
topics: ["/topics/kolmogorov-complexity.md"]
builds_on: ["/papers/26-kolmogorov-complexity-and-algorithmic-randomness.md"]
enables: ["/papers/25-coffee-automaton.md"]
sources:
  - id: reading-list
    resource: /references/the-30-papers-to-ai-mastery.md
    title: The 30 Papers to AI Mastery (curated by @rachit.speaks)
  - id: original
    resource: https://scottaaronson.blog/?p=762
    title: The First Law of Complexodynamics (Shtetl-Optimized (blog essay))
status: stable
generated: { by: okf_builder/1.0, at: 2026-11-17T16:30:00Z }
verified: { by: process:okf-validator, at: 2026-11-17T16:30:00Z }
extraction:
  full_text: web-extracted
  source_kind: web article
  coverage: excerpt
  tool: built-in page extractor
  characters: 5547
---

# The First Law of Complexodynamics

**Authors:** Scott Aaronson  
**Year:** 2011 · **Venue:** Shtetl-Optimized (blog essay) · **Position in the list:** 22 of 30  
**Read the original:** <https://scottaaronson.blog/?p=762>

## Overview

An essay asking for a law that explains why the 'complexity' of a closed system rises, peaks and falls while entropy only rises - and proposing resource-bounded Kolmogorov complexity as the measure that would make such a law precise.[^reading-list]

## Where it sits

This paper is part of [Theory, Complexity & Optimization](/sections/04-theory-complexity-and-optimization.md), the theory, complexity & optimization section of the list.

It assumes you have read: [26 - Kolmogorov Complexity and Algorithmic Randomness](/papers/26-kolmogorov-complexity-and-algorithmic-randomness.md).

It is a prerequisite for: [25 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton](/papers/25-coffee-automaton.md).

## Full text

The text below was extracted from the published source (web article) on 2026-11-17. An excerpt: the fetched text of the essay up to the point where the extractor's length cap cut it, followed by the essay's closing passage as published. The argument in between is at the link.

## The First Law of Complexodynamics

A few weeks ago, I had the pleasure of attending FQXi's Setting Time Aright conference, part of which took place on a cruise from Bergen, Norway to Copenhagen, Denmark. (Why aren't theoretical computer science conferences ever held on cruises? If nothing else, it certainly cuts down on attendees sneaking away from the conference venue.) This conference brought together physicists, cosmologists, philosophers, biologists, psychologists, and (for some strange reason) one quantum complexity blogger to pontificate about the existence, directionality, and nature of time. If you want to know more about the conference, check out Sean Carroll's Cosmic Variance posts here and here.

Sean also delivered the opening talk of the conference, during which (among other things) he asked a beautiful question: why does "complexity" or "interestingness" of physical systems seem to increase with time and then hit a maximum and decrease, in contrast to the entropy, which of course increases monotonically?

My purpose, in this post, is to sketch a possible answer to Sean's question, drawing on concepts from Kolmogorov complexity. If this answer has been suggested before, I'm sure someone will let me know in the comments section.

First, some background: we all know the Second Law, which says that the entropy of any closed system tends to increase with time until it reaches a maximum value. Here "entropy" is slippery to define—we'll come back to that later—but somehow measures how "random" or "generic" or "disordered" a system is. As Sean points out in his wonderful book From Eternity to Here, the Second Law is almost a tautology: how could a system not tend to evolve to more "generic" configurations? if it didn't, those configurations wouldn't be generic! So the real question is not why the entropy is increasing, but why it was ever low to begin with. In other words, why did the universe's initial state at the big bang contain so much order for the universe's subsequent evolution to destroy? I won't address that celebrated mystery in this post, but will simply take the low entropy of the initial state as given.

The point that interests us is this: even though isolated physical systems get monotonically more entropic, they don't get monotonically more "complicated" or "interesting." Sean didn't define what he meant by "complicated" or "interesting" here—indeed, defining those concepts was part of his challenge—but he illustrated what he had in mind with the example of a coffee cup. Shamelessly ripping off his slides:

Entropy increases monotonically from left to right, but intuitively, the "complexity" seems highest in the middle picture: the one with all the tendrils of milk. And same is true for the whole universe: shortly after the big bang, the universe was basically just a low-entropy soup of high-energy particles. A googol years from now, after the last black holes have sputtered away in bursts of Hawking radiation, the universe will basically be just a high-entropy soup of low-energy particles. But today, in between, the universe contains interesting structures such as galaxies and brains and hot-dog-shaped novelty vehicles. We see the pattern:

In answering Sean's provocative question (whether there's some "law of complexodynamics" that would explain his graph), it seems to me that the challenge is twofold:

1. Come up with a plausible formal definition of "complexity."
2. Prove that the "complexity," so defined, is large at intermediate times in natural model systems, despite being close to zero at the initial time and close to zero at late times.

To clarify: it's not hard to explain, at least at a handwaving level, why the complexity should be close to zero at the initial time. It's because we assumed the entropy is close to zero, and entropy plausibly gives an upper bound on complexity. Nor is it hard to explain why the complexity should be close to zero at late times: it's because the system reaches equilibrium (i.e., something resembling the uniform distribution over all possible states), which we're essentially defining to be simple. At intermediate times, neither of those constraints is operative, and therefore the complexity could become large. But does it become large? How large? How could we predict? And what kind of "complexity" are we talking about, anyway?

After thinking on and off about these questions, I now conjecture that they can be answered using a notion called sophistication from the theory of Kolmogorov complexity. Recall that the Kolmogorov complexity of a string x is the length of the shortest computer program that outputs x (in some Turing-universal programming language—the exact choice can be shown not to matter much). Sophistication is a more … well, sophisticated concept, but we'll get to that later.

As a first step, let's use Kolmogorov complexity to define entropy.

### Closing passage

But as long as we remember to put computational efficiency requirements on both algorithms, I conjecture that the complextropy will satisfy the "First Law of Complexodynamics," exhibiting exactly the behavior that Sean wants: small for the initial state, large for intermediate states, then small again once the mixing has finished. I don't yet know how to prove this conjecture. But crucially, it's not a hopelessly open-ended question that one tosses out just to show how wide-ranging one's thoughts are, but a relatively-bounded question about which actual theorems could be proved and actual papers published.

## Relationships

- **Section:** [Theory, Complexity & Optimization](/sections/04-theory-complexity-and-optimization.md)
- **Previous in the list:** [21 - Dropout: A Simple Way to Prevent Neural Networks from Overfitting](/papers/21-dropout-regularization.md)
- **Next in the list:** [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](/papers/23-keeping-neural-networks-simple.md)
- **Builds on:** [26 - Kolmogorov Complexity and Algorithmic Randomness](/papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)
- **Enables:** [25 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton](/papers/25-coffee-automaton.md)
- **Alongside:** [19](/papers/19-gpipe-pipeline-parallelism.md), [20](/papers/20-adam-stochastic-optimization.md), [21](/papers/21-dropout-regularization.md), [23](/papers/23-keeping-neural-networks-simple.md), [24](/papers/24-tutorial-minimum-description-length.md), [25](/papers/25-coffee-automaton.md) …
- **Topics:** [Kolmogorov Complexity](/topics/kolmogorov-complexity.md)
- **People:** [Scott Aaronson](/people/scott-aaronson.md)
- **Reading paths:** [Orientation in Seven Days](/reading-paths/orientation-seven-days.md), [Theory and Compression](/reading-paths/theory-and-compression.md)

## Source and provenance

- Listed at position 22 of the 30-paper reading list compiled by @rachit.speaks, the list Ilya Sutskever is reported to have given John Carmack.[^reading-list]
- Original: <https://scottaaronson.blog/?p=762>
- Full text not included in this bundle; follow the link above.

[^reading-list]: The 30 Papers to AI Mastery, curated by @rachit.speaks
[^original]: The First Law of Complexodynamics - Shtetl-Optimized (blog essay)
