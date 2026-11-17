---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/04-imagenet-classification-alexnet.md
source: ../../papers/04-imagenet-classification-alexnet.md
paper_title: ImageNet Classification with Deep Convolutional Neural Networks
sequence: 4
section: 3.1 ReLU Nonlinearity
section_role: other
section_index: 6
pages: []
topics: ["../../topics/convolutional-networks.md", "../../topics/regularization.md"]
description: "The standard way to model a neuron’s output f as a function of its input x is with f (x) = tanh(x) or f (x) = (1 + e−x)−1. In terms of training time…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.1 ReLU Nonlinearity

> Section 6 of 18 from [04 - ImageNet Classification with Deep Convolutional Neural Networks](../../papers/04-imagenet-classification-alexnet.md) · `other` · pages n/a

The standard way to model a neuron’s output *f* as
a function of its input *x* is with *f* (x) = tanh(x)
or f (x) = (1 + e−x)−1. In terms of training time
with gradient descent, these saturating nonlinearities
are much slower than the non-saturating nonlinearity
*f* (x) = max(0,x). Following Nair and Hinton [20],
we refer to neurons with this nonlinearity as Rectified
Linear Units (ReLUs). Deep convolutional neural networks with ReLUs train several times faster than their
equivalents with tanh units. This is demonstrated in
Figure 1, which shows the number of iterations required to reach 25% training error on the CIFAR-10
dataset for a particular four-layer convolutional network. This plot shows that we would not have been
able to experiment with such large neural networks for
this work if we had used traditional saturating neuron
models.

$$
f(x)=\tanh(x)
$$

$$
f(x)=(1+e^{-x})^{-1}
$$

$$
f(x)=\max(0,x)
$$

We are not the first to consider alternatives to traditional neuron models in CNNs. For example, Jarrett
et al. [11] claim that the nonlinearityf (x) = *|*tanh(x)*|*
works particularly well with their type of contrast normalization followed by local average pooling on the
Caltech-101 dataset. However, on this dataset the primary concern is preventing overfitting, so the effect
they are observing is different from the accelerated
ability to fit the training set which we report when using ReLUs. Faster learning has a great influence on the
performance of large models trained on large datasets.

$$
f(x)=\left|\tanh(x)\right|
$$

| Epochs | Training error rate |
| --- | --- |
| 0 | 0.75 |
| 5 | 0.26 |
| 10 | 0.36 |
| 15 | 0.32 |
| 20 | 0.30 |
| 25 | 0.28 |
| 30 | 0.27 |
| 35 | 0.26 |

Figure 1: A four-layer convolutional neural
network with ReLUs **(solid line)** reaches a 25%
training error rate on CIFAR-10 six times faster
than an equivalent network with tanh neurons
**(dashed line).** The learning rates for each network were chosen independently to make training as fast as possible. No regularization of
any kind was employed. The magnitude of the
effect demonstrated here varies with network
architecture, but networks with ReLUs consistently learn several times faster than equivalents
with saturating neurons.

---

Full document: [04 - ImageNet Classification with Deep Convolutional Neural Networks](../../papers/04-imagenet-classification-alexnet.md) · Page-level evidence: [paper-pages/04-imagenet-classification-alexnet](../../paper-pages/04-imagenet-classification-alexnet/index.md)
