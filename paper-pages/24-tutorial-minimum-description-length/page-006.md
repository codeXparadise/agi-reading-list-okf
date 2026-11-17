---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 6
pages: [6]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "...and Compression We claimed that any regularity detected in the data can be used to compress the data, i.e. to describe it in a short manner.…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 6 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 6 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

...and Compression We claimed that any regularity detected in the data can be used to compress the data, i.e. to describe it in a short manner. Descriptions are always relative to some description method which maps descriptions D′ in a unique manner to data sets D. A particularly versatile description method is a general-purpose computer language like C or Pascal. A description of D is then any computer program that prints D and then halts. Let us see whether our claim works for the three sequences above. Using a language similar to Pascal, we can write a program

for i = 1 to 2500; print ‘0001‘; next; halt

which prints sequence (1) but is clearly a lot shorter. Thus, sequence (1) is indeed highly compressible. On the other hand, we show in Section 2.2, that if one generates a sequence like (2) by tosses of a fair coin, then with extremely high probability, the shortest program that prints (2) and then halts will look something like this:

print ‘011101001101000010101010........1010111010111011000101100010‘; halt

This program’s size is about equal to the length of the sequence. Clearly, it does nothing more than repeat the sequence.

The third sequence lies in between the first two: generalizing n = 10000 to arbitrary length n, we show in Section 2.2 that the first sequence can be compressed to O(log n) bits; with overwhelming probability, the second sequence cannot be compressed at all; and the third sequence can be compressed to some length αn, with 0 < α < 1.

Example 1.1 \[compressing various regular sequences\] The regularities underlying sequences (1) and (3) were of a very particular kind. To illustrate that any type of regularity in a sequence may be exploited to compress that sequence, we give a few more examples:

The Number π Evidently, there exists a computer program for generating the first

n digits of π – such a program could be based, for example, on an infinite series expansion of π. This computer program has constant size, except for the specification of n which takes no more than O(log n) bits. Thus, when n is very large, the size of the program generating the first n digits of π will be very small compared to n: the π-digit sequence is deterministic, and therefore extremely regular.

Physics Data Consider a two-column table where the first column contains numbers

representing various heights from which an object was dropped. The second column contains the corresponding times it took for the object to reach the ground. Assume both heights and times are recorded to some finite precision. In Section 1.3 we illustrate that such a table can be substantially compressed by first describing the coeﬃcients of the second-degree polynomial H that expresses Newton’s law; then describing the heights; and then describing the deviation of the time points from the numbers predicted by H.

7

---

[previous page](page-005.md) · [next page](page-007.md) · [all pages](index.md)
