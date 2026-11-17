---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 71
pages: [71]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "this without having been designed for consistency, being based on a philosophy which makes no metaphysical assumptions about the existence of ‘true’…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 71 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 71 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

this without having been designed for consistency, being based on a philosophy which makes no metaphysical assumptions about the existence of ‘true’ distributions. All this strongly suggests that it is a good method to use in practice. Practical evidence shows that in many contexts it is, in other contexts its behavior can be problematic. In the author’s view, the main challenge for the future is to improve MDL for such cases, by somehow extending and further refining MDL procedures in a non ad-hoc manner. I am confident that this can be done, and that MDL will continue to play an important role in the development of statistical, and more generally, inductive inference.

Further Reading MDL can be found on the web at www.mdl-research.org. Good places to start further exploration of MDL are \[Barron, Rissanen, and Yu 1998\] and \[Hansen and Yu 2001\]. Both papers provide excellent introductions, but they are geared towards a more specialized audience of information theorists and statisticians, respectively. Also worth reading is Rissanen’s \[1989\] monograph. While outdated as an introduction to MDL methods, this famous ‘little green book’ still serves as a great introduction to Rissanen’s radical but appealing philosophy, which is described very eloquently.

Acknowledgments The author would like to thank Jay Myung, Mark Pitt, Steven de Rooij and Teemu Roos, who read a preliminary version of this chapter and suggested several improvements.

## Notes

1. But see Section 2.9.4. 2. Working directly with distributions on infinite sequences is more elegant, but it requires measure theory, which we want to avoid here.

3. Also known as instantaneous codes and called, perhaps more justifiably, ‘prefix-free’ codes in \[Li and Vit´anyi 1997\].

4. For example, with non-integer codelengths the notion of ‘code’ becomes invariant to the size of the alphabet in which we describe data.

5. As understood in elementary probability, i.e. with respect to Lebesgue measure. 6. Even if one adopts a Bayesian stance and postulates that an agent can come up with a (subjective) distribution for every conceivable domain, this problem remains: in practice, the adopted distribution may be so complicated that we cannot design the optimal code corresponding to it, and have to use some ad hoc-instead.

7. Henceforth, we simply use ‘model’ to denote probabilistic models; we typically use H to denote sets of hypotheses such as polynomials, and reserve M for probabilistic models.

8. The terminology ‘crude MDL’ is not standard. It is introduced here for pedagogical reasons, to make clear the importance of having a single, unified principle for designing codes. It should be noted that Rissanen’s and Barron’s early theoretical papers on MDL already contain such principles, albeit in a slightly diﬀerent form than in their recent papers. Early practical applications \[Quinlan and Rivest 1989; Gr¨unwald 1996\] often do use ad hoc two-part codes which really are ‘crude’ in the sense defined here.

9. See the previous endnote. 10. but see \[Gr¨unwald 1998\], Chapter 5 for more discussion.

72

---

[previous page](page-070.md) · [next page](page-072.md) · [all pages](index.md)
