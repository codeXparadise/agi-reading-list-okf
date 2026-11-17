---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
section: 2.3. Complexity as the amount of information
section_role: other
section_index: 6
pages: [57, 58, 59, 60, 61, 62, 63, 64, 65, 66]
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "As we know (Theorem 18), the conditional complexity 𝐶(𝑦|𝑥) does not exceed the unconditional one 𝐶(𝑦) (up to a constant). The difference 𝐶(𝑦) −…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.3. Complexity as the amount of information

> Section 6 of 11 from [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md) · `other` · pages 57-66

As we know (Theorem 18), the conditional complexity 𝐶(𝑦|𝑥) does not exceed
the unconditional one 𝐶(𝑦) (up to a constant). The difference 𝐶(𝑦) − 𝐶(𝑦|𝑥) tells
us how much the knowledge of 𝑦 makes 𝑥 easier to describe. So this difference can
be called the amount of information in 𝑥 about 𝑦. Notation: 𝐼(𝑥 : 𝑦).
Theorem 18 says that 𝐼(𝑥 : 𝑦) is non-negative (up to a constant): there exists
some 𝑐 such that 𝐼(𝑥 : 𝑦) > 𝑐 for all 𝑥 and 𝑦.
58 Let 𝑓 be a computable function. Prove that 𝐼(𝑓 (𝑥) : 𝑦) 6 𝐼(𝑥 : 𝑦) + 𝑐 for
some 𝑐 and for all 𝑥, 𝑦 such that 𝑓 (𝑥) is defined.
A generalization of this statement to probabilistic algorithms is possible.
59 Let 𝑓 (𝑥, 𝑟) be a computable function of two arguments, and 𝑟 is chosen at
random uniformly among 𝑛-bit strings for some 𝑛. Then for each 𝑙 the probability
of the event
𝐼(𝑓 (𝑥, 𝑟) : 𝑦) > 𝐼(𝑥 : 𝑦) + 𝑙
does not exceed 2−𝑙+𝑂(𝐶(𝑛)+𝐶(𝑙)). [Hint: Use the conditional version of Problem 41.]

2.3. COMPLEXITY AS THE AMOUNT OF INFORMATION 59
These properties of information can be described as “conservation laws” for
information (about something) in algorithmic or random processes. As Leonid
Levin once put it: “by torturing an uninformed person you do not get any evidence
about the crime”. He discusses this property (for different notion of information)
in [99].
Recall that
𝐶(𝑥, 𝑦) = 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + 𝑂(log 𝐶(𝑥, 𝑦)),
(Theorem 22, p. 53). This allows us to express conditional complexity in terms of
unconditional one: 𝐶(𝑦 | 𝑥) = 𝐶(𝑥, 𝑦) − 𝐶(𝑥) + 𝑂(log 𝐶(𝑥, 𝑦)). Then we get the
following expression for the information:
𝐼(𝑥 : 𝑦) = 𝐶(𝑦) − 𝐶(𝑦 | 𝑥) = 𝐶(𝑥) + 𝐶(𝑦) − 𝐶(𝑥, 𝑦) + 𝑂(log 𝐶(𝑥, 𝑦)).
This expression immediately implies the following theorem:
Theorem 23 (information symmetry).
𝐼(𝑥 : 𝑦) = 𝐼(𝑦 : 𝑥) + 𝑂(log 𝐶(𝑥, 𝑦))
So the difference between 𝐼(𝑥 : 𝑦) and 𝐼(𝑦 : 𝑥) is logarithmically small compared
to 𝐶(𝑥, 𝑦). The following problem shows that at the same time this difference could
be comparable with the values 𝐼(𝑥 : 𝑦) and 𝐼(𝑦 : 𝑥) if they are much less than 𝐶(𝑥, 𝑦).
60 Let 𝑥 be a string of length 𝑛 such that 𝐶(𝑥 | 𝑛) > 𝑛. Show that
𝐼(𝑥 : 𝑛) = 𝐶(𝑛) + 𝑂(1) and 𝐼(𝑛 : 𝑥) = 𝑂(1).
The property of information symmetry (up to a logarithmic term) explains
why 𝐼(𝑥 : 𝑦) (or 𝐼(𝑦 : 𝑥)) is sometimes called mutual information in two strings 𝑥
and 𝑦. The connection between mutual information, conditional and unconditional
complexities and pair complexity can be illustrated by a (rather symbolic) picture
(Fig. 2).
𝐶(𝑥 | 𝑦) 𝐶(𝑦 | 𝑥)
𝐼(𝑥 : 𝑦)
𝑥 𝑦
Figure 2. Mutual information and conditional complexity
It shows that strings 𝑥 and 𝑦 have 𝐼(𝑥 : 𝑦) ≈ 𝐼(𝑦 : 𝑥) bits of mutual information.
Adding 𝐶(𝑥 | 𝑦) bits (information that is present in 𝑥 but not in 𝑦, the left part),
we obtain
𝐼(𝑦 : 𝑥) + 𝐶(𝑥 | 𝑦) ≈ (𝐶(𝑥) − 𝐶(𝑥 | 𝑦)) + 𝐶(𝑥 | 𝑦) = 𝐶(𝑥)
bits (matching the complexity of 𝑥). Similarly, the central part together with
𝐶(𝑦 | 𝑥) (the right part) give 𝐶(𝑦). Finally, all three parts together give us
𝐶(𝑥 | 𝑦) + 𝐼(𝑥 : 𝑦) + 𝐶(𝑦 | 𝑥) = 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) = 𝐶(𝑥 | 𝑦) + 𝐶(𝑦) = 𝐶(𝑥, 𝑦)
bits (all equalities are true up to 𝑂(log 𝑛) for strings 𝑥 and 𝑦 of length at most 𝑛).
In some cases this picture can be understood quite literally. Consider, for
instance, an incompressible string 𝑟 = 𝑟1 . . . 𝑟𝑛 of length 𝑛, so 𝐶(𝑟1 . . . 𝑟𝑛) > 𝑛.

