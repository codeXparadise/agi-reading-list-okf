---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/25-coffee-automaton.md
source: ../../papers/25-coffee-automaton.md
paper_title: "Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton"
sequence: 25
page: 19
pages: [19]
page_of: 22
topics: ["../../topics/kolmogorov-complexity.md"]
description: "7 Conclusions and Further Work Of the metrics considered in this project, the coarse-graining approaches such as apparent complexity provide the most…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 19 of 22 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton

> Page 19 of the source PDF, verbatim as extracted. Canonical document: [25 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton](../../papers/25-coffee-automaton.md)

## 7 Conclusions and Further Work

Of the metrics considered in this project, the coarse-graining approaches such as apparent complexity provide the most eﬀective estimate of complexity that produces results which mirror human intuition. However, this metric suﬀers from the disadvantage that it is based on human intuition and perceptions of complexity. Ideally, a complexity metric would be found which produces similar results without relying on such assumptions. The OSCR approach seems promising for its independence from these assumptions and for its theoretical foundations. It is possible that a diﬀerent implementation of this algorithm could produce better results than the one we used for this project.

It would also be worthwhile to investigate other complexity metrics, beyond those already explored in this paper. Shalizi et al. \[12\] propose a metric based on the concept of light cones. They define C (x), the complexity of a point x in the spacetime history, as the mutual information between descriptions of its past and future light cones. Letting P (x) be the past light cone and F (x) the future light cone, C (x) = H (P (x)) + H (F (x)) −H (P (x) , F (x)). This metric is of particular interest because it avoids the problem of artifacts created by coarse-graining; it can also be approximated in a way that avoids the use of gzip. Running experiments with the automaton using the light cone metric, and comparing the results to those generated using coarse-graining, could provide more information about both metrics.

Ultimately, numerical simulation is of limited use in reasoning about the problem of complexity. Approximation algorithms can provide only an upper bound, not a lower bound, on Kolmogorov complexity and sophistication. To show that a system really does become complex at intermediate points in time, it is necessary to find a lower bound for the system’s complexity. Future theoretical work could help provide such a lower bound, and could also generate further insight into the origins of complexity in closed systems.

## 8 Acknowledgments

We thank Alex Arkhipov, Charles Bennett, Ian Durham, Dietrich Leibfried, Aldo Pacchiano, and Luca Trevisan for helpful discussions.

## 9 Appendix: The Non-Interacting Case

Let’s consider the non-interacting coﬀee automaton on an n × n grid with periodic boundary conditions. At each time step, each cream particle moves to one of the 4 neighboring pixels uniformly at random. Let at (x, y) be the number of cream particles at point (x, y) after t steps.

Claim 1. For all x, y, t, we have E \[at (x, y)\] ≤1.

Proof. By induction on t. If t = 0, then a0 (x, y) ∈{0, 1}. Furthermore, by linearity of expectation,

E \[at+1 (x, y)\] = E \[at (x −1, y)\] + E \[at (x + 1, y)\] + E \[at (x, y −1)\] + E \[at (x, y + 1)\]

4 .

20

---

[previous page](page-018.md) · [next page](page-020.md) · [all pages](index.md)
