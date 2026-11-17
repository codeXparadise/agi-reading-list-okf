---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
section: 2.2. Conditional complexity
section_role: other
section_index: 5
pages: [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "When transmitting a file, one could try to save communication charges by compressing it. The transmission could be made even more effective if and…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.2. Conditional complexity

> Section 5 of 11 from [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md) · `other` · pages 47-57

When transmitting a file, one could try to save communication charges by
compressing it. The transmission could be made even more effective if and old
version of the same file already exists at the other side. In this case we need only
to describe the changes made. This could be considered as a kind of motivation
for the definition of conditional complexity of a given string 𝑥 relative to (known)
string 𝑦.
A conditional decompressor is a computable function 𝐷 of two arguments,
the description and the condition (both arguments and the value of 𝐷 are binary
strings). If 𝐷(𝑦, 𝑧) = 𝑥 we say that 𝑦 is a (conditional) description of 𝑥 when 𝑧 is
known (or relative to 𝑧) The complexity 𝐶𝐷 (𝑥 | 𝑧) is then defined as the length of
the shortest conditional description:
𝐶𝐷 (𝑥 | 𝑧) = min{𝑙(𝑦) | 𝐷(𝑦, 𝑧) = 𝑥}.
We say that (conditional) decompressor 𝐷1 is not worse than 𝐷2 if
𝐶𝐷1 (𝑥 | 𝑧) 6 𝐶𝐷2 (𝑥 | 𝑧) + 𝑐
for some constant 𝑐 and for all 𝑥 and 𝑧. A conditional decompressor is optimal if
it is not worse than any other conditional decompressor.
Theorem 17. There exist optimal conditional decompressors.
Proof. This “conditional” version of Kolmogorov–Solomonoff theorem can be
proved in the same way as the unconditional one (Theorem 1, p. 13).
Fix some programming language where one can write programs for computable
functions of two arguments, and let
𝐷(ˆ𝑝𝑦, 𝑧) = 𝑝(𝑦, 𝑧),
where 𝑝(𝑦, 𝑧) is the output of program 𝑝 on inputs 𝑦 and 𝑧, and ˆ𝑝 is the prefix-free
encoding of 𝑝.
It is easy to see now that if 𝐷′ is a conditional decompressor and 𝑝 is a program
for 𝐷′, then
𝐶𝐷 (𝑥 | 𝑧) 6 𝐶𝐷′ (𝑥 | 𝑧) + 𝑙(ˆ𝑝).
Theorem is proved. 
Again, we fix some optimal conditional decompressor 𝐷 and omit index 𝐷 in
the notation.
Let us start with some simple properties of conditional complexity.
Theorem 18.
𝐶(𝑥 | 𝑦) 6 𝐶(𝑥) + 𝑂(1);
𝐶(𝑥 | 𝑥) = 𝑂(1);
𝐶(𝑓 (𝑥, 𝑦) | 𝑦) 6 𝐶(𝑥 | 𝑦) + 𝑂(1);
𝐶(𝑥 | 𝑦) 6 𝐶(𝑥 | 𝑔(𝑦)) + 𝑂(1).
Here 𝑔 and 𝑓 are arbitrary computable functions (of one and two arguments,
respectively); the inequalities are valid if 𝑓 (𝑥, 𝑦) and 𝑔(𝑦) are defined.

2.2. CONDITIONAL COMPLEXITY 49
Proof. First inequality: any unconditional decompressor can be considered
as a conditional one that ignores the second argument.
Second inequality: consider 𝐷 such that 𝐷(𝑝, 𝑧) = 𝑧.
Third inequality: Let 𝐷 be the optimal conditional decompressor used to define
complexity. Consider another decompressor 𝐷′ such that
𝐷′(𝑝, 𝑦) = 𝑓 (𝐷(𝑝, 𝑦), 𝑦)
and apply the optimality property.
Similar argument works for the last inequality, but 𝐷′ should be defined in a
different way:
𝐷′(𝑝, 𝑦) = 𝐷(𝑝, 𝑔(𝑦)).
Theorem is proven. 
25 Prove that conditional complexity is “continuous as a function of its second
argument”: 𝐶(𝑥 | 𝑦0) = 𝐶(𝑥 | 𝑦) + 𝑂(1); 𝐶(𝑥 | 𝑦1) = 𝐶(𝑥 | 𝑦) + 𝑂(1). Using this
property, show that for every string 𝑥 and for every non-negative integer 𝑙 6 𝐶(𝑥)
there exists a string 𝑦 such that 𝐶(𝑥 | 𝑦) = 𝑙 + 𝑂(1).
Similar argument based on two-dimensional topology is used in [155].
26 Prove that for any fixed 𝑦 the function 𝑥 ↦ → 𝐶(𝑥 | 𝑦) differs from 𝐶 at most
by 2𝐶(𝑦) + 𝑂(1).
27 Prove that 𝐶([𝑥, 𝑧] | [𝑦, 𝑧]) 6 𝐶(𝑥 | 𝑦) + 𝑂(1) for any strings 𝑥, 𝑦, 𝑧 (here
[·, ·] stands for the computable encoding of pairs).
28 Fix some “reasonable” programming language. (Formally, we require the
corresponding universal function to be a G¨odel one; this means that translation
algorithm exists for any other programming language, see, e.g., [182].) Show that
conditional complexity 𝐶(𝑥 | 𝑦) is equal (up to 𝑂(1) additive term) to the minimal
complexity of a program that produces output 𝑥 on input 𝑦. [Hint: Let 𝐷 be an
optimal conditional decompressor. If we fix its first argument 𝑝, we get a program
of complexity at most 𝑙(𝑝) + 𝑂(1). On the other hand, if program 𝑝 maps 𝑦 to 𝑥,
then 𝐶(𝑥 | 𝑦) = 𝐶(𝑝(𝑦) | 𝑦) 6 𝐶(𝑝) + 𝑂(1).]
This interpretation of conditional complexity as a minimal complexity of a
program with some property will be considered in Chapter 13.
If we restrict ourselves to total programs (that terminate on all inputs), we
get an essentially different notion of conditional complexity that can be called total
conditional complexity.
29 Show that the notion of total conditional complexity CT(𝑥 | 𝑦), the minimal
(plain) complexity of a total program that maps 𝑦 to 𝑥, is well defined (i.e., changes
at most by 𝑂(1) when we change the programming language in a reasonable way).
Prove that
𝐶(𝑥 | 𝑦) 6 CT(𝑥 | 𝑦) 6 𝐶(𝑥)
with 𝑂(1)-precision.
30 Show that the total complexity sometimes exceeds significantly the usual
conditional complexity: for every 𝑛 there exist two 𝑛-bit strings 𝑥 and 𝑦 such that
𝐶(𝑥 | 𝑦) = 𝑂(1) while CT(𝑥 | 𝑦) > 𝑛.
[Hint: Let us enumerate all programs of complexity less than 𝑛 defined on all 𝑛-bit
strings, and maintain two 𝑛-bit strings 𝑥 and 𝑦 with the following property: none of
the programs found maps 𝑦 to 𝑥. When a new program is found that maps 𝑦 to 𝑥,

50 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
we choose a fresh value of 𝑦 and then choose appropriate 𝑥. This process is effective
if 𝑛 (=length of 𝑦) is given, it defines a partial function 𝑦 ↦ → 𝑥, so 𝐶(𝑥 | 𝑦) = 𝑂(1)
for every pair selected.]
31 Let 𝑥 and 𝑦 be two bit strings such that CT(𝑥 | 𝑦) 6 𝑛 and CT(𝑦 | 𝑥) 6 𝑛.
Prove that there exists a program of a computable permutation of the set of bit
strings that maps 𝑥 to 𝑦 and has complexity at most 2𝑛 + 𝑂(1). [Hint: it is easy
to construct a string 𝑣 of length 2𝑛 + 𝑂(1) that encodes a pair of total programs
𝑓 that maps 𝑥 to 𝑦 and 𝑔 that maps 𝑦 to 𝑥. We may assume without loss of
generality that 𝑥 and 𝑦 have 0 as their first bits. Consider a binary relation on
binary strings that starts with 0, defined as 𝑅(𝑢, 𝑣) : (𝑓 (𝑢) = 𝑣) and (𝑔(𝑣) = 𝑢)).
This is a decidable one-to-one correspondence between decidable sets of strings with
infinite complements, and it can be easily extended to a computable permutation.]
32 Show that the upper bound in the preceding problem cannot be improved
significantly: for every 𝑘 there are two strings 𝑥 and 𝑦 of length 𝑛 = 2𝑘 + 𝑂(1)
such that 𝐶(𝑥), 𝐶(𝑦) 6 𝑘 + 𝑂(1) (and therefore CT(𝑥 | 𝑦), CT(𝑦 | 𝑥) 6 𝑘 + 𝑂(1)),
but every permutation of 𝑛-bit strings that maps 𝑥 to 𝑦 has complexity at least
2𝑘. [Hint: Let us first select (arbitrarily) 2𝑘 strings 𝑦 and pair them with some
string 𝑥. Let us enumerate computable permutations of 𝑛-bit strings that have
complexity less than 2𝑘. If and when all selected pairs are served by some of these
permutations, choose a new string 𝑥 that is connected (by existing permutation)
with at most half of the selected 𝑦-strings. After that Ω(2𝑘) new permutations are
needed to connect new 𝑥 to all 𝑦-strings. Therefore at most 22𝑘/Ω(2𝑘) = 𝑂(2𝑘)
𝑥-strings will be used, so the final 𝑥 and 𝑦 have complexity at most 𝑘 + 𝑂(1). The
selection of 𝑥 connected with at most half of selected 𝑦-strings is always possible,
since each of 𝑦-strings is connected with a small fraction of 𝑥-strings, and we can
change the order of summation in the double sum. Note that this argument may
be used to guarantee that one of the strings 𝑥 and 𝑦 belongs to a given set of 2𝑘
strings.]
See [135] for the detailed proofs of these results about total conditional com-
plexity.
Many properties of unconditional complexity have conditional counterparts
with essentially the same proofs. Here are some of these counterparts:
∙ Function 𝐶(· | ·) is upper semicomputable (this means that the set of triples
⟨𝑥, 𝑦, 𝑛⟩ such that 𝐶(𝑥 | 𝑦) < 𝑛 is enumerable).
∙ For any 𝑦 and 𝑛 the set of all strings 𝑥 such that 𝐶(𝑥 | 𝑦) < 𝑛 has cardi-
nality less then 2𝑛.
∙ For any 𝑦 and 𝑛 there exists a string 𝑥 of length 𝑛 such that 𝐶(𝑥 | 𝑦) > 𝑛.
33 Prove that for any strings 𝑦 and 𝑧 and for any number 𝑛 there exists a
string 𝑥 of length 𝑛 such that 𝐶(𝑥 | 𝑦) > 𝑛 − 1 and 𝐶(𝑥 | 𝑧) > 𝑛 − 1. [Hint: both
requirements are violated by a minority of strings.]
Theorem 19. Let ⟨𝑥, 𝑦⟩ ↦ → 𝑘(𝑥, 𝑦) be an upper semicomputable function such
that the set {𝑥 | 𝑘(𝑥, 𝑦) < 𝑛} has cardinality less than 2𝑛 for any string 𝑦 and
integer 𝑛. Then 𝐶(𝑥 | 𝑦) 6 𝑘(𝑥, 𝑦) + 𝑐 for some 𝑐 and for all 𝑥 and 𝑦.
The proof repeats the proof of Theorem simple-upper-reformulated.
Using conditional complexity, we get a stronger inequality for the complexity
of pairs (compared with Theorem 16, p. 45):

