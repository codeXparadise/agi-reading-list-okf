---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/02-the-annotated-transformer.md
source: ../../papers/02-the-annotated-transformer.md
paper_title: The Annotated Transformer
sequence: 2
section: Prelims
section_role: other
section_index: 2
pages: []
topics: ["../../topics/transformer-architecture.md", "../../topics/attention.md"]
description: "python !pip install http://download.pytorch.org/whl/cu80/torch-0.3.0.post4-cp36-cp36m-linuxx8664.whl numpy matplotlib spacy torchtext seaborn python…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Prelims

> Section 2 of 28 from [02 - The Annotated Transformer](../../papers/02-the-annotated-transformer.md) · `other` · pages n/a

```python
## !pip install http://download.pytorch.org/whl/cu80/torch-0.3.0.post4-cp36-cp36m-linux_x86_64.whl numpy matplotlib spacy torchtext seaborn
```

```python
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import math, copy, time
from torch.autograd import Variable
import matplotlib.pyplot as plt
import seaborn
seaborn.set_context(context="talk")
%matplotlib inline
```

Table of Contents

- [Prelims](https://nlp.seas.harvard.edu/2018/04/03/attention.html#prelims)
- [Background](https://nlp.seas.harvard.edu/2018/04/03/attention.html#background)
- [Model Architecture](https://nlp.seas.harvard.edu/2018/04/03/attention.html#model-architecture)
  - [Encoder and Decoder Stacks](https://nlp.seas.harvard.edu/2018/04/03/attention.html#encoder-and-decoder-stacks)
    - [Encoder](https://nlp.seas.harvard.edu/2018/04/03/attention.html#encoder)
    - [Decoder](https://nlp.seas.harvard.edu/2018/04/03/attention.html#decoder)
    - [Attention](https://nlp.seas.harvard.edu/2018/04/03/attention.html#attention)
    - [Applications of Attention in our Model](https://nlp.seas.harvard.edu/2018/04/03/attention.html#applications-of-attention-in-our-model)
  - [Position-wise Feed-Forward Networks](https://nlp.seas.harvard.edu/2018/04/03/attention.html#position-wise-feed-forward-networks)
  - [Embeddings and Softmax](https://nlp.seas.harvard.edu/2018/04/03/attention.html#embeddings-and-softmax)
  - [Positional Encoding](https://nlp.seas.harvard.edu/2018/04/03/attention.html#positional-encoding)
  - [Full Model](https://nlp.seas.harvard.edu/2018/04/03/attention.html#full-model)
- [Training](https://nlp.seas.harvard.edu/2018/04/03/attention.html#training)
  - [Batches and Masking](https://nlp.seas.harvard.edu/2018/04/03/attention.html#batches-and-masking)
  - [Training Loop](https://nlp.seas.harvard.edu/2018/04/03/attention.html#training-loop)
  - [Training Data and Batching](https://nlp.seas.harvard.edu/2018/04/03/attention.html#training-data-and-batching)
  - [Hardware and Schedule](https://nlp.seas.harvard.edu/2018/04/03/attention.html#hardware-and-schedule)
  - [Optimizer](https://nlp.seas.harvard.edu/2018/04/03/attention.html#optimizer)
  - [Regularization](https://nlp.seas.harvard.edu/2018/04/03/attention.html#regularization)
    - [Label Smoothing](https://nlp.seas.harvard.edu/2018/04/03/attention.html#label-smoothing)
- [A First Example](https://nlp.seas.harvard.edu/2018/04/03/attention.html#a-first--example)
  - [Synthetic Data](https://nlp.seas.harvard.edu/2018/04/03/attention.html#synthetic-data)
  - [Loss Computation](https://nlp.seas.harvard.edu/2018/04/03/attention.html#loss-computation)
  - [Greedy Decoding](https://nlp.seas.harvard.edu/2018/04/03/attention.html#greedy-decoding)
- [A Real World Example](https://nlp.seas.harvard.edu/2018/04/03/attention.html#a-real-world-example)
  - [Data Loading](https://nlp.seas.harvard.edu/2018/04/03/attention.html#data-loading)
  - [Iterators](https://nlp.seas.harvard.edu/2018/04/03/attention.html#iterators)
  - [Multi-GPU Training](https://nlp.seas.harvard.edu/2018/04/03/attention.html#multi-gpu-training)
  - [Training the System](https://nlp.seas.harvard.edu/2018/04/03/attention.html#training-the-system)
- [Additional Components: BPE, Search, Averaging](https://nlp.seas.harvard.edu/2018/04/03/attention.html#additional-components-bpe-search-averaging)
- [Results](https://nlp.seas.harvard.edu/2018/04/03/attention.html#results)
  - [Attention Visualization](https://nlp.seas.harvard.edu/2018/04/03/attention.html#attention-visualization)
- [Conclusion](https://nlp.seas.harvard.edu/2018/04/03/attention.html#conclusion)

> My comments are blockquoted. The main text is all from the paper itself.

---

Full document: [02 - The Annotated Transformer](../../papers/02-the-annotated-transformer.md) · Page-level evidence: [paper-pages/02-the-annotated-transformer](../../paper-pages/02-the-annotated-transformer/index.md)