60 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
Then any substring 𝑢 of 𝑥 has complexity 𝑙(𝑢) up to 𝑂(log 𝑛) terms. Indeed, since
𝑢 is a substring of 𝑟, we have 𝑟 = 𝑡𝑢𝑣 for some strings 𝑡, 𝑣. Then
𝑙(𝑟) = 𝐶(𝑟) 6 𝐶(𝑡) + 𝐶(𝑢) + 𝐶(𝑣) 6 𝑙(𝑡) + 𝑙(𝑢) + 𝑙(𝑣) = 𝑙(𝑟)
(up to a logarithmic error) and therefore all the inequalities are equalities (with the
same logarithmic precision).
Now take two overlapping substrings 𝑥 and 𝑦 (Fig. 3). Then 𝐶(𝑥) is the length
of 𝑥, 𝐶(𝑦) is the length of 𝑦 (up to 𝑂(log 𝑛)).
𝑥 : 𝑦	𝑥 | 𝑦 𝑦 | 𝑥
𝑥 𝑦
𝑥, 𝑦
Figure 3. Common information in overlapping substrings
The complexity 𝐶(𝑥, 𝑦) is equal to the length of the union of segments (since
the pair ⟨𝑥, 𝑦⟩ is equivalent to this union plus information about lengths requiring
𝑂(log 𝑛) bits).
Therefore, conditional complexities 𝐶(𝑥 | 𝑦), 𝐶(𝑦 | 𝑥) and the mutual informa-
tion 𝐼(𝑥 : 𝑦) are equal to the lengths of the corresponding segments (up to 𝑂(log 𝑛)).
However, not always the mutual information can be extracted in form of some
string (like it happened in our example, where this common information is just the
intersection of strings 𝑥 and 𝑦). As we will see in Chapter 11, there exist two strings
𝑥 and 𝑦 that have large mutual information 𝐼(𝑥 : 𝑦) but there is no string 𝑧 that
represents (“materializes”) this information in the following sense: 𝐶(𝑧 | 𝑥) ≈ 0,
𝐶(𝑧 | 𝑦) ≈ 0 (all information that is present in 𝑧 is also present both in 𝑥 and in 𝑦)
and 𝐶(𝑧) ≈ 𝐼(𝑥 : 𝑦) (all mutual information is extracted). In our last example we
can take the intersection substring for 𝑧, but in general this is not possible.
61 Prove that for any string 𝑥 of length at most 𝑛 the expected value of the
mutual information 𝐼(𝑥 : 𝑦) in 𝑥 and random string 𝑦 of length 𝑛 is 𝑂(log 𝑛).
Now we move to triples of strings instead of pairs. Here we have an important
tool that can be called relativization: most of the results proved for unconditional
complexities remain valid for conditional complexities (and proofs remain valid with
minimal changes). Let us give some example of this type.
A theorem about the complexity of pairs (p. 45) says that
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 2 log 𝐶(𝑥) + 𝐶(𝑦) + 𝑂(1).
Replacing all complexities by conditional ones (with the same condition 𝑧 in all
cases), we get the following inequality:
𝐶(𝑥, 𝑦 | 𝑧) 6 𝐶(𝑥 | 𝑧) + 2 log 𝐶(𝑥 | 𝑧) + 𝐶(𝑦 | 𝑧) + 𝑂(1),
By conditional complexity of a pair 𝑥, 𝑦 relative to 𝑧 we mean, as one can expect,
the conditional complexity of its encoding: 𝐶(𝑥, 𝑦 | 𝑧) = 𝐶([𝑥, 𝑦] | 𝑧). As for un-
conditional complexity, the choice of encoding is not important (the complexity
changes by 𝑂(1)).

