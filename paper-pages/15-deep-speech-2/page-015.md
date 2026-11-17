---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/15-deep-speech-2.md
source: ../../papers/15-deep-speech-2.md
paper_title: "Deep Speech 2: End-to-End Speech Recognition in English and Mandarin"
sequence: 15
page: 15
pages: [15]
page_of: 28
topics: ["../../topics/speech-recognition.md", "../../topics/recurrent-neural-networks.md"]
description: "fixed delay and this can happen with unidirectional RNNs [54]. However, we found that CTC produces an accurate alignment when trained with a…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 15 of 28 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin

> Page 15 of the source PDF, verbatim as extracted. Canonical document: [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md)

fixed delay and this can happen with unidirectional RNNs \[54\]. However, we found that CTC produces an accurate alignment when trained with a bidirectional RNN.

Following the alignment is a segmentation step that splices the audio and the corresponding aligned transcription whenever it encounters a long series of consecutive blank labels occurs, since this usually denotes a stretch of silence. By tuning the number of consecutive blanks, we can tune the length of the utterances generated. For the English speech data, we also require a space token to be within the stretch of blanks in order to segment only on word boundaries. We tune the segmentation to generate utterances that are on average 7 seconds long.

The final step in the pipeline removes erroneous examples that arise from a failed alignment. We crowd source the ground truth transcriptions for several thousand examples. The word level edit distance between the ground truth and the aligned transcription is used to produce a good or bad label. The threshold for the word level edit distance is chosen such that the resulting WER of the good portion of the development set is less than 5%. We then train a linear classifier to accurately predict bad examples given the input features generated from the speech recognizer. We find the following features useful: the raw CTC cost, the CTC cost normalized by the sequence length, the CTC cost normalized by the transcript length, the ratio of the sequence length to the transcript length, the number of words in the transcription and the number of characters in the transcription. For the English dataset, we find that the filtering pipeline reduces the WER from 17% to 5% while retaining more than 50% of the examples.

## 5.2 Data Augmentation

We augment our training data by adding noise to increase the effective size of our training data and to improve our robustness to noisy speech \[26\]. Although the training data contains some intrinsic noise, we can increase the quantity and variety of noise through augmentation. Too much noise augmentation tends to make optimization difficult and can lead to worse results, and too little noise augmentation makes the system less robust to low signal-to-noise speech. We find that a good balance is to add noise to 40% of the utterances that are chosen at random. The noise source consists of several thousand hours of randomly selected audio clips combined to produce hundreds of hours of noise.

## 5.3 Scaling Data

Our English and Mandarin corpora are substantially larger than those commonly reported in speech recognition literature. In Table 10, we show the effect of increasing the amount of labeled training data on WER. This is done by randomly sampling the full dataset before training. For each dataset, the model was trained for up to 20 epochs though usually early-stopped based on the error on a held out development set. We note that the WER decreases with a power law for both the regular and noisy development sets. The WER decreases by ∼40% relative for each factor of 10 increase in training set size. We also observe a consistent gap in WER (∼60% relative) between the regular and noisy datasets, implying that more data benefits both cases equally.

This implies that a speech system will continue to improve with more labeled training data. We hypothesize that equally as important as increasing raw number of hours is increasing the number of speech contexts that are captured in the dataset. A context can be any property that makes speech unique including different speakers, background noise, environment, and microphone hardware. While we do not have the labels needed to validate this claim, we suspect that measuring WER as a function of speakers in the dataset would lead to much larger relative gains than simple random sampling.

## 6 Results

To better assess the real-world applicability of our speech system, we evaluate on a wide range of test sets. We use several publicly available benchmarks and several test sets collected internally. Together these test sets represent a wide range of challenging speech environments including low signal-to-noise ratios (noisy and far-field), accented, read, spontaneous and conversational speech.

---

[previous page](page-014.md) · [next page](page-016.md) · [all pages](index.md)
