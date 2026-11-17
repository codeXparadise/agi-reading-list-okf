---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/11-recurrent-neural-network-regularization.md
source: ../../papers/11-recurrent-neural-network-regularization.md
paper_title: Recurrent Neural Network Regularization
sequence: 11
page: 4
pages: [4]
page_of: 8
topics: ["../../topics/regularization.md", "../../topics/recurrent-neural-networks.md"]
description: "Model Validation set Test set A single model Pascanu et al. (2013) 107.5 Cheng et al. 100.0 non-regularized LSTM 120.7 114.5 Medium regularized LSTM…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 4 of 8 - Recurrent Neural Network Regularization

> Page 4 of the source PDF, verbatim as extracted. Canonical document: [11 - Recurrent Neural Network Regularization](../../papers/11-recurrent-neural-network-regularization.md)

Model Validation set Test set

A single model

Pascanu et al. (2013) 107.5 Cheng et al. 100.0 non-regularized LSTM 120.7 114.5 Medium regularized LSTM 86.2 82.7 Large regularized LSTM 82.2 78.4

Model averaging

Mikolov (2012) 83.5 Cheng et al. 80.6 2 non-regularized LSTMs 100.4 96.1 5 non-regularized LSTMs 87.9 84.1 10 non-regularized LSTMs 83.5 80.0 2 medium regularized LSTMs 80.6 77.0 5 medium regularized LSTMs 76.7 73.3 10 medium regularized LSTMs 75.2 72.0 2 large regularized LSTMs 76.9 73.6 10 large regularized LSTMs 72.8 69.5 38 large regularized LSTMs 71.9 68.7

Model averaging with dynamic RNNs and n-gram models

Mikolov & Zweig (2012) 72.9

Table 1: Word-level perplexity on the Penn Tree Bank dataset.

The medium LSTM has 650 units per layer and its parameters are initialized uniformly in \[−0.05, 0.05\]. As described earlier, we apply 50% dropout on the non-recurrent connections. We train the LSTM for 39 epochs with a learning rate of 1, and after 6 epochs we decrease it by a factor of 1.2 after each epoch. We clip the norm of the gradients (normalized by minibatch size) at 5. Training this network takes about half a day on an NVIDIA K20 GPU.

The large LSTM has 1500 units per layer and its parameters are initialized uniformly in \[−0.04, 0.04\]. We apply 65% dropout on the non-recurrent connections. We train the model for 55 epochs with a learning rate of 1; after 14 epochs we start to reduce the learning rate by a factor of 1.15 after each epoch. We clip the norm of the gradients (normalized by minibatch size) at 10 Mikolov et al. (2010). Training this network takes an entire day on an NVIDIA K20 GPU.

For comparison, we trained a non-regularized network. We optimized its parameters to get the best validation performance. The lack of regularization effectively constrains size of the network, forcing us to use small network because larger networks overfit. Our best performing non-regularized LSTM has two hidden layers with 200 units per layer, and its weights are initialized uniformly in \[−0.1, 0.1\]. We train it for 4 epochs with a learning rate of 1 and then we decrease the learning rate by a factor of 2 after each epoch, for a total of 13 training epochs. The size of each minibatch is 20, and we unroll the network for 20 steps. Training this network takes 2-3 hours on an NVIDIA K20 GPU.

Table 1 compares previous results with our LSTMs, and Figure 4 shows samples drawn from a single large regularized LSTM.

4.2 SPEECH RECOGNITION

Deep Neural Networks have been used for acoustic modeling for over half a century (see Bourlard & Morgan (1993) for a good review). Acoustic modeling is a key component in mapping acoustic signals to sequences of words, as it models p(st|X) where st is the phonetic state at time t and X is the acoustic observation. Recent work has shown that LSTMs can achieve excellent performance on acoustic modeling Sak et al. (2014), yet relatively small LSTMs (in terms of the number of their parameters) can easily overfit the training set. A useful metric for measuring the performance of acoustic models is frame accuracy, which is measured at each st for all timesteps t. Generally, this metric correlates with the actual metric of interest, the Word Error Rate (WER).

---

[previous page](page-003.md) · [next page](page-005.md) · [all pages](index.md)
