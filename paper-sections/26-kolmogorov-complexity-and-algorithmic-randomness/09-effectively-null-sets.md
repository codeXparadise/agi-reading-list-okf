---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
section: 3.3. Effectively null sets
section_role: other
section_index: 9
pages: [71, 72, 73, 74, 75, 76, 77, 78]
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "Let a measure on Ω be fixed and let 𝑝(𝑥) be the measure of the interval Ω𝑥. 3.3. EFFECTIVELY NULL SETS 73 We say that a set 𝐴 ⊂ Ω is an effectively…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.3. Effectively null sets

> Section 9 of 11 from [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md) · `other` · pages 71-78

Let a measure on Ω be fixed and let 𝑝(𝑥) be the measure of the interval Ω𝑥.

3.3. EFFECTIVELY NULL SETS 73
We say that a set 𝐴 ⊂ Ω is an effectively null set (with respect to the given
measure) if for every 𝜀 > 0 one can effectively find a family of intervals that cover
𝐴 and whose total measure does not exceed 𝜀.
Some details should be specified in this definition. First, we consider only
rational values of 𝜀 (otherwise it is not clear how 𝜀 could be given to an algorithm).
Second, we need to specify how the sequence of intervals (that cover 𝐴) is generated.
We do this as follows:
Definition. A set 𝐴 ⊂ Ω is called an effectively null set (with respect to a
given measure) if there exists a computable function 𝑥(·, ·) whose first argument is
a positive rational number, second argument is a natural number and values are
binary strings, such that:
(1) 𝐴 ⊂ Ω𝑥(𝜀,0) ∪ Ω𝑥(𝜀,1) ∪ Ω𝑥(𝜀,2) . . .;
(2) 𝑝(𝑥(𝜀, 0)) + 𝑝(𝑥(𝜀, 1)) + 𝑝(𝑥(𝜀, 2)) + . . . 6 𝜀
for any rational 𝜀 > 0. Note that we do not require the function 𝑥 to be total; if
𝑥(𝜀, 𝑖) is undefined, the corresponding term (in both conditions) is omitted.
68 Show that we get an equivalent version of the definition if we consider an
algorithm that gets 𝜀 > 0 as an input and enumerates a set of binary strings (by
printing its elements with arbitrary delays between elements) such that intervals
Ω𝑥 for generated 𝑥 cover 𝐴 and have total measure (the measure of the union of
the intervals) at most 𝜀. (Note that the total measure can be much smaller than
the sum of measures, if the intervals are not disjoint.)
69 Show that we get an equivalent definition if we consider only rational
numbers of the form 2−𝑘 (for integer 𝑘) instead of all rational 𝜀. Show that the
definition does not change if we replace the sign 6 by < in the second inequality.
[Hint: subtract from each interval its part covered by previous intervals, possibly
splitting it into several intervals.]
70 Show that we get an equivalent definition if we require that for each 𝜀 > 0
the domain of the function 𝑖 ↦ → 𝑥(𝜀, 𝑖) is an initial segment of N (or N itself).
71 Show that we get an equivalent definition if we require that the family
of intervals is decidable (instead of being enumerable). [Hint: An interval can
be split into small parts, so we may assume that intervals in the sequence have
non-increasing length, and the family of intervals becomes decicable.]
Let us give some examples of effectively null subsets of Ω (with respect to the
uniform measure).
A singleton whose only element is a sequence of zeros, is an effectively null
set. Indeed, for every 𝜀 > 0 we find an integer 𝑘 such that 2−𝑘 < 𝜀, and consider a
covering that consists of one interval Ω00...0 (corresponding to the string of 𝑘 zeros).
Formally speaking, 𝑥(𝜀, 0) = 0𝑘, where 0𝑘 stands for the sequence formed by
𝑘 zeros, and 𝑘 is the smallest integer such that 2−𝑘 < 𝜀. The values 𝑥(𝜀, 𝑖) are
undefined for 𝑖 > 0.
In this example the sequence 0000 . . . can be replaced by arbitrary computable
sequence of zeros and ones; we need only to consider its prefix of length 𝑘 instead
of 0𝑘.
However, for noncomputable sequences the situation could be different:
72 Prove that there exists a sequence 𝜔 ∈ Ω such that singleton {𝜔} is not
an effectively null set. [Hint: Consider all computable functions 𝑥 that satisfy

74 3. MARTIN-L ¨OF RANDOMNESS
the second condition of the definition of effectively null set. There are countably
many such functions. For each of them consider the largest set 𝐴 that satisfies the
requirement (1) of the definition (i.e., the intersection of the unions of coverings
over all 𝜀). This set is an (effectively) null set, and the union of a countable family
of those sets is a null set. Therefore, there exists a sequence 𝜔 which does not
belong to this union.]
Let us note that the statement of this problem is a straightforward corollary
of the Martin-L¨of theorem on the existence of the largest effectively null set (The-
orem 28, p. 75) proved later in this section, and the hint just follows its proof. As
we will see later, the set {𝜔} is an effectively null set if and only if the sequence 𝜔
is not “Martin-L¨of random”.
It is easy to construct a non-computable sequence 𝜔 such that the singleton {𝜔}
is an effective null set. Indeed, consider any sequence of the form 𝜔 = 0?0?0?0 . . .
(each second term is zero, the rest is arbitrary). Let us show that {𝜔} is indeed an
effectively null set. To find a covering with total measure 2−𝑛, consider all strings
of length 2𝑛 that are formed by 𝑛 arbitrary bits interleaved with 𝑛 zeros (as in 𝜔).
There are 2𝑛 strings of this form, and each corresponds to an interval of length
2−2𝑛, so the total measure is 2−𝑛.
In fact we have proved a bit more: the set of all sequences that have only
zeros at even positions, is an effectively null set. Therefore, each of its subsets (in
particular, every singleton) is an effectively null set.
Let us now return to the definition of an effectively null set and separate the
requirements used in this definition. We say that a computable function 𝑥 is “regu-
lar” if is satisfies the requirement (2). The requirement (1) then says that for every
rational 𝜀 > 0 the set 𝐴 is a subset of the union
Ω𝑥(𝜀,0) ∪ Ω𝑥(𝜀,1) ∪ Ω𝑥(𝜀,2) . . .
Therefore, a regular function “serves” all the subsets of the set⋂︁
𝜀>0
(Ω𝑥(𝜀,0) ∪ Ω𝑥(𝜀,1) ∪ Ω𝑥(𝜀,2) . . .) =⋂︁
𝜀>0
⋃︁
 𝑖