2.3. COMPLEXITY AS THE AMOUNT OF INFORMATION 61
The proof of this relativized inequality repeats the proof of the unrelativized
one: we combine description 𝑝 for 𝑥 (with condition 𝑧) and description 𝑞 for 𝑦 (with
condition 𝑧) into a string ˆ𝑝𝑞 that is a description of [𝑝, 𝑞] (with condition 𝑧) relative
to some suitable conditional decompressor.
So this is nothing really new. However, we may express all the conditional
complexities in terms of unconditional ones: recall that 𝐶(𝑥, 𝑦 | 𝑧) = 𝐶(𝑥, 𝑦, 𝑧) −
𝐶(𝑧) and 𝐶(𝑥 | 𝑧) = 𝐶(𝑥, 𝑧) − 𝐶(𝑧), 𝐶(𝑦 | 𝑧) = 𝐶(𝑦, 𝑧) − 𝐶(𝑧) (with logarithmic
precision). Then we get the following theorem:
Theorem 24.
𝐶(𝑥, 𝑦, 𝑧) + 𝐶(𝑧) 6 𝐶(𝑥, 𝑧) + 𝐶(𝑦, 𝑧) + 𝑂(log 𝑛)
for all strings 𝑥, 𝑦, 𝑧 of complexity at most 𝑛.
Sometimes this inequality is called the basic inequality for complexities.
The same relativization can be applied to Theorem 21 (p. 51) that relates
the complexity of a pair and conditional complexity. Then we get the following
statement:
Theorem 25.
𝐶(𝑥, 𝑦 | 𝑧) = 𝐶(𝑥 | 𝑧) + 𝐶(𝑦 | 𝑥, 𝑧) + 𝑂(log 𝑛),
for all strings 𝑥, 𝑦, 𝑧 of complexity at most 𝑛.
Proof. We can follow the proof of theorem 21, replacing unconditional de-
scriptions by conditional ones (with 𝑧 as the condition). Doing this, we replace
𝐶(𝑦 | 𝑥) by 𝐶(𝑦 | 𝑥, 𝑧). One can say that now we work in three-dimensional space
with coordinates 𝑥, 𝑦, 𝑧 and apply the same arguments simultaneously in all planes
parallel to 𝑥𝑦 plane.
If this argument does not look convincing for you, there is a more formal one.
Express all the conditional complexities in terms of unconditional ones:
𝐶(𝑥, 𝑦 | 𝑧) = 𝐶(𝑥, 𝑦, 𝑧) − 𝐶(𝑧),
and for the right-hand side
𝐶(𝑥 | 𝑧) + 𝐶(𝑦 | 𝑥, 𝑧) = 𝐶(𝑥, 𝑧) − 𝐶(𝑧) + 𝐶(𝑦, 𝑥, 𝑧) − 𝐶(𝑥, 𝑧).
We see that both sides coincide (up to 𝑂(log 𝑛)). (A careful reader may note that
this simplified argument gives larger hidden constants in 𝑂(log 𝑛)-notation.) 
62 Proof that in Theorem 25 a weaker assumption “𝐶(𝑥 | 𝑧) and 𝐶(𝑦 | 𝑥, 𝑧) do
not exceed 𝑛” is sufficient.
We also relativize the definition of mutual information and let 𝐼(𝑥 : 𝑦 | 𝑧) be the
difference 𝐶(𝑦 | 𝑧) − 𝐶(𝑦 | 𝑥, 𝑧). As for the case of (unconditional) information, this
quantity is non-negative (with 𝑂(1) precision). Replacing conditional complexities
by the expressions involving unconditional ones (with logarithmic precision), we
can rewrite the inequality 𝐼(𝑥 : 𝑦 | 𝑧) > 0 as follows:
𝐶(𝑦 | 𝑧) − 𝐶(𝑦 | 𝑥, 𝑧) = 𝐶(𝑦, 𝑧) − 𝐶(𝑧) − 𝐶(𝑦, 𝑥, 𝑧) + 𝐶(𝑥, 𝑧) > 0.
So we get the basic inequality of Theorem 24 again.
In fact, almost all known equalities and inequalities that involve complexities
(unconditional and conditional) and information (and have logarithmic precision)
are immediate consequences of Theorems 21 and 24. The first examples of linear

