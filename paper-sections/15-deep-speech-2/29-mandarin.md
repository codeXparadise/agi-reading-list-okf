---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/15-deep-speech-2.md
source: ../../papers/15-deep-speech-2.md
paper_title: "Deep Speech 2: End-to-End Speech Recognition in English and Mandarin"
sequence: 15
section: 6.2 Mandarin
section_role: other
section_index: 29
pages: [18, 19]
topics: ["../../topics/speech-recognition.md", "../../topics/recurrent-neural-networks.md"]
description: "In Table 16 we compare several architectures trained on the Mandarin Chinese speech, on a development set of 2000 utterances as well as a test set of…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 6.2 Mandarin

> Section 29 of 38 from [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md) · `other` · pages 18-19

In Table 16 we compare several architectures trained on the Mandarin Chinese speech, on a development set of 2000 utterances as well as a test set of 1882 examples of noisy speech. This development set was also used to tune the decoding parameters We see that the deepest model with 2D-invariant

convolution and BatchNorm outperforms the shallow RNN by 48% relative, thus continuing the trend that we saw with the English system—multiple layers of bidirectional recurrence improves performance substantially.

Architecture Dev Test

5-layer, 1 RNN 7.13 15.41 5-layer, 3 RNN 6.49 11.85 5-layer, 3 RNN + BatchNorm 6.22 9.39 9-layer, 7 RNN + BatchNorm + 2D conv 5.81 7.93

Table 16: Comparison of the improvements in DeepSpeech with architectural improvements. The development and test sets are Baidu internal corpora. All the models in the table have about 80 million parameters each

We find that our best Mandarin Chinese speech system transcribes short voice-query like utterances better than a typical Mandarin Chinese speaker. To benchmark against humans we ran a test with 100 randomly selected utterances and had a group of 5 humans label all of them together. The group of humans had an error rate of 4.0% as compared to the speech systems performance of 3.7%. We also compared a single human transcriber to the speech system on 250 randomly selected utterances. In this case the speech system performs much better: 9.7% for the human compared to 5.7% for the speech model.

---

Full document: [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md) · Page-level evidence: [paper-pages/15-deep-speech-2](../../paper-pages/15-deep-speech-2/index.md)