Ω𝑥(𝜀,𝑖)
So for each (computable) regular function 𝑥 we get an effectively null set (defined
by the formula above), and effectively null sets are all these sets (for all regular
functions) and all their subsets, and that’s all.
Before we formulate Martin-L¨of theorem, let us give the definition of a com-
putable measure on the set Ω.
A real number 𝛼 is called computable if there exists an algorithm that computes
rational approximations to 𝛼 with any given precision. Formally, 𝛼 is a computable
real if there exists a computable function 𝜀 ↦ → 𝑎(𝜀) defined on all positive rational
numbers and having rational values such that
|𝛼 − 𝑎(𝜀)| < 𝜀
for all rational 𝜀 > 0.
73 Show that we get an equivalent definition if we additionally require that
all approximation given by 𝑎 are approximations from below, i.e., 𝑎(𝜀) < 𝛼 for all
𝜀. [Hint: we can transform any approximation to the approximation from below
losing only factor 2 in precision.]
74 Prove that the sum, difference, product and quotient of two computable
reals are computable reals.

3.3. EFFECTIVELY NULL SETS 75
75 Prove that 𝑒 (the base of natural logarithms) and 𝜋 are computable.
76 Prove that elementary function (roots, sine, exponent, logarithm etc.) pre-
serve computability, i.e., have computable values for computable arguments. (We
assume, of course, that the base is computable in case of logarithm and exponent.)
A measure 𝜇 on Ω is computable if measures of all intervals are computable
reals, and, moreover, we can effectively find an approximation algorithm for 𝜇(Ω𝑥)
given 𝑥. Here is a formal definition:
Definition. A measure 𝜇 on the set Ω is computable if there exists a com-
putable function ⟨𝑥, 𝜀⟩ ↦ → 𝑎(𝑥, 𝜀), defined for all strings 𝑥 and all positive rational
numbers 𝜀, such that
|𝜇(Ω𝑥) − 𝑎(𝑥, 𝜀)| < 𝜀
for all 𝑥 and 𝜀.
This definition does not assume that the measure of the entire space Ω equals 1,
but in fact we will use it only in this case (i.e., for probability distributions).
Theorem 28. Let 𝜇 be a computable measure on Ω. Then there exists a largest
effectively null set with respect to 𝜇. In other words, the union of all effectively 𝜇-
null sets is an effectively 𝜇-null set.
Proof. As we have seen, for each regular function 𝑥 we get a corresponding
effectively null set. Since there is countably many regular functions, we get a
countably many effectively null sets and their union contains every effectively null
set. Therefore, the union of all effectively null sets is a null set. (When speaking
about null sets and effectively null sets we have in mind measure 𝜇.)
However, we need more: we have to prove that this union is an effectively null
set. To achieve this goal, we enumerate all regular functions and then use the
effective version of the theorem that says that the countable union of null sets is a
null set.
For technical reasons it is convenient to change a bit the definition of a regular
function. Namely, we now say that a computable function 𝑥(·, ·) is regular if all the
finite partial sums of the series
𝑝(𝑥(𝜀, 0)) + 𝑝(𝑥(𝜀, 1)) + 𝑝(𝑥(𝜀, 2)) + . . .
are less than 𝜀 (note the strict inequality). Here 𝑝(𝑥) stands for 𝜇(Ω𝑥). This makes
our requirements for regular functions a bit stronger (if all partial sums are less
than 𝜀, the sum of the series does not exceed 𝜀, but the reverse is not always true).
However, the notion of the effectively null set is not affected, since we always can
replace 𝜀 by (say) 𝜀/2.
In the sequel the regular functions are understood in this modified sense (in
fact, regular functions are used only locally, in the proof of Martin-L¨of theorem).
The following Lemma allows us to enumerate all regular functions.
Lemma. There exists a computable (partial) function
⟨𝑞, 𝜀, 𝑖⟩ ↦ → 𝑋(𝑞, 𝜀, 𝑖)
(where 𝑞 and 𝑖 are natural numbers, 𝜀 is a positive rational number ) such that for
any fixed 𝑞 we get a regular function 𝑋𝑞 (of two remaining arguments) and all
regular functions can be obtained in this way.
Proof. Let us enumerate all programs for the functions of two arguments
(whether these functions are regular or not); we get a computable sequence of

