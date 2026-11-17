---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 17
pages: [17]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "is clever even if the data generating process is highly complex, as illustrated by the following example: Example 1.6 [‘Infinitely’ Complex Sources]…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 17 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 17 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

is clever even if the data generating process is highly complex, as illustrated by the following example:

Example 1.6 \[‘Infinitely’ Complex Sources\] Suppose that data are subject to the law Y = g(X) + Z where g is some continuous function and Z is some noise term with mean 0. If g is not a polynomial, but X only takes values in a finite interval, say \[−1, 1\], we may still approximate g arbitrarily well by taking higher and higher degree polynomials. For example, let g(x) = exp(x). Then, if we use MDL to learn a polynomial for data D = ((x1, y1), . . . , (xn, yn)), the degree of the polynomial ¨f (n)

selected by MDL at sample size n will increase with n, and with high probability,

¨f (n) converges to g(x) = exp(x) in the sense that maxx∈\[−1,1\] | ¨f (n)(x) −g(x)| →0. Of course, if we had better prior knowledge about the problem we could have tried to learn g using a model class M containing the function y = exp(x). But in general, both our imagination and our computational resources are limited, and we may be forced to use imperfect models.

If, based on a small sample, we choose the best-fitting polynomial ˆf within the set of all polynomials, then, even though ˆf will fit the data very well, it is likely to be quite unrelated to the ‘true’ g, and ˆf may lead to disastrous predictions of future data. The reason is that, for small samples, the set of all polynomials is very large compared to the set of possible data patterns that we might have observed. Therefore, any particular data pattern can only give us very limited information about which high-degree polynomial best approximates g. On the other hand, if we choose the best-fitting ˆf ◦in some much smaller set such as the set of second-degree polynomials, then it is highly probable that the prediction quality (mean squared error) of ˆf ◦on future data is about the same as its mean squared error on the data we observed: the size (complexity) of the contemplated model is relatively small compared to the set of possible data patterns that we might have observed. Therefore, the particular pattern that we do observe gives us a lot of information on what second-degree polynomial best approximates g.

Thus, (a) ˆf ◦typically leads to better predictions of future data than ˆf; and (b) unlike ˆf, ˆf ◦is reliable in that it gives a correct impression of how good it will predict future data even if the ‘true’ g is ‘infinitely’ complex. This idea does not just appear in MDL, but is also the basis of Vapnik’s \[1998\] Structural Risk Minimization approach and many standard statistical methods for non-parametric inference. In such approaches one acknowledges that the data generating machinery can be infinitely complex (e.g., not describable by a finite degree polynomial). Nevertheless, it is still a good strategy to approximate it by simple hypotheses (low-degree polynomials) as long as the sample size is small. Summarizing:

18

---

[previous page](page-016.md) · [next page](page-018.md) · [all pages](index.md)
