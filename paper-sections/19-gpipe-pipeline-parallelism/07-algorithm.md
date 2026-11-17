---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/19-gpipe-pipeline-parallelism.md
source: ../../papers/19-gpipe-pipeline-parallelism.md
paper_title: "GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism"
sequence: 19
section: 2.2 Algorithm
section_role: method
section_index: 7
pages: [2, 3]
topics: ["../../topics/pipeline-parallelism.md", "../../topics/scaling-laws.md"]
description: "Once the user defines the sequence of layers in their network in terms of model parameters wi, forward computation function fi, and the cost…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.2 Algorithm

> Section 7 of 14 from [19 - GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism](../../papers/19-gpipe-pipeline-parallelism.md) · `method` · pages 2-3

Once the user defines the sequence of layers in their network in terms of model parameters wi, forward computation function fi, and the cost estimation function ci, GPipe partitions the network into K cells and places the k-th cell on the k-th accelerator. Communication primitives are automatically inserted at partition boundaries to allow data transfer between neighboring partitions. The partitioning algorithm minimizes the variance in the estimated costs of all cells in order to maximize the efficiency of the pipeline by syncing the computation time across all partitions.

During the forward pass, GPipe first divides every mini-batch of size N into M equal micro-batches, which are pipelined through the K accelerators. During the backward pass, gradients for each micro-batch are computed based on the same model parameters used for the forward pass. At the end of each mini-batch, gradients from all M micro-batches are accumulated and applied to update the model parameters across all accelerators. This sequence of operations is illustrated in Figure 2c.

If batch normalization \[20\] is used in the network, the sufficient statistics of inputs during training are computed over each micro-batch and over replicas if necessary \[21\]. We also track the moving average of the sufficient statistics over the entire mini-batch to be used during evaluation.

Table 1: Maximum model size of AmoebaNet supported by GPipe under different scenarios. Naive-1 refers to the sequential version without GPipe. Pipeline-k means k partitions with GPipe on k accelerators. AmoebaNet-D (L, D): AmoebaNet model with L normal cell layers and filter size D . Transformer-L: Transformer model with L layers, 2048 model and 8192 hidden dimensions. Each model parameter needs 12 bytes since we applied RMSProp during training.

NVIDIA GPUs (8GB each) Naive-1 Pipeline-1 Pipeline-2 Pipeline-4 Pipeline-8

AmoebaNet-D (L, D) (18, 208) (18, 416) (18, 544) (36, 544) (72, 512) # of Model Parameters 82M 318M 542M 1.05B 1.8B Total Model Parameter Memory 1.05GB 3.8GB 6.45GB 12.53GB 24.62GB Peak Activation Memory 6.26GB 3.46GB 8.11GB 15.21GB 26.24GB

Cloud TPUv3 (16GB each) Naive-1 Pipeline-1 Pipeline-8 Pipeline-32 Pipeline-128

Transformer-L 3 13 103 415 1663 # of Model Parameters 282.2M 785.8M 5.3B 21.0B 83.9B Total Model Parameter Memory 11.7G 8.8G 59.5G 235.1G 937.9G Peak Activation Memory 3.15G 6.4G 50.9G 199.9G 796.1G

---

Full document: [19 - GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism](../../papers/19-gpipe-pipeline-parallelism.md) · Page-level evidence: [paper-pages/19-gpipe-pipeline-parallelism](../../paper-pages/19-gpipe-pipeline-parallelism/index.md)