76 3. MARTIN-L ¨OF RANDOMNESS
programs, and 𝑞th term of this sequence is called “𝑞th program” in the rest of the
proof.
Then we define 𝑋(𝑞, 𝜀, 𝑖) as the output of the 𝑞th program on input 𝜀, 𝑖, assum-
ing that some conditions are met; otherwise 𝑋(𝑞, 𝜀, 𝑖) is undefined. The conditions
guarantee that all 𝑋𝑞 are regular, and that regular functions are untouched.
To compute 𝑋(𝑞, 𝜀, 𝑖), we apply 𝑞th program in parallel to all pairs
(𝜀, 0), (𝜀, 1), . . . ,
(starting with one step of the first computation, then making two steps of the first
two computations, etc.)
When some computation terminates with some output, we interrupt this pro-
cess to verify that strings obtained so far do not violate the regularity condition.
This means that we start to compute more and more precise approximations to
𝑝(𝑧) for all these strings until we could guarantee that the sum of all these 𝑝(𝑧) is
less then 𝜀 (this happens if the sum of approximations is less than 𝜀 minus the sum
of approximation errors). (Since 𝜇 is computable, we can compute approximations
to 𝑝(𝑧) for any 𝑧 with any precision.)
It is possible that we do not return from this interrupt; this happens if the sum
of measures is not less than 𝜀.
Now 𝑋(𝑞, 𝜀, 𝑖) is defined as the output of 𝑞th program on (𝜀, 𝑖) if this output
appears and passes the test during the process described.
If 𝑞th program computes a regular function, the verification will never fail and
𝑋𝑞 coincides with this function. On the other hand, for every 𝑞 the function 𝑋𝑞 is
regular: if for some 𝜀 the 𝑞th program (applied to 𝜀 and all 𝑖 = 0, 1, 2, . . .) generates
strings whose total measure is too large, only finitely many of the strings will be
let through, and their total measure is still less than 𝜀. Lemma is proven.
77 Explain why we need to change the definition of correctness. [Answer: if
the sum consists of finite number of terms and their sum is exactly 𝜀, we may newer
know this.]
Now we finish the proof of Martin-L¨of theorem. Let 𝑋 be the function provided
by the Lemma. For all 𝑞 = 0, 1, 2, . . . consider the effectively null set 𝑍𝑞 that
corresponds to the regular function 𝑋𝑞 . Every effectively null set by definition is
a subset of 𝑍𝑞 for some 𝑞. It remains to show that the union 𝑍0 ∪ 𝑍1 ∪ . . . is an
effective null set.
We do the same trick that is used to prove that a countable union of null sets
is a null set. To find a covering of total measure less that 𝜀 for ∪𝑞 𝑍𝑞 , we combine
the (𝜀/2)-covering for 𝑍0 with (𝜀/4)-covering for 𝑍1, etc.
More formally, we consider a function 𝑥(𝜀, 𝑖), that is defined as follows:
𝑥(𝜀, [𝑞, 𝑘]) = 𝑋(𝑞, 𝜀/2𝑞+1, 𝑘).
Here [𝑞, 𝑘] stands for the number of pair 𝑞, 𝑘 under some computable bijection
between N2 and N. 
Now we are ready to give the definition of Martin-L¨of random sequence. Assume
that some computable measure 𝜇 on the set Ω is fixed.
Definition. A sequence 𝜔 is called Martin-L¨of random (ML-random) with
respect to 𝜇 if 𝜔 does not belong to the largest effectively null set (with respect to
𝜇) provided by Theorem 28.

