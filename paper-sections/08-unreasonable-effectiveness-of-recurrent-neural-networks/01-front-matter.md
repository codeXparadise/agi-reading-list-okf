---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md
source: ../../papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md
paper_title: The Unreasonable Effectiveness of Recurrent Neural Networks
sequence: 8
section: Front matter
section_role: front-matter
section_index: 1
pages: []
topics: ["../../topics/recurrent-neural-networks.md"]
description: "The text below was extracted from the published source (web article) on 2026-11-17. The published blog post, converted to markdown; code samples and…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Front matter

> Section 1 of 10 from [08 - The Unreasonable Effectiveness of Recurrent Neural Networks](../../papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md) · `front-matter` · pages n/a

The text below was extracted from the published source (web article) on 2026-11-17. The published blog post, converted to markdown; code samples and generated-text examples are kept verbatim.

There’s something magical about Recurrent Neural Networks (RNNs). I still remember when I trained my first recurrent network for [Image Captioning](http://cs.stanford.edu/people/karpathy/deepimagesent/). Within a few dozen minutes of training my first baby model (with rather arbitrarily-chosen hyperparameters) started to generate very nice looking descriptions of images that were on the edge of making sense. Sometimes the ratio of how simple your model is to the quality of the results you get out of it blows past your expectations, and this was one of those times. What made this result so shocking at the time was that the common wisdom was that RNNs were supposed to be difficult to train (with more experience I’ve in fact reached the opposite conclusion). Fast forward about a year: I’m training RNNs all the time and I’ve witnessed their power and robustness many times, and yet their magical outputs still find ways of amusing me. This post is about sharing some of that magic with you.

> We’ll train RNNs to generate text character by character and ponder the question “how is that even possible?”

By the way, together with this post I am also releasing [code on Github](https://github.com/karpathy/char-rnn) that allows you to train character-level language models based on multi-layer LSTMs. You give it a large chunk of text and it will learn to generate text like it one character at a time. You can also use it to reproduce my experiments below. But we’re getting ahead of ourselves; What are RNNs anyway?

---

Full document: [08 - The Unreasonable Effectiveness of Recurrent Neural Networks](../../papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md) · Page-level evidence: [paper-pages/08-unreasonable-effectiveness-of-recurrent-neural-networks](../../paper-pages/08-unreasonable-effectiveness-of-recurrent-neural-networks/index.md)
