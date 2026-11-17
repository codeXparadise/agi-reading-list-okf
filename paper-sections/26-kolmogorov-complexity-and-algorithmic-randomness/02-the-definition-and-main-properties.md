---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
section: 1.1. The definition and main properties
section_role: other
section_index: 2
pages: [28, 29, 30, 31, 32, 33, 34]
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "Let us recall the definition of Kolmogorov complexity from the Introduction. This version of complexity was defined by Kolmogorov in his seminal…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 1.1. The definition and main properties

> Section 2 of 11 from [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md) · `other` · pages 28-34

Let us recall the definition of Kolmogorov complexity from the Introduction.
This version of complexity was defined by Kolmogorov in his seminal paper [77].
In order to distinguish it from later versions we call it the plain Kolmogorov com-
plexity. Later, starting from Chapter 4, we will consider also other versions of
Kolmogorov complexity, including the prefix one and the monotone one, but for
now by Kolmogorov complexity we always mean the plain one.
Recall that a description mode, or a decompressor , is a partial computable
function 𝐷 from the set of all binary strings Ξ into Ξ. A partial function 𝐷 is
computable if there is an algorithm that terminates and returns 𝐷(𝑥) on every
input 𝑥 in the domain of 𝐷 and does not terminate on all other inputs. We say
that 𝑦 is a description of 𝑥 with respect to 𝐷 if 𝐷(𝑦) = 𝑥.
The complexity of a string 𝑥 with respect to description mode 𝐷 is defined as
𝐶𝐷 (𝑥) = min{𝑙(𝑦) | 𝐷(𝑦) = 𝑥}.
The minimum of the empty set is +∞.
We say that a description mode 𝐷1 is not worse than a description mode 𝐷2
if there is a constant 𝑐 such that 𝐶𝐷1 (𝑥) 6 𝐶𝐷2 (𝑥) + 𝑐 for all 𝑥 and write this as
𝐶𝐷1 (𝑥) 6 𝐶𝐷2 (𝑥) + 𝑂(1).
A description mode is called optimal if it is not worse than any other description
mode. By Kolmogorov–Solomonoff universality theorem (Theorem 1, p. 13) optimal
description modes exist. Let us recall shortly its proof. Let 𝑈 be an interpreter of
a universal programming language, that is, 𝑈 (𝑝, 𝑥) is the output of the program 𝑝
on input 𝑥. We assume that programs and inputs are binary strings. Let
𝐷(ˆ𝑝𝑥) = 𝑈 (𝑝, 𝑥).
Here 𝑝 ↦ → ˆ𝑝 stands for any computable mapping having the following property:
given ˆ𝑝 we can effectively find 𝑝 and also the place where ˆ𝑝 ends (in particular, if ˆ𝑝
is a prefix of ˆ𝑞, then 𝑝 = 𝑞). This property implies that 𝐷 is well defined. For any
description mode 𝐷′ let 𝑝 be a program of 𝐷′. Then
𝐶𝐷′ (𝑥) 6 𝐶𝐷 (𝑥) + 𝑙(ˆ𝑝).
Indeed, for every description 𝑦 of 𝑥 with respect to 𝐷′ the string ˆ𝑝𝑦 is a description
of 𝑥 with respect to 𝐷.
Fix any optimal description mode 𝐷 and let 𝐶(𝑥) (we drop the subscript)
denote the complexity of 𝑥 with respect to 𝐷. (As we mentioned, in the first paper
of Kolmogorov [77] the letter 𝐾 was used, while in his second paper [78] the letter
𝐻 was used. We follow here the notation used by Li and Vit´anyi [102].)
29

