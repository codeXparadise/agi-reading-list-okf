---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/15-deep-speech-2.md
source: ../../papers/15-deep-speech-2.md
paper_title: "Deep Speech 2: End-to-End Speech Recognition in English and Mandarin"
sequence: 15
page: 5
pages: [5]
page_of: 28
topics: ["../../topics/speech-recognition.md", "../../topics/recurrent-neural-networks.md"]
description: "Architecture Hidden Units Train Dev Baseline BatchNorm Baseline BatchNorm 1 RNN, 5 total 2400 10.55 11.99 13.55 14.40 3 RNN, 5 total 1880 9.55 8.29…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 5 of 28 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin

> Page 5 of the source PDF, verbatim as extracted. Canonical document: [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md)

Architecture Hidden Units Train Dev

Baseline BatchNorm Baseline BatchNorm

1 RNN, 5 total 2400 10.55 11.99 13.55 14.40 3 RNN, 5 total 1880 9.55 8.29 11.61 10.56 5 RNN, 7 total 1510 8.59 7.61 10.77 9.78 7 RNN, 9 total 1280 8.76 7.68 10.83 9.52

Table 1: Comparison of WER on a training and development set for various depths of RNN, with and without BatchNorm. The number of parameters is kept constant as the depth increases, thus the number of hidden units per layer decreases. All networks have 38 million parameters. The architecture “M RNN, N total” implies 1 layer of 1D convolution at the input, M consecutive bidirectional RNN layers, and the rest as fully-connected layers with N total layers in the network.

## 3.2 Batch Normalization for Deep RNNs

To efficiently scale our model as we scale the training set, we increase the depth of the networks by adding more hidden layers, rather than making each layer larger. Previous work has examined doing so by increasing the number of consecutive bidirectional recurrent layers \[24\]. We explore Batch Normalization (BatchNorm) as a technique to accelerate training for such networks \[63\] since they often suffer from optimization issues.

Recent research has shown that BatchNorm improves the speed of convergence of recurrent nets, without showing any improvement in generalization performance \[37\]. In contrast, we demonstrate that when applied to very deep networks of simple RNNs on large data sets, batch normalization substantially improves final generalization error while greatly accelerating training.

In a typical feed-forward layer containing an affine transformation followed by a non-linearity f(·), we insert a BatchNorm transformation by applying f(B(Wh)) instead of f(Wh + b), where

B(x) = γ x −E\[x\]

(Var\[x\] + ϵ)1/2 + β. (6)

The terms E and Var are the empirical mean and variance over a minibatch. The bias b of the layer is dropped since its effect is cancelled by mean removal. The learnable parameters γ and β allow the layer to scale and shift each hidden unit as desired. The constant ϵ is small and positive, and is included only for numerical stability. In our convolutional layers the mean and variance are estimated over all the temporal output units for a given convolutional filter on a minibatch. The BatchNorm transformation reduces internal covariate shift by insulating a given layer from potentially uninteresting changes in the mean and variance of the layer’s input.

We consider two methods of extending BatchNorm to bidirectional RNNs \[37\]. A natural extension is to insert a BatchNorm transformation immediately before every non-linearity. Equation 3 then becomes −→h l

t + −→ U l−→h l

t = f(B(W lhl−1

t−1)). (7)

In this case the mean and variance statistics are accumulated over a single time-step of the minibatch. The sequential dependence between time-steps prevents averaging over all time-steps. We find that this technique does not lead to improvements in optimization. We also tried accumulating an average over successive time-steps, so later time-steps are normalized over all present and previous timesteps. This also proved ineffective and greatly complicated backpropagation.

We find that sequence-wise normalization \[37\] overcomes these issues. The recurrent computation is given by −→h l

t ) + −→ U l−→h l

t = f(B(W lhl−1

t−1). (8)

For each hidden unit, we compute the mean and variance statistics over all items in the minibatch over the length of the sequence. Figure 2 shows that deep networks converge faster with sequencewise normalization. Table 1 shows that the performance improvement from sequence-wise normalization increases with the depth of the network, with a 12% performance difference for the deepest network. When comparing depth, in order to control for model size we hold constant the total

---

[previous page](page-004.md) · [next page](page-006.md) · [all pages](index.md)
