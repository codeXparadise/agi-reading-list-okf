---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
section: 3.5. Randomness deficiencies
section_role: other
section_index: 11
pages: [83, 84]
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "Martin-L¨of’s definition requires that for an effectively null set 𝐴 there is an algorithm that, given 𝜀 0, produces a cover of 𝐴 by intervals whose…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.5. Randomness deficiencies

> Section 11 of 11 from [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md) · `other` · pages 83-84

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

3.5. RANDOMNESS DEFICIENCIES 85
open set are disjoint. (When a new interval app

---

Full document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md) · Page-level evidence: [paper-pages/26-kolmogorov-complexity-and-algorithmic-randomness](../../paper-pages/26-kolmogorov-complexity-and-algorithmic-randomness/index.md)
