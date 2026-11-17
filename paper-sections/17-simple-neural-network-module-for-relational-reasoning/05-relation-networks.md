---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/17-simple-neural-network-module-for-relational-reasoning.md
source: ../../papers/17-simple-neural-network-module-for-relational-reasoning.md
paper_title: A Simple Neural Network Module for Relational Reasoning
sequence: 17
section: 2 Relation Networks
section_role: other
section_index: 5
pages: [1, 2]
topics: ["../../topics/relational-reasoning.md", "../../topics/graph-neural-networks.md"]
description: "An RN is a neural network module with a structure primed for relational reasoning. The design philosophy behind RNs is to constrain the functional…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2 Relation Networks

> Section 5 of 22 from [17 - A Simple Neural Network Module for Relational Reasoning](../../papers/17-simple-neural-network-module-for-relational-reasoning.md) · `other` · pages 1-2

An RN is a neural network module with a structure primed for relational reasoning. The design philosophy behind RNs is to constrain the functional form of a neural network so that it captures the core common properties of relational reasoning. In other words, the capacity to compute relations is baked into the RN architecture without needing to be learned, just as the capacity to reason about spatial, translation invariant properties is built-in to CNNs, and the capacity to reason about sequential dependencies is built into recurrent neural networks.

In its simplest form the RN is a composite function:





X

RN(O) = fφ

gθ(oi, oj)

, (1)

i,j

where the input is a set of “objects” O = {o1, o2, ..., on}, oi ∈Rm is the ith object, and fφ and gθ are functions with parameters φ and θ, respectively. For our purposes, fφ and gθ are MLPs, and the

2

parameters are learnable synaptic weights, making RNs end-to-end diﬀerentiable. We call the output of gθ a “relation”; therefore, the role of gθ is to infer the ways in which two objects are related, or if they are even related at all.

RNs have three notable strengths: they learn to infer relations, they are data eﬃcient, and they operate on a set of objects – a particularly general and versatile input format – in a manner that is order invariant.

RNs learn to infer relations The functional form in Equation 1 dictates that an RN should consider the potential relations between all object pairs. This implies that an RN is not necessarily privy to which object relations actually exist, nor to the actual meaning of any particular relation. Thus, RNs must learn to infer the existence and implications of object relations.

In graph theory parlance, the input can be thought of as a complete and directed graph whose nodes are objects and whose edges denote the object pairs whose relations should be considered. Although we focus on this “all-to-all” version of the RN throughout this paper, this RN definition can be adjusted to consider only some object pairs. Similar to Interaction Networks \[2\], to which RNs are related, RNs can take as input a list of only those pairs that should be considered, if this information is available. This information could be explicit in the input data, or could perhaps be extracted by some upstream mechanism.

RNs are data eﬃcient RNs use a single function gθ to compute each relation. This can be thought of as a single function operating on a batch of object pairs, where each member of the batch is a particular object-object pair from the same object set. This mode of operation encourages greater generalization for computing relations, since gθ is encouraged not to over-fit to the features of any particular object pair. Consider how an MLP would learn the same function. An MLP would receive all objects from the object set simultaneously as its input. It must then learn and embed n2

(where n is the number of objects) identical functions within its weight parameters to account for all

possible object pairings. This quickly becomes intractable as the number of objects grows. Therefore, the cost of learning a relation function n2 times using a single feedforward pass per sample, as in an MLP, is replaced by the cost of n2 feedforward passes per object set (i.e., for each possible object pair in the set) and learning a relation function just once, as in an RN.

RNs operate on a set of objects The summation in Equation 1 ensures that the RN is invariant to the order of objects in the input. This invariance ensures that the RN’s input respects the property that sets are order invariant, and it ensures that the output is order invariant. Ultimately, this invariance ensures that the RN’s output contains information that is generally representative of the relations that exist in the object set.

---

Full document: [17 - A Simple Neural Network Module for Relational Reasoning](../../papers/17-simple-neural-network-module-for-relational-reasoning.md) · Page-level evidence: [paper-pages/17-simple-neural-network-module-for-relational-reasoning](../../paper-pages/17-simple-neural-network-module-for-relational-reasoning/index.md)
