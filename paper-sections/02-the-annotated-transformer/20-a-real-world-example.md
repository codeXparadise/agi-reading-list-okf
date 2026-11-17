---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/02-the-annotated-transformer.md
source: ../../papers/02-the-annotated-transformer.md
paper_title: The Annotated Transformer
sequence: 2
section: A Real World Example
section_role: other
section_index: 20
pages: []
topics: ["../../topics/transformer-architecture.md", "../../topics/attention.md"]
description: "Now we consider a real-world example using the IWSLT German-English Translation task. This task is much smaller than the WMT task considered in the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# A Real World Example

> Section 20 of 28 from [02 - The Annotated Transformer](../../papers/02-the-annotated-transformer.md) · `other` · pages n/a

> Now we consider a real-world example using the IWSLT German-English
> Translation task. This task is much smaller than the WMT task considered in the
> paper, but it illustrates the whole system. We also show how to use multi-gpu
> processing to make it really fast.

```python
#!pip install torchtext spacy
#!python -m spacy download en
#!python -m spacy download de
```

---

Full document: [02 - The Annotated Transformer](../../papers/02-the-annotated-transformer.md) · Page-level evidence: [paper-pages/02-the-annotated-transformer](../../paper-pages/02-the-annotated-transformer/index.md)
