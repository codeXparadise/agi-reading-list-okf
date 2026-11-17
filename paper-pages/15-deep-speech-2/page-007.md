---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/15-deep-speech-2.md
source: ../../papers/15-deep-speech-2.md
paper_title: "Deep Speech 2: End-to-End Speech Recognition in English and Mandarin"
sequence: 15
page: 7
pages: [7]
page_of: 28
topics: ["../../topics/speech-recognition.md", "../../topics/recurrent-neural-networks.md"]
description: "Architecture Simple RNN GRU 5 layers, 1 Recurrent 14.40 10.53 5 layers, 3 Recurrent 10.56 8.00 7 layers, 5 Recurrent 9.78 7.79 9 layers, 7 Recurrent…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 7 of 28 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin

> Page 7 of the source PDF, verbatim as extracted. Canonical document: [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md)

Architecture Simple RNN GRU

5 layers, 1 Recurrent 14.40 10.53 5 layers, 3 Recurrent 10.56 8.00 7 layers, 5 Recurrent 9.78 7.79 9 layers, 7 Recurrent 9.52 8.19

Table 3: Comparison of development set WER for networks with either simple RNN or GRU, for various depths. All models have batch normalization, one layer of 1D-invariant convolution, and approximately 38 million parameters.

In the first training epoch, we iterate through the training set in increasing order of the length of the longest utterance in the minibatch. After the first epoch, training reverts back to a random order over minibatches. Table 2 shows a comparison of training cost with and without SortaGrad on the 9 layer model with 7 recurrent layers. This effect is particularly pronounced for networks without BatchNorm, since they are numerically less stable. In some sense the two techniques substitute for one another, though we still find gains when applying SortaGrad and BatchNorm together. Even with BatchNorm we find that this curriculum improves numerical stability and sensitivity to small changes in training. Numerical instability can arise from different transcendental function implementations in the CPU and the GPU, especially when computing the CTC cost. This curriculum gives comparable results for both implementations.

We suspect that these benefits occur primarily because long utterances tend to have larger gradients, yet we use a fixed learning rate independent of utterance length. Furthermore, longer utterances are more likely to cause the internal state of the RNNs to explode at an early stage in training.

## 3.4 Comparison of simple RNNs and GRUs

The models we have shown so far are simple RNNs that have bidirectional recurrent layers with the recurrence for both the forward in time and backward in time directions modeled by Equation 3. Current research in speech and language processing has shown that having a more complex recurrence can allow the network to remember state over more time-steps while making them more computationally expensive to train \[52, 8, 62, 2\]. Two commonly used recurrent architectures are the Long Short-Term Memory (LSTM) units \[30\] and the Gated Recurrent Units (GRU) \[11\], though many other variations exist. A recent comprehensive study of thousands of variations of LSTM and GRU architectures showed that a GRU is comparable to an LSTM with a properly initialized forget gate bias, and their best variants are competitive with each other \[32\]. We decided to examine GRUs because experiments on smaller data sets showed the GRU and LSTM reach similar accuracy for the same number of parameters, but the GRUs were faster to train and less likely to diverge.

The GRUs we use are computed by

zt = σ(Wzxt + Uzht−1 + bz) rt = σ(Wrxt + Urht−1 + br) ˜ht = f(Whxt + rt ◦Uhht−1 + bh)

(10)

ht = (1 −zt)ht−1 + zt˜ht

where σ(·) is the sigmoid function, z and r represent the update and reset gates respectively, and we drop the layer superscripts for simplicity. We differ slightly from the standard GRU in that we multiply the hidden state ht−1 by Uh prior to scaling by the reset gate. This allows for all operations on ht−1 to be computed in a single matrix multiplication. The output nonlinearity f(·) is typically the hyperbolic tangent function tanh. However, we find similar performance for tanh and clippedReLU nonlinearities and choose to use the clipped-ReLU for simplicity and uniformity with the rest of the network.

Both GRU and simple RNN architectures benefit from batch normalization and show strong results with deep networks. However, Table 3 shows that for a fixed number of parameters, the GRU architectures achieve better WER for all network depths. This is clear evidence of the long term dependencies inherent in the speech recognition task present both within individual words and be-

---

[previous page](page-006.md) · [next page](page-008.md) · [all pages](index.md)
