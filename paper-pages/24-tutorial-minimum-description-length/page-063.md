---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 63
pages: [63]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "2.9 Relations to Other Approaches to Inductive Inference How does MDL compare to other model selection and statistical inference methods? In order to…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 63 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 63 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

## 2.9 Relations to Other Approaches to Inductive Inference

How does MDL compare to other model selection and statistical inference methods? In order to answer this question, we first have to be precise about what we mean by ‘MDL’; this is done in Section 2.9.1. We then continue in Section 2.9.2 by summarizing MDL’s relation to Bayesian inference, Wallace’s MML Principle, Dawid’s prequential model validation, cross-validation and an ‘idealized’ version of MDL based on Kolmogorov complexity. The literature has also established connections between MDL and Jaynes’ \[2003\] Maximum Entropy Principle \[Feder 1986; Li and Vit´anyi 1997; Gr¨unwald 1998; Gr¨unwald 2000; Gr¨unwald and Dawid 2004\] and Vapnik’s \[1998\] structural risk minimization principle \[Gr¨unwald 1998\], but there is no space here to discuss these. Relations between MDL and Akaike’s AIC \[Burnham and Anderson 2002\] are subtle. They are discussed by, for example, Speed and Yu \[1993\].

2.9.1 What is ‘MDL’?

‘MDL’ is used by diﬀerent authors in somewhat diﬀerent meanings. Some authors use MDL as a broad umbrella term for all types of inductive inference based on data compression. This would, for example, include the ‘idealized’ versions of MDL based on Kolmogorov complexity and Wallaces’s MML Principle, to be discussed below. On the other extreme, for historical reasons, some authors use the MDL Criterion to describe a very specific (and often not very successful) model selection criterion equivalent to BIC, discussed further below.

Here we adopt the meaning of the term that is embraced in the survey \[Barron, Rissanen, and Yu 1998\], written by arguably the three most important contributors to the field: we use MDL for general inference based on universal models. These include, but are not limited to approaches in the spirit of Figure 2.4. For example, some authors have based their inferences on ‘expected’ rather than ‘individual sequence’ universal models \[Barron, Rissanen, and Yu 1998; Liang and Barron 2004a\]. Moreover, if we go beyond model selection (Section 2.8), then the ideas of Figure 2.4 have to be modified to some extent. In fact, one of the main strengths of “MDL” in this broad sense is that it can be applied to ever more exotic modeling situations, in which the models do not resemble anything that is usually encountered in statistical practice. An example is the model of context-free grammars, already suggested by Solomonoﬀ \[1964\]. In this tutorial, we call applications of MDL that strictly fit into the scheme of Figure 2.4 refined MDL for model/hypothesis selection; when we simply say ‘MDL’, we mean ‘inductive inference based on universal models’. This form of inductive inference goes hand in hand with Rissanen’s radical MDL philosophy, which views learning as finding useful properties of the data, not necessarily related to the existence of a ‘truth’ underlying the data. This view was outlined in Chapter 1, Section 1.5. Although MDL practitioners and theorists are usually sympathetic to it, the diﬀerent interpretations of MDL listed in Section 2.6 make clear that MDL applications can also be justified without adopting such a radical philosophy.

64

---

[previous page](page-062.md) · [next page](page-064.md) · [all pages](index.md)
