---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
section: 3.2. The Strong Law of Large Numbers
section_role: other
section_index: 8
pages: [68, 69, 70, 71]
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "To see all these notions in action, let us state and prove the so-called Strong Law of Large Numbers. Fix some 𝑝, 𝑞 0 such that 𝑝 + 𝑞 = 1. Let 𝐴𝑝 be…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.2. The Strong Law of Large Numbers

> Section 8 of 11 from [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md) · `other` · pages 68-71

To see all these notions in action, let us state and prove the so-called Strong
Law of Large Numbers.
Fix some 𝑝, 𝑞 > 0 such that 𝑝 + 𝑞 = 1. Let 𝐴𝑝 be the set of all infinite sequences
𝜔0𝜔1𝜔2 . . . of zeros and ones such that limit frequency of ones exists and is equal
to 𝑝, i.e.,
lim
𝑛→∞
𝜔0 + 𝜔1 + . . . + 𝜔𝑛−1
𝑛 = 𝑝.

70 3. MARTIN-L ¨OF RANDOMNESS
Theorem 27. The set 𝐴𝑝 has measure 1 with respect to Bernoulli distribution
with parameters 𝑝 and 𝑞.
In other terms, the complement of 𝐴𝑝, i.e., the set of all sequences that either
do not have limit frequency at all or have a limit frequency different from 𝑝, is a
null set (according to this distribution).
Proof. We prove this theorem for the uniform case (i.e., for 𝑝 = 𝑞 = 1/2) by
an explicit calculation. The general case is left as an exercise (see also Section 9.6).
Let us consider first a finite number of coin tossings and fix some 𝑛. All
binary strings of length 𝑛 have the same probability. We claim that most of them
have approximately 𝑛/2 ones. Assume that some threshold 𝜀 is fixed. How many
sequences have more than (1/2 + 𝜀)𝑛 ones? The answer can be found using the
Pascal triangle: we have to sum up all the terms in the 𝑛th row starting from some
point that is slightly on the right of the midpoint. In this part we have a decreasing
sequence of less than 𝑛 terms, so the sum in question is bounded by the first term
multiplied by 𝑛. (We do not need to be very accurate in our bounds and ignore
factors that are polynomial in 𝑛. So we can omit the factor 𝑛 in our bound.)
The first term of the sum is the binomial coefficient
𝑛!
𝑘!(𝑛 − 𝑘)! ,
where 𝑘 is the smallest integer not less than (1/2 + 𝜀)𝑛. We use the Stirling’s
approximation:
𝑚! =√︀ (2𝜋 + 𝑜(1))𝑚
(︁
 
𝑚
𝑒
)︁
𝑚
,
where 𝑒 is the base of natural logarithms. Ignoring polynomial (in 𝑛) factors and
using the notation 𝑢 = 𝑘/𝑛, 𝑣 = (𝑛 − 𝑘)/𝑛, we get
𝑛!
𝑘!(𝑛 − 𝑘)! ≈ (𝑛/𝑒)𝑛
(𝑘/𝑒)𝑘((𝑛 − 𝑘)/𝑒)𝑛−𝑘 = 𝑛𝑛
𝑘𝑘(𝑛 − 𝑘)𝑛−𝑘 =
= 𝑛𝑛
(𝑢𝑛)𝑢𝑛(𝑣𝑛)𝑣𝑛 = 1
𝑢𝑢𝑛𝑣𝑣𝑛 = 2𝐻(𝑢,𝑣)𝑛,
where
𝐻(𝑢, 𝑣) = −𝑢 log 𝑢 − 𝑣 log 𝑣.
The value 𝐻(𝑢, 𝑣) is called the Shannon entropy of the random variable that has
two values whose probabilities are 𝑢 and 𝑣. (We study the Shannon entropy in
Chapter 7.) Figure 1 shows the corresponding graph (note that 𝑣 = 1 − 𝑢). It
is easy to check that 𝐻(𝑢, 1 − 𝑢) achieves its maximal value (equal to 1) only
at 𝑢 = 1/2.
Now we see that the number of binary strings of length 𝑛 that have frequency of
ones greater than (1/2 + 𝜀) does not exceed poly(𝑛)2𝐻(1/2+𝜀,1/2−𝜀)𝑛 and therefore
is bounded by 2𝑐𝑛+𝑜(𝑛), where 𝑐 is some constant less than 1 (depending on 𝜀).
Therefore, the fraction of these strings (among all strings of length 𝑛) exponentially
decreases as 𝑛 increases. The same is true for the strings that have frequency of
ones less than (1/2 − 𝜀).
Let us see where we are. For each fixed 𝜀 > 0 we have proved the following
statement:

