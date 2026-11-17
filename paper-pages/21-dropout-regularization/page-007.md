---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/21-dropout-regularization.md
source: ../../papers/21-dropout-regularization.md
paper_title: "Dropout: A Simple Way to Prevent Neural Networks from Overfitting"
sequence: 21
page: 7
pages: [7]
page_of: 18
topics: ["../../topics/regularization.md"]
description: "A Experiments on MNIST A.1 Details for dropout training The MNIST dataset consists of 28 × 28 digit images - 60,000 for training and 10,000 for…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 7 of 18 - Dropout: A Simple Way to Prevent Neural Networks from Overfitting

> Page 7 of the source PDF, verbatim as extracted. Canonical document: [21 - Dropout: A Simple Way to Prevent Neural Networks from Overfitting](../../papers/21-dropout-regularization.md)

## A Experiments on MNIST

## A.1 Details for dropout training

The MNIST dataset consists of 28 × 28 digit images - 60,000 for training and 10,000 for testing. The objective is to classify the digit images into their correct digit class. We experimented with neural nets of different architectures (different number of hidden units and layers) to evaluate the sensitivity of the dropout method to these choices. We show results for 4 nets (784-800800-10, 784-1200-1200-10, 784-2000-2000-10, 784-1200-1200-1200-10). For each of these architectures we use the same dropout rates - 50% dropout for all hidden units and 20% dropout for visible units. We use stochastic gradient descent with 100-sized minibatches and a crossentropy objective function. An exponentially decaying learning rate is used that starts at the value of 10.0 (applied to the average gradient in each minibatch). The learning rate is multiplied by 0.998 after each epoch of training. The incoming weight vector corresponding to each hidden unit is constrained to have a maximum squared length of l. If, as a result of an update, the squared length exceeds l, the vector is scaled down so as to make it have a squared length of l. Using cross validation we found that l = 15 gave best results. Weights are initialzed to small random values drawn from a zero-mean normal distribution with standard deviation 0.01. Momentum is used to speed up learning. The momentum starts off at a value of 0.5 and is increased linearly to 0.99 over the first 500 epochs, after which it stays at 0.99. Also, the learning rate is multiplied by a factor of (1-momentum). No weight decay is used. Weights were updated at the end of each minibatch. Training was done for 3000 epochs. The weight update takes the following form:

∆wt = pt∆wt−1 −(1 −pt)ϵt⟨∇wL⟩ wt = wt−1 + ∆wt,

where,

ϵt = ϵ0f t

(

t T pi + (1 −t

T )pf t < T pf t ≥T

pt =

with ϵ0 = 10.0, f = 0.998, pi = 0.5, pf = 0.99, T = 500. While using a constant learning rate also gives improvements over standard backpropagation, starting with a high learning rate and decaying it provided a significant boost in performance. Constraining input vectors to have a fixed length prevents weights from increasing arbitrarily in magnitude irrespective of the learning rate. This gives the network a lot of opportunity to search for a good configuration in the weight space. As the learning rate decays, the algorithm is able to take smaller steps and finds the right step size at which it can make learning progress. Using a high final momentum distributes gradient information over a large number of updates making learning stable in this scenario where each gradient computation is for a different stochastic network.

8

---

[previous page](page-006.md) · [next page](page-008.md) · [all pages](index.md)
