---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
section: 2.1. Complexity of pairs
section_role: other
section_index: 4
pages: [44, 45, 46, 47]
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "As we have discussed, we can define complexity of any constructive object using (computable) encodings by strings. In this section we deal with pairs…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.1. Complexity of pairs

> Section 4 of 11 from [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md) · `other` · pages 44-47

As we have discussed, we can define complexity of any constructive object using
(computable) encodings by strings. In this section we deal with pairs of strings.
A pair 𝑥, 𝑦 can be encoded, e.g., by a string [𝑥, 𝑦] = 𝑥01𝑦; here 𝑥 stands for 𝑥
with doubled bits. Any other computable encoding 𝑥, 𝑦 ↦ → [𝑥, 𝑦] could be used (of
course, we need that [𝑥, 𝑦]̸ = [𝑥′, 𝑦′] if 𝑥̸ = 𝑥′ or 𝑦̸ = 𝑦′). Any two encodings of
this type are equivalent (there are translation algorithms in both directions), so
Theorem 3 (p. 15) guarantees that complexities of the different encodings of the
same pair differ by 𝑂(1).
So let us fix some encoding [𝑥, 𝑦]. Kolmogorov complexity of a pair 𝑥, 𝑦 is
defined as 𝐶([𝑥, 𝑦]) and denoted by 𝐶(𝑥, 𝑦). Here are some evident properties:
∙ 𝐶(𝑥, 𝑥) = 𝐶(𝑥) + 𝑂(1);
∙ 𝐶(𝑥, 𝑦) = 𝐶(𝑦, 𝑥) + 𝑂(1);
∙ 𝐶(𝑥) 6 𝐶(𝑥, 𝑦) + 𝑂(1); 𝐶(𝑦) 6 𝐶(𝑥, 𝑦) + 𝑂(1).
The following theorem gives an upper bound for the complexity of a pair in
terms of complexities of its components:
Theorem 16.
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 2 log 𝐶(𝑥) + 𝐶(𝑦) + 𝑂(1);
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + log 𝐶(𝑥) + 2 log log 𝐶(𝑥) + 𝐶(𝑦) + 𝑂(1);
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + log 𝐶(𝑥) + log log 𝐶(𝑥) + 2 log log log 𝐶(𝑥) + 𝐶(𝑦) + 𝑂(1);
. . .
(We can continue this sequence of inequalities indefinitely. Also, one can ex-
change 𝑥 and 𝑦.)
Proof. This proof (for the first inequality) was already explained in the In-
troduction (Theorem 4, p. 16). The only difference is that we considered the con-
catenation 𝑥𝑦 instead of a pair. Let us repeat the argument for pairs.
A computable mapping 𝑥 ↦ → ˆ𝑥 (here 𝑥 and ˆ𝑥 are binary strings) is called a
prefix-free encoding, if for any two different strings 𝑥 and 𝑦 the string ˆ𝑥 is not a
prefix of the string ˆ𝑦. (In particular, ˆ𝑥̸ = ˆ𝑦 if 𝑥̸ = 𝑦.) This guarantees that both 𝑢
and 𝑣 can be uniquely reconstructed from ˆ𝑢𝑣.
An example of a prefix-free encoding: 𝑥 ↦ → 𝑥01, where 𝑥 stands for 𝑥 with
doubled bits. Here the block 01 are used as a delimiter. However, this encoding is
not the most space-efficient one, since it doubles the length. A better prefix-free
encoding:
𝑥 ↦ → ˆ𝑥 = bin(𝑙(𝑥)) 01𝑥
45

