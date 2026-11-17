---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 58
pages: [58]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "GENERAL ‘REFINED’ MDL PRINCIPLE for Model Selection Suppose we plan to select between models M(1), M(2), . . . for data D = (x1, . . . , xn). MDL…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 58 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 58 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

GENERAL ‘REFINED’ MDL PRINCIPLE for Model Selection Suppose we plan to select between models M(1), M(2), . . . for data D = (x1, . . . , xn). MDL tells us to design a universal code ¯P for X n, in which the index k of M(k) is encoded explicitly. The resulting code has two parts, the two sub-codes being defined such that

1. All models M(k) are treated on the same footing, as far as possible: we assign a uniform prior to these models, or, if that is not a possible, a prior ‘close to’ uniform.

2. All distributions within each M(k) are treated on the same footing, as far as possible: we use the minimax regret universal model ¯Pnml(xn | M(k)). If this model is undefined or too hard to compute, we instead use a diﬀerent universal model that achieves regret ‘close to’ the minimax regret for each submodel of M(k) in the sense of (2.35).

In the end, we encode data D using a hybrid two-part/one-part universal model, explicitly encoding the models we want to select between and implicitly encoding any distributions contained in those models.

Figure 2.4: The Refined MDL Principle.

59

---

[previous page](page-057.md) · [next page](page-059.md) · [all pages](index.md)
