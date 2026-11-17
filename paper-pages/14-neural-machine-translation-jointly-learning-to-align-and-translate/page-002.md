---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md
source: ../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md
paper_title: Neural Machine Translation by Jointly Learning to Align and Translate
sequence: 14
page: 2
pages: [2]
page_of: 15
topics: ["../../topics/attention.md", "../../topics/machine-translation.md", "../../topics/sequence-to-sequence.md"]
description: "The decoder is often trained to predict the next word yt′ given the context vector c and all the previously predicted words {y1, · · · , yt′−1}. In…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 2 of 15 - Neural Machine Translation by Jointly Learning to Align and Translate

> Page 2 of the source PDF, verbatim as extracted. Canonical document: [14 - Neural Machine Translation by Jointly Learning to Align and Translate](../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md)

The decoder is often trained to predict the next word yt′ given the context vector c and all the previously predicted words {y1, · · · , yt′−1}. In other words, the decoder defines a probability over the translation y by decomposing the joint probability into the ordered conditionals:

T Y

p(yt | {y1, · · · , yt−1} , c), (2)

p(y) =

t=1

y1, · · · , yTy

where y =

. With an RNN, each conditional probability is modeled as

p(yt | {y1, · · · , yt−1} , c) = g(yt−1, st, c), (3)

where g is a nonlinear, potentially multi-layered, function that outputs the probability of yt, and st is the hidden state of the RNN. It should be noted that other architectures such as a hybrid of an RNN and a de-convolutional neural network can be used (Kalchbrenner and Blunsom, 2013).

## 3 LEARNING TO ALIGN AND TRANSLATE

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

---

[previous page](page-001.md) · [next page](page-003.md) · [all pages](index.md)
