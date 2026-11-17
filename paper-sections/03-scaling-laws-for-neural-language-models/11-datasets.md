---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/03-scaling-laws-for-neural-language-models.md
source: ../../papers/03-scaling-laws-for-neural-language-models.md
paper_title: Scaling Laws for Neural Language Models
sequence: 3
section: 2.3 Datasets
section_role: other
section_index: 11
pages: [6]
topics: ["../../topics/scaling-laws.md", "../../topics/transformer-architecture.md", "../../topics/optimization.md"]
description: "We train our models on an extended version of the WebText dataset described in [RWC+19]. The original WebText dataset was a web scrape of outbound…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.3 Datasets

> Section 11 of 45 from [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md) · `other` · pages 6-6

We train our models on an extended version of the WebText dataset described in \[RWC+19\]. The original WebText dataset was a web scrape of outbound links from Reddit through December 2017 which received at least 3 karma. In the second version, WebText2, we added outbound Reddit links from the period of January to October 2018, also with a minimum of 3 karma. The karma threshold served as a heuristic for whether people found the link interesting or useful. The text of the new links was extracted with the Newspaper3k python library. In total, the dataset consists of 20.3M documents containing 96 GB of text and 1.62 × 1010 words (as defined by wc). We then apply the reversible tokenizer described in \[RWC+19\], which yields 2.29 × 1010 tokens. We reserve 6.6 × 108 of these tokens for use as a test set, and we also test on similarlyprepared samples of Books Corpus \[ZKZ+15\], Common Crawl \[Fou\], English Wikipedia, and a collection of publicly-available Internet Books.

---

Full document: [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md) · Page-level evidence: [paper-pages/03-scaling-laws-for-neural-language-models](../../paper-pages/03-scaling-laws-for-neural-language-models/index.md)
