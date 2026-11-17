---
okf_version: "0.2"
---

# The 30 Papers to AI Mastery - an OKF knowledge bundle

A structured, agent-readable knowledge base built from the 30-paper AI reading list curated by @rachit.speaks, the list Ilya Sutskever is reported to have handed to John Carmack. Every paper has its own concept document with the full extracted text, its figures, provenance and its relationships to the rest of the list.

## Start here

* [README](README.md) - what this bundle is, and how it was built
* [Agent guide](AGENTS.md) - how an agent should traverse, cite and answer from this bundle
* [Orientation in Seven Days](reading-paths/orientation-seven-days.md) - the fastest route through all 30

## Papers

* [Core Architecture & Transformers](sections/01-core-architecture-and-transformers.md) - The Transformer and the convolutional architectures that preceded and surround it: attention, scaling behaviour, ResNets and dilated convolutions. (7 papers: 01-07)
* [Recurrent Neural Networks](sections/02-recurrent-neural-networks.md) - Sequence modelling before and alongside attention: RNNs, LSTMs, regularisation, pointer networks, attention-based translation and end-to-end speech. (8 papers: 08-15)
* [Reasoning & External Memory](sections/03-reasoning-and-external-memory.md) - Giving a network somewhere to write and something to reason over: differentiable memory and relational reasoning modules. (3 papers: 16-18)
* [Theory, Complexity & Optimization](sections/04-theory-complexity-and-optimization.md) - How models are trained and why they generalise: optimisers, regularisation, scaling systems, minimum description length, Kolmogorov complexity and the theory of intelligence. (9 papers: 19-27)
* [Generative Models & Additional Domains](sections/05-generative-models-and-additional-domains.md) - Generating data rather than labelling it, and applying message passing to scientific domains. (3 papers: 28-30)

## Browse

* [All papers](papers/index.md) - the full 30 in reading order
* [Topics](topics/index.md) - 19 cross-cutting concepts: attention, scaling laws, MDL, Kolmogorov complexity, memory and more
* [People](people/index.md) - the researchers behind the list
* [Reading paths](reading-paths/index.md) - three curated routes through the material
* [References](references/index.md) - the original reading list and provenance
* [Assets](assets/) - figures extracted from the PDFs

## Conformance

This bundle targets Open Knowledge Format v0.2. Every concept document carries YAML frontmatter with a `type`, every directory has an `index.md`, and the history of the bundle is in [log.md](log.md). Validate it with `python tools/validate_okf.py`.