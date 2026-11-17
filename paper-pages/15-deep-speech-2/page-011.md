---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/15-deep-speech-2.md
source: ../../papers/15-deep-speech-2.md
paper_title: "Deep Speech 2: End-to-End Speech Recognition in English and Mandarin"
sequence: 15
page: 11
pages: [11]
page_of: 28
topics: ["../../topics/speech-recognition.md", "../../topics/recurrent-neural-networks.md"]
description: "Language Architecture Dev no LM Dev LM English 5-layer, 1 RNN 27.79 14.39 English 9-layer, 7 RNN 14.93 9.52 Mandarin 5-layer, 1 RNN 9.80 7.13…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 11 of 28 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin

> Page 11 of the source PDF, verbatim as extracted. Canonical document: [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md)

Language Architecture Dev no LM Dev LM

English 5-layer, 1 RNN 27.79 14.39 English 9-layer, 7 RNN 14.93 9.52 Mandarin 5-layer, 1 RNN 9.80 7.13 Mandarin 9-layer, 7 RNN 7.55 5.81

Table 6: Comparison of WER for English and CER for Mandarin with and without a language model. These are simple RNN models with only one layer of 1D invariant convolution.

Table 6 shows that an external language model helps both English and Mandarin speech systems. The relative improvement given by the language model drops from 48% to 36% in English and 27% to 23% in Mandarin, as we go from a model with 5 layers and 1 recurrent layer to a model with 9 layers and 7 recurrent layers. We hypothesize that the network builds a stronger implicit language model with more recurrent layers.

The relative performance improvement from a language model is higher in English than in Mandarin. We attribute this to the fact that a Chinese character represents a larger block of information than an English character. For example, if we output directly to syllables or words in English, the model would make fewer spelling mistakes and the language model would likely help less.

## 3.9 Adaptation to Mandarin

The techniques that we have described so far can be used to build an end-to-end Mandarin speech recognition system that outputs Chinese characters directly. This precludes the need to construct a pronunciation model, which is often a fairly involved component for porting speech systems to other languages \[59\]. Direct output to characters also precludes the need to explicitly model language specific pronunciation features. For example we do not need to model Mandarin tones explicitly, as some speech systems must do \[59, 45\].

The only architectural changes we make to our networks are due to the characteristics of the Chinese character set. Firstly, the output layer of the network outputs about 6000 characters, which includes the Roman alphabet, since hybrid Chinese-English transcripts are common. We incur an out of vocabulary error at evaluation time if a character is not contained in this set. This is not a major concern, as our test set has only 0.74% out of vocab characters.

We use a character level language model in Mandarin as words are not usually segmented in text. The word insertion term of Equation 12 becomes a character insertion term. In addition, we find that the performance of the beam search during decoding levels off at a smaller beam size. This allows us to use a beam size of 200 with a negligible degradation in CER. In Section 6.2, we show that our Mandarin speech models show roughly the same improvements to architectural changes as our English speech models.

## 4 System Optimizations

Our networks have tens of millions of parameters, and the training algorithm takes tens of singleprecision exaFLOPs to converge. Since our ability to evaluate hypotheses about our data and models depends on the ability to train models quickly, we built a highly optimized training system. This system has two main components—a deep learning library written in C++, along with a highperformance linear algebra library written in both CUDA and C++. Our optimized software, running on dense compute nodes with 8 Titan X GPUs per node, allows us to sustain 24 single-precision teraFLOP/second when training a single model on one node. This is 45% of the theoretical peak computational throughput of each node. We also can scale to multiple nodes, as outlined in the next subsection.

## 4.1 Scalability and Data-Parallelism

We use the standard technique of data-parallelism to train on multiple GPUs using synchronous SGD. Our most common configuration uses a minibatch of 512 on 8 GPUs. Our training pipeline

---

[previous page](page-010.md) · [next page](page-012.md) · [all pages](index.md)
