---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/13-order-matters-sequence-to-sequence-for-sets.md
source: ../../papers/13-order-matters-sequence-to-sequence-for-sets.md
paper_title: "Order Matters: Sequence to Sequence for Sets"
sequence: 13
section: 1 INTRODUCTION
section_role: introduction
section_index: 3
pages: [1]
topics: ["../../topics/sequence-to-sequence.md", "../../topics/attention.md"]
description: "Deep architectures have shown in the last few years that they often yield state-of-the-art performance on several tasks, ranging from image…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 1 INTRODUCTION

> Section 3 of 9 from [13 - Order Matters: Sequence to Sequence for Sets](../../papers/13-order-matters-sequence-to-sequence-for-sets.md) · `introduction` · pages 1-1

Deep architectures have shown in the last few years that they often yield state-of-the-art performance on several tasks, ranging from image classification (Ioffe & Szegedy, 2015) to speech recognition (Hinton et al., 2012). More recently, recurrent neural networks (RNNs) and variants such as the Long Short Term Memory network (LSTMs) proposed by Hochreiter & Schmidhuber (1997) have shown similar impressive performance on several inherently sequential tasks. Such examples range from machine translation (Sutskever et al., 2014; Bahdanau et al., 2015a), to image captioning (Vinyals et al., 2015c; Mao et al., 2015; Donahue et al., 2015), speech recognition (Chan et al., 2015; Bahdanau et al., 2015b), constituency parsing (Vinyals et al., 2015b) and learning to compute (Zaremba & Sutskever, 2014; Vinyals et al., 2015a). These approaches all follow a simple architecture, dubbed sequence-to-sequence (seq2seq), where the input is read completely using an encoder, which is either an LSTM when the input is a sequence, or a convolutional network for images. The final state of the encoder is then fed to a decoder LSTM whose purpose is to produce the target sequence, one token at a time.

When the data is naturally organized as a sequence, the sequence-to-sequence framework is well suited. For example, the chain rule is used to decompose the joint probability of sequences of words, and can be implemented by an LSTM without making any conditional independence assumption. But how should we represent data, either inputs or outputs, for problems where an obvious order cannot be determined? For instance, how should we encode a set of numbers when the task is to sort them? Alternatively, how should we output a set of detected objects in an image when there is no specific known order among them? Does the a priori choice of ordering of the data to be presented to the model matter?

The purpose of this paper is two-fold. First, we show that even when no natural order is known among input or output objects, there might still be one that yields better performance, hence, order matters. Second, we propose two approaches to consider sets either as inputs and/or outputs in our models and evaluate how they perform on various artificial and real datasets.

---

Full document: [13 - Order Matters: Sequence to Sequence for Sets](../../papers/13-order-matters-sequence-to-sequence-for-sets.md) · Page-level evidence: [paper-pages/13-order-matters-sequence-to-sequence-for-sets](../../paper-pages/13-order-matters-sequence-to-sequence-for-sets/index.md)
