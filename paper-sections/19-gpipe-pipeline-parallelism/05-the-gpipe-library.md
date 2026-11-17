---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/19-gpipe-pipeline-parallelism.md
source: ../../papers/19-gpipe-pipeline-parallelism.md
paper_title: "GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism"
sequence: 19
section: 2 The GPipe Library
section_role: method
section_index: 5
pages: [1, 2]
topics: ["../../topics/pipeline-parallelism.md", "../../topics/scaling-laws.md"]
description: "We now describe the interface and the main design features of GPipe. This open-source library is implemented under the Lingvo [16] framework. The…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2 The GPipe Library

> Section 5 of 14 from [19 - GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism](../../papers/19-gpipe-pipeline-parallelism.md) · `method` · pages 1-2

We now describe the interface and the main design features of GPipe. This open-source library is implemented under the Lingvo \[16\] framework. The core design features of GPipe are generally applicable and can be implemented for other frameworks \[17, 18, 19\].

Figure 2: (a) An example neural network with sequential layers is partitioned across four accelerators. Fk is the composite forward computation function of the k-th cell. Bk is the back-propagation function, which depends on both Bk+1 from the upper layer and Fk. (b) The naive model parallelism strategy leads to severe under-utilization due to the sequential dependency of the network. (c) Pipeline parallelism divides the input mini-batch into smaller micro-batches, enabling different accelerators to work on different micro-batches simultaneously. Gradients are applied synchronously at the end.

![Figure, page 3](../../assets/19/fig-19-p03-3.png)

![Figure, page 3](../../assets/19/fig-19-p03-4.png)

(b)

![Figure, page 3](../../assets/19/fig-19-p03-5.png)

(a)

(c)

---

Full document: [19 - GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism](../../papers/19-gpipe-pipeline-parallelism.md) · Page-level evidence: [paper-pages/19-gpipe-pipeline-parallelism](../../paper-pages/19-gpipe-pipeline-parallelism/index.md)
