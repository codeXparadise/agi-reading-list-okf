---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
section: 2.1 Plan of the Tutorial
section_role: other
section_index: 10
pages: [22, 23]
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "In Chapter 1 we introduced the MDL Principle in an informal way. In this chapter we give an introduction to MDL that is mathematically precise.…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.1 Plan of the Tutorial

> Section 10 of 23 from [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · `other` · pages 22-23

In Chapter 1 we introduced the MDL Principle in an informal way. In this chapter we give an introduction to MDL that is mathematically precise. Throughout the text, we assume some basic familiarity with probability theory. While some prior exposure to basic statistics is highly useful, it is not required. The chapter can be read without any prior knowledge of information theory. The tutorial is organized according to the following plan:

• The first two sections are of a preliminary nature:

– Any understanding of MDL requires some minimal knowledge of information

theory – in particular the relationship between probability distributions and codes. This relationship is explained in Section 2.2.

– Relevant statistical notions such as ‘maximum likelihood estimation’ are

reviewed in Section 2.3. There we also introduce the Markov chain model which will serve as an example model throughout the text.

• Based on this preliminary material, in Section 2.4 we formalize a simple version of the MDL Principle, called the crude two-part MDL Principle in this text. We explain why, for successful practical applications, crude MDL needs to be refined.

• Section 2.5 is once again preliminary: it discusses universal coding, the informationtheoretic concept underlying refined versions of MDL.

• Sections 2.6–2.8 define and discuss refined MDL. They are the key sections of the tutorial:

– Section 2.6 discusses basic refined MDL for comparing a finite number of

simple statistical models and introduces the central concepts of parametric

23

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

---

Full document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · Page-level evidence: [paper-pages/24-tutorial-minimum-description-length](../../paper-pages/24-tutorial-minimum-description-length/index.md)
