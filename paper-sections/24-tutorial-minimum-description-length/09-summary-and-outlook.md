---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
section: 1.8 Summary and Outlook
section_role: other
section_index: 9
pages: [19, 20, 21, 22]
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "We discussed how regularity is related to data compression, and how MDL employs this connection by viewing learning in terms of data compression. One…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 1.8 Summary and Outlook

> Section 9 of 23 from [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · `other` · pages 19-22

We discussed how regularity is related to data compression, and how MDL employs this connection by viewing learning in terms of data compression. One can make this precise in several ways; in idealized MDL one looks for the shortest program that generates the given data. This approach is not feasible in practice, and here we concern ourselves with practical MDL. Practical MDL comes in a crude version based on two-part codes and in a modern, more refined version based on the concept of universal coding. The basic ideas underlying all these approaches can be found in the boxes spread throughout the text.

These methods are mostly applied to model selection but can also be used for other problems of inductive inference. In contrast to most existing statistical methodology, they can be given a clear interpretation irrespective of whether or not there exists some ‘true’ distribution generating data – inductive inference is seen as a search for regular properties in (interesting statistics of) the data, and there is no need to assume anything outside the model and the data. In contrast to what is sometimes thought, there is no implicit belief that ‘simpler models are more likely to be true’ – MDL does embody a preference for ‘simple’ models, but this is best seen as a strategy for inference that can be useful even if the environment is not simple at all.

In the next chapter, we make precise both the crude and the refined versions of practical MDL. For this, it is absolutely essential that the reader familiarizes him- or herself with two basic notions of coding and information theory: the relation between codelength functions and probability distributions, and (for refined MDL), the idea of universal coding – a large part of the chapter will be devoted to these.

20

## Notes

1. See Section 2.9.2, Example 2.22. 2. By this we mean that a universal Turing Machine can be implemented in it \[Li and Vit´anyi 1997\]. 3. Strictly speaking, in our context it is not very accurate to speak of ‘simple’ or ‘complex’ polynomials; instead we should call the set of first degree polynomials ‘simple’, and the set of 100-th degree polynomials ‘complex’.

4. The terminology ‘crude MDL’ is not standard. It is introduced here for pedagogical reasons, to make clear the importance of having a single, unified principle for designing codes. It should be noted that Rissanen’s and Barron’s early theoretical papers on MDL already contain such principles, albeit in a slightly diﬀerent form than in their recent papers. Early practical applications \[Quinlan and Rivest 1989; Gr¨unwald 1996\] often do use ad hoc two-part codes which really are ‘crude’ in the sense defined here.

5. See the previous note. 6. For example, cross-validation cannot easily be interpreted in such terms of ‘a method hunting for the true distribution’.

7. The present author’s own views are somewhat milder in this respect, but this is not the place to discuss them.

8. Quoted with permission from KDD Nuggets 96:28, 1996.

21

22

## Chapter 2

---

Full document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · Page-level evidence: [paper-pages/24-tutorial-minimum-description-length](../../paper-pages/24-tutorial-minimum-description-length/index.md)
