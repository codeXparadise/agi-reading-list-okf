---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/12-pointer-networks.md
source: ../../papers/12-pointer-networks.md
paper_title: Pointer Networks
sequence: 12
section: 3 Motivation and Datasets Structure
section_role: introduction
section_index: 8
pages: [3]
topics: ["../../topics/sequence-to-sequence.md", "../../topics/attention.md"]
description: "In the following sections, we review each of the three problems we considered, as well as our data generation protocol.1 In the training data, the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3 Motivation and Datasets Structure

> Section 8 of 18 from [12 - Pointer Networks](../../papers/12-pointer-networks.md) · `introduction` · pages 3-3

In the following sections, we review each of the three problems we considered, as well as our data generation protocol.1

In the training data, the inputs are planar point sets P = {P1, . . . , Pn} with n elements each, where Pj = (xj, yj) are the cartesian coordinates of the points over which we find the convex hull, the Delaunay triangulation or the solution to the corresponding Travelling Salesman Problem. In all cases, we sample from a uniform distribution in \[0, 1\] × \[0, 1\]. The outputs CP = {C1, . . . , Cm(P)} are sequences representing the solution associated to the point set P. In Figure 2, we find an illustration of an input/output pair (P, CP) for the convex hull and the Delaunay problems.

---

Full document: [12 - Pointer Networks](../../papers/12-pointer-networks.md) · Page-level evidence: [paper-pages/12-pointer-networks](../../paper-pages/12-pointer-networks/index.md)
