---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/17-simple-neural-network-module-for-relational-reasoning.md
source: ../../papers/17-simple-neural-network-module-for-relational-reasoning.md
paper_title: A Simple Neural Network Module for Relational Reasoning
sequence: 17
section: 3.2 Sort-of-CLEVR
section_role: other
section_index: 8
pages: [3]
topics: ["../../topics/relational-reasoning.md", "../../topics/graph-neural-networks.md"]
description: "To explore our hypothesis that the RN architecture is better suited to general relational reasoning as compared to more standard neural…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.2 Sort-of-CLEVR

> Section 8 of 22 from [17 - A Simple Neural Network Module for Relational Reasoning](../../papers/17-simple-neural-network-module-for-relational-reasoning.md) · `other` · pages 3-3

To explore our hypothesis that the RN architecture is better suited to general relational reasoning as compared to more standard neural architectures, we constructed a dataset similar to CLEVR that we call “Sort-of-CLEVR”1. This dataset separates relational and non-relational questions.

Sort-of-CLEVR consists of images of 2D colored shapes along with questions and answers about the images. Each image has a total of 6 objects, where each object is a randomly chosen shape (square or circle). We used 6 colors (red, blue, green, orange, yellow, gray) to unambiguously identify

each object. Questions are hard-coded as fixed-length binary strings to reduce the diﬃculty involved with natural language question-word processing, and thereby remove any confounding diﬃculty with language parsing. For each image we generated 10 relational questions and 10 non-relational questions. Examples of relational questions are: “What is the shape of the object that is farthest from the gray object?”; and “How many objects have the same shape as the green object?”. Examples of

non-relational questions are: “What is the shape of the gray object?”; and “Is the blue object on the top or bottom of the scene?”. The dataset is also visually simple, reducing complexities involved in

image processing.

---

Full document: [17 - A Simple Neural Network Module for Relational Reasoning](../../papers/17-simple-neural-network-module-for-relational-reasoning.md) · Page-level evidence: [paper-pages/17-simple-neural-network-module-for-relational-reasoning](../../paper-pages/17-simple-neural-network-module-for-relational-reasoning/index.md)
