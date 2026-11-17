---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 75
pages: [75]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "76 3. MARTIN-L ¨OF RANDOMNESS programs, and 𝑞th term of this sequence is called “𝑞th program” in the rest of the proof. Then we define 𝑋(𝑞, 𝜀, 𝑖) as…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 75 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 75 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

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

---

[previous page](page-074.md) · [next page](page-076.md) · [all pages](index.md)