3.2. THE STRONG LAW OF LARGE NUMBERS 71
0 1	1/2 𝑢
1
𝐻(𝑢, 1 − 𝑢)
Figure 1. Shannon entropy as a function of 𝑢.
Lemma. The fraction of strings of length 𝑛 where frequency of ones differs
from 1/2 at least by 𝜀 (among all strings of length 𝑛) does not exceed some 𝛿𝑛 that
decreases exponentially as 𝑛 increases.
This lemma (without any specific claims for the fast convergence 𝛿𝑛 → 0) is
called the Law of Large Numbers. To prove the Strong Law of Large Numbers we
need to know that the series∑︀ 𝑛 𝛿𝑛 is convergent.
We need to prove that the set 𝐴1/2 of all sequences that have limit frequency
of ones equal to 1/2 has measure 1. In other terms, we need to prove that the
complement of this set (we denote this complement by 𝐵) is a null set.
According to the definition of limit the set 𝐵 is the union (over all 𝜀 > 0) of
the sets 𝐵𝜀. Here 𝐵𝜀 is the set of all sequences such that frequency of ones in their
prefixes exceeds 1/2 + 𝜀 (or is less than 1/2 − 𝜀) infinitely many times.
Evidently, we can consider only a countable set of different 𝜀 (e.g., only rational
values), and the countable union of null sets is a null set. Therefore it remains to
prove that the set 𝐵𝜀 is a null set for each 𝜀.
The set 𝐵𝜀 consists of the sequences that have arbitrarily long “bad” prefixes.
Here “bad” prefix is a string where the frequency of ones differs from 1/2 more
than by 𝜀. Therefore, for each 𝑁 the set 𝐵𝜀 is covered by the family of intervals
Ω𝑥 where 𝑥 ranges over all bad strings of length at least 𝑁 . The total (uniform)
measure of all this intervals does not exceed
𝛿𝑁 + 𝛿𝑁 +1 + 𝛿𝑁 +2 + . . . ,
and this sum can be made small since the series∑︀ 𝑖 𝛿𝑖 is convergent.
(Probability theorists call this argument Borel–Cantelli lemma. In its general
form this lemma says that if the sum of measures of some sets 𝐴0, 𝐴1, . . . is finite,
then the set of all points that belong to infinitely many 𝐴𝑖 is a null set.) 
One can get a bound for the number of bad strings of length 𝑛 without Stirling’s
approximation. We do it separately for bad strings that have too many and too few
ones. For example, let us consider the set of all “bad” strings that have frequency
of ones greater than 1/2 + 𝜀. To get a bound for the cardinality of this set, consider
two distributions (measures) on the set of all strings of length 𝑛. The first one,
called 𝐿, is the uniform distribution: all strings have probability 2−𝑛. The second
one, called 𝑆, is biased (ones are more likely than zeros) and corresponds to 𝑛
independent coin tossing where 1 appears with probability 𝑝 = 1/2 + 𝜀. In other

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

---

Full document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md) · Page-level evidence: [paper-pages/26-kolmogorov-complexity-and-algorithmic-randomness](../../paper-pages/26-kolmogorov-complexity-and-algorithmic-randomness/index.md)
