---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/15-deep-speech-2.md
source: ../../papers/15-deep-speech-2.md
paper_title: "Deep Speech 2: End-to-End Speech Recognition in English and Mandarin"
sequence: 15
section: 3.4 Comparison of simple RNNs and GRUs
section_role: other
section_index: 9
pages: [7, 8]
topics: ["../../topics/speech-recognition.md", "../../topics/recurrent-neural-networks.md"]
description: "The models we have shown so far are simple RNNs that have bidirectional recurrent layers with the recurrence for both the forward in time and…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.4 Comparison of simple RNNs and GRUs

> Section 9 of 38 from [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md) · `other` · pages 7-8

The models we have shown so far are simple RNNs that have bidirectional recurrent layers with the recurrence for both the forward in time and backward in time directions modeled by Equation 3. Current research in speech and language processing has shown that having a more complex recurrence can allow the network to remember state over more time-steps while making them more computationally expensive to train \[52, 8, 62, 2\]. Two commonly used recurrent architectures are the Long Short-Term Memory (LSTM) units \[30\] and the Gated Recurrent Units (GRU) \[11\], though many other variations exist. A recent comprehensive study of thousands of variations of LSTM and GRU architectures showed that a GRU is comparable to an LSTM with a properly initialized forget gate bias, and their best variants are competitive with each other \[32\]. We decided to examine GRUs because experiments on smaller data sets showed the GRU and LSTM reach similar accuracy for the same number of parameters, but the GRUs were faster to train and less likely to diverge.

The GRUs we use are computed by

zt = σ(Wzxt + Uzht−1 + bz) rt = σ(Wrxt + Urht−1 + br) ˜ht = f(Whxt + rt ◦Uhht−1 + bh)

(10)

ht = (1 −zt)ht−1 + zt˜ht

where σ(·) is the sigmoid function, z and r represent the update and reset gates respectively, and we drop the layer superscripts for simplicity. We differ slightly from the standard GRU in that we multiply the hidden state ht−1 by Uh prior to scaling by the reset gate. This allows for all operations on ht−1 to be computed in a single matrix multiplication. The output nonlinearity f(·) is typically the hyperbolic tangent function tanh. However, we find similar performance for tanh and clippedReLU nonlinearities and choose to use the clipped-ReLU for simplicity and uniformity with the rest of the network.

Both GRU and simple RNN architectures benefit from batch normalization and show strong results with deep networks. However, Table 3 shows that for a fixed number of parameters, the GRU architectures achieve better WER for all network depths. This is clear evidence of the long term dependencies inherent in the speech recognition task present both within individual words and be-

Architecture Channels Filter dimension Stride Regular Dev Noisy Dev

1-layer 1D 1280 11 2 9.52 19.36 2-layer 1D 640, 640 5, 5 1, 2 9.67 19.21 3-layer 1D 512, 512, 512 5, 5, 5 1, 1, 2 9.20 20.22 1-layer 2D 32 41x11 2x2 8.94 16.22 2-layer 2D 32, 32 41x11, 21x11 2x2, 2x1 9.06 15.71 3-layer 2D 32, 32, 96 41x11, 21x11, 21x11 2x2, 2x1, 2x1 8.61 14.74

Table 4: Comparison of WER for various arrangements of convolutional layers. In all cases, the convolutions are followed by 7 recurrent layers and 1 fully connected layer. For 2D-invariant convolutions the first dimension is frequency and the second dimension is time. All models have BatchNorm, SortaGrad, and 35 million parameters.

tween words. As we discuss in Section 3.8, even simple RNNs are able to implicitly learn a language model due to the large amount of training data. Interestingly, the GRU networks with 5 or more recurrent layers do not significantly improve performance. We attribute this to the thinning from 1728 hidden units per layer for 1 recurrent layer to 768 hidden units per layer for 7 recurrent layers, to keep the total number of parameters constant.

The GRU networks outperform the simple RNNs in Table 3. However, in later results (Section 6) we find that as we scale up the model size, for a fixed computational budget the simple RNN networks perform slightly better. Given this, most of the remaining experiments use the simple RNN layers rather than the GRUs.

---

Full document: [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md) · Page-level evidence: [paper-pages/15-deep-speech-2](../../paper-pages/15-deep-speech-2/index.md)
