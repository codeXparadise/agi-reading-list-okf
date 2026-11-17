---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/16-neural-turing-machines.md
source: ../../papers/16-neural-turing-machines.md
paper_title: Neural Turing Machines
sequence: 16
page: 3
pages: [3]
page_of: 26
topics: ["../../topics/memory-augmented-networks.md", "../../topics/recurrent-neural-networks.md"]
description: "structure within a connectionist framework. Our architecture draws on and potentiates this work. Recursive processing of variable-length structures…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 3 of 26 - Neural Turing Machines

> Page 3 of the source PDF, verbatim as extracted. Canonical document: [16 - Neural Turing Machines](../../papers/16-neural-turing-machines.md)

structure within a connectionist framework. Our architecture draws on and potentiates this work.

Recursive processing of variable-length structures continues to be regarded as a hallmark of human cognition. In the last decade, a firefight in the linguistics community staked several leaders of the field against one another. At issue was whether recursive processing is the “uniquely human” evolutionary innovation that enables language and is specialized to language, a view supported by Fitch, Hauser, and Chomsky (Fitch et al., 2005), or whether multiple new adaptations are responsible for human language evolution and recursive processing predates language (Jackendoff and Pinker, 2005). Regardless of recursive processing’s evolutionary origins, all agreed that it is essential to human cognitive flexibility.

## 2.3 Recurrent Neural Networks

Recurrent neural networks constitute a broad class of machines with dynamic state; that is, they have state whose evolution depends both on the input to the system and on the current state. In comparison to hidden Markov models, which also contain dynamic state, RNNs have a distributed state and therefore have significantly larger and richer memory and computational capacity. Dynamic state is crucial because it affords the possibility of context-dependent computation; a signal entering at a given moment can alter the behaviour of the network at a much later moment.

A crucial innovation to recurrent networks was the Long Short-Term Memory (LSTM) (Hochreiter and Schmidhuber, 1997). This very general architecture was developed for a specific purpose, to address the “vanishing and exploding gradient” problem (Hochreiter et al., 2001a), which we might relabel the problem of “vanishing and exploding sensitivity.” LSTM ameliorates the problem by embedding perfect integrators (Seung, 1998) for memory storage in the network. The simplest example of a perfect integrator is the equation x(t + 1) = x(t) + i(t), where i(t) is an input to the system. The implicit identity matrix Ix(t) means that signals do not dynamically vanish or explode. If we attach a mechanism to this integrator that allows an enclosing network to choose when the integrator listens to inputs, namely, a programmable gate depending on context, we have an equation of the form x(t + 1) = x(t) + g(context)i(t). We can now selectively store information for an indefinite length of time.

Recurrent networks readily process variable-length structures without modification. In sequential problems, inputs to the network arrive at different times, allowing variablelength or composite structures to be processed over multiple steps. Because they natively handle variable-length structures, they have recently been used in a variety of cognitive problems, including speech recognition (Graves et al., 2013; Graves and Jaitly, 2014), text generation (Sutskever et al., 2011), handwriting generation (Graves, 2013) and machine translation (Sutskever et al., 2014). Considering this property, we do not feel that it is urgent or even necessarily valuable to build explicit parse trees to merge composite structures greedily (Pollack, 1990) (Socher et al., 2012) (Frasconi et al., 1998).

Other important precursors to our work include differentiable models of attention (Graves,

4

---

[previous page](page-002.md) · [next page](page-004.md) · [all pages](index.md)
