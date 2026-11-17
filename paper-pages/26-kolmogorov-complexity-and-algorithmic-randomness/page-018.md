---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 18
pages: [18]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "NON-COMPUTABILITY OF 𝐶 AND BERRY’S PARADOX 19 randomness deficiency is close to 1/2. This translation implies the original state- ment since most of…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 18 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 18 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

NON-COMPUTABILITY OF 𝐶 AND BERRY’S PARADOX 19
randomness deficiency is close to 1/2. This translation implies the original state-
ment since most of the strings have small randomness deficiency. We will see later
that actually these formulations are equivalent.
If we insist on drawing a strict borderline between random and non-random
objects, we have to consider infinite sequences instead of strings. The notion of
randomness for infinite sequences of zeros and ones was defined by Kolmogorov’s
student P. Martin-L¨of (he came to Moscow from Sweden). We discuss it in Section 3.
Later C. Schnorr and L. Levin found a characterization of randomness in terms of
complexity: an infinite binary sequence is random if and only if the randomness
deficiency of its prefixes is bounded by a constant. This criterion, however, uses
another version of Kolmogorov complexity called monotone complexity.
Non-computability of 𝐶 and Berry’s paradox
Before discussing applications of Kolmogorov complexity, let us mention a fun-
damental problem that reappears in any application. Unfortunately, the function 𝐶
is not computable: there is no algorithm that given a string 𝑥 finds its Kolmogorov
complexity. Moreover, there is no computable nontrivial (unbounded) lower bound
for 𝐶.
Theorem 6. Let 𝑘 be a computable (not necessarily total ) function from Ξ
to N. (In other words, 𝑘 is an algorithm that terminates on some binary strings
and returns natural numbers as results.) If 𝑘 is a lower bound for Kolmogorov
complexity, that is, 𝑘(𝑥) 6 𝐶(𝑥) for all 𝑥 such that 𝑘(𝑥) is defined, then 𝑘 is
bounded: all its values do not exceed some constant.
The proof of this theorem is a reformulation of the so-called “Berry’s paradox”.
This paradox considers
the minimal natural number that cannot be defined by at most
fourteen English words.
This phrase has exactly fourteen words and defines that number. Thus we get a
contradiction.
Following this idea consider the first binary string whose Kolmogorov complexity
is greater than a given number 𝑁 . By definition, its complexity is greater than 𝑁 .
On the other hand, this string has a short description that includes some fixed
amount of information plus the binary notation of 𝑁 (which requires about log2 𝑁
bits), and the total number of bits needed is much less than 𝑁 for large 𝑁 . That
would be a contradiction if we knew how to effectively find this string given its
description. Using the computable lower bound 𝑘, we can convert this paradox into
the proof.
Proof. Consider the function 𝐵(𝑁 ) whose argument 𝑁 is a natural number;
it is computed by the following algorithm:
perform in parallel the computations 𝑘(Λ), 𝑘(0), 𝑘(1), 𝑘(00),
𝑘(01), 𝑘(10), 𝑘(11), . . . until some string 𝑥 such that 𝑘(𝑥) > 𝑁
appears; then return 𝑥.
If the function 𝑘 is unbounded then the function 𝐵 is total and 𝑘(𝐵(𝑁 )) > 𝑁
by construction for every 𝑁 . As 𝑘 is a lower bound for 𝐾, we have 𝐶(𝐵(𝑁 )) > 𝑁 .
On the other hand 𝐵(𝑁 ) can be computed given the binary representation bin(𝑁 )

---

[previous page](page-017.md) · [next page](page-019.md) · [all pages](index.md)
