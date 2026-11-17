---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 24
pages: [24]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "Basic notions and notations This section is intended for people who are already familiar with some notions of Kolmogorov complexity and algorithmic…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 24 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 24 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

Basic notions and notations
This section is intended for people who are already familiar with some notions
of Kolmogorov complexity and algorithmic randomness theory and want to take
a quick look at the terminology and notation used throughout this book. Other
readers can (and probably should) skip it and look back only when needed.
The set of all integer numbers is denoted by Z, the notation N refers to the
set of all non-negative integers (i.e. natural numbers), R stands for the set of all
reals. The set of all rational numbers is denoted by Q. Dyadic rationals are those
rationals having the form 𝑚/2𝑛 for some integer 𝑚 and 𝑛.
The cardinality of a set 𝐴 is denoted by |𝐴|.
When the base of the logarithmic function is omitted, it is assumed that the
base equals 2, thus log 𝑥 means the same as log2 𝑥 (as usual, ln 𝑥 denotes the natural
logarithm).
We use the notation ⌊𝑥⌋ for the integer part of a real number 𝑥 (the largest
integer number that is less than or equal to 𝑥). Similarly, ⌈𝑥⌉ denotes the smallest
integer number that is larger than or equal to 𝑥.
Order of magnitudes. The notation 𝑓 6 𝑔+𝑂(1), where 𝑓 and 𝑔 are expressions
containing variables, means that for some 𝑐 the inequality 𝑓 6 𝑔 + 𝑐 holds for all
values of variables. In a similar way we understand the expression 𝑓 6 𝑔 + 𝑂(ℎ)
(where ℎ is non-negative): it means that for some 𝑐 for all values of variables the
inequality 𝑓 6 𝑔 + 𝑐ℎ holds. The notation 𝑓 = 𝑔 + 𝑂(ℎ) (where ℎ in non-negative)
means that for some 𝑐 for all values of variables we have |𝑓 − 𝑔| 6 𝑐ℎ. In particular,
𝑓 = 𝑂(ℎ) holds if |𝑓 | 6 𝑐ℎ for some constant 𝑐; the notation 𝑓 = Ω(ℎ) means that
|𝑓 | > 𝑐ℎ for some constant 𝑐 > 0 (usually 𝑓 is positive). The notation 𝑓 = Θ(ℎ)
means that 𝑐1ℎ 6 |𝑓 | 6 𝑐2ℎ (again, usually 𝑓 is positive).
B denotes the set {0, 1}. Finite sequences of 0s and 1s are called binary strings.
The set of all binary strings is denoted by Ξ. If 𝐴 is a finite set (an alphabet) then
𝐴𝑛 denotes the set of all strings of length 𝑛 over the alphabet 𝐴, that is, the set
of all sequences of length 𝑛, whose terms belong to 𝐴. We denote by 𝐴* the set
of all strings over the alphabet 𝐴 (including the empty string Λ of length 0). For
instance, Ξ = B*. The length of a string 𝑥 is denoted by 𝑙(𝑥). The notation 𝑎𝑏
refers to the concatenation of strings 𝑎 and 𝑏, that is, the result of appending 𝑏
to 𝑎. We say that a string 𝑎 is a prefix of a string 𝑏 if 𝑏 = 𝑎𝑥 for some string 𝑥. We
say that 𝑎 is a suffix of a string 𝑏 if 𝑏 = 𝑥𝑎 for some string 𝑥. We say that 𝑎 is a
substring of 𝑏, if 𝑏 = 𝑥𝑎𝑦 for some strings 𝑥 and 𝑦 (in other words, 𝑎 is a suffix of
a prefix of 𝑏 or the other way around).
We consider also infinite sequences of zeros and ones and Ω denotes the set of
all such sequences. The set of infinite sequences of elements of a set 𝐴 is denoted
by 𝐴∞, thus Ω = B∞. For a finite sequence 𝑥 we use the notation Ω𝑥 for the set
of all infinite sequences that start with 𝑥 (i.e., have 𝑥 as a prefix); sets of this form
25

---

[previous page](page-023.md) · [next page](page-025.md) · [all pages](index.md)
