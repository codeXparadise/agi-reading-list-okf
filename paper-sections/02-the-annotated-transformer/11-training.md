---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/02-the-annotated-transformer.md
source: ../../papers/02-the-annotated-transformer.md
paper_title: The Annotated Transformer
sequence: 2
section: Training
section_role: experiments
section_index: 11
pages: []
topics: ["../../topics/transformer-architecture.md", "../../topics/attention.md"]
description: "This section describes the training regime for our models. We stop for a quick interlude to introduce some of the tools needed to train a standard…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Training

> Section 11 of 28 from [02 - The Annotated Transformer](../../papers/02-the-annotated-transformer.md) · `experiments` · pages n/a

This section describes the training regime for our models.

> We stop for a quick interlude to introduce some of the tools
> needed to train a standard encoder decoder model. First we define a batch object
> that holds the src and target sentences for training, as well as constructing
> the masks.

## Batches and Masking

```python
class Batch:
    "Object for holding a batch of data with mask during training."
    def __init__(self, src, trg=None, pad=0):
        self.src = src
        self.src_mask = (src != pad).unsqueeze(-2)
        if trg is not None:
            self.trg = trg[:, :-1]
            self.trg_y = trg[:, 1:]
            self.trg_mask = \
                self.make_std_mask(self.trg, pad)
            self.ntokens = (self.trg_y != pad).data.sum()

    @staticmethod
    def make_std_mask(tgt, pad):
        "Create a mask to hide padding and future words."
        tgt_mask = (tgt != pad).unsqueeze(-2)
        tgt_mask = tgt_mask & Variable(
            subsequent_mask(tgt.size(-1)).type_as(tgt_mask.data))
        return tgt_mask
```

> Next we create a generic training and scoring function to keep track of loss.
> We pass in a generic loss compute function that also handles parameter updates.

---

Full document: [02 - The Annotated Transformer](../../papers/02-the-annotated-transformer.md) · Page-level evidence: [paper-pages/02-the-annotated-transformer](../../paper-pages/02-the-annotated-transformer/index.md)
