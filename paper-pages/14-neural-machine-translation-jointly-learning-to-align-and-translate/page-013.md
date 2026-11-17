---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md
source: ../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md
paper_title: Neural Machine Translation by Jointly Learning to Align and Translate
sequence: 14
page: 13
pages: [13]
page_of: 15
topics: ["../../topics/attention.md", "../../topics/machine-translation.md", "../../topics/sequence-to-sequence.md"]
description: "Model Updates (×105) Epochs Hours GPU Train NLL Dev. NLL RNNenc-30 8.46 6.4 109 TITAN BLACK 28.1 53.0 RNNenc-50 6.00 4.5 108 Quadro K-6000 44.0 43.6…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 13 of 15 - Neural Machine Translation by Jointly Learning to Align and Translate

> Page 13 of the source PDF, verbatim as extracted. Canonical document: [14 - Neural Machine Translation by Jointly Learning to Align and Translate](../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md)

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

## B TRAINING PROCEDURE

B.1 PARAMETER INITIALIZATION

We initialized the recurrent weight matrices U, Uz, Ur, ←− U , ←− U z, ←− U r, −→ U , −→ U z and −→ U r as random orthogonal matrices. For Wa and Ua, we initialized them by sampling each element from the Gaussian distribution of mean 0 and variance 0.0012. All the elements of Va and all the bias vectors were initialized to zero. Any other weight matrix was initialized by sampling from the Gaussian distribution of mean 0 and variance 0.012.

B.2 TRAINING

We used the stochastic gradient descent (SGD) algorithm. Adadelta (Zeiler, 2012) was used to automatically adapt the learning rate of each parameter (ϵ = 10−6 and ρ = 0.95). We explicitly

---

[previous page](page-012.md) · [next page](page-014.md) · [all pages](index.md)
