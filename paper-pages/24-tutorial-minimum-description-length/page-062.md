---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 62
pages: [62]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "When the Codelength for xn Can Be Ignored If all models under consideration represent conditional densities or probability mass functions P(Y | X),…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 62 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 62 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

When the Codelength for xn Can Be Ignored If all models under consideration represent conditional densities or probability mass functions P(Y | X), then the codelength for X1, . . . , Xn can be ignored in model and parameter selection. Examples are applications of MDL in classification and regression.

Figure 2.5: Ignoring codelengths.

‘Non-probabilistic’ Regression and Classification In the approach we just described, we modeled the noise as being normally distributed. Alternatively, it has been tried to directly try to learn functions h ∈H from the data, without making any probabilistic assumptions about the noise \[Rissanen 1989; Barron 1990; Yamanishi 1998; Gr¨unwald 1998; Gr¨unwald 1999\]. The idea is to learn a function h that leads to good predictions of future data from the same source in the spirit of Vapnik’s \[1998\] statistical learning theory. Here prediction quality is measured by some fixed loss function; different loss functions lead to diﬀerent instantiations of the procedure. Such a version of MDL is meant to be more robust, leading to inference of a ‘good’ h ∈H irrespective of the details of the noise distribution. This loss-based approach has also been the method of choice in applying MDL to classification problems. Here Y takes on values in a finite set, and the goal is to match each feature X (for example, a bit map of a handwritten digit) with its corresponding label or class (e.g., a digit). While several versions of MDL for classification have been proposed \[Quinlan and Rivest 1989; Rissanen 1989; Kearns, Mansour, Ng, and Ron 1997\], most of these can be reduced to the same approach based on a 0/1-valued loss function \[Gr¨unwald 1998\]. In recent work \[Gr¨unwald and Langford 2004\] we show that this MDL approach to classification without making assumptions about the noise may behave suboptimally: we exhibit situations where no matter how large n, MDL keeps overfitting, selecting an overly complex model with suboptimal predictive behavior. Modifications of MDL suggested by Barron \[1990\] and Yamanishi \[1998\] do not suﬀer from this defect, but they do not admit a natural coding interpretation any longer. All in all, current versions of MDL that avoid probabilistic assumptions are still in their infancy, and more research is needed to find out whether they can be modified to perform well in more general and realistic settings.

Summary In the previous sections, we have covered basic refined MDL (Section 2.6), general refined MDL (Section 2.7), and several extensions of refined MDL (this section). This concludes our technical description of refined MDL. It only remains to place MDL in its proper context: what does it do compared to other methods of inductive inference? And how well does it perform, compared to other methods? The next two sections are devoted to these questions.

63

---

[previous page](page-061.md) · [next page](page-063.md) · [all pages](index.md)
