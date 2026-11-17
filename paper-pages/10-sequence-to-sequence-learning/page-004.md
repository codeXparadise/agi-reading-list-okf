---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/10-sequence-to-sequence-learning.md
source: ../../papers/10-sequence-to-sequence-learning.md
paper_title: Sequence to Sequence Learning with Neural Networks
sequence: 10
page: 4
pages: [4]
page_of: 9
topics: ["../../topics/sequence-to-sequence.md", "../../topics/machine-translation.md", "../../topics/recurrent-neural-networks.md"]
description: "trained on the raw source sentences (see sec. 3.7), which suggests that reversing the input sentences results in LSTMs with better memory…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 4 of 9 - Sequence to Sequence Learning with Neural Networks

> Page 4 of the source PDF, verbatim as extracted. Canonical document: [10 - Sequence to Sequence Learning with Neural Networks](../../papers/10-sequence-to-sequence-learning.md)

trained on the raw source sentences (see sec. 3.7), which suggests that reversing the input sentences results in LSTMs with better memory utilization.

## 3.4 Training details

We found that the LSTM models are fairly easy to train. We used deep LSTMs with 4 layers, with 1000 cells at each layer and 1000 dimensional word embeddings, with an input vocabulary of 160,000 and an output vocabulary of 80,000. Thus the deep LSTM uses 8000 real numbers to represent a sentence. We found deep LSTMs to significantly outperform shallow LSTMs, where each additional layer reduced perplexity by nearly 10%, possibly due to their much larger hidden state. We used a naive softmax over 80,000 words at each output. The resulting LSTM has 384M parameters of which 64M are pure recurrent connections (32M for the “encoder” LSTM and 32M for the “decoder” LSTM). The complete training details are given below:

• We initialized all of the LSTM’s parameters with the uniform distribution between -0.08 and 0.08

• We used stochastic gradient descent without momentum, with a fixed learning rate of 0.7. After 5 epochs, we begun halving the learning rate every half epoch. We trained our models for a total of 7.5 epochs.

• We used batches of 128 sequences for the gradient and divided it the size of the batch (namely, 128).

• Although LSTMs tend to not suffer from the vanishing gradient problem, they can have exploding gradients. Thus we enforced a hard constraint on the norm of the gradient \[10, 25\] by scaling it when its norm exceeded a threshold. For each training batch, we compute s = ∥g∥2, where g is the gradient divided by 128. If s > 5, we set g = 5g

s .

• Different sentences have different lengths. Most sentences are short (e.g., length 20-30) but some sentences are long (e.g., length > 100), so a minibatch of 128 randomly chosen training sentences will have many short sentences and few long sentences, and as a result, much of the computation in the minibatch is wasted. To address this problem, we made sure that all sentences in a minibatch are roughly of the same length, yielding a 2x speedup.

## 3.5 Parallelization

A C++ implementation of deep LSTM with the configuration from the previous section on a single GPU processes a speed of approximately 1,700 words per second. This was too slow for our purposes, so we parallelized our model using an 8-GPU machine. Each layer of the LSTM was executed on a different GPU and communicated its activations to the next GPU / layer as soon as they were computed. Our models have 4 layers of LSTMs, each of which resides on a separate GPU. The remaining 4 GPUs were used to parallelize the softmax, so each GPU was responsible for multiplying by a 1000 × 20000 matrix. The resulting implementation achieved a speed of 6,300 (both English and French) words per second with a minibatch size of 128. Training took about a ten days with this implementation.

## 3.6 Experimental Results

We used the cased BLEU score \[24\] to evaluate the quality of our translations. We computed our BLEU scores using multi-bleu.pl1 on the tokenized predictions and ground truth. This way of evaluating the BELU score is consistent with \[5\] and \[2\], and reproduces the 33.3 score of \[29\]. However, if we evaluate the best WMT’14 system \[9\] (whose predictions can be downloaded from statmt.org\\matrix) in this manner, we get 37.0, which is greater than the 35.8 reported by statmt.org\\matrix.

The results are presented in tables 1 and 2. Our best results are obtained with an ensemble of LSTMs that differ in their random initializations and in the random order of minibatches. While the decoded translations of the LSTM ensemble do not outperform the best WMT’14 system, it is the first time that a pure neural translation system outperforms a phrase-based SMT baseline on a large scale MT

1There several variants of the BLEU score, and each variant is defined with a perl script.

---

[previous page](page-003.md) · [next page](page-005.md) · [all pages](index.md)