30 1. PLAIN KOLMOGOROV COMPLEXITY
As the optimal description mode is not worse than the identity function 𝑥 ↦ → 𝑥,
we obtain the inequality 𝐶(𝑥) 6 𝑙(𝑥) + 𝑂(1) (Theorem 2, p. 15).
Let 𝐴 be a partial computable function. Comparing the optimal description
mode 𝐷 with the description mode 𝑦 ↦ → 𝐴(𝐷(𝑦)), we conclude that
𝐶(𝐴(𝑥)) 6 𝐶(𝑥) + 𝑂(1),
showing the non-growth of complexity under algorithmic transformations (Theo-
rem 3, p. 15).
Using this inequality, we can define Kolmogorov complexity of other “finite
objects” like natural numbers, graphs, permutations, finite sets of strings, etc.,
that can be naturally encoded by binary strings.
For example, let us define the complexity of natural numbers. A natural num-
ber 𝑛 can be written in binary notation. Another way to represent a number by a
string is as follows. Enumerate all the binary strings in the lexicographical order
Λ, 0, 1, 00, 01, 10, 11, 000, 001, 010, 011, 100, . . .
using the natural numbers 0, 1, 2, 3, . . . as indexes. This enumeration is more con-
venient compared to binary representation, as it is a bijection. Every string can be
considered as an encoding of its index in this enumeration. Finally, one can also
encode a natural number 𝑛 by a string consisting of 𝑛 ones.
Using either of these three encodings we can define the complexity of 𝑛 as
the complexity of the string encoding 𝑛. Three resulting complexities of 𝑛 differ
at most by an additive constant. Indeed, for every pair of these encodings there
is an algorithm translating the first encoding into the second one. Applying this
algorithm, we increase the complexity at most by a constant. Note that anyway
the Kolmogorov complexity of binary strings is defined up to an additive constant,
so the choice of a computable encoding does not matter.
As the length of the binary representation of a natural number 𝑛 is equal to
log 𝑛 + 𝑂(1), the Kolmogorov complexity of 𝑛 is at most log 𝑛 + 𝑂(1). (By log we
denote binary logarithms.)
Here is another application of the non-growth of complexity under algorithmic
transformations. Let us show that deleting the last bit of a string changes its
complexity at most by a constant. Indeed, all three functions 𝑥 ↦ → 𝑥0, 𝑥 ↦ → 𝑥1,
𝑥 ↦ → (𝑥 without the last bit) are computable.
The same is true for the first bit. However this does not apply to every bit of
the string. To show this, consider the string 𝑥 consisting of 2𝑛 zeros, its complexity
is at most 𝐶(𝑛) + 𝑂(1) 6 log 𝑛 + 𝑂(1). (By log we always mean binary logarithm.)
There are 2𝑛 different strings obtained from 𝑥 by flipping one bit. At least one of
them has complexity 𝑛 or more. (Recall that the number of strings of complexity
less than 𝑛 does not exceed the number of descriptions of length less than 𝑛, which
is less than 2𝑛, Theorem 5, p. 18.)
Incrementing a natural number 𝑛 by 1 changes 𝐶(𝑛) at most by a constant.
This implies that 𝐶(𝑛) satisfies “Lipschitz property”: for some 𝑐 and for all 𝑚, 𝑛
we have |𝐶(𝑚) − 𝐶(𝑛)| 6 𝑐|𝑚 − 𝑛|.
1 Prove a stronger inequality: |𝐶(𝑚) − 𝐶(𝑛)| 6 |𝑚 − 𝑛| + 𝑐 for some 𝑐 and for
all 𝑚, 𝑛 ∈ N, and, moreover, |𝐶(𝑚) − 𝐶(𝑛)| 6 2 log |𝑚 − 𝑛| + 𝑐 (the latter inequality
assumes that 𝑚̸ = 𝑛).

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

