---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md
source: ../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md
paper_title: Neural Machine Translation by Jointly Learning to Align and Translate
sequence: 14
section: 3 LEARNING TO ALIGN AND TRANSLATE
section_role: other
section_index: 5
pages: [2, 3]
topics: ["../../topics/attention.md", "../../topics/machine-translation.md", "../../topics/sequence-to-sequence.md"]
description: "In this section, we propose a novel architecture for neural machine translation. The new architecture consists of a bidirectional RNN as an encoder…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3 LEARNING TO ALIGN AND TRANSLATE

> Section 5 of 14 from [14 - Neural Machine Translation by Jointly Learning to Align and Translate](../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md) · `other` · pages 2-3

In this section, we propose a novel architecture for neural machine translation. The new architecture consists of a bidirectional RNN as an encoder (Sec. 3.2) and a decoder that emulates searching through a source sentence during decoding a translation (Sec. 3.1).

3.1 DECODER: GENERAL DESCRIPTION

In a new model architecture, we define each conditional probability in Eq. (2) as:

## yt-1 yt

p(yi|y1, . . . , yi−1, x) = g(yi−1, si, ci), (4)

s t-1 s t

where si is an RNN hidden state for time i, computed by

+ αt,1

si = f(si−1, yi−1, ci).

αt,T

It should be noted that unlike the existing encoder–decoder approach (see Eq. (2)), here the probability is conditioned on a distinct context vector ci for each target word yi.

αt,2 αt,3

h1 h2 h3 hT

The context vector ci depends on a sequence of annotations (h1, · · · , hTx) to which an encoder maps the input sentence. Each annotation hi contains information about the whole input sequence with a strong focus on the parts surrounding the i-th word of the input sequence. We explain in detail how the annotations are computed in the next section.

h1 h2 h3 hT

## x1 x2 x3 xT

Figure 1: The graphical illustration of the proposed model trying to generate the t-th target word yt given a source sentence (x1, x2, . . . , xT ).

The context vector ci is, then, computed as a weighted sum of these annotations hi:

Tx X

ci =

αijhj. (5)

j=1

The weight αij of each annotation hj is computed by

αij = exp (eij) PTx

, (6)

k=1 exp (eik)

where

eij = a(si−1, hj) is an alignment model which scores how well the inputs around position j and the output at position i match. The score is based on the RNN hidden state si−1 (just before emitting yi, Eq. (4)) and the j-th annotation hj of the input sentence.

We parametrize the alignment model a as a feedforward neural network which is jointly trained with all the other components of the proposed system. Note that unlike in traditional machine translation,

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

---

Full document: [14 - Neural Machine Translation by Jointly Learning to Align and Translate](../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md) · Page-level evidence: [paper-pages/14-neural-machine-translation-jointly-learning-to-align-and-translate](../../paper-pages/14-neural-machine-translation-jointly-learning-to-align-and-translate/index.md)
