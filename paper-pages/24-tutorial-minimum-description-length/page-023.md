---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 23
pages: [23]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "and stochastic complexity. It gives an asymptotic expansion of these quantities and interprets them from a compression, a geometric, a Bayesian and a…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 23 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 23 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

and stochastic complexity. It gives an asymptotic expansion of these quantities and interprets them from a compression, a geometric, a Bayesian and a predictive point of view.

– Section 2.7 extends refined MDL to harder model selection problems, and

in doing so reveals the general, unifying idea, which is summarized in Figure 2.4.

– Section 2.8 briefly discusses how to extend MDL to applications beyond

model section.

• Having defined ‘refined MDL’ in Sections 2.6–2.8, the next two sections place it in context:

– Section 2.9 compares MDL to other approaches to inductive inference, most

notably the related but diﬀerent Bayesian approach.

– Section 2.10 discusses perceived as well as real problems with MDL. The

perceived problems relate to MDL’s relation to Occam’s Razor, the real problems relate to the fact that applications of MDL sometimes perform suboptimally in practice.

• Finally, Section 2.11 provides a conclusion.

Reader’s Guide Throughout the text, paragraph headings reflect the most important concepts. Boxes summarize the most important findings. Together, paragraph headings and boxes provide an overview of MDL theory. It is possible to read this chapter without having read the non-technical overview of Chapter 1. However, we strongly recommend reading at least Sections 1.3 and Section 1.4 before embarking on the present chapter.

## 2.2 Information Theory I: Probabilities and Codelengths

This first section is a mini-primer on information theory, focusing on the relationship between probability distributions and codes. A good understanding of this relationship is essential for a good understanding of MDL. After some preliminaries, Section 2.2.1 introduces prefix codes, the type of codes we work with in MDL. These are related to probability distributions in two ways. In Section 2.2.2 we discuss the first relationship, which is related to the Kraft inequality: for every probability mass function P, there exists a code with lengths −log P, and vice versa. Section 2.2.3 discusses the second relationship, related to the information inequality, which says that if the data are

24

---

[previous page](page-022.md) · [next page](page-024.md) · [all pages](index.md)
