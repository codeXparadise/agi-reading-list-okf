---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/25-coffee-automaton.md
source: ../../papers/25-coffee-automaton.md
paper_title: "Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton"
sequence: 25
section: 7 Conclusions and Further Work
section_role: conclusion
section_index: 18
pages: [19]
topics: ["../../topics/kolmogorov-complexity.md"]
description: "Of the metrics considered in this project, the coarse-graining approaches such as apparent complexity provide the most eﬀective estimate of…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 7 Conclusions and Further Work

> Section 18 of 21 from [25 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton](../../papers/25-coffee-automaton.md) · `conclusion` · pages 19-19

Of the metrics considered in this project, the coarse-graining approaches such as apparent complexity provide the most eﬀective estimate of complexity that produces results which mirror human intuition. However, this metric suﬀers from the disadvantage that it is based on human intuition and perceptions of complexity. Ideally, a complexity metric would be found which produces similar results without relying on such assumptions. The OSCR approach seems promising for its independence from these assumptions and for its theoretical foundations. It is possible that a diﬀerent implementation of this algorithm could produce better results than the one we used for this project.

It would also be worthwhile to investigate other complexity metrics, beyond those already explored in this paper. Shalizi et al. \[12\] propose a metric based on the concept of light cones. They define C (x), the complexity of a point x in the spacetime history, as the mutual information between descriptions of its past and future light cones. Letting P (x) be the past light cone and F (x) the future light cone, C (x) = H (P (x)) + H (F (x)) −H (P (x) , F (x)). This metric is of particular interest because it avoids the problem of artifacts created by coarse-graining; it can also be approximated in a way that avoids the use of gzip. Running experiments with the automaton using the light cone metric, and comparing the results to those generated using coarse-graining, could provide more information about both metrics.

Ultimately, numerical simulation is of limited use in reasoning about the problem of complexity. Approximation algorithms can provide only an upper bound, not a lower bound, on Kolmogorov complexity and sophistication. To show that a system really does become complex at intermediate points in time, it is necessary to find a lower bound for the system’s complexity. Future theoretical work could help provide such a lower bound, and could also generate further insight into the origins of complexity in closed systems.

---

Full document: [25 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton](../../papers/25-coffee-automaton.md) · Page-level evidence: [paper-pages/25-coffee-automaton](../../paper-pages/25-coffee-automaton/index.md)
