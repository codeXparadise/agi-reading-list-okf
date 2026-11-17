---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/04-imagenet-classification-alexnet.md
source: ../../papers/04-imagenet-classification-alexnet.md
paper_title: ImageNet Classification with Deep Convolutional Neural Networks
sequence: 4
section: 4.2 Dropout
section_role: other
section_index: 13
pages: []
topics: ["../../topics/convolutional-networks.md", "../../topics/regularization.md"]
description: "Combining the predictions of many different models is a very successful way to reduce test errors [1, 3], but it appears to be too expensive for big…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 4.2 Dropout

> Section 13 of 18 from [04 - ImageNet Classification with Deep Convolutional Neural Networks](../../papers/04-imagenet-classification-alexnet.md) · `other` · pages n/a

Combining the predictions of many different models is a very successful way to reduce test errors
[1, 3], but it appears to be too expensive for big neural networks that already take several days
to train. There is, however, a very efficient version of model combination that only costs about a
factor of two during training. The recently-introduced technique, called “dropout” [10], consists
of setting to zero the output of each hidden neuron with probability 0.5. The neurons which are
“dropped out” in this way do not contribute to the forward pass and do not participate in backpropagation. So every time an input is presented, the neural network samples a different architecture,
but all these architectures share weights. This technique reduces complex co-adaptations of neurons,
since a neuron cannot rely on the presence of particular other neurons. It is, therefore, forced to
learn more robust features that are useful in conjunction with many different random subsets of the
other neurons. At test time, we use all the neurons but multiply their outputs by 0.5, which is a
reasonable approximation to taking the geometric mean of the predictive distributions produced by
the exponentially-many dropout networks.

We use dropout in the first two fully-connected layers of Figure 2. Without dropout, our network exhibits substantial overfitting. Dropout roughly doubles the number of iterations required to converge.

---

Full document: [04 - ImageNet Classification with Deep Convolutional Neural Networks](../../papers/04-imagenet-classification-alexnet.md) · Page-level evidence: [paper-pages/04-imagenet-classification-alexnet](../../paper-pages/04-imagenet-classification-alexnet/index.md)
