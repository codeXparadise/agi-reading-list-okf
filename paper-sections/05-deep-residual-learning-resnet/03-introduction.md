---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/05-deep-residual-learning-resnet.md
source: ../../papers/05-deep-residual-learning-resnet.md
paper_title: Deep Residual Learning for Image Recognition
sequence: 5
section: 1. Introduction
section_role: introduction
section_index: 3
pages: [1]
topics: ["../../topics/residual-connections.md", "../../topics/convolutional-networks.md"]
description: "Deep convolutional neural networks [22, 21] have led to a series of breakthroughs for image classification [21, 50, 40]. Deep networks naturally…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 1. Introduction

> Section 3 of 21 from [05 - Deep Residual Learning for Image Recognition](../../papers/05-deep-residual-learning-resnet.md) · `introduction` · pages 1-1

Deep convolutional neural networks \[22, 21\] have led to a series of breakthroughs for image classification \[21, 50, 40\]. Deep networks naturally integrate low/mid/highlevel features \[50\] and classifiers in an end-to-end multilayer fashion, and the “levels” of features can be enriched by the number of stacked layers (depth). Recent evidence \[41, 44\] reveals that network depth is of crucial importance, and the leading results \[41, 44, 13, 16\] on the challenging ImageNet dataset \[36\] all exploit “very deep” \[41\] models, with a depth of sixteen \[41\] to thirty \[16\]. Many other nontrivial visual recognition tasks \[8, 12, 7, 32, 27\] have also

The degradation (of training accuracy) indicates that not all systems are similarly easy to optimize. Let us consider a shallower architecture and its deeper counterpart that adds more layers onto it. There exists a solution by construction to the deeper model: the added layers are identity mapping, and the other layers are copied from the learned shallower model. The existence of this constructed solution indicates that a deeper model should produce no higher training error than its shallower counterpart. But experiments show that our current solvers on hand are unable to find solutions that

1http://image-net.org/challenges/LSVRC/2015/ and http://mscoco.org/dataset/#detections-challenge2015.

1

ImageNet test set, and won the 1st place in the ILSVRC 2015 classification competition. The extremely deep representations also have excellent generalization performance on other recognition tasks, and lead us to further win the 1st places on: ImageNet detection, ImageNet localization, COCO detection, and COCO segmentation in ILSVRC & COCO 2015 competitions. This strong evidence shows that the residual learning principle is generic, and we expect that it is applicable in other vision and non-vision problems.

## x

weight layer

relu

F(x) x

weight layer

identity

relu F(x)+x

Figure 2. Residual learning: a building block.

are comparably good or better than the constructed solution (or unable to do so in feasible time).

---

Full document: [05 - Deep Residual Learning for Image Recognition](../../papers/05-deep-residual-learning-resnet.md) · Page-level evidence: [paper-pages/05-deep-residual-learning-resnet](../../paper-pages/05-deep-residual-learning-resnet/index.md)