2.2. CONDITIONAL COMPLEXITY 51
Theorem 20.
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 2 log 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + 𝑂(1)
Proof. Let 𝐷1 be an optimal unconditional decompressor and let 𝐷2 be an
optimal conditional decompressor. Construct a new unconditional decompressor
𝐷′ as follows:
𝐷′(ˆ𝑝𝑞) = [𝐷1(𝑝), 𝐷2(𝑞, 𝐷1(𝑝))].
Here ˆ𝑝 stands for the prefix-free encoding of 𝑝, and [·, ·] is a computable encoding
of pairs used in the definition of the complexity of pairs. Let 𝑝 be the shortest 𝐷1-
description of 𝑥 and 𝑞 be the shortest 𝐷2-description of 𝑦 conditional to 𝑥. Then
the string ˆ𝑝𝑞 is a 𝐷3-description of [𝑥, 𝑦]. Therefore,
𝐶(𝑥, 𝑦) 6 𝐶𝐷′ (𝑥, 𝑦) + 𝑂(1) 6 𝑙(ˆ𝑝) + 𝑙(𝑞) + 𝑂(1).
As we have seen, one can choose a prefix-free encoding in such a way that 𝑙(ˆ𝑝) is
bounded by 𝑙(𝑝) + 2 log 𝑙(𝑝) + 𝑂(1) (see the proof of Theorem 16, p. 45), and we
get a desired inequality. 
As before, we may replace 2 log 𝐶(𝑥) by log 𝐶(𝑥) + 2 log log 𝐶(𝑥) etc., getting a
better bound. We also can use conditional complexity in the logarithmic term and
write
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + 2 log 𝐶(𝑦 | 𝑥) + 𝑂(1).
(In the proof we should then replace 𝐷′(ˆ𝑝𝑞) by 𝐷′(ˆ𝑞𝑝).)
34 Prove that
𝐶(𝑥 | 𝑧) 6 𝐶(𝑥 | 𝑦) + 2 log 𝐶(𝑥 | 𝑦) + 𝐶(𝑦 | 𝑧) + 𝑂(1)
for all 𝑥, 𝑦, 𝑧 (a sort of a “triangle inequality”).
If we are not interested in the exact form of the additional logarithmic term,
the statement of Theorem 20 can be reformulated as follows:
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + 𝑂(log 𝑛).
for all strings 𝑥, 𝑦 of length at most 𝑛.
It turns out (and this is the first nontrivial statement in this chapter, and
probably the first non-trivial result about Kolmogorov complexity; it was proven
independently by Kolmogorov and Levin and published in [78, 223]) that this
inequality is in fact an equality.
Theorem 21 (Kolmogorov–Levin).
𝐶(𝑥, 𝑦) = 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + 𝑂(log 𝑛).
for all strings 𝑥, 𝑦 of length at most 𝑛.
Proof. Since we already have one inequality, we need to prove only that
𝐶(𝑥, 𝑦) > 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + 𝑂(log 𝑛)
for all 𝑥 and 𝑦 of length at most 𝑛.
Let 𝑥 and 𝑦 be some strings of length at most 𝑛. Let 𝑎 be the complexity
𝐶(𝑥, 𝑦) of the pair ⟨𝑥, 𝑦⟩. Consider the set 𝐴 of all pairs whose complexity does not
exceed 𝑎. Then 𝐴 is a set of cardinality 𝑂(2𝑎) (in fact, at most 2𝑎+1) and ⟨𝑥, 𝑦⟩ is
one of its elements.
For each string 𝑡 consider the “vertical section” 𝐴𝑡 of 𝐴:
𝐴𝑡 = {𝑢 | ⟨𝑡, 𝑢⟩ ∈ 𝐴}

