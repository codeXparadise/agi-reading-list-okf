---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/11-recurrent-neural-network-regularization.md
source: ../../papers/11-recurrent-neural-network-regularization.md
paper_title: Recurrent Neural Network Regularization
sequence: 11
page: 1
pages: [1]
page_of: 8
topics: ["../../topics/regularization.md", "../../topics/recurrent-neural-networks.md"]
description: "There have been a number of architectural variants of the RNN that perform better on problems with long term dependencies Hochreiter & Schmidhuber…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 1 of 8 - Recurrent Neural Network Regularization

> Page 1 of the source PDF, verbatim as extracted. Canonical document: [11 - Recurrent Neural Network Regularization](../../papers/11-recurrent-neural-network-regularization.md)

There have been a number of architectural variants of the RNN that perform better on problems with long term dependencies Hochreiter & Schmidhuber (1997); Graves et al. (2009); Cho et al. (2014); Jaeger et al. (2007); Koutn´ık et al. (2014); Sundermeyer et al. (2012). In this work, we show how to correctly apply dropout to LSTMs, the most commonly-used RNN variant; this way of applying dropout is likely to work well with other RNN architectures as well.

In this paper, we consider the following tasks: language modeling, speech recognition, and machine translation. Language modeling is the first task where RNNs have achieved substantial success Mikolov et al. (2010; 2011); Pascanu et al. (2013). RNNs have also been successfully used for speech recognition Robinson et al. (1996); Graves et al. (2013) and have recently been applied to machine translation, where they are used for language modeling, re-ranking, or phrase modeling Devlin et al. (2014); Kalchbrenner & Blunsom (2013); Cho et al. (2014); Chow et al. (1987); Mikolov et al. (2013).

## 3 REGULARIZING RNNS WITH LSTM CELLS

In this section we describe the deep LSTM (Section 3.1). Next, we show how to regularize them (Section 3.2), and explain why our regularization scheme works.

We let subscripts denote timesteps and superscripts denote layers. All our states are n-dimensional. Let hl

t ∈Rn be a hidden state in layer l in timestep t. Moreover, let Tn,m : Rn →Rm be an affine transform (Wx + b for some W and b). Let ⊙be element-wise multiplication and let h0

t be an input word vector at timestep k. We use the activations hL

t to predict yt, since L is the number of layers in our deep LSTM.

3.1 LONG-SHORT TERM MEMORY UNITS

The RNN dynamics can be described using deterministic transitions from previous to current hidden states. The deterministic state transition is a function

RNN : hl−1

t , hl

t−1 →hl

t

For classical RNNs, this function is given by

t−1), where f ∈{sigm, tanh}

t = f(Tn,nhl−1

hl

t + Tn,nhl

The LSTM has complicated dynamics that allow it to easily “memorize” information for an extended number of timesteps. The “long term” memory is stored in a vector of memory cells cl

t ∈Rn. Although many LSTM architectures that differ in their connectivity structure and activation functions, all LSTM architectures have explicit memory cells for storing information for long periods of time. The LSTM can decide to overwrite the memory cell, retrieve it, or keep it for the next time step. The LSTM architecture used in our experiments is given by the following equations Graves et al. (2013):

LSTM : hl−1

t , hl

t−1, cl

t−1 →hl

t, cl

t 

i f o g

sigm sigm sigm tanh







hl−1

t hl

 T2n,4n

 =

 

 

t−1

cl

t = f ⊙cl

t−1 + i ⊙g

hl

t = o ⊙tanh(cl

t)

In these equations, sigm and tanh are applied element-wise. Figure 1 illustrates the LSTM equations.

3.2 REGULARIZATION WITH DROPOUT

The main contribution of this paper is a recipe for applying dropout to LSTMs in a way that successfully reduces overfitting. The main idea is to apply the dropout operator only to the non-recurrent

---

first page · [next page](page-002.md) · [all pages](index.md)
