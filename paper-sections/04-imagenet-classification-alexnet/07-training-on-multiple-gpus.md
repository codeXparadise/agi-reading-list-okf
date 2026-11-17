---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/04-imagenet-classification-alexnet.md
source: ../../papers/04-imagenet-classification-alexnet.md
paper_title: ImageNet Classification with Deep Convolutional Neural Networks
sequence: 4
section: 3.2 Training on Multiple GPUs
section_role: experiments
section_index: 7
pages: []
topics: ["../../topics/convolutional-networks.md", "../../topics/regularization.md"]
description: "A single GTX 580 GPU has only 3GB of memory, which limits the maximum size of the networks that can be trained on it. It turns out that 1.2 million…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.2 Training on Multiple GPUs

> Section 7 of 18 from [04 - ImageNet Classification with Deep Convolutional Neural Networks](../../papers/04-imagenet-classification-alexnet.md) · `experiments` · pages n/a

A single GTX 580 GPU has only 3GB of memory, which limits the maximum size of the networks
that can be trained on it. It turns out that 1.2 million training examples are enough to train networks
which are too big to fit on one GPU. Therefore we spread the net across two GPUs. Current GPUs
are particularly well-suited to cross-GPU parallelization, as they are able to read from and write to
one another’s memory directly, without going through host machine memory. The parallelization
scheme that we employ essentially puts half of the kernels (or neurons) on each GPU, with one
additional trick: the GPUs communicate only in certain layers. This means that, for example, the
kernels of layer 3 take input from all kernel maps in layer 2. However, kernels in layer 4 take input
only from those kernel maps in layer 3 which reside on the same GPU. Choosing the pattern of
connectivity is a problem for cross-validation, but this allows us to precisely tune the amount of
communication until it is an acceptable fraction of the amount of computation.

The resultant architecture is somewhat similar to that of the “columnar” CNN employed by Cirȩsan
et al. [5], except that our columns are not independent (see Figure 2). This scheme reduces our top-1
and top-5 error rates by 1.7% and 1.2%, respectively, as compared with a net with half as many
kernels in each convolutional layer trained on one GPU. The two-GPU net takes slightly less time
to train than the one-GPU net2.

2The one-GPU net actually has the same number of kernels as the two-GPU net in the final convolutional
layer. This is because most of the net’s parameters are in the first fully-connected layer, which takes the last
convolutional layer as input. So to make the two nets have approximately the same number of parameters, we
did not halve the size of the final convolutional layer (nor the fully-conneced layers which follow). Therefore
this comparison is biased in favor of the one-GPU net, since it is bigger than “half the size” of the two-GPU
net.

---

Full document: [04 - ImageNet Classification with Deep Convolutional Neural Networks](../../papers/04-imagenet-classification-alexnet.md) · Page-level evidence: [paper-pages/04-imagenet-classification-alexnet](../../paper-pages/04-imagenet-classification-alexnet/index.md)
