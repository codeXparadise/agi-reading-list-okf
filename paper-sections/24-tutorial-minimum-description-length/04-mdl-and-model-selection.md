---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
section: 1.3 MDL and Model Selection
section_role: other
section_index: 4
pages: [8, 9, 10, 11]
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "Let us recapitulate our main insights so far: MDL: The Basic Idea The goal of statistical inference may be cast as trying to find regularity in the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 1.3 MDL and Model Selection

> Section 4 of 23 from [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · `other` · pages 8-11

Let us recapitulate our main insights so far:

MDL: The Basic Idea The goal of statistical inference may be cast as trying to find regularity in the data. ‘Regularity’ may be identified with ‘ability to compress’. MDL combines these two insights by viewing learning as data compression: it tells us that, for a given set of hypotheses H and data set D, we should try to find the hypothesis or combination of hypotheses in H that compresses D most.

This idea can be applied to all sorts of inductive inference problems, but it turns out to be most fruitful in (and its development has mostly concentrated on) problems of model selection and, more generally, dealing with overfitting. Here is a standard example (we explain the diﬀerence between ‘model’ and ‘hypothesis’ after the example).

Example 1.2 \[Model Selection and Overfitting\] Consider the points in Figure 1.1. We would like to learn how the y-values depend on the x-values. To this end, we may want to fit a polynomial to the points. Straightforward linear regression will give us the leftmost polynomial - a straight line that seems overly simple: it does not capture the regularities in the data well. Since for any set of n points there exists a polynomial of the (n −1)-st degree that goes exactly through all these points, simply looking for the polynomial with the least error will give us a polynomial like the one in the second picture. This polynomial seems overly complex: it reflects the random fluctuations in the data rather than the general pattern underlying it. Instead of picking the overly simple or the overly complex polynomial, it seems more reasonable to prefer a relatively simple polynomial with small but nonzero error, as in the rightmost picture.

9

Figure 1.1: A simple, a complex and a trade-oﬀ(3rd degree) polynomial.

This intuition is confirmed by numerous experiments on real-world data from a broad variety of sources \[Rissanen 1989; Vapnik 1998; Ripley 1996\]: if one naively fits a highdegree polynomial to a small sample (set of data points), then one obtains a very good fit to the data. Yet if one tests the inferred polynomial on a second set of data coming from the same source, it typically fits this test data very badly in the sense that there is a large distance between the polynomial and the new data points. We say that the polynomial overfits the data. Indeed, all model selection methods that are used in practice either implicitly or explicitly choose a trade-oﬀbetween goodness-of-fit and complexity of the models involved. In practice, such trade-oﬀs lead to much better predictions of test data than one would get by adopting the ‘simplest’ (one degree) or most ‘complex3’ (n −1-degree) polynomial. MDL provides one particular means of achieving such a trade-oﬀ.

It will be useful to make a precise distinction between ‘model’ and ‘hypothesis’:

Models vs. Hypotheses We use the phrase point hypothesis to refer to a single probability distribution or function. An example is the polynomial 5x2 + 4x + 3. A point hypothesis is also known as a ‘simple hypothesis’ in the statistical literature. We use the word model to refer to a family (set) of probability distributions or functions with the same functional form. An example is the set of all seconddegree polynomials. A model is also known as a ‘composite hypothesis’ in the statistical literature. We use hypothesis as a generic term, referring to both point hypotheses and models.

In our terminology, the problem described in Example 1.2 is a ‘hypothesis selection problem’ if we are interested in selecting both the degree of a polynomial and the corresponding parameters; it is a ‘model selection problem’ if we are mainly interested in

10

selecting the degree.

To apply MDL to polynomial or other types of hypothesis and model selection, we have to make precise the somewhat vague insight ‘learning may be viewed as data compression’. This can be done in various ways. In this section, we concentrate on the earliest and simplest implementation of the idea. This is the so-called two-part code version of MDL:

Crude4, Two-part Version of MDL Principle (Informally Stated) Let H(1), H(2), . . . be a list of candidate models (e.g., H(k) is the set of k-th degree polynomials), each containing a set of point hypotheses (e.g., individual polynomials). The best point hypothesis H ∈H(1) ∪H(2) ∪. . . to explain the data D is the one which minimizes the sum L(H) + L(D|H), where

• L(H) is the length, in bits, of the description of the hypothesis; and

• L(D|H) is the length, in bits, of the description of the data when encoded with the help of the hypothesis.

The best model to explain D is the smallest model containing the selected H.

Example 1.3 \[Polynomials, cont.\] In our previous example, the candidate hypotheses were polynomials. We can describe a polynomial by describing its coeﬃcients in a certain precision (number of bits per parameter). Thus, the higher the degree of a polynomial or the precision, the more5 bits we need to describe it and the more ‘complex’ it becomes. A description of the data ‘with the help of’ a hypothesis means that the better the hypothesis fits the data, the shorter the description will be. A hypothesis that fits the data well gives us a lot of information about the data. Such information can always be used to compress the data (Section 2.2). Intuitively, this is because we only have to code the errors the hypothesis makes on the data rather than the full data. In our polynomial example, the better a polynomial H fits D, the fewer bits we need to encode the discrepancies between the actual y-values yi and the predicted y-values H(xi). We can typically find a very complex point hypothesis (large L(H)) with a very good fit (small L(D|H)). We can also typically find a very simple point hypothesis (small L(H)) with a rather bad fit (large L(D|H)). The sum of the two description lengths will be minimized at a hypothesis that is quite (but not too) ‘simple’, with a good (but not perfect) fit.

11

---

Full document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · Page-level evidence: [paper-pages/24-tutorial-minimum-description-length](../../paper-pages/24-tutorial-minimum-description-length/index.md)
