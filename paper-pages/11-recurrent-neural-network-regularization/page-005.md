---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/11-recurrent-neural-network-regularization.md
source: ../../papers/11-recurrent-neural-network-regularization.md
paper_title: Recurrent Neural Network Regularization
sequence: 11
page: 5
pages: [5]
page_of: 8
topics: ["../../topics/regularization.md", "../../topics/recurrent-neural-networks.md"]
description: "Model Training set Validation set Non-regularized LSTM 71.6 68.9 Regularized LSTM 69.4 70.5 Table 2: Frame-level accuracy on the Icelandic Speech…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 5 of 8 - Recurrent Neural Network Regularization

> Page 5 of the source PDF, verbatim as extracted. Canonical document: [11 - Recurrent Neural Network Regularization](../../papers/11-recurrent-neural-network-regularization.md)

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

## 5 CONCLUSION

We presented a simple way of applying dropout to LSTMs that results in large performance increases on several problems in different domains. Our work makes dropout useful for RNNs, and our results suggest that our implementation of dropout could improve performance on a wide variety of applications.

---

[previous page](page-004.md) · [next page](page-006.md) · [all pages](index.md)
