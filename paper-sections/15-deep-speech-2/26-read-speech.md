---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/15-deep-speech-2.md
source: ../../papers/15-deep-speech-2.md
paper_title: "Deep Speech 2: End-to-End Speech Recognition in English and Mandarin"
sequence: 15
section: 6.1.2 Read Speech
section_role: other
section_index: 26
pages: [17, 18]
topics: ["../../topics/speech-recognition.md", "../../topics/recurrent-neural-networks.md"]
description: "Read speech with high signal-to-noise ratio is arguably the easiest large vocabulary for a continuous speech recognition task. We benchmark our…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 6.1.2 Read Speech

> Section 26 of 38 from [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md) · `other` · pages 17-18

Read speech with high signal-to-noise ratio is arguably the easiest large vocabulary for a continuous speech recognition task. We benchmark our system on two test sets from the Wall Street Journal (WSJ) corpus of read news articles. These are available in the LDC catalog as LDC94S13B and LDC93S6B. We also take advantage of the recently developed LibriSpeech corpus constructed using audio books from the LibriVox project \[46\].

Table 13 shows that the DS2 system outperforms humans in 3 out of the 4 test sets and is competitive on the fourth. Given this result, we suspect that there is little room for a generic speech system to further improve on clean read speech without further domain adaptation.

Read Speech

Test set DS1 DS2 Human

WSJ eval’92 4.94 3.60 5.03 WSJ eval’93 6.94 4.98 8.08 LibriSpeech test-clean 7.89 5.33 5.83 LibriSpeech test-other 21.74 13.25 12.69

Table 13: Comparison of WER for two speech systems and human level performance on read speech.

Accented Speech

Test set DS1 DS2 Human

VoxForge American-Canadian 15.01 7.55 4.85 VoxForge Commonwealth 28.46 13.56 8.15 VoxForge European 31.20 17.55 12.76 VoxForge Indian 45.35 22.44 22.15

Table 14: Comparing WER of the DS1 system to the DS2 system on accented speech.

Noisy Speech

Test set DS1 DS2 Human

CHiME eval clean 6.30 3.34 3.46 CHiME eval real 67.94 21.79 11.84 CHiME eval sim 80.27 45.05 31.33

Table 15: Comparison of DS1 and DS2 system on noisy speech. “CHiME eval clean” is a noise-free baseline. The “CHiME eval real” dataset is collected in real noisy environments and the “CHiME eval sim” dataset has similar noise synthetically added to clean speech. Note that we use only one of the six channels to test each utterance.

---

Full document: [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md) · Page-level evidence: [paper-pages/15-deep-speech-2](../../paper-pages/15-deep-speech-2/index.md)
