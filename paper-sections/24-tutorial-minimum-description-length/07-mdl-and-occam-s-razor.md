---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
section: "1.6 MDL and Occam’s Razor"
section_role: other
section_index: 7
pages: [16, 17, 18]
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "When two models fit the data equally well, MDL will choose the one that is the ‘simplest’ in the sense that it allows for a shorter description of…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 1.6 MDL and Occam’s Razor

> Section 7 of 23 from [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · `other` · pages 16-18

When two models fit the data equally well, MDL will choose the one that is the ‘simplest’ in the sense that it allows for a shorter description of the data. As such, it implements a precise form of Occam’s Razor – even though as more and more data becomes available, the model selected by MDL may become more and more ‘complex’! Occam’s Razor is sometimes criticized for being either (1) arbitrary or (2) false \[Webb 1996; Domingos 1999\]. Do these criticisms apply to MDL as well?

‘1. Occam’s Razor (and MDL) is arbitrary’ Because ‘description length’ is a syntactic notion it may seem that MDL selects an arbitrary model: diﬀerent codes would have led to diﬀerent description lengths, and therefore, to diﬀerent models. By changing the encoding method, we can make ‘complex’ things ‘simple’ and vice versa. This overlooks the fact we are not allowed to use just any code we like! ‘Refined’ MDL tells us to use a specific code, independent of any specific parameterization of the model, leading to a notion of complexity that can also be interpreted without any reference to ‘description lengths’ (see also Section 2.10.1).

‘2. Occam’s Razor is false’ It is often claimed that Occam’s razor is false - we often try to model real-world situations that are arbitrarily complex, so why should we favor simple models? In the words of G. Webb8: ‘What good are simple models of a complex world?’

The short answer is: even if the true data generating machinery is very complex, it may be a good strategy to prefer simple models for small sample sizes. Thus, MDL (and the corresponding form of Occam’s razor) is a strategy for inferring models from data (“choose simple models at small sample sizes”), not a statement about how the world works (“simple models are more likely to be true”) – indeed, a strategy cannot be true or false, it is ‘clever’ or ‘stupid’. And the strategy of preferring simpler models

17

is clever even if the data generating process is highly complex, as illustrated by the following example:

Example 1.6 \[‘Infinitely’ Complex Sources\] Suppose that data are subject to the law Y = g(X) + Z where g is some continuous function and Z is some noise term with mean 0. If g is not a polynomial, but X only takes values in a finite interval, say \[−1, 1\], we may still approximate g arbitrarily well by taking higher and higher degree polynomials. For example, let g(x) = exp(x). Then, if we use MDL to learn a polynomial for data D = ((x1, y1), . . . , (xn, yn)), the degree of the polynomial ¨f (n)

selected by MDL at sample size n will increase with n, and with high probability,

¨f (n) converges to g(x) = exp(x) in the sense that maxx∈\[−1,1\] | ¨f (n)(x) −g(x)| →0. Of course, if we had better prior knowledge about the problem we could have tried to learn g using a model class M containing the function y = exp(x). But in general, both our imagination and our computational resources are limited, and we may be forced to use imperfect models.

If, based on a small sample, we choose the best-fitting polynomial ˆf within the set of all polynomials, then, even though ˆf will fit the data very well, it is likely to be quite unrelated to the ‘true’ g, and ˆf may lead to disastrous predictions of future data. The reason is that, for small samples, the set of all polynomials is very large compared to the set of possible data patterns that we might have observed. Therefore, any particular data pattern can only give us very limited information about which high-degree polynomial best approximates g. On the other hand, if we choose the best-fitting ˆf ◦in some much smaller set such as the set of second-degree polynomials, then it is highly probable that the prediction quality (mean squared error) of ˆf ◦on future data is about the same as its mean squared error on the data we observed: the size (complexity) of the contemplated model is relatively small compared to the set of possible data patterns that we might have observed. Therefore, the particular pattern that we do observe gives us a lot of information on what second-degree polynomial best approximates g.

Thus, (a) ˆf ◦typically leads to better predictions of future data than ˆf; and (b) unlike ˆf, ˆf ◦is reliable in that it gives a correct impression of how good it will predict future data even if the ‘true’ g is ‘infinitely’ complex. This idea does not just appear in MDL, but is also the basis of Vapnik’s \[1998\] Structural Risk Minimization approach and many standard statistical methods for non-parametric inference. In such approaches one acknowledges that the data generating machinery can be infinitely complex (e.g., not describable by a finite degree polynomial). Nevertheless, it is still a good strategy to approximate it by simple hypotheses (low-degree polynomials) as long as the sample size is small. Summarizing:

18

The Inherent Diﬀerence between Under- and Overfitting If we choose an overly simple model for our data, then the best-fitting point hypothesis within the model is likely to be almost the best predictor, within the simple model, of future data coming from the same source. If we overfit (choose a very complex model) and there is noise in our data, then, even if the complex model contains the ‘true’ point hypothesis, the best-fitting point hypothesis within the model is likely to lead to very bad predictions of future data coming from the same source.

This statement is very imprecise and is meant more to convey the general idea than to be completely true. As will become clear in Section 2.10.1, it becomes provably true if we use MDL’s measure of model complexity; we measure prediction quality by logarithmic loss; and we assume that one of the distributions in H actually generates the data.

---

Full document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · Page-level evidence: [paper-pages/24-tutorial-minimum-description-length](../../paper-pages/24-tutorial-minimum-description-length/index.md)
