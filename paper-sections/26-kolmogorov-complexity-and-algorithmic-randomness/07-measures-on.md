---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
section: "3.1. Measures on Ω"
section_role: other
section_index: 7
pages: [66, 67, 68]
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "Consider the set Ω = BN whose elements are infinite sequences of zeros and ones. This set is called Cantor space. For a binary string 𝑥 we consider a…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.1. Measures on Ω

> Section 7 of 11 from [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md) · `other` · pages 66-68

Consider the set Ω = BN whose elements are infinite sequences of zeros and
ones. This set is called Cantor space. For a binary string 𝑥 we consider a set Ω𝑥 of
all infinite sequences that have initial segment 𝑥. For example, Ω00 is the set of all
sequences that start with two zeros, and ΩΛ = Ω (where Λ is the empty string).
The sets Ω𝑥 are called intervals. All intervals and all unions of arbitrary families
of intervals are called open subsets of Ω. In this way we get a topology on Ω, and
this topology corresponds to a standard distance function on Ω defined as follows:
the longer common prefix two sequences 𝜔 = 𝜔0𝜔1 . . . and 𝜔′ = 𝜔′
0𝜔′
1 . . . have, the
smaller the distance between them is:
𝑑(𝜔, 𝜔′) = 2−𝑛,
where 𝑛 is the smallest index such that 𝜔𝑛̸ = 𝜔′
𝑛.
66 Prove that topological space Ω is homeomorphic to the Cantor set on the
real line. (This set is obtained from [0, 1] by deleting the middle third, then the
middle thirds of two remaining segments and so on.)
However, we are interested in measure theory rather than topology. A family
of subsets of Ω is called a 𝜎-algebra if it is closed under finite or countable unions
and intersections, and under negation (taking the complement).
A minimal 𝜎-algebra that contains all intervals Ω𝑥 (and therefore all open sets)
is called the algebra of Borel sets.
Consider an arbitrary 𝜎-algebra that contains all intervals. Let 𝜇 be a function
that maps every set in this 𝜎-algebra into a non-negative real number, and has the
following property (called 𝜎-additivity):
if a set 𝐴 is a union of a countable or finite family of disjoint
sets 𝐴0, 𝐴1, 𝐴2, . . . that belong to the 𝜎-algebra on which 𝜇 is
defined, then
𝜇(𝐴) = 𝜇(𝐴0) + 𝜇(𝐴1) + 𝜇(𝐴2) + . . .
(the right-hand side is a finite sum or a converging series with
non-negative terms).
67

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

3.2. THE STRONG LAW OF LARGE NUMBERS 69
∙ The definition does not change if we restrict ourselves to rational values
of 𝜀 (or even let 𝜀 = 2−𝑘 for integer 𝑘).
∙ Any subset of a null set is a null set.
∙ A finite or countable union of null sets is a null set. (Indeed, to cover the
union by a family of intervals of total measure less than 𝜀, we combine
the covers of its parts that have measure less than 𝜀/2, 𝜀/4, 𝜀/8 etc.).
∙ Assume that 𝑝 is chosen in such a way that any singleton is a null set
(it is equivalent to the following property: for any infinite sequence 𝜔 =
𝜔0𝜔1𝜔2 . . . the limit of 𝑝(𝜔0 . . . 𝜔𝑛) (as 𝑛 → ∞) equals 0). Then every
finite or countable set is a null set.
A uniform measure on Ω assigns to each interval Ω𝑥 the number 2−𝑙(𝑥):
𝑝(𝑥) = 2−𝑛 for all strings 𝑥 of length 𝑛.
The uniform measure is closely related to the standard measure on R (or, more
precisely, on [0, 1]). Formally, the measure of a set 𝐴 ⊂ Ω is equal to the measure
of the set of reals whose binary expansions are elements of 𝐴. (In fact, the cor-
respondence between infinite binary fractions and reals in [0, 1] is not a bijection,
since numbers of the form 𝑘/2𝑙 for integer 𝑘 and 𝑙 have two representations: e.g.,
0.01111 . . . = 0.10000 . . . But this happens only for a countable family of reals and
measure theory easily ignores this.)
Indeed, the reals whose binary expansions start with 𝑥, form an interval, and
the length of this interval is 2−𝑛 where 𝑛 is the length of 𝑥. This implies that for
every interval 𝐼 ⊂ [0, 1] the uniform measure of the sequences that represent reals
in 𝐼 is equal to the length of the interval 𝐼.
Probability theory describes the uniform distribution as the probability distri-
bution for the outcomes of independent fair coin tossing. Indeed, for 𝑛 independent
fair coin tossings all 2𝑛 binary strings of length 𝑛 appear with the same probability
2−𝑛. The set Ω𝑥 is the event “a random sequence of zeros and ones starts with 𝑥”,
and this event has probability 2−𝑙(𝑥).
Similarly, we may consider a biased coin assuming that coin tossings are still in-
dependent. The corresponding measure (probability distribution) is called Bernoulli
measure (or Bernoulli distribution) with parameters 𝑞, 𝑝 (probabilities of 0 and 1
respectively; we assume that 𝑝, 𝑞 > 0, and 𝑝 + 𝑞 = 1).
With respect to this distribution, the event “sequence 𝜔 starts with a string
𝑥” has probability 𝑞𝑢𝑝𝑣 where 𝑢 and 𝑣 are the numbers of zeros and ones in 𝑥. In
other terms, we consider a function
𝑥 ↦ → 𝑞𝑢(𝑥)𝑝𝑣(𝑥)
where 𝑢(𝑥) and 𝑣(𝑥) stand for the numbers of zeros and ones in 𝑥, respectively. (It
is easy to check that this function has the additivity property.)

---

Full document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md) · Page-level evidence: [paper-pages/26-kolmogorov-complexity-and-algorithmic-randomness](../../paper-pages/26-kolmogorov-complexity-and-algorithmic-randomness/index.md)
