---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/04-imagenet-classification-alexnet.md
source: ../../papers/04-imagenet-classification-alexnet.md
paper_title: ImageNet Classification with Deep Convolutional Neural Networks
sequence: 4
section: 4 Reducing Overfitting
section_role: other
section_index: 11
pages: []
topics: ["../../topics/convolutional-networks.md", "../../topics/regularization.md"]
description: "Our neural network architecture has 60 million parameters. Although the 1000 classes of ILSVRC make each training example impose 10 bits of…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 4 Reducing Overfitting

> Section 11 of 18 from [04 - ImageNet Classification with Deep Convolutional Neural Networks](../../papers/04-imagenet-classification-alexnet.md) · `other` · pages n/a

Our neural network architecture has 60 million parameters. Although the 1000 classes of ILSVRC
make each training example impose 10 bits of constraint on the mapping from image to label, this
turns out to be insufficient to learn so many parameters without considerable overfitting. Below, we
describe the two primary ways in which we combat overfitting.

---

Full document: [04 - ImageNet Classification with Deep Convolutional Neural Networks](../../papers/04-imagenet-classification-alexnet.md) · Page-level evidence: [paper-pages/04-imagenet-classification-alexnet](../../paper-pages/04-imagenet-classification-alexnet/index.md)
