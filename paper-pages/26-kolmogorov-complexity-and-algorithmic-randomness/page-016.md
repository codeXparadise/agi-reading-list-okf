---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 16
pages: [16]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "COMPLEXITY AND INFORMATION 17 Note also that we can exchange 𝑝 and 𝑞 and thus prove that 𝐶(𝑥𝑦) 6 𝐶(𝑥) + 𝐶(𝑦) + 2 log2 𝐶(𝑦) + 𝑐. How tight is the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 16 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 16 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

COMPLEXITY AND INFORMATION 17
Note also that we can exchange 𝑝 and 𝑞 and thus prove that
𝐶(𝑥𝑦) 6 𝐶(𝑥) + 𝐶(𝑦) + 2 log2 𝐶(𝑦) + 𝑐.
How tight is the inequality of Theorem 4? Can 𝐶(𝑥𝑦) be much less than
𝐶(𝑥) + 𝐶(𝑦)? According to our intuition, this happens when 𝑥 and 𝑦 have much in
common. For example, if 𝑥 = 𝑦, we have 𝐶(𝑥𝑦) = 𝐶(𝑥𝑥) = 𝐶(𝑥) + 𝑂(1), since 𝑥𝑥
can be algorithmically obtained from 𝑥 and vice versa (Theorem 3).
To refine this observation we will define the notion of the quantity of information
in 𝑥 that is missing in 𝑦 (for every strings 𝑥 and 𝑦). This value is called the the
Kolmogorov complexity of 𝑥 conditional to 𝑦 (or “given 𝑦”) and denoted by 𝐶(𝑥 | 𝑦).
Its definition is similar to the definition of the unconditional complexity. This time
the decompressor 𝐷 has access not only to the (compressed) description, but also
to the string 𝑦. We will discuss this notion later in Section 2. Here we mention
only that the following equality holds:
𝐶(𝑥𝑦) = 𝐶(𝑦) + 𝐶(𝑥 | 𝑦) + 𝑂(log 𝑛)
for all strings 𝑥 and 𝑦 of complexity at most 𝑛. The equality reads as follows: the
amount of information in 𝑥𝑦 is equal to the amount of information in 𝑦 plus the
amount of new information in 𝑥 (“new” = missing in 𝑦).
The difference 𝐶(𝑥)−𝐶(𝑥 | 𝑦) can be considered as “the quantity of information
in 𝑦 about 𝑥”. It indicates how much the knowledge of 𝑦 simplifies 𝑥.
Using the notion of conditional complexity we can ask questions like this: How
much new information has DNA of some organism compared to another organism’s
DNA? If 𝑑1 is the binary string that encodes the first DNA and 𝑑2 is the binary
string that encodes the second DNA, then the value in question is 𝐶(𝑑1 | 𝑑2). Sim-
ilarly we can ask what percentage of information has been lost when translating a
novel into another language: this percentage is the fraction
𝐶(original | translation)/𝐶(original).
The questions about information in different objects were studied before the
invention of algorithmic information theory. The information was measured using
the notion of Shannon entropy. Let us recall its definition. Let 𝜉 be a random
variable that takes 𝑛 values with probabilities 𝑝1, . . . , 𝑝𝑛. Then its Shannon entropy
𝐻(𝜉) is defined as follows:
𝐻(𝜉) =∑︁ 𝑝𝑖(− log2 𝑝𝑖).
Informally, the outcome having probability 𝑝𝑖 carries log(1/𝑝𝑖) = − log2 𝑝𝑖 bits of
information (=surprise). Then 𝐻(𝜉) can be understood as the average amount of
information in an outcome of the random variable.
Assume that we want to use Shannon entropy to measure the amount of infor-
mation contained in some English text. To do this we have to find an ensemble of
texts and a probability distribution on this ensemble such that the text is “typical”
with respect to this distribution. This makes sense for a short telegram, but for a
long text (say, a novel) such an ensemble is hard to imagine.
The same difficulty arises when we try to define the amount of information in
the genome of some species. If we consider as the ensemble the set of the genomes
of all existing species (or even all species ever existed), then the cardinality of this
set is rather small (it does not exceed 21000 for sure). And if we consider all its

---

[previous page](page-015.md) · [next page](page-017.md) · [all pages](index.md)