46 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
(bin(𝑙(𝑥)) is the binary representation of the length 𝑙(𝑥) of the string 𝑥). Now
𝑙(ˆ𝑥) = 𝑙(𝑥) + 2 log 𝑙(𝑥) + 𝑂(1).
This trick can be “iterated”: for any prefix-free encoding 𝑥 ↦ → ˆ𝑥 we can construct
another prefix-free encoding
𝑥 ↦ →	̂	 bin(𝑙(𝑥))𝑥.
Indeed, if	̂	 bin(𝑙(𝑥))𝑥 is a prefix of	̂	 bin(𝑙(𝑦))𝑦, then one of the strings	̂	 bin(𝑙(𝑥)) and
̂	
bin(𝑙(𝑦)) is a prefix of the other one, and therefore bin(𝑙(𝑥)) = bin(𝑙(𝑦)). Therefore
𝑥 is a prefix of 𝑦, and 𝑙(𝑥) = 𝑙(𝑦), so 𝑥 = 𝑦. (In other terms, we uniquely determine
the length of the string, since a prefix-free code is used for it, and then get the
string itself knowing where it ends.)
In this way we get a prefix-free encoding such that
𝑙(ˆ𝑥) = 𝑙(𝑥) + log 𝑙(𝑥) + 2 log log 𝑙(𝑥) + 𝑂(1),
then (one more iteration)
𝑙(ˆ𝑥) = 𝑙(𝑥) + log 𝑙(𝑥) + log log 𝑙(𝑥) + 2 log log log 𝑙(𝑥) + 𝑂(1),
etc.
Now we return to the proof. Let 𝐷 be the optimal decompressor used in
the definition of Kolmogorov complexity. Consider a decompressor 𝐷′ defined as
follows:
𝐷′(ˆ𝑝𝑞) = [𝐷(𝑝), 𝐷(𝑞)],
where ˆ𝑝 is a prefix-free encoding and [·, ·] is the encoding of pairs (used in the
definition of pairs complexity). Since ˆ𝑝 is a prefix-free encoding, 𝐷′ is well defined
(we can uniquely extract ˆ𝑝 out of ˆ𝑝𝑞).
Let 𝑝 and 𝑞 be the shortest descriptions of 𝑥 and 𝑦. Then ˆ𝑝𝑞 is a description
of [𝑥, 𝑦], and its length is exactly as we need in our theorem. (The more iterations
we use for the prefix-free encoding, the better bound we get.) 
Theorem 16 implies that
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 𝐶(𝑦) + 𝑂(log 𝑛)
for strings 𝑥 and 𝑦 of length at most 𝑛: one may say that the complexity of a
pair does not exceed the sum of the complexities of its component with logarithmic
precision.
16 Suggest a natural definition for the complexity of a triple. Show that
𝐶(𝑥, 𝑦, 𝑧) 6 𝐶(𝑥) + 𝐶(𝑦) + 𝐶(𝑧) + 𝑂(log 𝑛) for every three strings 𝑥, 𝑦, 𝑧 of length
at most 𝑛.
A natural question arises: is it true that 𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 𝐶(𝑦) + 𝑂(1)?
A simple argument shows that this is not the case. Indeed, this inequality would
imply 𝐶(𝑥, 𝑦) 6 𝑙(𝑥) + 𝑙(𝑦) + 𝑂(1). Consider some 𝑁 . For each 𝑛 = 0, 1, 2, . . . , 𝑁
we have 2𝑛 strings 𝑥 of length 𝑛 and 2𝑁 −𝑛 strings 𝑦 of length 𝑁 − 𝑛. Combining
them, we (for a given 𝑛) obtain 2𝑁 different pairs ⟨𝑥, 𝑦⟩. The total number of pairs
(all 𝑛 = 0, 1, . . . , 𝑁 give different pairs) is (𝑁 + 1)2𝑁 .
Assume that indeed 𝐾(𝑥, 𝑦) 6 𝑙(𝑥) + 𝑙(𝑦) + 𝑂(1) = 𝑁 + 𝑂(1) for all these pairs.
Then we get (𝑁 + 1)2𝑁 different strings [𝑥, 𝑦] of complexity at most 𝑁 + 𝑂(1), but
this is impossible (Theorem 7, p. 31, gives the upper bound 𝑂(2𝑁 )).

