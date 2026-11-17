---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/10-sequence-to-sequence-learning.md
source: ../../papers/10-sequence-to-sequence-learning.md
paper_title: Sequence to Sequence Learning with Neural Networks
sequence: 10
page: 2
pages: [2]
page_of: 9
topics: ["../../topics/sequence-to-sequence.md", "../../topics/machine-translation.md", "../../topics/recurrent-neural-networks.md"]
description: "sentences meanings will be far. A qualitative evaluation supports this claim, showing that our model is aware of word order and is fairly invariant…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 2 of 9 - Sequence to Sequence Learning with Neural Networks

> Page 2 of the source PDF, verbatim as extracted. Canonical document: [10 - Sequence to Sequence Learning with Neural Networks](../../papers/10-sequence-to-sequence-learning.md)

sentences meanings will be far. A qualitative evaluation supports this claim, showing that our model is aware of word order and is fairly invariant to the active and passive voice.

## 2 The model

The Recurrent Neural Network (RNN) \[31, 28\] is a natural generalization of feedforward neural networks to sequences. Given a sequence of inputs (x1, . . . , xT ), a standard RNN computes a sequence of outputs (y1, . . . , yT ) by iterating the following equation:

W hxxt + W hhht−1

ht = sigm

yt = W yhht

The RNN can easily map sequences to sequences whenever the alignment between the inputs the outputs is known ahead of time. However, it is not clear how to apply an RNN to problems whose input and the output sequences have different lengths with complicated and non-monotonic relationships.

The simplest strategy for general sequence learning is to map the input sequence to a fixed-sized vector using one RNN, and then to map the vector to the target sequence with another RNN (this approach has also been taken by Cho et al. \[5\]). While it could work in principle since the RNN is provided with all the relevant information, it would be difficult to train the RNNs due to the resulting long term dependencies (figure 1) \[14, 4, 16, 15\]. However, the Long Short-Term Memory (LSTM) \[16\] is known to learn problems with long range temporal dependencies, so an LSTM may succeed in this setting.

The goal of the LSTM is to estimate the conditional probability p(y1, . . . , yT ′|x1, . . . , xT ) where (x1, . . . , xT ) is an input sequence and y1, . . . , yT ′ is its corresponding output sequence whose length T ′ may differ from T . The LSTM computes this conditional probability by first obtaining the fixeddimensional representation v of the input sequence (x1, . . . , xT ) given by the last hidden state of the LSTM, and then computing the probability of y1, . . . , yT ′ with a standard LSTM-LM formulation whose initial hidden state is set to the representation v of x1, . . . , xT :

T ′ Y

p(yt|v, y1, . . . , yt−1) (1)

p(y1, . . . , yT ′|x1, . . . , xT ) =

t=1

In this equation, each p(yt|v, y1, . . . , yt−1) distribution is represented with a softmax over all the words in the vocabulary. We use the LSTM formulation from Graves \[10\]. Note that we require that each sentence ends with a special end-of-sentence symbol “<EOS>”, which enables the model to define a distribution over sequences of all possible lengths. The overall scheme is outlined in figure 1, where the shown LSTM computes the representation of “A”, “B”, “C”, “<EOS>” and then uses this representation to compute the probability of “W”, “X”, “Y”, “Z”, “<EOS>”.

Our actual models differ from the above description in three important ways. First, we used two different LSTMs: one for the input sequence and another for the output sequence, because doing so increases the number model parameters at negligible computational cost and makes it natural to train the LSTM on multiple language pairs simultaneously \[18\]. Second, we found that deep LSTMs significantly outperformed shallow LSTMs, so we chose an LSTM with four layers. Third, we found it extremely valuable to reverse the order of the words of the input sentence. So for example, instead of mapping the sentence a, b, c to the sentence α, β, γ, the LSTM is asked to map c, b, a to α, β, γ, where α, β, γ is the translation of a, b, c. This way, a is in close proximity to α, b is fairly close to β, and so on, a fact that makes it easy for SGD to “establish communication” between the input and the output. We found this simple data transformation to greatly improve the performance of the LSTM.

## 3 Experiments

We applied our method to the WMT’14 English to French MT task in two ways. We used it to directly translate the input sentence without using a reference SMT system and we it to rescore the n-best lists of an SMT baseline. We report the accuracy of these translation methods, present sample translations, and visualize the resulting sentence representation.

---

[previous page](page-001.md) · [next page](page-003.md) · [all pages](index.md)
