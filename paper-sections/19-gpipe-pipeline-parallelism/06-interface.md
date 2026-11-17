---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/19-gpipe-pipeline-parallelism.md
source: ../../papers/19-gpipe-pipeline-parallelism.md
paper_title: "GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism"
sequence: 19
section: 2.1 Interface
section_role: other
section_index: 6
pages: [2]
topics: ["../../topics/pipeline-parallelism.md", "../../topics/scaling-laws.md"]
description: "Any deep neural network can be defined as a sequence of L layers. Each layer Li is composed of a forward computation function fi, and a corresponding…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.1 Interface

> Section 6 of 14 from [19 - GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism](../../papers/19-gpipe-pipeline-parallelism.md) · `other` · pages 2-2

Any deep neural network can be defined as a sequence of L layers. Each layer Li is composed of a forward computation function fi, and a corresponding set of parameters wi. GPipe additionally allows the user to specify an optional computation cost estimation function, ci. With a given number of partitions K, the sequence of L layers can be partitioned into K composite layers, or cells. Let pk consist of consecutive layers between layers i and j. The set of parameters corresponding to pk is equivalent to the union of wi, wi+1, . . . , wj, and its forward function would be Fk = fj◦. . .◦fi+1◦fi. The corresponding back-propagation function Bk can be computed from Fk using automatic symbolic differentiation. The cost estimator, Ck, is set to Σj

l=icl.

The GPipe interface is extremely simple and intuitive, requiring the user to specify: (i) the number of model partitions K, (ii) the number of micro-batches M, and (iii) the sequence and definitions of L layers that define the model. Please refer to supplementary material for examples.

---

Full document: [19 - GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism](../../papers/19-gpipe-pipeline-parallelism.md) · Page-level evidence: [paper-pages/19-gpipe-pipeline-parallelism](../../paper-pages/19-gpipe-pipeline-parallelism/index.md)
