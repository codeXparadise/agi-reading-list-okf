---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/15-deep-speech-2.md
source: ../../papers/15-deep-speech-2.md
paper_title: "Deep Speech 2: End-to-End Speech Recognition in English and Mandarin"
sequence: 15
page: 17
pages: [17]
page_of: 28
topics: ["../../topics/speech-recognition.md", "../../topics/recurrent-neural-networks.md"]
description: "Model size Model type Regular Dev Noisy Dev 18 × 106 GRU 10.59 21.38 38 × 106 GRU 9.06 17.07 70 × 106 GRU 8.54 15.98 70 × 106 RNN 8.44 15.09 100 ×…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 17 of 28 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin

> Page 17 of the source PDF, verbatim as extracted. Canonical document: [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md)

Model size Model type Regular Dev Noisy Dev

18 × 106 GRU 10.59 21.38 38 × 106 GRU 9.06 17.07 70 × 106 GRU 8.54 15.98 70 × 106 RNN 8.44 15.09 100 × 106 GRU 7.78 14.17 100 × 106 RNN 7.73 13.06

Table 11: Comparing the effect of model size on the WER of the English speech system on both the regular and noisy development sets. We vary the number of hidden units in all but the convolutional layers. The GRU model has 3 layers of bidirectional GRUs with 1 layer of 2D-invariant convolution. The RNN model has 7 layers of bidirectional simple recurrence with 3 layers of 2D-invariant convolution. Both models output bigrams with a temporal stride of 3. All models contain approximately 35 million parameters and are trained with BatchNorm and SortaGrad.

Test set DS1 DS2

Baidu Test 24.01 13.59

Table 12: Comparison of DS1 and DS2 WER on an internal test set of 3,300 examples. The test set contains a wide variety of speech including accents, low signal-to-noise speech, spontaneous and conversational speech.

simple RNN. In fact, for the 100 million parameter networks the simple RNN performs better than the GRU network and is faster to train despite the 2 extra layers of convolution.

Table 11 shows that the performance of the system improves consistently up to 100 million parameters. All further English DS2 results are reported with this same 100 million parameter RNN model since it achieves the lowest generalization errors.

Table 12 shows that the 100 million parameter RNN model (DS2) gives a 43.4% relative improvement over the 5-layer model with 1 recurrent layer (DS1) on an internal Baidu dataset of 3,300 utterances that contains a wide variety of speech including challenging accents, low signal-to-noise ratios from far-field or background noise, spontaneous and conversational speech.

## 6.1.2 Read Speech

Read speech with high signal-to-noise ratio is arguably the easiest large vocabulary for a continuous speech recognition task. We benchmark our system on two test sets from the Wall Street Journal (WSJ) corpus of read news articles. These are available in the LDC catalog as LDC94S13B and LDC93S6B. We also take advantage of the recently developed LibriSpeech corpus constructed using audio books from the LibriVox project \[46\].

Table 13 shows that the DS2 system outperforms humans in 3 out of the 4 test sets and is competitive on the fourth. Given this result, we suspect that there is little room for a generic speech system to further improve on clean read speech without further domain adaptation.

Read Speech

Test set DS1 DS2 Human

WSJ eval’92 4.94 3.60 5.03 WSJ eval’93 6.94 4.98 8.08 LibriSpeech test-clean 7.89 5.33 5.83 LibriSpeech test-other 21.74 13.25 12.69

Table 13: Comparison of WER for two speech systems and human level performance on read speech.

---

[previous page](page-016.md) · [next page](page-018.md) · [all pages](index.md)
