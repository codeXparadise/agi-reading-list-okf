---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/05-deep-residual-learning-resnet.md
source: ../../papers/05-deep-residual-learning-resnet.md
paper_title: Deep Residual Learning for Image Recognition
sequence: 5
section: MS COCO
section_role: other
section_index: 18
pages: [9, 10]
topics: ["../../topics/residual-connections.md", "../../topics/convolutional-networks.md"]
description: "The MS COCO dataset [26] involves 80 object categories. We evaluate the PASCAL VOC metric (mAP @ IoU = 0.5) and the standard COCO metric (mAP @ IoU =…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# MS COCO

> Section 18 of 21 from [05 - Deep Residual Learning for Image Recognition](../../papers/05-deep-residual-learning-resnet.md) · `other` · pages 9-10

The MS COCO dataset \[26\] involves 80 object categories. We evaluate the PASCAL VOC metric (mAP @ IoU = 0.5) and the standard COCO metric (mAP @ IoU = .5:.05:.95). We use the 80k images on the train set for training and the 40k images on the val set for evaluation. Our detection system for COCO is similar to that for PASCAL VOC. We train the COCO models with an 8-GPU implementation, and thus the RPN step has a mini-batch size of

10

training data COCO train COCO trainval test data COCO val COCO test-dev mAP @.5 @\[.5, .95\] @.5 @\[.5, .95\] baseline Faster R-CNN (VGG-16) 41.5 21.2 baseline Faster R-CNN (ResNet-101) 48.4 27.2 +box refinement 49.9 29.9 +context 51.1 30.0 53.3 32.2 +multi-scale testing 53.8 32.5 55.7 34.9 ensemble 59.0 37.4

Table 9. Object detection improvements on MS COCO using Faster R-CNN and ResNet-101.

system net data mAP areo bike bird boat bottle bus car cat chair cow table dog horse mbike person plant sheep sofa train tv baseline VGG-16 07+12 73.2 76.5 79.0 70.9 65.5 52.1 83.1 84.7 86.4 52.0 81.9 65.7 84.8 84.6 77.5 76.7 38.8 73.6 73.9 83.0 72.6 baseline ResNet-101 07+12 76.4 79.8 80.7 76.2 68.3 55.9 85.1 85.3 89.8 56.7 87.8 69.4 88.3 88.9 80.9 78.4 41.7 78.6 79.8 85.3 72.0 baseline+++ ResNet-101 COCO+07+12 85.6 90.0 89.6 87.8 80.8 76.1 89.9 89.9 89.6 75.5 90.0 80.7 89.6 90.3 89.1 88.7 65.4 88.1 85.6 89.0 86.8

Table 10. Detection results on the PASCAL VOC 2007 test set. The baseline is the Faster R-CNN system. The system “baseline+++” include box refinement, context, and multi-scale testing in Table 9.

system net data mAP areo bike bird boat bottle bus car cat chair cow table dog horse mbike person plant sheep sofa train tv baseline VGG-16 07++12 70.4 84.9 79.8 74.3 53.9 49.8 77.5 75.9 88.5 45.6 77.1 55.3 86.9 81.7 80.9 79.6 40.1 72.6 60.9 81.2 61.5 baseline ResNet-101 07++12 73.8 86.5 81.6 77.2 58.0 51.0 78.6 76.6 93.2 48.6 80.4 59.0 92.1 85.3 84.8 80.7 48.1 77.3 66.5 84.7 65.6 baseline+++ ResNet-101 COCO+07++12 83.8 92.1 88.4 84.8 75.9 71.4 86.3 87.8 94.2 66.8 89.4 69.2 93.9 91.9 90.9 89.6 67.9 88.2 76.8 90.3 80.0

Table 11. Detection results on the PASCAL VOC 2012 test set (http://host.robots.ox.ac.uk:8080/leaderboard/ displaylb.php?challengeid=11&compid=4). The baseline is the Faster R-CNN system. The system “baseline+++” include box refinement, context, and multi-scale testing in Table 9.

We select two adjacent scales from the pyramid following \[33\]. RoI pooling and subsequent layers are performed on the feature maps of these two scales \[33\], which are merged by maxout as in \[33\]. Multi-scale testing improves the mAP by over 2 points (Table 9).

val2 test

GoogLeNet \[44\] (ILSVRC’14) 43.9

our single model (ILSVRC’15) 60.5 58.8 our ensemble (ILSVRC’15) 63.6 62.1

Table 12. Our results (mAP, %) on the ImageNet detection dataset. Our detection system is Faster R-CNN \[32\] with the improvements in Table 9, using ResNet-101.

Using validation data. Next we use the 80k+40k trainval set for training and the 20k test-dev set for evaluation. The testdev set has no publicly available ground truth and the result is reported by the evaluation server. Under this setting, the results are an mAP@.5 of 55.7% and an mAP@\[.5, .95\] of 34.9% (Table 9). This is our single-model result.

we achieve 85.6% mAP on PASCAL VOC 2007 (Table 10) and 83.8% on PASCAL VOC 2012 (Table 11)6. The result on PASCAL VOC 2012 is 10 points higher than the previous state-of-the-art result \[6\].

Ensemble. In Faster R-CNN, the system is designed to learn region proposals and also object classifiers, so an ensemble can be used to boost both tasks. We use an ensemble for proposing regions, and the union set of proposals are processed by an ensemble of per-region classifiers. Table 9 shows our result based on an ensemble of 3 networks. The mAP is 59.0% and 37.4% on the test-dev set. This result won the 1st place in the detection task in COCO 2015.

---

Full document: [05 - Deep Residual Learning for Image Recognition](../../papers/05-deep-residual-learning-resnet.md) · Page-level evidence: [paper-pages/05-deep-residual-learning-resnet](../../paper-pages/05-deep-residual-learning-resnet/index.md)
