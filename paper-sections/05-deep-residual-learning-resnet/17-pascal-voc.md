---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/05-deep-residual-learning-resnet.md
source: ../../papers/05-deep-residual-learning-resnet.md
paper_title: Deep Residual Learning for Image Recognition
sequence: 5
section: PASCAL VOC
section_role: other
section_index: 17
pages: [9]
topics: ["../../topics/residual-connections.md", "../../topics/convolutional-networks.md"]
description: "Following [7, 32], for the PASCAL VOC 2007 test set, we use the 5k trainval images in VOC 2007 and 16k trainval images in VOC 2012 for training…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# PASCAL VOC

> Section 17 of 21 from [05 - Deep Residual Learning for Image Recognition](../../papers/05-deep-residual-learning-resnet.md) · `other` · pages 9-9

Following \[7, 32\], for the PASCAL VOC 2007 test set, we use the 5k trainval images in VOC 2007 and 16k trainval images in VOC 2012 for training (“07+12”). For the PASCAL VOC 2012 test set, we use the 10k trainval+test images in VOC 2007 and 16k trainval images in VOC 2012 for training (“07++12”). The hyper-parameters for training Faster R-CNN are the same as in \[32\]. Table 7 shows the results. ResNet-101 improves the mAP by >3% over VGG-16. This gain is solely because of the improved features learned by ResNet.

Multi-scale testing. In the above, all results are obtained by single-scale training/testing as in \[32\], where the image’s shorter side is s = 600 pixels. Multi-scale training/testing has been developed in \[12, 7\] by selecting a scale from a feature pyramid, and in \[33\] by using maxout layers. In our current implementation, we have performed multi-scale testing following \[33\]; we have not performed multi-scale training because of limited time. In addition, we have performed multi-scale testing only for the Fast R-CNN step (but not yet for the RPN step). With a trained model, we compute conv feature maps on an image pyramid, where the image’s shorter sides are s ∈{200, 400, 600, 800, 1000}.

---

Full document: [05 - Deep Residual Learning for Image Recognition](../../papers/05-deep-residual-learning-resnet.md) · Page-level evidence: [paper-pages/05-deep-residual-learning-resnet](../../paper-pages/05-deep-residual-learning-resnet/index.md)
