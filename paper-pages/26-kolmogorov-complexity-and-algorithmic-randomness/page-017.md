---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 17
pages: [17]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "18 WHAT IS THIS BOOK ABOUT? elements as equiprobable, then we obtain a ridiculously small value (less than 1000 bits); for the non-uniform…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 17 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 17 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

18 WHAT IS THIS BOOK ABOUT?
elements as equiprobable, then we obtain a ridiculously small value (less than 1000
bits); for the non-uniform distributions the entropy is even less.
So we see that in these contexts Kolmogorov complexity looks like a more
adequate tool than Shannon entropy.
Complexity and randomness
Let us recall the inequality 𝐶(𝑥) 6 𝑙(𝑥) + 𝑂(1) (Theorem 2). For most of
the strings its left hand side is close to the right hand side. Indeed, the following
statement is true:
Theorem 5. Let 𝑛 be an integer. Then there are less than 2𝑛 strings 𝑥 such
that 𝐶(𝑥) < 𝑛.
Proof. Let 𝐷 be the optimal description mode used in the definition of Kol-
mogorov complexity. Then only strings 𝐷(𝑦) for all 𝑦 such that 𝑙(𝑦) < 𝑛 have
complexity less than 𝑛. The number of such strings does not exceed the number of
strings 𝑦 such that 𝑙(𝑦) < 𝑛, i.e., the sum
1 + 2 + 4 + 8 + . . . + 2𝑛−1 = 2𝑛 − 1
(there are 2𝑘 strings for each length 𝑘 < 𝑛). 
This implies that the fraction of strings of complexity less than 𝑛 − 𝑐 among all
strings of length 𝑛 is less than 2𝑛−𝑐/2𝑛 = 2−𝑐. For instance, the fraction of strings
of complexity less than 90 among all strings of length 100 is less than 2−10.
Thus the majority of strings (of a given length) are incompressible or almost
incompressible. In other words, a randomly chosen string of the given length is
almost incompressible. This can be illustrated by the following mental (or even
real) experiment. Toss a coin, say, 80000 times and get a sequence of 80000 bits.
Convert it into a file of size 10000 bytes (8 bits = 1 byte). One can bet that no
compression software (existing before the start of the experiment) can compress the
resulting file by more than 10 bytes. Indeed, the probability of this event is less
than 2−80 for every fixed compressor, and the number of (existing) compressors is
not so large.
It is natural to consider incompressible strings as “random” ones: informally
speaking, randomness is the absence of any regularities that may allow us to com-
press the string. Of course, there is no strict borderline between “random” and
“non-random” strings. It is ridiculous to ask which strings of length 3 (i.e., 000,
001, 010, 011, 100, 101, 110, 111) are random and which are not.
Another example: assume that we start with a “random” string of length 10000
and replace its bits by all zeros (one bit at a step). At the end we get a certainly
non-random string (zeros only). But it would be na¨ıve to ask at which step the
string has become non-random for the first time.
Instead, we can naturally define the “randomness deficiency” of a string 𝑥 as
the difference 𝑙(𝑥) − 𝐶(𝑥). Using this notion, we can restate Theorem 2 as follows:
the randomness deficiency is almost non-negative (i.e., larger than a constant).
Theorem 5 says that the randomness deficiency of a string of length 𝑛 is less than
𝑑 with probability at least 1 − 1/2𝑑 (assuming that all strings are equiprobable).
Now consider the Law of Large Numbers; it says that most of the 𝑛-bit strings
have frequency of ones close to 1/2. This law can be translated into Kolmogorov
complexity language as follows: the frequency of ones in every string with small

---

[previous page](page-016.md) · [next page](page-018.md) · [all pages](index.md)