52 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
𝑡
𝐴𝑡
𝐴
𝑥
𝑦
Figure 1. The section 𝐴𝑡 of the set 𝐴 of all simple pairs.
(Fig. 1). The sum of the cardinalities of all 𝐴𝑡 (over all strings 𝑡) is the cardinality
of 𝐴 and does not exceed 𝑂(2𝑎). Therefore there are few “large” sections 𝐴𝑡, and
this is the basic argument we need for the proof.
Let 𝑚 be equal to ⌊log2 |𝐴𝑥|⌋ where 𝑥 is the first component of the pair ⟨𝑥, 𝑦⟩
we started with. In other terms, assume that cardinality of 𝐴𝑥 is between 2𝑚 and
2𝑚+1. Let us prove that
(1) 𝐶(𝑦 | 𝑥) does not exceed 𝑚 significantly;
(2) 𝐶(𝑥) does not exceed 𝑎 − 𝑚 significantly.
We start with (1). Knowing 𝑎, we can enumerate the set 𝐴. If we know also 𝑥,
we can select only pairs whose first component equals 𝑥. In this way we get an
enumeration of 𝐴𝑥. To specify 𝑦, it is enough to tell the ordinal number of 𝑦 in
this enumeration (of 𝐴𝑥). This ordinal number takes 𝑚 + 𝑂(1) bits, and together
with 𝑎 we get 𝑚 + 𝑂(log 𝑛) bits for the conditional description of 𝑦 given 𝑥. Note
that 𝑎 = 𝐶(𝑥, 𝑦) does not exceed 𝑂(𝑛) for strings 𝑥 and 𝑦 of length 𝑛. Therefore,
we need only 𝑂(log 𝑛) to specify 𝑎 and 𝑛, and
𝐶(𝑦 | 𝑥) 6 𝑚 + 𝑂(log 𝑛).
Now let us prove (2). Consider the set 𝐵 of all strings 𝑡 such that cardinality
of 𝐴𝑡 is at least 2𝑚. The cardinality of 𝐵 does not exceed 2𝑎+1/2𝑚, otherwise the
sum |𝐴| =∑︀ |𝐴𝑡| would be greater than 2𝑎+1. We can enumerate 𝐵 if we know 𝑎
and 𝑚. Indeed, we should enumerate 𝐴 and group together the pairs with the same
first coordinate; if we find 2𝑚 pairs with the same value of the first coordinate, we
put this value into 𝐵. Therefore the string 𝑥 (as well as every element of 𝐵) can be
specified by (𝑎 − 𝑚) + 𝑂(log 𝑛) bits: 𝑎 − 𝑚 + 1 bits are needed for ordinal number
of 𝑥 in the enumeration of 𝐵, and 𝑂(log 𝑛) are used to specify 𝑎 and 𝑚. So we get
𝐶(𝑥) 6 (𝑎 − 𝑚) + 𝑂(log 𝑛),
and it remains to add this inequality and the preceding one. 
This theorem can be considered as the complexity counterpart of the following
combinatorial statement. Let 𝐴 be a finite set of pairs. Its cardinality is (obviously)
bounded by the product of the cardinality of 𝐴’s projection onto the first coordinate,
and the maximal cardinality of the sections 𝐴𝑥. This corresponds to the inequality
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + 𝑂(log 𝑛). The reverse inequality needs a more subtle
interpretation. Let 𝐴 be a set of pairs and let 𝑝 and 𝑞 be some numbers such that

