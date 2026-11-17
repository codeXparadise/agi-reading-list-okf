---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/15-deep-speech-2.md
source: ../../papers/15-deep-speech-2.md
paper_title: "Deep Speech 2: End-to-End Speech Recognition in English and Mandarin"
sequence: 15
page: 8
pages: [8]
page_of: 28
topics: ["../../topics/speech-recognition.md", "../../topics/recurrent-neural-networks.md"]
description: "Architecture Channels Filter dimension Stride Regular Dev Noisy Dev 1-layer 1D 1280 11 2 9.52 19.36 2-layer 1D 640, 640 5, 5 1, 2 9.67 19.21 3-layer…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 8 of 28 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin

> Page 8 of the source PDF, verbatim as extracted. Canonical document: [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md)

Architecture Channels Filter dimension Stride Regular Dev Noisy Dev

1-layer 1D 1280 11 2 9.52 19.36 2-layer 1D 640, 640 5, 5 1, 2 9.67 19.21 3-layer 1D 512, 512, 512 5, 5, 5 1, 1, 2 9.20 20.22 1-layer 2D 32 41x11 2x2 8.94 16.22 2-layer 2D 32, 32 41x11, 21x11 2x2, 2x1 9.06 15.71 3-layer 2D 32, 32, 96 41x11, 21x11, 21x11 2x2, 2x1, 2x1 8.61 14.74

Table 4: Comparison of WER for various arrangements of convolutional layers. In all cases, the convolutions are followed by 7 recurrent layers and 1 fully connected layer. For 2D-invariant convolutions the first dimension is frequency and the second dimension is time. All models have BatchNorm, SortaGrad, and 35 million parameters.

tween words. As we discuss in Section 3.8, even simple RNNs are able to implicitly learn a language model due to the large amount of training data. Interestingly, the GRU networks with 5 or more recurrent layers do not significantly improve performance. We attribute this to the thinning from 1728 hidden units per layer for 1 recurrent layer to 768 hidden units per layer for 7 recurrent layers, to keep the total number of parameters constant.

The GRU networks outperform the simple RNNs in Table 3. However, in later results (Section 6) we find that as we scale up the model size, for a fixed computational budget the simple RNN networks perform slightly better. Given this, most of the remaining experiments use the simple RNN layers rather than the GRUs.

## 3.5 Frequency Convolutions

Temporal convolution is commonly used in speech recognition to efficiently model temporal translation invariance for variable length utterances. This type of convolution was first proposed for neural networks in speech more than 25 years ago \[67\]. Many neural network speech models have a first layer that processes input frames with some context window \[16, 66\]. This can be viewed as a temporal convolution with a stride of one.

Additionally, sub-sampling is essential to make recurrent neural networks computationally tractable with high sample-rate audio. The DS1 system accomplished this through the use of a spectrogram as input and temporal convolution in the first layer with a stride parameter to reduce the number of time-steps \[26\].

Convolutions in frequency and time domains, when applied to the spectral input features prior to any other processing, can slightly improve ASR performance \[1, 53, 60\]. Convolution in frequency attempts to model spectral variance due to speaker variability more concisely than what is possible with large fully connected networks. Since spectral ordering of features is removed by fullyconnected and recurrent layers, frequency convolutions work better as the first layers of the network.

We experiment with adding between one and three layers of convolution. These are both in the timeand-frequency domain (2D invariance) and in the time-only domain (1D invariance). In all cases we use a same convolution, preserving the number of input features in both frequency and time. In some cases, we specify a stride across either dimension which reduces the size of the output. We do not explicitly control for the number of parameters, since convolutional layers add a small fraction of parameters to our networks. All networks shown in Table 4 have about 35 million parameters.

We report results on two datasets—a development set of 2048 utterances (“Regular Dev”) and a much noisier dataset of 2048 utterances (“Noisy Dev”) randomly sampled from the CHiME 2015 development datasets \[4\]. We find that multiple layers of 1D-invariant convolutions provides a very small benefit. The 2D-invariant convolutions improve results substantially on noisy data, while providing a small benefit on clean data. The change from one layer of 1D-invariant convolution to three layers of 2D-invariant convolution improves WER by 23.9% on the noisy development set.

---

[previous page](page-007.md) · [next page](page-009.md) · [all pages](index.md)