32 1. PLAIN KOLMOGOROV COMPLEXITY
Proof. Let us prove the theorem. First, we need to show that the set
{⟨𝑛, 𝑥⟩ | 𝑥 ∈ 𝑆𝑛} = {⟨𝑛, 𝑥⟩ | 𝐶(𝑥) < 𝑛},
where 𝑛 is a natural number and 𝑥 is a binary string, is enumerable.
Let 𝐷 be the optimal decompressor used in the definition of 𝐶. Perform in
parallel the computations of 𝐷 on all the inputs. (Say, for 𝑘 = 1, 2, . . . we make 𝑘
steps of 𝐷 on 𝑘 first inputs.) If we find that 𝐷 halts on some 𝑦 and returns 𝑥, the
generating algorithm outputs the pair ⟨𝑙(𝑦) + 1, 𝑥⟩. Indeed, this implies that the
complexity of 𝑥 is less than 𝑙(𝑦) + 1, as 𝑦 is a description of 𝑥. Also it outputs all
the pairs ⟨𝑙(𝑦) + 2, 𝑥⟩, ⟨𝑙(𝑦) + 3, 𝑥⟩ . . . in parallel to printing of other pairs.
For those familiar with computability theory, this proof can be compressed to
one line:
𝐶(𝑥) < 𝑛 ⇔ ∃𝑦 (𝑙(𝑦) < 𝑛 ∧ 𝐷(𝑦) = 𝑥).
(The set of pairs ⟨𝑥, 𝑦⟩ such that 𝐷(𝑦) = 𝑥 is enumerable, being the graph of
a computable function. The operations of intersection and projection preserve
enumerability.)
The converse implication is a bit harder. Assume that 𝑉𝑛 is an enumerable
family of finite sets of strings and |𝑉𝑛| < 2𝑛. Fix an algorithm generating the
set {⟨𝑛, 𝑥⟩ | 𝑥 ∈ 𝑉𝑛}. Consider the description mode 𝐷𝑉 that deals with strings
of length 𝑛 in the following way. Strings of length 𝑛 are used as descriptions of
strings in 𝑉𝑛. More specifically, let 𝑥𝑘 be the 𝑘th string in 𝑉𝑛 in the order the pairs
⟨𝑛, 𝑥⟩ appear while generating the set {⟨𝑛, 𝑥⟩ | 𝑥 ∈ 𝑉𝑛}. (We assume there are no
repetitions, so 𝑥0, 𝑥1, 𝑥2 . . . are distinct.) Let 𝑦𝑘 be the 𝑘th string of length 𝑛 in
the lexicographical order. Then 𝑦𝑘 is a description of 𝑥𝑘, that is, 𝐷(𝑦𝑘) = 𝑥𝑘. As
|𝑉𝑛| < 2𝑛, every string in 𝑉𝑛 gets a description of length 𝑛 with respect to 𝐷.
We need to verify that the description mode 𝐷𝑉 defined in this way is com-
putable. To compute 𝐷𝑉 (𝑦) we find the index 𝑘 of 𝑦 in the lexicographical ordering
of strings of length 𝑙(𝑦). Then we run the algorithm generating pairs ⟨𝑛, 𝑥⟩ such
that 𝑥 ∈ 𝑉𝑛 and wait until 𝑘 different pairs having the first component 𝑙(𝑦) appear.
The second component of the last of them is 𝐷𝑉 (𝑦).
By construction, for all 𝑥 ∈ 𝑉𝑛 we have 𝐶𝐷𝑉 (𝑥) 6 𝑛. Comparing 𝐷𝑉 with the
optimal description mode we see that there is a constant 𝑐 such that 𝐶(𝑥) < 𝑛 + 𝑐
for all 𝑥 ∈ 𝑉𝑛. Theorem 7 is proven. 
The intuitive meaning of Theorem 7 is as follows. The assertions “the number
of strings with certain property is small” (is less than 2𝑖) and “all the strings with
certain property are simple” (have complexity less than 𝑖) are equivalent provided
the property under consideration is enumerable and provided the complexity is
measured up to an additive constant (and the number of elements is measured up
to a multiplicative constant).
Theorem 7 can be reformulated as follows. Let 𝑓 (𝑥) be a function defined on
all binary strings and taking as values natural numbers and a special value +∞.
We call 𝑓 upper semicomputable, or enumerable from above, if there is a computable
function ⟨𝑥, 𝑘⟩ ↦ → 𝐹 (𝑥, 𝑘) defined on all strings 𝑥 and all natural numbers 𝑘 such
that
𝐹 (𝑥, 0) > 𝐹 (𝑥, 1) > 𝐹 (𝑥, 2) > . . .
and
𝑓 (𝑥) = lim
𝑘→∞ 𝐹 (𝑥, 𝑘),

