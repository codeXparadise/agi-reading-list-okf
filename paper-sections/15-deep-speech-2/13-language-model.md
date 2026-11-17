---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/15-deep-speech-2.md
source: ../../papers/15-deep-speech-2.md
paper_title: "Deep Speech 2: End-to-End Speech Recognition in English and Mandarin"
sequence: 15
section: 3.8 Language Model
section_role: other
section_index: 13
pages: [10, 11]
topics: ["../../topics/speech-recognition.md", "../../topics/recurrent-neural-networks.md"]
description: "We train our RNN Models over millions of unique utterances, which enables the network to learn a powerful implicit language model. Our best models…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.8 Language Model

> Section 13 of 38 from [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md) · `other` · pages 10-11

We train our RNN Models over millions of unique utterances, which enables the network to learn a powerful implicit language model. Our best models are quite adept at spelling, without any external language constraints. Further, in our development datasets we find many cases where our models can implicitly disambiguate homophones—for example, “he expects the Japanese agent to sell it for two hundred seventy five thousand dollars”. Nevertheless, the labeled training data is small compared to the size of unlabeled text corpora that are available. Thus we find that WER improves when we supplement our system with a language model trained from external text.

We use an n-gram language model since they scale well to large amounts of unlabeled text \[26\]. For English, our language model is a Kneser-Ney smoothed 5-gram model with pruning that is trained using the KenLM toolkit \[28\] on cleaned text from the Common Crawl Repository3. The vocabulary is the most frequently used 400,000 words from 250 million lines of text, which produces a language model with about 850 million n-grams. For Mandarin, the language model is a KneserNey smoothed character level 5-gram model with pruning that is trained on an internal text corpus of 8 billion lines of text. This produces a language model with about 2 billion n-grams.

During inference we search for the transcription y that maximizes Q(y) shown in Equation 12. This is a linear combination of log probabilities from the CTC trained network and language model, along with a word insertion term \[26\].

Q(y) = log(pctc(y|x)) + α log(plm(y)) + β word\_count(y) (12)

The weight α controls the relative contributions of the language model and the CTC network. The weight β encourages more words in the transcription. These parameters are tuned on a development set. We use a beam search to find the optimal transcription \[27\].

3http://commoncrawl.org

Language Architecture Dev no LM Dev LM

English 5-layer, 1 RNN 27.79 14.39 English 9-layer, 7 RNN 14.93 9.52 Mandarin 5-layer, 1 RNN 9.80 7.13 Mandarin 9-layer, 7 RNN 7.55 5.81

Table 6: Comparison of WER for English and CER for Mandarin with and without a language model. These are simple RNN models with only one layer of 1D invariant convolution.

Table 6 shows that an external language model helps both English and Mandarin speech systems. The relative improvement given by the language model drops from 48% to 36% in English and 27% to 23% in Mandarin, as we go from a model with 5 layers and 1 recurrent layer to a model with 9 layers and 7 recurrent layers. We hypothesize that the network builds a stronger implicit language model with more recurrent layers.

The relative performance improvement from a language model is higher in English than in Mandarin. We attribute this to the fact that a Chinese character represents a larger block of information than an English character. For example, if we output directly to syllables or words in English, the model would make fewer spelling mistakes and the language model would likely help less.

---

Full document: [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](../../papers/15-deep-speech-2.md) · Page-level evidence: [paper-pages/15-deep-speech-2](../../paper-pages/15-deep-speech-2/index.md)
