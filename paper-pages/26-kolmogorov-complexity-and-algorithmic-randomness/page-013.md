---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 13
pages: [13]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "14 WHAT IS THIS BOOK ABOUT? language. If 𝑦 is a shortest description of the string 𝑥 with respect to 𝑃 , then 𝑃 𝑦 is a description of 𝑥 with respect…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 13 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 13 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

14 WHAT IS THIS BOOK ABOUT?
language. If 𝑦 is a shortest description of the string 𝑥 with respect to 𝑃 , then 𝑃 𝑦
is a description of 𝑥 with respect to 𝐷 (though not necessarily a shortest one).
Therefore, compared to 𝑃 , the shortest description is at most 𝑙(𝑃 ) bits longer, and
𝐶𝐷 (𝑥) 6 𝐶𝑃 (𝑥) + 𝑙(𝑃 ).
The constant 𝑙(𝑃 ) depends only on the description mode 𝑃 (and not on 𝑥). 
Basically, we used the same trick as in the preceding example, but instead
of merging two description modes we join all of them. Each description mode
is prefixed by its index (program, identifier). The same idea is used in practice.
A “self-extracting archive” is an executable file starting with a small program (a
decompressor); the rest is considered as an input to that program. This program
is loaded into the memory and then it decompresses the rest of the file.
Note that in our construction optimal decompressor works for a very long time
on some inputs (as some programs have large running time), and is undefined on
some other inputs.
Kolmogorov complexity
Fix an optimal description mode 𝐷 and call 𝐶𝐷 (𝑥) the Kolmogorov complexity
of the string 𝑥. In the notation 𝐶𝐷 (𝑥) we drop the subscript 𝐷 and write just 𝐶(𝑥).
If we switch to another optimal description mode, the change in complexity is
bounded by an additive constant: for every optimal description modes 𝐷1 and 𝐷2
there is a constant 𝑐(𝐷1, 𝐷2) such that
|𝐶𝐷1 (𝑥) − 𝐶𝐷2 (𝑥)| 6 𝑐(𝐷1, 𝐷2)
for all 𝑥. Sometimes this inequality is written as follows:
𝐶𝐷1 (𝑥) = 𝐶𝐷2 (𝑥) + 𝑂(1),
where 𝑂(1) stands for a bounded function of 𝑥.
Could we then consider the Kolmogorov complexity of a particular string 𝑥
without having in mind a specific optimal description mode used in the definition
of 𝐶(𝑥)? No, since by adjusting the optimal description mode we can make the
complexity of 𝑥 arbitrarily small or arbitrarily large. Similarly, the relation “string 𝑥
is simpler than 𝑦”, that is, 𝐶(𝑥) < 𝐶(𝑦), has no meaning for two fixed strings 𝑥
and 𝑦: by adjusting the optimal description mode we can make any of these two
strings simpler than the other one.
One may wonder then whether Kolmogorov complexity has any sense at all.
Trying to defend this notion, let us recall the construction of the optimal description
mode used in the proof of the Solomonoff–Kolmogorov theorem. This construction
uses some programming language, and two different choices of this language lead
to two complexities that differ at most by a constant. This constant is in fact the
length of the program that is written in one of these two languages and interprets
the other one. If both languages are “natural”, we can expect this constant to be
not that huge, just several thousands or even several hundreds. Therefore if we
speak about strings whose complexity is, say, about 105 (i.e., a text of a long and
not very compressible novel), or 106 (which is reasonable for DNA strings, unless
they are compressible much more than the biologists think now), then the choice
of the programming language is not that important.
Nevertheless one should always have in mind that all statements about Kol-
mogorov complexity are inherently asymptotic: they involve infinite sequences of

---

[previous page](page-012.md) · [next page](page-014.md) · [all pages](index.md)
