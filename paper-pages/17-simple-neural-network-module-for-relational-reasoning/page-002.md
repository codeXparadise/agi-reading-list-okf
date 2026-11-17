---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/17-simple-neural-network-module-for-relational-reasoning.md
source: ../../papers/17-simple-neural-network-module-for-relational-reasoning.md
paper_title: A Simple Neural Network Module for Relational Reasoning
sequence: 17
page: 2
pages: [2]
page_of: 16
topics: ["../../topics/relational-reasoning.md", "../../topics/graph-neural-networks.md"]
description: "parameters are learnable synaptic weights, making RNs end-to-end diﬀerentiable. We call the output of gθ a “relation”; therefore, the role of gθ is…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 2 of 16 - A Simple Neural Network Module for Relational Reasoning

> Page 2 of the source PDF, verbatim as extracted. Canonical document: [17 - A Simple Neural Network Module for Relational Reasoning](../../papers/17-simple-neural-network-module-for-relational-reasoning.md)

parameters are learnable synaptic weights, making RNs end-to-end diﬀerentiable. We call the output of gθ a “relation”; therefore, the role of gθ is to infer the ways in which two objects are related, or if they are even related at all.

RNs have three notable strengths: they learn to infer relations, they are data eﬃcient, and they operate on a set of objects – a particularly general and versatile input format – in a manner that is order invariant.

RNs learn to infer relations The functional form in Equation 1 dictates that an RN should consider the potential relations between all object pairs. This implies that an RN is not necessarily privy to which object relations actually exist, nor to the actual meaning of any particular relation. Thus, RNs must learn to infer the existence and implications of object relations.

In graph theory parlance, the input can be thought of as a complete and directed graph whose nodes are objects and whose edges denote the object pairs whose relations should be considered. Although we focus on this “all-to-all” version of the RN throughout this paper, this RN definition can be adjusted to consider only some object pairs. Similar to Interaction Networks \[2\], to which RNs are related, RNs can take as input a list of only those pairs that should be considered, if this information is available. This information could be explicit in the input data, or could perhaps be extracted by some upstream mechanism.

RNs are data eﬃcient RNs use a single function gθ to compute each relation. This can be thought of as a single function operating on a batch of object pairs, where each member of the batch is a particular object-object pair from the same object set. This mode of operation encourages greater generalization for computing relations, since gθ is encouraged not to over-fit to the features of any particular object pair. Consider how an MLP would learn the same function. An MLP would receive all objects from the object set simultaneously as its input. It must then learn and embed n2

(where n is the number of objects) identical functions within its weight parameters to account for all

possible object pairings. This quickly becomes intractable as the number of objects grows. Therefore, the cost of learning a relation function n2 times using a single feedforward pass per sample, as in an MLP, is replaced by the cost of n2 feedforward passes per object set (i.e., for each possible object pair in the set) and learning a relation function just once, as in an RN.

RNs operate on a set of objects The summation in Equation 1 ensures that the RN is invariant to the order of objects in the input. This invariance ensures that the RN’s input respects the property that sets are order invariant, and it ensures that the output is order invariant. Ultimately, this invariance ensures that the RN’s output contains information that is generally representative of the relations that exist in the object set.

## 3 Tasks

We applied RN-augmented networks to a variety of tasks that hinge on relational reasoning. To

demonstrate the versatility of these networks we chose tasks from a number of diﬀerent domains, including visual QA, text-based QA, and dynamic physical systems.

## 3.1 CLEVR

In visual QA a model must learn to answer questions about an image (Figure 1). This is a challenging problem domain because it requires high-level scene understanding \[1, 29\]. Architectures must perform complex relational reasoning – spatial and otherwise – over the features in the visual inputs, language inputs, and their conjunction. However, the majority of visual QA datasets require reasoning in the absence of fully specified word vocabularies, and perhaps more perniciously, a vast and complicated knowledge of the world that is not available in the training data. They also contain ambiguities and exhibit strong linguistic biases that allow a model to learn answering strategies that exploit those biases, without reasoning about the visual input \[1, 31, 36\].

3

---

[previous page](page-001.md) · [next page](page-003.md) · [all pages](index.md)
