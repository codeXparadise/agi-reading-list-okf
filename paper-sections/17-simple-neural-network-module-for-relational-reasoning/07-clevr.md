---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/17-simple-neural-network-module-for-relational-reasoning.md
source: ../../papers/17-simple-neural-network-module-for-relational-reasoning.md
paper_title: A Simple Neural Network Module for Relational Reasoning
sequence: 17
section: 3.1 CLEVR
section_role: other
section_index: 7
pages: [2, 3]
topics: ["../../topics/relational-reasoning.md", "../../topics/graph-neural-networks.md"]
description: "In visual QA a model must learn to answer questions about an image (Figure 1). This is a challenging problem domain because it requires high-level…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.1 CLEVR

> Section 7 of 22 from [17 - A Simple Neural Network Module for Relational Reasoning](../../papers/17-simple-neural-network-module-for-relational-reasoning.md) · `other` · pages 2-3

In visual QA a model must learn to answer questions about an image (Figure 1). This is a challenging problem domain because it requires high-level scene understanding \[1, 29\]. Architectures must perform complex relational reasoning – spatial and otherwise – over the features in the visual inputs, language inputs, and their conjunction. However, the majority of visual QA datasets require reasoning in the absence of fully specified word vocabularies, and perhaps more perniciously, a vast and complicated knowledge of the world that is not available in the training data. They also contain ambiguities and exhibit strong linguistic biases that allow a model to learn answering strategies that exploit those biases, without reasoning about the visual input \[1, 31, 36\].

3

To control for these issues, and to distill the core challenges of visual QA, the CLEVR visual QA dataset was developed \[15\]. CLEVR contains images of 3D-rendered objects, such as spheres and cylinders (Figure 2). Each image is associated with a number of questions that fall into diﬀerent categories. For example, query attribute questions may ask “What is the color of the sphere?”, while compare attribute questions may ask “Is the cube the same material as the cylinder?”.

For our purposes, an important feature of CLEVR is that many questions are explicitly relational in nature. Remarkably, powerful QA architectures \[46\] are unable to solve CLEVR, presumably because they cannot handle core relational aspects of the task. For example, as reported in the original paper a model comprised of ResNet-101 image embeddings with LSTM question processing and augmented with stacked attention modules vastly outperformed other models at an overall performance of 68.5% (compared to 52.3% for the next best, and 92.6% human performance) \[15\]. However, for compare attribute and count questions (i.e., questions heavily involving relations across objects), the model performed little better than the simplest baseline, which answered questions solely based on the probability of answers in the training set for a given question category (Q-type baseline).

We used two versions of the CLEVR dataset: (i) the pixel version, in which images were represented in standard 2D pixel form, and (ii) a state description version, in which images were explicitly represented by state description matrices containing factored object descriptions. Each row in the matrix contained the features of a single object – 3D coordinates (x, y, z); color (r, g, b); shape (cube, cylinder, etc.); material (rubber, metal, etc.); size (small, large, etc.). When we trained our models, we used either the pixel version or the state description version, depending on the experiment, but not both together.

---

Full document: [17 - A Simple Neural Network Module for Relational Reasoning](../../papers/17-simple-neural-network-module-for-relational-reasoning.md) · Page-level evidence: [paper-pages/17-simple-neural-network-module-for-relational-reasoning](../../paper-pages/17-simple-neural-network-module-for-relational-reasoning/index.md)
