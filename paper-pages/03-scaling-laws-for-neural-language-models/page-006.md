---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/03-scaling-laws-for-neural-language-models.md
source: ../../papers/03-scaling-laws-for-neural-language-models.md
paper_title: Scaling Laws for Neural Language Models
sequence: 3
page: 6
pages: [6]
page_of: 30
topics: ["../../topics/scaling-laws.md", "../../topics/transformer-architecture.md", "../../topics/optimization.md"]
description: "Operation Parameters FLOPs per Token Embed (nvocab + nctx) dmodel 4dmodel Attention: QKV nlayerdmodel3dattn 2nlayerdmodel3dattn Attention: Mask —…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 6 of 30 - Scaling Laws for Neural Language Models

> Page 6 of the source PDF, verbatim as extracted. Canonical document: [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md)

## Operation Parameters FLOPs per Token

Embed (nvocab + nctx) dmodel 4dmodel

Attention: QKV nlayerdmodel3dattn 2nlayerdmodel3dattn

Attention: Mask — 2nlayernctxdattn

Attention: Project nlayerdattndmodel 2nlayerdattndembd

Feedforward nlayer2dmodeldﬀ 2nlayer2dmodeldﬀ

De-embed — 2dmodelnvocab

Total (Non-Embedding) N = 2dmodelnlayer (2dattn + dﬀ) Cforward = 2N + 2nlayernctxdattn

Table 1 Parameter counts and compute (forward pass) estimates for a Transformer model. Sub-leading terms such as nonlinearities, biases, and layer normalization are omitted.

For contexts and models with dmodel > nctx/12, the context-dependent computational cost per token is a relatively small fraction of the total compute. Since we primarily study models where dmodel ≫nctx/12, we do not include context-dependent terms in our training compute estimate. Accounting for the backwards pass (approximately twice the compute as the forwards pass), we then define the estimated non-embedding compute as C ≈6N floating point operators per training token.

## 2.2 Training Procedures

Unless otherwise noted, we train models with the Adam optimizer \[KB14\] for a fixed 2.5 × 105 steps with a batch size of 512 sequences of 1024 tokens. Due to memory constraints, our largest models (more than 1B parameters) were trained with Adafactor \[SS18\]. We experimented with a variety of learning rates and schedules, as discussed in Appendix D.6. We found that results at convergence were largely independent of learning rate schedule. Unless otherwise noted, all training runs included in our data used a learning rate schedule with a 3000 step linear warmup followed by a cosine decay to zero.

## 2.3 Datasets

We train our models on an extended version of the WebText dataset described in \[RWC+19\]. The original WebText dataset was a web scrape of outbound links from Reddit through December 2017 which received at least 3 karma. In the second version, WebText2, we added outbound Reddit links from the period of January to October 2018, also with a minimum of 3 karma. The karma threshold served as a heuristic for whether people found the link interesting or useful. The text of the new links was extracted with the Newspaper3k python library. In total, the dataset consists of 20.3M documents containing 96 GB of text and 1.62 × 1010 words (as defined by wc). We then apply the reversible tokenizer described in \[RWC+19\], which yields 2.29 × 1010 tokens. We reserve 6.6 × 108 of these tokens for use as a test set, and we also test on similarlyprepared samples of Books Corpus \[ZKZ+15\], Common Crawl \[Fou\], English Wikipedia, and a collection of publicly-available Internet Books.

## 3 Empirical Results and Basic Power Laws

To characterize language model scaling we train a wide variety of models, varying a number of factors including:

• Model size (ranging in size from 768 to 1.5 billion non-embedding parameters)

• Dataset size (ranging from 22 million to 23 billion tokens)

• Shape (including depth, width, attention heads, and feed-forward dimension)

• Context length (1024 for most runs, though we also experiment with shorter contexts)

• Batch size (219 for most runs, but we also vary it to measure the critical batch size)

---

[previous page](page-005.md) · [next page](page-007.md) · [all pages](index.md)