1.1. THE DEFINITION AND MAIN PROPERTIES 33
for all 𝑥. The values of 𝐹 are natural numbers as well as the special constant +∞.
The requirements imply that for every 𝑘 the value 𝐹 (𝑥, 𝑘) is an upper bound of
𝑓 (𝑥). This upper bound becomes more precise as 𝑘 increases. For every 𝑥 there
is a 𝑘 for which this upper bound is tight. However, we do not know the value of
that 𝑘. (If there is an algorithm that given any 𝑥 finds such 𝑘, then the function 𝑓
is computable.) Evidently, any computable function is upper semicomputable.
A function 𝑓 is upper semicomputable if and only if the set
𝐺𝑓 = {⟨𝑥, 𝑛⟩ | 𝑓 (𝑥) < 𝑛}
is enumerable. This set is sometimes called the “upper graph of 𝑓 ”, which explains
the strange names “upper semicomputable” and “enumerable from above”.
Let us verify this. Assume that a function 𝑓 is upper semicomputable. Let
𝐹 (𝑥, 𝑘) be the function from the definition of semicomputability. Then we have
𝑓 (𝑥) < 𝑛 ⇔ ∃𝑘 𝐹 (𝑥, 𝑘) < 𝑛.
Thus, performing in parallel the computations of 𝐹 (𝑥, 𝑘) for all 𝑥 and 𝑘, we can
generate all the pairs in the upper graph of 𝑓 .
Assume now that the set 𝐺𝑓 is enumerable. Fix an algorithm enumerating this
set. Then define 𝐹 (𝑥, 𝑘) as the best upper bound of 𝑓 obtained after 𝑘 steps of
generating elements in 𝐺𝑓 . That is, 𝐹 (𝑥, 𝑘) is equal to the minimal 𝑛 such that
the pair ⟨𝑥, 𝑛 + 1⟩ has been printed after 𝑘 steps. If there is no such pair, let
𝐹 (𝑥, 𝑘) = +∞.
Using the notion of an upper semicomputable function we can reformulate
Theorem 7 as follows.
Theorem 8. (a) The function 𝐶 is upper semicomputable and
|{𝑥 | 𝐶(𝑥) < 𝑛}| < 2𝑛
for all 𝑛.
(b) If a function 𝐶′ is upper semicomputable and |{𝑥 | 𝐶′(𝑥) < 𝑛}| < 2𝑛 for
all 𝑛, then 𝐶(𝑥) 6 𝐶′(𝑥) + 𝑐 for some 𝑐 and for all 𝑥.
Note that the upper bound 2𝑛 of the cardinality of |{𝑥 | 𝐶′(𝑥) < 𝑛}| in item
(b) can be replaced by a weaker upper bound 𝑂(2𝑛).
Theorem 8 allows to define Kolmogorov complexity as a minimal (up to an
additive constant) upper semicomputable function 𝑘 that satisfies the inequality
|{𝑥 | 𝑘(𝑥) < 𝑛}| = 𝑂(2𝑛).
One can replace the requirement of minimality in this definition by some other
properties of 𝐶. In this way we obtain the following “axiomatic” definition of
Kolmogorov complexity [172]:
Theorem 9. Let 𝑘 be a function defined on binary strings and taking natural
values. Assume that 𝑘 satisfies the following properties:
(a) 𝑘 is upper semicomputable; [enumerability axiom]
(b) for every partial computable function 𝐴 from Ξ to Ξ the inequality
𝑘(𝐴(𝑥)) 6 𝑘(𝑥) + 𝑐
is valid for some 𝑐 and all 𝑥 in the domain of 𝐴; [complexity non-increase axiom]
(c) the number of strings 𝑥 such that 𝑘(𝑥) < 𝑛 is in the range [2𝑛−𝑐1 ; 2𝑛+𝑐2 ]
for some 𝑐1, 𝑐2 and for any 𝑛. [calibration axiom]

