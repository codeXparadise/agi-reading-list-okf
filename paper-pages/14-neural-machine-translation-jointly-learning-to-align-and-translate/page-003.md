---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md
source: ../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md
paper_title: Neural Machine Translation by Jointly Learning to Align and Translate
sequence: 14
page: 3
pages: [3]
page_of: 15
topics: ["../../topics/attention.md", "../../topics/machine-translation.md", "../../topics/sequence-to-sequence.md"]
description: "the alignment is not considered to be a latent variable. Instead, the alignment model directly computes a soft alignment, which allows the gradient…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 3 of 15 - Neural Machine Translation by Jointly Learning to Align and Translate

> Page 3 of the source PDF, verbatim as extracted. Canonical document: [14 - Neural Machine Translation by Jointly Learning to Align and Translate](../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md)

the alignment is not considered to be a latent variable. Instead, the alignment model directly computes a soft alignment, which allows the gradient of the cost function to be backpropagated through. This gradient can be used to train the alignment model as well as the whole translation model jointly.

We can understand the approach of taking a weighted sum of all the annotations as computing an expected annotation, where the expectation is over possible alignments. Let αij be a probability that the target word yi is aligned to, or translated from, a source word xj. Then, the i-th context vector ci is the expected annotation over all the annotations with probabilities αij.

The probability αij, or its associated energy eij, reflects the importance of the annotation hj with respect to the previous hidden state si−1 in deciding the next state si and generating yi. Intuitively, this implements a mechanism of attention in the decoder. The decoder decides parts of the source sentence to pay attention to. By letting the decoder have an attention mechanism, we relieve the encoder from the burden of having to encode all information in the source sentence into a fixedlength vector. With this new approach the information can be spread throughout the sequence of annotations, which can be selectively retrieved by the decoder accordingly.

3.2 ENCODER: BIDIRECTIONAL RNN FOR ANNOTATING SEQUENCES

The usual RNN, described in Eq. (1), reads an input sequence x in order starting from the first symbol x1 to the last one xTx. However, in the proposed scheme, we would like the annotation of each word to summarize not only the preceding words, but also the following words. Hence, we propose to use a bidirectional RNN (BiRNN, Schuster and Paliwal, 1997), which has been successfully used recently in speech recognition (see, e.g., Graves et al., 2013).

A BiRNN consists of forward and backward RNN’s. The forward RNN −→f reads the input sequence as it is ordered (from x1 to xTx) and calculates a sequence of forward hidden states (−→h 1, · · · , −→h Tx). The backward RNN ←−f reads the sequence in the reverse order (from xTx to x1), resulting in a sequence of backward hidden states (←−h 1, · · · , ←−h Tx).

We obtain an annotation for each word xj by concatenating the forward hidden state −→h j and the

backward one ←−h j, i.e., hj =

h−→h ⊤

j ; ←−h ⊤

i⊤

. In this way, the annotation hj contains the summaries of both the preceding words and the following words. Due to the tendency of RNNs to better represent recent inputs, the annotation hj will be focused on the words around xj. This sequence of annotations is used by the decoder and the alignment model later to compute the context vector (Eqs. (5)–(6)).

j

See Fig. 1 for the graphical illustration of the proposed model.

## 4 EXPERIMENT SETTINGS

We evaluate the proposed approach on the task of English-to-French translation. We use the bilingual, parallel corpora provided by ACL WMT ’14.3 As a comparison, we also report the performance of an RNN Encoder–Decoder which was proposed recently by Cho et al. (2014a). We use the same training procedures and the same dataset for both models.4

4.1 DATASET

WMT ’14 contains the following English-French parallel corpora: Europarl (61M words), news commentary (5.5M), UN (421M) and two crawled corpora of 90M and 272.5M words respectively, totaling 850M words. Following the procedure described in Cho et al. (2014a), we reduce the size of the combined corpus to have 348M words using the data selection method by Axelrod et al. (2011).5 We do not use any monolingual data other than the mentioned parallel corpora, although it may be possible to use a much larger monolingual corpus to pretrain an encoder. We concatenate news-test-

3 http://www.statmt.org/wmt14/translation-task.html 4 Implementations are available at https://github.com/lisa-groundhog/GroundHog. 5 Available online at http://www-lium.univ-lemans.fr/˜schwenk/cslm\_joint\_paper/.

---

[previous page](page-002.md) · [next page](page-004.md) · [all pages](index.md)
