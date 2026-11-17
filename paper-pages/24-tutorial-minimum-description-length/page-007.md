---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
page: 7
pages: [7]
page_of: 80
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "Natural Language Most sequences of words are not valid sentences according to the English language. This fact can be exploited to substantially…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 7 of 80 - A Tutorial Introduction to the Minimum Description Length Principle

> Page 7 of the source PDF, verbatim as extracted. Canonical document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md)

Natural Language Most sequences of words are not valid sentences according to the

English language. This fact can be exploited to substantially compress English text, as long as it is syntactically mostly correct: by first describing a grammar for English, and then describing an English text D with the help of that grammar \[Gr¨unwald 1996\], D can be described using much less bits than are needed without the assumption that word order is constrained.

1.2.1 Kolmogorov Complexity and Ideal MDL

To formalize our ideas, we need to decide on a description method, that is, a formal language in which to express properties of the data. The most general choice is a general-purpose2 computer language such as C or Pascal. This choice leads to the definition of the Kolmogorov Complexity \[Li and Vit´anyi 1997\] of a sequence as the length of the shortest program that prints the sequence and then halts. The lower the Kolmogorov complexity of a sequence, the more regular it is. This notion seems to be highly dependent on the particular computer language used. However, it turns out that for every two general-purpose programming languages A and B and every data sequence D, the length of the shortest program for D written in language A and the length of the shortest program for D written in language B diﬀer by no more than a constant c, which does not depend on the length of D. This so-called invariance theorem says that, as long as the sequence D is long enough, it is not essential which computer language one chooses, as long as it is general-purpose. Kolmogorov complexity was introduced, and the invariance theorem was proved, independently by Kolmogorov \[1965\], Chaitin \[1969\] and Solomonoﬀ\[1964\]. Solomonoﬀ’s paper, called A Theory of Inductive Inference, contained the idea that the ultimate model for a sequence of data may be identified with the shortest program that prints the data. Solomonoﬀ’s ideas were later extended by several authors, leading to an ‘idealized’ version of MDL \[Solomonoﬀ1978; Li and Vit´anyi 1997; G´acs, Tromp, and Vit´anyi 2001\]. This idealized MDL is very general in scope, but not practically applicable, for the following two reasons:

1. uncomputability It can be shown that there exists no computer program that, for every set of data D, when given D as input, returns the shortest program that prints D \[Li and Vit´anyi 1997\].

2. arbitrariness/dependence on syntax In practice we are confronted with small data samples for which the invariance theorem does not say much. Then the hypothesis chosen by idealized MDL may depend on arbitrary details of the syntax of the programming language under consideration.

1.2.2 Practical MDL

Like most authors in the field, we concentrate here on non-idealized, practical versions of MDL that explicitly deal with the two problems mentioned above. The basic idea is to scale down Solomonoﬀ’s approach so that it does become applicable. This is

8

---

[previous page](page-006.md) · [next page](page-008.md) · [all pages](index.md)
