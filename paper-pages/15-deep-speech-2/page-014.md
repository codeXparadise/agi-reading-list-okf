---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/15-deep-speech-2.md
source: ../../papers/15-deep-speech-2.md
paper_title: "Deep Speech 2: End-to-End Speech Recognition in English and Mandarin"
sequence: 15
page: 14
pages: [14]
page_of: 28
topics: ["../../topics/speech-recognition.md", "../../topics/recurrent-neural-networks.md"]
description: "Dataset Speech Type Hours WSJ read 80 Switchboard conversational 300 Fisher conversational 2000 LibriSpeech read 960 Baidu read 5000 Baidu mixed 3600…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 14 of 28 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin

> Page 14 of the source PDF, verbatim as extracted. Canonical document: [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md)

Dataset Speech Type Hours

WSJ read 80 Switchboard conversational 300 Fisher conversational 2000 LibriSpeech read 960 Baidu read 5000 Baidu mixed 3600

Total 11940

Table 9: Summary of the datasets used to train DS2 in English. The Wall Street Journal (WSJ), Switchboard and Fisher \[13\] corpora are all published by the Linguistic Data Consortium. The LibriSpeech dataset \[46\] is available free on-line. The other datasets are internal Baidu corpora.

Most of the memory required for training deep recurrent networks is used to store activations through each layer for use by back propagation, not to store the parameters of the network. For example, storing the weights for a 70M parameter network with 9 layers requires approximately 280 MB of memory, but storing the activations for a batch of 64, seven-second utterances requires 1.5 GB of memory. TitanX GPUs include 12GB of GDDR5 RAM, and sometimes very deep networks can exceed the GPU memory capacity when processing long utterances. This can happen unpredictably, especially when the distribution of utterance lengths includes outliers, and it is desirable to avoid a catastrophic failure when this occurs. When a requested memory allocation exceeds available GPU memory, we allocate page-locked GPU-memory-mapped CPU memory using cudaMallocHost instead. This memory can be accessed directly by the GPU by forwarding individual memory transactions over PCIe at reduced bandwidth, and it allows a model to continue to make progress even after encountering an outlier.

The combination of fast memory allocation with a fallback mechanism that allows us to slightly overflow available GPU memory in exceptional cases makes the system significantly simpler, more robust, and more efficient.

## 5 Training Data

Large-scale deep learning systems require an abundance of labeled training data. We have collected an extensive training dataset for both English and Mandarin speech models, in addition to augmenting our training with publicly available datasets. In English we use 11,940 hours of labeled speech data containing 8 million utterances summarized in Table 9. For the Mandarin system we use 9,400 hours of labeled audio containing 11 million utterances. The Mandarin speech data consists of internal Baidu corpora, representing a mix of read speech and spontaneous speech, in both standard Mandarin and accented Mandarin.

## 5.1 Dataset Construction

Some of the internal English (3,600 hours) and Mandarin (1,400 hours) datasets were created from raw data captured as long audio clips with noisy transcriptions. The length of these clips ranged from several minutes to more than hour, making it impractical to unroll them in time in the RNN during training. To solve this problem, we developed an alignment, segmentation and filtering pipeline that can generate a training set with shorter utterances and few erroneous transcriptions.

The first step in the pipeline is to use an existing bidirectional RNN model trained with CTC to align the transcription to the frames of audio. For a given audio-transcript pair, (x, y), we find the alignment that maximizes

T Y

ℓ∗= arg max

pctc(ℓt|x; θ). (13)

ℓ∈Align(x,y)

t

This is essentially a Viterbi alignment found using a RNN model trained with CTC. Since Equation 9 integrates over the alignment, the CTC loss function is never explicitly asked to produce an accurate alignment. In principle, CTC could choose to emit all the characters of the transcription after some

---

[previous page](page-013.md) · [next page](page-015.md) · [all pages](index.md)