2.1. COMPLEXITY OF PAIRS 47
17 Prove that there is no constant 𝑐 such that
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + log 𝐶(𝑥) + 𝐶(𝑦) + 𝑐
for all 𝑥 and 𝑦. [Hint: Replace 𝐶 in the right hand side by 𝑙 and count the number
of corresponding pairs.]
18 (a) Prove that∑︁
𝑥∈Ξ
2−𝑙(^𝑥) 6 1
for any prefix-free encoding 𝑥 ↦ → ˆ𝑥 (here Ξ is the set of all binary strings).
(b) Prove that if a prefix-free encoding increases the length of a 𝑛-bit string at
most by 𝑓 (𝑛), i.e., if 𝑙(ˆ𝑥) 6 𝑙(𝑥) + 𝑓 (𝑙(𝑥)), then∑︀ 𝑛 2−𝑓 (𝑛) < ∞.
This problem explains why a coefficient 2 appears in the Theorem 16 (p. 45):
the series∑︁ 1
𝑛2 ,∑︁ 1
𝑛(log 𝑛)2 ,∑︁ 1
𝑛 log 𝑛(log log 𝑛)2 , . . .
converge, while the series∑︁	
1
𝑛 ,∑︁ 1
𝑛 log 𝑛 ,∑︁ 1
𝑛 log 𝑛 log log 𝑛 , . . .
diverge.
The following problem describes functions that can be used for bounds similar
to Theorem 16.
19 Let 𝑓 : N → N is a non-decreasing total computable function. Prove that
the following three properties are equivalent:
(a) 𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 𝐶(𝑦) + 𝑓 (𝐶(𝑥)) + 𝑂(1);
(b) 𝐶(𝑥, 𝑦) 6 𝑙(𝑥) + 𝑙(𝑦) + 𝑓 (𝑙(𝑥)) + 𝑂(1);
(c)∑︀ 𝑛 2−𝑓 (𝑛) < ∞. [Hint: (a) obviously implies (b); to get the reverse implica-
tion, consider the shortest descriptions. To derive (a) from (c), one can count pairs
with 𝑙(𝑥) + 𝑓 (𝑙(𝑥)) + 𝑙(𝑦) < 𝑛; one can also use results about prefix complexity (see
Chapter 4, Problem 107). Finally, to derive (c) from (b), note that the right hand
side in (b) is at most 𝑛 + 𝑂(1) if 𝑙(𝑥) = 𝑘 and 𝑙(𝑦) = 𝑛 − 𝑘 − 𝑓 (𝑘), for 𝑘 + 𝑓 (𝑘) 6 𝑛.
So the number of such pairs is at least∑︀ 2𝑘2𝑛−𝑘−𝑓 (𝑘) = 2𝑛∑︀ 𝑘 2−𝑓 (𝑘) where the
sum is taken over all 𝑘 such that 𝑘 + 𝑓 (𝑘) 6 𝑛. ]
20 Prove that all the inequalities of Theorem 16 become false if the coefficient
2 is replaced by 1, but remain true with the coefficient 1 + 𝜀 for any 𝜀 > 0. [Hint:
see the preceding problem.]
21 Prove that
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + log 𝐶(𝑥) + 𝐶(𝑦) + log 𝐶(𝑦) + 𝑂(1).
22 (Continued) Prove a stronger inequality:
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 𝐶(𝑦) + log(𝐶(𝑥) + 𝐶(𝑦)) + 𝑂(1).
(note that 𝐶(𝑥) + 𝐶(𝑦) can be replaced by max(𝐶(𝑥), 𝐶(𝑦)), this gives a factor at
most 2, which makes 𝑂(1) after taking logarithms).
23 Prove that 𝐶(𝑥, 𝐶(𝑥)) = 𝐶(𝑥) + 𝑂(1). [Hint: 𝐶(𝑥, 𝐶(𝑥)) > 𝐶(𝑥) + 𝑂(1)
for evident reasons; on the other hand, the shortest description of 𝑥 determines
both 𝑥 and 𝐶(𝑥).]
24 Prove that if 𝐶(𝑥) 6 𝑛 and 𝐶(𝑦) 6 𝑛, then 𝐶(𝑥, 𝑦) 6 2𝑛 + 𝑂(1).

48 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY

---

Full document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md) · Page-level evidence: [paper-pages/26-kolmogorov-complexity-and-algorithmic-randomness](../../paper-pages/26-kolmogorov-complexity-and-algorithmic-randomness/index.md)
