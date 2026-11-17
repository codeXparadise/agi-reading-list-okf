---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md
source: ../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md
paper_title: Neural Machine Translation by Jointly Learning to Align and Translate
sequence: 14
page: 11
pages: [11]
page_of: 15
topics: ["../../topics/attention.md", "../../topics/machine-translation.md", "../../topics/sequence-to-sequence.md"]
description: "A MODEL ARCHITECTURE A.1 ARCHITECTURAL CHOICES The proposed scheme in Section 3 is a general framework where one can freely define, for instance, the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 11 of 15 - Neural Machine Translation by Jointly Learning to Align and Translate

> Page 11 of the source PDF, verbatim as extracted. Canonical document: [14 - Neural Machine Translation by Jointly Learning to Align and Translate](../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md)

## A MODEL ARCHITECTURE

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

---

[previous page](page-010.md) · [next page](page-012.md) · [all pages](index.md)
