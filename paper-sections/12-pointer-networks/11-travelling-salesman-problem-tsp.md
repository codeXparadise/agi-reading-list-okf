---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/12-pointer-networks.md
source: ../../papers/12-pointer-networks.md
paper_title: Pointer Networks
sequence: 12
section: 3.3 Travelling Salesman Problem (TSP)
section_role: other
section_index: 11
pages: [4, 5]
topics: ["../../topics/sequence-to-sequence.md", "../../topics/attention.md"]
description: "TSP arises in many areas of theoretical computer science and is an important algorithm used for microchip design or DNA sequencing. In our work we…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.3 Travelling Salesman Problem (TSP)

> Section 11 of 18 from [12 - Pointer Networks](../../papers/12-pointer-networks.md) · `other` · pages 4-5

TSP arises in many areas of theoretical computer science and is an important algorithm used for microchip design or DNA sequencing. In our work we focused on the planar symmetric TSP: given a list of cities, we wish to find the shortest possible route that visits each city exactly once and returns to the starting point. Additionally, we assume the distance between two cities is the same in each opposite direction. This is an NP-hard problem which allows us to test the capabilities and limitations of our model.

The input/output pairs (P, CP) have a similar format as in the Convex Hull problem described in Section 3.1. P will be the cartesian coordinates representing the cities, which are chosen randomly in the \[0, 1\] × \[0, 1\] square. CP = {C1, . . . , Cn} will be a permutation of integers from 1 to n representing the optimal path (or tour). For consistency, in the training dataset, we always start in the first city without loss of generality.

To generate exact data, we implemented the Held-Karp algorithm \[17\] which finds the optimal solution in O(2nn2) (we used it up to n = 20). For larger n, producing exact solutions is extremely costly, therefore we also considered algorithms that produce approximated solutions: A1 \[18\] and A2 \[19\], which are both O(n2), and A3 \[20\] which implements the O(n3) Christofides algorithm. The latter algorithm is guaranteed to find a solution within a factor of 1.5 from the optimal length. Table 2 shows how they performed in our test sets.

2We choose Ci = (1, 2, 4) instead of (2,4,1) or any other permutation.

---

Full document: [12 - Pointer Networks](../../papers/12-pointer-networks.md) · Page-level evidence: [paper-pages/12-pointer-networks](../../paper-pages/12-pointer-networks/index.md)
