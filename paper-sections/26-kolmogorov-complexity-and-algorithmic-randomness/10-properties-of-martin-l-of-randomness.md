---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
section: "3.4. Properties of Martin-L¨of randomness"
section_role: other
section_index: 10
pages: [78, 79, 80, 81, 82, 83]
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "The Strong Law of Large Numbers also provides an example of an effective null set (with respect to the uniform measure). Theorem 32. A set of all bit…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.4. Properties of Martin-L¨of randomness

> Section 10 of 11 from [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md) · `other` · pages 78-83

The Strong Law of Large Numbers also provides an example of an effective null
set (with respect to the uniform measure).
Theorem 32. A set of all bit sequences that do no have limit frequency 1/2 is
an effectively null set with respect to the uniform measure.
Proof. It is enough to prove that for every rational 𝜀 > 0 the set of all
sequences such that frequency of ones is greater than 1/2 + 𝜀 infinitely many times
(or less than 1/2 − 𝜀 infinitely many times) is an effective null set.
Indeed, the upper bound for the measure of this set achieved in the proof of
the Strong Law of Large Numbers in the previous section (Theorem 27, p. 70) is
effective: the set of intervals was the set of all sufficiently long strings with large
frequency deviation, and its total measure was effectively bounded by a tail of the
converging geometric series. 
The statement of this theorem can be reformulated as the property of individual
ML-random sequences:
Theorem 33. Let 𝜔 = 𝜔0𝜔1 . . . be a ML-random sequence with respect to the
uniform measure. Then
lim
𝑛→∞
𝜔0 + 𝜔1 + . . . + 𝜔𝑛−1
𝑛 = 1
2 .
The similar statement is true for arbitrary Bernoulli measure. Let 𝑝 and 𝑞 be
computable positive reals such that 𝑝 + 𝑞 = 1. Consider the Bernoulli measure
with parameters 𝑞 and 𝑝 (the sequence of independent coin tossing with success
probability 𝑝). It is easy to check that this is a computable measure (since 𝑝 and 𝑞
are computable).

