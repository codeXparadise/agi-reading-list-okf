---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/12-pointer-networks.md
source: ../../papers/12-pointer-networks.md
paper_title: Pointer Networks
sequence: 12
section: 4.1 Architecture and Hyperparameters
section_role: method
section_index: 12
pages: [5]
topics: ["../../topics/sequence-to-sequence.md", "../../topics/attention.md"]
description: "No extensive architecture or hyperparameter search of the Ptr-Net was done in the work presented here, and we used virtually the same architecture…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 4.1 Architecture and Hyperparameters

> Section 12 of 18 from [12 - Pointer Networks](../../papers/12-pointer-networks.md) · `method` · pages 5-5

No extensive architecture or hyperparameter search of the Ptr-Net was done in the work presented here, and we used virtually the same architecture throughout all the experiments and datasets. Even though there are likely some gains to be obtained by tuning the model, we felt that having the same model hyperparameters operate on all the problems would make the main message of the paper stronger.

As a result, all our models used a single layer LSTM with either 256 or 512 hidden units, trained with stochastic gradient descent with a learning rate of 1.0, batch size of 128, random uniform weight initialization from -0.08 to 0.08, and L2 gradient clipping of 2.0. We generated 1M training example pairs, and we did observe overfitting in some cases where the task was simpler (i.e., for small n).

---

Full document: [12 - Pointer Networks](../../papers/12-pointer-networks.md) · Page-level evidence: [paper-pages/12-pointer-networks](../../paper-pages/12-pointer-networks/index.md)
