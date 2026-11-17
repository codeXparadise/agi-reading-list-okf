---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/06-identity-mappings-in-deep-residual-networks.md
source: ../../papers/06-identity-mappings-in-deep-residual-networks.md
paper_title: Identity Mappings in Deep Residual Networks
sequence: 6
section: 4.2 Analysis
section_role: results
section_index: 10
pages: [10, 11]
topics: ["../../topics/residual-connections.md", "../../topics/convolutional-networks.md"]
description: "We find the impact of pre-activation is twofold. First, the optimization is further eased (comparing with the baseline ResNet) because f is an…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 4.2 Analysis

> Section 10 of 12 from [06 - Identity Mappings in Deep Residual Networks](../../papers/06-identity-mappings-in-deep-residual-networks.md) · `results` · pages 10-11

We find the impact of pre-activation is twofold. First, the optimization is further eased (comparing with the baseline ResNet) because f is an identity mapping. Second, using BN as pre-activation improves regularization of the models.

Ease of optimization. This eﬀect is particularly obvious when training the 1001-layer ResNet. Fig. 1 shows the curves. Using the original design in \[1\], the training error is reduced very slowly at the beginning of training. For f = ReLU, the signal is impacted if it is negative, and when there are many Residual Units, this eﬀect becomes prominent and Eqn.(3) (so Eqn.(5)) is not a good approximation. On the other hand, when f is an identity mapping, the signal can be propagated directly between any two units. Our 1001-layer network reduces the training loss very quickly (Fig. 1). It also achieves the lowest loss among all models we investigated, suggesting the success of optimization.

We also find that the impact of f = ReLU is not severe when the ResNet has fewer layers (e.g., 164 in Fig. 6(right)). The training curve seems to suﬀer a little bit at the beginning of training, but goes into a healthy status soon. By monitoring the responses we observe that this is because after some training, the weights are adjusted into a status such that yl in Eqn.(1) is more frequently above zero and f does not truncate it (xl is always non-negative due to the previous ReLU, so yl is below zero only when the magnitude of F is very negative). The truncation, however, is more frequent when there are 1000 layers.

Table 4. Comparisons with state-of-the-art methods on CIFAR-10 and CIFAR-100 using “moderate data augmentation” (flip/translation), except for ELU \[12\] with no augmentation. Better results of \[13,14\] have been reported using stronger data augmentation and ensembling. For the ResNets we also report the number of parameters. Our results are the median of 5 runs with mean±std in the brackets. All ResNets results are obtained with a mini-batch size of 128 except † with a mini-batch size of 64 (code available at https://github.com/KaimingHe/resnet-1k-layers).

CIFAR-10 error (%)

CIFAR-100 error (%)

NIN \[15\] 8.81

NIN \[15\] 35.68

DSN \[16\] 8.22

DSN \[16\] 34.57

FitNet \[17\] 8.39

FitNet \[17\] 35.04

Highway \[7\] 7.72

Highway \[7\] 32.39

All-CNN \[14\] 7.25

All-CNN \[14\] 33.71

ELU \[12\] 6.55

ELU \[12\] 24.28

FitResNet, LSUV \[18\] 5.84

FitNet, LSUV \[18\] 27.66

ResNet-110 \[1\] (1.7M) 6.61

ResNet-164 \[1\] (1.7M) 25.16

ResNet-1202 \[1\] (19.4M) 7.93

ResNet-1001 \[1\] (10.2M) 27.82

ResNet-164 \[ours\] (1.7M) 5.46

ResNet-164 \[ours\] (1.7M) 24.33

ResNet-1001 \[ours\] (10.2M) 4.92 (4.89±0.14)

ResNet-1001 \[ours\] (10.2M) 22.71 (22.68±0.22)

ResNet-1001 \[ours\] (10.2M)† 4.62 (4.69±0.20)

Reducing overfitting. Another impact of using the proposed pre-activation unit is on regularization, as shown in Fig. 6 (right). The pre-activation version reaches slightly higher training loss at convergence, but produces lower test error. This phenomenon is observed on ResNet-110, ResNet-110(1-layer), and ResNet-164 on both CIFAR-10 and 100. This is presumably caused by BN’s regularization eﬀect \[8\]. In the original Residual Unit (Fig. 4(a)), although the BN normalizes the signal, this is soon added to the shortcut and thus the merged signal is not normalized. This unnormalized signal is then used as the input of the next weight layer. On the contrary, in our pre-activation version, the inputs to all weight layers have been normalized.

---

Full document: [06 - Identity Mappings in Deep Residual Networks](../../papers/06-identity-mappings-in-deep-residual-networks.md) · Page-level evidence: [paper-pages/06-identity-mappings-in-deep-residual-networks](../../paper-pages/06-identity-mappings-in-deep-residual-networks/index.md)
