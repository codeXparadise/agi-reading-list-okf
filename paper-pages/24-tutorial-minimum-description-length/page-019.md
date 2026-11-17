---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 19
pages: [19]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "time and [Rissanen 1987], introducing the Bayesian mixture codes into MDL. This led to the development of the notion of stochastic complexity as the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 19 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 19 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

time and \[Rissanen 1987\], introducing the Bayesian mixture codes into MDL. This led to the development of the notion of stochastic complexity as the shortest codelength of the data given a model \[Rissanen 1986; Rissanen 1987\]. However, the connection to Shtarkov’s normalized maximum likelihood code was not made until 1996, and this prevented the full development of the notion of ‘parametric complexity’. In the mean time, in his impressive Ph.D. thesis, Barron \[1985\] showed how a specific version of the two-part code criterion has excellent frequentist statistical consistency properties. This was extended by Barron and Cover \[1991\] who achieved a breakthrough for two-part codes: they gave clear prescriptions on how to design codes for hypotheses, relating codes with good minimax codelength properties to rates of convergence in statistical consistency theorems. Some of the ideas of Rissanen \[1987\] and Barron and Cover \[1991\] were, as it were, unified when Rissanen \[1996\] introduced a new definition of stochastic complexity based on the normalized maximum likelihood code (Section 2.5). The resulting theory was summarized for the first time by Barron, Rissanen, and Yu \[1998\], and is called ‘refined MDL’ in the present overview.

## 1.8 Summary and Outlook

We discussed how regularity is related to data compression, and how MDL employs this connection by viewing learning in terms of data compression. One can make this precise in several ways; in idealized MDL one looks for the shortest program that generates the given data. This approach is not feasible in practice, and here we concern ourselves with practical MDL. Practical MDL comes in a crude version based on two-part codes and in a modern, more refined version based on the concept of universal coding. The basic ideas underlying all these approaches can be found in the boxes spread throughout the text.

These methods are mostly applied to model selection but can also be used for other problems of inductive inference. In contrast to most existing statistical methodology, they can be given a clear interpretation irrespective of whether or not there exists some ‘true’ distribution generating data – inductive inference is seen as a search for regular properties in (interesting statistics of) the data, and there is no need to assume anything outside the model and the data. In contrast to what is sometimes thought, there is no implicit belief that ‘simpler models are more likely to be true’ – MDL does embody a preference for ‘simple’ models, but this is best seen as a strategy for inference that can be useful even if the environment is not simple at all.

In the next chapter, we make precise both the crude and the refined versions of practical MDL. For this, it is absolutely essential that the reader familiarizes him- or herself with two basic notions of coding and information theory: the relation between codelength functions and probability distributions, and (for refined MDL), the idea of universal coding – a large part of the chapter will be devoted to these.

20

---

[previous page](page-018.md) · [next page](page-020.md) · [all pages](index.md)
