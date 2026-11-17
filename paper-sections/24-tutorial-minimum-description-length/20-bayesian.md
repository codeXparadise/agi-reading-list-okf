---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
section: "Bayesian:"
section_role: other
section_index: 20
pages: [66, 67, 68]
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "according to in expectation codes optimal codes optimal in worst−case sense statistical more than length for log loss only of D inference, e.g.…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Bayesian:

> Section 20 of 23 from [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · `other` · pages 66-68

according to in expectation codes optimal codes optimal in worst−case sense

statistical more than

length

for log loss only

of D

inference, e.g. prequential probability

subjective prior

Figure 2.6: Rissanen’s MDL, Wallace’s MML and Dawid’s Prequential Approach.

Indeed, Wallace and his co-workers stress that their approach is fully (subjective) Bayesian. Strictly speaking, a Bayesian should report his findings by citing the full posterior distribution. But sometimes one is interested in a single model, or hypothesis for the data. A good example is the inference of phylogenetic trees in biological applications: the full posterior would consist of a mixture of several of such trees, which might all be quite diﬀerent from each other. Such a mixture is almost impossible to interpret – to get insight in the data we need a single tree. In that case, Bayesians often use the MAP (Maximum A Posteriori) hypothesis which maximizes the posterior, or the posterior mean parameter value. The first approach has some unpleasant properties, for example, it is not invariant under reparameterization. The posterior mean approach cannot be used if diﬀerent model families are to be compared with each other. The MML method provides a theoretically sound way of proceeding in such cases.

2.9.3 MDL, Prequential Analysis and Cross-Validation

In a series of papers, A.P. Dawid \[1984, 1992, 1997\] put forward a methodology for probability and statistics based on sequential prediction which he called the prequential approach. When applied to model selection problems, it is closely related to MDL Dawid proposes to construct, for each model M(j) under consideration, a ‘probability forecasting system’ (a sequential prediction strategy) where the i + 1-st outcome is predicted based on either the Bayesian posterior ¯PBayes(θ|xi) or on some estimator

ˆθ(xi). Then the model is selected for which the associated sequential prediction strategy minimizes the accumulated prediction error. Related ideas were put forward by Hjorth \[1982\] under the name forward validation and Rissanen \[1984\]. From Section 2.6.4 we see that this is just a form of MDL - strictly speaking, every universal code can be thought of as as prediction strategy, but for the Bayesian and the plug-in universal models (Sections 2.6.3, 2.6.4) the interpretation is much more natural than for others20. Dawid mostly talks about such ‘predictive’ universal models. On the other hand, Dawid’s framework allows to adjust the prediction loss to be measured in terms of arbitrary loss functions, not just the log loss. In this sense, it is more general than MDL. Finally, the prequential idea goes beyond statistics: there is also a ‘prequential approach’ to probability theory developed by Dawid \[Dawid and Vovk 1999\] and Shafer

67

and Vovk \[2001\].

Note that the prequential approach is similar in spirit to cross-validation. In this sense MDL is related to cross-validation as well. The main diﬀerences are that in MDL and the prequential approach, (1) all predictions are done sequentially (the future is never used to predict the past), and (2) each outcome is predicted exactly once.

2.9.4 Kolmogorov Complexity and Structure Function; Ideal MDL

Kolmogorov complexity \[Li and Vit´anyi 1997\] has played a large but mostly inspirational role in Rissanen’s development of MDL. Over the last fifteen years, several ‘idealized’ versions of MDL have been proposed, which are more directly based on Kolmogorov complexity theory \[Barron 1985; Barron and Cover 1991; Li and Vit´anyi 1997; Vereshchagin and Vit´anyi 2002\]. These are all based on two-part codes, where hypotheses are described using a universal programming language such as C or Pascal. For example, in one proposal \[Barron and Cover 1991\], given data D one picks the distribution minimizing

K(P) +

−log P(D)

, (2.43)

where the minimum is taken over all computable probability distributions, and K(P) is the length of the shortest computer program that, when input (x, d), outputs P(x) to d bits precision. While such a procedure is mathematically well-defined, it cannot be used in practice. The reason is that in general, the P minimizing (2.43) cannot be eﬀectively computed. Kolmogorov himself used a variation of (2.43) in which one adopts, among all P with K(P) −log P(D) ≈K(D), the P with smallest K(P). Here K(D) is the Kolmogorov complexity of D, that is, the length of the shortest computer program that prints D and then halts. This approach is known as the Kolmogorov structure function or minimum suﬃcient statistic approach \[Vit´anyi 2004\]. In this approach, the idea of separating data and noise (Section 2.6.1) is taken as basic, and the hypothesis selection procedure is defined in terms of it. The selected hypothesis may now be viewed as capturing all structure inherent in the data - given the hypothesis, the data cannot be distinguished from random noise. Therefore, it may be taken as a basis for lossy data compression – rather than sending the whole sequence, one only sends the hypothesis representing the ‘structure’ in the data. The receiver can then use this hypothesis to generate ‘typical’ data for it - this data should then ‘look just the same’ as the original data D. Rissanen views this separation idea as perhaps the most fundamental aspect of ‘learning by compression’. Therefore, in recent work he has tried to relate MDL (as defined here, based on lossless compression) to the Kolmogorov structure function, thereby connecting it to lossy compression, and, as he puts it, ‘opening up a new chapter in the MDL theory’ \[Vereshchagin and Vit´anyi 2002; Vit´anyi 2004; Rissanen and Tabus 2004\].

Summary and Outlook We have shown that MDL is closely related to, yet distinct from, several other methods for inductive inference. In the next section we discuss how

68

well it performs compared to such other methods.

---

Full document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · Page-level evidence: [paper-pages/24-tutorial-minimum-description-length](../../paper-pages/24-tutorial-minimum-description-length/index.md)
