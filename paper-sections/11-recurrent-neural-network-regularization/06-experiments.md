---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/11-recurrent-neural-network-regularization.md
source: ../../papers/11-recurrent-neural-network-regularization.md
paper_title: Recurrent Neural Network Regularization
sequence: 11
section: 4 EXPERIMENTS
section_role: experiments
section_index: 6
pages: [3, 4, 5]
topics: ["../../topics/regularization.md", "../../topics/recurrent-neural-networks.md"]
description: "We present results in three domains: language modeling (Section 4.1), speech recognition (Section 4.2), machine translation (Section 4.3), and image…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 4 EXPERIMENTS

> Section 6 of 9 from [11 - Recurrent Neural Network Regularization](../../papers/11-recurrent-neural-network-regularization.md) · `experiments` · pages 3-5

We present results in three domains: language modeling (Section 4.1), speech recognition (Section 4.2), machine translation (Section 4.3), and image caption generation (Section 4.4).

4.1 LANGUAGE MODELING

We conducted word-level prediction experiments on the Penn Tree Bank (PTB) dataset Marcus et al. (1993), which consists of 929k training words, 73k validation words, and 82k test words. It has 10k words in its vocabulary. We downloaded it from Tomas Mikolov’s webpage†. We trained regularized LSTMs of two sizes; these are denoted the medium LSTM and large LSTM. Both LSTMs have two layers and are unrolled for 35 steps. We initialize the hidden states to zero. We then use the final hidden states of the current minibatch as the initial hidden state of the subsequent minibatch (successive minibatches sequentially traverse the training set). The size of each minibatch is 20.

†http://www.fit.vutbr.cz/˜imikolov/rnnlm/simple-examples.tgz

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

Model Training set Validation set

Non-regularized LSTM 71.6 68.9 Regularized LSTM 69.4 70.5

Table 2: Frame-level accuracy on the Icelandic Speech Dataset. The training set has 93k utterances.

Model Test perplexity Test BLEU score

Non-regularized LSTM 5.8 25.9 Regularized LSTM 5.0 29.03

LIUM system 33.30

Table 3: Results on the English to French translation task.

Since computing the WER involves using a language model and tuning the decoding parameters for every change in the acoustic model, we decided to focus on frame accuracy in these experiments. Table 2 shows that dropout improves the frame accuracy of the LSTM. Not surprisingly, the training frame accuracy drops due to the noise added during training, but as is often the case with dropout, this yields models that generalize better to unseen data. Note that the test set is easier than the training set, as its accuracy is higher. We report the performance of an LSTM on an internal Google Icelandic Speech dataset, which is relatively small (93k utterances), so overfitting is a great concern.

4.3 MACHINE TRANSLATION

We formulate a machine translation problem as a language modelling task, where an LSTM is trained to assign high probability to a correct translation of a source sentence. Thus, the LSTM is trained on concatenations of source sentences and their translations Sutskever et al. (2014) (see also Cho et al. (2014)). We compute a translation by approximating the most probable sequence of words using a simple beam search with a beam of size 12. We ran an LSTM on the WMT’14 English to French dataset, on the “selected” subset from Schwenk (2014) which has 340M French words and 304M English words. Our LSTM has 4 hidden layers, and both its layers and word embeddings have 1000 units. Its English vocabulary has 160,000 words and its French vocabulary has 80,000 words. The optimal dropout probability was 0.2. Table 3 shows the performance of an LSTM trained with and without dropout. While our LSTM does not beat the phrase-based LIUM SMT system Schwenk et al. (2011), our results show that dropout improves the translation performance of the LSTM.

4.4 IMAGE CAPTION GENERATION

We applied the dropout variant to the image caption generation model of Vinyals et al. (2014). The image caption generation is similar to the sequence-to-sequence model of Sutskever et al. (2014), but where the input image is mapped onto a vector with a highly-accurate pre-trained convolutional neural network (Szegedy et al., 2014), which is converted into a caption with a single-layer LSTM (see Vinyals et al. (2014) for the details on the architecture). We test our dropout scheme on LSTM as the convolutional neural network is not trained on the image caption dataset because it is not large (MSCOCO (Lin et al., 2014)).

Our results are summarized in the following Table 4. In brief, dropout helps relative to not using dropout, but using an ensemble eliminates the gains attained by dropout. Thus, in this setting, the main effect of dropout is to produce a single model that is as good as an ensemble, which is a reasonable improvement given the simplicity of the technique.

---

Full document: [11 - Recurrent Neural Network Regularization](../../papers/11-recurrent-neural-network-regularization.md) · Page-level evidence: [paper-pages/11-recurrent-neural-network-regularization](../../paper-pages/11-recurrent-neural-network-regularization/index.md)
