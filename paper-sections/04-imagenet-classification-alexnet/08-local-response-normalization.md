---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/04-imagenet-classification-alexnet.md
source: ../../papers/04-imagenet-classification-alexnet.md
paper_title: ImageNet Classification with Deep Convolutional Neural Networks
sequence: 4
section: 3.3 Local Response Normalization
section_role: other
section_index: 8
pages: []
topics: ["../../topics/convolutional-networks.md", "../../topics/regularization.md"]
description: "ReLUs have the desirable property that they do not require input normalization to prevent them from saturating. If at least some training examples…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.3 Local Response Normalization

> Section 8 of 18 from [04 - ImageNet Classification with Deep Convolutional Neural Networks](../../papers/04-imagenet-classification-alexnet.md) · `other` · pages n/a

ReLUs have the desirable property that they do not require input normalization to prevent them
from saturating. If at least some training examples produce a positive input to a ReLU, learning will
happen in that neuron. However, we still find that the following local normalization scheme aids
generalization. Denoting by aix,y the activity of a neuron computed by applying kernel i at position
(x,y) and then applying the ReLU nonlinearity, the response-normalized activity bix,y is given by
the expression
0 1β

$$
a_{x,y}^{i}
$$

$$
b_{x,y}^{i}
$$

$$
b_{x,y}^{i}=a_{x,y}^{i}/\left(k+\alpha\sum_{j=\max(0,i-n/2)}^{\min(N-1,i+n/2)}(a_{x,y}^{j})^2\right)^{\beta}
$$

where the sum runs over *n* “adjacent” kernel maps at the same spatial position, and *N* is the total
number of kernels in the layer. The ordering of the kernel maps is of course arbitrary and determined
before training begins. This sort of response normalization implements a form of lateral inhibition
inspired by the type found in real neurons, creating competition for big activities amongst neuron
outputs computed using different kernels. The constants *k,n,α,* and *β* are hyper-parameters whose
values are determined using a validation set; we used k = 2, n = 5, α = 10−4, and β = 0.75. We
applied this normalization after applying the ReLU nonlinearity in certain layers (see Section 3.5).

$$
k,n,\alpha,
$$

$$
\beta
$$

$$
k=2,n=5,\alpha=10^{-4}
$$

$$
\beta=0.75
$$

This scheme bears some resemblance to the local contrast normalization scheme of Jarrett et al. [11],
but ours would be more correctly termed “brightness normalization”, since we do not subtract the
mean activity. Response normalization reduces our top-1 and top-5 error rates by 1.4% and 1.2%,
respectively. We also verified the effectiveness of this scheme on the CIFAR-10 dataset: a four-layer
CNN achieved a 13% test error rate without normalization and 11% with normalization3.

---

Full document: [04 - ImageNet Classification with Deep Convolutional Neural Networks](../../papers/04-imagenet-classification-alexnet.md) · Page-level evidence: [paper-pages/04-imagenet-classification-alexnet](../../paper-pages/04-imagenet-classification-alexnet/index.md)
