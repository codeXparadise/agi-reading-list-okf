---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md
source: ../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md
paper_title: Neural Machine Translation by Jointly Learning to Align and Translate
sequence: 14
page: 12
pages: [12]
page_of: 15
topics: ["../../topics/attention.md", "../../topics/machine-translation.md", "../../topics/sequence-to-sequence.md"]
description: "A.2 DETAILED DESCRIPTION OF THE MODEL A.2.1 ENCODER In this section, we describe in detail the architecture of the proposed model (RNNsearch) used in…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 12 of 15 - Neural Machine Translation by Jointly Learning to Align and Translate

> Page 12 of the source PDF, verbatim as extracted. Canonical document: [14 - Neural Machine Translation by Jointly Learning to Align and Translate](../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md)

A.2 DETAILED DESCRIPTION OF THE MODEL

A.2.1 ENCODER

In this section, we describe in detail the architecture of the proposed model (RNNsearch) used in the experiments (see Sec. 4–5). From here on, we omit all bias terms in order to increase readability.

The model takes a source sentence of 1-of-K coded word vectors as input

x = (x1, . . . , xTx), xi ∈RKx

and outputs a translated sentence of 1-of-K coded word vectors

y = (y1, . . . , yTy), yi ∈RKy,

where Kx and Ky are the vocabulary sizes of source and target languages, respectively. Tx and Ty respectively denote the lengths of source and target sentences.

First, the forward states of the bidirectional recurrent neural network (BiRNN) are computed:

(1 −−→z i) ◦−→h i−1 + −→z i ◦−→h i , if i > 0 0 , if i = 0

(

−→h i =

where

−→h i = tanh

h−→r i ◦−→h i−1

−→ WExi + −→ U

i

−→h i−1

−→ W zExi + −→ U z

−→z i =σ

−→h i−1

−→ W rExi + −→ U r

−→r i =σ

.

E ∈Rm×Kx is the word embedding matrix. −→ W, −→ W z, −→ W r ∈Rn×m, −→ U , −→ U z, −→ U r ∈Rn×n are weight matrices. m and n are the word embedding dimensionality and the number of hidden units, respectively. σ(·) is as usual a logistic sigmoid function.

The backward states (←−h 1, · · · , ←−h Tx) are computed similarly. We share the word embedding matrix E between the forward and backward RNNs, unlike the weight matrices.

We concatenate the forward and backward states to to obtain the annotations (h1, h2, · · · , hTx), where

" −→h i ←−h i

#

hi =

(7)

A.2.2 DECODER

The hidden state si of the decoder given the annotations from the encoder is computed by

si =(1 −zi) ◦si−1 + zi ◦˜si,

where

˜si = tanh (WEyi−1 + U \[ri ◦si−1\] + Cci) zi =σ (WzEyi−1 + Uzsi−1 + Czci) ri =σ (WrEyi−1 + Ursi−1 + Crci)

E is the word embedding matrix for the target language. W, Wz, Wr ∈Rn×m, U, Uz, Ur ∈Rn×n, and C, Cz, Cr ∈Rn×2n are weights. Again, m and n are the word embedding dimensionality and the number of hidden units, respectively. The initial hidden state s0 is computed by s0 = tanh

←−h 1

, where Ws ∈Rn×n.

Ws

The context vector ci are recomputed at each step by the alignment model:

Tx X

ci =

αijhj,

j=1

---

[previous page](page-011.md) · [next page](page-013.md) · [all pages](index.md)
