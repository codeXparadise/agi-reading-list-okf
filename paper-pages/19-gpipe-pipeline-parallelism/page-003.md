---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/19-gpipe-pipeline-parallelism.md
source: ../../papers/19-gpipe-pipeline-parallelism.md
paper_title: "GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism"
sequence: 19
page: 3
pages: [3]
page_of: 11
topics: ["../../topics/pipeline-parallelism.md", "../../topics/scaling-laws.md"]
description: "Table 1: Maximum model size of AmoebaNet supported by GPipe under different scenarios. Naive-1 refers to the sequential version without GPipe.…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 3 of 11 - GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism

> Page 3 of the source PDF, verbatim as extracted. Canonical document: [19 - GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism](../../papers/19-gpipe-pipeline-parallelism.md)

Table 1: Maximum model size of AmoebaNet supported by GPipe under different scenarios. Naive-1 refers to the sequential version without GPipe. Pipeline-k means k partitions with GPipe on k accelerators. AmoebaNet-D (L, D): AmoebaNet model with L normal cell layers and filter size D . Transformer-L: Transformer model with L layers, 2048 model and 8192 hidden dimensions. Each model parameter needs 12 bytes since we applied RMSProp during training.

NVIDIA GPUs (8GB each) Naive-1 Pipeline-1 Pipeline-2 Pipeline-4 Pipeline-8

AmoebaNet-D (L, D) (18, 208) (18, 416) (18, 544) (36, 544) (72, 512) # of Model Parameters 82M 318M 542M 1.05B 1.8B Total Model Parameter Memory 1.05GB 3.8GB 6.45GB 12.53GB 24.62GB Peak Activation Memory 6.26GB 3.46GB 8.11GB 15.21GB 26.24GB

Cloud TPUv3 (16GB each) Naive-1 Pipeline-1 Pipeline-8 Pipeline-32 Pipeline-128

Transformer-L 3 13 103 415 1663 # of Model Parameters 282.2M 785.8M 5.3B 21.0B 83.9B Total Model Parameter Memory 11.7G 8.8G 59.5G 235.1G 937.9G Peak Activation Memory 3.15G 6.4G 50.9G 199.9G 796.1G

## 2.3 Performance Optimization

In order to reduce activation memory requirements, GPipe supports re-materialization \[14\]. During forward computation, each accelerator only stores output activations at the partition boundaries. During the backward pass, the k-th accelerator recomputes the composite forward function Fk. As a consequence, peak activation memory requirement is reduced to O(N + L

K × N

M ), where N

M is the micro-batch size and L

K is the number of layers per partition. In comparison, memory requirement without re-materialization and partitioning would be O(N × L), since computing the gradients bi requires both the upper layer gradients bi+1 and the cached activations fi(x).

As illustrated in Figure 2c, partitioning introduces some idle time per accelerator, which we refer to as the bubble overhead. This bubble time is O( K−1 M+K−1) amortized over the number of micro-steps M. In our experiments, we found the bubble overhead to be negligible when M ≥4 × K. This is also partly because re-computation during the backward pass can be scheduled earlier, without waiting for the gradients from earlier layers.

GPipe also introduces low communication overhead, given that we only need to pass activation tensors at the partition boundaries between accelerators. Therefore, we can achieve efficient scaling performance even on accelerators without high-speed interconnects.

Figure 2c assumes partitions are evenly balanced. However, memory requirements and computation flops at different layers are often quite imbalanced. In such scenarios, imperfect partitioning algorithms might lead to load imbalance. Better partitioning algorithms can potentially improve the performance over our heuristic approach.

## 3 Performance Analyses

We evaluate GPipe performance with two very different types of model architectures: an AmoebaNet \[12\] convolutional model and a Transformer \[15\] sequence-to-sequence model. We ran experiments to study their scalability, efficiency and communication cost.

We expect both re-materialization and pipeline parallelism to benefit memory utilization and thus make fitting giant models feasible. We report the biggest model size GPipe can support under reasonably large input size in Table 1. For AmoebaNet, we ran the experiments on Cloud TPUv2s with 8GB memory per accelerator. We used a fixed input image size of 224 × 224 and mini-batch size of 128. Without GPipe, a single accelerator can train up to an 82M-parameter AmoebaNet, constrained by device memory limits. Owing to re-materialization in back-propagation and batch splitting, GPipe reduces the intermediate activation memory requirements from 6.26GB to 3.46GB, enabling a 318M-parameter model on a single accelerator. With model parallelism, we were able to scale AmoebaNet to 1.8 billion parameters on 8 accelerators, 25x more than what is possible without

---

[previous page](page-002.md) · [next page](page-004.md) · [all pages](index.md)