34 1. PLAIN KOLMOGOROV COMPLEXITY
Then 𝑘(𝑥) = 𝐶(𝑥) + 𝑂(1), that is, the difference |𝑘(𝑥) − 𝐶(𝑥)| is bounded by a
constant.
Proof. Theorem 8 implies that 𝐶(𝑥) 6 𝑘(𝑥) + 𝑂(1). So we need to prove that
𝑘(𝑥) 6 𝐶(𝑥) + 𝑂(1).
Lemma 1. There is a constant 𝑐 and a computable sequence of finite sets of
binary strings
𝑀0 ⊂ 𝑀1 ⊂ 𝑀2 ⊂ . . .
with the following properties: the set 𝑀𝑖 has exactly 2𝑖 strings and 𝑘(𝑥) 6 𝑖 + 𝑐 for
all 𝑥 ∈ 𝑀𝑖 and all 𝑖.
Computability of 𝑀0, 𝑀1, 𝑀2, . . . means that there is an algorithm that given
any 𝑖 computes the list of elements of 𝑀𝑖.
Proof. By axiom (c) there exists a constant 𝑐 such that for all 𝑖 the set
𝐴𝑖 = {𝑥 | 𝑘(𝑥) < 𝑖 + 𝑐}
has at least 2𝑖 elements. By item (a) the family 𝐴𝑖 is enumerable. Remove from
𝐴𝑖 all the elements except 2𝑖 strings generated first. Let 𝐵𝑖 denote the resulting
set. The list of the elements of 𝐵𝑖 can be found given 𝑖: we wait until the first 2𝑖
strings are generated. The set 𝐵𝑖 is not necessarily included in 𝐵𝑖+1. To fix this
we define 𝑀𝑖 inductively. We let 𝑀0 = 𝐵0, and we let 𝑀𝑖+1 be equal to 𝑀𝑖 plus
any 2𝑖 elements of 𝐵𝑖+1 that are outside 𝑀𝑖. Lemma 1 is proven.
Lemma 2. There is a constant 𝑐 such that 𝑘(𝑥) 6 𝑙(𝑥) + 𝑐 for all 𝑥 (recall that
𝑙(𝑥) denotes the length of 𝑥).
Proof. Let 𝑀0, 𝑀1, 𝑀2, . . . be the sequence of sets from the previous lemma.
There is a computable one-to-one function 𝐴 defined on the union of all 𝑀𝑖 that
maps 𝑀𝑖+1 ∖ 𝑀𝑖 onto the set of binary strings of length 𝑖. (Recall that the set
𝑀𝑖+1 ∖ 𝑀𝑖 has exactly 2𝑖 strings.) By item (b) we have 𝑘(𝐴(𝑦)) 6 𝑘(𝑦) + 𝑐′ for
some 𝑐′ and all 𝑥. For all 𝑥 of length 𝑖 there is 𝑦 ∈ 𝑀𝑖+1 ∖ 𝑀𝑖 such that 𝐴(𝑦) = 𝑥
hence 𝑘(𝑥) 6 𝑘(𝑦) + 𝑐′ 6 𝑖 + 𝑐 for some 𝑐 and all 𝑖. Lemma 2 is proven.
Let us finish the proof of the theorem. Let 𝐷 be the optimal description mode
and let 𝑝 be a shortest description of 𝑥 with respect to 𝐷. Then
𝑘(𝑥) = 𝑘(𝐷(𝑝)) 6 𝑘(𝑝) + 𝑂(1) 6 𝑙(𝑝) + 𝑂(1) = 𝐶(𝑥) + 𝑂(1).
Note that we have used twice the property (b): in the proof of Lemma 2 and just
now. 
4 Assume that strings over the alphabet {0, 1, 2, 3} are used as descriptions.
Prove that in this case the Kolmogorov complexity, defined as the length of the
shortest description (with respect to an optimal description mode) is equal to the
half of the regular complexity (up to an additive constant).
5 (Continued.) Formulate and prove a similar statement for the 𝑛-letter
alphabet.
6 Assume that 𝑓 : N → N is a total computable increasing function and
lim inf 𝑓 (𝑛 + 1)/𝑓 (𝑛) > 1.
Let 𝐴𝑛 be an enumerable family of finite sets such that |𝐴𝑛| 6 𝑓 (𝑛) for all 𝑛. Prove
that there is a constant 𝑐 such that 𝐶(𝑥) 6 log 𝑓 (𝑛) + 𝑐 for all 𝑛 and all 𝑥 ∈ 𝐴𝑛.
7 Prove that for some constant 𝑐 and for every 𝑛 the following holds. For
every string 𝑥 of length 𝑛 one can flip a bit in 𝑥 so that the resulting string 𝑦

1.2. ALGORITHMIC PROPERTIES 35
satisfies the inequality 𝐶(𝑦) 6 𝑛 − log 𝑛 + 𝑐. [Hint. For a given natural 𝑘 consider
a Boolean matrix of size 𝑘 × (2𝑘 − 1) whose columns are all nonzero strings of
length 𝑘. (Such matrix is used for Hamming codes.) Consider the linear mapping
B2𝑘 −1 → B𝑘 defined by this matrix, where B denotes the field {0, 1}. It is easy to
verify that for every vector 𝑥 one can flip one bit in 𝑥 so that the resulting string 𝑦
is in the kernel of this mapping, and the elements of the kernel have complexity at
most 2𝑘 − 𝑘 + 𝑂(1). This gives the desired result for 𝑛 = 2𝑘 − 1; if 𝑛 has not the
form 2𝑘 − 1, we can flip one of the first 2𝑘 − 1 bits for an appropriate 𝑘.]

---

Full document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md) · Page-level evidence: [paper-pages/26-kolmogorov-complexity-and-algorithmic-randomness](../../paper-pages/26-kolmogorov-complexity-and-algorithmic-randomness/index.md)