80 3. MARTIN-L ¨OF RANDOMNESS
Theorem 34. Any ML-random sequence with respect to Bernoulli measure
with computable parameters 𝑞, 𝑝 has limit frequency 𝑝.
Proof. Indeed, the upper bound for the probability of large deviations (ob-
tained by comparing the given Bernoulli measure with the other one, with shifted
𝑝, see Problem 67, p. 72), gives an explicit bound and an explicit set of intervals,
so we get an effectively null set. 
There are several other properties of ML-randomness with respect to the uni-
form measure:
Theorem 35. Let 𝜔 be a ML-random sequnce with respect to the uniform
measure. Then any other sequence which is obtained from 𝜔 by a finite number of
insertions/deletions/changes, is also ML-random.
Proof. It is enough to show that adding a zero/one in the beginning of a
ML-random sequence or deleting the first term of a ML-random sequence gives a
ML-random sequence. Indeed, assume that sequence 𝜔 is not ML-random, i.e.,
forms an effectively null singleton: for each 𝜀 one can effective construct a covering
by intervals with total measure less than 𝜀. Let us add zero at the beginning of
all these intervals (i.e., the corresponding strings). We get a covering for 0𝜔 whose
measure is twice smaller. This argument shows that if 𝜔 is not ML-random, then
0𝜔 is not ML-random either. (Similar argument works for 1𝜔.)
On the other hand, if we delete the first bit of all strings that form a covering
for 𝜔, we get a family of intervals of twice larger measure that covers 𝜔′ (obtained
from 𝜔 by deleting the first bit). Therefore, 𝜔′ is not ML-random, too. 
81 Prove that by replacing all zeros by ones and vice versa in a ML-random
sequence (with respect to the uniform measure) we get a ML-random sequence.
The folllowing problem shows that a computable subsequence of a ML-random
sequence is ML-random.
82 Let 𝑛0, 𝑛1, 𝑛2, . . . be a computable sequence of different integers (𝑛𝑖̸ = 𝑛𝑗
if 𝑖̸ = 𝑗). Let 𝜔 = 𝜔0𝜔1𝜔2 . . . be a ML-random sequence. Then its subsequence
𝜔|𝑛 = 𝜔𝑛0 𝜔𝑛1 𝜔𝑛2 . . .
is ML-random. [Hint: any interval Ω𝑥 in a cover for 𝜔|𝑛 produces a finite family of
intervals whose union is the set of sequences whose (𝑛0, 𝑛1, . . . , 𝑛𝑖−1)-subsequence
coincides with 𝑥 (here 𝑖 is the length of the string 𝑥). The total measure of these
intervals equals 2−𝑖, the measure of Ω𝑥.]
More general selection rules are consider in Chapter 9 (p. 273) where the fre-
quency approach to the notion of randomness (von Mises’ approach) is considered.
83 Let 𝜔 be a ML-random sequence with respect to the uniform measure. Let
us split 𝜔 into two-bit blocks and then replace blocks 00 by zeros and blocks 01, 10
and 11 by ones. Prove that the resulting sequence is ML-random with respect to
Bernoulli measure with parameters 1/4, 3/4. [Hint. We described a transformation
𝐹 : Ω → Ω. The preimage of any open set 𝑈 is open, and the uniform measure of
that preimage equals the (1/4, 3/4)-measure of the set 𝑈 .]
84 (Continued.) Prove that every ML-random sequence with respect to the
nonuniform Bernoulli (1/4, 3/4)-measure can be obtained in this way from a se-
quence that is ML-random with respect to the uniform measure. [Hint: For any

3.4. PROPERTIES OF MARTIN-L ¨OF RANDOMNESS 81
open set 𝐵 ⊂ Ω consider the set 𝐵′ of all sequences 𝜔 such that 𝐹 −1({𝜔}) ⊂ 𝐵
(the set of sequences that do not have a preimage outside 𝐵, i.e., the complement
to the image of the complement of 𝐵). The image of a compact set is a compact
set, therefore 𝐵′ is open. Show that if 𝐵 is a union of an enumerable family of
intervals, then 𝐵′ is also a union of enumerable family of intervals, and Bernoulli
measure of 𝐵′ does not exceed the uniform measure of 𝐵. See also the proof of a
more general statement (Theorem 123, p. 195).]
What can be said about the “complexity” of a ML-random sequence (with
respect to the uniform measure) from the viewpoint of the recursion theory? We
know already that ML-random sequence is not computable. It also cannot be
a characteristic function of an enumerable (recursively enumerable, computably
enumerable) set.
Theorem 36. Let 𝐴 be an enumerable set of natural numbers. Consider its
characteristic sequence 𝑎0𝑎1𝑎2 . . . (𝑎𝑖 = 0 for 𝑖 /∈ 𝐴 and 𝑎𝑖 = 1 for 𝑖 ∈ 𝐴). This
sequence is not ML-random.
Proof. Let 𝑘 be an arbitrary natural number. Let us enumerate the set 𝐴
and see what happens with 𝑘 first bits of its characteristic sequences. As (the
current version of) 𝐴 increases, we get more and more ones in this 𝑘-bit prefix. In
this way we get at most 𝑘 + 1 candidates; at some point we come to a final (true)
one, but we never know that this happened already. Anyway, the set of candidates
is enumerable and the number of candidates does not exceed 𝑘 + 1 (since 𝑘-bit
prefix can have 0 . . . 𝑘 ones). The total measure of these intervals is (𝑘 + 1)/2𝑘 and
therefore can be made arbitrarily small. (Note that the definition of the effectively
null set allows us to enumerate the intervals that form a covering, and this is exactly
what we can do in our case.) 
A natural question arises: in what sense one can provide explicitly a ML-
random sequence? As we have seen, neither computable sequences nor character-
istic sequences of enumerable sets are random. If you are familiar with the basics
of the recursion theory (see, e.g., [182]), you may appreciate the following result:
there exist a ML-random sequence that belongs to the class Σ2 ∩ Π2 of the arith-
metic hierarchy (this class can be also described as the class of all 0′-computable
sequences).
Theorem 37. There exists a 0′-computable sequence that is ML-random with
respect to the uniform measure.
Proof. It is enough to show that for any enumerable set of strings {𝑥0, 𝑥1, . . .}
such that∑︀ 2−𝑙(𝑥𝑖) < 1/2 there exists a 0′-computable sequence that does not have
any of 𝑥𝑖 as a prefix. (Indeed, the largest effective null set has such a covering with
total measure less than 1/2, and any sequence that is not covered is ML-random.)
The intervals Ω𝑥𝑖 are divided into two groups: some of them belong to the left
half of Ω (i.e., 𝑥𝑖 starts with 0) and some belong to the right half. Total measure of
both groups at most 1/2. Therefore, at least one of the groups has total measure
at most 1/4. However, looking at the sequence 𝑥𝑖, we cannot find out which half
has this property (since at any moment new large interval can arrive).
However, 0′-oracle allows us to make this choice, since the event “measure
exceeds 1/4” is enumerable. Then we divide this half into two parts of size 1/4

