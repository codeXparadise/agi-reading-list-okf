---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/25-coffee-automaton.md
source: ../../papers/25-coffee-automaton.md
paper_title: "Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton"
sequence: 25
page: 9
pages: [9]
page_of: 22
topics: ["../../topics/kolmogorov-complexity.md"]
description: "3 The Coﬀee Automaton The coﬀee cup system that we use as our model is a simple stochastic cellular automaton. A twodimensional array of bits…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 9 of 22 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton

> Page 9 of the source PDF, verbatim as extracted. Canonical document: [25 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton](../../papers/25-coffee-automaton.md)

## 3 The Coﬀee Automaton

The coﬀee cup system that we use as our model is a simple stochastic cellular automaton. A twodimensional array of bits describes the system’s state, with ones representing particles of cream, and zeros representing particles of coﬀee. The cellular automaton implementation used for this project is written in Python; source code is available for download.4

The automaton begins in a state in which the top half of the cells are filled with ones, and the bottom half is filled with zeros. At each time step, the values in the cells change according to a particular transition rule. We consider two diﬀerent models of the coﬀee cup system, each having its own transition rule.

## 3.1 Interacting Model

In the interacting model of the coﬀee cup system, only one particle may occupy each cell in the state array. The transition rule for this model is as follows: at each time step, one pair of horizontally or vertically adjacent, diﬀering particles is selected, and the particles’ positions are swapped. This model is interacting in the sense that the presence of a particle in a cell prevents another particle from entering that cell. The movements of particles in this model are not independent of one another.

This model reflects the physical principle that two pieces of matter may not occupy the same space at the same time. However, the interactions between particles that make this model more realistic also make it harder to reason about theoretically.

## 3.2 Non-Interacting Model

In the non-interacting model of the coﬀee cup system, any number of cream particles may occupy a single cell in the state array. Coﬀee particles are not considered important in this model; they are simply considered a background through which the cream particles move. The transition rule for this model is as follows: at each time step, each cream particle in the system moves one step in a randomly chosen direction. This model is non-interacting in that the location of each cream particle is independent of all the others. The presence of a cream particle in a particular cell does not prevent another cream particle from also moving into that cell.

We consider this model because it is easier to understand theoretically. Since the particles in the system do not interact, each particle can be considered to be taking an independent random walk. The dynamics of random walks are well-understood, so it is easy to make theoretical predictions about this model (see Appendix 9) and compare them to the experimental results.

## 4 Approximating Apparent Complexity

While Kolmogorov complexity and sophistication are useful theoretical notions to model our ideas of entropy and complexity, they cannot be directly applied in numerical simulations, because they are both uncomputable. As such, while we use these concepts as a theoretical foundation, we need to develop algorithms that attempt to approximate them.

Evans et al. \[5\] propose an algorithm, called the optimal symbol compression ratio (OSCR) algorithm, which directly estimates Kolmogorov complexity and sophistication. Given an input

4At www.scottaaronson.com/coffee automaton.zip

10

---

[previous page](page-008.md) · [next page](page-010.md) · [all pages](index.md)
