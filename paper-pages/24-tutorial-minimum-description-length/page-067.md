---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 67
pages: [67]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "and Vovk [2001]. Note that the prequential approach is similar in spirit to cross-validation. In this sense MDL is related to cross-validation as…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 67 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 67 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

and Vovk \[2001\].

Note that the prequential approach is similar in spirit to cross-validation. In this sense MDL is related to cross-validation as well. The main diﬀerences are that in MDL and the prequential approach, (1) all predictions are done sequentially (the future is never used to predict the past), and (2) each outcome is predicted exactly once.

2.9.4 Kolmogorov Complexity and Structure Function; Ideal MDL

Kolmogorov complexity \[Li and Vit´anyi 1997\] has played a large but mostly inspirational role in Rissanen’s development of MDL. Over the last fifteen years, several ‘idealized’ versions of MDL have been proposed, which are more directly based on Kolmogorov complexity theory \[Barron 1985; Barron and Cover 1991; Li and Vit´anyi 1997; Vereshchagin and Vit´anyi 2002\]. These are all based on two-part codes, where hypotheses are described using a universal programming language such as C or Pascal. For example, in one proposal \[Barron and Cover 1991\], given data D one picks the distribution minimizing

K(P) +

−log P(D)

, (2.43)

where the minimum is taken over all computable probability distributions, and K(P) is the length of the shortest computer program that, when input (x, d), outputs P(x) to d bits precision. While such a procedure is mathematically well-defined, it cannot be used in practice. The reason is that in general, the P minimizing (2.43) cannot be eﬀectively computed. Kolmogorov himself used a variation of (2.43) in which one adopts, among all P with K(P) −log P(D) ≈K(D), the P with smallest K(P). Here K(D) is the Kolmogorov complexity of D, that is, the length of the shortest computer program that prints D and then halts. This approach is known as the Kolmogorov structure function or minimum suﬃcient statistic approach \[Vit´anyi 2004\]. In this approach, the idea of separating data and noise (Section 2.6.1) is taken as basic, and the hypothesis selection procedure is defined in terms of it. The selected hypothesis may now be viewed as capturing all structure inherent in the data - given the hypothesis, the data cannot be distinguished from random noise. Therefore, it may be taken as a basis for lossy data compression – rather than sending the whole sequence, one only sends the hypothesis representing the ‘structure’ in the data. The receiver can then use this hypothesis to generate ‘typical’ data for it - this data should then ‘look just the same’ as the original data D. Rissanen views this separation idea as perhaps the most fundamental aspect of ‘learning by compression’. Therefore, in recent work he has tried to relate MDL (as defined here, based on lossless compression) to the Kolmogorov structure function, thereby connecting it to lossy compression, and, as he puts it, ‘opening up a new chapter in the MDL theory’ \[Vereshchagin and Vit´anyi 2002; Vit´anyi 2004; Rissanen and Tabus 2004\].

Summary and Outlook We have shown that MDL is closely related to, yet distinct from, several other methods for inductive inference. In the next section we discuss how

68

---

[previous page](page-066.md) · [next page](page-068.md) · [all pages](index.md)
