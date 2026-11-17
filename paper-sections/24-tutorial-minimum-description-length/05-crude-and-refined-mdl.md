---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
section: 1.4 Crude and Refined MDL
section_role: other
section_index: 5
pages: [11, 12, 13]
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "Crude MDL picks the H minimizing the sum L(H)+L(D|H). To make this procedure well-defined, we need to agree on precise definitions for the codes…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 1.4 Crude and Refined MDL

> Section 5 of 23 from [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · `other` · pages 11-13

Crude MDL picks the H minimizing the sum L(H)+L(D|H). To make this procedure well-defined, we need to agree on precise definitions for the codes (description methods) giving rise to lengths L(D|H) and L(H). We now discuss these codes in more detail. We will see that the definition of L(H) is problematic, indicating that we somehow need to ‘refine’ our crude MDL Principle.

Definition of L(D|H) Consider a two-part code as described above, and assume for the time being that all H under consideration define probability distributions. If H is a polynomial, we can turn it into a distribution by making the additional assumption that the Y -values are given by Y = H(X)+Z, where Z is a normally distributed noise term.

For each H we need to define a code with length L(· | H) such that L(D|H) can be interpreted as ‘the codelength of D when encoded with the help of H’. It turns out that for probabilistic hypotheses, there is only one reasonable choice for this code. It is the so-called Shannon-Fano code, satisfying, for all data sequences D, L(D|H) = −log P(D|H), where P(D|H) is the probability mass or density of D according to H – such a code always exists, Section 2.2.

Definition of L(H): A Problem for Crude MDL It is more problematic to find a good code for hypotheses H. Some authors have simply used ‘intuitively reasonable’ codes in the past, but this is not satisfactory: since the description length L(H) of any fixed point hypothesis H can be very large under one code, but quite short under another, our procedure is in danger of becoming arbitrary. Instead, we need some additional principle for designing a code for H. In the first publications on MDL \[Rissanen 1978; Rissanen 1983\], it was advocated to choose some sort of minimax code for H, minimizing, in some precisely defined sense, the shortest worst-case total description length L(H) + L(D|H), where the worst-case is over all possible data sequences. Thus, the MDL Principle is employed at a ‘meta-level’ to choose a code for H. However, this code requires a cumbersome discretization of the model space H, which is not always feasible in practice. Alternatively, Barron \[1985\] encoded H by the shortest computer program that, when input D, computes P(D|H). While it can be shown that this leads to similar codelengths, it is computationally problematic. Later, Rissanen \[1984\] realized that these problems could be side-stepped by using a one-part rather than a two-part code. This development culminated in 1996 in a completely precise prescription of MDL for many, but certainly not all practical situations \[Rissanen 1996\]. We call this modern version of MDL refined MDL:

Refined MDL In refined MDL, we associate a code for encoding D not with a single H ∈H, but with the full model H. Thus, given model H, we encode data not in two parts but we design a single one-part code with lengths ¯L(D|H). This code is designed such that whenever there is a member of (parameter in) H that fits the data well, in

12

the sense that L(D | H) is small, then the codelength ¯L(D|H) will also be small. Codes with this property are called universal codes in the information-theoretic literature \[Barron, Rissanen, and Yu 1998\]. Among all such universal codes, we pick the one that is minimax optimal in a sense made precise in Section 2.5. For example, the set H(3) of third-degree polynomials is associated with a code with lengths ¯L(· | H(3)) such that, the better the data D are fit by the best-fitting third-degree polynomial, the shorter the codelength ¯L(D | H). ¯L(D | H) is called the stochastic complexity of the data given the model.

Parametric Complexity The second fundamental concept of refined MDL is the parametric complexity of a parametric model H which we denote by COMP(H). This is a measure of the ‘richness’ of model H, indicating its ability to fit random data. This complexity is related to the degrees-of-freedom in H, but also to the geometrical structure of H; see Example 1.4. To see how it relates to stochastic complexity, let, for given data D, ˆH denote the distribution in H which maximizes the probability, and hence minimizes the codelength L(D | ˆH) of D. It turns out that

stochastic complexity of D given H = L(D | ˆH) + COMP(H).

Refined MDL model selection between two parametric models (such as the models of first and second degree polynomials) now proceeds by selecting the model such that the stochastic complexity of the given data D is smallest. Although we used a one-part code to encode data, refined MDL model selection still involves a trade-oﬀbetween two terms: a goodness-of-fit term L(D | ˆH) and a complexity term COMP(H). However, because we do not explicitly encode hypotheses H any more, there is no arbitrariness any more. The resulting procedure can be interpreted in several diﬀerent ways, some of which provide us with rationales for MDL beyond the pure coding interpretation (Sections 2.6.1–2.6.4):

1. Counting/diﬀerential geometric interpretation The parametric complexity of a model is the logarithm of the number of essentially diﬀerent, distinguishable point hypotheses within the model.

2. Two-part code interpretation For large samples, the stochastic complexity can be interpreted as a two-part codelength of the data after all, where hypotheses H are encoded with a special code that works by first discretizing the model space H into a set of ‘maximally distinguishable hypotheses’, and then assigning equal codelength to each of these.

3. Bayesian interpretation In many cases, refined MDL model selection coincides with Bayes factor model selection based on a non-informative prior such as Jeffreys’ prior \[Bernardo and Smith 1994\].

4. Prequential interpretation Refined MDL model selection can be interpreted as selecting the model with the best predictive performance when sequentially predicting unseen test data, in the sense described in Section 2.6.4. This makes it

13

an instance of Dawid’s \[1984\] prequential model validation and also relates it to cross-validation methods.

Refined MDL allows us to compare models of diﬀerent functional form. It even accounts for the phenomenon that diﬀerent models with the same number of parameters may not be equally ‘complex’:

Example 1.4 Consider two models from psychophysics describing the relationship between physical dimensions (e.g., light intensity) and their psychological counterparts (e.g. brightness) \[Myung, Balasubramanian, and Pitt 2000\]: y = axb + Z (Stevens’ model) and y = a ln(x + b) + Z (Fechner’s model) where Z is a normally distributed noise term. Both models have two free parameters; nevertheless, it turns out that in a sense, Stevens’ model is more flexible or complex than Fechner’s. Roughly speaking, this means there are a lot more data patterns that can be explained by Stevens’ model than can be explained by Fechner’s model. Myung, Balasubramanian, and Pitt \[2000\] generated many samples of size 4 from Fechner’s model, using some fixed parameter values. They then fitted both models to each sample. In 67% of the trials, Stevens’ model fitted the data better than Fechner’s, even though the latter generated the data. Indeed, in refined MDL, the ‘complexity’ associated with Stevens’ model is much larger than the complexity associated with Fechner’s, and if both models fit the data equally well, MDL will prefer Fechner’s model.

Summarizing, refined MDL removes the arbitrary aspect of crude, two-part code MDL and associates parametric models with an inherent ‘complexity’ that does not depend on any particular description method for hypotheses. We should, however, warn the reader that we only discussed a special, simple situation in which we compared a finite number of parametric models that satisfy certain regularity conditions. Whenever the models do not satisfy these conditions, or if we compare an infinite number of models, then the refined ideas have to be extended. We then obtain a ‘general’ refined MDL Principle, which employs a combination of one-part and two-part codes.

---

Full document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · Page-level evidence: [paper-pages/24-tutorial-minimum-description-length](../../paper-pages/24-tutorial-minimum-description-length/index.md)
