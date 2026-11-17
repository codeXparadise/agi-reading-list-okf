---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/18-relational-recurrent-neural-networks.md
source: ../../papers/18-relational-recurrent-neural-networks.md
paper_title: Relational Recurrent Neural Networks
sequence: 18
section: 2 Relational reasoning
section_role: other
section_index: 4
pages: [1]
topics: ["../../topics/relational-reasoning.md", "../../topics/memory-augmented-networks.md", "../../topics/recurrent-neural-networks.md"]
description: "We take relational reasoning to be the process of understanding the ways in which entities are connected and using this understanding to accomplish…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2 Relational reasoning

> Section 4 of 25 from [18 - Relational Recurrent Neural Networks](../../papers/18-relational-recurrent-neural-networks.md) · `other` · pages 1-1

We take relational reasoning to be the process of understanding the ways in which entities are connected and using this understanding to accomplish some higher order goal \[8\]. For example, consider sorting the distances of various trees to a park bench: the relations (distances) between the entities (trees and bench) are compared and contrasted to produce the solution, which could not be reached if one reasoned about the properties (positions) of each individual entity in isolation.

Since we can often quite fluidly define what constitutes an “entity” or a “relation”, one can imagine a spectrum of neural network inductive biases that can be cast in the language of relational reasoning 1. For example, a convolutional kernel can be said to compute a relation (linear combination) of the entities (pixels) within a receptive field. Some previous approaches make the relational inductive bias more explicit: in message passing neural networks \[e.g. 9–12\], the nodes comprise the entities and relations are computed using learnable functions applied to nodes connected with an edge, or sometimes reducing the relational function to a weighted sum of the source entities \[e.g. 13, 14\]. In Relation Networks \[15–17\] entities are obtained by exploiting spatial locality in the input image, and the model focuses on computing binary relations between each entity pair. Even further, some approaches emphasize that more capable reasoning may be possible by employing simple computational principles; by recognizing that relations might not always be tied to proximity in space, non-local computations may be better able to capture the relations between entities located far away from each other \[18, 19\].

In the temporal domain relational reasoning could comprise a capacity to compare and contrast information seen at different points in time \[20\]. Here, attention mechanisms \[e.g. 21, 22\] implicitly perform some form of relational reasoning; if previous hidden states are interpreted as entities, then computing a weighted sum of entities using attention helps to remove the locality bias present in vanilla RNNs, allowing embeddings to be better related using content rather than proximity.

Since our current architectures solve complicated temporal tasks they must have some capacity for temporal relational reasoning. However, it is unclear whether their inductive biases are limiting, and whether these limitations can be exposed with tasks demanding particular types of temporal relational reasoning. For example, memory-augmented neural networks \[4–7\] solve a compartmentalization problem with a slot-based memory matrix, but may have a harder time allowing memories to interact, or relate, with one another once they are encoded. LSTMs \[3, 23\], on the other hand, pack all information into a common hidden memory vector, potentially making compartmentalization and relational reasoning more difficult.

---

Full document: [18 - Relational Recurrent Neural Networks](../../papers/18-relational-recurrent-neural-networks.md) · Page-level evidence: [paper-pages/18-relational-recurrent-neural-networks](../../paper-pages/18-relational-recurrent-neural-networks/index.md)
