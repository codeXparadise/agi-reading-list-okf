---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/15-deep-speech-2.md
source: ../../papers/15-deep-speech-2.md
paper_title: "Deep Speech 2: End-to-End Speech Recognition in English and Mandarin"
sequence: 15
page: 3
pages: [3]
page_of: 28
topics: ["../../topics/speech-recognition.md", "../../topics/recurrent-neural-networks.md"]
description: "bootstrapping larger datasets and data augmentation to increase the effective amount of labeled data for our system. 3 Model Architecture A simple…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 3 of 28 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin

> Page 3 of the source PDF, verbatim as extracted. Canonical document: [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md)

bootstrapping larger datasets and data augmentation to increase the effective amount of labeled data for our system.

## 3 Model Architecture

A simple multi-layer model with a single recurrent layer cannot exploit thousands of hours of labelled speech. In order to learn from datasets this large, we increase the model capacity via depth. We explore architectures with up to 11 layers including many bidirectional recurrent layers and convolutional layers. These models have nearly 8 times the amount of computation per data example as the models in Deep Speech 1 making fast optimization and computation critical. In order to optimize these models successfully, we use Batch Normalization for RNNs and a novel optimization curriculum we call SortaGrad. We also exploit long strides between RNN inputs to reduce computation per example by a factor of 3. This is helpful for both training and evaluation, though requires some modifications in order to work well with CTC. Finally, though many of our research results make use of bidirectional recurrent layers, we find that excellent models exist using only unidirectional recurrent layers—a feature that makes such models much easier to deploy. Taken together these features allow us to tractably optimize deep RNNs and improve performance by more than 40% in both English and Mandarin error rates over the smaller baseline models.

## 3.1 Preliminaries

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

---

[previous page](page-002.md) · [next page](page-004.md) · [all pages](index.md)
