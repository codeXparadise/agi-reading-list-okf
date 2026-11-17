---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
section: 1.1 Introduction and Overview
section_role: introduction
section_index: 2
pages: [4, 5]
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "How does one decide among competing explanations of data given limited observations? This is the problem of model selection. It stands out as one of…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 1.1 Introduction and Overview

> Section 2 of 23 from [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · `introduction` · pages 4-5

How does one decide among competing explanations of data given limited observations? This is the problem of model selection. It stands out as one of the most important problems of inductive and statistical inference. The Minimum Description Length (MDL) Principle is a relatively recent method for inductive inference that provides a generic solution to the model selection problem. MDL is based on the following insight: any regularity in the data can be used to compress the data, i.e. to describe it using fewer symbols than the number of symbols needed to describe the data literally. The more regularities there are, the more the data can be compressed. Equating ‘learning’ with ‘finding regularity’, we can therefore say that the more we are able to compress the data, the more we have learned about the data. Formalizing this idea leads to a general theory of inductive inference with several attractive properties:

1. Occam’s Razor MDL chooses a model that trades-oﬀgoodness-of-fit on the observed data with ‘complexity’ or ‘richness’ of the model. As such, MDL embodies a form of Occam’s Razor, a principle that is both intuitively appealing and informally applied throughout all the sciences.

2. No overfitting, automatically MDL procedures automatically and inherently protect against overfitting and can be used to estimate both the parameters and the structure (e.g., number of parameters) of a model. In contrast, to avoid overfitting when estimating the structure of a model, traditional methods such as maximum likelihood must be modified and extended with additional, typically ad hoc principles.

3. Bayesian interpretation MDL is closely related to Bayesian inference, but avoids some of the interpretation diﬃculties of the Bayesian approach1, especially in the realistic case when it is known a priori to the modeler that none of the models under consideration is true. In fact:

5

4. No need for ‘underlying truth’ In contrast to other statistical methods, MDL procedures have a clear interpretation independent of whether or not there exists some underlying ‘true’ model.

5. Predictive interpretation Because data compression is formally equivalent to a form of probabilistic prediction, MDL methods can be interpreted as searching for a model with good predictive performance on unseen data.

In this chapter, we introduce the MDL Principle in an entirely non-technical way, concentrating on its most important applications, model selection and avoiding overfitting. In Section 1.2 we discuss the relation between learning and data compression. Section 1.3 introduces model selection and outlines a first, ‘crude’ version of MDL that can be applied to model selection. Section 1.4 indicates how these ‘crude’ ideas need to be refined to tackle small sample sizes and diﬀerences in model complexity between models with the same number of parameters. Section 1.5 discusses the philosophy underlying MDL, and considers its relation to Occam’s Razor. Section 1.7 briefly discusses the history of MDL. All this is summarized in Section 1.8.

---

Full document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · Page-level evidence: [paper-pages/24-tutorial-minimum-description-length](../../paper-pages/24-tutorial-minimum-description-length/index.md)
