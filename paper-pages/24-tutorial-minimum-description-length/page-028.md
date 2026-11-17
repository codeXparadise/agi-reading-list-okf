---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 28
pages: [28]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "New Definition of Code Length Function In MDL we are NEVER concerned with actual encodings; we are only concerned with code length functions. The set…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 28 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 28 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

New Definition of Code Length Function

In MDL we are NEVER concerned with actual encodings; we are only concerned with code length functions. The set of all codelength functions for finite or countable sample space Z is defined as:

2−L(z) ≤1

X

LZ =

L : Z →\[0, ∞\] |

, (2.4)

z∈X

or equivalently, LZ is the set of those functions L on Z such that there exists a function Q with P

z Q(z) ≤1 and for all z, L(z) = −log Q(z). (Q(z) = 0 corresponds to L(z) = ∞). Again, Z usually represents a sample of n outcomes: Z = X n (n ≥1) where X is the sample space for one observation.

Figure 2.2: Code lengths are probabilities.

mass functions, such that a short codelength corresponds to a high probability and vice versa. Furthermore, as we will see, in MDL we are not interested in the details of actual encodings C(z); we only care about the code lengths LC(z). It is so useful to think about these as log-probabilities, and so convenient to allow for non-integer nonprobabilities, that we will simply redefine prefix code length functions as (defective) probability mass functions that can have non-integer code lengths – see Figure 2.2. The following example illustrates idealized codelength functions and at the same time introduces a type of code that will be frequently used in the sequel:

Example 2.4 ‘Almost’ Uniform Code for the Positive Integers Suppose we want to encode a number k ∈{1, 2, . . . }. In Example 2.3, we saw that in order to encode a number between 1 and M, we need log M bits. What if we cannot determine the maximum M in advance? We cannot just encode k using the uniform code for {1, . . . , k}, since the resulting code would not be prefix. So in general, we will need more than log k bits. Yet there exists a prefix-free code which performs ‘almost’ as well as log k. The simplest of such codes works as follows. k is described by a codeword starting with ⌈log k⌉0s. This is followed by a 1, and then k is encoded using the uniform code for {1, . . . , 2⌈log k⌉}. With this protocol, a decoder can first reconstruct ⌈log k⌉by counting all 0’s before the leftmost 1 in the encoding. He then has an upper bound on k and can use this knowledge to decode k itself. This protocol uses less than 2⌈log k⌉+ 1 bits. Working with idealized, non-integer code-lengths we can simplify this to 2 log k + 1 bits. To see this, consider the function P(x) = 2−2 log x−1. An easy

29

---

[previous page](page-027.md) · [next page](page-029.md) · [all pages](index.md)
