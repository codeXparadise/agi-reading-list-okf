---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/21-dropout-regularization.md
source: ../../papers/21-dropout-regularization.md
paper_title: "Dropout: A Simple Way to Prevent Neural Networks from Overfitting"
sequence: 21
section: F.6 Training
section_role: other
section_index: 12
pages: [16]
topics: ["../../topics/regularization.md"]
description: "We train our models using stochastic gradient descent with a batch size of 128 examples and momentum of 0.9. Therefore the update rule for weight w…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# F.6 Training

> Section 12 of 14 from [21 - Dropout: A Simple Way to Prevent Neural Networks from Overfitting](../../papers/21-dropout-regularization.md) · `other` · pages 16-16

We train our models using stochastic gradient descent with a batch size of 128 examples and momentum of 0.9. Therefore the update rule for weight w is

vi+1 = 0.9vi + ϵ < ∂E ∂wi

>i

wi+1 = wi + vi+1

where i is the iteration index, v is a momentum variable, ϵ is the learning rate, and < ∂E ∂wi >i is the average over the ith batch of the derivative of the objective with respect to wi. We use the publicly available cuda-convnet package to train all of our models on a single NVIDIA GTX 580 GPU. Training on CIFAR-10 takes roughly 90 minutes. Training on ImageNet takes roughly four days with dropout and two days without.

## F.7 Learning rates

We use an equal learning rate for each layer, whose value we determine heuristically as the largest power of ten that produces reductions in the objective function. In practice it is typically of the order 10−2 or 10−3. We reduce the learning rate twice by a factor of ten shortly before terminating training.

---

Full document: [21 - Dropout: A Simple Way to Prevent Neural Networks from Overfitting](../../papers/21-dropout-regularization.md) · Page-level evidence: [paper-pages/21-dropout-regularization](../../paper-pages/21-dropout-regularization/index.md)
