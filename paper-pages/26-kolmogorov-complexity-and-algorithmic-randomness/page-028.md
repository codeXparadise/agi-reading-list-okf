---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 28
pages: [28]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "CHAPTER 1 Plain Kolmogorov complexity 1.1. The definition and main properties Let us recall the definition of Kolmogorov complexity from the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 28 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 28 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

CHAPTER 1
Plain Kolmogorov complexity
### 1.1. The definition and main properties
Let us recall the definition of Kolmogorov complexity from the Introduction.
This version of complexity was defined by Kolmogorov in his seminal paper [77].
In order to distinguish it from later versions we call it the plain Kolmogorov com-
plexity. Later, starting from Chapter 4, we will consider also other versions of
Kolmogorov complexity, including the prefix one and the monotone one, but for
now by Kolmogorov complexity we always mean the plain one.
Recall that a description mode, or a decompressor , is a partial computable
function 𝐷 from the set of all binary strings Ξ into Ξ. A partial function 𝐷 is
computable if there is an algorithm that terminates and returns 𝐷(𝑥) on every
input 𝑥 in the domain of 𝐷 and does not terminate on all other inputs. We say
that 𝑦 is a description of 𝑥 with respect to 𝐷 if 𝐷(𝑦) = 𝑥.
The complexity of a string 𝑥 with respect to description mode 𝐷 is defined as
𝐶𝐷 (𝑥) = min{𝑙(𝑦) | 𝐷(𝑦) = 𝑥}.
The minimum of the empty set is +∞.
We say that a description mode 𝐷1 is not worse than a description mode 𝐷2
if there is a constant 𝑐 such that 𝐶𝐷1 (𝑥) 6 𝐶𝐷2 (𝑥) + 𝑐 for all 𝑥 and write this as
𝐶𝐷1 (𝑥) 6 𝐶𝐷2 (𝑥) + 𝑂(1).
A description mode is called optimal if it is not worse than any other description
mode. By Kolmogorov–Solomonoff universality theorem (Theorem 1, p. 13) optimal
description modes exist. Let us recall shortly its proof. Let 𝑈 be an interpreter of
a universal programming language, that is, 𝑈 (𝑝, 𝑥) is the output of the program 𝑝
on input 𝑥. We assume that programs and inputs are binary strings. Let
𝐷(ˆ𝑝𝑥) = 𝑈 (𝑝, 𝑥).
Here 𝑝 ↦ → ˆ𝑝 stands for any computable mapping having the following property:
given ˆ𝑝 we can effectively find 𝑝 and also the place where ˆ𝑝 ends (in particular, if ˆ𝑝
is a prefix of ˆ𝑞, then 𝑝 = 𝑞). This property implies that 𝐷 is well defined. For any
description mode 𝐷′ let 𝑝 be a program of 𝐷′. Then
𝐶𝐷′ (𝑥) 6 𝐶𝐷 (𝑥) + 𝑙(ˆ𝑝).
Indeed, for every description 𝑦 of 𝑥 with respect to 𝐷′ the string ˆ𝑝𝑦 is a description
of 𝑥 with respect to 𝐷.
Fix any optimal description mode 𝐷 and let 𝐶(𝑥) (we drop the subscript)
denote the complexity of 𝑥 with respect to 𝐷. (As we mentioned, in the first paper
of Kolmogorov [77] the letter 𝐾 was used, while in his second paper [78] the letter
𝐻 was used. We follow here the notation used by Li and Vit´anyi [102].)
29

---

[previous page](page-027.md) · [next page](page-029.md) · [all pages](index.md)
