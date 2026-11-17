---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 25
pages: [25]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "We already designed a code C for the elements in X. The natural thing to do is to encode (x1, . . . , xn) by the concatenated string C(x1)C(x2) . . .…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 25 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 25 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

We already designed a code C for the elements in X. The natural thing to do is to encode (x1, . . . , xn) by the concatenated string C(x1)C(x2) . . . C(xn). In order for this method to succeed for all n, all (x1, . . . , xn) ∈X n, the resulting procedure must define a code, i.e. the function C(n) mapping (x1, . . . , xn) to C(x1)C(x2) . . . C(xn) must be invertible. If it were not, we would have to use some marker such as a comma to separate the codewords. We would then really be using a ternary rather than a binary alphabet.

Since we always want to construct codes for sequences rather than single symbols, we only allow codes C such that the extension C(n) defines a code for all n. We say that such codes have ‘uniquely decodable extensions’. It is easy to see that (a) every prefix code has uniquely decodable extensions. Conversely, although this is not at all easy to see, it turns out that (b), for every code C with uniquely decodable extensions, there exists a prefix code C0 such that for all n, xn ∈X n, LC(n)(xn) = LC(n)

0 (xn) \[Cover

and Thomas 1991\]. Since in MDL we are only interested in code-lengths, and never in actual codes, we can restrict ourselves to prefix codes without loss of generality.

Thus, the restriction to prefix code may also be understood as a means to send concatenated messages while avoiding the need to introduce extra symbols into the alphabet.

Whenever in the sequel we speak of ‘code’, we really mean ‘prefix code’. We call a prefix code C for a set X complete if there exists no other prefix code that compresses at least one x more and no x less then C, i.e. if there exists no code C′ such that for all x, LC′(x) ≤LC(x) with strict inequality for at least one x.

2.2.2 The Kraft Inequality - Codelengths and Probabilities, Part I

In this subsection we relate prefix codes to probability distributions. Essential for understanding the relation is the fact that no matter what code we use, most sequences cannot be compressed, as demonstrated by the following example:

Example 2.2 \[Compression and Small Subsets: Example 1.2, Continued.\] In Example 1.2 we featured the following three sequences:

00010001000100010001 . . . 0001000100010001000100010001 (2.1)

01110100110100100110 . . . 1010111010111011000101100010 (2.2)

00011000001010100000 . . . 0010001000010000001000110000 (2.3)

We showed that (a) the first sequence - an n-fold repetition of 0001 - could be substantially compressed if we use as our code a general-purpose programming language (assuming that valid programs must end with a halt-statement or a closing bracket, such codes satisfy the prefix property). We also claimed that (b) the second sequence, n independent outcomes of fair coin tosses, cannot be compressed, and that (c) the third sequence could be compressed to αn bits, with 0 < α < 1. We are now in a position to prove statement (b): strings which are ‘intuitively’ random cannot be substantially

26

---

[previous page](page-024.md) · [next page](page-026.md) · [all pages](index.md)
