---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/15-deep-speech-2.md
source: ../../papers/15-deep-speech-2.md
paper_title: "Deep Speech 2: End-to-End Speech Recognition in English and Mandarin"
sequence: 15
page: 4
pages: [4]
page_of: 28
topics: ["../../topics/speech-recognition.md", "../../topics/recurrent-neural-networks.md"]
description: "CTC Fully Connected Recurrent or GRU (Bidirectional) Batch Normalization 1D or 2D Invariant Convolution Spectrogram Figure 1: Architecture of the DS2…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 4 of 28 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin

> Page 4 of the source PDF, verbatim as extracted. Canonical document: [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md)

CTC

Fully Connected

Recurrent

or GRU (Bidirectional)

Batch Normalization

1D or 2D Invariant Convolution

Spectrogram

Figure 1: Architecture of the DS2 system used to train on both English and Mandarin speech. We explore variants of this architecture by varying the number of convolutional layers from 1 to 3 and the number of recurrent or GRU layers from 1 to 7.

The two sets of activations are summed to form the output activations for the layer hl = −→h l + ←−h l. The function g(·) can be the standard recurrent operation

−→h l

t + −→ U l−→h l

t = f(W lhl−1

t−1 + bl) (3)

where W l is the input-hidden weight matrix, −→ U l is the recurrent weight matrix and bl is a bias term. In this case the input-hidden weights are shared for both directions of the recurrence. The function g(·) can also represent more complex recurrence operations such as the Long Short-Term Memory (LSTM) units \[30\] and the gated recurrent units (GRU) \[11\].

After the bidirectional recurrent layers we apply one or more fully connected layers with

t = f(W lhl−1

hl

t + bl) (4)

The output layer L is a softmax computing a probability distribution over characters given by

k · hL−1

p(ℓt = k|x) = exp(wL

t ) P

t ) (5)

j · hL−1

j exp(wL

The model is trained using the CTC loss function \[22\]. Given an input-output pair (x, y) and the current parameters of the network θ, we compute the loss function L(x, y; θ) and its derivative with respect to the parameters of the network ∇θL(x, y; θ). This derivative is then used to update the network parameters through the backpropagation through time algorithm.

In the following subsections we describe the architectural and algorithmic improvements made relative to DS1 \[26\]. Unless otherwise stated these improvements are language agnostic. We report results on an English speaker held out development set which is an internal dataset containing 2048 utterances of primarily read speech. All models are trained on datasets described in Section 5. We report Word Error Rate (WER) for the English system and Character Error Rate (CER) for the Mandarin system. In both cases we integrate a language model in a beam search decoding step as described in Section 3.8.

---

[previous page](page-003.md) · [next page](page-005.md) · [all pages](index.md)
