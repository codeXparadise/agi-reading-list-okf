---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
section: 1.2. Algorithmic properties
section_role: other
section_index: 3
pages: [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "The function 𝐶 is upper semicomputable. On the other hand, it is not com- putable and, moreover, it has no unbounded computable lower bounds (Theorem…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 1.2. Algorithmic properties

> Section 3 of 11 from [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md) · `other` · pages 34-44

The function 𝐶 is upper semicomputable. On the other hand, it is not com-
putable and, moreover, it has no unbounded computable lower bounds (Theorem 6,
p. 19).
This implies that all optimal description modes are necessarily non-total, that
is, some strings describe nothing. Indeed, if a description mode 𝐷 is total then we
can compute 𝐶𝐷 (𝑥) just by trying all descriptions in the lexicographical order until
we find the shortest one.
At first glance, this contradicts to our intuition: the bigger the domain of 𝐷
is, the better 𝐷 is. If optimal decompressor 𝐷 is undefined on some string 𝑦 then
we can define another description mode 𝐷′ as follows. Let 𝐷′(𝑦) be equal to a
string 𝑧 of complexity (with respect to 𝐷) greater than 𝑙(𝑦) and let 𝐷′ coincide
with 𝐷 on all other strings. The description mode 𝐷′ is a bit better than 𝐷, as the
complexity of all strings except 𝑧 remains the same while the complexity of 𝑧 has
been decreased.
There is no formal contradiction here, as 𝐷 is still not worse than 𝐷′ (they differ
only at one point, the difference between the complexities is bounded by a constant,
and both 𝐷 and 𝐷′ are optimal). However, this is still a bit strange. This observa-
tion was made by Yu. Manin in his book “Computable and non-computable” [113]
(by the way, in this book he also discussed the computational power of quantum
mechanics long before quantum computing became fashionable).
A similar argument shows that the domain of every optimal description mode
is undecidable. (The set of strings is called decidable, or computable, if there is an
algorithm that for any given string decides whether it belongs to the set or not.)
Indeed, if there were an algorithm deciding whether 𝐷(𝑥) is defined or not, then
there would be a total computable extension of 𝐷 (for example, let 𝐷(𝑥) = 0 for all
𝑥 outside the domain of 𝐷). This extension would be a total optimal description
mode, but this is impossible as we have seen.
As a byproduct we get an algorithm whose domain is undecidable. This is one
of the central theorems in computability theory (see, for example, [182]).
In general the notion of Kolmogorov complexity has a lot of connections with
computability theory. Recently many interesting facts were discovered, see [146,
49]. We consider here only two basic examples (a simple set of simple strings, and
the complexity of large numbers).
1.2.1. Simple strings and simple sets. In this section, the word “simple”
has two unrelated meanings. First, when applied to strings, it means that the
Kolmogorov complexity of the string is small. Second, it is applied to sets of

36 1. PLAIN KOLMOGOROV COMPLEXITY
strings. The notion of a simple set was introduced by an American logician Emil
Post and has no relation to Kolmogorov complexity.
Definition. An enumerable set 𝐴 is simple (according to Post) if its comple-
ment is infinite but has no infinite enumerable subset.
Call a string 𝑥 “simple” if 𝐶(𝑥) < 𝑙(𝑥)/2.
Theorem 10. The set of all “simple” strings is simple in the sense of Post.
Proof. That set 𝑆 of all “simple” strings is enumerable. Indeed, the function
𝐶 is upper semicomputable, and if 𝐶(𝑥) is less than |𝑥|/2, this can be seen while
approximating 𝐶(𝑥) from above.
The number of strings of complexity less than 𝑛/2 does not exceed 2𝑛/2. There-
fore the fraction of “simple” strings among strings of length 𝑛 is negligible, and the
complement of 𝑆 is infinite.
Assume now that the complement of 𝑆 has an infinite enumerable subset 𝑈 . We
can use 𝑈 to obtain a computable unbounded lower bound of 𝐶. To find a string of
complexity greater than 𝑡 we can generate elements of 𝑈 until we find a string 𝑢𝑡 of
length greater than 2𝑡. As 𝑈 is infinite, there is such a string. The complexity of 𝑢𝑡
is greater than 𝑡, otherwise 𝑢𝑡 is simple. Without loss of generality we can assume
that the strings 𝑢𝑡, 𝑡 = 1, 2, . . . are pairwise different. Thus the function 𝑢𝑡 ↦ → 𝑡
is a computable unbounded lower bound for 𝐶. This contradicts to Theorem 6
(page 19). 
Note that the choice of the threshold 𝑙(𝑥)/2 in the definition of a simple string
was not essential. The proof of Theorem 10 would work as well with 𝑙(𝑥) − 1 or
log log 𝑙(𝑥) in place of 𝑙(𝑥)/2.
1.2.2. Complexity of large numbers. Let us identify a natural number 𝑚
with the binary string having index 𝑚 in the standard enumeration of binary strings.
In this way 𝐶 becomes a function of a natural argument. The function 𝐶(𝑚) goes
to infinity as 𝑚 → ∞. Indeed, for all 𝑛 there are only finitely many integers of
complexity less than 𝑛. However, the convergence is not effective. That is, there
is no algorithm that for every given 𝑛 finds a number 𝑁 such that the complexity
of 𝑁 and of all larger numbers is bigger than 𝑛. Indeed, such an algorithm would
provide an effective way to describe the number 𝑁 , whose complexity is at least 𝑛,
by log 𝑛 + 𝑂(1) bits. We have seen this in the proof of Theorem 6 (p. 19).
In this section, we study in detail the rate of convergence of 𝐶 to infinity.
Following Chaitin [31], we consider for every natural 𝑛 the largest number B (𝑛)
whose complexity is at most 𝑛:
B (𝑛) = max{𝑚 ∈ N | 𝐶(𝑚) 6 𝑛}
The function 𝑛 ↦ → B (𝑛) may be called the modulus of the convergence of 𝐶(𝑚) to
infinity. Indeed, 𝐾(𝑥) > 𝑛 for all 𝑥 > B (𝑛) (and B (𝑛) is the minimal number with
this property). Note also that it can happen (for small values of 𝑛) that 𝐶(𝑚) > 𝑛
for all 𝑚. In this case we let B (𝑛) = −1.
The function B can be considered as an inverse function to the function
𝐶>(𝑁 ) = min{𝐶(𝑚) | 𝑚 > 𝑁 }.
The function 𝐶> grows very slowly. It takes the value 𝑛 between 𝐵(𝑛 − 1) and
𝐵(𝑛), more precisely, on the interval (B (𝑛 − 1), B (𝑛)]. The slow increase of 𝐶>

1.2. ALGORITHMIC PROPERTIES 37
𝑚
𝐶(𝑚)
𝑛 − 1
𝐵(𝑛 − 1)
𝑛
𝐵(𝑛) = 𝐵(𝑛 + 1)
𝑛 + 1
Figure 1. The definition of B (𝑛): the value 𝐶(𝑚) does not exceed
𝑛−1 for 𝑚 = B (𝑛−1) (the case when 𝐶(B (𝑛−1)) = 𝑛−1 is shown),
and 𝐶(𝑚) > 𝑛 for all 𝑚 > B (𝑛 − 1). At the point 𝑚 = B (𝑛)
the value of 𝐶 does not exceed 𝑛 (the case when 𝐶(B (𝑛)) = 𝑛
is shown), and 𝐶(𝑚) > 𝑛 for all 𝑚 > B (𝑛). The case when
𝐶(𝑚) is even greater than 𝑛 + 1 for all 𝑚 > B (𝑛) is shown, thus
B (𝑛 + 1) = B (𝑛). For 𝑚 ∈ (B (𝑛 − 1), B (𝑛)] the value of the
function 𝐶>(𝑚) is equal to 𝑛.
corresponds to the fast increase of B . The latter can be illustrated by the following
result.
Theorem 11. Let 𝑓 be a computable function from N to N. Then B (𝑛) > 𝑓 (𝑛)
for all but finitely many 𝑛.
Note that 𝑓 may be a partial function. In this case we claim that B (𝑛) > 𝑓 (𝑛)
for all sufficiently large 𝑛 that are in the domain of 𝑓 .
Proof. As algorithmic transformations do not increase complexity, for some
constant 𝑐 for all 𝑛 we have
𝐶(𝑓 (𝑛)) 6 𝐶(𝑛) + 𝑂(1) 6 log 𝑛 + 𝑐.
On the other hand, the definition of B and the inequality 𝑓 (𝑛) > B (𝑛) imply
𝐶(𝑓 (𝑛)) > 𝑛. Thus
𝑛 < 𝐶(𝑓 (𝑛)) 6 log 𝑛 + 𝑐
whenever 𝑓 (𝑛) > B (𝑛). This can happen only for finitely many 𝑛. 
Let us reformulate the definition of B (𝑛) as follows. Let 𝐷 be the optimal
description mode used in the definition of Kolmogorov complexity. Then B (𝑛) is
the maximal value of 𝐷 on strings of length at most 𝑛:
B (𝑛) = max{𝐷(𝑥) | 𝑙(𝑥) 6 𝑛}.
Recall that we identify natural numbers and binary strings and consider the values
of 𝐷 as natural numbers. The minimum of the empty set is defined as −1.
Consider now any partial computable function 𝑑 : Ξ → N in place of 𝐷 and let
B 𝑑(𝑛) = max{𝑑(𝑥) | 𝑙(𝑥) 6 𝑛 and 𝑑(𝑥) is defined}.
Next theorem shows that the function B is the largest function among all functions
B 𝑑, in the following sense:

38 1. PLAIN KOLMOGOROV COMPLEXITY
Theorem 12. For every function 𝑑 there is a constant 𝑐 such that
B 𝑑(𝑛) 6 B (𝑛 + 𝑐)
for all 𝑛.
Proof. For every 𝑥 of length at most 𝑛 the complexity of 𝑑(𝑥) is less than
𝑛 + 𝑐 for some constant 𝑐. Indeed, the complexity of 𝑑(𝑥) exceeds at most by a
constant the complexity of 𝑥, which is less than 𝑛 + 𝑂(1). Hence 𝑑(𝑥) does not
exceed the largest number of complexity 𝑛 + 𝑐 or less, i.e., B (𝑛 + 𝑐). 
This (trivial) observation is useful in the following special case. Let 𝑀 be an
algorithm and let 𝑋 be a set of binary strings. A halting problem for 𝑀 restricted
to 𝑋 is the following problem: given a string 𝑥 ∈ 𝑋, find out whether 𝑀 terminates
on 𝑥 or not.
A classical result in computability theory states that for some algorithm 𝑀 the
unrestricted halting problem (𝑋 = Ξ) for 𝑀 is undecidable.
We are interested now in the case when 𝑋 is the set of all strings of bounded
length. Fix some algorithm 𝑀 and consider the running time 𝑡(𝑥) of 𝑀 for some
input 𝑥. If 𝑀 does not halt on 𝑥, then 𝑡(𝑥) is undefined. Thus the domains of 𝑡
and 𝑀 coincide. By definition, B 𝑡(𝑛) is the maximal running time of 𝑀 on inputs
of length at most 𝑛. If we know B 𝑡(𝑛) or any larger number 𝑚, we can solve the
halting problem for 𝑀 and every input 𝑥 of length at most 𝑛: Run 𝑀 on input 𝑥;
if the computation does not terminate after 𝑚 steps, it never terminates.
We have seen that B 𝑡(𝑛) 6 B (𝑛 + 𝑐) for some constant 𝑐 (depending on 𝑀 ).
Therefore the knowledge of B (𝑛 + 𝑐) or any greater number is enough to solve the
halting problem of 𝑀 on inputs of length at most 𝑛. In other words, the following
holds:
Theorem 13. For every algorithm 𝑀 there is a constant 𝑐 and another al-
gorithm 𝐴 having the following property. For every 𝑛 and for every number 𝑡 >
B (𝑛 + 𝑐) the algorithm 𝐴, given 𝑛 and 𝑡, produces the list of all strings 𝑥 of length
at most 𝑛 such that 𝑀 halts on input 𝑥.
This theorem says that the halting problem for inputs of length at most 𝑛 is
reducible to the problem of finding a number greater than B (𝑛 + 𝑐).
If 𝑀 is the optimal decompressor 𝐷 then the converse is also true: given 𝑛 and
the list of all strings 𝑥 of length at most 𝑛 in the domain of 𝐷 we can find B (𝑛).
Continuing this argument, we can prove the following result:
Theorem 14. Let BB (𝑛) denote the maximal running time of the optimal
decompressor 𝐷 on strings of length at most 𝑛 (in the domain of 𝐷). Then
BB (𝑛) 6 B (𝑛 + 𝑐) and B (𝑛) 6 BB (𝑛 + 𝑐)
for some 𝑐 and all 𝑛.
Proof. Let 𝛼𝑛 be the most time-consuming description of length at most 𝑛,
that is, the string 𝑥 of length at most 𝑛 in the domain of 𝐷 that maximizes the
running time of 𝐷 on 𝑥. Knowing 𝑛 and 𝛼𝑛, one can generate the list of all strings
of length at most 𝑛 in the domain of 𝐷, and hence the number BB (𝑛). Both 𝑛 and
𝛼𝑛 can be encoded in one string of length 𝑛 + 1, the string 0 . . . 01𝛼𝑛 (there are
𝑛 − 𝑙(𝛼𝑛) zeros in the beginning). Therefore, the Kolmogorov complexity of BB (𝑛)
is at most 𝑛 + 𝑂(1), and BB (𝑛) 6 B (𝑛 + 𝑐) for some 𝑐 and all 𝑛.

1.2. ALGORITHMIC PROPERTIES 39
Let us prove the second inequality of the theorem showing that every 𝑡 > BB (𝑛)
has complexity at least 𝑛 − 𝑂(1). Assume that 𝑡 has a description 𝑢 of length 𝑘; we
need to show that 𝑘 > 𝑛−𝑂(1). Knowing 𝑢 and 𝑛, one can effectively obtain a string
of complexity greater than 𝑛. Indeed, we reconstruct 𝑡 (from 𝑢) and wait 𝑡 steps for
every description of size at most 𝑛. This gives us all strings of complexity at most
𝑛, and we can take some other string. By definition of B (𝑛) we conclude that the
pair (𝑢, 𝑛) has complexity at least 𝑛 − 𝑂(1). On the other hand, this pair can be
described using 𝑘+𝑂(log(𝑛−𝑘)) bits if we join the self-delimited description of 𝑛−𝑘
and 𝑢. Therefore, 𝑘 +𝑂(log(𝑛−𝑘)) > 𝑛−𝑂(1), and (𝑛−𝑘)−𝑂(log(𝑛−𝑘)) 6 𝑂(1),
therefore 𝑛 − 𝑘 6 𝑂(1). (We assumed that 𝑛 > 𝑘, otherwise there is nothing to
prove.) 
This theorem shows that, within to an additive constant in the argument, B (𝑛)
is the maximal running time of the optimal decompressor on descriptions of length
at most 𝑛. A similar function appeared in the literature under the name of “busy
beaver function”. It was introduced by T. Rad´o [149] and is defined usually as the
maximal number of 1s on the tape of Turing machine with 𝑛 states and binary tape
alphabet (1 and blank) after it terminates (starting with blank tape).
More generally, given 𝑛 and any object from the following list we can find any
other object from the list for a little bit smaller value of 𝑛:
(a): the list of all strings of Kolmogorov complexity at most 𝑛 with their
Kolmogorov complexities;
(b): the number of such strings;
(c): B (𝑛);
(d): BB (𝑛);
(e): the list of all strings of length at most 𝑛 in the domain of the optimal
decompressor (the halting problem for the optimal decompressor restricted
to inputs of length at most 𝑛);
(f ): the number of such strings;
(g): the most time-consuming input of length at most 𝑛 for the optimal
decompressor;
(h): the graph 𝑇𝑛 of the function 𝐶(𝑥) on strings 𝑥 of length 𝑛;
(i): the lexicographically first string 𝛾𝑛 of length 𝑛 with Kolmogorov com-
plexity at least 𝑛 (it exists since the number of strings of complexity less
than 𝑛 is less than 2𝑛).
More specifically, the following statement holds.
Theorem 15. The complexity of every object in (a)–(i) is equal to 𝑛 + 𝑂(1).
These objects are equivalent to each other in the following sense: Let 𝑋𝑛 and 𝑌𝑛
are objects described in two items among (a)–(i). Then there is a constant 𝑐 and
an algorithm that given 𝑛 and 𝑋𝑛 finds 𝑌𝑛−𝑐.
Proof. The equivalence of (d), (e), (f) and (g) is easy. Each of the objects (d),
(e), (f) and (g) together with 𝑛 determines the list of all terminating computations
of the optimal decompressor 𝐷 on strings of length at most 𝑛. Indeed, knowing
BB (𝑛) we can run 𝐷 on all inputs of length at most 𝑛 for BB (𝑛) steps. Knowing
(e), that is, the list of strings of length at most 𝑛 in the domain of 𝐷, we can run
𝐷 on all those strings until all the computations terminate (and we know that this
happens). Knowing (f), the number of strings of length at most 𝑛 on which 𝐷
terminates, we run 𝐷 on all strings of length at most 𝑛 until the desired number

40 1. PLAIN KOLMOGOROV COMPLEXITY
of computations do terminate. Knowing the string (g), we run 𝐷 on that string,
count the number of steps 𝑡 and then run 𝐷 on all other strings of length at most
𝑛 for 𝑡 steps.
Conversely, the list of all halting computations of the optimal decompressor 𝐷
on strings of length at most 𝑛 together with 𝑛 identifies each of the objects (d)–(g),
as well as the objects (a)–(c). Therefore, by transitivity (which is easy to check)
all the objects (d)–(g) are equivalent.
Let us prove now that (a)–(c) are equivalent to each other and equivalent to
(d)–(g). Given the list of strings of complexity at most 𝑛 we can find the number of
them (so (a)→(b)) and the largest number of complexity at most 𝑛 (so (a)→(c)).
It is not that easy to find (a) given (b) and 𝑛. Given 𝑛 and the number of strings
of complexity at most 𝑛 we can reconstruct the list of these strings (generating them
until we obtain the desired number of strings), and find a maximal number among
them ((b)→(c)). But we still do not know Kolmogorov complexity of the generated
strings. We will prove the implication (c)→(a) indirectly, by showing (c)→(d);
we know already that (d) implies (a). This will prove that all objects (a)–(g) are
equivalent.
The implication (c)→(d) follows from Theorem 14. We know that B (𝑛) is an
upper bound for BB (𝑛 − 𝑐) (for appropriate 𝑐). Thus, given 𝑛 and B (𝑛), we can
find BB (𝑛 − 𝑐) as follows: run 𝐷 on all inputs of length at most 𝑛 − 𝑐 within B (𝑛)
steps. Then find BB (𝑛 − 𝑐) as the number of steps in the longest run.
It remains to consider the objects (h) and (i). The implication (a)→(h) is easy.
Indeed, for some constant 𝑐 the complexity of every string of length 𝑛 − 𝑐 does not
exceed 𝑛. If we know the list (a) and 𝑛, then removing all the strings of length
different from 𝑛 − 𝑐 from the list, we get (h) for 𝑛 − 𝑐.
The conversion (h)→(i) is straightforward.
Thus it remains to prove (i)→(a). It is enough to show that given the lex-
icographically first string 𝛾𝑛 of length 𝑛 and complexity at least 𝑛 we can find
BB (𝑛 − 𝑂(1)) or a number greater than BB (𝑛 − 𝑂(1)). This can be done as
follows.
Given 𝛾𝑛 find 𝑛 and for each string 𝑥 of length 𝑛 preceding 𝛾𝑛 in the lexicograph-
ical order find a description 𝑝𝑥 of 𝑥 that has length 𝑛 or less, and find out the running
time 𝑡𝑥 of 𝐷 on 𝑝𝑥. (Note that 𝑝𝑥 may be not the shortest description of 𝑥.) Let 𝑇
be the maximum of 𝑡𝑥 for those 𝑥. We claim that 𝑇 > BB (𝑛 − 𝑐) for some 𝑐 that
does not depend on 𝑛. Assume that this inequality is false, that is, 𝑇 6 BB (𝑛 − 𝑐).
We will prove that then 𝑐 is small. Consider the most time-consuming description
𝛼𝑛−𝑐 of length at most 𝑛 − 𝑐; let 𝑛 − 𝑐 − 𝑑 be its length. Given 𝛼𝑛−𝑐 and 𝑐 + 𝑑 we
can find 𝑛 and BB (𝑛 − 𝑐). From this we can find 𝛾𝑛: run 𝐷 on all strings of length
at most 𝑛 within BB (𝑛 − 𝑐) steps. Consider all the strings of length 𝑛 for which
we have found descriptions of length 𝑛 or less. Then 𝛾𝑛 is the lexicographically
first remaining string (since 𝑇 6 BB (𝑛 − 𝑐) according to our assumption). As the
complexity of 𝛾𝑛 is at least 𝑛 we have 𝑛 6 𝐶(𝛾𝑛) 6 (𝑛 − 𝑐 − 𝑑) + 2 log(𝑐 + 𝑑) + 𝑂(1),
hence (𝑐 + 𝑑) = 𝑂(1).
We have thus proven the equivalence of objects (a)–(h). It remains to prove
that complexity of each of them is 𝑛 + 𝑂(1).
Let 𝑋𝑛 be one of objects (a)–(h). We have just proven that 𝑋𝑛 can be obtained
from 𝛾𝑛+𝑐 and 𝑛 (actually, we do not need 𝑛, as 𝑛 = 𝑙(𝛾𝑛+𝑐) − 𝑐). Therefore,
𝐶(𝑋𝑛) 6 𝐶(𝛾𝑛+𝑐) + 𝑂(1) 6 𝑛 + 𝑂(1).

1.2. ALGORITHMIC PROPERTIES 41
To prove the lower bound of 𝐶(𝑋𝑛) let 𝑛 − 𝑑 be the complexity of 𝑋𝑛. For
some constant 𝑐 the string 𝛾𝑛−𝑐 can be obtained from the shortest description of
𝑋𝑛 of length 𝑛 − 𝑑 and from 𝑑 (note that 𝑛 can be retrieved from the length of
the shortest description and 𝑑). Thus, 𝑛 − 𝑐 6 𝐶(𝛾𝑛−𝑐) 6 (𝑛 − 𝑑) + 2 log 𝑑 + 𝑂(1).
Therefore 𝑑 6 2 log 𝑑 + 𝑐 + 𝑂(1) and hence 𝑑 = 𝑂(1). 
8 The objects in Theorem 15 depend on the choice of the optimal decompres-
sor. In the proof we assumed that the same optimal decompressor is used in all the
items (a)–(h). Prove that the statement of the theorem remains true if different
decompressors are used.
9 Prove that the complexity of all the objects in Theorem 15 becomes 𝑂(log 𝑛)
if we relativize the definition of Kolmogorov complexity by 0′, that is, if we allow
the decompressor to query the oracle for the halting problem.
We have seen that there exist a constant 𝑐 and an algorithm 𝐴 that given the
string 𝛾𝑛 solves the halting problem for the optimal decompressor on inputs of
length at most 𝑛 − 𝑐. This means that given an “oracle” that finds 𝛾𝑛 for every
given 𝑛 we can solve the halting problem. The same can be done given an oracle
deciding whether a given string 𝑥 is “incompressible”, that is, 𝐶(𝑥) > 𝑙(𝑥). Indeed,
using that oracle we can find 𝛾𝑛 by probing all strings of length 𝑛.
Using the terminology of computability theory, we can say that halting problem
is Turing reducible to the set of incompressible strings (or its complement, the set
of compressible strings). This implies that halting problem is also reducible to the
“upper graph” of 𝐶, that is, to the set {⟨𝑥, 𝑘⟩ | 𝐶(𝑥) < 𝑘}. Using the terminology
of computability theory, we say that the set of compressible strings (as well as the
upper graph of 𝐶) is Turing complete in the class of enumerable sets (this means
that it is enumerable and that the halting problem is Turing reducible to it).
10 Find some upper bound for the number of oracle queries for the set
{⟨𝑥, 𝑘⟩ | 𝐶(𝑥) < 𝑘}
needed to solve the halting problem for a fixed machine 𝑀 and for all strings of
length at most 𝑛.
11 Let 𝑓 be a computable partial function from N to N. Prove that there
is a constant 𝑐 such that for all 𝑛 such that 𝑓 (B (𝑛)) is defined the inequality
B (𝑛 + 𝑐) > 𝑓 (B (𝑛)) is true. [Hint: the complexity of 𝑓 (B (𝑛)) is at most 𝑛 + 𝑂(1).]
12 Call a set 𝑈 𝑟-separable [136] if every enumerable set 𝑉 disjoint with 𝑈
can be separated from 𝑈 by a decidable set, that is, there is a decidable set 𝑅 that
includes 𝑉 and is disjoint with 𝑈 .
(a) Prove that the the set {⟨𝑥, 𝑘⟩ | 𝐶(𝑥) < 𝑘} (the upper graph of 𝐶) is an
𝑟-separable set. The set of compressible strings is 𝑟-separable, too. [Hint: assume
that the upper graph of 𝐶 is disjoint with some enumerable set 𝑉 . The set of
the second components of pairs in 𝑉 is finite, otherwise we get an unbounded
computable lower bound for 𝐶. That is, 𝑉 is included in a horizontal strip of finite
height. The intersection of the strip with the upper graph is finite.]
(b) We say that a set 𝑈1 is 𝑚-reducible to a set 𝑈2 if there is a total computable
function 𝑓 such that 𝑈1 = 𝑓 −1(𝑈2). Prove that if 𝑈2 is 𝑟-separable and 𝑈1 is 𝑚-
reducible to 𝑈2 then 𝑈1 is 𝑟-separable as well. [Hint. If 𝑉 is an enumerable set
disjoint with 𝑈1 then 𝑓 (𝑉 ) is an enumerable set disjoint with 𝑈2. If 𝑅 is a decidable
set separating 𝑓 (𝑉 ) and 𝑈2 then 𝑓 −1(𝑅) is a decidable set separating 𝑉 and 𝑈1.]

42 1. PLAIN KOLMOGOROV COMPLEXITY
(c) Prove that there is an enumerable set that is not 𝑟-separable (such set does
not 𝑚-reduce to the upper graph of 𝐶). [Hint: there is a pair of disjoint enumerable
inseparable sets.]
13 Following [73], prove that the problems “for a given integer 𝑛 find some
string of complexity at least 𝑛” and “for a given algorithm without input find some
string that is different from its output” (if the algorithm does not terminate, any
string is OK) are equivalent: an oracle that fulfills one of the tasks can be used to
(effectively) fulfill the other. [Hint: given an algorithm, we can provide an upper
bound for the complexity of its output: it is bounded by complexity (and therefore
the length) of the algorithm itself. On the other hand, to provide a string of high
complexity means to provide a string which is guaranteed to be different from the
outputs of finitely many algorithms. At first, this looks like a more difficult task
than for one algorithm (as the oracle does). However, the following trick helps: we
may assume that the outputs are tuples and construct a tuple that differs from the
output of 𝑖-th algorithm in 𝑖-th position.]
14 (Continued.) Prove that both these problems are equivalent to the problem
of computing a fixed-point free function: “for every algorithm construct another
algorithm that computes a different function” (not the same as the first one).
15 (Continued.) Prove that an enumerable oracle can solve these problems if
and only if it solves the halting problem (M. Arslanov proved this result without
using Kolmogorov complexity). [Hint: Assume that an enumerable oracle 𝐴 allows
us to compute strings of arbitrarily high complexity. Then let us compute a string
of complexity at least 𝑛 using this oracle, and look at all elements of 𝐴 that were
questioned during this computation. How many steps are needed to enumerate all
this elements? This is a big number: any 𝑇 greater than this number, has the
Kolmogorov complexity at least 𝑛, since 𝑇 -approximation of 𝐴 can be used instead
of 𝐴. On the other hand, having an oracle for 𝐴, we can find 𝑇 for a given 𝑛.]
Kolmogorov complexity and functions 𝐵 and BB turn out to be useful to study
the the so-called “generic” and “coarse” algorithms that solve the halting problem
for most inputs (the fraction of errors converges to zero), see [11]. The versions
of these functions based on prefix complexity were introduced by G´acs [57], see
also [4] for recent results related to the busy beaver functions for different versions
of Kolmogorov complexity.
We have shown only several (simple) example that show how Kolmogorov com-
plexity is related to computability theory (also called “recursion theory”). This area
now actively grows, so we refer the interested reader to two recent monographs [146]
(by A. Nies) and [49] (by R. Downey and D. Hirschfeldt).
Theorem 15 selects some very special objects among all objects of complexity 𝑛
(in fact, one object up to equivalence described above). At first glance, this seems
strange: our intuition says that all “random” (incompressible) strings of length 𝑛
should be indistinguishable, and any special property of a string could be used to
compress it. However, we have found a very special random string 𝛾𝑛 of length 𝑛.
This paradox can be explained as follows: the individual properties of 𝛾𝑛 does allow
us to find a short description for 𝛾𝑛, but we need the oracle for 0′ to decompress
that description.
We will come back to this question in Section 5.7 discussing “the number of
wisdom” Ω and in Section 14.3 studying two-part descriptions.

1.2. ALGORITHMIC PROPERTIES 43
Finally, let us note that although all the objects in Theorem 15 are equivalent,
they have very different lengths. The lengths of (a), (b), (e)–(i) is about 𝑛 while
the length of (c) and (d) grows faster than every computable function of 𝑛.

CHAPTER 2
Complexity of pairs and conditional complexity

---

Full document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md) · Page-level evidence: [paper-pages/26-kolmogorov-complexity-and-algorithmic-randomness](../../paper-pages/26-kolmogorov-complexity-and-algorithmic-randomness/index.md)
