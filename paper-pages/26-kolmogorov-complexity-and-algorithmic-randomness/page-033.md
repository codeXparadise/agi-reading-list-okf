---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 33
pages: [33]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "34 1. PLAIN KOLMOGOROV COMPLEXITY Then 𝑘(𝑥) = 𝐶(𝑥) + 𝑂(1), that is, the difference |𝑘(𝑥) − 𝐶(𝑥)| is bounded by a constant. Proof. Theorem 8 implies…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 33 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 33 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

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

---

[previous page](page-032.md) · [next page](page-034.md) · [all pages](index.md)
