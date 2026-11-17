---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 60
pages: [60]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "2.3. COMPLEXITY AS THE AMOUNT OF INFORMATION 61 The proof of this relativized inequality repeats the proof of the unrelativized one: we combine…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 60 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 60 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

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

---

[previous page](page-059.md) · [next page](page-061.md) · [all pages](index.md)
