---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/02-the-annotated-transformer.md
source: ../../papers/02-the-annotated-transformer.md
paper_title: The Annotated Transformer
sequence: 2
section: Model Architecture
section_role: method
section_index: 4
pages: []
topics: ["../../topics/transformer-architecture.md", "../../topics/attention.md"]
description: "Most competitive neural sequence transduction models have an encoder-decoder structure [(cite)](https://arxiv.org/abs/1409.0473). Here, the encoder…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Model Architecture

> Section 4 of 28 from [02 - The Annotated Transformer](../../papers/02-the-annotated-transformer.md) · `method` · pages n/a

Most competitive neural sequence transduction models have an encoder-decoder
structure [(cite)](https://arxiv.org/abs/1409.0473). Here, the encoder maps an
input sequence of symbol representations (x1,…,xn)(x1,…,xn) to a sequence of
continuous representations z=(z1,…,zn)z=(z1,…,zn). Given zz,
the decoder then generates an output sequence (y1,…,ym)(y1,…,ym) of symbols one
element at a time. At each step the model is auto-regressive
[(cite)](https://arxiv.org/abs/1308.0850), consuming the previously generated
symbols as additional input when generating the next.

```python
class EncoderDecoder(nn.Module):
    """
    A standard Encoder-Decoder architecture. Base for this and many
    other models.
    """
    def __init__(self, encoder, decoder, src_embed, tgt_embed, generator):
        super(EncoderDecoder, self).__init__()
        self.encoder = encoder
        self.decoder = decoder
        self.src_embed = src_embed
        self.tgt_embed = tgt_embed
        self.generator = generator

    def forward(self, src, tgt, src_mask, tgt_mask):
        "Take in and process masked src and target sequences."
        return self.decode(self.encode(src, src_mask), src_mask,
                            tgt, tgt_mask)

    def encode(self, src, src_mask):
        return self.encoder(self.src_embed(src), src_mask)

    def decode(self, memory, src_mask, tgt, tgt_mask):
        return self.decoder(self.tgt_embed(tgt), memory, src_mask, tgt_mask)
```

```python
class Generator(nn.Module):
    "Define standard linear + softmax generation step."
    def __init__(self, d_model, vocab):
        super(Generator, self).__init__()
        self.proj = nn.Linear(d_model, vocab)

    def forward(self, x):
        return F.log_softmax(self.proj(x), dim=-1)
```

The Transformer follows this overall architecture using stacked self-attention
and point-wise, fully connected layers for both the encoder and decoder, shown
in the left and right halves of Figure 1, respectively.

```python
Image(filename='images/ModalNet-21.png')
```

![png](https://nlp.seas.harvard.edu/images/the-annotated-transformer_14_0.png)

---

Full document: [02 - The Annotated Transformer](../../papers/02-the-annotated-transformer.md) · Page-level evidence: [paper-pages/02-the-annotated-transformer](../../paper-pages/02-the-annotated-transformer/index.md)
