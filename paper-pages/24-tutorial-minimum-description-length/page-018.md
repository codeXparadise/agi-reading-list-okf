---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 18
pages: [18]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "The Inherent Diﬀerence between Under- and Overfitting If we choose an overly simple model for our data, then the best-fitting point hypothesis within…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 18 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 18 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

The Inherent Diﬀerence between Under- and Overfitting If we choose an overly simple model for our data, then the best-fitting point hypothesis within the model is likely to be almost the best predictor, within the simple model, of future data coming from the same source. If we overfit (choose a very complex model) and there is noise in our data, then, even if the complex model contains the ‘true’ point hypothesis, the best-fitting point hypothesis within the model is likely to lead to very bad predictions of future data coming from the same source.

This statement is very imprecise and is meant more to convey the general idea than to be completely true. As will become clear in Section 2.10.1, it becomes provably true if we use MDL’s measure of model complexity; we measure prediction quality by logarithmic loss; and we assume that one of the distributions in H actually generates the data.

## 1.7 History

The MDL Principle has mainly been developed by J. Rissanen in a series of papers starting with \[Rissanen 1978\]. It has its roots in the theory of Kolmogorov or algorithmic complexity \[Li and Vit´anyi 1997\], developed in the 1960s by Solomonoﬀ\[1964\], Kolmogorov \[1965\] and Chaitin \[1966, 1969\]. Among these authors, Solomonoﬀ(a former student of the famous philosopher of science, Rudolf Carnap) was explicitly interested in inductive inference. The 1964 paper contains explicit suggestions on how the underlying ideas could be made practical, thereby foreshadowing some of the later work on two-part MDL. While Rissanen was not aware of Solomonoﬀ’s work at the time, Kolmogorov’s \[1965\] paper did serve as an inspiration for Rissanen’s \[1978\] development of MDL.

Another important inspiration for Rissanen was Akaike’s \[1973\] AIC method for model selection, essentially the first model selection method based on informationtheoretic ideas. Even though Rissanen was inspired by AIC, both the actual method and the underlying philosophy are substantially diﬀerent from MDL.

MDL is much closer related to the Minimum Message Length Principle, developed by Wallace and his co-workers in a series of papers starting with the ground-breaking \[Wallace and Boulton 1968\]; other milestones are \[Wallace and Boulton 1975\] and \[Wallace and Freeman 1987\]. Remarkably, Wallace developed his ideas without being aware of the notion of Kolmogorov complexity. Although Rissanen became aware of Wallace’s work before the publication of \[Rissanen 1978\], he developed his ideas mostly independently, being influenced rather by Akaike and Kolmogorov. Indeed, despite the close resemblance of both methods in practice, the underlying philosophy is quite diﬀerent - see Section 2.9.

The first publications on MDL only mention two-part codes. Important progress was made by Rissanen \[1984\], in which prequential codes are employed for the first

19

---

[previous page](page-017.md) · [next page](page-019.md) · [all pages](index.md)
