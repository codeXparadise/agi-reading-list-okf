---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/12-pointer-networks.md
source: ../../papers/12-pointer-networks.md
paper_title: Pointer Networks
sequence: 12
section: 4.4 Travelling Salesman Problem
section_role: other
section_index: 15
pages: [6, 7]
topics: ["../../topics/sequence-to-sequence.md", "../../topics/attention.md"]
description: "We considered the planar symmetric travelling salesman problem (TSP), which is NP-hard as the third problem. Similarly to finding convex hulls, it…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 4.4 Travelling Salesman Problem

> Section 15 of 18 from [12 - Pointer Networks](../../papers/12-pointer-networks.md) · `other` · pages 6-7

We considered the planar symmetric travelling salesman problem (TSP), which is NP-hard as the third problem. Similarly to finding convex hulls, it also has sequential outputs. Given that the PtrNet implements an O(n2) algorithm, it was unclear if it would have enough capacity to learn a useful algorithm solely from data.

As discussed in Section 3.3, it is feasible to generate exact solutions for relatively small values of n to be used as training data. For larger n, due to the importance of TSP, good and efficient algorithms providing reasonable approximate solutions exist. We used three different algorithms in our experiments – A1, A2, and A3 (see Section 3.3 for references).

Table 2 shows all of our results on TSP. The number reported is the length of the proposed tour. Unlike the convex hull and Delaunay triangulation cases, where the decoder was unconstrained, in

Table 2: Tour length of the Ptr-Net and a collection of algorithms on a small scale TSP problem.

n OPTIMAL A1 A2 A3 PTR-NET

5 2.12 2.18 2.12 2.12 2.12 10 2.87 3.07 2.87 2.87 2.88 50 (A1 TRAINED) N/A 6.46 5.84 5.79 6.42 50 (A3 TRAINED) N/A 6.46 5.84 5.79 6.09 5 (5-20 TRAINED) 2.12 2.18 2.12 2.12 2.12 10 (5-20 TRAINED) 2.87 3.07 2.87 2.87 2.87 20 (5-20 TRAINED) 3.83 4.24 3.86 3.85 3.88 25 (5-20 TRAINED) N/A 4.71 4.27 4.24 4.30 30 (5-20 TRAINED) N/A 5.11 4.63 4.60 4.72 40 (5-20 TRAINED) N/A 5.82 5.27 5.23 5.91 50 (5-20 TRAINED) N/A 6.46 5.84 5.79 7.66

this example we set the beam search procedure to only consider valid tours. Otherwise, the Ptr-Net model would sometimes output an invalid tour – for instance, it would repeat two cities or decided to ignore a destination. This procedure was relevant for n > 20, where at least 10% of instances would not produce any valid tour.

The first group of rows in the table show the Ptr-Net trained on optimal data, except for n = 50, since that is not feasible computationally (we trained a separate model for each n). Interestingly, when using the worst algorithm (A1) data to train the Ptr-Net, our model outperforms the algorithm that is trying to imitate.

The second group of rows in the table show how the Ptr-Net trained on optimal data with 5 to 20 cities can generalize beyond that. The results are virtually perfect for n = 25, and good for n = 30, but it seems to break for 40 and beyond (still, the results are far better than chance). This contrasts with the convex hull case, where we were able to generalize by a factor of 10. However, the underlying algorithms are of far greater complexity than O(n log n), which could explain this phenomenon.

---

Full document: [12 - Pointer Networks](../../papers/12-pointer-networks.md) · Page-level evidence: [paper-pages/12-pointer-networks](../../paper-pages/12-pointer-networks/index.md)
