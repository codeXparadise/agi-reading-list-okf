---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 74
pages: [74]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "3.3. EFFECTIVELY NULL SETS 75 75 Prove that 𝑒 (the base of natural logarithms) and 𝜋 are computable. 76 Prove that elementary function (roots, sine,…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 74 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 74 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

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

---

[previous page](page-073.md) · [next page](page-075.md) · [all pages](index.md)
