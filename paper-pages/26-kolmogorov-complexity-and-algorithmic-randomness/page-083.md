---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 83
pages: [83]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "84 3. MARTIN-L ¨OF RANDOMNESS 90 Prove that a sequence 𝜔 is not Schnorr random if and only if there exists a computable sequence of strings 𝑥0, 𝑥1, .…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 83 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 83 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

84 3. MARTIN-L ¨OF RANDOMNESS
90 Prove that a sequence 𝜔 is not Schnorr random if and only if there exists a
computable sequence of strings 𝑥0, 𝑥1, . . . such that the series∑︀ 𝑖 𝑝(𝑥𝑖) computably
converges (has a computable sum) and infinitely many of 𝑥𝑖 are prefixes of 𝜔. [Hint:
This is a version of Theorem 31 for Schnorr randomness and can be proven in a
similar way. In fact, in this case even the standard proof of Borel–Cantelli lemma
works.]
Another version of effectively null sets is obtained if we consider only finite
families of intervals (each family is presented as the list of all intervals in the
family): given a rational 𝜀, the algorithm should output a finite list of intervals
that cover the set and have the sum of measures less than 𝜀. This corresponds to
Jordan contruction of measure often used in the elementary calculus textbooks. In
this way we get a smaller class of null sets (e.g., a null set cannot cover all rational
points).
91 Prove that a set is an effectively null set in this sense if and only if it is
contained in the complement of some effectively open set of measure 1.
The sequences not covered by any effectively null sets in this sense (=contained
in every effectively open set of full measure) are called Kurtz random. In this
definition we again restrict the class of effectively null sets and therefore enlarge
the class of random sequences. Indeed we get more random sequences, as the
following problem shows.
92 Show that every Schnorr random sequence (with respect to the uniform
measure) satisfies the Strong Law of Large Numbers, but there exists a Kurtz
random sequence that does not. [Hint: The proof of the Strong Law of Large
Numbers gives a cover with computable sum of measures since the series converges
exponentially fast. For the second part one can consider generic sequences, see
Section 5.9, p. 192.]
### 3.5. Randomness deficiencies
Martin-L¨of’s definition requires that for an effectively null set 𝐴 there is an
algorithm that, given 𝜀 > 0, produces a cover of 𝐴 by intervals whose total measure
does not exceed 𝜀. The union of these intervals in an open set of measure at most 𝜀.
In general, the unions of computable sequences of intervals are called effectively
open sets. As in the definition of effectively null sets (p. 73), we allow the com-
putable sequence to be non-total, so the empty set is also effectively open. In other
words, an effectively open set is a union of an enumerable family of intervals.
Now the definition of an effectively null set can be reformulated as follows:
Theorem 38. A set 𝐴 is an effectively null set with respect to a measure 𝜇 if
and only if 𝐴 ⊂⋂︀ 𝑛 𝑈𝑛 for some uniformly effectively open sets 𝑈𝑛 with 𝜇(𝑈𝑛) 6
2−𝑛. We may assume also that 𝑈1 ⊃ 𝑈2 ⊃ . . . .
Speaking about “uniformly effectively open sets”, we mean that there exists an
algorithm that, given 𝑛, enumerates a family of intervals whose union is 𝑈𝑛.
Proof. There are several differences between this definition and the one we
used earlier. First difference (a trivial one) is that we use only 𝜀 = 2−𝑛.
Second, we speak here about the measure of an effectively open set, not about
the sum of measures of intervals whose union it is. This does not matter either, since
we may assume without loss of generality that the intervals forming an effectively

---

[previous page](page-082.md) · [next page](page-084.md) · [all pages](index.md)
