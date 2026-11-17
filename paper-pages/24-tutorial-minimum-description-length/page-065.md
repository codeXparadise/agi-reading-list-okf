---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 65
pages: [65]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "philosophy (e.g. De Finetti [1974]’s) which avoid the conceptual problem we just described. MDL and BIC In the first paper on MDL, Rissanen [1978]…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 65 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 65 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

philosophy (e.g. De Finetti \[1974\]’s) which avoid the conceptual problem we just described.

MDL and BIC In the first paper on MDL, Rissanen \[1978\] used a two-part code and showed that, asymptotically, and under regularity conditions, the two-part codelength of xn based on a k-parameter model M with an optimally discretized parameter space is given by

−log P(xn | ˆθ(xn)) + k

2 log n, (2.42)

thus ignoring O(1)-terms, which, as we have already seen, can be quite important. In the same year Schwarz \[1978\] showed that, for large enough n, Bayesian model selection between two exponential families amounts to selecting the model minimizing (2.42), ignoring O(1)-terms as well. As a result of Schwarz’s paper, model selection based on (2.42) became known as the BIC (Bayesian Information Criterion). Not taking into account the functional form of the model M, it often does not work very well in practice.

It has sometimes been claimed that MDL = BIC; for example, \[Burnham and Anderson 2002, page 286\] write “Rissanen’s result is equivalent to BIC”. This is wrong, even for the 1989 version of MDL that Burnham and Anderson refer to – as pointed out by Foster and Stine \[2004\], the BIC approximation only holds if the number of parameters k is kept fixed and n goes to infinity. If we select between nested families of models where the maximum number of parameters k considered is either infinite or grows with n, then model selection based on both ¯Pnml and on ¯PBayes tends to select quite diﬀerent models than BIC - if k gets closer to n, the contribution to COMPn(M) of each additional parameter becomes much smaller than 0.5 log n \[Foster and Stine 2004\]. However, researchers who claim MDL = BIC have a good excuse: in early work, Rissanen himself has used the phrase ‘MDL criterion’ to refer to (2.42), and unfortunately, the phrase has stuck.

MDL and MML MDL shares some ideas with the Minimum Message Length (MML) Principle which predates MDL by 10 years. Key references are \[Wallace and Boulton 1968; Wallace and Boulton 1975\] and \[Wallace and Freeman 1987\]; a long list is in \[Comley and Dowe 2004\]. Just as in MDL, MML chooses the hypothesis minimizing the code-length of the data. But the codes that are used are quite diﬀerent from those in MDL. First of all, in MML one always uses two-part codes, so that MML automatically selects both a model family and parameter values. Second, while the MDL codes such as

¯Pnml minimize worst-case relative code-length (regret), the two-part codes used by MML are designed to minimize expected absolute code-length. Here the expectation is taken over a subjective prior distribution defined on the collection of models and parameters under consideration. While this approach contradicts Rissanen’s philosophy, in practice it often leads to similar results.

66

---

[previous page](page-064.md) · [next page](page-066.md) · [all pages](index.md)
