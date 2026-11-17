---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/05-deep-residual-learning-resnet.md
source: ../../papers/05-deep-residual-learning-resnet.md
paper_title: Deep Residual Learning for Image Recognition
sequence: 5
section: PASCAL VOC
section_role: other
section_index: 20
pages: [10, 11]
topics: ["../../topics/residual-connections.md", "../../topics/convolutional-networks.md"]
description: "We revisit the PASCAL VOC dataset based on the above model. With the single model on the COCO dataset (55.7% mAP@.5 in Table 9), we fine-tune this…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# PASCAL VOC

> Section 20 of 21 from [05 - Deep Residual Learning for Image Recognition](../../papers/05-deep-residual-learning-resnet.md) · `other` · pages 10-11

We revisit the PASCAL VOC dataset based on the above model. With the single model on the COCO dataset (55.7% mAP@.5 in Table 9), we fine-tune this model on the PASCAL VOC sets. The improvements of box refinement, context, and multi-scale testing are also adopted. By doing so

6http://host.robots.ox.ac.uk:8080/anonymous/3OJ4OJ.html, submitted on 2015-11-26.

11

method top-5 localization err

top-5 LOC error on predicted CLS VGG’s \[41\] VGG-16 1-crop 33.1 \[41\] RPN ResNet-101 1-crop 13.3 RPN ResNet-101 dense 11.7 RPN ResNet-101 dense ResNet-101 14.4 RPN+RCNN ResNet-101 dense ResNet-101 10.6 RPN+RCNN ensemble dense ensemble 8.9

LOC method

LOC network testing LOC error

classification

on GT CLS

network

val test OverFeat \[40\] (ILSVRC’13) 30.0 29.9 GoogLeNet \[44\] (ILSVRC’14) 26.7 VGG \[41\] (ILSVRC’14) 26.9 25.3 ours (ILSVRC’15) 8.9 9.0

Table 14. Comparisons of localization error (%) on the ImageNet dataset with state-of-the-art methods.

Table 13. Localization error (%) on the ImageNet validation. In the column of “LOC error on GT class” (\[41\]), the ground truth class is used. In the “testing” column, “1-crop” denotes testing on a center crop of 224×224 pixels, “dense” denotes dense (fully convolutional) and multi-scale testing.

ports a center-crop error of 33.1% (Table 13) using ground truth classes. Under the same setting, our RPN method using ResNet-101 net significantly reduces the center-crop error to 13.3%. This comparison demonstrates the excellent performance of our framework. With dense (fully convolutional) and multi-scale testing, our ResNet-101 has an error of 11.7% using ground truth classes. Using ResNet-101 for predicting classes (4.6% top-5 classification error, Table 4), the top-5 localization error is 14.4%.

58.8% mAP and our ensemble of 3 models has 62.1% mAP on the DET test set (Table 12). This result won the 1st place in the ImageNet detection task in ILSVRC 2015, surpassing the second place by 8.5 points (absolute).

---

Full document: [05 - Deep Residual Learning for Image Recognition](../../papers/05-deep-residual-learning-resnet.md) · Page-level evidence: [paper-pages/05-deep-residual-learning-resnet](../../paper-pages/05-deep-residual-learning-resnet/index.md)
