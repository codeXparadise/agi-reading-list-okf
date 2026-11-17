---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/04-imagenet-classification-alexnet.md
source: ../../papers/04-imagenet-classification-alexnet.md
paper_title: ImageNet Classification with Deep Convolutional Neural Networks
sequence: 4
section: 5 Details of learning
section_role: other
section_index: 14
pages: []
topics: ["../../topics/convolutional-networks.md", "../../topics/regularization.md"]
description: "We trained our models using stochastic gradient descent with a batch size of 128 examples, momentum of 0.9, and weight decay of 0.0005. We found that…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 5 Details of learning

> Section 14 of 18 from [04 - ImageNet Classification with Deep Convolutional Neural Networks](../../papers/04-imagenet-classification-alexnet.md) · `other` · pages n/a

We trained our models using stochastic gradient descent
with a batch size of 128 examples, momentum of 0.9, and
weight decay of 0.0005. We found that this small amount
of weight decay was important for the model to learn. In
other words, weight decay here is not merely a regularizer:
it reduces the model’s training error. The update rule for
weight *w* was
〈 〉
∣

$$
\begin{array}{l c l}{v_{i+1}}&{:=}&{0.9\cdot v_{i}-0.0005\cdot\epsilon\cdot w_{i}-\epsilon\cdot\left\langle\frac{\partial L}{\partial w}\big|_{w_{i}}\right\rangle_{D_{i}}}\\ \end{array}
$$

Figure 3: 96 convolutional kernels of size
11×11×3 learned by the first convolutional
layer on the 224×224×3 input images. The
top 48 kernels were learned on GPU 1 while
the bottom 48 kernels were learned on GPU
2. See Section 6.1 for details.

$$
w_{i+1}\quad:=\quad w_i+v_{i+1}
$$

$$
224×224×3
$$

〈 ∣ 〉
∂L∣
where *i* is the iteration index, *v* is the momentum variable, is the learning rate, and is
∂w wi
Di
the average over the ith batch Di of the derivative of the objective with respect to w, evaluated at
wi.

$$
\left\langle\frac{\partial L}{\partial w}\big|_{w_{i}}\right\rangle_{D_{i}}
$$

$$
D_{i}
$$

$$
w_{i}
$$

We initialized the weights in each layer from a zero-mean Gaussian distribution with standard deviation 0.01. We initialized the neuron biases in the second, fourth, and fifth convolutional layers,
as well as in the fully-connected hidden layers, with the constant 1. This initialization accelerates
the early stages of learning by providing the ReLUs with positive inputs. We initialized the neuron
biases in the remaining layers with the constant 0.

We used an equal learning rate for all layers, which we adjusted manually throughout training.
The heuristic which we followed was to divide the learning rate by 10 when the validation error
rate stopped improving with the current learning rate. The learning rate was initialized at 0.01 and reduced three times prior to termination. We trained the network for roughly 90 cycles through the
training set of 1.2 million images, which took five to six days on two NVIDIA GTX 580 3GB GPUs.

---

Full document: [04 - ImageNet Classification with Deep Convolutional Neural Networks](../../papers/04-imagenet-classification-alexnet.md) · Page-level evidence: [paper-pages/04-imagenet-classification-alexnet](../../paper-pages/04-imagenet-classification-alexnet/index.md)
