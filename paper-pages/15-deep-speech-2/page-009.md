---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/15-deep-speech-2.md
source: ../../papers/15-deep-speech-2.md
paper_title: "Deep Speech 2: End-to-End Speech Recognition in English and Mandarin"
sequence: 15
page: 9
pages: [9]
page_of: 28
topics: ["../../topics/speech-recognition.md", "../../topics/recurrent-neural-networks.md"]
description: "Dev no LM Dev LM Stride Unigrams Bigrams Unigrams Bigrams 2 14.93 14.56 9.52 9.66 3 15.01 15.60 9.65 10.06 4 18.86 14.84 11.92 9.93 Table 5:…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 9 of 28 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin

> Page 9 of the source PDF, verbatim as extracted. Canonical document: [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md)

Dev no LM Dev LM

Stride Unigrams Bigrams Unigrams Bigrams

2 14.93 14.56 9.52 9.66 3 15.01 15.60 9.65 10.06 4 18.86 14.84 11.92 9.93

Table 5: Comparison of WER with different amounts of striding for unigram and bigram outputs on a model with 1 layer of 1D-invariant convolution, 7 recurrent layers, and 1 fully connected layer. All models have BatchNorm, SortaGrad, and 35 million parameters. The models are compared on a development set with and without the use of a 5-gram language model.

## 3.6 Striding

In the convolutional layers, we apply a longer stride and wider context to speed up training as fewer time-steps are required to model a given utterance. Downsampling the input sound (through FFT and convolutional striding) reduces the number of time-steps and computation required in the following layers, but at the expense of reduced performance.

In our Mandarin models, we employ striding in the straightforward way. However, in English, striding can reduce accuracy simply because the output of our network requires at least one timestep per output character, and the number of characters in English speech per time-step is high enough to cause problems when striding2. To overcome this, we can enrich the English alphabet with symbols representing alternate labellings like whole words, syllables or non-overlapping ngrams. In practice, we use non-overlapping bi-graphemes or bigrams, since these are simple to construct, unlike syllables, and there are few of them compared to alternatives such as whole words. We transform unigram labels into bigram labels through a simple isomorphism.

Non-overlapping bigrams shorten the length of the output transcription and thus allow for a decrease in the length of the unrolled RNN. The sentence the cat sat with non-overlapping bigrams is segmented as \[th, e, space, ca, t, space, sa, t\]. Notice that for words with odd number of characters, the last character becomes an unigram and space is treated as an unigram as well. This isomorphism ensures that the same words are always composed of the same bigram and unigram tokens. The output set of bigrams consists of all bigrams that occur in the training set.

In Table 5 we show results for both the bigram and unigram systems for various levels of striding, with or without a language model. We observe that bigrams allow for larger strides without any sacrifice in in the word error rate. This allows us to reduce the number of time-steps of the unrolled RNN benefiting both computation and memory usage.

## 3.7 Row Convolution and Unidirectional Models

Bidirectional RNN models are challenging to deploy in an online, low-latency setting, because they are built to operate on an entire sample, and so it is not possible to perform the transcription process as the utterance streams from the user. We have found an unidirectional architecture that performs as well as our bidirectional models. This allows us to use unidirectional, forward-only RNN layers in our deployment system.

To accomplish this, we employ a special layer that we call row convolution, shown in Figure 3. The intuition behind this layer is that we only need a small portion of future information to make an accurate prediction at the current time-step. Suppose at time-step t, we use a future context of τ steps. We now have a feature matrix ht:t+τ = \[ht, ht+1, ..., ht+τ\] of size d × (τ + 1). We define a parameter matrix W of the same size as ht:t+τ. The activations rt for the new layer at time-step t are

2Chinese characters are more similar to English syllables than English characters. This is reflected in our training data, where there are on average 14.1 characters/s in English, while only 3.3 characters/s in Mandarin. Conversely, the Shannon entropy per character as calculated from occurrence in the training set, is less in English due to the smaller character set—4.9 bits/char compared to 12.6 bits/char in Mandarin. This implies that spoken Mandarin has a lower temporal entropy density, ∼41 bits/s compared to ∼58 bits/s, and can thus more easily be temporally compressed without losing character information.

---

[previous page](page-008.md) · [next page](page-010.md) · [all pages](index.md)