82 3. MARTIN-L ¨OF RANDOMNESS
each and choose one of them where the total measure of corresponding intervals
does not exceed 1/8, and so on.
In this way we get a 0′-computable sequence with the following property: each
its prefix is at most half-covered by our intervals. In particular, no prefix of this
sequence can appear in the sequence 𝑥𝑖, and this is what we need. 
A similar but more geometric argument can be given if we consider reals in [0, 1]
instead of binary sequences. A point 𝑥 ∈ [0, 1] is ML-random with respect to the
Lebesgue measure on [0, 1] if its binary representation is ML-random with respect to
the uniform measure on the Cantor space. (A point can have two representations
but in this case both are computable and non-random, so we may ignore this
problem.) One can also give an equivalent definition of randomness directly. A set
𝑋 ⊂ [0, 1] is called an effectively null subset of [0, 1] if there exists an algorithm
that for every rational 𝜀 > 0 enumerates a cover of 𝑋 that consists of intervals with
rational endpoints whose sum of measures is less than 𝜀. Then a ML-random real
is a real not contained in any effectively null subset of [0, 1]. All this is just a simple
reformulation of corresponding notions and results for Cantor space since the only
difference is that some numbers have two representations (but this happens only
for countably many computable reals), and that we consider intervals with rational
endpoints instead of intervals with dyadic-rational endpoints (this does not matter
since we can split an interval with rational endpoints into a computable sequence
of dyadic intervals). In particular, the following statement is true:
85 Prove that there exists the largest effectively null subset of [0, 1], and its
elements are reals whose binary representations are not ML-random with respect
to the uniform measure in the Cantor space.
Now we can point out an “explicit” ML-random point. Consider an enumerable
family of open intervals that have total length less than 1 and cover all non-ML-
random points. The union of this intervals is an open set which is a proper subset
of [0, 1]. Its complement is a closed set, and this closed set has a minimal point.
By construction this point is ML-random.
86 Prove that the minimal point that is not covered by enumerable family of
open intervals with rational endpoints is lower semicomputable, i.e., it is a limit of
an increasing computable sequence of rational numbers (and therefore is computable
with the oracle for halting problem, 0′).
(See Section 5.7 (p. 170) for more details about random reals and for an alter-
native construction of a lower semicomputable ML-random real.)
The proof of Theorem 37 given above is a relativized version of the following
result:
87 Assume that 𝑥0, 𝑥1, 𝑥2, . . . is a computable sequence of binary strings and
the sum	∑︁
𝑖
2−𝑙(𝑥𝑖)
is less than 1 and is a computable real number. Then there exists a computable
sequence of zeros and ones that has neither of 𝑥𝑖 as its prefix.
[Hint: Let this sum be less than some rational 𝑆 < 1. By induction construct
a computable sequence 𝜔0𝜔1𝜔2 . . . with the following property: the fraction of the
set 𝑈 = ∪Ω𝑥𝑖 among the sequences that have prefix 𝜔0 . . . 𝜔𝑘 is less than 𝑆.]