62 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
inequalities for complexities that do not follow from basic inequalities were found
fairly recently (see [220, 221]) and they are rather complicated and not very intu-
itive. We discuss them in Section 10.13; we conclude this discussion by two simple
corollaries of basic inequalities.
Independent strings. We say that strings 𝑥 and 𝑦 are “independent” if
𝐼(𝑥 : 𝑦) ≈ 0. We need to specify what we mean by “≈”, but we always ignore the
terms of order 𝑂(log 𝑛) where 𝑛 is the maximal length (or complexity) of the strings
involved.
Independent strings could be considered as some counterpart of the notion of
independent random variables, which is central in the probability theory. There is
a simple observation: if a random variable 𝜉 is independent with the pair of random
variables ⟨𝛼, 𝛽⟩, then 𝜉 is independent with 𝛼 and with 𝛽 (separately).
The Kolmogorov complexity counterpart of this statement (if a string 𝑥 is
independent with a pair ⟨𝑦, 𝑧⟩, then 𝑥 is independent with 𝑦 and 𝑥 is independent
with 𝑧) can be expressed as an inequality:
𝐼(𝑥 : ⟨𝑦, 𝑧⟩) > 𝐼(𝑥 : 𝑦)
(and the similar inequality for 𝑧 instead of 𝑦). This inequality is indeed true (with
logarithmic precision), and it is easy to see if we rewrite it in terms of unconditional
complexities:
𝐶(𝑥) + 𝐶(𝑦, 𝑧) − 𝐶(𝑥, 𝑦, 𝑧) > 𝐶(𝑥) + 𝐶(𝑦) − 𝐶(𝑥, 𝑦),
which after cancellation of similar terms gives a basic inequality (Theorem 24). (In
classical probability theory one may also apply a similar inequality for Shannon
entropies.)
Complexity of pairs and triples. On the other hand, to prove the following
theorem (which we have already mentioned on p.22), it is convenient to replace
unconditional complexities by conditional ones:
Theorem 26.
2𝐶(𝑥, 𝑦, 𝑧) 6 𝐶(𝑥, 𝑦) + 𝐶(𝑥, 𝑧) + 𝐶(𝑦, 𝑧) + 𝑂(log 𝑛),
for all strings 𝑥, 𝑦, 𝑧 of complexity at most 𝑛.
Proof. Moving 𝐶(𝑥, 𝑦) and 𝐶(𝑥, 𝑧) to the left-hand side and replacing the
differences 𝐶(𝑥, 𝑦, 𝑧) − 𝐶(𝑥, 𝑦) and 𝐶(𝑥, 𝑦, 𝑧) − 𝐶(𝑥, 𝑧) by conditional complexities
𝐶(𝑧 | 𝑥, 𝑦) and 𝐶(𝑦 | 𝑥, 𝑧), we get the following inequality:
𝐶(𝑧 | 𝑥, 𝑦) + 𝐶(𝑦 | 𝑥, 𝑧) 6 𝐶(𝑦, 𝑧) + 𝑂(log 𝑛).
It remains to rewrite the right-hand side of this inequality as 𝐶(𝑦) + 𝐶(𝑧 | 𝑦), and
note that 𝐶(𝑧 | 𝑥, 𝑦) 6 𝐶(𝑧 | 𝑦) and 𝐶(𝑦 | 𝑥, 𝑧) 6 𝐶(𝑦). 
Instead we could just add two inequalities (the basic one and the inequality for
the complexity of a pair):
𝐶(𝑥, 𝑦, 𝑧) + 𝐶(𝑦) 6 𝐶(𝑥, 𝑦) + 𝐶(𝑦, 𝑧) + 𝑂(log 𝑛),
𝐶(𝑥, 𝑦, 𝑧) 6 𝐶(𝑦) + 𝐶(𝑥, 𝑧) + 𝑂(log 𝑛),
and then cancel 𝐶(𝑦) in both sides. (This proof, as well as the previous one, has
an important esthetic problem: both treat 𝑥, 𝑦, 𝑧 in a non-symmetric way while the
statement of the theorem is symmetric.)

