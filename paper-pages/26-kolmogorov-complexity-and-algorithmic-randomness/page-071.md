---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 71
pages: [71]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "72 3. MARTIN-L ¨OF RANDOMNESS terms, 𝑆(𝑥) = 𝑞𝑢𝑝𝑣 for a string 𝑥 that has 𝑢 zeros and 𝑣 ones (here 𝑞 = 1/2 − 𝜀 is the probability of zero outcome).…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 71 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 71 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

72 3. MARTIN-L ¨OF RANDOMNESS
terms, 𝑆(𝑥) = 𝑞𝑢𝑝𝑣 for a string 𝑥 that has 𝑢 zeros and 𝑣 ones (here 𝑞 = 1/2 − 𝜀 is
the probability of zero outcome). The ratio 𝑆(𝑥)/𝐿(𝑥) increases when the number
of ones in 𝑥 increases, and for all bad strings this ratio is at least 2𝑛/2𝐻(𝑝,𝑞)𝑛.
Therefore, the total 𝐿-measure of all bad strings does not exceed their total 𝑆-
measure divided by this lower bound. Recalling that the total 𝑆-measure of all bad
strings does not exceed 1, we conclude that the total 𝐿-measure (i.e., the fraction)
of all bad strings does not exceed 2𝐻(𝑝,𝑞)𝑛/2𝑛. So we get another proof of our bound,
which is less technical (though more difficult to find). This proof works not only for
the uniform Bernoulli measure (𝑝 = 1/2), but also for arbitrary 𝑝 (after appropriate
changes).
67 Prove the Strong Law of Large Numbers for arbitrary 𝑝. [Hint: Let
𝑝0 and 𝑞0 be fixed positive reals such that 𝑝0 + 𝑞0 = 1. Then the expression
−𝑝0 log 𝑝 − 𝑞0 log 𝑞, where 𝑝, 𝑞 are arbitrary positive reals such that 𝑝 + 𝑞 = 1, is
minimal when 𝑝 = 𝑝0, 𝑞 = 𝑞0. See also Section 9.6, p. 287.]
People often say that “the Strong Law of Large Numbers guarantees that in
every random (with respect to uniform Bernoulli measure) sequence the frequency
of 1s tends to 1/2”. (The case of nonuniform Bernoulli measures is similar.) How-
ever, in this sentence the word “random” should not be understood literally: the
phrase “every random sequence satisfies 𝛼” (for some condition 𝛼) is an idiomatic
expression that means that the set of all sequences that do not satisfy 𝛼 is a null
set.
A natural question arises: can we define the notion of random sequence in such
a way that this idiomatic expression can be understood literally? Let us fix some
distribution on Ω, say, the uniform Bernoulli distribution. We would like to find
some subset of Ω and call its elements “random sequences”. Our goal would be
achieved if for any condition 𝛼 the following two statements were equivalent:
∙ all random sequences satisfy the condition 𝛼;
∙ the set of all sequences that does not satisfy 𝛼 is a null set.
In other terms, the sets of measure 1 should be exactly those sets that contain
all random sequences (and, may be, some nonrandom ones).
One more reformulation: the set of all random sequences should be the smallest
(with respect to inclusion) set of measure 1, and the set of non-random sequences
should be the largest (with respect to inclusion) null set. Now it easy to see that
our goal cannot be achieved. Indeed, any singleton in Ω is a null set. However, the
union of all these singletons is the entire space Ω.
In 1965 Per Martin-L¨of (a Swedish mathematician, who was Kolmogorov’s
student at that time) found that we can save the game if we restrict ourselves to
“effectively null sets”. There exist a largest (with respect to inclusion) effectively
null set, and therefore we can define the notion of a random sequence is such a way
that any condition 𝛼 is satisfied for all random sequences if and only if the set of all
sequences that do not satisfy 𝛼 is an effectively null set. Martin-L¨of construction
is explained in the next section.
### 3.3. Effectively null sets
Let a measure on Ω be fixed and let 𝑝(𝑥) be the measure of the interval Ω𝑥.

---

[previous page](page-070.md) · [next page](page-072.md) · [all pages](index.md)
