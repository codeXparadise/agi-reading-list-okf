---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
section: Front matter
section_role: front-matter
section_index: 1
pages: [1, 2, 3, 4]
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "The text below was extracted programmatically from the published PDF, page by page, with figures kept inline where they appear. comments mark the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Front matter

> Section 1 of 23 from [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · `front-matter` · pages 1-4

The text below was extracted programmatically from the published PDF, page by page, with figures kept inline where they appear. `<!-- page N -->` comments mark the original page boundaries. Mathematical notation is preserved as plain text rather than LaTeX, so equations read approximately rather than exactly.[^original]

## A Tutorial Introduction to the Minimum Description Length Principle

Peter Gr¨unwald Centrum voor Wiskunde en Informatica

Kruislaan 413, 1098 SJ Amsterdam

The Netherlands

pdg@cwi.nl www.grunwald.nl

Abstract

This tutorial provides an overview of and introduction to Rissanen’s Minimum Description Length (MDL) Principle. The first chapter provides a conceptual, entirely non-technical introduction to the subject. It serves as a basis for the technical introduction given in the second chapter, in which all the ideas of the first chapter are made mathematically precise. This tutorial will appear as the first two chapters in the collection Advances in Minimum Description Length: Theory and Applications \[Gr¨unwald, Myung, and Pitt 2004\], to be published by the MIT Press.

## Contents

1 Introducing MDL 5 1.1 Introduction and Overview . . . . . . . . . . . . . . . . . . . . . . . . . 5 1.2 The Fundamental Idea: Learning as Data Compression . . . . . . . . . . . . . . . . . . . . . . . 6 1.2.1 Kolmogorov Complexity and Ideal MDL . . . . . . . . . . . . . . 8 1.2.2 Practical MDL . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8 1.3 MDL and Model Selection . . . . . . . . . . . . . . . . . . . . . . . . . . 9 1.4 Crude and Refined MDL . . . . . . . . . . . . . . . . . . . . . . . . . . . 12 1.5 The MDL Philosophy . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14 1.6 MDL and Occam’s Razor . . . . . . . . . . . . . . . . . . . . . . . . . . 17 1.7 History . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19 1.8 Summary and Outlook . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

2 Tutorial on MDL 23 2.1 Plan of the Tutorial . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23 2.2 Information Theory I: Probabilities and Codelengths . . . . . . . . . . . 24 2.2.1 Prefix Codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25 2.2.2 The Kraft Inequality - Codelengths & Probabilities, I . . . . . . 26 2.2.3 The Information Inequality - Codelengths & Probabilities, II . . 31 2.3 Statistical Preliminaries and Example Models . . . . . . . . . . . . . . . 32 2.4 Crude MDL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34 2.4.1 Description Length of Data given Hypothesis . . . . . . . . . . . 35 2.4.2 Description Length of Hypothesis . . . . . . . . . . . . . . . . . . 35 2.5 Information Theory II: Universal Codes and Models . . . . . . . . . . . 37 2.5.1 Two-part Codes as simple Universal Codes . . . . . . . . . . . . 39 2.5.2 From Universal Codes to Universal Models . . . . . . . . . . . . 40 2.5.3 NML as an Optimal Universal Model . . . . . . . . . . . . . . . . 42 2.6 Simple Refined MDL and its Four Interpretations . . . . . . . . . . . . . 44 2.6.1 Compression Interpretation . . . . . . . . . . . . . . . . . . . . . 46 2.6.2 Counting Interpretation . . . . . . . . . . . . . . . . . . . . . . . 47 2.6.3 Bayesian Interpretation . . . . . . . . . . . . . . . . . . . . . . . 50 2.6.4 Prequential Interpretation . . . . . . . . . . . . . . . . . . . . . . 51

3

2.7 General Refined MDL: Gluing it All Together . . . . . . . . . . . . . . . 54 2.7.1 Model Selection with Infinitely Many Models . . . . . . . . . . . 54 2.7.2 The Infinity Problem . . . . . . . . . . . . . . . . . . . . . . . . . 55 2.7.3 The General Picture . . . . . . . . . . . . . . . . . . . . . . . . . 58 2.8 Beyond Parametric Model Selection . . . . . . . . . . . . . . . . . . . . 60 2.9 Relations to Other Approaches to Inductive Inference . . . . . . . . . . 64 2.9.1 What is ‘MDL’? . . . . . . . . . . . . . . . . . . . . . . . . . . . 64 2.9.2 MDL and Bayesian Inference . . . . . . . . . . . . . . . . . . . . 65 2.9.3 MDL, Prequential Analysis and Cross-Validation . . . . . . . . . 67 2.9.4 Kolmogorov Complexity and Structure Function; Ideal MDL . . 68 2.10 Problems for MDL? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69 2.10.1 Conceptual Problems: Occam’s Razor . . . . . . . . . . . . . . . 69 2.10.2 Practical Problems with MDL . . . . . . . . . . . . . . . . . . . 71 2.11 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71

4

## Chapter 1

---

Full document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · Page-level evidence: [paper-pages/24-tutorial-minimum-description-length](../../paper-pages/24-tutorial-minimum-description-length/index.md)
