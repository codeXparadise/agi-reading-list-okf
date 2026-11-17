---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 15
pages: [15]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "16 WHAT IS THIS BOOK ABOUT? This theorem implies that the amount of information “does not depend on the specific encoding”. For instance, if we…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 15 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 15 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

16 WHAT IS THIS BOOK ABOUT?
This theorem implies that the amount of information “does not depend on the
specific encoding”. For instance, if we reverse all bits of some string (replace 0
by 1 and vice versa), or add a zero bit after each bit of that string, the resulting
string has the same Kolmogorov complexity as the original one (up to an additive
constant). Indeed, the transformation itself and its inverse can be performed by an
algorithm.
Here is one more example of a natural property of Kolmogorov complexity. Let
𝑥 and 𝑦 be strings. How much information has their concatenation 𝑥𝑦? We expect
that the quantity of information in 𝑥𝑦 does not exceed the sum of those in 𝑥 and 𝑦.
This is indeed true, however, a small additive term is needed.
Theorem 4. There is a constant 𝑐 such that for all 𝑥 and 𝑦
𝐶(𝑥𝑦) 6 𝐶(𝑥) + 2 log 𝐶(𝑥) + 𝐶(𝑦) + 𝑐
Proof. Let us try first to prove the statement in a stronger form, without
the term 2 log 𝐶(𝑥). Let 𝐷 be the optimal description mode that is used in the
definition of Kolmogorov complexity. Define the following description mode 𝐷′.
If 𝐷(𝑝) = 𝑥 and 𝐷(𝑞) = 𝑦 we consider 𝑝𝑞 as a description of 𝑥𝑦, that is, we let
𝐷′(𝑝𝑞) = 𝑥𝑦. Then the complexity of 𝑥𝑦 with respect to 𝐷′ does not exceed the
length of 𝑝𝑞, that is, 𝑙(𝑝) + 𝑙(𝑞). If 𝑝 and 𝑞 are minimal descriptions, we obtain
𝐶𝐷′ (𝑥𝑦) 6 𝐶𝐷 (𝑥) + 𝐶𝐷 (𝑦). By optimality the same inequality holds for 𝐷 in place
of 𝐷′, up to an additive constant.
What is wrong with this argument? The problem is that 𝐷′ is not well defined.
We let 𝐷′(𝑝𝑞) = 𝐷(𝑝)𝐷(𝑞). However, 𝐷′ has no means to separate 𝑝 from 𝑞. It may
happen that there are two ways to split the input into 𝑝 and 𝑞 yielding different
results:
𝑝1𝑞1 = 𝑝2𝑞2 but 𝐷(𝑝1)𝐷(𝑞1)̸ = 𝐷(𝑝2)𝐷(𝑞2).
There are two ways to fix this bug. The first one, which we use now, goes
as follows. Let us prepend the string 𝑝𝑞 by the length 𝑙(𝑝) of string 𝑝 (in binary
notation). This allows us to separate 𝑝 and 𝑞. However, we need to find where
𝑙(𝑝) ends, so let us double all the bits in the binary representation of 𝑙(𝑝) and then
put 01 as separator. More specifically, let bin(𝑘) denote the binary representation
of integer 𝑘 and let 𝑥 be the result of doubling each bit in 𝑥. (For example,
bin(5) = 101, and bin(5) = 110011.) Let
𝐷′( bin(𝑙(𝑝)) 01𝑝𝑞) = 𝐷(𝑝)𝐷(𝑞).
Thus 𝐷′ is well defined: the algorithm 𝐷′ scans bin(𝑙(𝑝)) while all the digits are
doubled. Once it sees 01, it determines 𝑙(𝑝) and then scans 𝑙(𝑝) digits to find 𝑝.
The rest of the input is 𝑞 and the algorithm is able to compute 𝐷(𝑝)𝐷(𝑞).
Now we see that 𝐶𝐷′ (𝑥𝑦) is at most 2𝑙(bin(𝑙(𝑝))) + 2 + 𝑙(𝑝) + 𝑙(𝑞). The length
of the binary representation of 𝑙(𝑝) is at most log2 𝑙(𝑝) + 1. Therefore, 𝑥𝑦 has a
description of length at most 2 log2 𝑙(𝑝) + 4 + 𝑙(𝑝) + 𝑙(𝑞) with respect to 𝐷′, which
implies the statement of the theorem. 
The second way to fix the bug mentioned above goes as follows. We could
modify the definition of Kolmogorov complexity by requiring descriptions to be
“self-delimiting”; we discuss this approach in detail in Chapter 4.

---

[previous page](page-014.md) · [next page](page-016.md) · [all pages](index.md)
