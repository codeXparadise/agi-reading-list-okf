---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/17-simple-neural-network-module-for-relational-reasoning.md
source: ../../papers/17-simple-neural-network-module-for-relational-reasoning.md
paper_title: A Simple Neural Network Module for Relational Reasoning
sequence: 17
section: A Related Work
section_role: other
section_index: 20
pages: [9, 10]
topics: ["../../topics/relational-reasoning.md", "../../topics/graph-neural-networks.md"]
description: "Since the RN is highly versatile, it can be used for visual, text-based, and state-based tasks. As such, it touches upon a broad range of areas in…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# A Related Work

> Section 20 of 22 from [17 - A Simple Neural Network Module for Relational Reasoning](../../papers/17-simple-neural-network-module-for-relational-reasoning.md) · `other` · pages 9-10

Since the RN is highly versatile, it can be used for visual, text-based, and state-based tasks. As such, it touches upon a broad range of areas in machine learning, computer vision, and natural language understanding. Here, we provide a brief overview of some of the most relevant related work.

## Relational reasoning

Relational reasoning is implicit in many symbolic approaches \[11, 32\] and has been explicitly pursued using neural networks as well \[4\]. There is recent work applying neural networks to graphs, which are a natural structure for formalising relations \[12, 19, 33, 37, 26, 2\]. Perhaps a crucial diﬀerence between this work and our work here is that RNs require minimal oversight to produce their input (a set of objects), and can be applied successfully to tasks even when provided with relatively unstructured inputs coming from CNNs and LSTMs. There has also been some recent work on reasoning about sets, although this work does not explicitly reason about the relations of elements within sets \[47\].

## Grounding spatial relations

Although grounding language in spatial percepts has a long-standing tradition, the majority of previous research has focused on either rule-based spatial representations or hand-engineered spatial features \[8, 10, 20, 21, 24, 29, 38, 39\]. Although there are some attempts to learn spatial relations using spatial templates \[28, 30\], these approaches are less versatile than ours.

## Visual question answering

Visual question answering is a recently introduced task that measures a machine understanding of the scene through questions \[1, 29\]. Related to our work, we are mostly interested in the newly introduced CLEVR dataset \[15\] that distills core challenges of the task, namely relational and multi-modal reasoning. The majority of approaches to question answering share the same pipeline \[6, 31, 36\]. First, questions are encoded with recurrent neural networks, and images are encoded with convolutional neural networks. Next, both representations are combined, and the answers are either predicted or generated. Most successful methods also use an attention mechanism that locate important image regions \[5, 44, 45, 46\]. In our work, we follow a similar pipeline, but we use Relation Networks as a powerful reasoning module.

Parallel to our work, two architectures have shown impressive results on the CLEVR dataset \[14, 16\]. Both approaches hinge on compositionality principles, and have shown they are capable of some relational reasoning. However, both require either designing modules, or require direct access to ground-truth programs. The RN module, on the other hand, is conceptually simpler, can readily be combined with basic neural components such as CNNs or LSTMs, can be broadly applied to various tasks, and achieves significantly better results on CLEVR \[15\] than \[14\], and on par with strongly supervised system of \[16\].

## Text-based question answering

Answering text-based questions has long been an active research area in the NLP community \[3, 22, 27, 48\]. Recently, in addition to traditional symbolic-based question answering architectures, we observe a growing interest in neural-based approaches to text based question answering \[34, 42, 43\]. While these architectures rely on ‘memories’, we empirically show that the RN module has similar

10

capabilities, reaching very competitive results on the bAbI dataset \[41\] – a dataset that test reasoning capabilities of text-based question answering models.

## B CLEVR from pixels

Our model (described in Section 4 of the main text) was trained on 70000 scenes from the CLEVR dataset and a total of 699989 questions. Images were first down-sampled to size 128 × 128, then pre-processed with padding to size 136 × 136, followed by random cropping back to size 128 × 128 and slight random rotations between −0.05 and 0.05 rads. We used 10 distributed workers that synchronously updated a central parameter server. Each worker learned with mini-batches of size 64, using the Adam optimizer and a learning rate of 2.5e−4. Dropout of 50% was used on the penultimate layer of the RN. In our best performing model each convolutional layer used 24 kernels of size 3 × 3 and stride 2, batch normalization, and rectified linear units. The model stopped improving in performance after approximately 1.4 million iterations, at which point training was concluded. The model achieved 96.8% accuracy on the validation set. In general, we found that smaller models performed best. For example, 128 hidden unit LSTMs performed better than 256 or 512, and CNNs with 24 kernels were better than CNNs with more kernels, such as 32, 64, or more.

## Failure cases

Although our model gets most answers correct, a closer examination of the failure cases help us to identify limitations of our architecture. In Table 2, we show some examples of CLEVR questions that our model fails to answer correctly, along with the ground-truth answers. Based on our observations, we hypothesize that our architecture fails especially when objects are heavily occluded, or whenever a high precision object position representation is required. We also observe that many failure cases for our model are also challenging for humans.

## C CLEVR from state descriptions

The model that we train on the state description version of CLEVR is similar to the model trained on the pixel version of CLEVR, but without the vision processing module. We used a 256 unit LSTM for question processing and word-lookup embeddings of size 32. For the RN we used a four-layer MLP with 512 units per layer, with ReLU non-linearities for gθ. A three-layer MLP consisting of 512, 1024 (with 2% dropout) and 29 units with ReLU non-linearities was used for fθ. To train the model we used 10 distributed workers that synchronously updated a central parameter server. Each worker learned with mini-batches of size 64, using the Adam optimizer and a learning rate of 1e−4.

---

Full document: [17 - A Simple Neural Network Module for Relational Reasoning](../../papers/17-simple-neural-network-module-for-relational-reasoning.md) · Page-level evidence: [paper-pages/17-simple-neural-network-module-for-relational-reasoning](../../paper-pages/17-simple-neural-network-module-for-relational-reasoning/index.md)
