---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 26
pages: [26]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "BASIC NOTIONS AND NOTATIONS 27 identify such sequences with probability distributions on the set N⊥, which consists of natural numbers and of the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 26 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 26 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

BASIC NOTIONS AND NOTATIONS 27
identify such sequences with probability distributions on the set N⊥, which consists
of natural numbers and of the special symbol ⊥ (“undefined value”).
Among all semimeasures (on the tree or on natural numbers) we distinguish
lower semicomputable ones. Both the class of lower semicomputable semimeasures
on the tree and the class of lower semicomputable semimeasures on natural numbers
have a maximal semimeasure (up to a multiplicative constant). Any maximal lower
semicomputable semimeasure is called a priori probability (on the tree or on natural
numbers). A priori probability of a natural number 𝑛 is denoted by 𝑚(𝑛); a priori
probability of a node 𝑥 in the binary tree (that is, of the string 𝑥) is denoted by
𝑎(𝑥). We use also the notation 𝑚(𝑥) for a binary string 𝑥, which means a priory
probability of the number of 𝑥 with respect to some fixed computable one-to-one
correspondence between strings and natural numbers.
The plain Kolmogorov complexity is denoted by 𝐶(𝑥), the prefix Kolmogorov
complexity is denoted by 𝐾(𝑥) (and by 𝐾′(𝑥) when we want to stress that we are
using prefix-free description modes). The same letters are used to denote complexi-
ties of pairs, triples etc. and to denote conditional complexity. For instance, 𝐶(𝑥 | 𝑦)
stands for the plain conditional complexity of 𝑥 when 𝑦 is known, and 𝑚(𝑥, 𝑦 | 𝑧)
denotes a priori probability of the pair (𝑥, 𝑦) (that is, of the corresponding num-
ber) when 𝑧 is known. The monotone Kolmogorov complexity is denoted by KM ,
a priori complexity (negative logarithm of the a priory probability on the tree)
is denoted by KA . (In the literature monotone complexity is sometimes denoted
by Km and 𝐾𝑚 and a priori complexity is denoted by KM.) Finally the decision
complexity is denoted by KR .
BB (𝑛) denotes the maximal halting time of the optimal decompressor on inputs
of length at most 𝑛 (if the optimal prefix decompressor is meant, then we use the
notation BP (𝑛)). The function BB (𝑛) is closely related to the function 𝐵(𝑛)
defined as the maximal natural number of Kolmogorov complexity at most 𝑛.
We use also several topological notions. The space N⊥ consists of natural
numbers and of a special element ⊥ (“undefined value”); the family of open sets
consists of the whole space and of all sets that do not contain ⊥. This topological
space, as well as the space Σ (where the family of open sets consists of all unions of
sets of the form Σ𝑥), is used for the general classification of complexities. For the
spaces Ω and Σ and for the space of real numbers we call a set effectively open if it
is a union of a computably enumerable family of intervals (sets of the form Σ𝑥 for
the second space and intervals with rational endpoints for the space of reals).
Most notions of computability theory (including Kolmogorov complexity) can
be relativized, which means that all involved algorithms are supplied by an external
procedure, called an oracle. That procedure can be asked whether any given number
belongs to a set 𝐴. That set is also called an oracle. Thus we get the notions of
“decidability relative to an oracle 𝐴”, “computability relative to 𝐴”, etc. In the
corresponding notations we use the superscript 𝐴, for example, 𝐶𝐴(𝑥).
In the chapter on classical information theory, we use the notion of Shannon en-
tropy of a random variable 𝜉. If the variable has 𝑘 possible outcomes and 𝑝1, . . . , 𝑝𝑘
are their probabilities then its Shannon entropy 𝐻(𝜉) is defined as −∑︀ 𝑘 𝑝𝑘 log 𝑝𝑘.
This definition makes sense also for pairs of jointly distributed random variables.
For such a pair the conditional entropy of a random variable 𝜉 when 𝜂 is known
is defined as 𝐻(𝜉, 𝜂) − 𝐻(𝜂). The difference 𝐻(𝜉) + 𝐻(𝜂) − 𝐻(𝜉, 𝜂) is called the

---

[previous page](page-025.md) · [next page](page-027.md) · [all pages](index.md)
