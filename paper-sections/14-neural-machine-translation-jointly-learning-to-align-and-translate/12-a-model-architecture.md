---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md
source: ../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md
paper_title: Neural Machine Translation by Jointly Learning to Align and Translate
sequence: 14
section: A MODEL ARCHITECTURE
section_role: other
section_index: 12
pages: [11, 12, 13]
topics: ["../../topics/attention.md", "../../topics/machine-translation.md", "../../topics/sequence-to-sequence.md"]
description: "A.1 ARCHITECTURAL CHOICES The proposed scheme in Section 3 is a general framework where one can freely define, for instance, the activation functions…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# A MODEL ARCHITECTURE

> Section 12 of 14 from [14 - Neural Machine Translation by Jointly Learning to Align and Translate](../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md) · `other` · pages 11-13

A.1 ARCHITECTURAL CHOICES

The proposed scheme in Section 3 is a general framework where one can freely define, for instance, the activation functions f of recurrent neural networks (RNN) and the alignment model a. Here, we describe the choices we made for the experiments in this paper.

A.1.1 RECURRENT NEURAL NETWORK

For the activation function f of an RNN, we use the gated hidden unit recently proposed by Cho et al. (2014a). The gated hidden unit is an alternative to the conventional simple units such as an element-wise tanh. This gated unit is similar to a long short-term memory (LSTM) unit proposed earlier by Hochreiter and Schmidhuber (1997), sharing with it the ability to better model and learn long-term dependencies. This is made possible by having computation paths in the unfolded RNN for which the product of derivatives is close to 1. These paths allow gradients to flow backward easily without suffering too much from the vanishing effect (Hochreiter, 1991; Bengio et al., 1994; Pascanu et al., 2013a). It is therefore possible to use LSTM units instead of the gated hidden unit described here, as was done in a similar context by Sutskever et al. (2014).

The new state si of the RNN employing n gated hidden units8 is computed by

si = f(si−1, yi−1, ci) = (1 −zi) ◦si−1 + zi ◦˜si,

where ◦is an element-wise multiplication, and zi is the output of the update gates (see below). The proposed updated state ˜si is computed by

˜si = tanh (We(yi−1) + U \[ri ◦si−1\] + Cci) ,

where e(yi−1) ∈Rm is an m-dimensional embedding of a word yi−1, and ri is the output of the reset gates (see below). When yi is represented as a 1-of-K vector, e(yi) is simply a column of an embedding matrix E ∈Rm×K. Whenever possible, we omit bias terms to make the equations less cluttered.

The update gates zi allow each hidden unit to maintain its previous activation, and the reset gates ri control how much and what information from the previous state should be reset. We compute them by

zi = σ (Wze(yi−1) + Uzsi−1 + Czci) , ri = σ (Wre(yi−1) + Ursi−1 + Crci) ,

where σ (·) is a logistic sigmoid function.

At each step of the decoder, we compute the output probability (Eq. (4)) as a multi-layered function (Pascanu et al., 2014). We use a single hidden layer of maxout units (Goodfellow et al., 2013) and normalize the output probabilities (one for each word) with a softmax function (see Eq. (6)).

A.1.2 ALIGNMENT MODEL

The alignment model should be designed considering that the model needs to be evaluated Tx × Ty times for each sentence pair of lengths Tx and Ty. In order to reduce computation, we use a singlelayer multilayer perceptron such that

a(si−1, hj) = v⊤

a tanh (Wasi−1 + Uahj) ,

where Wa ∈Rn×n, Ua ∈Rn×2n and va ∈Rn are the weight matrices. Since Uahj does not depend on i, we can pre-compute it in advance to minimize the computational cost.

8 Here, we show the formula of the decoder. The same formula can be used in the encoder by simply ignoring the context vector ci and the related terms.

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

Model Updates (×105) Epochs Hours GPU Train NLL Dev. NLL RNNenc-30 8.46 6.4 109 TITAN BLACK 28.1 53.0 RNNenc-50 6.00 4.5 108 Quadro K-6000 44.0 43.6 RNNsearch-30 4.71 3.6 113 TITAN BLACK 26.7 47.2 RNNsearch-50 2.88 2.2 111 Quadro K-6000 40.7 38.1 RNNsearch-50⋆ 6.67 5.0 252 Quadro K-6000 36.7 35.2

Table 2: Learning statistics and relevant information. Each update corresponds to updating the parameters once using a single minibatch. One epoch is one pass through the training set. NLL is the average conditional log-probabilities of the sentences in either the training set or the development set. Note that the lengths of the sentences differ.

where

αij = exp (eij) PTx

k=1 exp (eik)

eij =v⊤

a tanh (Wasi−1 + Uahj) ,

and hj is the j-th annotation in the source sentence (see Eq. (7)). va ∈Rn′, Wa ∈Rn′×n and Ua ∈Rn′×2n are weight matrices. Note that the model becomes RNN Encoder–Decoder (Cho et al., 2014a), if we fix ci to −→h Tx.

With the decoder state si−1, the context ci and the last generated word yi−1, we define the probability of a target word yi as

y⊤

p(yi|si, yi−1, ci) ∝exp

i Woti

,

where

⊤

˜ti,2j−1, ˜ti,2j

ti =

max

j=1,...,l

and ˜ti,k is the k-th element of a vector ˜ti which is computed by

˜ti =Uosi−1 + VoEyi−1 + Coci.

Wo ∈RKy×l, Uo ∈R2l×n, Vo ∈R2l×m and Co ∈R2l×2n are weight matrices. This can be understood as having a deep output (Pascanu et al., 2014) with a single maxout hidden layer (Goodfellow et al., 2013).

A.2.3 MODEL SIZE

For all the models used in this paper, the size of a hidden layer n is 1000, the word embedding dimensionality m is 620 and the size of the maxout hidden layer in the deep output l is 500. The number of hidden units in the alignment model n′ is 1000.

---

Full document: [14 - Neural Machine Translation by Jointly Learning to Align and Translate](../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md) · Page-level evidence: [paper-pages/14-neural-machine-translation-jointly-learning-to-align-and-translate](../../paper-pages/14-neural-machine-translation-jointly-learning-to-align-and-translate/index.md)
