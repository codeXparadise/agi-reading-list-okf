---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/02-the-annotated-transformer.md
source: ../../papers/02-the-annotated-transformer.md
paper_title: The Annotated Transformer
sequence: 2
section: Training Data and Batching
section_role: experiments
section_index: 13
pages: []
topics: ["../../topics/transformer-architecture.md", "../../topics/attention.md"]
description: "We trained on the standard WMT 2014 English-German dataset consisting of about 4.5 million sentence pairs. Sentences were encoded using byte-pair…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Training Data and Batching

> Section 13 of 28 from [02 - The Annotated Transformer](../../papers/02-the-annotated-transformer.md) · `experiments` · pages n/a

We trained on the standard WMT 2014 English-German dataset consisting of about
4.5 million sentence pairs. Sentences were encoded using byte-pair encoding,
which has a shared source-target vocabulary of about 37000 tokens. For English-
French, we used the significantly larger WMT 2014 English-French dataset
consisting of 36M sentences and split tokens into a 32000 word-piece vocabulary.

Sentence pairs were batched together by approximate sequence length. Each
training batch contained a set of sentence pairs containing approximately 25000
source tokens and 25000 target tokens.

> We will use torch text for batching. This is discussed in more detail below.
> Here we create batches in a torchtext function that ensures our batch size
> padded to the maximum batchsize does not surpass a threshold (25000 if we have 8
> gpus).

```python
global max_src_in_batch, max_tgt_in_batch
def batch_size_fn(new, count, sofar):
    "Keep augmenting batch and calculate total number of tokens + padding."
    global max_src_in_batch, max_tgt_in_batch
    if count == 1:
        max_src_in_batch = 0
        max_tgt_in_batch = 0
    max_src_in_batch = max(max_src_in_batch,  len(new.src))
    max_tgt_in_batch = max(max_tgt_in_batch,  len(new.trg) + 2)
    src_elements = count * max_src_in_batch
    tgt_elements = count * max_tgt_in_batch
    return max(src_elements, tgt_elements)
```

## Hardware and Schedule

We trained our models on one machine with 8 NVIDIA P100 GPUs. For our base
models using the hyperparameters described throughout the paper, each training
step took about 0.4 seconds. We trained the base models for a total of 100,000
steps or 12 hours. For our big models, step time was 1.0 seconds. The big
models were trained for 300,000 steps (3.5 days).

---

Full document: [02 - The Annotated Transformer](../../papers/02-the-annotated-transformer.md) · Page-level evidence: [paper-pages/02-the-annotated-transformer](../../paper-pages/02-the-annotated-transformer/index.md)
