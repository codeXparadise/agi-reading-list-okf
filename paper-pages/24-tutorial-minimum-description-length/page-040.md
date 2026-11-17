---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 40
pages: [40]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "The reasoning is now as follows: we think that one of the P ∈M will assign a high likelihood to the data to be observed. Therefore we would like to…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 40 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 40 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

The reasoning is now as follows: we think that one of the P ∈M will assign a high likelihood to the data to be observed. Therefore we would like to design a code that, for all xn we might observe, performs essentially as well as the code corresponding to the best-fitting, maximum likelihood (minimum codelength) P ∈M for xn. Similarly, we can think of universal codes such as the two-part code in terms of the (possibly defective, see Section 2.2 and Figure 2.1)) distributions corresponding to it. Such distributions corresponding to universal codes are called universal models. The use of mapping universal codes back to distributions is illustrated by the Bayesian universal model which we now introduce.

Universal model: Twice Misleading Terminology The words ‘universal’ and ‘model’ are somewhat of a misnomer: first, these codes/models are only ‘universal’ relative to a restricted ‘universe’ M. Second, the use of the word ‘model’ will be very confusing to statisticians, who (as we also do in this paper) call a family of distributions such as M a ’model’. But the phrase originates from information theory, where a ‘model’ often refers to a single distribution rather than a family. Thus, a ‘universal model’ is a single distribution, representing a statistical ‘model’ M.

Example 2.12 \[Bayesian Universal Model\] Let M be a finite or countable set of probabilistic sources, parameterized by some parameter set Θ. Let W be a distribution on Θ. Adopting terminology from Bayesian statistics, W is usually called a prior distribution. We can construct a new probabilistic source ¯PBayes by taking a weighted (according to W) average or mixture over the distributions in M. That is, we define for all n, xn ∈X,

P(xn | θ)W(θ). (2.12)

¯PBayes(xn) :=

X

θ∈Θ

It is easy to check that ¯PBayes is a probabilistic source according to our definition. In case Θ is continuous, the sum gets replaced by an integral but otherwise nothing changes in the definition. In Bayesian statistics, ¯PBayes is called the Bayesian marginal likelihood or Bayesian mixture \[Bernardo and Smith 1994\]. To see that ¯PBayes is a universal model, note that for all θ0 ∈Θ,

P(xn | θ)W(θ) ≤−log P(xn | θ0) + cθ0 (2.13)

−log ¯PBayes(xn) := −log

X

θ∈Θ

where the inequality follows because a sum is at least as large as each of its terms, and cθ = −log W(θ) depends on θ but not on n. Thus, ¯PBayes is a universal model or equivalently, the code with lengths −log ¯PBayes is a universal code. Note that the derivation in (2.13) only works if Θ is finite or countable; the case of continuous Θ is treated in Section 2.6.

41

---

[previous page](page-039.md) · [next page](page-041.md) · [all pages](index.md)
