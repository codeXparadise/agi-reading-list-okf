---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 16
pages: [16]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "MDL with ‘clever’ codes achieves good rates of convergence in this sense (Barron and Cover [1991], complemented by [Zhang 2004], show that in many…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 16 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 16 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

MDL with ‘clever’ codes achieves good rates of convergence in this sense (Barron and Cover \[1991\], complemented by \[Zhang 2004\], show that in many situations, the rates are minimax optimal). The same seems to be true for refined one-part code MDL \[Barron, Rissanen, and Yu 1998\], although there is at least one surprising exception where inference based on the NML and Bayesian universal model behaves abnormally – see \[Csisz´ar and Shields 2000\] for the details.

Summarizing this section, the MDL philosophy is quite agnostic about whether any of the models under consideration is ‘true’, or whether something like a ‘true distribution’ even exists. Nevertheless, it has been suggested \[Webb 1996; Domingos 1999\] that MDL embodies a naive belief that ‘simple models’ are ‘a priori more likely to be true’ than complex models. Below we explain why such claims are mistaken.

## 1.6 MDL and Occam’s Razor

When two models fit the data equally well, MDL will choose the one that is the ‘simplest’ in the sense that it allows for a shorter description of the data. As such, it implements a precise form of Occam’s Razor – even though as more and more data becomes available, the model selected by MDL may become more and more ‘complex’! Occam’s Razor is sometimes criticized for being either (1) arbitrary or (2) false \[Webb 1996; Domingos 1999\]. Do these criticisms apply to MDL as well?

‘1. Occam’s Razor (and MDL) is arbitrary’ Because ‘description length’ is a syntactic notion it may seem that MDL selects an arbitrary model: diﬀerent codes would have led to diﬀerent description lengths, and therefore, to diﬀerent models. By changing the encoding method, we can make ‘complex’ things ‘simple’ and vice versa. This overlooks the fact we are not allowed to use just any code we like! ‘Refined’ MDL tells us to use a specific code, independent of any specific parameterization of the model, leading to a notion of complexity that can also be interpreted without any reference to ‘description lengths’ (see also Section 2.10.1).

‘2. Occam’s Razor is false’ It is often claimed that Occam’s razor is false - we often try to model real-world situations that are arbitrarily complex, so why should we favor simple models? In the words of G. Webb8: ‘What good are simple models of a complex world?’

The short answer is: even if the true data generating machinery is very complex, it may be a good strategy to prefer simple models for small sample sizes. Thus, MDL (and the corresponding form of Occam’s razor) is a strategy for inferring models from data (“choose simple models at small sample sizes”), not a statement about how the world works (“simple models are more likely to be true”) – indeed, a strategy cannot be true or false, it is ‘clever’ or ‘stupid’. And the strategy of preferring simpler models

17

---

[previous page](page-015.md) · [next page](page-017.md) · [all pages](index.md)
