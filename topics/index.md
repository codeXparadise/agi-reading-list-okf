# Topics

Cross-cutting ideas that appear across several papers. Each topic lists the papers that develop it.

## By subject

* [Attention](attention.md) - A mechanism that lets a model weight the parts of its input it should look at, instead of compressing everything into one state vector.
* [Transformer Architecture](transformer-architecture.md) - The self-attention stack - multi-head attention, positional encodings, residual streams and layer norm - that underpins modern language models.
* [Scaling Laws](scaling-laws.md) - Empirical power-law relationships between loss and model size, data size and compute.
* [Convolutional Networks](convolutional-networks.md) - Weight-sharing architectures built for grid-structured data such as images.
* [Residual Connections](residual-connections.md) - Identity shortcuts that let gradients flow through very deep networks.
* [Recurrent Neural Networks](recurrent-neural-networks.md) - Networks that process a sequence one step at a time while carrying a hidden state.
* [Long Short-Term Memory](long-short-term-memory.md) - A gated recurrent cell designed to preserve information over long spans.
* [Sequence to Sequence](sequence-to-sequence.md) - Encoder-decoder models that map one sequence to another of arbitrary length.
* [Machine Translation](machine-translation.md) - Translating text between languages; historically the benchmark that drove sequence modelling.
* [Speech Recognition](speech-recognition.md) - Mapping audio to text end-to-end with neural networks.
* [Memory-Augmented Networks](memory-augmented-networks.md) - Models with an explicit memory they learn to read and write.
* [Relational Reasoning](relational-reasoning.md) - Reasoning explicitly over the relations between pairs or groups of entities rather than over their raw features.
* [Graph Neural Networks](graph-neural-networks.md) - Networks that compute over graphs by passing messages between nodes.
* [Optimization](optimization.md) - The algorithms that decide how weights move in response to gradients.
* [Regularization](regularization.md) - Techniques that trade training fit for generalisation.
* [Minimum Description Length](minimum-description-length.md) - The principle that the best model is the one that compresses the data shortest.
* [Kolmogorov Complexity](kolmogorov-complexity.md) - The length of the shortest program that produces a given object.
* [Generative Models](generative-models.md) - Models that learn a data distribution and can sample from it.
* [Pipeline Parallelism](pipeline-parallelism.md) - Splitting a model across devices by layer and streaming micro-batches through the split.
