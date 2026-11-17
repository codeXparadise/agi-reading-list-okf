---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/12-pointer-networks.md
source: ../../papers/12-pointer-networks.md
paper_title: Pointer Networks
sequence: 12
section: 3.2 Delaunay Triangulation
section_role: other
section_index: 10
pages: [4]
topics: ["../../topics/sequence-to-sequence.md", "../../topics/attention.md"]
description: "A Delaunay triangulation for a set P of points in a plane is a triangulation such that each circumcircle of every triangle is empty, that is, there…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.2 Delaunay Triangulation

> Section 10 of 18 from [12 - Pointer Networks](../../papers/12-pointer-networks.md) · `other` · pages 4-4

A Delaunay triangulation for a set P of points in a plane is a triangulation such that each circumcircle of every triangle is empty, that is, there is no point from P in its interior. Exact O(n log n) solutions are available \[16\], where n is the number of points in P.

In this example, the outputs CP = {C1, . . . , Cm(P)} are the corresponding sequences representing the triangulation of the point set P . Each Ci is a triple of integers from 1 to n corresponding to the position of triangle vertices in P or the beginning/end of sequence tokens. See Figure 2 (b).

We note that any permutation of the sequence CP represents the same triangulation for P, additionally each triangle representation Ci of three integers can also be permuted. Without loss of generality, and similarly to what we did for convex hulls at training time, we order the triangles Ci by their incenter coordinates (lexicographic order) and choose the increasing triangle representation2. Without ordering, the models learned were not as good, and finding a better ordering that the Ptr-Net could better exploit is part of future work.

---

Full document: [12 - Pointer Networks](../../papers/12-pointer-networks.md) · Page-level evidence: [paper-pages/12-pointer-networks](../../paper-pages/12-pointer-networks/index.md)
