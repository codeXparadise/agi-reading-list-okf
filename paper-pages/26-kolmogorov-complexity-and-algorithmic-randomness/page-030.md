---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 30
pages: [30]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "1.1. THE DEFINITION AND MAIN PROPERTIES 31 We have used several times the upper bound 2𝑛 for the number of strings 𝑥 with 𝐶(𝑥) < 𝑛. Note that, in…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 30 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 30 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

1.1. THE DEFINITION AND MAIN PROPERTIES 31
We have used several times the upper bound 2𝑛 for the number of strings 𝑥
with 𝐶(𝑥) < 𝑛. Note that, in contrast to other bounds, it involves no constants.
Nevertheless this bound has a hidden dependence on the choice of the optimal
description mode: if we switch to another optimal description mode, the set of
strings 𝑥 such that 𝐶(𝑥) < 𝑛 can change!
2 Show that the number of strings of complexity less than 𝑛 is in the range
[2𝑛−𝑐; 2𝑛] for some constant 𝑐 for all 𝑛. [Hint: the upper bound 2𝑛 is proved in
Introduction, the lower bound is implied by the inequality 𝐶(𝑥) 6 𝑙(𝑥) + 𝑐: the
complexity of all the strings of length less than 𝑛 − 𝑐 is less than 𝑛.]
Show that the number of strings of complexity exactly 𝑛 does not exceed 2𝑛
but can be much less: e.g., it is possible that this set is empty for infinitely many 𝑛.
[Hint: Change an optimal description mode by adding 0 or 11 to each description,
so that all descriptions have even length.]
3 Prove that the average complexity of strings of length 𝑛 is equal to 𝑛+𝑂(1).
[Hint: let 𝛼𝑘 denote the fraction of strings of complexity 𝑛 − 𝑘 among strings of
length 𝑛. Then the average compexity is by∑︀ 𝑘 𝑘𝛼𝑘 less than 𝑛. Use the inequality
𝛼𝑘 6 2−𝑘 and the convergence of the series∑︀ 𝑘/2𝑘.]
In the next statement we establish a formal relation between upper bounds of
complexity and upper bounds of cardinality.
Theorem 7. (a) The family of sets 𝑆𝑛 = {𝑥 | 𝐶(𝑥) < 𝑛} is enumerable and
|𝑆𝑛| < 2𝑛 for all 𝑛. Here |𝑆𝑛| denotes the cardinality of 𝑆𝑛.
(b) If 𝑉𝑛 (𝑛 = 0, 1, . . . ) is an enumerable family of sets of strings and |𝑉𝑛| < 2𝑛
for all 𝑛, then there exists 𝑐 such that 𝐶(𝑥) < 𝑛 + 𝑐 for all 𝑛 and all 𝑥 ∈ 𝑉𝑛.
In this theorem we use the notion of an enumerable family of sets. It is de-
fined as follows. A set of strings (or natural numbers, or other finite objects) is
enumerable (= computably enumerable = recursively enumerable) if there is an al-
gorithm generating all elements of this set in some order. This means that there
is a program that never terminates and prints all the elements of the set in some
order. The intervals between printing elements can be arbitrarily large; if the set is
finite, the program can print nothing after some time (unknown to the observer).
Repetitions are allowed but this does not matter since we can filter the output and
delete the elements that have already been printed.
For example, the set of all 𝑛 such that the decimal expansion of √2 has exactly
𝑛 consecutive nines is enumerable. The following algorithm generates the set: com-
pute decimal digits of √2 starting with the most significant ones. Once a sequence
of consecutive 𝑛 nines surrounded by non-nines is found, print 𝑛 and continue.
A family of sets 𝑉𝑛 is called enumerable if the set of pairs {⟨𝑛, 𝑥⟩ | 𝑥 ∈ 𝑉𝑛}
is enumerable. This implies that each of the sets 𝑉𝑛 is enumerable. Indeed, to
generate elements of the set 𝑉𝑛 for a fixed 𝑛 we run the algorithm enumerating the
set {⟨𝑛, 𝑥⟩ | 𝑥 ∈ 𝑉𝑛} and print the second components of all the pairs that have 𝑛
as the first component. However, the converse statement is not true. For instance,
assume that 𝑉𝑛 is finite for every 𝑛. Then every 𝑉𝑛 is enumerable, but at the same
time it may happen that the set {⟨𝑛, 𝑥⟩ | 𝑥 ∈ 𝑉𝑛} is not enumerable (say 𝑉𝑛 = {0}
if 𝑛 ∈ 𝑆 and 𝑉𝑛 = ∅ otherwise, where 𝑆 is any non-enumerable set of integers).
One can verify that a family is enumerable if and only if there is an algorithm that
given any 𝑛 finds a program generating 𝑉𝑛. A detailed study of enumerable sets
can be found in every textbook on computability theory, for instance, in [182].

---

[previous page](page-029.md) · [next page](page-031.md) · [all pages](index.md)