2.3. COMPLEXITY AS THE AMOUNT OF INFORMATION 63
We return to the inequality of Theorem 26 and to its geometric consequences
in Chapter 10.
We can provide a more systematic treatment of the different complexity quan-
tities related to three strings as follows. There are seven basic quantities: three
of them are complexities of individual strings, another three are complexities of
pairs and one more is the complexity of the entire triple. Other quantities such as
conditional complexity and mutual information can be expressed in terms of these
seven complexities. To understand better what requirements these seven quantities
should satisfy, let us make a linear transformation in the 7-dimensional space and
switch to new coordinates. Consider seven variables 𝑎1, 𝑎2, . . . , 𝑎7 that correspond
to 7 regions shown in Fig. 4.
𝑥 𝑦
𝑧
1 2 3
4 5 6
7
Figure 4. New coordinates 𝑎1, 𝑎2, . . . , 𝑎7.
Formally, the coordinate transformation is given by the following equations:
𝐶(𝑥) = 𝑎1 + 𝑎2 + 𝑎4 + 𝑎5,
𝐶(𝑦) = 𝑎2 + 𝑎3 + 𝑎5 + 𝑎6,
𝐶(𝑧) = 𝑎4 + 𝑎5 + 𝑎6 + 𝑎7,
𝐶(𝑥, 𝑦) = 𝑎1 + 𝑎2 + 𝑎3 + 𝑎4 + 𝑎5 + 𝑎6,
𝐶(𝑥, 𝑧) = 𝑎1 + 𝑎2 + 𝑎4 + 𝑎5 + 𝑎6 + 𝑎7,
𝐶(𝑦, 𝑧) = 𝑎2 + 𝑎3 + 𝑎4 + 𝑎5 + 𝑎6 + 𝑎7,
𝐶(𝑥, 𝑦, 𝑧) = 𝑎1 + 𝑎2 + 𝑎3 + 𝑎4 + 𝑎5 + 𝑎6 + 𝑎7.
Indeed, it is easy to see that these equations determine an invertible linear transfor-
mation of R7: each 7-tuple of complexities corresponds to unique value of variables
𝑎1, . . . , 𝑎7.
Conditional complexities and mutual informations could be expressed in terms
of complexities and therefore could be rewritten in new coordinates. For example,
𝐼(𝑥 : 𝑦) = 𝐶(𝑥) + 𝐶(𝑦) − 𝐶(𝑥, 𝑦) = 𝑎2 + 𝑎5 and 𝐶(𝑥 | 𝑦) = 𝐶(𝑥, 𝑦) − 𝐶(𝑦) = 𝑎1 + 𝑎4.
What is the intuitive meaning of these new coordinates? It is easy to see that
𝑎1 = 𝐶(𝑥 | 𝑦, 𝑧) (with logarithmic precision). The meaning of 𝑎3 (and 𝑎7) is similar.
The coordinate 𝑎2 is (with the same precision) 𝐼(𝑥 : 𝑦 | 𝑧); coordinates 𝑎4 and 𝑎6
have similar meaning (see Fig. 5). In particular, we conclude that for any strings
𝑥, 𝑦, 𝑧 the corresponding values of coordinates 𝑎1, 𝑎2, 𝑎3, 𝑎4, 𝑎6, 𝑎7 are non-negative
(up to 𝑂(log 𝑛) for strings 𝑥, 𝑦, 𝑧 of complexity at most 𝑛).
The coordinate 𝑎5 is more delicate. Informally, we would like to understand
it as the “amount of mutual information in three strings 𝑥, 𝑦, 𝑧”. Sometimes the

