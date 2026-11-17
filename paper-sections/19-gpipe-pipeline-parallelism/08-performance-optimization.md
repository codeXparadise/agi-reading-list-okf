---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/19-gpipe-pipeline-parallelism.md
source: ../../papers/19-gpipe-pipeline-parallelism.md
paper_title: "GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism"
sequence: 19
section: 2.3 Performance Optimization
section_role: other
section_index: 8
pages: [3]
topics: ["../../topics/pipeline-parallelism.md", "../../topics/scaling-laws.md"]
description: "In order to reduce activation memory requirements, GPipe supports re-materialization [14]. During forward computation, each accelerator only stores…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.3 Performance Optimization

> Section 8 of 14 from [19 - GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism](../../papers/19-gpipe-pipeline-parallelism.md) · `other` · pages 3-3

In order to reduce activation memory requirements, GPipe supports re-materialization \[14\]. During forward computation, each accelerator only stores output activations at the partition boundaries. During the backward pass, the k-th accelerator recomputes the composite forward function Fk. As a consequence, peak activation memory requirement is reduced to O(N + L

K × N

M ), where N

M is the micro-batch size and L

K is the number of layers per partition. In comparison, memory requirement without re-materialization and partitioning would be O(N × L), since computing the gradients bi requires both the upper layer gradients bi+1 and the cached activations fi(x).

As illustrated in Figure 2c, partitioning introduces some idle time per accelerator, which we refer to as the bubble overhead. This bubble time is O( K−1 M+K−1) amortized over the number of micro-steps M. In our experiments, we found the bubble overhead to be negligible when M ≥4 × K. This is also partly because re-computation during the backward pass can be scheduled earlier, without waiting for the gradients from earlier layers.

GPipe also introduces low communication overhead, given that we only need to pass activation tensors at the partition boundaries between accelerators. Therefore, we can achieve efficient scaling performance even on accelerators without high-speed interconnects.

Figure 2c assumes partitions are evenly balanced. However, memory requirements and computation flops at different layers are often quite imbalanced. In such scenarios, imperfect partitioning algorithms might lead to load imbalance. Better partitioning algorithms can potentially improve the performance over our heuristic approach.

---

Full document: [19 - GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism](../../papers/19-gpipe-pipeline-parallelism.md) · Page-level evidence: [paper-pages/19-gpipe-pipeline-parallelism](../../paper-pages/19-gpipe-pipeline-parallelism/index.md)
