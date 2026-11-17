---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 76
pages: [76]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "3.3. EFFECTIVELY NULL SETS 77 Reformulation: a sequence is Martin-L¨of random if it does not belong to any effectively null set. One more version: a…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 76 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 76 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

3.3. EFFECTIVELY NULL SETS 77
Reformulation: a sequence is Martin-L¨of random if it does not belong to any
effectively null set.
One more version: a sequence 𝜔 is Martin-L¨of random if the singleton {𝜔} is
not an effectively null set.
A digression: terminology. The notion of Martin-L¨of randomness is a
refinement of the intuitive idea of a “typical sequence”. One could say that a
sequence is “typical” if it does not have any regularities or special features which
separates it from most sequences. (If somebody says that “Mr. X is a typical math
professor”, she probably means that Mr. X has no special characteristics that make
him different from the majority of math professors.) A “special feature” is a feature
that is possessed only by a negligible fraction of the objects considered (sequences).
For example, if a sequence 𝜔 starts with 0, this is not a special feature, since half
of the sequences start with 0. On the other hand, if each other term of 𝜔 is zero,
this is indeed a special feature.
This informal idea is implemented in the Martin-L¨of definition: a special fea-
ture is a feature that corresponds to an effectively null set, and therefore typical
sequences are sequences that do not belong to any effectively null set, i.e., Martin-
L¨of random sequences.
It would be more logical to use the word “typical” for Martin-L¨of’s defini-
tion and reserve the word “random” for more general intuitive notion that can be
formalized in different ways (and the idea of a typical sequence is one of them).
However, the attempts to introduce a new, more logical, terminology often make
the situation worse (authors have to confess that this can be said about their own
attempts!). And there is already a lot of confusion, the term “random sequence” is
already used in different ways.
So we keep the term “Martin-L¨of random sequence” (“ML-random sequence”)
for the definition given above keeping the general term “random sequence” for
a vague philosophical notion of randomness that needs additional clarification to
become a mathematical notion. (End of digression.)
The following statement is a trivial corollary of Martin-L¨of theorem; however,
it deserves a careful thinking since it looks counter-intuitive.
Theorem 29. A set 𝐴 ⊂ Ω is an effectively null set if and only if all its
elements are not Martin-L¨of random (are non-typical ).
In particular, the set of all non-ML-random sequences is the largest effectively
null set, and the set of all ML-random sequences has measure 1.
Proof. Indeed, any element of any effectively null set is not ML-random by
definition; on the other hand, if all elements of some set 𝐴 are not ML-random,
then 𝐴 is a subset of the largest effectively null set and therefore 𝐴 is an effectively
null set. 
What is strange here? Intuitively, a set 𝐴 is a null set if it has “few elements”;
the nature of these elements does not matter much. Any singleton {𝜔} ⊂ Ω is a
null set and this does not depend on the properties of the sequence 𝜔.
On the other hand, now we see that if we replace null sets by effectively null
sets, the situation changes drastically: we may put as many non-ML-random (non-
typical) sequences in a set as we wish, and it would remain an effectively null

---

[previous page](page-075.md) · [next page](page-077.md) · [all pages](index.md)
