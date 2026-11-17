---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/21-dropout-regularization.md
source: ../../papers/21-dropout-regularization.md
paper_title: "Dropout: A Simple Way to Prevent Neural Networks from Overfitting"
sequence: 21
page: 9
pages: [9]
page_of: 18
topics: ["../../topics/regularization.md"]
description: "(a) (b) Fig. 5: Visualization of features learned by first layer hidden units for (a) backprop and (b) dropout on the MNIST dataset. the word and…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 9 of 18 - Dropout: A Simple Way to Prevent Neural Networks from Overfitting

> Page 9 of the source PDF, verbatim as extracted. Canonical document: [21 - Dropout: A Simple Way to Prevent Neural Networks from Overfitting](../../papers/21-dropout-regularization.md)

(a)

(b)

Fig. 5: Visualization of features learned by first layer hidden units for (a) backprop and (b) dropout on the MNIST dataset.

the word and phone-level transcriptions of the speech. The objective is to convert a given speech signal into a transcription sequence of phones. This data needs to be pre-processed to extract input features and output targets. We used Kaldi, an open source code library for speech 3, to pre-process the dataset so that our results can be reproduced exactly. The inputs to our networks are log filter bank responses. They are extracted for 25 ms speech windows with strides of 10 ms.

Each dimension of the input representation was normalized to have mean 0 and variance 1. Minibatches of size 100 were used for both pretraining and dropout finetuning. We tried several network architectures by varying the number of input frames (15 and 31), number of layers in the neural network (3, 4 and 5) and the number of hidden units in each layer (2000 and 4000). Figure 6 shows the validation error curves for a number of these combinations. Using dropout consistently leads to lower error rates.

## B.1 Pretraining

For all our experiments on TIMIT, we pretrain the neural network with a Deep Belief Network (5). Since the inputs are real-valued, the first layer was pre-trained as a Gaussian RBM.

3http://kaldi.sourceforge.net

10

---

[previous page](page-008.md) · [next page](page-010.md) · [all pages](index.md)
