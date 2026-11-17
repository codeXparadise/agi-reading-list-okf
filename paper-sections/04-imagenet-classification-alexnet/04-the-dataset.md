---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/04-imagenet-classification-alexnet.md
source: ../../papers/04-imagenet-classification-alexnet.md
paper_title: ImageNet Classification with Deep Convolutional Neural Networks
sequence: 4
section: 2 The Dataset
section_role: other
section_index: 4
pages: []
topics: ["../../topics/convolutional-networks.md", "../../topics/regularization.md"]
description: "ImageNet is a dataset of over 15 million labeled high-resolution images belonging to roughly 22,000 categories. The images were collected from the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2 The Dataset

> Section 4 of 18 from [04 - ImageNet Classification with Deep Convolutional Neural Networks](../../papers/04-imagenet-classification-alexnet.md) · `other` · pages n/a

ImageNet is a dataset of over 15 million labeled high-resolution images belonging to roughly 22,000
categories. The images were collected from the web and labeled by human labelers using Amazon’s Mechanical Turk crowd-sourcing tool. Starting in 2010, as part of the Pascal Visual Object
Challenge, an annual competition called the ImageNet Large-Scale Visual Recognition Challenge
(ILSVRC) has been held. ILSVRC uses a subset of ImageNet with roughly 1000 images in each of
1000 categories. In all, there are roughly 1.2 million training images, 50,000 validation images, and
150,000 testing images.

ILSVRC-2010 is the only version of ILSVRC for which the test set labels are available, so this is
the version on which we performed most of our experiments. Since we also entered our model in
the ILSVRC-2012 competition, in Section 6 we report our results on this version of the dataset as
well, for which test set labels are unavailable. On ImageNet, it is customary to report two error rates:
top-1 and top-5, where the top-5 error rate is the fraction of test images for which the correct label
is not among the five labels considered most probable by the model.

ImageNet consists of variable-resolution images, while our system requires a constant input dimensionality. Therefore, we down-sampled the images to a fixed resolution of 256 *×* 256. Given a
rectangular image, we first rescaled the image such that the shorter side was of length 256, and then
cropped out the central 256×256 patch from the resulting image. We did not pre-process the images
in any other way, except for subtracting the mean activity over the training set from each pixel. So
we trained our network on the (centered) raw RGB values of the pixels.

---

Full document: [04 - ImageNet Classification with Deep Convolutional Neural Networks](../../papers/04-imagenet-classification-alexnet.md) · Page-level evidence: [paper-pages/04-imagenet-classification-alexnet](../../paper-pages/04-imagenet-classification-alexnet/index.md)
