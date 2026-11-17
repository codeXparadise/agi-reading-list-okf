---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
section: 1.7 History
section_role: other
section_index: 8
pages: [18, 19]
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "The MDL Principle has mainly been developed by J. Rissanen in a series of papers starting with [Rissanen 1978]. It has its roots in the theory of…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 1.7 History

> Section 8 of 23 from [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · `other` · pages 18-19

The MDL Principle has mainly been developed by J. Rissanen in a series of papers starting with \[Rissanen 1978\]. It has its roots in the theory of Kolmogorov or algorithmic complexity \[Li and Vit´anyi 1997\], developed in the 1960s by Solomonoﬀ\[1964\], Kolmogorov \[1965\] and Chaitin \[1966, 1969\]. Among these authors, Solomonoﬀ(a former student of the famous philosopher of science, Rudolf Carnap) was explicitly interested in inductive inference. The 1964 paper contains explicit suggestions on how the underlying ideas could be made practical, thereby foreshadowing some of the later work on two-part MDL. While Rissanen was not aware of Solomonoﬀ’s work at the time, Kolmogorov’s \[1965\] paper did serve as an inspiration for Rissanen’s \[1978\] development of MDL.

Another important inspiration for Rissanen was Akaike’s \[1973\] AIC method for model selection, essentially the first model selection method based on informationtheoretic ideas. Even though Rissanen was inspired by AIC, both the actual method and the underlying philosophy are substantially diﬀerent from MDL.

MDL is much closer related to the Minimum Message Length Principle, developed by Wallace and his co-workers in a series of papers starting with the ground-breaking \[Wallace and Boulton 1968\]; other milestones are \[Wallace and Boulton 1975\] and \[Wallace and Freeman 1987\]. Remarkably, Wallace developed his ideas without being aware of the notion of Kolmogorov complexity. Although Rissanen became aware of Wallace’s work before the publication of \[Rissanen 1978\], he developed his ideas mostly independently, being influenced rather by Akaike and Kolmogorov. Indeed, despite the close resemblance of both methods in practice, the underlying philosophy is quite diﬀerent - see Section 2.9.

The first publications on MDL only mention two-part codes. Important progress was made by Rissanen \[1984\], in which prequential codes are employed for the first

19

time and \[Rissanen 1987\], introducing the Bayesian mixture codes into MDL. This led to the development of the notion of stochastic complexity as the shortest codelength of the data given a model \[Rissanen 1986; Rissanen 1987\]. However, the connection to Shtarkov’s normalized maximum likelihood code was not made until 1996, and this prevented the full development of the notion of ‘parametric complexity’. In the mean time, in his impressive Ph.D. thesis, Barron \[1985\] showed how a specific version of the two-part code criterion has excellent frequentist statistical consistency properties. This was extended by Barron and Cover \[1991\] who achieved a breakthrough for two-part codes: they gave clear prescriptions on how to design codes for hypotheses, relating codes with good minimax codelength properties to rates of convergence in statistical consistency theorems. Some of the ideas of Rissanen \[1987\] and Barron and Cover \[1991\] were, as it were, unified when Rissanen \[1996\] introduced a new definition of stochastic complexity based on the normalized maximum likelihood code (Section 2.5). The resulting theory was summarized for the first time by Barron, Rissanen, and Yu \[1998\], and is called ‘refined MDL’ in the present overview.

---

Full document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · Page-level evidence: [paper-pages/24-tutorial-minimum-description-length](../../paper-pages/24-tutorial-minimum-description-length/index.md)
