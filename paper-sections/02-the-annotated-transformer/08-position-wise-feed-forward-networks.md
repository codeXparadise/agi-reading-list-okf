---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/02-the-annotated-transformer.md
source: ../../papers/02-the-annotated-transformer.md
paper_title: The Annotated Transformer
sequence: 2
section: Position-wise Feed-Forward Networks
section_role: other
section_index: 8
pages: []
topics: ["../../topics/transformer-architecture.md", "../../topics/attention.md"]
description: "In addition to attention sub-layers, each of the layers in our encoder and decoder contains a fully connected feed-forward network, which is applied…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Position-wise Feed-Forward Networks

> Section 8 of 28 from [02 - The Annotated Transformer](../../papers/02-the-annotated-transformer.md) · `other` · pages n/a

In addition to attention sub-layers, each of the layers in our encoder and
decoder contains a fully connected feed-forward network, which is applied to
each position separately and identically. This consists of two linear
transformations with a ReLU activation in between.

FFN(x)=max(0,xW1+b1)W2+b2FFN(x)=max(0,xW1+b1)W2+b2

While the linear transformations are the same across different positions, they
use different parameters from layer to layer. Another way of describing this is
as two convolutions with kernel size 1. The dimensionality of input and output
is dmodel=512dmodel=512, and the inner-layer has dimensionality dff=2048dff=2048.

```python
class PositionwiseFeedForward(nn.Module):
    "Implements FFN equation."
    def __init__(self, d_model, d_ff, dropout=0.1):
        super(PositionwiseFeedForward, self).__init__()
        self.w_1 = nn.Linear(d_model, d_ff)
        self.w_2 = nn.Linear(d_ff, d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        return self.w_2(self.dropout(F.relu(self.w_1(x))))
```

## Embeddings and Softmax

Similarly to other sequence transduction models, we use learned embeddings to
convert the input tokens and output tokens to vectors of dimension
dmodeldmodel. We also use the usual learned linear transformation and
softmax function to convert the decoder output to predicted next-token
probabilities. In our model, we share the same weight matrix between the two
embedding layers and the pre-softmax linear transformation, similar to
[(cite)](https://arxiv.org/abs/1608.05859). In the embedding layers, we multiply
those weights by √dmodeldmodel.

```python
class Embeddings(nn.Module):
    def __init__(self, d_model, vocab):
        super(Embeddings, self).__init__()
        self.lut = nn.Embedding(vocab, d_model)
        self.d_model = d_model

    def forward(self, x):
        return self.lut(x) * math.sqrt(self.d_model)
```

---

Full document: [02 - The Annotated Transformer](../../papers/02-the-annotated-transformer.md) · Page-level evidence: [paper-pages/02-the-annotated-transformer](../../paper-pages/02-the-annotated-transformer/index.md)
