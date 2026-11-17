---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/15-deep-speech-2.md
source: ../../papers/15-deep-speech-2.md
paper_title: "Deep Speech 2: End-to-End Speech Recognition in English and Mandarin"
sequence: 15
page: 18
pages: [18]
page_of: 28
topics: ["../../topics/speech-recognition.md", "../../topics/recurrent-neural-networks.md"]
description: "Accented Speech Test set DS1 DS2 Human VoxForge American-Canadian 15.01 7.55 4.85 VoxForge Commonwealth 28.46 13.56 8.15 VoxForge European 31.20…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 18 of 28 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin

> Page 18 of the source PDF, verbatim as extracted. Canonical document: [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md)

Accented Speech

Test set DS1 DS2 Human

VoxForge American-Canadian 15.01 7.55 4.85 VoxForge Commonwealth 28.46 13.56 8.15 VoxForge European 31.20 17.55 12.76 VoxForge Indian 45.35 22.44 22.15

Table 14: Comparing WER of the DS1 system to the DS2 system on accented speech.

Noisy Speech

Test set DS1 DS2 Human

CHiME eval clean 6.30 3.34 3.46 CHiME eval real 67.94 21.79 11.84 CHiME eval sim 80.27 45.05 31.33

Table 15: Comparison of DS1 and DS2 system on noisy speech. “CHiME eval clean” is a noise-free baseline. The “CHiME eval real” dataset is collected in real noisy environments and the “CHiME eval sim” dataset has similar noise synthetically added to clean speech. Note that we use only one of the six channels to test each utterance.

## 6.1.3 Accented Speech

Our source for accented speech is the publicly available VoxForge (http://www.voxforge.org) dataset, which has clean speech read from speakers with many different accents. We group these accents into four categories. The American-Canadian and Indian groups are self-explanatory. The Commonwealth accent denotes speakers with British, Irish, South African, Australian and New Zealand accents. The European group contains speakers with accents from countries in Europe that do not have English as a first language. We construct a test set from the VoxForge data with 1024 examples from each accent group for a total of 4096 examples.

Performance on these test sets is to some extent a measure of the breadth and quality of our training data. Table 14 shows that our performance improved on all the accents when we include more accented training data and use an architecture that can effectively train on that data. However human level performance is still notably better than that of DS2 for all but the Indian accent.

## 6.1.4 Noisy Speech

We test our performance on noisy speech using the publicly available test sets from the recently completed third CHiME challenge \[4\]. This dataset has 1320 utterances from the WSJ test set read in various noisy environments, including a bus, a cafe, a street and a pedestrian area. The CHiME set also includes 1320 utterances with simulated noise from the same environments as well as the control set containing the same utterances delivered by the same speakers in a noise-free environment. Differences between results on the control set and the noisy sets provide a measure of the network’s ability to handle a variety of real and synthetic noise conditions. The CHiME audio has 6 channels and using all of them can provide substantial performance improvements \[69\]. We use a single channel for all our results, since multi-channel audio is not pervasive on most devices. Table 15 shows that DS2 substantially improves upon DS1, however DS2 is worse than human level performance on noisy data. The relative gap between DS2 and human level performance is larger when the data comes from a real noisy environment instead of synthetically adding noise to clean speech.

## 6.2 Mandarin

In Table 16 we compare several architectures trained on the Mandarin Chinese speech, on a development set of 2000 utterances as well as a test set of 1882 examples of noisy speech. This development set was also used to tune the decoding parameters We see that the deepest model with 2D-invariant

---

[previous page](page-017.md) · [next page](page-019.md) · [all pages](index.md)
