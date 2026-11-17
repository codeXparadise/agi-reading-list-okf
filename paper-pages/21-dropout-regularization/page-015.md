---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/21-dropout-regularization.md
source: ../../papers/21-dropout-regularization.md
paper_title: "Dropout: A Simple Way to Prevent Neural Networks from Overfitting"
sequence: 21
page: 15
pages: [15]
page_of: 18
topics: ["../../topics/regularization.md"]
description: "where the sum runs over N “adjacent” banks of neurons at the same position in the topographic organization. The ordering of the banks is of course…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 15 of 18 - Dropout: A Simple Way to Prevent Neural Networks from Overfitting

> Page 15 of the source PDF, verbatim as extracted. Canonical document: [21 - Dropout: A Simple Way to Prevent Neural Networks from Overfitting](../../papers/21-dropout-regularization.md)

where the sum runs over N “adjacent” banks of neurons at the same position in the topographic organization. The ordering of the banks is of course arbitrary and determined before training begins. Response normalization layers implement a form of lateral inhibition found in real neurons. The constants N, α, and β are hyper-parameters whose values are determined using a validation set.

## F.3 Neuron nonlinearities

All of the neurons in our networks utilize the max-with-zero nonlinearity. That is, their output is computed as ai

x,y = max(0, zi

x,y) where zi

x,y is the total input to the neuron (equivalently, the output of the neuron’s linear filter added to the bias). This nonlinearity has several advantages over traditional saturating neuron models, including a significant reduction in the training time required to reach a given error rate. This nonlinearity also reduces the need for contrastnormalization and similar data pre-processing schemes, because neurons with this nonlinearity do not saturate – their activities simply scale up when presented with unusually large input values. Consequently, the only data pre-processing step which we take is to subtract the mean activity from each pixel, so that the data is centered. So we train our networks on the (centered) raw RGB values of the pixels.

## F.4 Objective function

Our networks maximize the multinomial logistic regression objective, which is equivalent to minimizing the average across training cases of the cross-entropy between the true label distribution and the model’s predicted label distribution.

## F.5 Weight initialization

We initialize the weights in our model from a zero-mean normal distribution with a variance set high enough to produce positive inputs into the neurons in each layer. This is a slightly tricky point when using the max-with-zero nonlinearity. If the input to a neuron is always negative, no learning will take place because its output will be uniformly zero, as will the derivative of its output with respect to its input. Therefore it’s important to initialize the weights from a distribution with a sufficiently large variance such that all neurons are likely to get positive inputs at least occasionally. In practice, we simply try different variances until we find an initialization that works. It usually only takes a few attempts. We also find that initializing the biases of the neurons in the hidden layers with some positive constant (1 in our case) helps get learning off the ground, for the same reason.

16

---

[previous page](page-014.md) · [next page](page-016.md) · [all pages](index.md)
