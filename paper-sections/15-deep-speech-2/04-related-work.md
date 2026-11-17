---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/15-deep-speech-2.md
source: ../../papers/15-deep-speech-2.md
paper_title: "Deep Speech 2: End-to-End Speech Recognition in English and Mandarin"
sequence: 15
section: 2 Related Work
section_role: background
section_index: 4
pages: [2, 3]
topics: ["../../topics/speech-recognition.md", "../../topics/recurrent-neural-networks.md"]
description: "This work is inspired by previous work in both deep learning and speech recognition. Feed-forward neural network acoustic models were explored more…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2 Related Work

> Section 4 of 38 from [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md) · `background` · pages 2-3

This work is inspired by previous work in both deep learning and speech recognition. Feed-forward neural network acoustic models were explored more than 20 years ago \[7, 50, 19\]. Recurrent neural networks and networks with convolution were also used in speech recognition around the same time \[51, 67\]. More recently DNNs have become a fixture in the ASR pipeline with almost all state of the art speech work containing some form of deep neural network \[42, 29, 17, 16, 43, 58\]. Convolutional networks have also been found beneficial for acoustic models \[1, 53\]. Recurrent neural networks, typically LSTMs, are just beginning to be deployed in state-of-the art recognizers \[24, 25, 55\] and work well together with convolutional layers for the feature extraction \[52\]. Models with both bidirectional \[24\] and unidirectional recurrence have been explored as well.

End-to-end speech recognition is an active area of research, showing compelling results when used to re-score the outputs of a DNN-HMM \[23\] and standalone \[26\]. Two methods are currently used to map variable length audio sequences directly to variable length transcriptions. The RNN encoderdecoder paradigm uses an encoder RNN to map the input to a fixed length vector and a decoder network to expand the fixed length vector into a sequence of output predictions \[11, 62\]. Adding an attentional mechanism to the decoder greatly improves performance of the system, particularly with long inputs or outputs \[2\]. In speech, the RNN encoder-decoder with attention performs well both in predicting phonemes \[12\] or graphemes \[3, 8\].

The other commonly used technique for mapping variable length audio input to variable length output is the CTC loss function \[22\] coupled with an RNN to model temporal information. The CTCRNN model performs well in end-to-end speech recognition with grapheme outputs \[23, 27, 26, 40\]. The CTC-RNN model has also been shown to work well in predicting phonemes \[41, 54\], though a lexicon is still needed in this case. Furthermore it has been necessary to pre-train the CTC-RNN network with a DNN cross-entropy network that is fed frame-wise alignments from a GMM-HMM system \[54\]. In contrast, we train the CTC-RNN networks from scratch without the need of framewise alignments for pre-training.

Exploiting scale in deep learning has been central to the success of the field thus far \[36, 38\]. Training on a single GPU resulted in substantial performance gains \[49\], which were subsequently scaled linearly to two \[36\] or more GPUs \[15\]. We take advantage of work in increasing individual GPU efficiency for low-level deep learning primitives \[9\]. We build on the past work in using modelparallelism \[15\], data-parallelism \[18\] or a combination of the two \[64, 26\] to create a fast and highly scalable system for training deep RNNs in speech recognition.

Data has also been central to the success of end-to-end speech recognition, with over 7000 hours of labeled speech used in Deep Speech 1 (DS1) \[26\]. Data augmentation has been highly effective in improving the performance of deep learning in computer vision \[39, 56, 14\]. This has also been shown to improve speech systems \[21, 26\]. Techniques used for data augmentation in speech range from simple noise addition \[26\] to complex perturbations such as simulating changes to the vocal tract length and rate of speech of the speaker \[31, 35\].

Existing speech systems can also be used to bootstrap new data collection. In one approach, the authors use one speech engine to align and filter a thousand hours of read speech \[46\]. In another approach, a heavy-weight offline speech recognizer is used to generate transcriptions for tens of thousands of hours of speech \[33\]. This is then passed through a filter and used to re-train the recognizer, resulting in significant performance gains. We draw inspiration from these past approaches in

bootstrapping larger datasets and data augmentation to increase the effective amount of labeled data for our system.

---

Full document: [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md) · Page-level evidence: [paper-pages/15-deep-speech-2](../../paper-pages/15-deep-speech-2/index.md)