2.2. CONDITIONAL COMPLEXITY 53
cardinality of 𝐴 does not exceed 𝑝𝑞. Then we can split 𝐴 into parts 𝑃 and 𝑄 with
the following properties: the projection of 𝑃 onto the first coordinate has at most 𝑝
elements, while all the sections 𝑄𝑥 of 𝑄 (for element in 𝑄𝑥 the first coordinate equals
𝑥) have at most 𝑞 elements. (Indeed, let 𝑃 be the union of all sections that have
more than 𝑞 elements. The number of such sections do not exceed 𝑝. Remaining
elements form 𝑄.) We return to this combinatorial translation in Chapter 10.
Note that in fact we have not used the lengths of 𝑥 and 𝑦, only their complex-
ities. So we have proved the following statement:
Theorem 22 (Kolmogorov–Levin, complexity version).
𝐶(𝑥, 𝑦) = 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + 𝑂(log 𝐶(𝑥, 𝑦))
for all strings 𝑥 and 𝑦.
35 Give a more detailed analysis of the additive terms in the proof and show
that
𝐶(𝑥) + 𝐶(𝑦 | 𝑥) 6 𝐶(𝑥, 𝑦) + 3 log 𝐶(𝑥, 𝑦) + 𝑂(log log 𝐶(𝑥, 𝑦)).
36 Show that if 𝐶(𝑥, 𝑦 | 𝑘, 𝑙) < 𝑘+𝑙, then 𝐶(𝑥 | 𝑘, 𝑙) < 𝑘+𝑂(1) or 𝐶(𝑦 | 𝑥, 𝑘, 𝑙) <
𝑙 + 𝑂(1). [Hint: This is what we proved actually in the proof of Theorem 22.]
37 Show that 𝑂(log 𝑛) terms are unavoidable in Kolmogorov–Levin theorem
in both directions: for each 𝑛 there exist strings 𝑥 and 𝑦 of length at most 𝑛 such
that
𝐶(𝑥, 𝑦) > 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + log 𝑛 − 𝑂(1),
as well as strings 𝑥 and 𝑦 of length at most 𝑛 such that
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) − log 𝑛 + 𝑂(1).
[Hint: For the first inequality we can refer to the remark after Theorem 16 (p. 45).
For the second note that 𝐶(𝑥, 𝑙(𝑥)) = 𝐶(𝑥) for every 𝑥, while 𝐶(𝑥|𝑙(𝑥)) can be
equal to 𝑙(𝑥) + 𝑂(1) and 𝐶(𝑥) + 𝑂(1). Then we can take a random length between
𝑛/2 and 𝑛 and a random string of this length.]
38 Prove that changing one bit in a string of length 𝑛 changes its complexity
at most by log 𝑛 + 𝑂(log log 𝑛). Prove the same for the conditional complexity
𝐶(𝑥 | 𝑛).
As we have seen in Problem 7 (p. 34), for every 𝑛-bit string 𝑥 there exists
another string 𝑥′ of the same length that differs from 𝑥 in one position only such
that 𝐶(𝑥′) < 𝑛 − log 𝑛 + 𝑂(1) (and therefore 𝐶(𝑥′ | 𝑛) < 𝑛 − log 𝑛 + 𝑂(1)). In
particular, if 𝑥 is incompressible (given 𝑛), one can change one bit in 𝑥 and decrease
𝐶(𝑥 | 𝑛).
One can move also in the other direction: if 𝐶(𝑥 | 𝑛) is small enough (this means
that 𝐶(𝑥 | 𝑛) 6 𝛼𝑛 for some positive constant 𝛼), we can increase this complexity
by changing one bit in 𝑛: there exists some 𝛼 > 0 such that for each 𝑛-bit string
𝑥 with 𝐶(𝑥 | 𝑛) 6 𝛼𝑛 one can change one bit in 𝑥 and get another 𝑛-bit string 𝑥′
such that 𝐶(𝑥′ | 𝑛) > 𝐶(𝑥 | 𝑛). (The proof of this statement requires more involved
combinatorial argument [24] than the decrease in complexity.)
39 Fix some unconditional decompressor 𝐷. Prove that for some constant 𝑐
and for all integers 𝑛 and 𝑘 the following statement is true: if some string 𝑥 has
at least 2𝑘 descriptions of length at most 𝑛, then 𝐶(𝑥 | 𝑘) 6 𝑛 − 𝑘 + 𝑐. [Hint: Fix
some 𝑘. For each 𝑛 consider all strings 𝑥 that have at least 2𝑘 descriptions of length

54 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
at most 𝑛. The number of these strings does not exceed 2𝑛−𝑘, and we can apply
Theorem 19, p. 50.]
Using this problem, we can prove the following statement about unconditional
complexity (see [102, Exercises 4.3.9, 4.3.10]):
40 Let 𝐷 be some optimal unconditional decompressor. Then there exists
some constant 𝑐 such that for any string 𝑥 the number of shortest 𝐷-descriptions
of 𝑥 does not exceed 𝑐.
[Hint: The previous problems show that 𝐶(𝑥) 6 𝑛 − 𝑘 + 2 log 𝑘 + 𝑂(1), so for
𝐶(𝑥) = 𝑛 we get an upper bound for 𝑘.]
41 Prove that there exists a constant 𝑐 with the following property: if for
some 𝑥 and 𝑛 the probability of the event 𝐶(𝑥 | 𝑦) 6 𝑘 (all strings 𝑦 of lengths 𝑛 are
considered as equiprobable here) is at least 2−𝑙, then 𝐶(𝑥 | 𝑛, 𝑙) 6 𝑘 + 𝑙 + 𝑐. [Hint:
Connect each string 𝑦 of length 𝑛 to all strings 𝑥 such that 𝐶(𝑥 | 𝑦) 6 𝑘. We get
a bipartite graph that has 𝑂(2𝑛+𝑘) edges. In this graph the number of vertices 𝑥
that have degree at least 2𝑛−𝑙 does not exceed 𝑂(2𝑘+𝑙). Note that 𝐶(𝑥 | 𝑛, 𝑙) does
not include 𝑘—this is not a typo!]
This problem could help us to find the average value of 𝐶(𝑥 | 𝑦) for given 𝑥 and
all string 𝑦 of some length 𝑛. It is evident that 𝐶(𝑥 | 𝑦) 6 𝐶(𝑥 | 𝑛) + 𝑂(1) since
𝑛 = 𝑙(𝑦) is determined by 𝑦. It turns out that for most strings 𝑦 (of given length)
this inequality is close to an equality:
42 Prove that there exists some constant 𝑐 such that for each string 𝑥 and for
all natural numbers 𝑛 and 𝑑 the fraction of strings 𝑦 such that 𝐶(𝑥 | 𝑦) < 𝐶(𝑥 | 𝑛)−𝑑
(among all strings of length 𝑛) does not exceed 𝑐𝑑2/2𝑑. Using this statement, prove
that the average value of 𝐶(𝑥 | 𝑦) taken over all strings 𝑦 of a given length 𝑛 equals
𝐶(𝑥 | 𝑛) + 𝑂(1) (the constant in 𝑂(1) does not depend on 𝑥 and 𝑛).
43 Prove that 𝐶(𝑥 | 𝑘) 6 𝑘 implies 𝐶(𝑥) 6 𝑘 + 𝑂(1). [Hint: See Theorem 7.
One can also note that if a conditional description of 𝑥 given 𝑘 has length 𝑘, then 𝑘
is known anyway, and if this description is shorter, we have enough space to specify
the difference between 𝑘 and the description length.]
A similar (though not identical) statement:
44 Prove that 𝐶(𝑥) = 𝐶(𝑥 | 𝐶(𝑥)) + 𝑂(1). [Hint: Assume that 𝑥 has a condi-
tional description 𝑞 with condition 𝐶(𝑥) that is shorter than 𝐶(𝑥). Then one can
specify 𝑥 by providing 𝑞 and the difference 𝐶(𝑥) − 𝑙(𝑞), and we get a description of
𝑥 that is shorter than 𝐶(𝑥)—a contradiction.]
45 Prove that for every 𝑛 there exists a 𝑛-bit string 𝑥 such that
𝐶(𝐶(𝑥) | 𝑥) = log 𝑛 − 𝑂(1).
(This is a maximal possible value, since 𝐶(𝑥) 6 𝑛 for 𝑛-bit string 𝑥.)
This result (in a bit weaker form) was proven long ago by P. G´acs [55]. Re-
cently E. Kalinina and B. Bauwens suggested a simple game-theoretic proof of this
statement. Here is a sketch is this argument (see [6] for details). Consider a rectan-
gular game board of width 2𝑛 and height 𝑛. Two players, White and Black, make
alternating moves and place pawns of their respective colors into the board cells.
Unlike chess, each cell may contain both white and black pawns (at most one of
each color). At each move player may place several pawns into different cells (or no

2.2. CONDITIONAL COMPLEXITY 55
pawns at all); after a pawn is places, it cannot be moved or removed. Also Black
can irreversibly mark some cells. The players should obey the following restrictions:
(a) each of the players can place at most 2𝑖 pawns at row 𝑖 (the bottom row
has number 0, the upper row has number 𝑛 − 1);
(b) Black can mark at most half of the cells in each column.
A white pawn is declared as killed if its cell is marked or if there is a black
paws below it (in the same column). The game does not end formally (though it is
essentially a finite game); White wins if in the limit there is at least one non-killed
white pawn.
White has a winning strategy in this game: place a pawn in the top row and
wait until it is killed. If it is killed by the black pawn below, switch to the next
column (for example, White can go from left to right starting with the leftmost
column). If the pawn was killed by marking its cell, White places another pawn
just below the first one, etc. (We may assume that Black’s moves kill the white
pawn, all other moves can be postponed, since the winner is determined by the
limit position.) Recall that Black can mark at most half of the column, so Black
is forced to put some pawn in the column at some point. It cannot be done in all
columns, since the sum of 2𝑖 for all rows is less (by 1) than the width of the table.
Note also that White will not violate restrictions on the number of pawns in each
row, since in all the columns (except the currently active one) under each white
pawn (in row 𝑖) there is a black paws (in some row 𝑗 < 𝑖), and the sum of 2𝑗 for
all 𝑗 < 𝑖 is less that 2𝑖 and there is a space for one more white pawn.
After a winning strategy for White is described, consider the following “univer-
sal” strategy for Black: the cell (𝑥, 𝑖) is marked as soon as we find that 𝐶(𝑖 | 𝑥) <
log 𝑛 − 1; a black pawn in placed at (𝑥, 𝑖) when a conditional description of 𝑥
(given 𝑛) of length 𝑖 is found. It is easy to check that Black obeys the game rules.
White wins, and a live white pawn at the cell (𝑥, 𝑖) means that 𝐶(𝑥 | 𝑛) > 𝑖 and
𝐶(𝑖 | 𝑥) > log 𝑛−1. Since the actions of White (playing against computable strategy
of Black) are computable, we conclude that 𝐶(𝑥 | 𝑛) > 𝑖 + 𝑂(1): the set of white
pawns in row 𝑖 is enumerable and it contains at most 2𝑖 elements.
This argument shows that 𝐶(𝐶(𝑥 | 𝑛) | 𝑥) > log 𝑛 − 1 (not exactly what we
wanted); to get the desired result, we should change the game and consider in
paraller boards of all sizes.
46 Prove that for some constant 𝑐 for any string 𝑥 and for every number 𝑛
there exists a string 𝑦 of length 𝑛 such that
𝐶(𝑥𝑦) > 𝐶(𝑥 | 𝑛) + 𝑛 − 𝑐.
[Hint: For a given 𝑛 the number of strings 𝑥 such that 𝐶(𝑥𝑦) < 𝑘 for any 𝑦 of
length 𝑛, does not exceed 2𝑘/2𝑛, and this property is enumerable. So we can apply
Theorem 19 (p. 50).]
47 Let 𝑓 be a function with natural arguments and values. Assume that
𝑓 (𝑛) + 𝜀ℎ 6 𝑓 (𝑛 + ℎ) 6 𝑓 (𝑛) + (1 − 𝜀)ℎ
for some 𝜀 > 0 and for all 𝑛 and ℎ. Prove that there exist an infinite bit sequence
𝜔 whose 𝑛-bit prefix has complexity 𝑓 (𝑛) + 𝑂(1) for every 𝑛.
[Hint: let us add blocks of length ℎ where ℎ is large enough. Each new block
being added to 𝑛-bit prefix increases complexity by more than 𝑓 (𝑛 + ℎ) − 𝑓 (𝑛) or
by less than 𝑓 (𝑛 + ℎ) − 𝑓 (𝑛), depending on the current situation (whether we are

56 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
below or above the boundary). To find a block with big complexity increase we
may use the previous problem, for a block with small increase we can use a block
or zeros. Note that (large enough) ℎ is fixed, so it is enough to control complexity
on the blocks’ boundaries.]
48 Prove that an infinite sequence 𝑥0𝑥1𝑥2 . . . of zeros and ones is computable
if and only if the values 𝐶(𝑥0 . . . 𝑥𝑛−1 | 𝑛) (the complexities of its prefixes conditional
to their lengths) remain bounded by a constant.
[Hint: Consider an infinite binary tree. Let 𝑆 be the enumerable set of vertices
(binary strings) that have conditional complexity (w.r.t. their length) less than
some constant 𝑐. The “horizontal” sections of 𝑆 have cardinality 𝑂(1). We need to
derive from this that each infinite path that lies entirely inside 𝑆, is computable.
We may assume that 𝑆 is a subtree (only strings whose prefixes are in 𝑆, remain
in 𝑆).
Let 𝜔 be an infinite path that goes through 𝑆 only. At each level 𝑛 we count
vertices in 𝑆 on the left of 𝜔 (𝑙𝑛 vertices) and on the right of 𝜔 (𝑟𝑛 vertices). Let
𝐿 = lim sup 𝑙𝑛 and 𝑅 = lim sup 𝑟𝑛. Let 𝑁 be the level such that 𝐿 and 𝑅 are never
exceeded after this level. Knowing 𝐿, 𝑅 and 𝑁 we can compute arbitrarily large
prefixes of 𝜔. We should look for a path 𝜋 in a tree such that at some level above
𝑁 there are at least 𝐿 elements of 𝑆 on the left of 𝜋, and at some (possibly other)
level above 𝑁 there are at least 𝑅 elements on the right of 𝜋. When such a path 𝜋
is found, we can be sure that its initial segment (up to the first of those two levels)
coincides with 𝜔.]
This result was published in [107] (attributed to A.R. Meyer).
49 Prove that in the previous problem a weaker assumption is sufficient:
instead of 𝐶(𝑥0 . . . 𝑥𝑛−1 | 𝑛) = 𝑂(1) we can require that 𝐶(𝑥0 . . . 𝑥𝑛−1) 6 log 𝑛 + 𝑐
for some 𝑐 and for all 𝑛. [Hint: In this case we get an enumerable set 𝑆 of strings
(=tree vertices) with the following property: the number of vertices below level 𝑁
is 𝑂(𝑁 ). This means that the average number of vertices per level is bounded by a
constant. To use the previous problem, we need a bound for all levels and not for
the average value. We can achieve this if we consider only vertices 𝑥 ∈ 𝑆 that have
a extension of length 2𝑙(𝑥) that goes entirely inside 𝑆.]
This result was published in [33].
Following Problem 48, we can suggest different definitions of the complexity
notion for computable bit sequences:
∙ a minimal complexity of a program that, given 𝑛, computes 𝑥0 . . . 𝑥𝑛−1.
We can also consider a program that computes 𝑥𝑛 for input 𝑛, it gives the
same (up to 𝑂(1)) complexity. We denote this complexity by 𝐶(𝑥).
∙ a minimal complexity of a program that, given 𝑛, computes 𝑥0 . . . 𝑥𝑛 for
all sufficiently large 𝑛. For other 𝑛 (finitely many of them) this program
may provide a wrong answer or never terminate. It is denoted by 𝐶∞(𝑥).
∙ max{𝐶(𝑥0 . . . 𝑥𝑛−1 | 𝑛) | 𝑛 = 0, 1, . . . }, denoted by 𝑀 (𝑥).
∙ lim sup𝑛→∞ 𝐶(𝑥0 . . . 𝑥𝑛−1 | 𝑛), denoted by 𝑀∞(𝑥).
There are evident relations between these notions:
𝑀∞(𝑥) 6 𝑀 (𝑥) 6 𝐶(𝑥)
(up to 𝑂(1) additive term) and
𝑀∞(𝑥) 6 𝐶∞(𝑥) 6 𝐶(𝑥)

