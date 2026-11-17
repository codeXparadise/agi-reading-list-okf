---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/04-imagenet-classification-alexnet.md
source: ../../papers/04-imagenet-classification-alexnet.md
paper_title: ImageNet Classification with Deep Convolutional Neural Networks
sequence: 4
section: 3.4 Overlapping Pooling
section_role: other
section_index: 9
pages: []
topics: ["../../topics/convolutional-networks.md", "../../topics/regularization.md"]
description: "Pooling layers in CNNs summarize the outputs of neighboring groups of neurons in the same kernel map. Traditionally, the neighborhoods summarized by…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.4 Overlapping Pooling

> Section 9 of 18 from [04 - ImageNet Classification with Deep Convolutional Neural Networks](../../papers/04-imagenet-classification-alexnet.md) · `other` · pages n/a

Pooling layers in CNNs summarize the outputs of neighboring groups of neurons in the same kernel
map. Traditionally, the neighborhoods summarized by adjacent pooling units do not overlap (e.g.,
[17, 11, 4]). To be more precise, a pooling layer can be thought of as consisting of a grid of pooling
units spaced *s* pixels apart, each summarizing a neighborhood of size *z × z* centered at the location
of the pooling unit. If we set *s* = *z,* we obtain traditional local pooling as commonly employed
in CNNs. If we set *s < z,* we obtain overlapping pooling. This is what we use throughout our
network, with *s* = 2 and *z* = 3. This scheme reduces the top-1 and top-5 error rates by 0.4% and
0.3%, respectively, as compared with the non-overlapping scheme *s* = *2,z* = 2, which produces
output of equivalent dimensions. We generally observe during training that models with overlapping
pooling find it slightly more difficult to overfit.

$$
s=2,z=2
$$

---

Full document: [04 - ImageNet Classification with Deep Convolutional Neural Networks](../../papers/04-imagenet-classification-alexnet.md) · Page-level evidence: [paper-pages/04-imagenet-classification-alexnet](../../paper-pages/04-imagenet-classification-alexnet/index.md)