3.3. EFFECTIVELY NULL SETS 77
Reformulation: a sequence is Martin-L¨of random if it does not belong to any
effectively null set.
One more version: a sequence 𝜔 is Martin-L¨of random if the singleton {𝜔} is
not an effectively null set.
A digression: terminology. The notion of Martin-L¨of randomness is a
refinement of the intuitive idea of a “typical sequence”. One could say that a
sequence is “typical” if it does not have any regularities or special features which
separates it from most sequences. (If somebody says that “Mr. X is a typical math
professor”, she probably means that Mr. X has no special characteristics that make
him different from the majority of math professors.) A “special feature” is a feature
that is possessed only by a negligible fraction of the objects considered (sequences).
For example, if a sequence 𝜔 starts with 0, this is not a special feature, since half
of the sequences start with 0. On the other hand, if each other term of 𝜔 is zero,
this is indeed a special feature.
This informal idea is implemented in the Martin-L¨of definition: a special fea-
ture is a feature that corresponds to an effectively null set, and therefore typical
sequences are sequences that do not belong to any effectively null set, i.e., Martin-
L¨of random sequences.
It would be more logical to use the word “typical” for Martin-L¨of’s defini-
tion and reserve the word “random” for more general intuitive notion that can be
formalized in different ways (and the idea of a typical sequence is one of them).
However, the attempts to introduce a new, more logical, terminology often make
the situation worse (authors have to confess that this can be said about their own
attempts!). And there is already a lot of confusion, the term “random sequence” is
already used in different ways.
So we keep the term “Martin-L¨of random sequence” (“ML-random sequence”)
for the definition given above keeping the general term “random sequence” for
a vague philosophical notion of randomness that needs additional clarification to
become a mathematical notion. (End of digression.)
The following statement is a trivial corollary of Martin-L¨of theorem; however,
it deserves a careful thinking since it looks counter-intuitive.
Theorem 29. A set 𝐴 ⊂ Ω is an effectively null set if and only if all its
elements are not Martin-L¨of random (are non-typical ).
In particular, the set of all non-ML-random sequences is the largest effectively
null set, and the set of all ML-random sequences has measure 1.
Proof. Indeed, any element of any effectively null set is not ML-random by
definition; on the other hand, if all elements of some set 𝐴 are not ML-random,
then 𝐴 is a subset of the largest effectively null set and therefore 𝐴 is an effectively
null set. 
What is strange here? Intuitively, a set 𝐴 is a null set if it has “few elements”;
the nature of these elements does not matter much. Any singleton {𝜔} ⊂ Ω is a
null set and this does not depend on the properties of the sequence 𝜔.
On the other hand, now we see that if we replace null sets by effectively null
sets, the situation changes drastically: we may put as many non-ML-random (non-
typical) sequences in a set as we wish, and it would remain an effectively null