2.2. CONDITIONAL COMPLEXITY 57
(with the same precision).
50 Prove that there exists a computable bit sequence 𝑥 such that 𝐶∞(𝑥) is
much less than 𝑀 (𝑥) (and, therefore, much less than 𝐶(𝑥)). More precisely, there
exists a sequence 𝑥𝑚 of computable sequences such that 𝐶∞(𝑥𝑚) = 𝑂(log 𝑚) and
𝑀 (𝑥𝑚) > 𝑚. [Hint: Consider the sequence 𝑥𝑚 = 𝑦𝑚000 . . . , where 𝑦𝑚 is the
lexicographically first string of length 𝑚 that has conditional complexity (given 𝑚)
at least 𝑚.]
51 Prove that for some computable sequence 𝑥 the value of 𝑀 (𝑥) is much
less than 𝐶(𝑥). More precisely, there exist a sequence 𝑥𝑚 of computable sequences
such that 𝑀 (𝑥𝑚) = 𝑂(log 𝑚) and 𝐶(𝑥𝑚) > 𝑚. [Hint: Consider the sequence
𝑥𝑚 = (1BB (𝑚)000 . . . ), where the number of 1s before trailing zeros equals BB (𝑚),
defined on p. 38.]
52 Prove that 𝐶∞(𝑥) 6 2𝑀∞(𝑥) + 𝑂(1). [Hint: Use the same argument as
in Problem 48.]
In fact, the constant 2 in the preceding problem is optimal, as shown in [52].
53 Consider strings of length 𝑛 that have complexity at least 𝑛 (incompressible
strings).
(a) Prove that the number of incompressible strings of length 𝑛 is between 2𝑛−𝑐
and 2𝑛 − 2𝑛−𝑐 (for some 𝑐 and for all 𝑛)
(b) Prove that the cardinality of the set of incompressible strings of length 𝑛
has complexity 𝑛 − 𝑂(1) (note that this implies the statement (a));
(c) Prove that if the string 𝑥 of length 2𝑛 is incompressible, then its halves 𝑥1
and 𝑥2 (of length 𝑛) have complexity 𝑛 − 𝑂(1).
(d) Prove that if a string 𝑥 of length 𝑛 is incompressible, then each its substring
of length 𝑘 has complexity at least 𝑘 − 𝑂(log 𝑛).
(e) Prove that for any constant 𝑐 < 1 all incompressible strings of sufficiently
large length 𝑛 contain a substring of ⌊𝑐 log2 𝑛⌋ zeros.
[Hints: (a) There is at most 2𝑛 − 1 descritions of length less than 𝑛. and part
of them is used for shorter strings: any string of length 𝑛 − 𝑑 (for some 𝑑) has
complexity less than 𝑛. This gives a lower bound for the number of uncompressible
strings. To prove the upper bound, note that strings of length 𝑛 that have prefix
of 𝑘 zeros, could be described by 2 log 𝑘 + (𝑛 − 𝑘) bits.
(b) Let 𝑡 be the shortest description of the number of incompressible strings. If
𝑡 has 𝑛 − 𝑘 bits, then knowing 𝑡 and log 𝑘 additional bits, we can reconstruct first 𝑛
and then the list of all incompressible strings of length 𝑛, so the first incompressible
string has complexity less than 𝑛, a contradiction.
(c) If one part of the string is has a short description, the entire string has a
short description that starts with prefix-free encoding of the difference between the
length and complexity of the compressible part.
(d) If a string has a simple substring, then the entire string can be compressed
(we need to specify the substring, its position and the rest of the string).
(e) Let us count the number of strings of length 𝑛 that do not contain 𝑘 zeros in
a row; a recurrent relation shows that this number grows like a geometric sequence
whose base is the maximal real root of the equation 𝑥 = 2 − (1/𝑥𝑘), and we can
get a bound for complexity of strings that do not have 𝑘 zeros in a row.]

