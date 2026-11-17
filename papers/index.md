# Papers

All 30 papers in the list, in reading order. Every entry links to a concept document with the full extracted text, figures and relationships.

## Core Architecture & Transformers

* [01 - Attention Is All You Need](01-attention-is-all-you-need.md) - Introduces the Transformer, an architecture built entirely from multi-head self-attention and positional encodings, with no recurrence or… (2017)
* [02 - The Annotated Transformer](02-the-annotated-transformer.md) - A line-by-line, runnable reimplementation of the Transformer paper in PyTorch, with commentary that ties every equation to code. The practical… (2018)
* [03 - Scaling Laws for Neural Language Models](03-scaling-laws-for-neural-language-models.md) - Shows that language-model loss falls as a smooth power law in model size, dataset size and compute, across many orders of magnitude. This is the… (2020)
* [04 - ImageNet Classification with Deep Convolutional Neural Networks](04-imagenet-classification-alexnet.md) - AlexNet: the 2012 ImageNet winner that made deep convolutional networks the default in vision and set off the modern deep learning era. ReLU, dropout… (2012)
* [05 - Deep Residual Learning for Image Recognition](05-deep-residual-learning-resnet.md) - ResNet: reformulates a layer as learning a residual on top of an identity mapping, which lets networks train at 100+ layers. Skip connections turned… (2015)
* [06 - Identity Mappings in Deep Residual Networks](06-identity-mappings-in-deep-residual-networks.md) - The pre-activation follow-up to ResNet: an analysis of why identity shortcuts keep gradients healthy, and a redesign that makes very deep residual… (2016)
* [07 - Multi-Scale Context Aggregation by Dilated Convolutions](07-multi-scale-context-aggregation-dilated-convolutions.md) - Dilated (atrous) convolutions widen the receptive field exponentially without losing resolution or adding parameters. The idea later reappears in… (2015)

## Recurrent Neural Networks

* [08 - The Unreasonable Effectiveness of Recurrent Neural Networks](08-unreasonable-effectiveness-of-recurrent-neural-networks.md) - A hands-on essay: train character-level RNNs and watch them produce Shakespeare, LaTeX, C code and Wikipedia markup. The best intuition pump for why… (2015)
* [09 - Understanding LSTM Networks](09-understanding-lstm-networks.md) - The clearest visual walkthrough of LSTM gates - forget, input and output - and of why a cell state can carry information across long sequences where… (2015)
* [10 - Sequence to Sequence Learning with Neural Networks](10-sequence-to-sequence-learning.md) - Encoder-decoder LSTMs for machine translation: one network reads a sentence into a fixed vector, another writes the translation. The template every… (2014)
* [11 - Recurrent Neural Network Regularization](11-recurrent-neural-network-regularization.md) - Shows how to apply dropout to LSTMs correctly - on the non-recurrent connections only - which is what made regularised RNNs competitive on language… (2014)
* [12 - Pointer Networks](12-pointer-networks.md) - Outputs are pointers into the input sequence rather than indices into a fixed vocabulary, so the model can solve variable-size combinatorial problems… (2015)
* [13 - Order Matters: Sequence to Sequence for Sets](13-order-matters-sequence-to-sequence-for-sets.md) - Reads an unordered set in one order and decodes in another, showing how input ordering and attention interact - and when a set-to-sequence model can… (2015)
* [14 - Neural Machine Translation by Jointly Learning to Align and Translate](14-neural-machine-translation-jointly-learning-to-align-and-translate.md) - Introduces attention: instead of squeezing the source sentence into one vector, the decoder learns where to look at each step. This paper is the… (2014)
* [15 - Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](15-deep-speech-2.md) - End-to-end deep learning for speech recognition: recurrent networks plus CTC, scaled into a production system that works in both English and… (2015)

## Reasoning & External Memory

* [16 - Neural Turing Machines](16-neural-turing-machines.md) - A neural network coupled to an external memory matrix that it learns to read from and write to with differentiable operations. The founding paper for… (2014)
* [17 - A Simple Neural Network Module for Relational Reasoning](17-simple-neural-network-module-for-relational-reasoning.md) - The Relation Network: a small module that reasons explicitly over all pairs of objects, giving strong results on CLEVR-style visual question… (2017)
* [18 - Relational Recurrent Neural Networks](18-relational-recurrent-neural-networks.md) - Puts a relation-network memory inside a recurrent network so that separate facts in memory can interact with each other - relational reasoning… (2018)

## Theory, Complexity & Optimization

* [19 - GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism](19-gpipe-pipeline-parallelism.md) - Pipeline parallelism plus micro-batching, so a model too large for one accelerator can still be trained efficiently. The arXiv record is titled… (2018)
* [20 - Adam: A Method for Stochastic Optimization](20-adam-stochastic-optimization.md) - Adaptive moment estimation: per-parameter learning rates derived from running estimates of the first and second gradient moments, plus bias… (2014)
* [21 - Dropout: A Simple Way to Prevent Neural Networks from Overfitting](21-dropout-regularization.md) - Randomly dropping units during training, read as training an ensemble of thinned networks. The arXiv record is the 2012 preprint 'Improving neural… (2014)
* [22 - The First Law of Complexodynamics](22-first-law-of-complexodynamics.md) - An essay asking for a law that explains why the 'complexity' of a closed system rises, peaks and falls while entropy only rises - and proposing… (2011)
* [23 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights](23-keeping-neural-networks-simple.md) - Treats each weight as a distribution and penalises the number of bits needed to describe it, linking generalisation to compression. An early… (1993)
* [24 - A Tutorial Introduction to the Minimum Description Length Principle](24-tutorial-minimum-description-length.md) - A readable tutorial on MDL: learning as finding the model that compresses the data shortest, with the theory of why that controls overfitting. The… (2004)
* [25 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton](25-coffee-automaton.md) - Turns the coffee-and-milk thought experiment into a simulation, separating entropy from 'apparent complexity' and measuring how the latter rises and… (2014)
* [26 - Kolmogorov Complexity and Algorithmic Randomness](26-kolmogorov-complexity-and-algorithmic-randomness.md) - The standard graduate text on Kolmogorov complexity, randomness deficiency and the two-part-code view of a good model. The reading list points at the… (2017)
* [27 - Machine Super Intelligence](27-machine-super-intelligence.md) - Defines universal intelligence formally as expected performance across all computable environments, weighted by simplicity, and follows the… (2008)

## Generative Models & Additional Domains

* [28 - Generative Adversarial Nets](28-generative-adversarial-nets.md) - Two networks trained against each other: a generator that produces samples and a discriminator that tries to tell them from real data. The paper that… (2014)
* [29 - Variational Lossy Autoencoder](29-variational-lossy-autoencoder.md) - Combines variational autoencoders with expressive autoregressive decoders and explicit control over what the latent code is allowed to keep, giving… (2016)
* [30 - Neural Message Passing for Quantum Chemistry](30-neural-message-passing-for-quantum-chemistry.md) - Shows that a wide family of graph neural networks is really one message-passing algorithm, and sets a strong benchmark on molecular property… (2017)
