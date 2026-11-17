---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 8
pages: [8]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "achieved by using description methods that are less expressive than general-purpose computer languages. Such description methods C should be…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 8 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 8 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

achieved by using description methods that are less expressive than general-purpose computer languages. Such description methods C should be restrictive enough so that for any data sequence D, we can always compute the length of the shortest description of D that is attainable using method C; but they should be general enough to allow us to compress many of the intuitively ‘regular’ sequences. The price we pay is that, using the ‘practical’ MDL Principle, there will always be some regular sequences which we will not be able to compress. But we already know that there can be no method for inductive inference at all which will always give us all the regularity there is — simply because there can be no automated method which for any sequence D finds the shortest computer program that prints D and then halts. Moreover, it will often be possible to guide a suitable choice of C by a priori knowledge we have about our problem domain. For example, below we consider a description method C that is based on the class of all polynomials, such that with the help of C we can compress all data sets which can meaningfully be seen as points on some polynomial.

## 1.3 MDL and Model Selection

Let us recapitulate our main insights so far:

MDL: The Basic Idea The goal of statistical inference may be cast as trying to find regularity in the data. ‘Regularity’ may be identified with ‘ability to compress’. MDL combines these two insights by viewing learning as data compression: it tells us that, for a given set of hypotheses H and data set D, we should try to find the hypothesis or combination of hypotheses in H that compresses D most.

This idea can be applied to all sorts of inductive inference problems, but it turns out to be most fruitful in (and its development has mostly concentrated on) problems of model selection and, more generally, dealing with overfitting. Here is a standard example (we explain the diﬀerence between ‘model’ and ‘hypothesis’ after the example).

Example 1.2 \[Model Selection and Overfitting\] Consider the points in Figure 1.1. We would like to learn how the y-values depend on the x-values. To this end, we may want to fit a polynomial to the points. Straightforward linear regression will give us the leftmost polynomial - a straight line that seems overly simple: it does not capture the regularities in the data well. Since for any set of n points there exists a polynomial of the (n −1)-st degree that goes exactly through all these points, simply looking for the polynomial with the least error will give us a polynomial like the one in the second picture. This polynomial seems overly complex: it reflects the random fluctuations in the data rather than the general pattern underlying it. Instead of picking the overly simple or the overly complex polynomial, it seems more reasonable to prefer a relatively simple polynomial with small but nonzero error, as in the rightmost picture.

9

---

[previous page](page-007.md) · [next page](page-009.md) · [all pages](index.md)