58 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
54 Prove that (for some constant 𝑐) for every infinite sequence 𝑥0𝑥1𝑥2 . . . of
zeros and ones there exist infinitely many 𝑛 such that
𝐶(𝑥0𝑥1 . . . 𝑥𝑛−1) 6 𝑛 − log 𝑛 + 𝑐.
Prove that there is a constant 𝑐 and the sequence 𝑥0𝑥1𝑥2 . . . such that
𝐶(𝑥0𝑥1 . . . 𝑥𝑛−1) > 𝑛 − 2 log 𝑛 − 𝑐
for all 𝑛. [Hint: The series∑︀ 1/𝑛 diverges while the series∑︀ (1/𝑛2) converges. For
details see Theorem 95 and 99.]
This result was published by Martin-L¨of [116] for conditional complexity (and
a reference to an earlier unpiblished work in Russian was given for unconditional
complexity; see also [223, Theorem 2.6]).
55 For a string 𝑥 of length 𝑛 let us define 𝑑(𝑥) and 𝑑𝑐(𝑥) as follows:
𝑑(𝑥) = 𝑛 − 𝐶(𝑥) and 𝑑𝑐(𝑥) = 𝑛 − 𝐶(𝑥 | 𝑛).
Show that they are rather close to each other:
𝑑𝑐(𝑥) − 2 log 𝑑𝑐(𝑥) − 𝑂(1) 6 𝑑(𝑥) 6 𝑑𝑐(𝑥) + 𝑂(1).
[Hint: We need to show that 𝐶(𝑥 | 𝑛) = 𝑛−𝑑 implies 𝐶(𝑥) 6 𝑛−𝑑+2 log 𝑑+𝑂(1).
Indeed, let us take the conditional description of 𝑥 of length 𝑛 − 𝑑 and put it after
the self-delimiting description of 𝑑 that has size 2 log 𝑑 + 𝑂(1). Knowing this string,
we can reconstruct 𝑑, then 𝑛 and finally 𝑥.]
56 Prove that 𝑑(𝑥𝑦) = 𝑑(𝑥)+𝑑(𝑦 | 𝑥)+𝑂(log 𝑑(𝑥𝑦)) for every two 𝑛-bit strings
𝑥 and 𝑦. (Here 𝑑(𝑢) = 𝑙(𝑢) − 𝐶(𝑢).) [Hint: use Problem 36.]
The intuitive meaning of the difference between length and complexity as a
kind of “randomness deficiency” is discussed (for different complexity versions) in
## Chapter 5 and Chapter 14.)
57 Prove that for sufficiently large values of a constant 𝑐 the enumerable set
of pairs (𝑥, 𝑦) such that 𝐶(𝑥 | 𝑦) < 𝑐, is Turing complete (one can solve halting
problem using an oracle for such a set). [Hint: Use Problem 15 and the fact that
the output of a program has 𝑂(1) conditional complexity given the program.]

---

Full document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md) · Page-level evidence: [paper-pages/26-kolmogorov-complexity-and-algorithmic-randomness](../../paper-pages/26-kolmogorov-complexity-and-algorithmic-randomness/index.md)
