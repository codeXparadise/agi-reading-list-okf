---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 67
pages: [67]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "68 3. MARTIN-L ¨OF RANDOMNESS Then 𝜇 is called a measure on Ω, and the value 𝜇(𝐴) is called the measure of the set 𝐴. The set 𝐴 for which 𝜇(𝐴) is…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 67 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 67 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

68 3. MARTIN-L ¨OF RANDOMNESS
Then 𝜇 is called a measure on Ω, and the value 𝜇(𝐴) is called the measure of the
set 𝐴. The set 𝐴 for which 𝜇(𝐴) is defined, is called 𝜇-measurable.
A measure 𝜇 such that 𝜇(Ω) = 1 is called a probability distribution on Ω.
Elements of the 𝜎-algebra that is the domain of 𝜇 are called events, and 𝜇(𝐴) is
called the probability of the event 𝐴.
Any measure is monotone (𝐴 ⊂ 𝐵 implies 𝜇(𝐴) 6 𝜇(𝐵)). Indeed,
𝜇(𝐵) − 𝜇(𝐴) = 𝜇(𝐵 ∖ 𝐴) > 0.
Another important property of measures is continuity: if a set 𝐵 is a union of
increasing sequence of sets
𝐵0 ⊂ 𝐵1 ⊂ 𝐵2 ⊂ . . . ,
then 𝜇(𝐵𝑛) tends to 𝜇(𝐵) as 𝑛 → ∞. (Indeed, let us apply the additivity property
to all sets 𝐴𝑖 = 𝐵𝑖 ∖ 𝐵𝑖−1 and then to all sets 𝐴𝑖 such that 𝑖 6 𝑛.) The similar
property holds for decreasing sequences of sets.
For any measure 𝜇 on Ω let us consider a function 𝑝 defined of binary strings
as follows:
𝑝(𝑥) = 𝜇(Ω𝑥).
This function has non-negative real values and satisfies the following additivity
property:
𝑝(𝑥) = 𝑝(𝑥0) + 𝑝(𝑥1)
for any string 𝑥. (Indeed, the interval Ω𝑥 is the union of its two halves Ω𝑥0 and
Ω𝑥1, which are disjoint sets.)
As we know from measure theory (Lebesgue’s theorem), an inverse transition
is possible. Namely, for every additive function 𝑝 on binary strings that has non-
negative real values, the Lebesgue theorem provides a measure 𝜇 such that 𝜇(Ω𝑥) =
𝑝(𝑥) for all binary strings 𝑥.
The measure provided by Lebesgue theorem has the following additional prop-
erty: if 𝜇(𝐴) = 0 for some set 𝐴 and 𝐵 ⊂ 𝐴, then 𝜇(𝐵) is defined (and therefore
𝜇(𝐵) = 0). In the sequel we consider only measures that have this additional
property.
We do not explain Lebesgue’s construction here and refer the reader to any
textbook in measure theory, e.g., [80, 63]. However, let us recall the definition of
sets having measure 0, since Martin-L¨of definition of randomness uses its effective
version.
Let 𝑝 be an additive nonnegative real-valued function on strings. We call 𝑝(𝑥)
the measure of the interval Ω𝑥. A subset 𝐴 ⊂ Ω is a null set (a set of measure 0)
if for every 𝜀 > 0 there exist a finite or countable family of intervals that cover 𝐴
and have total measure at most 𝜀.
In other words, a set 𝐴 is a null set if there exists a function ⟨𝜀, 𝑖⟩ ↦ → 𝑥(𝜀, 𝑖)
(first argument is a positive real, the second argument is a non-negative integer;
values are binary strings) such that
∙ 𝐴 ⊂ Ω𝑥(𝜀,0) ∪ Ω𝑥(𝜀,1) ∪ Ω𝑥(𝜀,2) . . . and
∙ 𝑝(𝑥(𝜀, 0)) + 𝑝(𝑥(𝜀, 1)) + 𝑝(𝑥(𝜀, 2)) + . . . 6 𝜀
for every positive 𝜀. Note that the family of intervals can be finite, since we do not
require the function 𝑥 to be total (undefined values are skipped both in the union
and in the sum).
Here are some simple but useful observations:

---

[previous page](page-066.md) · [next page](page-068.md) · [all pages](index.md)
