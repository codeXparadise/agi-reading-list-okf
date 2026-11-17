---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 70
pages: [70]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "2.10.2 Practical Problems with MDL We just described some perceived problems about MDL. Unfortunately, there are also some real ones: MDL is not a…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 70 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 70 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

2.10.2 Practical Problems with MDL

We just described some perceived problems about MDL. Unfortunately, there are also some real ones: MDL is not a perfect method. While in many cases, the methods described here perform very well22 there are also cases where they perform suboptimally compared to other state-of-the-art methods. Often this is due to one of two reasons:

1. An asymptotic formula like (2.21) was used and the sample size was not large enough to justify this \[Navarro 2004\].

2. ¯Pnml was undefined for the models under consideration, and this was solved by cutting oﬀthe parameter ranges at ad hoc values \[Lanterman 2004\].

In these cases the problem probably lies with the use of invalid approximations rather than with the MDL idea itself. More research is needed to find out when the asymptotics and other approximations can be trusted, and what is the ‘best’ way to deal with undefined ¯Pnml. For the time being, we suggest to avoid using (2.21) whenever possible, and to never cut oﬀthe parameter ranges at arbitrary values – instead, if COMPn(M) becomes infinite, then some of the methods described in Section 2.7.2 should be used. Given these restrictions, ¯Pnml and Bayesian inference with Jeﬀreys’ prior are the preferred methods, since they both achieve the minimax regret. If they are either ill-defined or computationally prohibitive for the models under consideration, one can use a prequential method or a sophisticated two-part code such as described by Barron and Cover \[1991\].

MDL and Misspecification However, there is a class of problems where MDL is problematic in a more fundamental sense. Namely, if none of the distributions under consideration represents the data generating machinery very well, then both MDL and Bayesian inference may sometimes do a bad job in finding the ‘best’ approximation within this class of not-so-good hypotheses. This has been observed in practice23

\[Kearns, Mansour, Ng, and Ron 1997; Clarke 2002; Pednault 2003\]. Gr¨unwald and Langford \[2004\] show that MDL can behave quite unreasonably for some classification problems in which the true distribution is not in M. This is closely related to the problematic behavior of MDL for classification tasks as mentioned in Section 2.8. All this is a bit ironic, since MDL was explicitly designed not to depend on the untenable assumption that some P ∗∈M generates the data. But empirically we find that while it generally works quite well if some P ∗∈M generates the data, it may sometimes fail if this is not the case.

## 2.11 Conclusion

MDL is a versatile method for inductive inference: it can be interpreted in at least four diﬀerent ways, all of which indicate that it does something reasonable. It is typically asymptotically consistent, achieving good rates of convergence. It achieves all

71

---

[previous page](page-069.md) · [next page](page-071.md) · [all pages](index.md)
