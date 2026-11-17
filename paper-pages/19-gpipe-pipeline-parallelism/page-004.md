---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/19-gpipe-pipeline-parallelism.md
source: ../../papers/19-gpipe-pipeline-parallelism.md
paper_title: "GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism"
sequence: 19
page: 4
pages: [4]
page_of: 11
topics: ["../../topics/pipeline-parallelism.md", "../../topics/scaling-laws.md"]
description: "GPipe. In this case, the maximum model size did not scale perfectly linearly due to the imbalanced distribution of model parameters over different…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 4 of 11 - GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism

> Page 4 of the source PDF, verbatim as extracted. Canonical document: [19 - GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism](../../papers/19-gpipe-pipeline-parallelism.md)

GPipe. In this case, the maximum model size did not scale perfectly linearly due to the imbalanced distribution of model parameters over different layers in AmoebaNet.

We next trained Transformer models using Cloud TPUv3s with 16GB memory per accelerator core. We used a fixed vocabulary size of 32k, sequence length 1024 and batch size 32. Each Transformer layer has 2048 for model dimension, 8192 for feed-forward hidden dimension and 32 attention heads. We scaled the model by varying the number of layers. Re-materialization allows training a 2.7× larger model on a single accelerator. With 128 partitions, GPipe allows scaling Transformer up to 83.9B parameters, a 298× increase than what is possible on a single accelerator. Different from AmoebaNet, the maximum model size scales linearly with the number of accelerators for Transformer, since each layer has the same number of parameters and input sizes.

To evaluate efficiency, we report the normalized training throughput of AmoebaNet-D (18, 256) and Transformer-48 using GPipe with different numbers of partitions and different numbers of micro-batches in Table 2. Each partition is assigned to a separate accelerator. We observe that when the number of micro-batches M is at least 4× the number of partitions, the bubble overhead is almost negligible. For Transformer model, there is a 3.5× speedup when it is partitioned across four times more accelerators. Furthermore, training throughput scales almost linearly with the number of devices, thanks to the computation being evenly distributed across Transformer layers. In contrast, the AmoebaNet model achieves sub-linear speedup due to its imbalanced computation distribution. When M is relatively small, the bubble overhead can no longer be negligible. When M is 1, there is effectively no pipeline parallelism. We observe relatively constant throughput regardless of the number of accelerators used, indicating only one device is actively computing at any given time.

Table 2: Normalized training throughput using GPipe with different # of partitions K and different # of micro-batches M on TPUs. Performance increases with more micro-batches. There is an almost linear speedup with the number of accelerators for Transformer model when M ≫K. Batch size was adjusted to fit memory if necessary.

TPU AmoebaNet Transformer

K = 2 4 8 2 4 8 M = 1 1 1.13 1.38 1 1.07 1.3 M = 4 1.07 1.26 1.72 1.7 3.2 4.8 M = 32 1.21 1.84 3.48 1.8 3.4 6.3

To measure the effect of communication overhead with GPipe, we ran our experiments on a single host with multiple NVIDIA P100 GPUs but without NVLinks. Data transfer across GPUs then has to involve the relatively slow device-to-host and host-to-device transfers through PCI-E. The number of micro-batches was fixed at 32. As shown in Table 3, we observe 2.7× speedup for AmoebaNet-D (18, 128) when we increase the number of partitions from 2 to 8. For the 24-layer Transformer,

the speedup is 3.3×. There is similar linear speedup to what we observe on TPUs where high-speed interconnects are equipped. The communication bandwidth between devices is no longer a bottleneck for model parallelism since GPipe only transfers activation tensors at the boundaries of partitions.

Table 3: Normalized training throughput using GPipe on GPUs without high-speed interconnect.

GPU AmoebaNet Transformer

K = 2 4 8 2 4 8 M = 32 1 1.7 2.7 1 1.8 3.3

## 4 Image Classification

As a proof of concept, we first used GPipe to scale AmoebaNet. We increased the number of channels in an AmoebaNet and scaled the input image size to 480 × 480. We trained this 557-millionparameter AmoebaNet-B(18, 512) on the ImageNet 2012 dataset, using the same hyper-parameters as described in \[12\]. The network was divided into 4 partitions. This single model achieves 84.4% top-1 and 97% top-5 validation accuracy with single-crop.

We further demonstrate the effectiveness of giant convolution networks on other image datasets through transfer learning \[22, 23\]. Specifically, we used the pre-trained ImageNet model to fine-tune on a variety of target datasets ranging from general to fine-grained classification. We changed the number of output units in the last softmax classification layer to the number of classes in the target dataset and initialized the new softmax layer randomly. All the other layers were initialized from

---

[previous page](page-003.md) · [next page](page-005.md) · [all pages](index.md)