64 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
𝑥 𝑦
𝑧
𝐶(𝑥 | 𝑦, 𝑧)
𝐼(𝑥 : 𝑦 | 𝑧) 𝐶(𝑦 | 𝑥, 𝑧)
𝐼(𝑥 : 𝑧 | 𝑦)
𝐼(𝑥 : 𝑦 : 𝑧)
𝐼(𝑦 : 𝑧 | 𝑥)
𝐶(𝑧 | 𝑥, 𝑦)
Figure 5. The complexity interpretation of new coordinates.
notation 𝐼(𝑥 : 𝑦 : 𝑧) is used. However, the meaning of this expression is not quite
clear, especially if we take into accout that 𝑎5 can be negative.
Consider the following example where 𝑎5 < 0. Let 𝑥 and 𝑦 be two halves of
an incompressible strings of length 2𝑛. Then 𝐶(𝑥) = 𝑛, 𝐶(𝑦) = 𝑛, 𝐶(𝑥, 𝑦) = 2𝑛
and 𝐼(𝑥 : 𝑦) = 0 (up to 𝑂(log 𝑛)). Consider a string 𝑧 of length 𝑛 which is a bitwise
sum modulo 2 of 𝑥 and 𝑦 (XOR-operation). Then each of the strings 𝑥, 𝑦, 𝑧 can
be reconstructed if two others are known; therefore the complexities of all pairs
𝐶(𝑥, 𝑦), 𝐶(𝑦, 𝑧), 𝐶(𝑥, 𝑧) are equal to 2𝑛 (again up to 𝑂(log 𝑛)), and the complexity
𝐶(𝑥, 𝑦, 𝑧) is also 2𝑛. The complexity of 𝑧 is equal to 𝑛 (it can not be larger, since
the length is 𝑛; on the other hand, it cannot be smaller, since 𝑧 and 𝑦 form a pair
of complexity 2𝑛).
So we get the following values of 𝑎1, . . . , 𝑎7 for this example (Fig. 6):
0 𝑛 0
𝑛 −𝑛 𝑛
0
Figure 6. Two independent incompressible strings of length 𝑛
and their XOR.
Note that even if 𝑎5 is negative, the sums 𝑎5 + 𝑎2, 𝑎5 + 𝑎4 and 𝑎5 + 𝑎6, being
mutual informations for pairs, are non-negative. (In our examples these sums are
equal to 0.)
This example corresponds to the simple case of secret sharing of secret 𝑧 be-
tween two people: if one of them knows 𝑥 and the other one knows 𝑦, then none of

