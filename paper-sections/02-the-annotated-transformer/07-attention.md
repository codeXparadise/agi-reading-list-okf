---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/02-the-annotated-transformer.md
source: ../../papers/02-the-annotated-transformer.md
paper_title: The Annotated Transformer
sequence: 2
section: Attention
section_role: other
section_index: 7
pages: []
topics: ["../../topics/transformer-architecture.md", "../../topics/attention.md"]
description: "An attention function can be described as mapping a query and a set of key-value pairs to an output, where the query, keys, values, and output are…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Attention

> Section 7 of 28 from [02 - The Annotated Transformer](../../papers/02-the-annotated-transformer.md) · `other` · pages n/a

An attention function can be described as mapping a query and a set of key-value
pairs to an output, where the query, keys, values, and output are all vectors.
The output is computed as a weighted sum of the values, where the weight
assigned to each value is computed by a compatibility function of the query with
the corresponding key.

We call our particular attention “Scaled Dot-Product Attention”. The input
consists of queries and keys of dimension dkdk, and values of dimension dvdv.
We compute the dot products of the query with all keys, divide each by
√dkdk, and apply a softmax function to obtain the weights on the values.

```python
Image(filename='images/ModalNet-19.png')
```

![png](https://nlp.seas.harvard.edu/images/the-annotated-transformer_33_0.png)

In practice, we compute the attention function on a set of queries
simultaneously, packed together into a matrix QQ. The keys and values are
also packed together into matrices KK and VV. We compute the matrix of
outputs as:

Attention(Q,K,V)=softmax(QKT√dk)VAttention(Q,K,V)=softmax(QKTdk)V

```python
def attention(query, key, value, mask=None, dropout=None):
    "Compute 'Scaled Dot Product Attention'"
    d_k = query.size(-1)
    scores = torch.matmul(query, key.transpose(-2, -1)) \
             / math.sqrt(d_k)
    if mask is not None:
        scores = scores.masked_fill(mask == 0, -1e9)
    p_attn = F.softmax(scores, dim = -1)
    if dropout is not None:
        p_attn = dropout(p_attn)
    return torch.matmul(p_attn, value), p_attn
```

The two most commonly used attention functions are additive attention
[(cite)](https://arxiv.org/abs/1409.0473), and dot-product (multiplicative)
attention. Dot-product attention is identical to our algorithm, except for the
scaling factor of 1√dk1dk. Additive attention computes the
compatibility function using a feed-forward network with a single hidden layer.
While the two are similar in theoretical complexity, dot-product attention is
much faster and more space-efficient in practice, since it can be implemented
using highly optimized matrix multiplication code.

While for small values of dkdk the two mechanisms perform similarly, additive
attention outperforms dot product attention without scaling for larger values of
dkdk [(cite)](https://arxiv.org/abs/1703.03906). We suspect that for large
values of dkdk, the dot products grow large in magnitude, pushing the softmax
function into regions where it has extremely small gradients (To illustrate why
the dot products get large, assume that the components of qq and kk are
independent random variables with mean 00 and variance 11. Then their dot
product, q⋅k=∑dki=1qikiq⋅k=∑i=1dkqiki, has mean 00 and variance
dkdk.). To counteract this effect, we scale the dot products by
1√dk1dk.

```python
Image(filename='images/ModalNet-20.png')
```

![png](https://nlp.seas.harvard.edu/images/the-annotated-transformer_38_0.png)

Multi-head attention allows the model to jointly attend to information from
different representation subspaces at different positions. With a single
attention head, averaging inhibits this.
MultiHead(Q,K,V)=Concat(head1,...,headh)WOwhereheadi=Attention(QWQi,KWKi,VWVi)MultiHead(Q,K,V)=Concat(head1,...,headh)WOwhereheadi=Attention(QWiQ,KWiK,VWiV)

Where the projections are parameter matrices WQi∈Rdmodel×dkWiQ∈Rdmodel×dk, WKi∈Rdmodel×dkWiK∈Rdmodel×dk, WVi∈Rdmodel×dvWiV∈Rdmodel×dv and WO∈Rhdv×dmodelWO∈Rhdv×dmodel.
In this work we employ h=8h=8 parallel attention layers, or heads. For each of
these we use dk=dv=dmodel/h=64dk=dv=dmodel/h=64. Due to the reduced dimension of
each head, the total computational cost is similar to that of single-head
attention with full dimensionality.

```python
class MultiHeadedAttention(nn.Module):
    def __init__(self, h, d_model, dropout=0.1):
        "Take in model size and number of heads."
        super(MultiHeadedAttention, self).__init__()
        assert d_model % h == 0
        # We assume d_v always equals d_k
        self.d_k = d_model // h
        self.h = h
        self.linears = clones(nn.Linear(d_model, d_model), 4)
        self.attn = None
        self.dropout = nn.Dropout(p=dropout)

    def forward(self, query, key, value, mask=None):
        "Implements Figure 2"
        if mask is not None:
            # Same mask applied to all h heads.
            mask = mask.unsqueeze(1)
        nbatches = query.size(0)

        # 1) Do all the linear projections in batch from d_model => h x d_k
        query, key, value = \
            [l(x).view(nbatches, -1, self.h, self.d_k).transpose(1, 2)\
             for l, x in zip(self.linears, (query, key, value))]

        # 2) Apply attention on all the projected vectors in batch.
        x, self.attn = attention(query, key, value, mask=mask,
                                 dropout=self.dropout)

        # 3) "Concat" using a view and apply a final linear.
        x = x.transpose(1, 2).contiguous() \
             .view(nbatches, -1, self.h * self.d_k)
        return self.linears[-1](x)
```

### Applications of Attention in our Model

The Transformer uses multi-head attention in three different ways:
1) In “encoder-decoder attention” layers, the queries come from the previous
decoder layer, and the memory keys and values come from the output of the
encoder. This allows every position in the decoder to attend over all
positions in the input sequence. This mimics the typical encoder-decoder
attention mechanisms in sequence-to-sequence models such as
[(cite)](https://arxiv.org/abs/1609.08144).

2) The encoder contains self-attention layers. In a self-attention layer all of
the keys, values and queries come from the same place, in this case, the output
of the previous layer in the encoder. Each position in the encoder can attend
to all positions in the previous layer of the encoder.

3) Similarly, self-attention layers in the decoder allow each position in the
decoder to attend to all positions in the decoder up to and including that
position. We need to prevent leftward information flow in the decoder to
preserve the auto-regressive property. We implement this inside of scaled dot-
product attention by masking out (setting to −∞−∞) all values in the input
of the softmax which correspond to illegal connections.

---

Full document: [02 - The Annotated Transformer](../../papers/02-the-annotated-transformer.md) · Page-level evidence: [paper-pages/02-the-annotated-transformer](../../paper-pages/02-the-annotated-transformer/index.md)
