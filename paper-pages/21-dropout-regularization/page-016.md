---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/21-dropout-regularization.md
source: ../../papers/21-dropout-regularization.md
paper_title: "Dropout: A Simple Way to Prevent Neural Networks from Overfitting"
sequence: 21
page: 16
pages: [16]
page_of: 18
topics: ["../../topics/regularization.md"]
description: "F.6 Training We train our models using stochastic gradient descent with a batch size of 128 examples and momentum of 0.9. Therefore the update rule…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 16 of 18 - Dropout: A Simple Way to Prevent Neural Networks from Overfitting

> Page 16 of the source PDF, verbatim as extracted. Canonical document: [21 - Dropout: A Simple Way to Prevent Neural Networks from Overfitting](../../papers/21-dropout-regularization.md)

## F.6 Training

We train our models using stochastic gradient descent with a batch size of 128 examples and momentum of 0.9. Therefore the update rule for weight w is

vi+1 = 0.9vi + ϵ < ∂E ∂wi

>i

wi+1 = wi + vi+1

where i is the iteration index, v is a momentum variable, ϵ is the learning rate, and < ∂E ∂wi >i is the average over the ith batch of the derivative of the objective with respect to wi. We use the publicly available cuda-convnet package to train all of our models on a single NVIDIA GTX 580 GPU. Training on CIFAR-10 takes roughly 90 minutes. Training on ImageNet takes roughly four days with dropout and two days without.

## F.7 Learning rates

We use an equal learning rate for each layer, whose value we determine heuristically as the largest power of ten that produces reductions in the objective function. In practice it is typically of the order 10−2 or 10−3. We reduce the learning rate twice by a factor of ten shortly before terminating training.

## G Models for CIFAR-10

Our model for CIFAR-10 without dropout is a CNN with three convolutional layers. Pooling layers follow all three. All of the pooling layers summarize a 3×3 neighborhood and use a stride of 2. The pooling layer which follows the first convolutional layer performs max-pooling, while the remaining pooling layers perform average-pooling. Response normalization layers follow the first two pooling layers, with N = 9, α = 0.001, and β = 0.75. The upper-most pooling layer is connected to a ten-unit softmax layer which outputs a probability distribution over class labels. All convolutional layers have 64 filter banks and use a filter size of 5 × 5 (times the number of channels in the preceding layer).

Our model for CIFAR-10 with dropout is similar, but because dropout imposes a strong regularization on the network, we are able to use more parameters. Therefore we add a fourth weight layer, which takes its input from the third pooling layer. This weight layer is locallyconnected but not convolutional. It is like a convolutional layer in which filters in the same bank do not share weights. This layer contains 16 banks of filters of size 3 × 3. This is the layer in which we use 50% dropout. The softmax layer takes its input from this fourth weight layer.

17

---

[previous page](page-015.md) · [next page](page-017.md) · [all pages](index.md)
