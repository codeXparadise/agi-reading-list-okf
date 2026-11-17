---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/02-the-annotated-transformer.md
source: ../../papers/02-the-annotated-transformer.md
paper_title: The Annotated Transformer
sequence: 2
section: "Additional Components: BPE, Search, Averaging"
section_role: other
section_index: 25
pages: []
topics: ["../../topics/transformer-architecture.md", "../../topics/attention.md"]
description: "So this mostly covers the transformer model itself. There are four aspects that we didn’t cover explicitly. We also have all these additional…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Additional Components: BPE, Search, Averaging

> Section 25 of 28 from [02 - The Annotated Transformer](../../papers/02-the-annotated-transformer.md) · `other` · pages n/a

> So this mostly covers the transformer model itself. There are four aspects
> that we didn’t cover explicitly. We also have all these additional features
> implemented in [OpenNMT-py](https://github.com/opennmt/opennmt-py).

> 1) BPE/ Word-piece: We can use a library to first preprocess the data into
> subword units. See Rico Sennrich’s [subword-\\
> nmt](https://github.com/rsennrich/subword-nmt) implementation. These models will
> transform the training data to look like this:

▁Die ▁Protokoll datei ▁kann ▁ heimlich ▁per ▁E - Mail ▁oder ▁FTP ▁an ▁einen
▁bestimmte n ▁Empfänger ▁gesendet ▁werden .

> 2) Shared Embeddings: When using BPE with shared vocabulary we can share the
> same weight vectors between the source / target / generator. See the
> [(cite)](https://arxiv.org/abs/1608.05859) for details. To add this to the model
> simply do this:

```python
if False:
    model.src_embed[0].lut.weight = model.tgt_embeddings[0].lut.weight
    model.generator.lut.weight = model.tgt_embed[0].lut.weight
```

> 3) Beam Search: This is a bit too complicated to cover here. See the [OpenNMT-\\
> py](https://github.com/OpenNMT/OpenNMT-py/blob/master/onmt/translate/Beam.py)
> for a pytorch implementation.

> 4) Model Averaging: The paper averages the last k checkpoints to create an
> ensembling effect. We can do this after the fact if we have a bunch of models:

```python
def average(model, models):
    "Average models into model"
    for ps in zip(*[m.params() for m in [model] + models]):
        p[0].copy_(torch.sum(*ps[1:]) / len(ps[1:]))
```

---

Full document: [02 - The Annotated Transformer](../../papers/02-the-annotated-transformer.md) · Page-level evidence: [paper-pages/02-the-annotated-transformer](../../paper-pages/02-the-annotated-transformer/index.md)