3.4. PROPERTIES OF MARTIN-L ¨OF RANDOMNESS 83
This problem is related to the definition of randomness suggested by C. Schnorr
in [165]. He gave a more restrictive definition of an effectively null set than Martin-
L¨of. The additional requirement: for every (rational) 𝜀 > 0 the total measure of
corresponding intervals is not only less than 𝜀 but also is a computable real (and the
approximation algorithm computably depends on 𝜀). This requirement is equivalent
to the following one: for every 𝜀 > 0 and 𝛿 > 0 one can effectively find out how
many terms in the series∑︀ 𝑖 𝑝(𝑥(𝜀, 𝑖)) are needed to make the tail less than 𝛿.
(For a series with non-negative terms the computability of sum is equivalent to
computable convergence.)
By Schnorr effectively null sets we mean the effectively null sets according
to this modified definition. (Schnorr calls them total rekursive Nullmenge, see
Definition 8.1 in [165]; effectively null sets (as in the Martin-L¨of defintion) are
called rekursive Nullmenge, see Definition 4.1.)
88 Let us change the definition of an effectively null set in another way: now
we require that the total measure of all intervals in the covering is exactly 𝜀. Show
that this definition is equivalent to the definition of Schnorr effectively null set.
(One can also consider the measure of the union of all intervals instead of the sum
of measures.)
Problem 87 shows that for every Schorr effectively null set there exists a com-
putable sequence outside this set. (For simplicity let us consider the case of uniform
measure.) On the other hand, every computable sequence (i.e., the singleton made
of it) is a Schnorr effectively null set. Therefore, none of the Schnorr effectively
null sets is the largest one in the class (in other words, the union of all Schnorr
effectively null sets is not a Schnorr effectively null set). Nevertheless we can call a
sequence which does not belong to any Schnorr null set a Schnorr random sequence
(or “Schnorr typical” sequence).
Since now we have less effectively null sets, we may get the broader class of
random sequences, and it is indeed the case. The following problem (together with
the results of Chapter 5) guarantees that there exist Schnorr random sequences
that are not Martin-L¨of random.
89 Prove that there exists a Schnorr random sequence 𝜔 = 𝜔0𝜔1𝜔2 . . . whose
prefixes have logarithmic complexity, i.e., 𝐶(𝜔0 . . . 𝜔𝑛−1) = 𝑂(log 𝑛).
[Hint: Problem 87 shows how one can construct a computable sequence that
does not belong to a given Schnorr effectively null set. At some point of this
construction we can take into account another Schnorr effectively null set and get
a computable sequence that does not belong to both. (Indeed, we need to take a
sufficiently small cover for the second set that does not go out of the safety margin
in the construction for the first set.) Moreover, we can consider infinitely many
Schnorr effectively null sets in this way (adding them one after another). This will
not give us a computable Schnorr random sequnce (it does not exist at all), because
we need additional information that says us which algorithms correspond to Schnorr
effectively null sets and which do not. But if we postpone the introduction of a new
algorithm until the moment when the constructed prefix of our sequence is rather
long, this additional information is logarithmic compared to the prefix length.]
We return to Schnorr’s definition of randomness in Section 9.8 where it is
reformulated in terms of computable martingales.

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

---

Full document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md) · Page-level evidence: [paper-pages/26-kolmogorov-complexity-and-algorithmic-randomness](../../paper-pages/26-kolmogorov-complexity-and-algorithmic-randomness/index.md)