2.3. COMPLEXITY AS THE AMOUNT OF INFORMATION 65
them has any information about 𝑧 in isolation (since 𝐼(𝑥 : 𝑧) ≈ 0 and 𝐼(𝑦 : 𝑧) ≈ 0)),
but together they can reconstruct 𝑧 as a bitwise sum of 𝑥 and 𝑦.
One can check that we have already given a full list of inequalities that are true
for complexities of three strings and their combinations (all 𝑎𝑖, except for 𝑎5, are
non-negative, as well as three sums mentioned above). We return to this question
in Chapter 10.
Our diagram is a good mnenonic tool. For example, consider again the inequal-
ity
𝐶(𝑥, 𝑦, 𝑧) 6 𝐶(𝑥, 𝑦) + 𝐶(𝑥, 𝑧) + 𝐶(𝑦, 𝑧).
In our new variables it can be rewritten as 𝑎2 + 𝑎4 + 𝑎5 + 𝑎6 > 0 (you can easily
check it by counting the multiplicity of each 𝑎𝑖 in both sides of the inequality). It
remains to note that 𝑎2 + 𝑎5 > 0, 𝑎4 > 0 and 𝑎6 > 0. (Alas, the symmetry is broken
again!)
63 Prove that 𝐼(𝑥𝑦 : 𝑧) = 𝐼(𝑥 : 𝑧) + 𝐼(𝑦 : 𝑧 | 𝑥) + 𝑂(log 𝑛) for strings 𝑥, 𝑦, 𝑧 of
complexity at most 𝑛. [Hint: Use the diagram.]
This problem shows that information in 𝑥𝑦 about 𝑧 can be somehow split into
two parts: information in 𝑥 about 𝑧 and information in 𝑦 about 𝑧 (when 𝑥 is
known). This is somehow similar to the equality 𝐶(𝑥, 𝑦) = 𝐶(𝑥) + 𝐶(𝑦 | 𝑥), but now
complexity is replaced by the quantity of information about 𝑧. As a corollary we
immediately get that if 𝑥𝑦 is independent with 𝑧 then 𝑥 in independent with 𝑧 and,
at the same time 𝑦 is independent with 𝑧 when 𝑥 is known. (Here independence
means that mutual information is negligible.) A symmetric argument shows that 𝑦
is independent with 𝑧 and 𝑥 is independent with 𝑧 when 𝑦 is known.
64 Show that properties “𝑥 is independent with 𝑦” and “𝑥 is independent
with 𝑦 when 𝑧 is known” are quite different: each of them can be true when the
other one is false.
65 We say that strings 𝑥, 𝑦, 𝑧, 𝑡 form a Markov chain (a well known notion
in the probability theory now transferred to the algorithmic information theory) if
𝐼(𝑥 : 𝑧 | 𝑦) and 𝐼(⟨𝑥, 𝑦⟩ : 𝑡 | 𝑧) are negligible. (Of course, we need to specify what is
“negligible” to get a formal definition.) Show that the reversed sequence of strings
also forms a Markov chain, i.e., that 𝐼(𝑡 : 𝑦 | 𝑧) and 𝐼(⟨𝑡, 𝑧⟩ : 𝑥 | 𝑦) are negligible. [Hint:
Since 𝐼(⟨𝑥, 𝑦⟩ : 𝑡 | 𝑧) = 𝐼(𝑦 : 𝑡 | 𝑧) + 𝐼(𝑥 : 𝑡 | 𝑦, 𝑧), the left hand side in this equality is
zero if and only if both terms in the right hand side are zero; and the second term
in the right-hand side does not change when the order of 𝑥, 𝑦, 𝑧, 𝑡 is reversed.]

CHAPTER 3
Martin-L¨	of randomness
Here we interrupt the exposition of Kolmogorov complexity and its properties
and define another basic notion of the algorithmic information theory, the notion
of Martin-L¨of random (or “typical”) sequence. This chapter does not refer to the
preceding one and is not used until Chapter 5 where we characterize randomness
in terms of Kolmogorov complexity.
Let us recall some basic facts of measure theory for the case of the Cantor space
of infinite sequences of zeros and ones.

---

Full document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md) · Page-level evidence: [paper-pages/26-kolmogorov-complexity-and-algorithmic-randomness](../../paper-pages/26-kolmogorov-complexity-and-algorithmic-randomness/index.md)
