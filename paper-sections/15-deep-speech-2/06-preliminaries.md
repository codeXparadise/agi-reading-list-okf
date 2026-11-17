---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/15-deep-speech-2.md
source: ../../papers/15-deep-speech-2.md
paper_title: "Deep Speech 2: End-to-End Speech Recognition in English and Mandarin"
sequence: 15
section: 3.1 Preliminaries
section_role: other
section_index: 6
pages: [3, 4, 5]
topics: ["../../topics/speech-recognition.md", "../../topics/recurrent-neural-networks.md"]
description: "Figure 1 shows the architecture of the DS2 system which at its core is similar to the previous DS1 system [26]: a recurrent neural network (RNN)…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.1 Preliminaries

> Section 6 of 38 from [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md) · `other` · pages 3-5

Figure 1 shows the architecture of the DS2 system which at its core is similar to the previous DS1 system \[26\]: a recurrent neural network (RNN) trained to ingest speech spectrograms and generate text transcriptions.

Let a single utterance x(i) and label y(i) be sampled from a training set X = {(x(1), y(1)), (x(2), y(2)), . . .}. Each utterance, x(i), is a time-series of length T (i) where every time-slice is a vector of audio features, x(i)

t , t = 0, . . . , T (i) −1. We use a spectrogram of power normalized audio clips as the features to the system, so x(i)

t,p denotes the power of the p’th frequency bin in the audio frame at time t. The goal of the RNN is to convert an input sequence x(i) into a final transcription y(i). For notational convenience, we drop the superscripts and use x to denote a chosen utterance and y the corresponding label.

The outputs of the network are the graphemes of each language. At each output time-step t, the RNN makes a prediction over characters, p(ℓt|x), where ℓt is either a character in the alphabet or the blank symbol. In English we have ℓt ∈{a, b, c, . . . , z, space, apostrophe, blank}, where we have added the apostrophe as well as a space symbol to denote word boundaries. For the Mandarin system the network outputs simplified Chinese characters. We describe this in more detail in Section 3.9.

The RNN model is composed of several layers of hidden units. The architectures we experiment with consist of one or more convolutional layers, followed by one or more recurrent layers, followed by one or more fully connected layers.

The hidden representation at layer l is given by hl with the convention that h0 represents the input x. The bottom of the network is one or more convolutions over the time dimension of the input. For a context window of size c, the i-th activation at time-step t of the convolutional layer is given by

i ◦hl−1

hl

t,i = f(wl

t−c:t+c) (1)

where ◦denotes the element-wise product between the i-th filter and the context window of the previous layers activations, and f denotes a unary nonlinear function. We use the clipped rectifiedlinear (ReLU) function σ(x) = min{max{x, 0}, 20} as our nonlinearity. In some layers, usually the first, we sub-sample by striding the convolution by s frames. The goal is to shorten the number of time-steps for the recurrent layers above.

Following the convolutional layers are one or more bidirectional recurrent layers \[57\]. The forward in time −→h l and backward in time ←−h l recurrent layer activations are computed as

−→h l

t , −→h l

t = g(hl−1

t−1) ←−h l

(2)

t , ←−h l

t = g(hl−1

t+1)

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

Architecture Hidden Units Train Dev

Baseline BatchNorm Baseline BatchNorm

1 RNN, 5 total 2400 10.55 11.99 13.55 14.40 3 RNN, 5 total 1880 9.55 8.29 11.61 10.56 5 RNN, 7 total 1510 8.59 7.61 10.77 9.78 7 RNN, 9 total 1280 8.76 7.68 10.83 9.52

Table 1: Comparison of WER on a training and development set for various depths of RNN, with and without BatchNorm. The number of parameters is kept constant as the depth increases, thus the number of hidden units per layer decreases. All networks have 38 million parameters. The architecture “M RNN, N total” implies 1 layer of 1D convolution at the input, M consecutive bidirectional RNN layers, and the rest as fully-connected layers with N total layers in the network.

---

Full document: [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md) · Page-level evidence: [paper-pages/15-deep-speech-2](../../paper-pages/15-deep-speech-2/index.md)