78 3. MARTIN-L ¨OF RANDOMNESS
set, but just one ML-random (typical) sequence added is enough to destroy this
property.
For example, recall that any computable sequence forms an effectively null
singleton (with respect to uniform measure). We immediately get the following
corollary:
Theorem 30. The set of all computable sequences of zeros and ones is an
effectively null subset of Ω (with respect to the uniform measure).
It is interesting to note that this observation was made before Martin-L¨of gave
the definition of randomness, while developing the constructive version of calculus
(“Zaslavsky construction” [219] used for many counterexamples; it deals with real
numbers instead of bit sequences).
In the next section we explore the properties of ML-random sequences (with re-
spect to the uniform measure). We end this section with the following nice criterion
for ML-randomness which is attributed to R. Solovay in [34].
Theorem 31. A sequence 𝜔 is not ML-random with respect to a computable
measure 𝜇 if and only if there exists s computable sequence of intervals with finite
sum of measures that covers 𝜔 infinitely many times, i.e., a computable sequence
of binary strings 𝑥0, 𝑥1, 𝑥2, . . . such that∑︁
𝑖
𝜇(Ω𝑥𝑖 ) < ∞
and 𝜔 ∈ Ω𝑥𝑖 for infinitely many 𝑖.
Proof. Assume that 𝜔 is not ML-random. Then for each 𝜀 we can effectively
find a computable sequence of intervals that covers {𝜔} and has the sum of measures
less than 𝜀. Then we combine these sequences for 𝜀 = 1, 1/2, 1/4, 1/8, . . . and get a
computable sequence of intervals with sum of measures not exceeding 2 that covers
𝜔 infinitely many times (at least once for each 𝜀).
On the other hand, assume that there is a computable sequence 𝑥0, 𝑥1, 𝑥2 . . .
of strings such that the sum of measures of corresponding intervals Ω𝑥𝑖 does not
exceed some constant 𝑐 and infinitely many of them contain 𝜔. We may assume
without loss of generality that 𝑐 is a rational number. To find a covering for 𝜔 that
has sum of measures less than 𝜀, we consider the set 𝑀𝑁 of all sequences in Ω that
are covered at least 𝑁 times. Here 𝑁 is a positive integer such that 𝑐/𝑁 < 𝜀. It
is easy to see that 𝑀𝑁 can be represented as the union of a computable sequence
of disjoint intervals (while reading 𝑥0, 𝑥1, . . ., we discover more and more elements
of 𝑀𝑁 and add respective intervals as they appear). Therefore the set {𝜔} is an
effectively null set and the sequence 𝜔 is not ML-random. 
Remark. This result is a constructive version of Borel–Cantelli Lemma (if the
sum of measures of sets 𝐴0, 𝐴1, . . . is finite, then the set of all points that belong
to infinitely many 𝐴𝑖 is a null set), and our argument is an effective version of
a classical proof of Borel–Cantelli Lemma. However, we should be careful since
not any classical proof can be effectivized. The standard proof (since the series is
converging, its tails could be made as small is needed) does not work here, since
there is no way to find an appropriate tail given 𝜀.
Martin-L¨of randomness is defined for computable measures: we used com-
putability to prove that the largest effectively null set exists. One could refor-
mulate the definition and call a sequence random (for an arbitrary measure 𝜇 on

3.4. PROPERTIES OF MARTIN-L ¨OF RANDOMNESS 79
Ω) if it does not belong to any effectively null set. For this notion B. Kjos-Hansen
suggested the name Hippocratic randomness (and P. G´acs suggested more neutral
name blind randomness). This is not the only existing notion of randomness with
respect to non-computable measures; we do not go into details here and mention
only that one can use uniform tests of randomness (following Levin and G´acs, see
[13]).
78 Prove that for an upper semicomputable measure there exists the largest
effectively null set. (We do not assume here that the measure of the entire Ω equals
1, otherwise all upper semicomputable measures would be computable.)
79 Construct an example of a (non-computable) measure for which there is no
largest effectively null set. [Hint: Construct a measure that has two properties at
the same time: (1) every computable sequence forms a singleton that is an effective
null set (moreover, some prefix already has measure zero); (2) every algorithm that
pretends to generate an effectively null set, either gives an interval whose measure
is too big, or does not cover some computable sequence. This can be done by a
diagonal argument where we consider one by one all the computable sequences and
all possible algorithms.]
80 Show that there is a non-computable measure for which there exists the
largest effectively null set. [Hint: consider a non-computable measure that is very
close to the uniform one (say, at most twice bigger and at most twice smaller for
all sets).]

---

Full document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md) · Page-level evidence: [paper-pages/26-kolmogorov-complexity-and-algorithmic-randomness](../../paper-pages/26-kolmogorov-complexity-and-algorithmic-randomness/index.md)
