---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/21-dropout-regularization.md
source: ../../papers/21-dropout-regularization.md
paper_title: "Dropout: A Simple Way to Prevent Neural Networks from Overfitting"
sequence: 21
page: 8
pages: [8]
page_of: 18
topics: ["../../topics/regularization.md"]
description: "A.2 Details for dropout finetuning Apart from training a neural network starting from random weights, dropout can also be used to finetune pretrained…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 8 of 18 - Dropout: A Simple Way to Prevent Neural Networks from Overfitting

> Page 8 of the source PDF, verbatim as extracted. Canonical document: [21 - Dropout: A Simple Way to Prevent Neural Networks from Overfitting](../../papers/21-dropout-regularization.md)

## A.2 Details for dropout finetuning

Apart from training a neural network starting from random weights, dropout can also be used to finetune pretrained models. We found that finetuning a model using dropout with a small learning rate can give much better performace than standard backpropagation finetuning.

Deep Belief Nets - We took a neural network pretrained using a Deep Belief Network (5). It had a 784-500-500-2000 architecture and was trained using greedy layer-wise Contrastive Divergence learning 1. Instead of fine-tuning it with the usual backpropagation algorithm, we used the dropout version of it. Dropout rate was same as before : 50% for hidden units and 20% for visible units. A constant small learning rate of 1.0 was used. No constraint was imposed on the length of incoming weight vectors. No weight decay was used. All other hyper-parameters were set to be the same as before. The model was trained for 1000 epochs with stochstic gradient descent using minibatches of size 100. While standard back propagation gave about 118 errors, dropout decreased the errors to about 92.

Deep Boltzmann Machines - We also took a pretrained Deep Boltzmann Machine (18) 2

(784-500-1000-10) and finetuned it using dropout-backpropagation. The model uses a 1784 500 - 1000 - 10 architecture (The extra 1000 input units come from the mean-field activations of the second layer of hidden units in the DBM, See (18) for details). All finetuning hyperparameters were set to be the same as the ones used for a Deep Belief Network. We were able to get a mean of about 79 errors with dropout whereas usual finetuning gives about 94 errors.

## A.3 Effect on features

One reason why dropout gives major improvements over backpropagation is that it encourages each individual hidden unit to learn a useful feature without relying on specific other hidden units to correct its mistakes. In order to verify this and better understand the effect of dropout on feature learning, we look at the first level of features learned by a 784-500-500 neural network without any generative pre-training. The features are shown in Figure 5. Each panel shows 100 random features learned by each network. The features that dropout learns are simpler and look like strokes, whereas the ones learned by standard backpropagation are difficult to interpret. This confirms that dropout indeed forces the discriminative model to learn good features which are less co-adapted and leads to better generalization.

## B Experiments on TIMIT

The TIMIT Acoustic-Phonetic Continuous Speech Corpus is a standard dataset used for evaluation of automatic speech recognition systems. It consists of recordings of 630 speakers of 8 dialects of American English each reading 10 phonetically-rich sentences. It also comes with

1For code see http://www.cs.toronto.edu/˜hinton/MatlabForSciencePaper.html 2 For code see http://www.utstat.toronto.edu/˜rsalakhu/DBM.html

9

---

[previous page](page-007.md) · [next page](page-009.md) · [all pages](index.md)
