---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 4
pages: [4]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "Chapter 1 Introducing the MDL Principle 1.1 Introduction and Overview How does one decide among competing explanations of data given limited…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 4 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 4 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

## Chapter 1

## Introducing the MDL Principle

## 1.1 Introduction and Overview

How does one decide among competing explanations of data given limited observations? This is the problem of model selection. It stands out as one of the most important problems of inductive and statistical inference. The Minimum Description Length (MDL) Principle is a relatively recent method for inductive inference that provides a generic solution to the model selection problem. MDL is based on the following insight: any regularity in the data can be used to compress the data, i.e. to describe it using fewer symbols than the number of symbols needed to describe the data literally. The more regularities there are, the more the data can be compressed. Equating ‘learning’ with ‘finding regularity’, we can therefore say that the more we are able to compress the data, the more we have learned about the data. Formalizing this idea leads to a general theory of inductive inference with several attractive properties:

1. Occam’s Razor MDL chooses a model that trades-oﬀgoodness-of-fit on the observed data with ‘complexity’ or ‘richness’ of the model. As such, MDL embodies a form of Occam’s Razor, a principle that is both intuitively appealing and informally applied throughout all the sciences.

2. No overfitting, automatically MDL procedures automatically and inherently protect against overfitting and can be used to estimate both the parameters and the structure (e.g., number of parameters) of a model. In contrast, to avoid overfitting when estimating the structure of a model, traditional methods such as maximum likelihood must be modified and extended with additional, typically ad hoc principles.

3. Bayesian interpretation MDL is closely related to Bayesian inference, but avoids some of the interpretation diﬃculties of the Bayesian approach1, especially in the realistic case when it is known a priori to the modeler that none of the models under consideration is true. In fact:

5

---

[previous page](page-003.md) · [next page](page-005.md) · [all pages](index.md)
