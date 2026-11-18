---
type: Book
title: Kolmogorov Complexity and Algorithmic Randomness
description: "The standard graduate text on Kolmogorov complexity, randomness deficiency and the two-part-code view of a good model."
resource: https://www.lirmm.fr/~ashen/kolmbook-eng-scan.pdf
tags: [agi-reading-list, book, kolmogorov-complexity, minimum-description-length, modern]
sequence: 26
section: /sections/04-theory-complexity-and-optimization.md
authors: [Alexander Shen, Vladimir A. Uspensky, Nikolay Vereshchagin]
year: 2017
venue: AMS Mathematical Surveys and Monographs 220
topics: ["/topics/kolmogorov-complexity.md", "/topics/minimum-description-length.md"]
builds_on: []
enables: ["/papers/22-first-law-of-complexodynamics.md", "/papers/25-coffee-automaton.md", "/papers/27-machine-super-intelligence.md"]
sources:
  - id: reading-list
    resource: /references/the-30-papers-to-ai-mastery.md
    title: The 30 Papers to AI Mastery (curated by @rachit.speaks)
  - id: original
    resource: https://www.lirmm.fr/~ashen/kolmbook-eng-scan.pdf
    title: Kolmogorov Complexity and Algorithmic Randomness (AMS Mathematical Surveys and Monographs 220)
status: stable
generated: { by: okf_builder/1.0, at: 2026-11-17T16:30:00Z }
verified: { by: process:okf-validator, at: 2026-11-17T16:30:00Z }
extraction:
  full_text: web-extracted
  source_kind: book
  coverage: pages 1-85 of 519
  tool: Apify web-fetch
  characters: 208689
figures:
  local: 0
  remote: 0
  note: no figures: the source PDF is larger than the transfer limit, read them in the original
---

# Kolmogorov Complexity and Algorithmic Randomness

**Authors:** Alexander Shen, Vladimir A. Uspensky, Nikolay Vereshchagin  
**Year:** 2017 · **Venue:** AMS Mathematical Surveys and Monographs 220 · **Position in the list:** 26 of 30  
**Read the original:** <https://www.lirmm.fr/~ashen/kolmbook-eng-scan.pdf>

## Overview

The standard graduate text on Kolmogorov complexity, randomness deficiency and the two-part-code view of a good model. The reading list points at the final chapter on algorithmic statistics: what it means for a model to be a good explanation of one particular string.[^reading-list]

## Where it sits

This paper is part of [Theory, Complexity & Optimization](/sections/04-theory-complexity-and-optimization.md), the theory, complexity & optimization section of the list.

It is a prerequisite for: [22 - The First Law of Complexodynamics](/papers/22-first-law-of-complexodynamics.md), [25 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton](/papers/25-coffee-automaton.md), [27 - Machine Super Intelligence](/papers/27-machine-super-intelligence.md).

## Full text

The text below was extracted from the published source (book) on 2026-11-17. The open English text edition of the book, pages 1 to 85 of 519 - the fetch was capped at that length. The reading list points at chapter 14, *Algorithmic statistics* (page 425), which falls outside the fetched range; read it at the link. Book page numbers are preserved as `<!-- page N -->` markers, so page chunks below carry the book's own pagination.

To the memory of Andrei Muchnik

<!-- page 1 -->

<!-- page 2 -->

Preface
The notion of algorithmic complexity (also sometimes called “algorithmic en-
tropy”) appeared in 1960s inbetween the theory of computation, probability theory
and information theory.
The idea of A.N. Kolmogorov was to measure the amount of information in
finite objects (and not in random variables, as it is done in classical Shannon infor-
mation theory). His famous paper [77], published in 1965, explains how this can
be done (up to a bounded additive term) using the algorithmic approach.
Similar ideas was suggested few years earlier by R. Solomonoff (see [185] and
his other papers; the historical account and reference can be found in [102]).1
The motivation of Solomonoff was quite different. He tried to define the notion
of “a priori probability”. Imagine there is some experiment (random process) and
we know nothing about its internal structure. Can we say something about the
probabilities of different outcomes in this situation? One can relate this to the
complexity measures saying that simple objects have greater a priori probability
than complex ones. (Unfortunately, Solomonoff’s work become popular only after
Kolmogorov mentioned it in his paper.)
In 1965 G. Chaitin (then an 18-years-old undergaduate student) submitted
two papers [28] and [29]; they were published in 1966 and 1969 respectively. In
the second paper he proposed the same definition of algorithmic complexity as
Kolmogorov.
The basic properties of Kolmogorov complexity were established in 1970s.
Working independently, C.P. Schnorr and L. Levin (who was a student of Kol-
mogorov) found a link between complexity and the notion of algorithmic random-
ness (introduced in 1966 by P. Martin-L¨of [114]). To achieve this, they introduced
a slightly different version of complexity, the so-called monotone complexity. Also
the Solomonoff’s ideas about a priori probability were formalized in the form of pre-
fix complexity, introduced by Levin and later by Chaitin. The notions of complexity
turned out to be useful both for theory of computation and probability theory.
The Kolmogorov complexity became popular (and for a good reason: it is a
basic and philosophically important notion of algorithms theory) after M. Li and
P. Vit´anyi published a book on the subject [102] (first edition appeared in 1993).
Almost everything about Kolmogorov complexity that was known at the moment
was covered in the book or at least mentioned as an exercise. This book also
provided a detailed historical account, references to first publications, etc. Then
the books of C. Calude [25], and A. Nies [146] appeared, as well as the book of
R. Downey and D. Hirschfeldt [49]. These books cover many interesting results
1Kolmogorov wrote in [78]: “I came to a similar notion not knowing about Solomonoff’s
work”.
3

<!-- page 3 -->

4 PREFACE
obtained recently (in particular, the results that relate complexity and randomness
with classical recursion theory).
Our book does not try to be comprehensive (in particular, we do not say much
about the recent results mentioned above). Instead, we tried to select the most
important topics and results (both from technical and philosophical viewpoint)
and explain them clearly. We do not say much about the history of the topic: as
it is usually done in textbooks, we formulate most statements without references,
and this does not mean (of course) any authorship claim.
We start the book with a section “What is this book about?” where we try to
overview briefly the main ideas and topics related to Kolmogorov complexity and
algorithmic randomness, so the reader can browse this section to decide whether
the book is worth reading.
As an appendix we reproduce the (English translation) of a small brochure
written by one of the authors (V.U.), based on his talk for high school students
and undergraduates (July 23, 2005) delivered during the “Modern Mathematics”
Summer School (Dubna near Moscow); the brochure was published in 2006 by
MCCME publishing house (Moscow). The lecture was devoted to different notions
of algorithmic randomness, and the reader who has no time or incentive to study
the corresponding chapters of the book in detail, still can get some acquaintance
with this topic.
Unfortunately, the notation and terminology related to Kolmogorov complexity
is not very logical (and different people often use different notation). Even the same
authors used different notation in different papers. For example, Kolmogorov used
both the letters 𝐾 and 𝐻 in his two basic publications [77, 78]. In [77] he used the
term “complexity” and denoted the complexity of a string 𝑥 by 𝐾(𝑥). Later he used
for the same notion the term “entropy” used in Shannon information theory (and
earlier in physics). Shannon information theory is based on probability theory;
Kolmogorov had an ambitious plan to construct a parallel theory that does not
depend on the notion of probability. In [78] Kolmogorov wrote, using the same
word ‘entropy’ in this new sense:
The ordinary definition of entropy uses probability concepts, and
thus does not pertain to individual values, but to random val-
ues, i.e., to probability distributions within a group of values.
⟨. . .⟩ By far, not all applications of information theory fit ratio-
nally into such an interpretation of its basic concepts. I believe
that the need for attaching definite meanings to the expressions
𝐻(𝑥|𝑦) and 𝐼(𝑥|𝑦), in the case of individual values 𝑥 and 𝑦 that
are not viewed as a result of random tests with a definite law
of distribution, was realized long ago by many who dealt with
information theory.
As far as I know, the first paper published on the idea of
revising information theory so as to satisfy the above conditions
was the article of Solomonoff [185]. I came to similar conclu-
sions, before becoming aware of Solomonoff’s work in 1963–1964,
and published my first article on the subject [77] in early 1965.
⟨. . .⟩

<!-- page 4 -->

PREFACE 5
The meaning of the new definition is very simple. Entropy
𝐻(𝑥|𝑦) is the minimal [bit] length of a ⟨. . .⟩ program 𝑃 that per-
mits construction of the value of 𝑥, the value of 𝑦 being known,
𝐻(𝑥 | 𝑦) = min
𝐴(𝑃,𝑦)=𝑥 𝑙(𝑃 ).
This concept is supported by the general theory of “computable”
(partially recursive) functions, i.e., by theory of algorithms in
general.
⟨. . .⟩ The preceding rather superficial discourse should prove
two general theses.
1) Basic information theory concepts must and can be
founded without recourse to the probability theory, and in such
a manner that “entropy” and “mutual information” concepts are
applicable to individual values.
2) Thus introduced, information theory concepts can form
the basis of the term random, which naturally suggests that ran-
domness is the absence of regularities.2
And earlier (April 23, 1965), giving a talk “The notion of information and the
foundations of the probability theory” at the Institute of Philosophy of the USSR
Academy of Sciences, Kolmogorov said:
So the two problems arise sequentially:
1. Is it possible to free the information theory (and the
notion of the “amount of information”) from probabilities?
2. It is possible to develop the intuitive idea of randomness
as incompressibility (the law describing the object cannot be
shortened)?
(the transcript of his talk was published in [84] on p. 126).
So Kolmogorov uses the term “entropy” for the same notion that was named
“complexity” in his first paper, and denotes it by letter 𝐻 instead of 𝐾.
Later the same notion was denoted by 𝐶 (see, e.g., [102]) while the letter 𝐾
is used for prefix complexity (denoted by KP(𝑥) in the Levin’s papers where prefix
complexity was introduced).
Unfortunately, the attempts to unify the terminology and notation made by
different people (including the authors) have lead mostly to increasing confusion.
In the English version of this book we follow the terminology that is most used
nowadays, with few exceptions, and mention the other notations used. For reader’s
convenience, the list of the used notation and the index are provided.
2The published English version of this paper says “random is the absence of periodicity”, but
this evidently is a translation error, and we correct the text following the Russian version.

<!-- page 5 -->

6 PREFACE
In the beginning of 1980s Kolmogorov (with the assistance of A. Semenov)
initiated a seminar at the Mathematics and Mechanics Department of Moscow
State (Lomonosov) University called “Description and computation complexity”;
now the seminar (still active) is known as “Kolmogorov seminar”. The authors are
deeply grateful to their colleagues working in this seminar, including A. Zvonkin,
E. Asarin, V. Vovk (they were Kolmogorov’s students), S. Soprunov, V. Vyu-
gin, A. Romashchenko, M. Vyalyi, S. Tarasov, A. Chernov, M. Vyugin, S. Posit-
selsky, K. Makarychev, Yu. Makarychev, M. Ushakov, M. Ustinov, S. Salnikov,
A. Rumyantsev, D. Musatov, V. Podolskii, I. Mezhirov, Yu. Pritykin, M. Raskin,
A. Khodyrev, P. Karpovich, A. Minasyan, E. Kalinina, G. Chelnokov, I. Razen-
shteyn, M. Andreev, A. Savin, M. Dektyarev, A. Savchik, A. Kumok, V. Arzu-
manyan, A. Makhlin, G. Novikov, A. Milovanov; the book would not be possible
without them.
The frog drawing for the cover was made by Marina Feigelman; the cover itself
was designed by Olga Lehtonen. As usual, we are grateful (in particular, for the
help in the preparation of a camera-ready copy for the Russian edition) to Victor
Shuvalov.
Authors were supported by International Science Foundation (Soros founda-
tion), STINT (Sweden), Russian Fund for Basic Research (01-01-00493-a, 01-01-
01028-a, 06-01-00122-a, 09-01-00709-a, 12-01-00864-a), CNRS and ANR (France,
ANR-08-EMER-008 NAFIT and ANR-15-CE40-0016-01 RaCAF grants).
The book was made possible by the generous support of our colleagues, in-
cluding Bruno Bauwens, Laurent Bienvenu, Harry Buhrman, Cris Calude, Bruno
Durand, P´eter G´acs, Denis Hirschfeldt, Rupert H¨olzl,, Mathieu Hoyrup, Michal
Kouck´y, Leonid Levin, Wolfgang Merkle, Joseph Miller, Andre Nies, Christopher
Porter, Jan Reimann, Jason Rute, Michael Sipser, Steven Simpson, Paul Vit´anyi,
Sergey Vorobyov, and many others.
We are thankful to American Mathematical Society (in particular, Sergey
Gelfand) for the suggestion to submit the book for publication in their book pro-
gram and for the kind permission to keep the book available freely in electronic
form at our homepages. We thank the (anonymous) referees for their attention and
suggestions, and the language editors for correcting our English errors.
For many years the authors had the privilege to work in a close professional and
personal contact with Andrej Muchnik (1958–2007), an outstanding mathematician,
deep thinker and an admirable person, who participated in the work of Kolmogorov
seminar and inspired a lot of work done in this seminar. We devote this book to
his memory.
A. Shen, V. Uspensky, N. Vereshchagin September 1, 2016

<!-- page 6 -->

<!-- page 12 -->

OPTIMAL DESCRIPTION MODES 13
them. Indeed, let
𝐷(0𝑦) = 𝐷1(𝑦),
𝐷(1𝑦) = 𝐷2(𝑦).
In other words, we consider the first bit of a description as the index of a description
mode and the rest as the description (for this mode).
If 𝑦 is a description of 𝑥 with respect to 𝐷1 (or 𝐷2), then 0𝑦 (respectively, 1𝑦)
is a description of 𝑥 with respect to 𝐷 as well. This description is only one bit
longer, therefore we have
𝐶𝐷 (𝑥) 6 𝐶𝐷1 (𝑥) + 1,
𝐶𝐷 (𝑥) 6 𝐶𝐷2 (𝑥) + 1
for all 𝑥. Thus the mode 𝐷 is not worse than both 𝐷1 and 𝐷2.
This idea is often used in practice. For instance, a zip-archive has a preamble;
the preamble says (among other things) which mode was used to compress this
particular file, and the compressed file follows the preamble.
If we want to use 𝑁 different compression modes, we need to reserve initial
log2 𝑁 bits for the index of the compression mode.
Using a generalization of this idea, we can prove the following theorem:
Theorem 1 (Solomonoff–Kolmogorov). There is a description mode 𝐷 that is
not worse than any other one: for every description mode 𝐷′ there is a constant 𝑐
such that
𝐶𝐷 (𝑥) 6 𝐶𝐷′ (𝑥) + 𝑐
for every string 𝑥.
A description mode 𝐷 having this property is called optimal.
Proof. Recall that a description mode by definition is a computable function.
Every computable function has a program. We assume that programs are binary
strings. Moreover, we assume that reading the program bits from left to right we
can determine uniquely where it ends, that is, programs are “self-delimiting”. Note
that every programming language can be modified in such a way that programs are
self-delimiting. For instance, we can double every bit of a given program (changing
0 to 00 and 1 to 11) and append the pattern 01 to its end.
Define now a new description mode 𝐷 as follows:
𝐷(𝑃 𝑦) = 𝑃 (𝑦)
where 𝑃 is a program (in the chosen self-delimiting programming language) and
𝑦 is any binary string. That is, the algorithm 𝐷 scans the input string from the
left to the right and extracts a program 𝑃 from the input. (If the input does not
start with a valid program, 𝐷 does whatever it wants, say, goes into an infinite
loop. The self-delimiting property guarantees that the decomposition of input is
unique: if 𝑃 𝑦 = 𝑃 ′𝑦′ for two programs 𝑃 and 𝑃 ′, then one of the programs is a
prefix of the other one.) Then 𝐷 applies the extracted program 𝑃 to the rest of the
input (𝑦) and returns the obtained result. (So 𝐷 is just an “universal algorithm”,
or “interpreter”; the only difference is that program and input are not separated
and therefore we need to use a self-delimiting programming language.)
Let us show that indeed 𝐷 is not worse than any other description mode 𝑃 . We
assume that the program 𝑃 is written in the chosen self-delimiting programming

<!-- page 13 -->

14 WHAT IS THIS BOOK ABOUT?
language. If 𝑦 is a shortest description of the string 𝑥 with respect to 𝑃 , then 𝑃 𝑦
is a description of 𝑥 with respect to 𝐷 (though not necessarily a shortest one).
Therefore, compared to 𝑃 , the shortest description is at most 𝑙(𝑃 ) bits longer, and
𝐶𝐷 (𝑥) 6 𝐶𝑃 (𝑥) + 𝑙(𝑃 ).
The constant 𝑙(𝑃 ) depends only on the description mode 𝑃 (and not on 𝑥). 
Basically, we used the same trick as in the preceding example, but instead
of merging two description modes we join all of them. Each description mode
is prefixed by its index (program, identifier). The same idea is used in practice.
A “self-extracting archive” is an executable file starting with a small program (a
decompressor); the rest is considered as an input to that program. This program
is loaded into the memory and then it decompresses the rest of the file.
Note that in our construction optimal decompressor works for a very long time
on some inputs (as some programs have large running time), and is undefined on
some other inputs.
Kolmogorov complexity
Fix an optimal description mode 𝐷 and call 𝐶𝐷 (𝑥) the Kolmogorov complexity
of the string 𝑥. In the notation 𝐶𝐷 (𝑥) we drop the subscript 𝐷 and write just 𝐶(𝑥).
If we switch to another optimal description mode, the change in complexity is
bounded by an additive constant: for every optimal description modes 𝐷1 and 𝐷2
there is a constant 𝑐(𝐷1, 𝐷2) such that
|𝐶𝐷1 (𝑥) − 𝐶𝐷2 (𝑥)| 6 𝑐(𝐷1, 𝐷2)
for all 𝑥. Sometimes this inequality is written as follows:
𝐶𝐷1 (𝑥) = 𝐶𝐷2 (𝑥) + 𝑂(1),
where 𝑂(1) stands for a bounded function of 𝑥.
Could we then consider the Kolmogorov complexity of a particular string 𝑥
without having in mind a specific optimal description mode used in the definition
of 𝐶(𝑥)? No, since by adjusting the optimal description mode we can make the
complexity of 𝑥 arbitrarily small or arbitrarily large. Similarly, the relation “string 𝑥
is simpler than 𝑦”, that is, 𝐶(𝑥) < 𝐶(𝑦), has no meaning for two fixed strings 𝑥
and 𝑦: by adjusting the optimal description mode we can make any of these two
strings simpler than the other one.
One may wonder then whether Kolmogorov complexity has any sense at all.
Trying to defend this notion, let us recall the construction of the optimal description
mode used in the proof of the Solomonoff–Kolmogorov theorem. This construction
uses some programming language, and two different choices of this language lead
to two complexities that differ at most by a constant. This constant is in fact the
length of the program that is written in one of these two languages and interprets
the other one. If both languages are “natural”, we can expect this constant to be
not that huge, just several thousands or even several hundreds. Therefore if we
speak about strings whose complexity is, say, about 105 (i.e., a text of a long and
not very compressible novel), or 106 (which is reasonable for DNA strings, unless
they are compressible much more than the biologists think now), then the choice
of the programming language is not that important.
Nevertheless one should always have in mind that all statements about Kol-
mogorov complexity are inherently asymptotic: they involve infinite sequences of

<!-- page 14 -->

COMPLEXITY AND INFORMATION 15
strings. This situation is typical also for computational complexity: usually upper
and lower bounds for complexity of some computational problem are asymptotic
bounds.
Complexity and information
One can consider the Kolmogorov complexity of 𝑥 as the amount of informa-
tion in 𝑥. Indeed, a string of zeros, which has a very short description, has little
information, and a chaotic string, which cannot be compressed, has a lot of informa-
tion (although that information can be meaningless—we do not try to distinguish
between meaningful and meaningless information; so, in our view, any abracadabra
has much information unless it has a short description).
If the complexity of a string 𝑥 is equal to 𝑘, we say that 𝑥 has 𝑘 bits of
information. One can expect that the amount of information in a string does not
exceed its length, that is, 𝐶(𝑥) 6 𝑙(𝑥). This is true (up to an additive constant, as
we have already said).
Theorem 2. There is a constant 𝑐 such that
𝐶(𝑥) 6 𝑙(𝑥) + 𝑐
for all strings 𝑥.
Proof. Let 𝐷(𝑦) = 𝑦 for all 𝑦. Then 𝐶𝐷 (𝑥) = 𝑙(𝑥). By optimality, there
exists some 𝑐 such that
𝐶(𝑥) 6 𝐶𝐷 (𝑥) + 𝑐 = 𝑙(𝑥) + 𝑐
for all 𝑥. 
Usually this statement is written as follows: 𝐶(𝑥) 6 𝑙(𝑥) + 𝑂(1). Theorem 2
implies, in particular, that Kolmogorov complexity is always finite, that is, every
string has a description.
Here is another property of “amount of information” that one can expect: the
amount of information does not increase when algorithmic transformation is per-
formed. (More precisely, the increase is bounded by an additive constant depending
on the transformation algorithm.)
Theorem 3. For every algorithm 𝐴 there exists a constant 𝑐 such that
𝐶(𝐴(𝑥)) 6 𝐶(𝑥) + 𝑐
for all 𝑥 such that 𝐴(𝑥) is defined.
Proof. Let 𝐷 be an optimal decompressor that is used in the definition of the
Kolmogorov complexity. Consider another decompressor 𝐷′:
𝐷′(𝑝) = 𝐴(𝐷(𝑝)).
(We apply first 𝐷 and then 𝐴.) If 𝑝 is a description of a string 𝑥 with respect to 𝐷
and 𝐴(𝑥) is defined, then 𝑝 is a description of 𝐴(𝑥) with respect to 𝐷′. Let 𝑝 be a
shortest description of 𝑥 with respect to 𝐷. Then we have
𝐶𝐷′ (𝐴(𝑥)) 6 𝑙(𝑝) = 𝐶𝐷 (𝑥) = 𝐶(𝑥).
By optimality we obtain
𝐶(𝐴(𝑥)) 6 𝐶𝐷′ (𝐴(𝑥)) + 𝑐 6 𝐶(𝑥) + 𝑐
for some 𝑐 and all 𝑥. 

<!-- page 15 -->

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

<!-- page 16 -->

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

<!-- page 17 -->

18 WHAT IS THIS BOOK ABOUT?
elements as equiprobable, then we obtain a ridiculously small value (less than 1000
bits); for the non-uniform distributions the entropy is even less.
So we see that in these contexts Kolmogorov complexity looks like a more
adequate tool than Shannon entropy.
Complexity and randomness
Let us recall the inequality 𝐶(𝑥) 6 𝑙(𝑥) + 𝑂(1) (Theorem 2). For most of
the strings its left hand side is close to the right hand side. Indeed, the following
statement is true:
Theorem 5. Let 𝑛 be an integer. Then there are less than 2𝑛 strings 𝑥 such
that 𝐶(𝑥) < 𝑛.
Proof. Let 𝐷 be the optimal description mode used in the definition of Kol-
mogorov complexity. Then only strings 𝐷(𝑦) for all 𝑦 such that 𝑙(𝑦) < 𝑛 have
complexity less than 𝑛. The number of such strings does not exceed the number of
strings 𝑦 such that 𝑙(𝑦) < 𝑛, i.e., the sum
1 + 2 + 4 + 8 + . . . + 2𝑛−1 = 2𝑛 − 1
(there are 2𝑘 strings for each length 𝑘 < 𝑛). 
This implies that the fraction of strings of complexity less than 𝑛 − 𝑐 among all
strings of length 𝑛 is less than 2𝑛−𝑐/2𝑛 = 2−𝑐. For instance, the fraction of strings
of complexity less than 90 among all strings of length 100 is less than 2−10.
Thus the majority of strings (of a given length) are incompressible or almost
incompressible. In other words, a randomly chosen string of the given length is
almost incompressible. This can be illustrated by the following mental (or even
real) experiment. Toss a coin, say, 80000 times and get a sequence of 80000 bits.
Convert it into a file of size 10000 bytes (8 bits = 1 byte). One can bet that no
compression software (existing before the start of the experiment) can compress the
resulting file by more than 10 bytes. Indeed, the probability of this event is less
than 2−80 for every fixed compressor, and the number of (existing) compressors is
not so large.
It is natural to consider incompressible strings as “random” ones: informally
speaking, randomness is the absence of any regularities that may allow us to com-
press the string. Of course, there is no strict borderline between “random” and
“non-random” strings. It is ridiculous to ask which strings of length 3 (i.e., 000,
001, 010, 011, 100, 101, 110, 111) are random and which are not.
Another example: assume that we start with a “random” string of length 10000
and replace its bits by all zeros (one bit at a step). At the end we get a certainly
non-random string (zeros only). But it would be na¨ıve to ask at which step the
string has become non-random for the first time.
Instead, we can naturally define the “randomness deficiency” of a string 𝑥 as
the difference 𝑙(𝑥) − 𝐶(𝑥). Using this notion, we can restate Theorem 2 as follows:
the randomness deficiency is almost non-negative (i.e., larger than a constant).
Theorem 5 says that the randomness deficiency of a string of length 𝑛 is less than
𝑑 with probability at least 1 − 1/2𝑑 (assuming that all strings are equiprobable).
Now consider the Law of Large Numbers; it says that most of the 𝑛-bit strings
have frequency of ones close to 1/2. This law can be translated into Kolmogorov
complexity language as follows: the frequency of ones in every string with small

<!-- page 18 -->

NON-COMPUTABILITY OF 𝐶 AND BERRY’S PARADOX 19
randomness deficiency is close to 1/2. This translation implies the original state-
ment since most of the strings have small randomness deficiency. We will see later
that actually these formulations are equivalent.
If we insist on drawing a strict borderline between random and non-random
objects, we have to consider infinite sequences instead of strings. The notion of
randomness for infinite sequences of zeros and ones was defined by Kolmogorov’s
student P. Martin-L¨of (he came to Moscow from Sweden). We discuss it in Section 3.
Later C. Schnorr and L. Levin found a characterization of randomness in terms of
complexity: an infinite binary sequence is random if and only if the randomness
deficiency of its prefixes is bounded by a constant. This criterion, however, uses
another version of Kolmogorov complexity called monotone complexity.
Non-computability of 𝐶 and Berry’s paradox
Before discussing applications of Kolmogorov complexity, let us mention a fun-
damental problem that reappears in any application. Unfortunately, the function 𝐶
is not computable: there is no algorithm that given a string 𝑥 finds its Kolmogorov
complexity. Moreover, there is no computable nontrivial (unbounded) lower bound
for 𝐶.
Theorem 6. Let 𝑘 be a computable (not necessarily total ) function from Ξ
to N. (In other words, 𝑘 is an algorithm that terminates on some binary strings
and returns natural numbers as results.) If 𝑘 is a lower bound for Kolmogorov
complexity, that is, 𝑘(𝑥) 6 𝐶(𝑥) for all 𝑥 such that 𝑘(𝑥) is defined, then 𝑘 is
bounded: all its values do not exceed some constant.
The proof of this theorem is a reformulation of the so-called “Berry’s paradox”.
This paradox considers
the minimal natural number that cannot be defined by at most
fourteen English words.
This phrase has exactly fourteen words and defines that number. Thus we get a
contradiction.
Following this idea consider the first binary string whose Kolmogorov complexity
is greater than a given number 𝑁 . By definition, its complexity is greater than 𝑁 .
On the other hand, this string has a short description that includes some fixed
amount of information plus the binary notation of 𝑁 (which requires about log2 𝑁
bits), and the total number of bits needed is much less than 𝑁 for large 𝑁 . That
would be a contradiction if we knew how to effectively find this string given its
description. Using the computable lower bound 𝑘, we can convert this paradox into
the proof.
Proof. Consider the function 𝐵(𝑁 ) whose argument 𝑁 is a natural number;
it is computed by the following algorithm:
perform in parallel the computations 𝑘(Λ), 𝑘(0), 𝑘(1), 𝑘(00),
𝑘(01), 𝑘(10), 𝑘(11), . . . until some string 𝑥 such that 𝑘(𝑥) > 𝑁
appears; then return 𝑥.
If the function 𝑘 is unbounded then the function 𝐵 is total and 𝑘(𝐵(𝑁 )) > 𝑁
by construction for every 𝑁 . As 𝑘 is a lower bound for 𝐾, we have 𝐶(𝐵(𝑁 )) > 𝑁 .
On the other hand 𝐵(𝑁 ) can be computed given the binary representation bin(𝑁 )

<!-- page 19 -->

20 WHAT IS THIS BOOK ABOUT?
of 𝑁 , therefore
𝐶(𝐵(𝑁 )) 6 𝐶(bin(𝑁 )) + 𝑂(1) 6 𝑙(bin(𝑁 )) + 𝑂(1) 6 log2 𝑁 + 𝑂(1)
(the first inequality is provided by Theorem 3, the second one is provided by The-
orem 2; term 𝑂(1) stands for a bounded function). So we obtain
𝑁 < 𝐶(𝐵(𝑁 )) 6 log2 𝑁 + 𝑂(1),
which cannot happen if 𝑁 is large enough. 
Some applications of Kolmogorov complexity
Let us start with a disclaimer: the applications we will talk about are not real
“practical” applications; we just establish relations between Kolmogorov complexity
and other important notions.
Occam’s razor. We start with a philosophical question. What do we mean
when we say that a theory provides a good explanation for some experimental data?
Assume that we are given some experimental data and there are several theories to
explain the data. For example, the data might be the observed positions of planets
in the sky. We can explain them as Ptolemy did, with epicycles and deferents,
introducing extra corrections when needed. On the other hand, we can use the
laws of the modern mechanics. Why do we think that the modern theory is better?
A possible answer: the modern theory can compute the positions of planets with
the same (or even better) accuracy given less parameters. In other words, Kepler’s
achievement is a shorter description of the experimental data.
Roughly speaking, experimenters obtain binary strings and theorists find short
descriptions for them (thus proving upper bounds for complexities of those strings);
the shorter the description is, the better is the theorist.
This approach is sometimes called “Occam’s razor” and is attributed to the
philosopher William of Ockham who said that entities should not be multiplied be-
yond necessity. It is hard to judge whether he would agree with such interpretation
of his words.
We can use the same idea in more practical contexts. Assume that we design
a machine that reads handwritten zip codes on envelopes. We are looking for a
rule that separates, say, images of zeros from images of ones. An image is given as
a Boolean matrix (or a binary string). We have several thousands of images and
for each image we know whether it means 0 or 1. We want to find a reasonable
separating rule (with the hope that it can be applied to the forthcoming images).
What means “reasonable” in this context? If we just list all the images in our list
together with their classification, we get a valid separation rule—at least it works
until we receive a new image—however, the rule is way too long. It is natural to
assume that a reasonable rule must have a short description, that is, it must have
low Kolmogorov complexity.
Foundations of probability theory. The probability theory itself, being
currently a part of measure theory, is mathematically sound and does not need any
extra “foundations”. The difficult questions arise, however, if we try to understand
why this theory could be applied to the real world phenomena and how it should
be applied.
Assume that we toss a coin thousand times (or test some other hardware ran-
dom number generator) and get a bit string of length 1000. If this string contains

<!-- page 20 -->

SOME APPLICATIONS OF KOLMOGOROV COMPLEXITY 21
only zeros or equals 0101010101 . . . (zeros and ones alternate), then we definitely
will conclude that the generator is bad. Why?
Usual explanation: the probability of obtaining thousand zeros is negligible
(2−1000) provided the coin is fair. Therefore the conjecture of a fair coin is refuted
by the experiment.
The problem with this explanation is that we do not always reject the generator:
there should be some sequence 𝛼 of thousand zeros and ones which is consistent
with this conjecture. Note, however, that the probability of obtaining the sequence
𝛼 as a result of fair coin tossing is also 2−1000. So what is the reason behind our
complaints? What is the difference between the sequence of thousand zeros and
the sequence 𝛼?
The reason is revealed when we compare Kolmogorov complexities of these
sequences.
Proving theorems of probability theory. As an example, consider the
Strong Law of Large Numbers. It claims that for almost all (according to the the
uniform Bernoulli probability distribution) infinite binary sequences the limit of
frequencies of 1s in their initial segments equals 1/2.
More formally, let Ω be the set of all infinite sequences of zeros and ones.
The uniform Bernoulli measure on Ω is defined as follows. For every finite binary
string 𝑥 consider the set Ω𝑥 consisting of all infinite sequences that start with 𝑥.
For example, ΩΛ = Ω. The measure of Ω𝑥 is equal to 2−𝑙(𝑥). For example, the
measure of the set Ω01 that consists of all sequences starting with 01, equals 1/4.
For each sequence 𝜔 = 𝜔0𝜔1𝜔2 . . . consider the limit of the frequencies of 1s in
the prefixes of 𝜔, that is,
lim
𝑛→∞
𝜔0 + 𝜔1 + . . . + 𝜔𝑛−1
𝑛
We say that 𝜔 satisfies the Strong Law of Large Numbers (SLLN) if this limit exists
and is equal to 1/2. For instance, the sequence 010101 . . . , having period 2, satisfies
the SLLN and the sequence 011011011 . . ., having period 3, does not.
The Strong Law of Large Numbers says that the set of sequences that do not
satisfy SLLN has measure 0. Recall that a set 𝐴 ⊂ Ω has measure 0 if for all 𝜀 > 0
there is a sequence of strings 𝑥0, 𝑥1, 𝑥2, . . . such that
𝐴 ⊂ Ω𝑥0 ∪ Ω𝑥1 ∪ Ω𝑥2 ∪ . . .
and the sum of the series
2−𝑙(𝑥0) + 2−𝑙(𝑥1) + 2−𝑙(𝑥2) + . . .
(the sum of the measures of Ω𝑥𝑖 ) is less than 𝜀.
One can prove SLLN using the notion of a Martin-L¨of random sequence men-
tioned above. The proof consists of two parts. First, we show that every Martin-L¨of
random sequence satisfies SLLN. This can be done using Levin–Schnorr random-
ness criterion (if the limit does not exist or differs from 1/2, then the complexity
of some prefix is less than it should be for a random sequence).
The second part is rather general and does not depend on the specific law of
probability theory. We prove that the set of all Martin-L¨of non-random sequences
has measure zero. This implies that the set of sequences that do not satisfy SLLN
is included in a set of measure 0 and hence has measure 0 itself.
The notion of a random sequence is philosophically interesting in its own right.
In the beginning of XXth century Richard von Mises suggested to use this notion

<!-- page 21 -->

22 WHAT IS THIS BOOK ABOUT?
(he called it in German “Kollektiv”) as a basis for probability theory (at that time
the measure theory approach was not developed yet). He considered the so-called
“frequency stability” as a main property of random sequences. We will consider
von Mises’ approach to the definition of a random sequence (and the subsequent
developments) in Chapter 9.
Lower bounds for computational complexity. Kolmogorov complexity
turned out to be a useful technical tool when proving lower bounds for computa-
tional complexity. Let us explain the idea using the following model example.
Consider the following problem: Initially a string 𝑥 of length 𝑛 is located in
the 𝑛 leftmost cells of the tape of a Turing machine. The machine has to copy 𝑥,
that is, to get 𝑥𝑥 on the tape (the string 𝑥 is intact and its copy is appended) and
halt.
Since the middle of 1960ies it is well known that (one-tape) Turing machine
needs time proportional to 𝑛2 to perform this task. More specifically, one can show
that for every Turing machine 𝑀 that can copying every string 𝑥 there exists some
𝜀 > 0 such that for all 𝑛 there is a string 𝑥 of length 𝑛 whose copying requires at
least 𝜀𝑛2 steps.
Consider the following intuitive argument supporting this claim. The number
of internal states of a Turing machine is a constant (depending on the machine).
That is, the machine can keep in its memory only a finite number of bits. The
speed of the head movement is also limited: one cell per step. Hence the rate of
information transfer (measured in bit·cell/step) is bounded by a constant depending
on the number of internal states. To copy a string 𝑥 of length 𝑛, we need to move 𝑛
bits by 𝑛 cells to the right, therefore the number of steps should be proportional
to 𝑛2 (or more).
Using Kolmogorov complexity, we can make this argument rigorous. A string
is hard to copy if it contains maximal amount of information, i.e., its complexity is
close to 𝑛. We consider this example in detail in Section 8.2 (p. 245).
A combinatorial interpretation of Kolmogorov complexity. We con-
sider here one example of this kind (see Chapter 10, p. 323, for more details).
One can prove the following inequality for complexity of three strings and their
combinations:
2𝐶(𝑥𝑦𝑧) 6 𝐶(𝑥𝑦) + 𝐶(𝑥𝑧) + 𝐶(𝑦𝑧) + 𝑂(log 𝑛)
for all strings 𝑥, 𝑦, 𝑧 of length at most 𝑛.
It turns out that this inequality has natural interpretations that are not related
to complexity at all. In particular, it implies (see [65]) the following geometrical
fact:
Consider a body 𝐵 in a three-dimensional Euclidean space with coordinate axes
𝑂𝑋, 𝑂𝑌 and 𝑂𝑍. Let 𝑉 be 𝐵’s volume. Consider 𝐵’s orthogonal projections onto
coordinate planes 𝑂𝑋𝑌 , 𝑂𝑋𝑍 and 𝑂𝑌 𝑍. Let 𝑆𝑥𝑦 , 𝑆𝑥𝑧 and 𝑆𝑦𝑧 be the areas of
these projections. Then
𝑉 2 6 𝑆𝑥𝑦 · 𝑆𝑥𝑧 · 𝑆𝑦𝑧 .
Here is an algebraic corollary of the same inequality. For every group 𝐺 and
its subgroups 𝑋, 𝑌 and 𝑍 we have
|𝑋 ∩ 𝑌 ∩ 𝑍|2 > |𝑋 ∩ 𝑌 | · |𝑋 ∩ 𝑍| · |𝑌 ∩ 𝑍|
|𝐺| ,
where |𝐻| denotes the number of elements in 𝐻.

<!-- page 22 -->

SOME APPLICATIONS OF KOLMOGOROV COMPLEXITY 23
G¨odel incompleteness theorem. Following G. Chaitin, let us explain how
to use Theorem 6 in order to prove the famous G¨odel incompleteness theorem. This
theorem states that not all true statements of a formal theory that is “rich enough”
(the formal arithmetic and the axiomatic set theory are two examples of such a
theory) are provable in the theory.
Assume that for every string 𝑥 and every natural number 𝑛, one can express
the statement 𝐶(𝑥) > 𝑛 as a formula in the language of our theory. (This statement
says that the chosen optimal decompressor 𝐷 does not output 𝑥 on any input of
length at most 𝑛; one can easily write this statement in the formal arithmetic and
therefore in the set theory.)
Let us generate all the proofs (derivations) in our theory and select those of
them who prove some statement of the form 𝐶(𝑥) > 𝑛 where 𝑥 is some string
and 𝑛 is some integer (statements of this type have no free variables). Once we
have found a new theorem of this type, we compare 𝑛 with all previously found 𝑛’s.
If the new 𝑛 is greater than all previous 𝑛’s we write the new 𝑛 into the “records
table” together with the corresponding 𝑥𝑛.
There are two possibilities: either (1) the table will grow infinitely, or (2) there
is the last statement 𝐶(𝑋) > 𝑁 in the table which remains unbeaten forever. If (2)
happens, there is an entire class of true statements that have no proof. Namely, all
true statements of the form 𝐶(𝑥) > 𝑛 with 𝑛 > 𝑁 have no proofs. (Recall that by
Theorem 5 there are infinitely many such statements.)
In the first case we have infinite computable sequences of strings 𝑥0, 𝑥1, 𝑥2 . . .
and numbers 𝑛0 < 𝑛1 < 𝑛2 < . . . such that all statements 𝐶(𝑥𝑖) > 𝑛𝑖 are provable.
We assume that the theory proves only true statements, thus all the inequalities
𝐶(𝑥𝑖) > 𝑛𝑖 are true. Without loss of generality we can assume that all 𝑥𝑖 are
pairwise different (we can omit 𝑥𝑖 if there exists 𝑗 < 𝑖 such that 𝑥𝑗 = 𝑥𝑖; every string
can occur only finitely many times in the sequence 𝑥0, 𝑥1, 𝑥2 . . . since 𝑛𝑖 → ∞ as
𝑖 → ∞). The computable function 𝑘, defined by the equation 𝑘(𝑥𝑖) = 𝑛𝑖, is then an
unbounded lower bound for Kolmogorov complexity. This contradicts Theorem 6.

<!-- page 23 -->

<!-- page 24 -->

Basic notions and notations
This section is intended for people who are already familiar with some notions
of Kolmogorov complexity and algorithmic randomness theory and want to take
a quick look at the terminology and notation used throughout this book. Other
readers can (and probably should) skip it and look back only when needed.
The set of all integer numbers is denoted by Z, the notation N refers to the
set of all non-negative integers (i.e. natural numbers), R stands for the set of all
reals. The set of all rational numbers is denoted by Q. Dyadic rationals are those
rationals having the form 𝑚/2𝑛 for some integer 𝑚 and 𝑛.
The cardinality of a set 𝐴 is denoted by |𝐴|.
When the base of the logarithmic function is omitted, it is assumed that the
base equals 2, thus log 𝑥 means the same as log2 𝑥 (as usual, ln 𝑥 denotes the natural
logarithm).
We use the notation ⌊𝑥⌋ for the integer part of a real number 𝑥 (the largest
integer number that is less than or equal to 𝑥). Similarly, ⌈𝑥⌉ denotes the smallest
integer number that is larger than or equal to 𝑥.
Order of magnitudes. The notation 𝑓 6 𝑔+𝑂(1), where 𝑓 and 𝑔 are expressions
containing variables, means that for some 𝑐 the inequality 𝑓 6 𝑔 + 𝑐 holds for all
values of variables. In a similar way we understand the expression 𝑓 6 𝑔 + 𝑂(ℎ)
(where ℎ is non-negative): it means that for some 𝑐 for all values of variables the
inequality 𝑓 6 𝑔 + 𝑐ℎ holds. The notation 𝑓 = 𝑔 + 𝑂(ℎ) (where ℎ in non-negative)
means that for some 𝑐 for all values of variables we have |𝑓 − 𝑔| 6 𝑐ℎ. In particular,
𝑓 = 𝑂(ℎ) holds if |𝑓 | 6 𝑐ℎ for some constant 𝑐; the notation 𝑓 = Ω(ℎ) means that
|𝑓 | > 𝑐ℎ for some constant 𝑐 > 0 (usually 𝑓 is positive). The notation 𝑓 = Θ(ℎ)
means that 𝑐1ℎ 6 |𝑓 | 6 𝑐2ℎ (again, usually 𝑓 is positive).
B denotes the set {0, 1}. Finite sequences of 0s and 1s are called binary strings.
The set of all binary strings is denoted by Ξ. If 𝐴 is a finite set (an alphabet) then
𝐴𝑛 denotes the set of all strings of length 𝑛 over the alphabet 𝐴, that is, the set
of all sequences of length 𝑛, whose terms belong to 𝐴. We denote by 𝐴* the set
of all strings over the alphabet 𝐴 (including the empty string Λ of length 0). For
instance, Ξ = B*. The length of a string 𝑥 is denoted by 𝑙(𝑥). The notation 𝑎𝑏
refers to the concatenation of strings 𝑎 and 𝑏, that is, the result of appending 𝑏
to 𝑎. We say that a string 𝑎 is a prefix of a string 𝑏 if 𝑏 = 𝑎𝑥 for some string 𝑥. We
say that 𝑎 is a suffix of a string 𝑏 if 𝑏 = 𝑥𝑎 for some string 𝑥. We say that 𝑎 is a
substring of 𝑏, if 𝑏 = 𝑥𝑎𝑦 for some strings 𝑥 and 𝑦 (in other words, 𝑎 is a suffix of
a prefix of 𝑏 or the other way around).
We consider also infinite sequences of zeros and ones and Ω denotes the set of
all such sequences. The set of infinite sequences of elements of a set 𝐴 is denoted
by 𝐴∞, thus Ω = B∞. For a finite sequence 𝑥 we use the notation Ω𝑥 for the set
of all infinite sequences that start with 𝑥 (i.e., have 𝑥 as a prefix); sets of this form
25

<!-- page 25 -->

26 BASIC NOTIONS AND NOTATIONS
are called intervals. The concatenation 𝑥𝜔 of a finite sequence 𝑥 and an infinite
sequence 𝜔 is defined in a natural way.
In some contexts it is convenient to consider finite and infinite sequences to-
gether. We use the notation Σ for the set of all finite and infinite sequences of zeros
and ones, i.e., Σ = Ξ ∪ Ω, and Σ𝑥 denotes the set of all finite and infinite extensions
of a string 𝑥.
We consider computable functions whose arguments and values are binary
strings. Unless it is stated otherwise functions are partial (not necessarily total).
A function 𝑓 is called computable if there is a machine (a program, an algorithm)
that for all 𝑥 such that 𝑓 (𝑥) is defined halts on input 𝑥 and outputs the result 𝑓 (𝑥)
and does not halt on all inputs 𝑥 outside the domain of 𝑓 . We also consider com-
putable functions whose arguments and values are finite objects of different type,
like natural numbers, integer numbers, finite graphs etc. We assume that finite
objects are encoded by binary strings. The choice of an encoding is not important
provided different encodings can be translated to each other. The latter means that
we can algorithmically decide whether a string is an encoding of an object and, if
this is the case, we can find an encoding of the same object with respect to the
other encoding.
Sometimes we consider computable functions of infinite objects, like real num-
bers or measures. Such considerations require rigorous definitions of the notion of
computability, which are provided when needed (see below).
A set of finite objects (binary strings, natural numbers etc.) is called computably
enumerable, or just enumerable, if there is a machine (a program, an algorithm)
without input that prints all elements from the set (and no other elements) with
arbitrary delays between printing consecutive elements. The algorithm is not re-
quired to halt even when the set is finite. The order in which the elements are
printed can be arbitrary.
A real number 𝛼 is computable if there exists an algorithm that computes 𝛼
with any given precision: for any given rational 𝜀 > 0 the algorithm must produce a
rational number at distance at most 𝜀 from 𝛼 (in this case we say that the algorithm
computes the number). A real number 𝛼 is lower semicomputable if it can be
represented as a limit of a non-decreasing computable sequence of rational numbers.
An equivalent definition: 𝛼 is lower semicomputable if the set of rational numbers
that are less than 𝛼 is enumerable. A sequence of real numbers is computable if
all its terms are computable, and given any 𝑛 we are able to find an algorithm
computing the 𝑛th number in the sequence. The notion of a lower semicomputable
sequence of reals is defined in an entirely similar way (for any given 𝑛 we have to
find an algorithm that lower semicomputes the 𝑛th number).
We consider measures (more specifically, probability measures, or probability
distributions) on Ω. Every measure can be identified by its values on intervals Ω𝑥.
So measures are identified with non-negative functions 𝑝 on strings which satisfy
the following two conditions: 𝑝(Λ) = 1 and 𝑝(𝑥) = 𝑝(𝑥0) + 𝑝(𝑥1) for all 𝑥. Such
measures are called measures on the binary tree. We consider also semimeasures
on the binary tree, which are probability measures on the space Σ of all finite and
infinite binary sequences. They correspond to functions 𝑝 such that 𝑝(Λ) = 1 and
𝑝(𝑥) > 𝑝(𝑥0)+𝑝(𝑥1). We consider also semimeasures on natural numbers, which are
defined as sequences {𝑝𝑖} of non-negative reals with∑︀ 𝑖∈N 𝑝𝑖 6 1. It is natural to

<!-- page 26 -->

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

<!-- page 27 -->

28 BASIC NOTIONS AND NOTATIONS
mutual information in random variables 𝜉 and 𝜂 and is denoted by 𝐼(𝜉 : 𝜂). A sim-
ilar notation 𝐼(𝑥 : 𝑦) is used in the algorithmic information theory. As 𝐼(𝑥 : 𝑦) is
commutative only up to a small error term, we usually say “the information in 𝑥
about 𝑦” and define this notion as 𝐶(𝑦) − 𝐶(𝑦 | 𝑥).

<!-- page 28 -->

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

<!-- page 29 -->

30 1. PLAIN KOLMOGOROV COMPLEXITY
As the optimal description mode is not worse than the identity function 𝑥 ↦ → 𝑥,
we obtain the inequality 𝐶(𝑥) 6 𝑙(𝑥) + 𝑂(1) (Theorem 2, p. 15).
Let 𝐴 be a partial computable function. Comparing the optimal description
mode 𝐷 with the description mode 𝑦 ↦ → 𝐴(𝐷(𝑦)), we conclude that
𝐶(𝐴(𝑥)) 6 𝐶(𝑥) + 𝑂(1),
showing the non-growth of complexity under algorithmic transformations (Theo-
rem 3, p. 15).
Using this inequality, we can define Kolmogorov complexity of other “finite
objects” like natural numbers, graphs, permutations, finite sets of strings, etc.,
that can be naturally encoded by binary strings.
For example, let us define the complexity of natural numbers. A natural num-
ber 𝑛 can be written in binary notation. Another way to represent a number by a
string is as follows. Enumerate all the binary strings in the lexicographical order
Λ, 0, 1, 00, 01, 10, 11, 000, 001, 010, 011, 100, . . .
using the natural numbers 0, 1, 2, 3, . . . as indexes. This enumeration is more con-
venient compared to binary representation, as it is a bijection. Every string can be
considered as an encoding of its index in this enumeration. Finally, one can also
encode a natural number 𝑛 by a string consisting of 𝑛 ones.
Using either of these three encodings we can define the complexity of 𝑛 as
the complexity of the string encoding 𝑛. Three resulting complexities of 𝑛 differ
at most by an additive constant. Indeed, for every pair of these encodings there
is an algorithm translating the first encoding into the second one. Applying this
algorithm, we increase the complexity at most by a constant. Note that anyway
the Kolmogorov complexity of binary strings is defined up to an additive constant,
so the choice of a computable encoding does not matter.
As the length of the binary representation of a natural number 𝑛 is equal to
log 𝑛 + 𝑂(1), the Kolmogorov complexity of 𝑛 is at most log 𝑛 + 𝑂(1). (By log we
denote binary logarithms.)
Here is another application of the non-growth of complexity under algorithmic
transformations. Let us show that deleting the last bit of a string changes its
complexity at most by a constant. Indeed, all three functions 𝑥 ↦ → 𝑥0, 𝑥 ↦ → 𝑥1,
𝑥 ↦ → (𝑥 without the last bit) are computable.
The same is true for the first bit. However this does not apply to every bit of
the string. To show this, consider the string 𝑥 consisting of 2𝑛 zeros, its complexity
is at most 𝐶(𝑛) + 𝑂(1) 6 log 𝑛 + 𝑂(1). (By log we always mean binary logarithm.)
There are 2𝑛 different strings obtained from 𝑥 by flipping one bit. At least one of
them has complexity 𝑛 or more. (Recall that the number of strings of complexity
less than 𝑛 does not exceed the number of descriptions of length less than 𝑛, which
is less than 2𝑛, Theorem 5, p. 18.)
Incrementing a natural number 𝑛 by 1 changes 𝐶(𝑛) at most by a constant.
This implies that 𝐶(𝑛) satisfies “Lipschitz property”: for some 𝑐 and for all 𝑚, 𝑛
we have |𝐶(𝑚) − 𝐶(𝑛)| 6 𝑐|𝑚 − 𝑛|.
1 Prove a stronger inequality: |𝐶(𝑚) − 𝐶(𝑛)| 6 |𝑚 − 𝑛| + 𝑐 for some 𝑐 and for
all 𝑚, 𝑛 ∈ N, and, moreover, |𝐶(𝑚) − 𝐶(𝑛)| 6 2 log |𝑚 − 𝑛| + 𝑐 (the latter inequality
assumes that 𝑚̸ = 𝑛).

<!-- page 30 -->

1.1. THE DEFINITION AND MAIN PROPERTIES 31
We have used several times the upper bound 2𝑛 for the number of strings 𝑥
with 𝐶(𝑥) < 𝑛. Note that, in contrast to other bounds, it involves no constants.
Nevertheless this bound has a hidden dependence on the choice of the optimal
description mode: if we switch to another optimal description mode, the set of
strings 𝑥 such that 𝐶(𝑥) < 𝑛 can change!
2 Show that the number of strings of complexity less than 𝑛 is in the range
[2𝑛−𝑐; 2𝑛] for some constant 𝑐 for all 𝑛. [Hint: the upper bound 2𝑛 is proved in
Introduction, the lower bound is implied by the inequality 𝐶(𝑥) 6 𝑙(𝑥) + 𝑐: the
complexity of all the strings of length less than 𝑛 − 𝑐 is less than 𝑛.]
Show that the number of strings of complexity exactly 𝑛 does not exceed 2𝑛
but can be much less: e.g., it is possible that this set is empty for infinitely many 𝑛.
[Hint: Change an optimal description mode by adding 0 or 11 to each description,
so that all descriptions have even length.]
3 Prove that the average complexity of strings of length 𝑛 is equal to 𝑛+𝑂(1).
[Hint: let 𝛼𝑘 denote the fraction of strings of complexity 𝑛 − 𝑘 among strings of
length 𝑛. Then the average compexity is by∑︀ 𝑘 𝑘𝛼𝑘 less than 𝑛. Use the inequality
𝛼𝑘 6 2−𝑘 and the convergence of the series∑︀ 𝑘/2𝑘.]
In the next statement we establish a formal relation between upper bounds of
complexity and upper bounds of cardinality.
Theorem 7. (a) The family of sets 𝑆𝑛 = {𝑥 | 𝐶(𝑥) < 𝑛} is enumerable and
|𝑆𝑛| < 2𝑛 for all 𝑛. Here |𝑆𝑛| denotes the cardinality of 𝑆𝑛.
(b) If 𝑉𝑛 (𝑛 = 0, 1, . . . ) is an enumerable family of sets of strings and |𝑉𝑛| < 2𝑛
for all 𝑛, then there exists 𝑐 such that 𝐶(𝑥) < 𝑛 + 𝑐 for all 𝑛 and all 𝑥 ∈ 𝑉𝑛.
In this theorem we use the notion of an enumerable family of sets. It is de-
fined as follows. A set of strings (or natural numbers, or other finite objects) is
enumerable (= computably enumerable = recursively enumerable) if there is an al-
gorithm generating all elements of this set in some order. This means that there
is a program that never terminates and prints all the elements of the set in some
order. The intervals between printing elements can be arbitrarily large; if the set is
finite, the program can print nothing after some time (unknown to the observer).
Repetitions are allowed but this does not matter since we can filter the output and
delete the elements that have already been printed.
For example, the set of all 𝑛 such that the decimal expansion of √2 has exactly
𝑛 consecutive nines is enumerable. The following algorithm generates the set: com-
pute decimal digits of √2 starting with the most significant ones. Once a sequence
of consecutive 𝑛 nines surrounded by non-nines is found, print 𝑛 and continue.
A family of sets 𝑉𝑛 is called enumerable if the set of pairs {⟨𝑛, 𝑥⟩ | 𝑥 ∈ 𝑉𝑛}
is enumerable. This implies that each of the sets 𝑉𝑛 is enumerable. Indeed, to
generate elements of the set 𝑉𝑛 for a fixed 𝑛 we run the algorithm enumerating the
set {⟨𝑛, 𝑥⟩ | 𝑥 ∈ 𝑉𝑛} and print the second components of all the pairs that have 𝑛
as the first component. However, the converse statement is not true. For instance,
assume that 𝑉𝑛 is finite for every 𝑛. Then every 𝑉𝑛 is enumerable, but at the same
time it may happen that the set {⟨𝑛, 𝑥⟩ | 𝑥 ∈ 𝑉𝑛} is not enumerable (say 𝑉𝑛 = {0}
if 𝑛 ∈ 𝑆 and 𝑉𝑛 = ∅ otherwise, where 𝑆 is any non-enumerable set of integers).
One can verify that a family is enumerable if and only if there is an algorithm that
given any 𝑛 finds a program generating 𝑉𝑛. A detailed study of enumerable sets
can be found in every textbook on computability theory, for instance, in [182].

<!-- page 31 -->

32 1. PLAIN KOLMOGOROV COMPLEXITY
Proof. Let us prove the theorem. First, we need to show that the set
{⟨𝑛, 𝑥⟩ | 𝑥 ∈ 𝑆𝑛} = {⟨𝑛, 𝑥⟩ | 𝐶(𝑥) < 𝑛},
where 𝑛 is a natural number and 𝑥 is a binary string, is enumerable.
Let 𝐷 be the optimal decompressor used in the definition of 𝐶. Perform in
parallel the computations of 𝐷 on all the inputs. (Say, for 𝑘 = 1, 2, . . . we make 𝑘
steps of 𝐷 on 𝑘 first inputs.) If we find that 𝐷 halts on some 𝑦 and returns 𝑥, the
generating algorithm outputs the pair ⟨𝑙(𝑦) + 1, 𝑥⟩. Indeed, this implies that the
complexity of 𝑥 is less than 𝑙(𝑦) + 1, as 𝑦 is a description of 𝑥. Also it outputs all
the pairs ⟨𝑙(𝑦) + 2, 𝑥⟩, ⟨𝑙(𝑦) + 3, 𝑥⟩ . . . in parallel to printing of other pairs.
For those familiar with computability theory, this proof can be compressed to
one line:
𝐶(𝑥) < 𝑛 ⇔ ∃𝑦 (𝑙(𝑦) < 𝑛 ∧ 𝐷(𝑦) = 𝑥).
(The set of pairs ⟨𝑥, 𝑦⟩ such that 𝐷(𝑦) = 𝑥 is enumerable, being the graph of
a computable function. The operations of intersection and projection preserve
enumerability.)
The converse implication is a bit harder. Assume that 𝑉𝑛 is an enumerable
family of finite sets of strings and |𝑉𝑛| < 2𝑛. Fix an algorithm generating the
set {⟨𝑛, 𝑥⟩ | 𝑥 ∈ 𝑉𝑛}. Consider the description mode 𝐷𝑉 that deals with strings
of length 𝑛 in the following way. Strings of length 𝑛 are used as descriptions of
strings in 𝑉𝑛. More specifically, let 𝑥𝑘 be the 𝑘th string in 𝑉𝑛 in the order the pairs
⟨𝑛, 𝑥⟩ appear while generating the set {⟨𝑛, 𝑥⟩ | 𝑥 ∈ 𝑉𝑛}. (We assume there are no
repetitions, so 𝑥0, 𝑥1, 𝑥2 . . . are distinct.) Let 𝑦𝑘 be the 𝑘th string of length 𝑛 in
the lexicographical order. Then 𝑦𝑘 is a description of 𝑥𝑘, that is, 𝐷(𝑦𝑘) = 𝑥𝑘. As
|𝑉𝑛| < 2𝑛, every string in 𝑉𝑛 gets a description of length 𝑛 with respect to 𝐷.
We need to verify that the description mode 𝐷𝑉 defined in this way is com-
putable. To compute 𝐷𝑉 (𝑦) we find the index 𝑘 of 𝑦 in the lexicographical ordering
of strings of length 𝑙(𝑦). Then we run the algorithm generating pairs ⟨𝑛, 𝑥⟩ such
that 𝑥 ∈ 𝑉𝑛 and wait until 𝑘 different pairs having the first component 𝑙(𝑦) appear.
The second component of the last of them is 𝐷𝑉 (𝑦).
By construction, for all 𝑥 ∈ 𝑉𝑛 we have 𝐶𝐷𝑉 (𝑥) 6 𝑛. Comparing 𝐷𝑉 with the
optimal description mode we see that there is a constant 𝑐 such that 𝐶(𝑥) < 𝑛 + 𝑐
for all 𝑥 ∈ 𝑉𝑛. Theorem 7 is proven. 
The intuitive meaning of Theorem 7 is as follows. The assertions “the number
of strings with certain property is small” (is less than 2𝑖) and “all the strings with
certain property are simple” (have complexity less than 𝑖) are equivalent provided
the property under consideration is enumerable and provided the complexity is
measured up to an additive constant (and the number of elements is measured up
to a multiplicative constant).
Theorem 7 can be reformulated as follows. Let 𝑓 (𝑥) be a function defined on
all binary strings and taking as values natural numbers and a special value +∞.
We call 𝑓 upper semicomputable, or enumerable from above, if there is a computable
function ⟨𝑥, 𝑘⟩ ↦ → 𝐹 (𝑥, 𝑘) defined on all strings 𝑥 and all natural numbers 𝑘 such
that
𝐹 (𝑥, 0) > 𝐹 (𝑥, 1) > 𝐹 (𝑥, 2) > . . .
and
𝑓 (𝑥) = lim
𝑘→∞ 𝐹 (𝑥, 𝑘),

<!-- page 32 -->

1.1. THE DEFINITION AND MAIN PROPERTIES 33
for all 𝑥. The values of 𝐹 are natural numbers as well as the special constant +∞.
The requirements imply that for every 𝑘 the value 𝐹 (𝑥, 𝑘) is an upper bound of
𝑓 (𝑥). This upper bound becomes more precise as 𝑘 increases. For every 𝑥 there
is a 𝑘 for which this upper bound is tight. However, we do not know the value of
that 𝑘. (If there is an algorithm that given any 𝑥 finds such 𝑘, then the function 𝑓
is computable.) Evidently, any computable function is upper semicomputable.
A function 𝑓 is upper semicomputable if and only if the set
𝐺𝑓 = {⟨𝑥, 𝑛⟩ | 𝑓 (𝑥) < 𝑛}
is enumerable. This set is sometimes called the “upper graph of 𝑓 ”, which explains
the strange names “upper semicomputable” and “enumerable from above”.
Let us verify this. Assume that a function 𝑓 is upper semicomputable. Let
𝐹 (𝑥, 𝑘) be the function from the definition of semicomputability. Then we have
𝑓 (𝑥) < 𝑛 ⇔ ∃𝑘 𝐹 (𝑥, 𝑘) < 𝑛.
Thus, performing in parallel the computations of 𝐹 (𝑥, 𝑘) for all 𝑥 and 𝑘, we can
generate all the pairs in the upper graph of 𝑓 .
Assume now that the set 𝐺𝑓 is enumerable. Fix an algorithm enumerating this
set. Then define 𝐹 (𝑥, 𝑘) as the best upper bound of 𝑓 obtained after 𝑘 steps of
generating elements in 𝐺𝑓 . That is, 𝐹 (𝑥, 𝑘) is equal to the minimal 𝑛 such that
the pair ⟨𝑥, 𝑛 + 1⟩ has been printed after 𝑘 steps. If there is no such pair, let
𝐹 (𝑥, 𝑘) = +∞.
Using the notion of an upper semicomputable function we can reformulate
Theorem 7 as follows.
Theorem 8. (a) The function 𝐶 is upper semicomputable and
|{𝑥 | 𝐶(𝑥) < 𝑛}| < 2𝑛
for all 𝑛.
(b) If a function 𝐶′ is upper semicomputable and |{𝑥 | 𝐶′(𝑥) < 𝑛}| < 2𝑛 for
all 𝑛, then 𝐶(𝑥) 6 𝐶′(𝑥) + 𝑐 for some 𝑐 and for all 𝑥.
Note that the upper bound 2𝑛 of the cardinality of |{𝑥 | 𝐶′(𝑥) < 𝑛}| in item
(b) can be replaced by a weaker upper bound 𝑂(2𝑛).
Theorem 8 allows to define Kolmogorov complexity as a minimal (up to an
additive constant) upper semicomputable function 𝑘 that satisfies the inequality
|{𝑥 | 𝑘(𝑥) < 𝑛}| = 𝑂(2𝑛).
One can replace the requirement of minimality in this definition by some other
properties of 𝐶. In this way we obtain the following “axiomatic” definition of
Kolmogorov complexity [172]:
Theorem 9. Let 𝑘 be a function defined on binary strings and taking natural
values. Assume that 𝑘 satisfies the following properties:
(a) 𝑘 is upper semicomputable; [enumerability axiom]
(b) for every partial computable function 𝐴 from Ξ to Ξ the inequality
𝑘(𝐴(𝑥)) 6 𝑘(𝑥) + 𝑐
is valid for some 𝑐 and all 𝑥 in the domain of 𝐴; [complexity non-increase axiom]
(c) the number of strings 𝑥 such that 𝑘(𝑥) < 𝑛 is in the range [2𝑛−𝑐1 ; 2𝑛+𝑐2 ]
for some 𝑐1, 𝑐2 and for any 𝑛. [calibration axiom]

<!-- page 33 -->

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

<!-- page 34 -->

1.2. ALGORITHMIC PROPERTIES 35
satisfies the inequality 𝐶(𝑦) 6 𝑛 − log 𝑛 + 𝑐. [Hint. For a given natural 𝑘 consider
a Boolean matrix of size 𝑘 × (2𝑘 − 1) whose columns are all nonzero strings of
length 𝑘. (Such matrix is used for Hamming codes.) Consider the linear mapping
B2𝑘 −1 → B𝑘 defined by this matrix, where B denotes the field {0, 1}. It is easy to
verify that for every vector 𝑥 one can flip one bit in 𝑥 so that the resulting string 𝑦
is in the kernel of this mapping, and the elements of the kernel have complexity at
most 2𝑘 − 𝑘 + 𝑂(1). This gives the desired result for 𝑛 = 2𝑘 − 1; if 𝑛 has not the
form 2𝑘 − 1, we can flip one of the first 2𝑘 − 1 bits for an appropriate 𝑘.]
### 1.2. Algorithmic properties
The function 𝐶 is upper semicomputable. On the other hand, it is not com-
putable and, moreover, it has no unbounded computable lower bounds (Theorem 6,
p. 19).
This implies that all optimal description modes are necessarily non-total, that
is, some strings describe nothing. Indeed, if a description mode 𝐷 is total then we
can compute 𝐶𝐷 (𝑥) just by trying all descriptions in the lexicographical order until
we find the shortest one.
At first glance, this contradicts to our intuition: the bigger the domain of 𝐷
is, the better 𝐷 is. If optimal decompressor 𝐷 is undefined on some string 𝑦 then
we can define another description mode 𝐷′ as follows. Let 𝐷′(𝑦) be equal to a
string 𝑧 of complexity (with respect to 𝐷) greater than 𝑙(𝑦) and let 𝐷′ coincide
with 𝐷 on all other strings. The description mode 𝐷′ is a bit better than 𝐷, as the
complexity of all strings except 𝑧 remains the same while the complexity of 𝑧 has
been decreased.
There is no formal contradiction here, as 𝐷 is still not worse than 𝐷′ (they differ
only at one point, the difference between the complexities is bounded by a constant,
and both 𝐷 and 𝐷′ are optimal). However, this is still a bit strange. This observa-
tion was made by Yu. Manin in his book “Computable and non-computable” [113]
(by the way, in this book he also discussed the computational power of quantum
mechanics long before quantum computing became fashionable).
A similar argument shows that the domain of every optimal description mode
is undecidable. (The set of strings is called decidable, or computable, if there is an
algorithm that for any given string decides whether it belongs to the set or not.)
Indeed, if there were an algorithm deciding whether 𝐷(𝑥) is defined or not, then
there would be a total computable extension of 𝐷 (for example, let 𝐷(𝑥) = 0 for all
𝑥 outside the domain of 𝐷). This extension would be a total optimal description
mode, but this is impossible as we have seen.
As a byproduct we get an algorithm whose domain is undecidable. This is one
of the central theorems in computability theory (see, for example, [182]).
In general the notion of Kolmogorov complexity has a lot of connections with
computability theory. Recently many interesting facts were discovered, see [146,
49]. We consider here only two basic examples (a simple set of simple strings, and
the complexity of large numbers).
1.2.1. Simple strings and simple sets. In this section, the word “simple”
has two unrelated meanings. First, when applied to strings, it means that the
Kolmogorov complexity of the string is small. Second, it is applied to sets of

<!-- page 35 -->

36 1. PLAIN KOLMOGOROV COMPLEXITY
strings. The notion of a simple set was introduced by an American logician Emil
Post and has no relation to Kolmogorov complexity.
Definition. An enumerable set 𝐴 is simple (according to Post) if its comple-
ment is infinite but has no infinite enumerable subset.
Call a string 𝑥 “simple” if 𝐶(𝑥) < 𝑙(𝑥)/2.
Theorem 10. The set of all “simple” strings is simple in the sense of Post.
Proof. That set 𝑆 of all “simple” strings is enumerable. Indeed, the function
𝐶 is upper semicomputable, and if 𝐶(𝑥) is less than |𝑥|/2, this can be seen while
approximating 𝐶(𝑥) from above.
The number of strings of complexity less than 𝑛/2 does not exceed 2𝑛/2. There-
fore the fraction of “simple” strings among strings of length 𝑛 is negligible, and the
complement of 𝑆 is infinite.
Assume now that the complement of 𝑆 has an infinite enumerable subset 𝑈 . We
can use 𝑈 to obtain a computable unbounded lower bound of 𝐶. To find a string of
complexity greater than 𝑡 we can generate elements of 𝑈 until we find a string 𝑢𝑡 of
length greater than 2𝑡. As 𝑈 is infinite, there is such a string. The complexity of 𝑢𝑡
is greater than 𝑡, otherwise 𝑢𝑡 is simple. Without loss of generality we can assume
that the strings 𝑢𝑡, 𝑡 = 1, 2, . . . are pairwise different. Thus the function 𝑢𝑡 ↦ → 𝑡
is a computable unbounded lower bound for 𝐶. This contradicts to Theorem 6
(page 19). 
Note that the choice of the threshold 𝑙(𝑥)/2 in the definition of a simple string
was not essential. The proof of Theorem 10 would work as well with 𝑙(𝑥) − 1 or
log log 𝑙(𝑥) in place of 𝑙(𝑥)/2.
1.2.2. Complexity of large numbers. Let us identify a natural number 𝑚
with the binary string having index 𝑚 in the standard enumeration of binary strings.
In this way 𝐶 becomes a function of a natural argument. The function 𝐶(𝑚) goes
to infinity as 𝑚 → ∞. Indeed, for all 𝑛 there are only finitely many integers of
complexity less than 𝑛. However, the convergence is not effective. That is, there
is no algorithm that for every given 𝑛 finds a number 𝑁 such that the complexity
of 𝑁 and of all larger numbers is bigger than 𝑛. Indeed, such an algorithm would
provide an effective way to describe the number 𝑁 , whose complexity is at least 𝑛,
by log 𝑛 + 𝑂(1) bits. We have seen this in the proof of Theorem 6 (p. 19).
In this section, we study in detail the rate of convergence of 𝐶 to infinity.
Following Chaitin [31], we consider for every natural 𝑛 the largest number B (𝑛)
whose complexity is at most 𝑛:
B (𝑛) = max{𝑚 ∈ N | 𝐶(𝑚) 6 𝑛}
The function 𝑛 ↦ → B (𝑛) may be called the modulus of the convergence of 𝐶(𝑚) to
infinity. Indeed, 𝐾(𝑥) > 𝑛 for all 𝑥 > B (𝑛) (and B (𝑛) is the minimal number with
this property). Note also that it can happen (for small values of 𝑛) that 𝐶(𝑚) > 𝑛
for all 𝑚. In this case we let B (𝑛) = −1.
The function B can be considered as an inverse function to the function
𝐶>(𝑁 ) = min{𝐶(𝑚) | 𝑚 > 𝑁 }.
The function 𝐶> grows very slowly. It takes the value 𝑛 between 𝐵(𝑛 − 1) and
𝐵(𝑛), more precisely, on the interval (B (𝑛 − 1), B (𝑛)]. The slow increase of 𝐶>

<!-- page 36 -->

1.2. ALGORITHMIC PROPERTIES 37
𝑚
𝐶(𝑚)
𝑛 − 1
𝐵(𝑛 − 1)
𝑛
𝐵(𝑛) = 𝐵(𝑛 + 1)
𝑛 + 1
Figure 1. The definition of B (𝑛): the value 𝐶(𝑚) does not exceed
𝑛−1 for 𝑚 = B (𝑛−1) (the case when 𝐶(B (𝑛−1)) = 𝑛−1 is shown),
and 𝐶(𝑚) > 𝑛 for all 𝑚 > B (𝑛 − 1). At the point 𝑚 = B (𝑛)
the value of 𝐶 does not exceed 𝑛 (the case when 𝐶(B (𝑛)) = 𝑛
is shown), and 𝐶(𝑚) > 𝑛 for all 𝑚 > B (𝑛). The case when
𝐶(𝑚) is even greater than 𝑛 + 1 for all 𝑚 > B (𝑛) is shown, thus
B (𝑛 + 1) = B (𝑛). For 𝑚 ∈ (B (𝑛 − 1), B (𝑛)] the value of the
function 𝐶>(𝑚) is equal to 𝑛.
corresponds to the fast increase of B . The latter can be illustrated by the following
result.
Theorem 11. Let 𝑓 be a computable function from N to N. Then B (𝑛) > 𝑓 (𝑛)
for all but finitely many 𝑛.
Note that 𝑓 may be a partial function. In this case we claim that B (𝑛) > 𝑓 (𝑛)
for all sufficiently large 𝑛 that are in the domain of 𝑓 .
Proof. As algorithmic transformations do not increase complexity, for some
constant 𝑐 for all 𝑛 we have
𝐶(𝑓 (𝑛)) 6 𝐶(𝑛) + 𝑂(1) 6 log 𝑛 + 𝑐.
On the other hand, the definition of B and the inequality 𝑓 (𝑛) > B (𝑛) imply
𝐶(𝑓 (𝑛)) > 𝑛. Thus
𝑛 < 𝐶(𝑓 (𝑛)) 6 log 𝑛 + 𝑐
whenever 𝑓 (𝑛) > B (𝑛). This can happen only for finitely many 𝑛. 
Let us reformulate the definition of B (𝑛) as follows. Let 𝐷 be the optimal
description mode used in the definition of Kolmogorov complexity. Then B (𝑛) is
the maximal value of 𝐷 on strings of length at most 𝑛:
B (𝑛) = max{𝐷(𝑥) | 𝑙(𝑥) 6 𝑛}.
Recall that we identify natural numbers and binary strings and consider the values
of 𝐷 as natural numbers. The minimum of the empty set is defined as −1.
Consider now any partial computable function 𝑑 : Ξ → N in place of 𝐷 and let
B 𝑑(𝑛) = max{𝑑(𝑥) | 𝑙(𝑥) 6 𝑛 and 𝑑(𝑥) is defined}.
Next theorem shows that the function B is the largest function among all functions
B 𝑑, in the following sense:

<!-- page 37 -->

38 1. PLAIN KOLMOGOROV COMPLEXITY
Theorem 12. For every function 𝑑 there is a constant 𝑐 such that
B 𝑑(𝑛) 6 B (𝑛 + 𝑐)
for all 𝑛.
Proof. For every 𝑥 of length at most 𝑛 the complexity of 𝑑(𝑥) is less than
𝑛 + 𝑐 for some constant 𝑐. Indeed, the complexity of 𝑑(𝑥) exceeds at most by a
constant the complexity of 𝑥, which is less than 𝑛 + 𝑂(1). Hence 𝑑(𝑥) does not
exceed the largest number of complexity 𝑛 + 𝑐 or less, i.e., B (𝑛 + 𝑐). 
This (trivial) observation is useful in the following special case. Let 𝑀 be an
algorithm and let 𝑋 be a set of binary strings. A halting problem for 𝑀 restricted
to 𝑋 is the following problem: given a string 𝑥 ∈ 𝑋, find out whether 𝑀 terminates
on 𝑥 or not.
A classical result in computability theory states that for some algorithm 𝑀 the
unrestricted halting problem (𝑋 = Ξ) for 𝑀 is undecidable.
We are interested now in the case when 𝑋 is the set of all strings of bounded
length. Fix some algorithm 𝑀 and consider the running time 𝑡(𝑥) of 𝑀 for some
input 𝑥. If 𝑀 does not halt on 𝑥, then 𝑡(𝑥) is undefined. Thus the domains of 𝑡
and 𝑀 coincide. By definition, B 𝑡(𝑛) is the maximal running time of 𝑀 on inputs
of length at most 𝑛. If we know B 𝑡(𝑛) or any larger number 𝑚, we can solve the
halting problem for 𝑀 and every input 𝑥 of length at most 𝑛: Run 𝑀 on input 𝑥;
if the computation does not terminate after 𝑚 steps, it never terminates.
We have seen that B 𝑡(𝑛) 6 B (𝑛 + 𝑐) for some constant 𝑐 (depending on 𝑀 ).
Therefore the knowledge of B (𝑛 + 𝑐) or any greater number is enough to solve the
halting problem of 𝑀 on inputs of length at most 𝑛. In other words, the following
holds:
Theorem 13. For every algorithm 𝑀 there is a constant 𝑐 and another al-
gorithm 𝐴 having the following property. For every 𝑛 and for every number 𝑡 >
B (𝑛 + 𝑐) the algorithm 𝐴, given 𝑛 and 𝑡, produces the list of all strings 𝑥 of length
at most 𝑛 such that 𝑀 halts on input 𝑥.
This theorem says that the halting problem for inputs of length at most 𝑛 is
reducible to the problem of finding a number greater than B (𝑛 + 𝑐).
If 𝑀 is the optimal decompressor 𝐷 then the converse is also true: given 𝑛 and
the list of all strings 𝑥 of length at most 𝑛 in the domain of 𝐷 we can find B (𝑛).
Continuing this argument, we can prove the following result:
Theorem 14. Let BB (𝑛) denote the maximal running time of the optimal
decompressor 𝐷 on strings of length at most 𝑛 (in the domain of 𝐷). Then
BB (𝑛) 6 B (𝑛 + 𝑐) and B (𝑛) 6 BB (𝑛 + 𝑐)
for some 𝑐 and all 𝑛.
Proof. Let 𝛼𝑛 be the most time-consuming description of length at most 𝑛,
that is, the string 𝑥 of length at most 𝑛 in the domain of 𝐷 that maximizes the
running time of 𝐷 on 𝑥. Knowing 𝑛 and 𝛼𝑛, one can generate the list of all strings
of length at most 𝑛 in the domain of 𝐷, and hence the number BB (𝑛). Both 𝑛 and
𝛼𝑛 can be encoded in one string of length 𝑛 + 1, the string 0 . . . 01𝛼𝑛 (there are
𝑛 − 𝑙(𝛼𝑛) zeros in the beginning). Therefore, the Kolmogorov complexity of BB (𝑛)
is at most 𝑛 + 𝑂(1), and BB (𝑛) 6 B (𝑛 + 𝑐) for some 𝑐 and all 𝑛.

<!-- page 38 -->

1.2. ALGORITHMIC PROPERTIES 39
Let us prove the second inequality of the theorem showing that every 𝑡 > BB (𝑛)
has complexity at least 𝑛 − 𝑂(1). Assume that 𝑡 has a description 𝑢 of length 𝑘; we
need to show that 𝑘 > 𝑛−𝑂(1). Knowing 𝑢 and 𝑛, one can effectively obtain a string
of complexity greater than 𝑛. Indeed, we reconstruct 𝑡 (from 𝑢) and wait 𝑡 steps for
every description of size at most 𝑛. This gives us all strings of complexity at most
𝑛, and we can take some other string. By definition of B (𝑛) we conclude that the
pair (𝑢, 𝑛) has complexity at least 𝑛 − 𝑂(1). On the other hand, this pair can be
described using 𝑘+𝑂(log(𝑛−𝑘)) bits if we join the self-delimited description of 𝑛−𝑘
and 𝑢. Therefore, 𝑘 +𝑂(log(𝑛−𝑘)) > 𝑛−𝑂(1), and (𝑛−𝑘)−𝑂(log(𝑛−𝑘)) 6 𝑂(1),
therefore 𝑛 − 𝑘 6 𝑂(1). (We assumed that 𝑛 > 𝑘, otherwise there is nothing to
prove.) 
This theorem shows that, within to an additive constant in the argument, B (𝑛)
is the maximal running time of the optimal decompressor on descriptions of length
at most 𝑛. A similar function appeared in the literature under the name of “busy
beaver function”. It was introduced by T. Rad´o [149] and is defined usually as the
maximal number of 1s on the tape of Turing machine with 𝑛 states and binary tape
alphabet (1 and blank) after it terminates (starting with blank tape).
More generally, given 𝑛 and any object from the following list we can find any
other object from the list for a little bit smaller value of 𝑛:
(a): the list of all strings of Kolmogorov complexity at most 𝑛 with their
Kolmogorov complexities;
(b): the number of such strings;
(c): B (𝑛);
(d): BB (𝑛);
(e): the list of all strings of length at most 𝑛 in the domain of the optimal
decompressor (the halting problem for the optimal decompressor restricted
to inputs of length at most 𝑛);
(f ): the number of such strings;
(g): the most time-consuming input of length at most 𝑛 for the optimal
decompressor;
(h): the graph 𝑇𝑛 of the function 𝐶(𝑥) on strings 𝑥 of length 𝑛;
(i): the lexicographically first string 𝛾𝑛 of length 𝑛 with Kolmogorov com-
plexity at least 𝑛 (it exists since the number of strings of complexity less
than 𝑛 is less than 2𝑛).
More specifically, the following statement holds.
Theorem 15. The complexity of every object in (a)–(i) is equal to 𝑛 + 𝑂(1).
These objects are equivalent to each other in the following sense: Let 𝑋𝑛 and 𝑌𝑛
are objects described in two items among (a)–(i). Then there is a constant 𝑐 and
an algorithm that given 𝑛 and 𝑋𝑛 finds 𝑌𝑛−𝑐.
Proof. The equivalence of (d), (e), (f) and (g) is easy. Each of the objects (d),
(e), (f) and (g) together with 𝑛 determines the list of all terminating computations
of the optimal decompressor 𝐷 on strings of length at most 𝑛. Indeed, knowing
BB (𝑛) we can run 𝐷 on all inputs of length at most 𝑛 for BB (𝑛) steps. Knowing
(e), that is, the list of strings of length at most 𝑛 in the domain of 𝐷, we can run
𝐷 on all those strings until all the computations terminate (and we know that this
happens). Knowing (f), the number of strings of length at most 𝑛 on which 𝐷
terminates, we run 𝐷 on all strings of length at most 𝑛 until the desired number

<!-- page 39 -->

40 1. PLAIN KOLMOGOROV COMPLEXITY
of computations do terminate. Knowing the string (g), we run 𝐷 on that string,
count the number of steps 𝑡 and then run 𝐷 on all other strings of length at most
𝑛 for 𝑡 steps.
Conversely, the list of all halting computations of the optimal decompressor 𝐷
on strings of length at most 𝑛 together with 𝑛 identifies each of the objects (d)–(g),
as well as the objects (a)–(c). Therefore, by transitivity (which is easy to check)
all the objects (d)–(g) are equivalent.
Let us prove now that (a)–(c) are equivalent to each other and equivalent to
(d)–(g). Given the list of strings of complexity at most 𝑛 we can find the number of
them (so (a)→(b)) and the largest number of complexity at most 𝑛 (so (a)→(c)).
It is not that easy to find (a) given (b) and 𝑛. Given 𝑛 and the number of strings
of complexity at most 𝑛 we can reconstruct the list of these strings (generating them
until we obtain the desired number of strings), and find a maximal number among
them ((b)→(c)). But we still do not know Kolmogorov complexity of the generated
strings. We will prove the implication (c)→(a) indirectly, by showing (c)→(d);
we know already that (d) implies (a). This will prove that all objects (a)–(g) are
equivalent.
The implication (c)→(d) follows from Theorem 14. We know that B (𝑛) is an
upper bound for BB (𝑛 − 𝑐) (for appropriate 𝑐). Thus, given 𝑛 and B (𝑛), we can
find BB (𝑛 − 𝑐) as follows: run 𝐷 on all inputs of length at most 𝑛 − 𝑐 within B (𝑛)
steps. Then find BB (𝑛 − 𝑐) as the number of steps in the longest run.
It remains to consider the objects (h) and (i). The implication (a)→(h) is easy.
Indeed, for some constant 𝑐 the complexity of every string of length 𝑛 − 𝑐 does not
exceed 𝑛. If we know the list (a) and 𝑛, then removing all the strings of length
different from 𝑛 − 𝑐 from the list, we get (h) for 𝑛 − 𝑐.
The conversion (h)→(i) is straightforward.
Thus it remains to prove (i)→(a). It is enough to show that given the lex-
icographically first string 𝛾𝑛 of length 𝑛 and complexity at least 𝑛 we can find
BB (𝑛 − 𝑂(1)) or a number greater than BB (𝑛 − 𝑂(1)). This can be done as
follows.
Given 𝛾𝑛 find 𝑛 and for each string 𝑥 of length 𝑛 preceding 𝛾𝑛 in the lexicograph-
ical order find a description 𝑝𝑥 of 𝑥 that has length 𝑛 or less, and find out the running
time 𝑡𝑥 of 𝐷 on 𝑝𝑥. (Note that 𝑝𝑥 may be not the shortest description of 𝑥.) Let 𝑇
be the maximum of 𝑡𝑥 for those 𝑥. We claim that 𝑇 > BB (𝑛 − 𝑐) for some 𝑐 that
does not depend on 𝑛. Assume that this inequality is false, that is, 𝑇 6 BB (𝑛 − 𝑐).
We will prove that then 𝑐 is small. Consider the most time-consuming description
𝛼𝑛−𝑐 of length at most 𝑛 − 𝑐; let 𝑛 − 𝑐 − 𝑑 be its length. Given 𝛼𝑛−𝑐 and 𝑐 + 𝑑 we
can find 𝑛 and BB (𝑛 − 𝑐). From this we can find 𝛾𝑛: run 𝐷 on all strings of length
at most 𝑛 within BB (𝑛 − 𝑐) steps. Consider all the strings of length 𝑛 for which
we have found descriptions of length 𝑛 or less. Then 𝛾𝑛 is the lexicographically
first remaining string (since 𝑇 6 BB (𝑛 − 𝑐) according to our assumption). As the
complexity of 𝛾𝑛 is at least 𝑛 we have 𝑛 6 𝐶(𝛾𝑛) 6 (𝑛 − 𝑐 − 𝑑) + 2 log(𝑐 + 𝑑) + 𝑂(1),
hence (𝑐 + 𝑑) = 𝑂(1).
We have thus proven the equivalence of objects (a)–(h). It remains to prove
that complexity of each of them is 𝑛 + 𝑂(1).
Let 𝑋𝑛 be one of objects (a)–(h). We have just proven that 𝑋𝑛 can be obtained
from 𝛾𝑛+𝑐 and 𝑛 (actually, we do not need 𝑛, as 𝑛 = 𝑙(𝛾𝑛+𝑐) − 𝑐). Therefore,
𝐶(𝑋𝑛) 6 𝐶(𝛾𝑛+𝑐) + 𝑂(1) 6 𝑛 + 𝑂(1).

<!-- page 40 -->

1.2. ALGORITHMIC PROPERTIES 41
To prove the lower bound of 𝐶(𝑋𝑛) let 𝑛 − 𝑑 be the complexity of 𝑋𝑛. For
some constant 𝑐 the string 𝛾𝑛−𝑐 can be obtained from the shortest description of
𝑋𝑛 of length 𝑛 − 𝑑 and from 𝑑 (note that 𝑛 can be retrieved from the length of
the shortest description and 𝑑). Thus, 𝑛 − 𝑐 6 𝐶(𝛾𝑛−𝑐) 6 (𝑛 − 𝑑) + 2 log 𝑑 + 𝑂(1).
Therefore 𝑑 6 2 log 𝑑 + 𝑐 + 𝑂(1) and hence 𝑑 = 𝑂(1). 
8 The objects in Theorem 15 depend on the choice of the optimal decompres-
sor. In the proof we assumed that the same optimal decompressor is used in all the
items (a)–(h). Prove that the statement of the theorem remains true if different
decompressors are used.
9 Prove that the complexity of all the objects in Theorem 15 becomes 𝑂(log 𝑛)
if we relativize the definition of Kolmogorov complexity by 0′, that is, if we allow
the decompressor to query the oracle for the halting problem.
We have seen that there exist a constant 𝑐 and an algorithm 𝐴 that given the
string 𝛾𝑛 solves the halting problem for the optimal decompressor on inputs of
length at most 𝑛 − 𝑐. This means that given an “oracle” that finds 𝛾𝑛 for every
given 𝑛 we can solve the halting problem. The same can be done given an oracle
deciding whether a given string 𝑥 is “incompressible”, that is, 𝐶(𝑥) > 𝑙(𝑥). Indeed,
using that oracle we can find 𝛾𝑛 by probing all strings of length 𝑛.
Using the terminology of computability theory, we can say that halting problem
is Turing reducible to the set of incompressible strings (or its complement, the set
of compressible strings). This implies that halting problem is also reducible to the
“upper graph” of 𝐶, that is, to the set {⟨𝑥, 𝑘⟩ | 𝐶(𝑥) < 𝑘}. Using the terminology
of computability theory, we say that the set of compressible strings (as well as the
upper graph of 𝐶) is Turing complete in the class of enumerable sets (this means
that it is enumerable and that the halting problem is Turing reducible to it).
10 Find some upper bound for the number of oracle queries for the set
{⟨𝑥, 𝑘⟩ | 𝐶(𝑥) < 𝑘}
needed to solve the halting problem for a fixed machine 𝑀 and for all strings of
length at most 𝑛.
11 Let 𝑓 be a computable partial function from N to N. Prove that there
is a constant 𝑐 such that for all 𝑛 such that 𝑓 (B (𝑛)) is defined the inequality
B (𝑛 + 𝑐) > 𝑓 (B (𝑛)) is true. [Hint: the complexity of 𝑓 (B (𝑛)) is at most 𝑛 + 𝑂(1).]
12 Call a set 𝑈 𝑟-separable [136] if every enumerable set 𝑉 disjoint with 𝑈
can be separated from 𝑈 by a decidable set, that is, there is a decidable set 𝑅 that
includes 𝑉 and is disjoint with 𝑈 .
(a) Prove that the the set {⟨𝑥, 𝑘⟩ | 𝐶(𝑥) < 𝑘} (the upper graph of 𝐶) is an
𝑟-separable set. The set of compressible strings is 𝑟-separable, too. [Hint: assume
that the upper graph of 𝐶 is disjoint with some enumerable set 𝑉 . The set of
the second components of pairs in 𝑉 is finite, otherwise we get an unbounded
computable lower bound for 𝐶. That is, 𝑉 is included in a horizontal strip of finite
height. The intersection of the strip with the upper graph is finite.]
(b) We say that a set 𝑈1 is 𝑚-reducible to a set 𝑈2 if there is a total computable
function 𝑓 such that 𝑈1 = 𝑓 −1(𝑈2). Prove that if 𝑈2 is 𝑟-separable and 𝑈1 is 𝑚-
reducible to 𝑈2 then 𝑈1 is 𝑟-separable as well. [Hint. If 𝑉 is an enumerable set
disjoint with 𝑈1 then 𝑓 (𝑉 ) is an enumerable set disjoint with 𝑈2. If 𝑅 is a decidable
set separating 𝑓 (𝑉 ) and 𝑈2 then 𝑓 −1(𝑅) is a decidable set separating 𝑉 and 𝑈1.]

<!-- page 41 -->

42 1. PLAIN KOLMOGOROV COMPLEXITY
(c) Prove that there is an enumerable set that is not 𝑟-separable (such set does
not 𝑚-reduce to the upper graph of 𝐶). [Hint: there is a pair of disjoint enumerable
inseparable sets.]
13 Following [73], prove that the problems “for a given integer 𝑛 find some
string of complexity at least 𝑛” and “for a given algorithm without input find some
string that is different from its output” (if the algorithm does not terminate, any
string is OK) are equivalent: an oracle that fulfills one of the tasks can be used to
(effectively) fulfill the other. [Hint: given an algorithm, we can provide an upper
bound for the complexity of its output: it is bounded by complexity (and therefore
the length) of the algorithm itself. On the other hand, to provide a string of high
complexity means to provide a string which is guaranteed to be different from the
outputs of finitely many algorithms. At first, this looks like a more difficult task
than for one algorithm (as the oracle does). However, the following trick helps: we
may assume that the outputs are tuples and construct a tuple that differs from the
output of 𝑖-th algorithm in 𝑖-th position.]
14 (Continued.) Prove that both these problems are equivalent to the problem
of computing a fixed-point free function: “for every algorithm construct another
algorithm that computes a different function” (not the same as the first one).
15 (Continued.) Prove that an enumerable oracle can solve these problems if
and only if it solves the halting problem (M. Arslanov proved this result without
using Kolmogorov complexity). [Hint: Assume that an enumerable oracle 𝐴 allows
us to compute strings of arbitrarily high complexity. Then let us compute a string
of complexity at least 𝑛 using this oracle, and look at all elements of 𝐴 that were
questioned during this computation. How many steps are needed to enumerate all
this elements? This is a big number: any 𝑇 greater than this number, has the
Kolmogorov complexity at least 𝑛, since 𝑇 -approximation of 𝐴 can be used instead
of 𝐴. On the other hand, having an oracle for 𝐴, we can find 𝑇 for a given 𝑛.]
Kolmogorov complexity and functions 𝐵 and BB turn out to be useful to study
the the so-called “generic” and “coarse” algorithms that solve the halting problem
for most inputs (the fraction of errors converges to zero), see [11]. The versions
of these functions based on prefix complexity were introduced by G´acs [57], see
also [4] for recent results related to the busy beaver functions for different versions
of Kolmogorov complexity.
We have shown only several (simple) example that show how Kolmogorov com-
plexity is related to computability theory (also called “recursion theory”). This area
now actively grows, so we refer the interested reader to two recent monographs [146]
(by A. Nies) and [49] (by R. Downey and D. Hirschfeldt).
Theorem 15 selects some very special objects among all objects of complexity 𝑛
(in fact, one object up to equivalence described above). At first glance, this seems
strange: our intuition says that all “random” (incompressible) strings of length 𝑛
should be indistinguishable, and any special property of a string could be used to
compress it. However, we have found a very special random string 𝛾𝑛 of length 𝑛.
This paradox can be explained as follows: the individual properties of 𝛾𝑛 does allow
us to find a short description for 𝛾𝑛, but we need the oracle for 0′ to decompress
that description.
We will come back to this question in Section 5.7 discussing “the number of
wisdom” Ω and in Section 14.3 studying two-part descriptions.

<!-- page 42 -->

1.2. ALGORITHMIC PROPERTIES 43
Finally, let us note that although all the objects in Theorem 15 are equivalent,
they have very different lengths. The lengths of (a), (b), (e)–(i) is about 𝑛 while
the length of (c) and (d) grows faster than every computable function of 𝑛.

<!-- page 43 -->

<!-- page 44 -->

CHAPTER 2
Complexity of pairs and conditional complexity
### 2.1. Complexity of pairs
As we have discussed, we can define complexity of any constructive object using
(computable) encodings by strings. In this section we deal with pairs of strings.
A pair 𝑥, 𝑦 can be encoded, e.g., by a string [𝑥, 𝑦] = 𝑥01𝑦; here 𝑥 stands for 𝑥
with doubled bits. Any other computable encoding 𝑥, 𝑦 ↦ → [𝑥, 𝑦] could be used (of
course, we need that [𝑥, 𝑦]̸ = [𝑥′, 𝑦′] if 𝑥̸ = 𝑥′ or 𝑦̸ = 𝑦′). Any two encodings of
this type are equivalent (there are translation algorithms in both directions), so
Theorem 3 (p. 15) guarantees that complexities of the different encodings of the
same pair differ by 𝑂(1).
So let us fix some encoding [𝑥, 𝑦]. Kolmogorov complexity of a pair 𝑥, 𝑦 is
defined as 𝐶([𝑥, 𝑦]) and denoted by 𝐶(𝑥, 𝑦). Here are some evident properties:
∙ 𝐶(𝑥, 𝑥) = 𝐶(𝑥) + 𝑂(1);
∙ 𝐶(𝑥, 𝑦) = 𝐶(𝑦, 𝑥) + 𝑂(1);
∙ 𝐶(𝑥) 6 𝐶(𝑥, 𝑦) + 𝑂(1); 𝐶(𝑦) 6 𝐶(𝑥, 𝑦) + 𝑂(1).
The following theorem gives an upper bound for the complexity of a pair in
terms of complexities of its components:
Theorem 16.
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 2 log 𝐶(𝑥) + 𝐶(𝑦) + 𝑂(1);
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + log 𝐶(𝑥) + 2 log log 𝐶(𝑥) + 𝐶(𝑦) + 𝑂(1);
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + log 𝐶(𝑥) + log log 𝐶(𝑥) + 2 log log log 𝐶(𝑥) + 𝐶(𝑦) + 𝑂(1);
. . .
(We can continue this sequence of inequalities indefinitely. Also, one can ex-
change 𝑥 and 𝑦.)
Proof. This proof (for the first inequality) was already explained in the In-
troduction (Theorem 4, p. 16). The only difference is that we considered the con-
catenation 𝑥𝑦 instead of a pair. Let us repeat the argument for pairs.
A computable mapping 𝑥 ↦ → ˆ𝑥 (here 𝑥 and ˆ𝑥 are binary strings) is called a
prefix-free encoding, if for any two different strings 𝑥 and 𝑦 the string ˆ𝑥 is not a
prefix of the string ˆ𝑦. (In particular, ˆ𝑥̸ = ˆ𝑦 if 𝑥̸ = 𝑦.) This guarantees that both 𝑢
and 𝑣 can be uniquely reconstructed from ˆ𝑢𝑣.
An example of a prefix-free encoding: 𝑥 ↦ → 𝑥01, where 𝑥 stands for 𝑥 with
doubled bits. Here the block 01 are used as a delimiter. However, this encoding is
not the most space-efficient one, since it doubles the length. A better prefix-free
encoding:
𝑥 ↦ → ˆ𝑥 = bin(𝑙(𝑥)) 01𝑥
45

<!-- page 45 -->

46 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
(bin(𝑙(𝑥)) is the binary representation of the length 𝑙(𝑥) of the string 𝑥). Now
𝑙(ˆ𝑥) = 𝑙(𝑥) + 2 log 𝑙(𝑥) + 𝑂(1).
This trick can be “iterated”: for any prefix-free encoding 𝑥 ↦ → ˆ𝑥 we can construct
another prefix-free encoding
𝑥 ↦ →	̂	 bin(𝑙(𝑥))𝑥.
Indeed, if	̂	 bin(𝑙(𝑥))𝑥 is a prefix of	̂	 bin(𝑙(𝑦))𝑦, then one of the strings	̂	 bin(𝑙(𝑥)) and
̂	
bin(𝑙(𝑦)) is a prefix of the other one, and therefore bin(𝑙(𝑥)) = bin(𝑙(𝑦)). Therefore
𝑥 is a prefix of 𝑦, and 𝑙(𝑥) = 𝑙(𝑦), so 𝑥 = 𝑦. (In other terms, we uniquely determine
the length of the string, since a prefix-free code is used for it, and then get the
string itself knowing where it ends.)
In this way we get a prefix-free encoding such that
𝑙(ˆ𝑥) = 𝑙(𝑥) + log 𝑙(𝑥) + 2 log log 𝑙(𝑥) + 𝑂(1),
then (one more iteration)
𝑙(ˆ𝑥) = 𝑙(𝑥) + log 𝑙(𝑥) + log log 𝑙(𝑥) + 2 log log log 𝑙(𝑥) + 𝑂(1),
etc.
Now we return to the proof. Let 𝐷 be the optimal decompressor used in
the definition of Kolmogorov complexity. Consider a decompressor 𝐷′ defined as
follows:
𝐷′(ˆ𝑝𝑞) = [𝐷(𝑝), 𝐷(𝑞)],
where ˆ𝑝 is a prefix-free encoding and [·, ·] is the encoding of pairs (used in the
definition of pairs complexity). Since ˆ𝑝 is a prefix-free encoding, 𝐷′ is well defined
(we can uniquely extract ˆ𝑝 out of ˆ𝑝𝑞).
Let 𝑝 and 𝑞 be the shortest descriptions of 𝑥 and 𝑦. Then ˆ𝑝𝑞 is a description
of [𝑥, 𝑦], and its length is exactly as we need in our theorem. (The more iterations
we use for the prefix-free encoding, the better bound we get.) 
Theorem 16 implies that
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 𝐶(𝑦) + 𝑂(log 𝑛)
for strings 𝑥 and 𝑦 of length at most 𝑛: one may say that the complexity of a
pair does not exceed the sum of the complexities of its component with logarithmic
precision.
16 Suggest a natural definition for the complexity of a triple. Show that
𝐶(𝑥, 𝑦, 𝑧) 6 𝐶(𝑥) + 𝐶(𝑦) + 𝐶(𝑧) + 𝑂(log 𝑛) for every three strings 𝑥, 𝑦, 𝑧 of length
at most 𝑛.
A natural question arises: is it true that 𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 𝐶(𝑦) + 𝑂(1)?
A simple argument shows that this is not the case. Indeed, this inequality would
imply 𝐶(𝑥, 𝑦) 6 𝑙(𝑥) + 𝑙(𝑦) + 𝑂(1). Consider some 𝑁 . For each 𝑛 = 0, 1, 2, . . . , 𝑁
we have 2𝑛 strings 𝑥 of length 𝑛 and 2𝑁 −𝑛 strings 𝑦 of length 𝑁 − 𝑛. Combining
them, we (for a given 𝑛) obtain 2𝑁 different pairs ⟨𝑥, 𝑦⟩. The total number of pairs
(all 𝑛 = 0, 1, . . . , 𝑁 give different pairs) is (𝑁 + 1)2𝑁 .
Assume that indeed 𝐾(𝑥, 𝑦) 6 𝑙(𝑥) + 𝑙(𝑦) + 𝑂(1) = 𝑁 + 𝑂(1) for all these pairs.
Then we get (𝑁 + 1)2𝑁 different strings [𝑥, 𝑦] of complexity at most 𝑁 + 𝑂(1), but
this is impossible (Theorem 7, p. 31, gives the upper bound 𝑂(2𝑁 )).

<!-- page 46 -->

2.1. COMPLEXITY OF PAIRS 47
17 Prove that there is no constant 𝑐 such that
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + log 𝐶(𝑥) + 𝐶(𝑦) + 𝑐
for all 𝑥 and 𝑦. [Hint: Replace 𝐶 in the right hand side by 𝑙 and count the number
of corresponding pairs.]
18 (a) Prove that∑︁
𝑥∈Ξ
2−𝑙(^𝑥) 6 1
for any prefix-free encoding 𝑥 ↦ → ˆ𝑥 (here Ξ is the set of all binary strings).
(b) Prove that if a prefix-free encoding increases the length of a 𝑛-bit string at
most by 𝑓 (𝑛), i.e., if 𝑙(ˆ𝑥) 6 𝑙(𝑥) + 𝑓 (𝑙(𝑥)), then∑︀ 𝑛 2−𝑓 (𝑛) < ∞.
This problem explains why a coefficient 2 appears in the Theorem 16 (p. 45):
the series∑︁ 1
𝑛2 ,∑︁ 1
𝑛(log 𝑛)2 ,∑︁ 1
𝑛 log 𝑛(log log 𝑛)2 , . . .
converge, while the series∑︁	
1
𝑛 ,∑︁ 1
𝑛 log 𝑛 ,∑︁ 1
𝑛 log 𝑛 log log 𝑛 , . . .
diverge.
The following problem describes functions that can be used for bounds similar
to Theorem 16.
19 Let 𝑓 : N → N is a non-decreasing total computable function. Prove that
the following three properties are equivalent:
(a) 𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 𝐶(𝑦) + 𝑓 (𝐶(𝑥)) + 𝑂(1);
(b) 𝐶(𝑥, 𝑦) 6 𝑙(𝑥) + 𝑙(𝑦) + 𝑓 (𝑙(𝑥)) + 𝑂(1);
(c)∑︀ 𝑛 2−𝑓 (𝑛) < ∞. [Hint: (a) obviously implies (b); to get the reverse implica-
tion, consider the shortest descriptions. To derive (a) from (c), one can count pairs
with 𝑙(𝑥) + 𝑓 (𝑙(𝑥)) + 𝑙(𝑦) < 𝑛; one can also use results about prefix complexity (see
Chapter 4, Problem 107). Finally, to derive (c) from (b), note that the right hand
side in (b) is at most 𝑛 + 𝑂(1) if 𝑙(𝑥) = 𝑘 and 𝑙(𝑦) = 𝑛 − 𝑘 − 𝑓 (𝑘), for 𝑘 + 𝑓 (𝑘) 6 𝑛.
So the number of such pairs is at least∑︀ 2𝑘2𝑛−𝑘−𝑓 (𝑘) = 2𝑛∑︀ 𝑘 2−𝑓 (𝑘) where the
sum is taken over all 𝑘 such that 𝑘 + 𝑓 (𝑘) 6 𝑛. ]
20 Prove that all the inequalities of Theorem 16 become false if the coefficient
2 is replaced by 1, but remain true with the coefficient 1 + 𝜀 for any 𝜀 > 0. [Hint:
see the preceding problem.]
21 Prove that
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + log 𝐶(𝑥) + 𝐶(𝑦) + log 𝐶(𝑦) + 𝑂(1).
22 (Continued) Prove a stronger inequality:
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 𝐶(𝑦) + log(𝐶(𝑥) + 𝐶(𝑦)) + 𝑂(1).
(note that 𝐶(𝑥) + 𝐶(𝑦) can be replaced by max(𝐶(𝑥), 𝐶(𝑦)), this gives a factor at
most 2, which makes 𝑂(1) after taking logarithms).
23 Prove that 𝐶(𝑥, 𝐶(𝑥)) = 𝐶(𝑥) + 𝑂(1). [Hint: 𝐶(𝑥, 𝐶(𝑥)) > 𝐶(𝑥) + 𝑂(1)
for evident reasons; on the other hand, the shortest description of 𝑥 determines
both 𝑥 and 𝐶(𝑥).]
24 Prove that if 𝐶(𝑥) 6 𝑛 and 𝐶(𝑦) 6 𝑛, then 𝐶(𝑥, 𝑦) 6 2𝑛 + 𝑂(1).

<!-- page 47 -->

48 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
### 2.2. Conditional complexity
When transmitting a file, one could try to save communication charges by
compressing it. The transmission could be made even more effective if and old
version of the same file already exists at the other side. In this case we need only
to describe the changes made. This could be considered as a kind of motivation
for the definition of conditional complexity of a given string 𝑥 relative to (known)
string 𝑦.
A conditional decompressor is a computable function 𝐷 of two arguments,
the description and the condition (both arguments and the value of 𝐷 are binary
strings). If 𝐷(𝑦, 𝑧) = 𝑥 we say that 𝑦 is a (conditional) description of 𝑥 when 𝑧 is
known (or relative to 𝑧) The complexity 𝐶𝐷 (𝑥 | 𝑧) is then defined as the length of
the shortest conditional description:
𝐶𝐷 (𝑥 | 𝑧) = min{𝑙(𝑦) | 𝐷(𝑦, 𝑧) = 𝑥}.
We say that (conditional) decompressor 𝐷1 is not worse than 𝐷2 if
𝐶𝐷1 (𝑥 | 𝑧) 6 𝐶𝐷2 (𝑥 | 𝑧) + 𝑐
for some constant 𝑐 and for all 𝑥 and 𝑧. A conditional decompressor is optimal if
it is not worse than any other conditional decompressor.
Theorem 17. There exist optimal conditional decompressors.
Proof. This “conditional” version of Kolmogorov–Solomonoff theorem can be
proved in the same way as the unconditional one (Theorem 1, p. 13).
Fix some programming language where one can write programs for computable
functions of two arguments, and let
𝐷(ˆ𝑝𝑦, 𝑧) = 𝑝(𝑦, 𝑧),
where 𝑝(𝑦, 𝑧) is the output of program 𝑝 on inputs 𝑦 and 𝑧, and ˆ𝑝 is the prefix-free
encoding of 𝑝.
It is easy to see now that if 𝐷′ is a conditional decompressor and 𝑝 is a program
for 𝐷′, then
𝐶𝐷 (𝑥 | 𝑧) 6 𝐶𝐷′ (𝑥 | 𝑧) + 𝑙(ˆ𝑝).
Theorem is proved. 
Again, we fix some optimal conditional decompressor 𝐷 and omit index 𝐷 in
the notation.
Let us start with some simple properties of conditional complexity.
Theorem 18.
𝐶(𝑥 | 𝑦) 6 𝐶(𝑥) + 𝑂(1);
𝐶(𝑥 | 𝑥) = 𝑂(1);
𝐶(𝑓 (𝑥, 𝑦) | 𝑦) 6 𝐶(𝑥 | 𝑦) + 𝑂(1);
𝐶(𝑥 | 𝑦) 6 𝐶(𝑥 | 𝑔(𝑦)) + 𝑂(1).
Here 𝑔 and 𝑓 are arbitrary computable functions (of one and two arguments,
respectively); the inequalities are valid if 𝑓 (𝑥, 𝑦) and 𝑔(𝑦) are defined.

<!-- page 48 -->

2.2. CONDITIONAL COMPLEXITY 49
Proof. First inequality: any unconditional decompressor can be considered
as a conditional one that ignores the second argument.
Second inequality: consider 𝐷 such that 𝐷(𝑝, 𝑧) = 𝑧.
Third inequality: Let 𝐷 be the optimal conditional decompressor used to define
complexity. Consider another decompressor 𝐷′ such that
𝐷′(𝑝, 𝑦) = 𝑓 (𝐷(𝑝, 𝑦), 𝑦)
and apply the optimality property.
Similar argument works for the last inequality, but 𝐷′ should be defined in a
different way:
𝐷′(𝑝, 𝑦) = 𝐷(𝑝, 𝑔(𝑦)).
Theorem is proven. 
25 Prove that conditional complexity is “continuous as a function of its second
argument”: 𝐶(𝑥 | 𝑦0) = 𝐶(𝑥 | 𝑦) + 𝑂(1); 𝐶(𝑥 | 𝑦1) = 𝐶(𝑥 | 𝑦) + 𝑂(1). Using this
property, show that for every string 𝑥 and for every non-negative integer 𝑙 6 𝐶(𝑥)
there exists a string 𝑦 such that 𝐶(𝑥 | 𝑦) = 𝑙 + 𝑂(1).
Similar argument based on two-dimensional topology is used in [155].
26 Prove that for any fixed 𝑦 the function 𝑥 ↦ → 𝐶(𝑥 | 𝑦) differs from 𝐶 at most
by 2𝐶(𝑦) + 𝑂(1).
27 Prove that 𝐶([𝑥, 𝑧] | [𝑦, 𝑧]) 6 𝐶(𝑥 | 𝑦) + 𝑂(1) for any strings 𝑥, 𝑦, 𝑧 (here
[·, ·] stands for the computable encoding of pairs).
28 Fix some “reasonable” programming language. (Formally, we require the
corresponding universal function to be a G¨odel one; this means that translation
algorithm exists for any other programming language, see, e.g., [182].) Show that
conditional complexity 𝐶(𝑥 | 𝑦) is equal (up to 𝑂(1) additive term) to the minimal
complexity of a program that produces output 𝑥 on input 𝑦. [Hint: Let 𝐷 be an
optimal conditional decompressor. If we fix its first argument 𝑝, we get a program
of complexity at most 𝑙(𝑝) + 𝑂(1). On the other hand, if program 𝑝 maps 𝑦 to 𝑥,
then 𝐶(𝑥 | 𝑦) = 𝐶(𝑝(𝑦) | 𝑦) 6 𝐶(𝑝) + 𝑂(1).]
This interpretation of conditional complexity as a minimal complexity of a
program with some property will be considered in Chapter 13.
If we restrict ourselves to total programs (that terminate on all inputs), we
get an essentially different notion of conditional complexity that can be called total
conditional complexity.
29 Show that the notion of total conditional complexity CT(𝑥 | 𝑦), the minimal
(plain) complexity of a total program that maps 𝑦 to 𝑥, is well defined (i.e., changes
at most by 𝑂(1) when we change the programming language in a reasonable way).
Prove that
𝐶(𝑥 | 𝑦) 6 CT(𝑥 | 𝑦) 6 𝐶(𝑥)
with 𝑂(1)-precision.
30 Show that the total complexity sometimes exceeds significantly the usual
conditional complexity: for every 𝑛 there exist two 𝑛-bit strings 𝑥 and 𝑦 such that
𝐶(𝑥 | 𝑦) = 𝑂(1) while CT(𝑥 | 𝑦) > 𝑛.
[Hint: Let us enumerate all programs of complexity less than 𝑛 defined on all 𝑛-bit
strings, and maintain two 𝑛-bit strings 𝑥 and 𝑦 with the following property: none of
the programs found maps 𝑦 to 𝑥. When a new program is found that maps 𝑦 to 𝑥,

<!-- page 49 -->

50 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
we choose a fresh value of 𝑦 and then choose appropriate 𝑥. This process is effective
if 𝑛 (=length of 𝑦) is given, it defines a partial function 𝑦 ↦ → 𝑥, so 𝐶(𝑥 | 𝑦) = 𝑂(1)
for every pair selected.]
31 Let 𝑥 and 𝑦 be two bit strings such that CT(𝑥 | 𝑦) 6 𝑛 and CT(𝑦 | 𝑥) 6 𝑛.
Prove that there exists a program of a computable permutation of the set of bit
strings that maps 𝑥 to 𝑦 and has complexity at most 2𝑛 + 𝑂(1). [Hint: it is easy
to construct a string 𝑣 of length 2𝑛 + 𝑂(1) that encodes a pair of total programs
𝑓 that maps 𝑥 to 𝑦 and 𝑔 that maps 𝑦 to 𝑥. We may assume without loss of
generality that 𝑥 and 𝑦 have 0 as their first bits. Consider a binary relation on
binary strings that starts with 0, defined as 𝑅(𝑢, 𝑣) : (𝑓 (𝑢) = 𝑣) and (𝑔(𝑣) = 𝑢)).
This is a decidable one-to-one correspondence between decidable sets of strings with
infinite complements, and it can be easily extended to a computable permutation.]
32 Show that the upper bound in the preceding problem cannot be improved
significantly: for every 𝑘 there are two strings 𝑥 and 𝑦 of length 𝑛 = 2𝑘 + 𝑂(1)
such that 𝐶(𝑥), 𝐶(𝑦) 6 𝑘 + 𝑂(1) (and therefore CT(𝑥 | 𝑦), CT(𝑦 | 𝑥) 6 𝑘 + 𝑂(1)),
but every permutation of 𝑛-bit strings that maps 𝑥 to 𝑦 has complexity at least
2𝑘. [Hint: Let us first select (arbitrarily) 2𝑘 strings 𝑦 and pair them with some
string 𝑥. Let us enumerate computable permutations of 𝑛-bit strings that have
complexity less than 2𝑘. If and when all selected pairs are served by some of these
permutations, choose a new string 𝑥 that is connected (by existing permutation)
with at most half of the selected 𝑦-strings. After that Ω(2𝑘) new permutations are
needed to connect new 𝑥 to all 𝑦-strings. Therefore at most 22𝑘/Ω(2𝑘) = 𝑂(2𝑘)
𝑥-strings will be used, so the final 𝑥 and 𝑦 have complexity at most 𝑘 + 𝑂(1). The
selection of 𝑥 connected with at most half of selected 𝑦-strings is always possible,
since each of 𝑦-strings is connected with a small fraction of 𝑥-strings, and we can
change the order of summation in the double sum. Note that this argument may
be used to guarantee that one of the strings 𝑥 and 𝑦 belongs to a given set of 2𝑘
strings.]
See [135] for the detailed proofs of these results about total conditional com-
plexity.
Many properties of unconditional complexity have conditional counterparts
with essentially the same proofs. Here are some of these counterparts:
∙ Function 𝐶(· | ·) is upper semicomputable (this means that the set of triples
⟨𝑥, 𝑦, 𝑛⟩ such that 𝐶(𝑥 | 𝑦) < 𝑛 is enumerable).
∙ For any 𝑦 and 𝑛 the set of all strings 𝑥 such that 𝐶(𝑥 | 𝑦) < 𝑛 has cardi-
nality less then 2𝑛.
∙ For any 𝑦 and 𝑛 there exists a string 𝑥 of length 𝑛 such that 𝐶(𝑥 | 𝑦) > 𝑛.
33 Prove that for any strings 𝑦 and 𝑧 and for any number 𝑛 there exists a
string 𝑥 of length 𝑛 such that 𝐶(𝑥 | 𝑦) > 𝑛 − 1 and 𝐶(𝑥 | 𝑧) > 𝑛 − 1. [Hint: both
requirements are violated by a minority of strings.]
Theorem 19. Let ⟨𝑥, 𝑦⟩ ↦ → 𝑘(𝑥, 𝑦) be an upper semicomputable function such
that the set {𝑥 | 𝑘(𝑥, 𝑦) < 𝑛} has cardinality less than 2𝑛 for any string 𝑦 and
integer 𝑛. Then 𝐶(𝑥 | 𝑦) 6 𝑘(𝑥, 𝑦) + 𝑐 for some 𝑐 and for all 𝑥 and 𝑦.
The proof repeats the proof of Theorem simple-upper-reformulated.
Using conditional complexity, we get a stronger inequality for the complexity
of pairs (compared with Theorem 16, p. 45):

<!-- page 50 -->

2.2. CONDITIONAL COMPLEXITY 51
Theorem 20.
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 2 log 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + 𝑂(1)
Proof. Let 𝐷1 be an optimal unconditional decompressor and let 𝐷2 be an
optimal conditional decompressor. Construct a new unconditional decompressor
𝐷′ as follows:
𝐷′(ˆ𝑝𝑞) = [𝐷1(𝑝), 𝐷2(𝑞, 𝐷1(𝑝))].
Here ˆ𝑝 stands for the prefix-free encoding of 𝑝, and [·, ·] is a computable encoding
of pairs used in the definition of the complexity of pairs. Let 𝑝 be the shortest 𝐷1-
description of 𝑥 and 𝑞 be the shortest 𝐷2-description of 𝑦 conditional to 𝑥. Then
the string ˆ𝑝𝑞 is a 𝐷3-description of [𝑥, 𝑦]. Therefore,
𝐶(𝑥, 𝑦) 6 𝐶𝐷′ (𝑥, 𝑦) + 𝑂(1) 6 𝑙(ˆ𝑝) + 𝑙(𝑞) + 𝑂(1).
As we have seen, one can choose a prefix-free encoding in such a way that 𝑙(ˆ𝑝) is
bounded by 𝑙(𝑝) + 2 log 𝑙(𝑝) + 𝑂(1) (see the proof of Theorem 16, p. 45), and we
get a desired inequality. 
As before, we may replace 2 log 𝐶(𝑥) by log 𝐶(𝑥) + 2 log log 𝐶(𝑥) etc., getting a
better bound. We also can use conditional complexity in the logarithmic term and
write
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + 2 log 𝐶(𝑦 | 𝑥) + 𝑂(1).
(In the proof we should then replace 𝐷′(ˆ𝑝𝑞) by 𝐷′(ˆ𝑞𝑝).)
34 Prove that
𝐶(𝑥 | 𝑧) 6 𝐶(𝑥 | 𝑦) + 2 log 𝐶(𝑥 | 𝑦) + 𝐶(𝑦 | 𝑧) + 𝑂(1)
for all 𝑥, 𝑦, 𝑧 (a sort of a “triangle inequality”).
If we are not interested in the exact form of the additional logarithmic term,
the statement of Theorem 20 can be reformulated as follows:
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + 𝑂(log 𝑛).
for all strings 𝑥, 𝑦 of length at most 𝑛.
It turns out (and this is the first nontrivial statement in this chapter, and
probably the first non-trivial result about Kolmogorov complexity; it was proven
independently by Kolmogorov and Levin and published in [78, 223]) that this
inequality is in fact an equality.
Theorem 21 (Kolmogorov–Levin).
𝐶(𝑥, 𝑦) = 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + 𝑂(log 𝑛).
for all strings 𝑥, 𝑦 of length at most 𝑛.
Proof. Since we already have one inequality, we need to prove only that
𝐶(𝑥, 𝑦) > 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + 𝑂(log 𝑛)
for all 𝑥 and 𝑦 of length at most 𝑛.
Let 𝑥 and 𝑦 be some strings of length at most 𝑛. Let 𝑎 be the complexity
𝐶(𝑥, 𝑦) of the pair ⟨𝑥, 𝑦⟩. Consider the set 𝐴 of all pairs whose complexity does not
exceed 𝑎. Then 𝐴 is a set of cardinality 𝑂(2𝑎) (in fact, at most 2𝑎+1) and ⟨𝑥, 𝑦⟩ is
one of its elements.
For each string 𝑡 consider the “vertical section” 𝐴𝑡 of 𝐴:
𝐴𝑡 = {𝑢 | ⟨𝑡, 𝑢⟩ ∈ 𝐴}

<!-- page 51 -->

52 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
𝑡
𝐴𝑡
𝐴
𝑥
𝑦
Figure 1. The section 𝐴𝑡 of the set 𝐴 of all simple pairs.
(Fig. 1). The sum of the cardinalities of all 𝐴𝑡 (over all strings 𝑡) is the cardinality
of 𝐴 and does not exceed 𝑂(2𝑎). Therefore there are few “large” sections 𝐴𝑡, and
this is the basic argument we need for the proof.
Let 𝑚 be equal to ⌊log2 |𝐴𝑥|⌋ where 𝑥 is the first component of the pair ⟨𝑥, 𝑦⟩
we started with. In other terms, assume that cardinality of 𝐴𝑥 is between 2𝑚 and
2𝑚+1. Let us prove that
(1) 𝐶(𝑦 | 𝑥) does not exceed 𝑚 significantly;
(2) 𝐶(𝑥) does not exceed 𝑎 − 𝑚 significantly.
We start with (1). Knowing 𝑎, we can enumerate the set 𝐴. If we know also 𝑥,
we can select only pairs whose first component equals 𝑥. In this way we get an
enumeration of 𝐴𝑥. To specify 𝑦, it is enough to tell the ordinal number of 𝑦 in
this enumeration (of 𝐴𝑥). This ordinal number takes 𝑚 + 𝑂(1) bits, and together
with 𝑎 we get 𝑚 + 𝑂(log 𝑛) bits for the conditional description of 𝑦 given 𝑥. Note
that 𝑎 = 𝐶(𝑥, 𝑦) does not exceed 𝑂(𝑛) for strings 𝑥 and 𝑦 of length 𝑛. Therefore,
we need only 𝑂(log 𝑛) to specify 𝑎 and 𝑛, and
𝐶(𝑦 | 𝑥) 6 𝑚 + 𝑂(log 𝑛).
Now let us prove (2). Consider the set 𝐵 of all strings 𝑡 such that cardinality
of 𝐴𝑡 is at least 2𝑚. The cardinality of 𝐵 does not exceed 2𝑎+1/2𝑚, otherwise the
sum |𝐴| =∑︀ |𝐴𝑡| would be greater than 2𝑎+1. We can enumerate 𝐵 if we know 𝑎
and 𝑚. Indeed, we should enumerate 𝐴 and group together the pairs with the same
first coordinate; if we find 2𝑚 pairs with the same value of the first coordinate, we
put this value into 𝐵. Therefore the string 𝑥 (as well as every element of 𝐵) can be
specified by (𝑎 − 𝑚) + 𝑂(log 𝑛) bits: 𝑎 − 𝑚 + 1 bits are needed for ordinal number
of 𝑥 in the enumeration of 𝐵, and 𝑂(log 𝑛) are used to specify 𝑎 and 𝑚. So we get
𝐶(𝑥) 6 (𝑎 − 𝑚) + 𝑂(log 𝑛),
and it remains to add this inequality and the preceding one. 
This theorem can be considered as the complexity counterpart of the following
combinatorial statement. Let 𝐴 be a finite set of pairs. Its cardinality is (obviously)
bounded by the product of the cardinality of 𝐴’s projection onto the first coordinate,
and the maximal cardinality of the sections 𝐴𝑥. This corresponds to the inequality
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + 𝑂(log 𝑛). The reverse inequality needs a more subtle
interpretation. Let 𝐴 be a set of pairs and let 𝑝 and 𝑞 be some numbers such that

<!-- page 52 -->

2.2. CONDITIONAL COMPLEXITY 53
cardinality of 𝐴 does not exceed 𝑝𝑞. Then we can split 𝐴 into parts 𝑃 and 𝑄 with
the following properties: the projection of 𝑃 onto the first coordinate has at most 𝑝
elements, while all the sections 𝑄𝑥 of 𝑄 (for element in 𝑄𝑥 the first coordinate equals
𝑥) have at most 𝑞 elements. (Indeed, let 𝑃 be the union of all sections that have
more than 𝑞 elements. The number of such sections do not exceed 𝑝. Remaining
elements form 𝑄.) We return to this combinatorial translation in Chapter 10.
Note that in fact we have not used the lengths of 𝑥 and 𝑦, only their complex-
ities. So we have proved the following statement:
Theorem 22 (Kolmogorov–Levin, complexity version).
𝐶(𝑥, 𝑦) = 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + 𝑂(log 𝐶(𝑥, 𝑦))
for all strings 𝑥 and 𝑦.
35 Give a more detailed analysis of the additive terms in the proof and show
that
𝐶(𝑥) + 𝐶(𝑦 | 𝑥) 6 𝐶(𝑥, 𝑦) + 3 log 𝐶(𝑥, 𝑦) + 𝑂(log log 𝐶(𝑥, 𝑦)).
36 Show that if 𝐶(𝑥, 𝑦 | 𝑘, 𝑙) < 𝑘+𝑙, then 𝐶(𝑥 | 𝑘, 𝑙) < 𝑘+𝑂(1) or 𝐶(𝑦 | 𝑥, 𝑘, 𝑙) <
𝑙 + 𝑂(1). [Hint: This is what we proved actually in the proof of Theorem 22.]
37 Show that 𝑂(log 𝑛) terms are unavoidable in Kolmogorov–Levin theorem
in both directions: for each 𝑛 there exist strings 𝑥 and 𝑦 of length at most 𝑛 such
that
𝐶(𝑥, 𝑦) > 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + log 𝑛 − 𝑂(1),
as well as strings 𝑥 and 𝑦 of length at most 𝑛 such that
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) − log 𝑛 + 𝑂(1).
[Hint: For the first inequality we can refer to the remark after Theorem 16 (p. 45).
For the second note that 𝐶(𝑥, 𝑙(𝑥)) = 𝐶(𝑥) for every 𝑥, while 𝐶(𝑥|𝑙(𝑥)) can be
equal to 𝑙(𝑥) + 𝑂(1) and 𝐶(𝑥) + 𝑂(1). Then we can take a random length between
𝑛/2 and 𝑛 and a random string of this length.]
38 Prove that changing one bit in a string of length 𝑛 changes its complexity
at most by log 𝑛 + 𝑂(log log 𝑛). Prove the same for the conditional complexity
𝐶(𝑥 | 𝑛).
As we have seen in Problem 7 (p. 34), for every 𝑛-bit string 𝑥 there exists
another string 𝑥′ of the same length that differs from 𝑥 in one position only such
that 𝐶(𝑥′) < 𝑛 − log 𝑛 + 𝑂(1) (and therefore 𝐶(𝑥′ | 𝑛) < 𝑛 − log 𝑛 + 𝑂(1)). In
particular, if 𝑥 is incompressible (given 𝑛), one can change one bit in 𝑥 and decrease
𝐶(𝑥 | 𝑛).
One can move also in the other direction: if 𝐶(𝑥 | 𝑛) is small enough (this means
that 𝐶(𝑥 | 𝑛) 6 𝛼𝑛 for some positive constant 𝛼), we can increase this complexity
by changing one bit in 𝑛: there exists some 𝛼 > 0 such that for each 𝑛-bit string
𝑥 with 𝐶(𝑥 | 𝑛) 6 𝛼𝑛 one can change one bit in 𝑥 and get another 𝑛-bit string 𝑥′
such that 𝐶(𝑥′ | 𝑛) > 𝐶(𝑥 | 𝑛). (The proof of this statement requires more involved
combinatorial argument [24] than the decrease in complexity.)
39 Fix some unconditional decompressor 𝐷. Prove that for some constant 𝑐
and for all integers 𝑛 and 𝑘 the following statement is true: if some string 𝑥 has
at least 2𝑘 descriptions of length at most 𝑛, then 𝐶(𝑥 | 𝑘) 6 𝑛 − 𝑘 + 𝑐. [Hint: Fix
some 𝑘. For each 𝑛 consider all strings 𝑥 that have at least 2𝑘 descriptions of length

<!-- page 53 -->

54 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
at most 𝑛. The number of these strings does not exceed 2𝑛−𝑘, and we can apply
Theorem 19, p. 50.]
Using this problem, we can prove the following statement about unconditional
complexity (see [102, Exercises 4.3.9, 4.3.10]):
40 Let 𝐷 be some optimal unconditional decompressor. Then there exists
some constant 𝑐 such that for any string 𝑥 the number of shortest 𝐷-descriptions
of 𝑥 does not exceed 𝑐.
[Hint: The previous problems show that 𝐶(𝑥) 6 𝑛 − 𝑘 + 2 log 𝑘 + 𝑂(1), so for
𝐶(𝑥) = 𝑛 we get an upper bound for 𝑘.]
41 Prove that there exists a constant 𝑐 with the following property: if for
some 𝑥 and 𝑛 the probability of the event 𝐶(𝑥 | 𝑦) 6 𝑘 (all strings 𝑦 of lengths 𝑛 are
considered as equiprobable here) is at least 2−𝑙, then 𝐶(𝑥 | 𝑛, 𝑙) 6 𝑘 + 𝑙 + 𝑐. [Hint:
Connect each string 𝑦 of length 𝑛 to all strings 𝑥 such that 𝐶(𝑥 | 𝑦) 6 𝑘. We get
a bipartite graph that has 𝑂(2𝑛+𝑘) edges. In this graph the number of vertices 𝑥
that have degree at least 2𝑛−𝑙 does not exceed 𝑂(2𝑘+𝑙). Note that 𝐶(𝑥 | 𝑛, 𝑙) does
not include 𝑘—this is not a typo!]
This problem could help us to find the average value of 𝐶(𝑥 | 𝑦) for given 𝑥 and
all string 𝑦 of some length 𝑛. It is evident that 𝐶(𝑥 | 𝑦) 6 𝐶(𝑥 | 𝑛) + 𝑂(1) since
𝑛 = 𝑙(𝑦) is determined by 𝑦. It turns out that for most strings 𝑦 (of given length)
this inequality is close to an equality:
42 Prove that there exists some constant 𝑐 such that for each string 𝑥 and for
all natural numbers 𝑛 and 𝑑 the fraction of strings 𝑦 such that 𝐶(𝑥 | 𝑦) < 𝐶(𝑥 | 𝑛)−𝑑
(among all strings of length 𝑛) does not exceed 𝑐𝑑2/2𝑑. Using this statement, prove
that the average value of 𝐶(𝑥 | 𝑦) taken over all strings 𝑦 of a given length 𝑛 equals
𝐶(𝑥 | 𝑛) + 𝑂(1) (the constant in 𝑂(1) does not depend on 𝑥 and 𝑛).
43 Prove that 𝐶(𝑥 | 𝑘) 6 𝑘 implies 𝐶(𝑥) 6 𝑘 + 𝑂(1). [Hint: See Theorem 7.
One can also note that if a conditional description of 𝑥 given 𝑘 has length 𝑘, then 𝑘
is known anyway, and if this description is shorter, we have enough space to specify
the difference between 𝑘 and the description length.]
A similar (though not identical) statement:
44 Prove that 𝐶(𝑥) = 𝐶(𝑥 | 𝐶(𝑥)) + 𝑂(1). [Hint: Assume that 𝑥 has a condi-
tional description 𝑞 with condition 𝐶(𝑥) that is shorter than 𝐶(𝑥). Then one can
specify 𝑥 by providing 𝑞 and the difference 𝐶(𝑥) − 𝑙(𝑞), and we get a description of
𝑥 that is shorter than 𝐶(𝑥)—a contradiction.]
45 Prove that for every 𝑛 there exists a 𝑛-bit string 𝑥 such that
𝐶(𝐶(𝑥) | 𝑥) = log 𝑛 − 𝑂(1).
(This is a maximal possible value, since 𝐶(𝑥) 6 𝑛 for 𝑛-bit string 𝑥.)
This result (in a bit weaker form) was proven long ago by P. G´acs [55]. Re-
cently E. Kalinina and B. Bauwens suggested a simple game-theoretic proof of this
statement. Here is a sketch is this argument (see [6] for details). Consider a rectan-
gular game board of width 2𝑛 and height 𝑛. Two players, White and Black, make
alternating moves and place pawns of their respective colors into the board cells.
Unlike chess, each cell may contain both white and black pawns (at most one of
each color). At each move player may place several pawns into different cells (or no

<!-- page 54 -->

2.2. CONDITIONAL COMPLEXITY 55
pawns at all); after a pawn is places, it cannot be moved or removed. Also Black
can irreversibly mark some cells. The players should obey the following restrictions:
(a) each of the players can place at most 2𝑖 pawns at row 𝑖 (the bottom row
has number 0, the upper row has number 𝑛 − 1);
(b) Black can mark at most half of the cells in each column.
A white pawn is declared as killed if its cell is marked or if there is a black
paws below it (in the same column). The game does not end formally (though it is
essentially a finite game); White wins if in the limit there is at least one non-killed
white pawn.
White has a winning strategy in this game: place a pawn in the top row and
wait until it is killed. If it is killed by the black pawn below, switch to the next
column (for example, White can go from left to right starting with the leftmost
column). If the pawn was killed by marking its cell, White places another pawn
just below the first one, etc. (We may assume that Black’s moves kill the white
pawn, all other moves can be postponed, since the winner is determined by the
limit position.) Recall that Black can mark at most half of the column, so Black
is forced to put some pawn in the column at some point. It cannot be done in all
columns, since the sum of 2𝑖 for all rows is less (by 1) than the width of the table.
Note also that White will not violate restrictions on the number of pawns in each
row, since in all the columns (except the currently active one) under each white
pawn (in row 𝑖) there is a black paws (in some row 𝑗 < 𝑖), and the sum of 2𝑗 for
all 𝑗 < 𝑖 is less that 2𝑖 and there is a space for one more white pawn.
After a winning strategy for White is described, consider the following “univer-
sal” strategy for Black: the cell (𝑥, 𝑖) is marked as soon as we find that 𝐶(𝑖 | 𝑥) <
log 𝑛 − 1; a black pawn in placed at (𝑥, 𝑖) when a conditional description of 𝑥
(given 𝑛) of length 𝑖 is found. It is easy to check that Black obeys the game rules.
White wins, and a live white pawn at the cell (𝑥, 𝑖) means that 𝐶(𝑥 | 𝑛) > 𝑖 and
𝐶(𝑖 | 𝑥) > log 𝑛−1. Since the actions of White (playing against computable strategy
of Black) are computable, we conclude that 𝐶(𝑥 | 𝑛) > 𝑖 + 𝑂(1): the set of white
pawns in row 𝑖 is enumerable and it contains at most 2𝑖 elements.
This argument shows that 𝐶(𝐶(𝑥 | 𝑛) | 𝑥) > log 𝑛 − 1 (not exactly what we
wanted); to get the desired result, we should change the game and consider in
paraller boards of all sizes.
46 Prove that for some constant 𝑐 for any string 𝑥 and for every number 𝑛
there exists a string 𝑦 of length 𝑛 such that
𝐶(𝑥𝑦) > 𝐶(𝑥 | 𝑛) + 𝑛 − 𝑐.
[Hint: For a given 𝑛 the number of strings 𝑥 such that 𝐶(𝑥𝑦) < 𝑘 for any 𝑦 of
length 𝑛, does not exceed 2𝑘/2𝑛, and this property is enumerable. So we can apply
Theorem 19 (p. 50).]
47 Let 𝑓 be a function with natural arguments and values. Assume that
𝑓 (𝑛) + 𝜀ℎ 6 𝑓 (𝑛 + ℎ) 6 𝑓 (𝑛) + (1 − 𝜀)ℎ
for some 𝜀 > 0 and for all 𝑛 and ℎ. Prove that there exist an infinite bit sequence
𝜔 whose 𝑛-bit prefix has complexity 𝑓 (𝑛) + 𝑂(1) for every 𝑛.
[Hint: let us add blocks of length ℎ where ℎ is large enough. Each new block
being added to 𝑛-bit prefix increases complexity by more than 𝑓 (𝑛 + ℎ) − 𝑓 (𝑛) or
by less than 𝑓 (𝑛 + ℎ) − 𝑓 (𝑛), depending on the current situation (whether we are

<!-- page 55 -->

56 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
below or above the boundary). To find a block with big complexity increase we
may use the previous problem, for a block with small increase we can use a block
or zeros. Note that (large enough) ℎ is fixed, so it is enough to control complexity
on the blocks’ boundaries.]
48 Prove that an infinite sequence 𝑥0𝑥1𝑥2 . . . of zeros and ones is computable
if and only if the values 𝐶(𝑥0 . . . 𝑥𝑛−1 | 𝑛) (the complexities of its prefixes conditional
to their lengths) remain bounded by a constant.
[Hint: Consider an infinite binary tree. Let 𝑆 be the enumerable set of vertices
(binary strings) that have conditional complexity (w.r.t. their length) less than
some constant 𝑐. The “horizontal” sections of 𝑆 have cardinality 𝑂(1). We need to
derive from this that each infinite path that lies entirely inside 𝑆, is computable.
We may assume that 𝑆 is a subtree (only strings whose prefixes are in 𝑆, remain
in 𝑆).
Let 𝜔 be an infinite path that goes through 𝑆 only. At each level 𝑛 we count
vertices in 𝑆 on the left of 𝜔 (𝑙𝑛 vertices) and on the right of 𝜔 (𝑟𝑛 vertices). Let
𝐿 = lim sup 𝑙𝑛 and 𝑅 = lim sup 𝑟𝑛. Let 𝑁 be the level such that 𝐿 and 𝑅 are never
exceeded after this level. Knowing 𝐿, 𝑅 and 𝑁 we can compute arbitrarily large
prefixes of 𝜔. We should look for a path 𝜋 in a tree such that at some level above
𝑁 there are at least 𝐿 elements of 𝑆 on the left of 𝜋, and at some (possibly other)
level above 𝑁 there are at least 𝑅 elements on the right of 𝜋. When such a path 𝜋
is found, we can be sure that its initial segment (up to the first of those two levels)
coincides with 𝜔.]
This result was published in [107] (attributed to A.R. Meyer).
49 Prove that in the previous problem a weaker assumption is sufficient:
instead of 𝐶(𝑥0 . . . 𝑥𝑛−1 | 𝑛) = 𝑂(1) we can require that 𝐶(𝑥0 . . . 𝑥𝑛−1) 6 log 𝑛 + 𝑐
for some 𝑐 and for all 𝑛. [Hint: In this case we get an enumerable set 𝑆 of strings
(=tree vertices) with the following property: the number of vertices below level 𝑁
is 𝑂(𝑁 ). This means that the average number of vertices per level is bounded by a
constant. To use the previous problem, we need a bound for all levels and not for
the average value. We can achieve this if we consider only vertices 𝑥 ∈ 𝑆 that have
a extension of length 2𝑙(𝑥) that goes entirely inside 𝑆.]
This result was published in [33].
Following Problem 48, we can suggest different definitions of the complexity
notion for computable bit sequences:
∙ a minimal complexity of a program that, given 𝑛, computes 𝑥0 . . . 𝑥𝑛−1.
We can also consider a program that computes 𝑥𝑛 for input 𝑛, it gives the
same (up to 𝑂(1)) complexity. We denote this complexity by 𝐶(𝑥).
∙ a minimal complexity of a program that, given 𝑛, computes 𝑥0 . . . 𝑥𝑛 for
all sufficiently large 𝑛. For other 𝑛 (finitely many of them) this program
may provide a wrong answer or never terminate. It is denoted by 𝐶∞(𝑥).
∙ max{𝐶(𝑥0 . . . 𝑥𝑛−1 | 𝑛) | 𝑛 = 0, 1, . . . }, denoted by 𝑀 (𝑥).
∙ lim sup𝑛→∞ 𝐶(𝑥0 . . . 𝑥𝑛−1 | 𝑛), denoted by 𝑀∞(𝑥).
There are evident relations between these notions:
𝑀∞(𝑥) 6 𝑀 (𝑥) 6 𝐶(𝑥)
(up to 𝑂(1) additive term) and
𝑀∞(𝑥) 6 𝐶∞(𝑥) 6 𝐶(𝑥)

<!-- page 56 -->

2.2. CONDITIONAL COMPLEXITY 57
(with the same precision).
50 Prove that there exists a computable bit sequence 𝑥 such that 𝐶∞(𝑥) is
much less than 𝑀 (𝑥) (and, therefore, much less than 𝐶(𝑥)). More precisely, there
exists a sequence 𝑥𝑚 of computable sequences such that 𝐶∞(𝑥𝑚) = 𝑂(log 𝑚) and
𝑀 (𝑥𝑚) > 𝑚. [Hint: Consider the sequence 𝑥𝑚 = 𝑦𝑚000 . . . , where 𝑦𝑚 is the
lexicographically first string of length 𝑚 that has conditional complexity (given 𝑚)
at least 𝑚.]
51 Prove that for some computable sequence 𝑥 the value of 𝑀 (𝑥) is much
less than 𝐶(𝑥). More precisely, there exist a sequence 𝑥𝑚 of computable sequences
such that 𝑀 (𝑥𝑚) = 𝑂(log 𝑚) and 𝐶(𝑥𝑚) > 𝑚. [Hint: Consider the sequence
𝑥𝑚 = (1BB (𝑚)000 . . . ), where the number of 1s before trailing zeros equals BB (𝑚),
defined on p. 38.]
52 Prove that 𝐶∞(𝑥) 6 2𝑀∞(𝑥) + 𝑂(1). [Hint: Use the same argument as
in Problem 48.]
In fact, the constant 2 in the preceding problem is optimal, as shown in [52].
53 Consider strings of length 𝑛 that have complexity at least 𝑛 (incompressible
strings).
(a) Prove that the number of incompressible strings of length 𝑛 is between 2𝑛−𝑐
and 2𝑛 − 2𝑛−𝑐 (for some 𝑐 and for all 𝑛)
(b) Prove that the cardinality of the set of incompressible strings of length 𝑛
has complexity 𝑛 − 𝑂(1) (note that this implies the statement (a));
(c) Prove that if the string 𝑥 of length 2𝑛 is incompressible, then its halves 𝑥1
and 𝑥2 (of length 𝑛) have complexity 𝑛 − 𝑂(1).
(d) Prove that if a string 𝑥 of length 𝑛 is incompressible, then each its substring
of length 𝑘 has complexity at least 𝑘 − 𝑂(log 𝑛).
(e) Prove that for any constant 𝑐 < 1 all incompressible strings of sufficiently
large length 𝑛 contain a substring of ⌊𝑐 log2 𝑛⌋ zeros.
[Hints: (a) There is at most 2𝑛 − 1 descritions of length less than 𝑛. and part
of them is used for shorter strings: any string of length 𝑛 − 𝑑 (for some 𝑑) has
complexity less than 𝑛. This gives a lower bound for the number of uncompressible
strings. To prove the upper bound, note that strings of length 𝑛 that have prefix
of 𝑘 zeros, could be described by 2 log 𝑘 + (𝑛 − 𝑘) bits.
(b) Let 𝑡 be the shortest description of the number of incompressible strings. If
𝑡 has 𝑛 − 𝑘 bits, then knowing 𝑡 and log 𝑘 additional bits, we can reconstruct first 𝑛
and then the list of all incompressible strings of length 𝑛, so the first incompressible
string has complexity less than 𝑛, a contradiction.
(c) If one part of the string is has a short description, the entire string has a
short description that starts with prefix-free encoding of the difference between the
length and complexity of the compressible part.
(d) If a string has a simple substring, then the entire string can be compressed
(we need to specify the substring, its position and the rest of the string).
(e) Let us count the number of strings of length 𝑛 that do not contain 𝑘 zeros in
a row; a recurrent relation shows that this number grows like a geometric sequence
whose base is the maximal real root of the equation 𝑥 = 2 − (1/𝑥𝑘), and we can
get a bound for complexity of strings that do not have 𝑘 zeros in a row.]

<!-- page 57 -->

58 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
54 Prove that (for some constant 𝑐) for every infinite sequence 𝑥0𝑥1𝑥2 . . . of
zeros and ones there exist infinitely many 𝑛 such that
𝐶(𝑥0𝑥1 . . . 𝑥𝑛−1) 6 𝑛 − log 𝑛 + 𝑐.
Prove that there is a constant 𝑐 and the sequence 𝑥0𝑥1𝑥2 . . . such that
𝐶(𝑥0𝑥1 . . . 𝑥𝑛−1) > 𝑛 − 2 log 𝑛 − 𝑐
for all 𝑛. [Hint: The series∑︀ 1/𝑛 diverges while the series∑︀ (1/𝑛2) converges. For
details see Theorem 95 and 99.]
This result was published by Martin-L¨of [116] for conditional complexity (and
a reference to an earlier unpiblished work in Russian was given for unconditional
complexity; see also [223, Theorem 2.6]).
55 For a string 𝑥 of length 𝑛 let us define 𝑑(𝑥) and 𝑑𝑐(𝑥) as follows:
𝑑(𝑥) = 𝑛 − 𝐶(𝑥) and 𝑑𝑐(𝑥) = 𝑛 − 𝐶(𝑥 | 𝑛).
Show that they are rather close to each other:
𝑑𝑐(𝑥) − 2 log 𝑑𝑐(𝑥) − 𝑂(1) 6 𝑑(𝑥) 6 𝑑𝑐(𝑥) + 𝑂(1).
[Hint: We need to show that 𝐶(𝑥 | 𝑛) = 𝑛−𝑑 implies 𝐶(𝑥) 6 𝑛−𝑑+2 log 𝑑+𝑂(1).
Indeed, let us take the conditional description of 𝑥 of length 𝑛 − 𝑑 and put it after
the self-delimiting description of 𝑑 that has size 2 log 𝑑 + 𝑂(1). Knowing this string,
we can reconstruct 𝑑, then 𝑛 and finally 𝑥.]
56 Prove that 𝑑(𝑥𝑦) = 𝑑(𝑥)+𝑑(𝑦 | 𝑥)+𝑂(log 𝑑(𝑥𝑦)) for every two 𝑛-bit strings
𝑥 and 𝑦. (Here 𝑑(𝑢) = 𝑙(𝑢) − 𝐶(𝑢).) [Hint: use Problem 36.]
The intuitive meaning of the difference between length and complexity as a
kind of “randomness deficiency” is discussed (for different complexity versions) in
## Chapter 5 and Chapter 14.)
57 Prove that for sufficiently large values of a constant 𝑐 the enumerable set
of pairs (𝑥, 𝑦) such that 𝐶(𝑥 | 𝑦) < 𝑐, is Turing complete (one can solve halting
problem using an oracle for such a set). [Hint: Use Problem 15 and the fact that
the output of a program has 𝑂(1) conditional complexity given the program.]
### 2.3. Complexity as the amount of information
As we know (Theorem 18), the conditional complexity 𝐶(𝑦|𝑥) does not exceed
the unconditional one 𝐶(𝑦) (up to a constant). The difference 𝐶(𝑦) − 𝐶(𝑦|𝑥) tells
us how much the knowledge of 𝑦 makes 𝑥 easier to describe. So this difference can
be called the amount of information in 𝑥 about 𝑦. Notation: 𝐼(𝑥 : 𝑦).
Theorem 18 says that 𝐼(𝑥 : 𝑦) is non-negative (up to a constant): there exists
some 𝑐 such that 𝐼(𝑥 : 𝑦) > 𝑐 for all 𝑥 and 𝑦.
58 Let 𝑓 be a computable function. Prove that 𝐼(𝑓 (𝑥) : 𝑦) 6 𝐼(𝑥 : 𝑦) + 𝑐 for
some 𝑐 and for all 𝑥, 𝑦 such that 𝑓 (𝑥) is defined.
A generalization of this statement to probabilistic algorithms is possible.
59 Let 𝑓 (𝑥, 𝑟) be a computable function of two arguments, and 𝑟 is chosen at
random uniformly among 𝑛-bit strings for some 𝑛. Then for each 𝑙 the probability
of the event
𝐼(𝑓 (𝑥, 𝑟) : 𝑦) > 𝐼(𝑥 : 𝑦) + 𝑙
does not exceed 2−𝑙+𝑂(𝐶(𝑛)+𝐶(𝑙)). [Hint: Use the conditional version of Problem 41.]

<!-- page 58 -->

2.3. COMPLEXITY AS THE AMOUNT OF INFORMATION 59
These properties of information can be described as “conservation laws” for
information (about something) in algorithmic or random processes. As Leonid
Levin once put it: “by torturing an uninformed person you do not get any evidence
about the crime”. He discusses this property (for different notion of information)
in [99].
Recall that
𝐶(𝑥, 𝑦) = 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) + 𝑂(log 𝐶(𝑥, 𝑦)),
(Theorem 22, p. 53). This allows us to express conditional complexity in terms of
unconditional one: 𝐶(𝑦 | 𝑥) = 𝐶(𝑥, 𝑦) − 𝐶(𝑥) + 𝑂(log 𝐶(𝑥, 𝑦)). Then we get the
following expression for the information:
𝐼(𝑥 : 𝑦) = 𝐶(𝑦) − 𝐶(𝑦 | 𝑥) = 𝐶(𝑥) + 𝐶(𝑦) − 𝐶(𝑥, 𝑦) + 𝑂(log 𝐶(𝑥, 𝑦)).
This expression immediately implies the following theorem:
Theorem 23 (information symmetry).
𝐼(𝑥 : 𝑦) = 𝐼(𝑦 : 𝑥) + 𝑂(log 𝐶(𝑥, 𝑦))
So the difference between 𝐼(𝑥 : 𝑦) and 𝐼(𝑦 : 𝑥) is logarithmically small compared
to 𝐶(𝑥, 𝑦). The following problem shows that at the same time this difference could
be comparable with the values 𝐼(𝑥 : 𝑦) and 𝐼(𝑦 : 𝑥) if they are much less than 𝐶(𝑥, 𝑦).
60 Let 𝑥 be a string of length 𝑛 such that 𝐶(𝑥 | 𝑛) > 𝑛. Show that
𝐼(𝑥 : 𝑛) = 𝐶(𝑛) + 𝑂(1) and 𝐼(𝑛 : 𝑥) = 𝑂(1).
The property of information symmetry (up to a logarithmic term) explains
why 𝐼(𝑥 : 𝑦) (or 𝐼(𝑦 : 𝑥)) is sometimes called mutual information in two strings 𝑥
and 𝑦. The connection between mutual information, conditional and unconditional
complexities and pair complexity can be illustrated by a (rather symbolic) picture
(Fig. 2).
𝐶(𝑥 | 𝑦) 𝐶(𝑦 | 𝑥)
𝐼(𝑥 : 𝑦)
𝑥 𝑦
Figure 2. Mutual information and conditional complexity
It shows that strings 𝑥 and 𝑦 have 𝐼(𝑥 : 𝑦) ≈ 𝐼(𝑦 : 𝑥) bits of mutual information.
Adding 𝐶(𝑥 | 𝑦) bits (information that is present in 𝑥 but not in 𝑦, the left part),
we obtain
𝐼(𝑦 : 𝑥) + 𝐶(𝑥 | 𝑦) ≈ (𝐶(𝑥) − 𝐶(𝑥 | 𝑦)) + 𝐶(𝑥 | 𝑦) = 𝐶(𝑥)
bits (matching the complexity of 𝑥). Similarly, the central part together with
𝐶(𝑦 | 𝑥) (the right part) give 𝐶(𝑦). Finally, all three parts together give us
𝐶(𝑥 | 𝑦) + 𝐼(𝑥 : 𝑦) + 𝐶(𝑦 | 𝑥) = 𝐶(𝑥) + 𝐶(𝑦 | 𝑥) = 𝐶(𝑥 | 𝑦) + 𝐶(𝑦) = 𝐶(𝑥, 𝑦)
bits (all equalities are true up to 𝑂(log 𝑛) for strings 𝑥 and 𝑦 of length at most 𝑛).
In some cases this picture can be understood quite literally. Consider, for
instance, an incompressible string 𝑟 = 𝑟1 . . . 𝑟𝑛 of length 𝑛, so 𝐶(𝑟1 . . . 𝑟𝑛) > 𝑛.

<!-- page 59 -->

60 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
Then any substring 𝑢 of 𝑥 has complexity 𝑙(𝑢) up to 𝑂(log 𝑛) terms. Indeed, since
𝑢 is a substring of 𝑟, we have 𝑟 = 𝑡𝑢𝑣 for some strings 𝑡, 𝑣. Then
𝑙(𝑟) = 𝐶(𝑟) 6 𝐶(𝑡) + 𝐶(𝑢) + 𝐶(𝑣) 6 𝑙(𝑡) + 𝑙(𝑢) + 𝑙(𝑣) = 𝑙(𝑟)
(up to a logarithmic error) and therefore all the inequalities are equalities (with the
same logarithmic precision).
Now take two overlapping substrings 𝑥 and 𝑦 (Fig. 3). Then 𝐶(𝑥) is the length
of 𝑥, 𝐶(𝑦) is the length of 𝑦 (up to 𝑂(log 𝑛)).
𝑥 : 𝑦	𝑥 | 𝑦 𝑦 | 𝑥
𝑥 𝑦
𝑥, 𝑦
Figure 3. Common information in overlapping substrings
The complexity 𝐶(𝑥, 𝑦) is equal to the length of the union of segments (since
the pair ⟨𝑥, 𝑦⟩ is equivalent to this union plus information about lengths requiring
𝑂(log 𝑛) bits).
Therefore, conditional complexities 𝐶(𝑥 | 𝑦), 𝐶(𝑦 | 𝑥) and the mutual informa-
tion 𝐼(𝑥 : 𝑦) are equal to the lengths of the corresponding segments (up to 𝑂(log 𝑛)).
However, not always the mutual information can be extracted in form of some
string (like it happened in our example, where this common information is just the
intersection of strings 𝑥 and 𝑦). As we will see in Chapter 11, there exist two strings
𝑥 and 𝑦 that have large mutual information 𝐼(𝑥 : 𝑦) but there is no string 𝑧 that
represents (“materializes”) this information in the following sense: 𝐶(𝑧 | 𝑥) ≈ 0,
𝐶(𝑧 | 𝑦) ≈ 0 (all information that is present in 𝑧 is also present both in 𝑥 and in 𝑦)
and 𝐶(𝑧) ≈ 𝐼(𝑥 : 𝑦) (all mutual information is extracted). In our last example we
can take the intersection substring for 𝑧, but in general this is not possible.
61 Prove that for any string 𝑥 of length at most 𝑛 the expected value of the
mutual information 𝐼(𝑥 : 𝑦) in 𝑥 and random string 𝑦 of length 𝑛 is 𝑂(log 𝑛).
Now we move to triples of strings instead of pairs. Here we have an important
tool that can be called relativization: most of the results proved for unconditional
complexities remain valid for conditional complexities (and proofs remain valid with
minimal changes). Let us give some example of this type.
A theorem about the complexity of pairs (p. 45) says that
𝐶(𝑥, 𝑦) 6 𝐶(𝑥) + 2 log 𝐶(𝑥) + 𝐶(𝑦) + 𝑂(1).
Replacing all complexities by conditional ones (with the same condition 𝑧 in all
cases), we get the following inequality:
𝐶(𝑥, 𝑦 | 𝑧) 6 𝐶(𝑥 | 𝑧) + 2 log 𝐶(𝑥 | 𝑧) + 𝐶(𝑦 | 𝑧) + 𝑂(1),
By conditional complexity of a pair 𝑥, 𝑦 relative to 𝑧 we mean, as one can expect,
the conditional complexity of its encoding: 𝐶(𝑥, 𝑦 | 𝑧) = 𝐶([𝑥, 𝑦] | 𝑧). As for un-
conditional complexity, the choice of encoding is not important (the complexity
changes by 𝑂(1)).

<!-- page 60 -->

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

<!-- page 61 -->

62 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
inequalities for complexities that do not follow from basic inequalities were found
fairly recently (see [220, 221]) and they are rather complicated and not very intu-
itive. We discuss them in Section 10.13; we conclude this discussion by two simple
corollaries of basic inequalities.
Independent strings. We say that strings 𝑥 and 𝑦 are “independent” if
𝐼(𝑥 : 𝑦) ≈ 0. We need to specify what we mean by “≈”, but we always ignore the
terms of order 𝑂(log 𝑛) where 𝑛 is the maximal length (or complexity) of the strings
involved.
Independent strings could be considered as some counterpart of the notion of
independent random variables, which is central in the probability theory. There is
a simple observation: if a random variable 𝜉 is independent with the pair of random
variables ⟨𝛼, 𝛽⟩, then 𝜉 is independent with 𝛼 and with 𝛽 (separately).
The Kolmogorov complexity counterpart of this statement (if a string 𝑥 is
independent with a pair ⟨𝑦, 𝑧⟩, then 𝑥 is independent with 𝑦 and 𝑥 is independent
with 𝑧) can be expressed as an inequality:
𝐼(𝑥 : ⟨𝑦, 𝑧⟩) > 𝐼(𝑥 : 𝑦)
(and the similar inequality for 𝑧 instead of 𝑦). This inequality is indeed true (with
logarithmic precision), and it is easy to see if we rewrite it in terms of unconditional
complexities:
𝐶(𝑥) + 𝐶(𝑦, 𝑧) − 𝐶(𝑥, 𝑦, 𝑧) > 𝐶(𝑥) + 𝐶(𝑦) − 𝐶(𝑥, 𝑦),
which after cancellation of similar terms gives a basic inequality (Theorem 24). (In
classical probability theory one may also apply a similar inequality for Shannon
entropies.)
Complexity of pairs and triples. On the other hand, to prove the following
theorem (which we have already mentioned on p.22), it is convenient to replace
unconditional complexities by conditional ones:
Theorem 26.
2𝐶(𝑥, 𝑦, 𝑧) 6 𝐶(𝑥, 𝑦) + 𝐶(𝑥, 𝑧) + 𝐶(𝑦, 𝑧) + 𝑂(log 𝑛),
for all strings 𝑥, 𝑦, 𝑧 of complexity at most 𝑛.
Proof. Moving 𝐶(𝑥, 𝑦) and 𝐶(𝑥, 𝑧) to the left-hand side and replacing the
differences 𝐶(𝑥, 𝑦, 𝑧) − 𝐶(𝑥, 𝑦) and 𝐶(𝑥, 𝑦, 𝑧) − 𝐶(𝑥, 𝑧) by conditional complexities
𝐶(𝑧 | 𝑥, 𝑦) and 𝐶(𝑦 | 𝑥, 𝑧), we get the following inequality:
𝐶(𝑧 | 𝑥, 𝑦) + 𝐶(𝑦 | 𝑥, 𝑧) 6 𝐶(𝑦, 𝑧) + 𝑂(log 𝑛).
It remains to rewrite the right-hand side of this inequality as 𝐶(𝑦) + 𝐶(𝑧 | 𝑦), and
note that 𝐶(𝑧 | 𝑥, 𝑦) 6 𝐶(𝑧 | 𝑦) and 𝐶(𝑦 | 𝑥, 𝑧) 6 𝐶(𝑦). 
Instead we could just add two inequalities (the basic one and the inequality for
the complexity of a pair):
𝐶(𝑥, 𝑦, 𝑧) + 𝐶(𝑦) 6 𝐶(𝑥, 𝑦) + 𝐶(𝑦, 𝑧) + 𝑂(log 𝑛),
𝐶(𝑥, 𝑦, 𝑧) 6 𝐶(𝑦) + 𝐶(𝑥, 𝑧) + 𝑂(log 𝑛),
and then cancel 𝐶(𝑦) in both sides. (This proof, as well as the previous one, has
an important esthetic problem: both treat 𝑥, 𝑦, 𝑧 in a non-symmetric way while the
statement of the theorem is symmetric.)

<!-- page 62 -->

2.3. COMPLEXITY AS THE AMOUNT OF INFORMATION 63
We return to the inequality of Theorem 26 and to its geometric consequences
in Chapter 10.
We can provide a more systematic treatment of the different complexity quan-
tities related to three strings as follows. There are seven basic quantities: three
of them are complexities of individual strings, another three are complexities of
pairs and one more is the complexity of the entire triple. Other quantities such as
conditional complexity and mutual information can be expressed in terms of these
seven complexities. To understand better what requirements these seven quantities
should satisfy, let us make a linear transformation in the 7-dimensional space and
switch to new coordinates. Consider seven variables 𝑎1, 𝑎2, . . . , 𝑎7 that correspond
to 7 regions shown in Fig. 4.
𝑥 𝑦
𝑧
1 2 3
4 5 6
7
Figure 4. New coordinates 𝑎1, 𝑎2, . . . , 𝑎7.
Formally, the coordinate transformation is given by the following equations:
𝐶(𝑥) = 𝑎1 + 𝑎2 + 𝑎4 + 𝑎5,
𝐶(𝑦) = 𝑎2 + 𝑎3 + 𝑎5 + 𝑎6,
𝐶(𝑧) = 𝑎4 + 𝑎5 + 𝑎6 + 𝑎7,
𝐶(𝑥, 𝑦) = 𝑎1 + 𝑎2 + 𝑎3 + 𝑎4 + 𝑎5 + 𝑎6,
𝐶(𝑥, 𝑧) = 𝑎1 + 𝑎2 + 𝑎4 + 𝑎5 + 𝑎6 + 𝑎7,
𝐶(𝑦, 𝑧) = 𝑎2 + 𝑎3 + 𝑎4 + 𝑎5 + 𝑎6 + 𝑎7,
𝐶(𝑥, 𝑦, 𝑧) = 𝑎1 + 𝑎2 + 𝑎3 + 𝑎4 + 𝑎5 + 𝑎6 + 𝑎7.
Indeed, it is easy to see that these equations determine an invertible linear transfor-
mation of R7: each 7-tuple of complexities corresponds to unique value of variables
𝑎1, . . . , 𝑎7.
Conditional complexities and mutual informations could be expressed in terms
of complexities and therefore could be rewritten in new coordinates. For example,
𝐼(𝑥 : 𝑦) = 𝐶(𝑥) + 𝐶(𝑦) − 𝐶(𝑥, 𝑦) = 𝑎2 + 𝑎5 and 𝐶(𝑥 | 𝑦) = 𝐶(𝑥, 𝑦) − 𝐶(𝑦) = 𝑎1 + 𝑎4.
What is the intuitive meaning of these new coordinates? It is easy to see that
𝑎1 = 𝐶(𝑥 | 𝑦, 𝑧) (with logarithmic precision). The meaning of 𝑎3 (and 𝑎7) is similar.
The coordinate 𝑎2 is (with the same precision) 𝐼(𝑥 : 𝑦 | 𝑧); coordinates 𝑎4 and 𝑎6
have similar meaning (see Fig. 5). In particular, we conclude that for any strings
𝑥, 𝑦, 𝑧 the corresponding values of coordinates 𝑎1, 𝑎2, 𝑎3, 𝑎4, 𝑎6, 𝑎7 are non-negative
(up to 𝑂(log 𝑛) for strings 𝑥, 𝑦, 𝑧 of complexity at most 𝑛).
The coordinate 𝑎5 is more delicate. Informally, we would like to understand
it as the “amount of mutual information in three strings 𝑥, 𝑦, 𝑧”. Sometimes the

<!-- page 63 -->

64 2. COMPLEXITY OF PAIRS AND CONDITIONAL COMPLEXITY
𝑥 𝑦
𝑧
𝐶(𝑥 | 𝑦, 𝑧)
𝐼(𝑥 : 𝑦 | 𝑧) 𝐶(𝑦 | 𝑥, 𝑧)
𝐼(𝑥 : 𝑧 | 𝑦)
𝐼(𝑥 : 𝑦 : 𝑧)
𝐼(𝑦 : 𝑧 | 𝑥)
𝐶(𝑧 | 𝑥, 𝑦)
Figure 5. The complexity interpretation of new coordinates.
notation 𝐼(𝑥 : 𝑦 : 𝑧) is used. However, the meaning of this expression is not quite
clear, especially if we take into accout that 𝑎5 can be negative.
Consider the following example where 𝑎5 < 0. Let 𝑥 and 𝑦 be two halves of
an incompressible strings of length 2𝑛. Then 𝐶(𝑥) = 𝑛, 𝐶(𝑦) = 𝑛, 𝐶(𝑥, 𝑦) = 2𝑛
and 𝐼(𝑥 : 𝑦) = 0 (up to 𝑂(log 𝑛)). Consider a string 𝑧 of length 𝑛 which is a bitwise
sum modulo 2 of 𝑥 and 𝑦 (XOR-operation). Then each of the strings 𝑥, 𝑦, 𝑧 can
be reconstructed if two others are known; therefore the complexities of all pairs
𝐶(𝑥, 𝑦), 𝐶(𝑦, 𝑧), 𝐶(𝑥, 𝑧) are equal to 2𝑛 (again up to 𝑂(log 𝑛)), and the complexity
𝐶(𝑥, 𝑦, 𝑧) is also 2𝑛. The complexity of 𝑧 is equal to 𝑛 (it can not be larger, since
the length is 𝑛; on the other hand, it cannot be smaller, since 𝑧 and 𝑦 form a pair
of complexity 2𝑛).
So we get the following values of 𝑎1, . . . , 𝑎7 for this example (Fig. 6):
0 𝑛 0
𝑛 −𝑛 𝑛
0
Figure 6. Two independent incompressible strings of length 𝑛
and their XOR.
Note that even if 𝑎5 is negative, the sums 𝑎5 + 𝑎2, 𝑎5 + 𝑎4 and 𝑎5 + 𝑎6, being
mutual informations for pairs, are non-negative. (In our examples these sums are
equal to 0.)
This example corresponds to the simple case of secret sharing of secret 𝑧 be-
tween two people: if one of them knows 𝑥 and the other one knows 𝑦, then none of

<!-- page 64 -->

2.3. COMPLEXITY AS THE AMOUNT OF INFORMATION 65
them has any information about 𝑧 in isolation (since 𝐼(𝑥 : 𝑧) ≈ 0 and 𝐼(𝑦 : 𝑧) ≈ 0)),
but together they can reconstruct 𝑧 as a bitwise sum of 𝑥 and 𝑦.
One can check that we have already given a full list of inequalities that are true
for complexities of three strings and their combinations (all 𝑎𝑖, except for 𝑎5, are
non-negative, as well as three sums mentioned above). We return to this question
in Chapter 10.
Our diagram is a good mnenonic tool. For example, consider again the inequal-
ity
𝐶(𝑥, 𝑦, 𝑧) 6 𝐶(𝑥, 𝑦) + 𝐶(𝑥, 𝑧) + 𝐶(𝑦, 𝑧).
In our new variables it can be rewritten as 𝑎2 + 𝑎4 + 𝑎5 + 𝑎6 > 0 (you can easily
check it by counting the multiplicity of each 𝑎𝑖 in both sides of the inequality). It
remains to note that 𝑎2 + 𝑎5 > 0, 𝑎4 > 0 and 𝑎6 > 0. (Alas, the symmetry is broken
again!)
63 Prove that 𝐼(𝑥𝑦 : 𝑧) = 𝐼(𝑥 : 𝑧) + 𝐼(𝑦 : 𝑧 | 𝑥) + 𝑂(log 𝑛) for strings 𝑥, 𝑦, 𝑧 of
complexity at most 𝑛. [Hint: Use the diagram.]
This problem shows that information in 𝑥𝑦 about 𝑧 can be somehow split into
two parts: information in 𝑥 about 𝑧 and information in 𝑦 about 𝑧 (when 𝑥 is
known). This is somehow similar to the equality 𝐶(𝑥, 𝑦) = 𝐶(𝑥) + 𝐶(𝑦 | 𝑥), but now
complexity is replaced by the quantity of information about 𝑧. As a corollary we
immediately get that if 𝑥𝑦 is independent with 𝑧 then 𝑥 in independent with 𝑧 and,
at the same time 𝑦 is independent with 𝑧 when 𝑥 is known. (Here independence
means that mutual information is negligible.) A symmetric argument shows that 𝑦
is independent with 𝑧 and 𝑥 is independent with 𝑧 when 𝑦 is known.
64 Show that properties “𝑥 is independent with 𝑦” and “𝑥 is independent
with 𝑦 when 𝑧 is known” are quite different: each of them can be true when the
other one is false.
65 We say that strings 𝑥, 𝑦, 𝑧, 𝑡 form a Markov chain (a well known notion
in the probability theory now transferred to the algorithmic information theory) if
𝐼(𝑥 : 𝑧 | 𝑦) and 𝐼(⟨𝑥, 𝑦⟩ : 𝑡 | 𝑧) are negligible. (Of course, we need to specify what is
“negligible” to get a formal definition.) Show that the reversed sequence of strings
also forms a Markov chain, i.e., that 𝐼(𝑡 : 𝑦 | 𝑧) and 𝐼(⟨𝑡, 𝑧⟩ : 𝑥 | 𝑦) are negligible. [Hint:
Since 𝐼(⟨𝑥, 𝑦⟩ : 𝑡 | 𝑧) = 𝐼(𝑦 : 𝑡 | 𝑧) + 𝐼(𝑥 : 𝑡 | 𝑦, 𝑧), the left hand side in this equality is
zero if and only if both terms in the right hand side are zero; and the second term
in the right-hand side does not change when the order of 𝑥, 𝑦, 𝑧, 𝑡 is reversed.]

<!-- page 65 -->

<!-- page 66 -->

CHAPTER 3
Martin-L¨	of randomness
Here we interrupt the exposition of Kolmogorov complexity and its properties
and define another basic notion of the algorithmic information theory, the notion
of Martin-L¨of random (or “typical”) sequence. This chapter does not refer to the
preceding one and is not used until Chapter 5 where we characterize randomness
in terms of Kolmogorov complexity.
Let us recall some basic facts of measure theory for the case of the Cantor space
of infinite sequences of zeros and ones.
### 3.1. Measures on Ω
Consider the set Ω = BN whose elements are infinite sequences of zeros and
ones. This set is called Cantor space. For a binary string 𝑥 we consider a set Ω𝑥 of
all infinite sequences that have initial segment 𝑥. For example, Ω00 is the set of all
sequences that start with two zeros, and ΩΛ = Ω (where Λ is the empty string).
The sets Ω𝑥 are called intervals. All intervals and all unions of arbitrary families
of intervals are called open subsets of Ω. In this way we get a topology on Ω, and
this topology corresponds to a standard distance function on Ω defined as follows:
the longer common prefix two sequences 𝜔 = 𝜔0𝜔1 . . . and 𝜔′ = 𝜔′
0𝜔′
1 . . . have, the
smaller the distance between them is:
𝑑(𝜔, 𝜔′) = 2−𝑛,
where 𝑛 is the smallest index such that 𝜔𝑛̸ = 𝜔′
𝑛.
66 Prove that topological space Ω is homeomorphic to the Cantor set on the
real line. (This set is obtained from [0, 1] by deleting the middle third, then the
middle thirds of two remaining segments and so on.)
However, we are interested in measure theory rather than topology. A family
of subsets of Ω is called a 𝜎-algebra if it is closed under finite or countable unions
and intersections, and under negation (taking the complement).
A minimal 𝜎-algebra that contains all intervals Ω𝑥 (and therefore all open sets)
is called the algebra of Borel sets.
Consider an arbitrary 𝜎-algebra that contains all intervals. Let 𝜇 be a function
that maps every set in this 𝜎-algebra into a non-negative real number, and has the
following property (called 𝜎-additivity):
if a set 𝐴 is a union of a countable or finite family of disjoint
sets 𝐴0, 𝐴1, 𝐴2, . . . that belong to the 𝜎-algebra on which 𝜇 is
defined, then
𝜇(𝐴) = 𝜇(𝐴0) + 𝜇(𝐴1) + 𝜇(𝐴2) + . . .
(the right-hand side is a finite sum or a converging series with
non-negative terms).
67

<!-- page 67 -->

68 3. MARTIN-L ¨OF RANDOMNESS
Then 𝜇 is called a measure on Ω, and the value 𝜇(𝐴) is called the measure of the
set 𝐴. The set 𝐴 for which 𝜇(𝐴) is defined, is called 𝜇-measurable.
A measure 𝜇 such that 𝜇(Ω) = 1 is called a probability distribution on Ω.
Elements of the 𝜎-algebra that is the domain of 𝜇 are called events, and 𝜇(𝐴) is
called the probability of the event 𝐴.
Any measure is monotone (𝐴 ⊂ 𝐵 implies 𝜇(𝐴) 6 𝜇(𝐵)). Indeed,
𝜇(𝐵) − 𝜇(𝐴) = 𝜇(𝐵 ∖ 𝐴) > 0.
Another important property of measures is continuity: if a set 𝐵 is a union of
increasing sequence of sets
𝐵0 ⊂ 𝐵1 ⊂ 𝐵2 ⊂ . . . ,
then 𝜇(𝐵𝑛) tends to 𝜇(𝐵) as 𝑛 → ∞. (Indeed, let us apply the additivity property
to all sets 𝐴𝑖 = 𝐵𝑖 ∖ 𝐵𝑖−1 and then to all sets 𝐴𝑖 such that 𝑖 6 𝑛.) The similar
property holds for decreasing sequences of sets.
For any measure 𝜇 on Ω let us consider a function 𝑝 defined of binary strings
as follows:
𝑝(𝑥) = 𝜇(Ω𝑥).
This function has non-negative real values and satisfies the following additivity
property:
𝑝(𝑥) = 𝑝(𝑥0) + 𝑝(𝑥1)
for any string 𝑥. (Indeed, the interval Ω𝑥 is the union of its two halves Ω𝑥0 and
Ω𝑥1, which are disjoint sets.)
As we know from measure theory (Lebesgue’s theorem), an inverse transition
is possible. Namely, for every additive function 𝑝 on binary strings that has non-
negative real values, the Lebesgue theorem provides a measure 𝜇 such that 𝜇(Ω𝑥) =
𝑝(𝑥) for all binary strings 𝑥.
The measure provided by Lebesgue theorem has the following additional prop-
erty: if 𝜇(𝐴) = 0 for some set 𝐴 and 𝐵 ⊂ 𝐴, then 𝜇(𝐵) is defined (and therefore
𝜇(𝐵) = 0). In the sequel we consider only measures that have this additional
property.
We do not explain Lebesgue’s construction here and refer the reader to any
textbook in measure theory, e.g., [80, 63]. However, let us recall the definition of
sets having measure 0, since Martin-L¨of definition of randomness uses its effective
version.
Let 𝑝 be an additive nonnegative real-valued function on strings. We call 𝑝(𝑥)
the measure of the interval Ω𝑥. A subset 𝐴 ⊂ Ω is a null set (a set of measure 0)
if for every 𝜀 > 0 there exist a finite or countable family of intervals that cover 𝐴
and have total measure at most 𝜀.
In other words, a set 𝐴 is a null set if there exists a function ⟨𝜀, 𝑖⟩ ↦ → 𝑥(𝜀, 𝑖)
(first argument is a positive real, the second argument is a non-negative integer;
values are binary strings) such that
∙ 𝐴 ⊂ Ω𝑥(𝜀,0) ∪ Ω𝑥(𝜀,1) ∪ Ω𝑥(𝜀,2) . . . and
∙ 𝑝(𝑥(𝜀, 0)) + 𝑝(𝑥(𝜀, 1)) + 𝑝(𝑥(𝜀, 2)) + . . . 6 𝜀
for every positive 𝜀. Note that the family of intervals can be finite, since we do not
require the function 𝑥 to be total (undefined values are skipped both in the union
and in the sum).
Here are some simple but useful observations:

<!-- page 68 -->

3.2. THE STRONG LAW OF LARGE NUMBERS 69
∙ The definition does not change if we restrict ourselves to rational values
of 𝜀 (or even let 𝜀 = 2−𝑘 for integer 𝑘).
∙ Any subset of a null set is a null set.
∙ A finite or countable union of null sets is a null set. (Indeed, to cover the
union by a family of intervals of total measure less than 𝜀, we combine
the covers of its parts that have measure less than 𝜀/2, 𝜀/4, 𝜀/8 etc.).
∙ Assume that 𝑝 is chosen in such a way that any singleton is a null set
(it is equivalent to the following property: for any infinite sequence 𝜔 =
𝜔0𝜔1𝜔2 . . . the limit of 𝑝(𝜔0 . . . 𝜔𝑛) (as 𝑛 → ∞) equals 0). Then every
finite or countable set is a null set.
A uniform measure on Ω assigns to each interval Ω𝑥 the number 2−𝑙(𝑥):
𝑝(𝑥) = 2−𝑛 for all strings 𝑥 of length 𝑛.
The uniform measure is closely related to the standard measure on R (or, more
precisely, on [0, 1]). Formally, the measure of a set 𝐴 ⊂ Ω is equal to the measure
of the set of reals whose binary expansions are elements of 𝐴. (In fact, the cor-
respondence between infinite binary fractions and reals in [0, 1] is not a bijection,
since numbers of the form 𝑘/2𝑙 for integer 𝑘 and 𝑙 have two representations: e.g.,
0.01111 . . . = 0.10000 . . . But this happens only for a countable family of reals and
measure theory easily ignores this.)
Indeed, the reals whose binary expansions start with 𝑥, form an interval, and
the length of this interval is 2−𝑛 where 𝑛 is the length of 𝑥. This implies that for
every interval 𝐼 ⊂ [0, 1] the uniform measure of the sequences that represent reals
in 𝐼 is equal to the length of the interval 𝐼.
Probability theory describes the uniform distribution as the probability distri-
bution for the outcomes of independent fair coin tossing. Indeed, for 𝑛 independent
fair coin tossings all 2𝑛 binary strings of length 𝑛 appear with the same probability
2−𝑛. The set Ω𝑥 is the event “a random sequence of zeros and ones starts with 𝑥”,
and this event has probability 2−𝑙(𝑥).
Similarly, we may consider a biased coin assuming that coin tossings are still in-
dependent. The corresponding measure (probability distribution) is called Bernoulli
measure (or Bernoulli distribution) with parameters 𝑞, 𝑝 (probabilities of 0 and 1
respectively; we assume that 𝑝, 𝑞 > 0, and 𝑝 + 𝑞 = 1).
With respect to this distribution, the event “sequence 𝜔 starts with a string
𝑥” has probability 𝑞𝑢𝑝𝑣 where 𝑢 and 𝑣 are the numbers of zeros and ones in 𝑥. In
other terms, we consider a function
𝑥 ↦ → 𝑞𝑢(𝑥)𝑝𝑣(𝑥)
where 𝑢(𝑥) and 𝑣(𝑥) stand for the numbers of zeros and ones in 𝑥, respectively. (It
is easy to check that this function has the additivity property.)
### 3.2. The Strong Law of Large Numbers
To see all these notions in action, let us state and prove the so-called Strong
Law of Large Numbers.
Fix some 𝑝, 𝑞 > 0 such that 𝑝 + 𝑞 = 1. Let 𝐴𝑝 be the set of all infinite sequences
𝜔0𝜔1𝜔2 . . . of zeros and ones such that limit frequency of ones exists and is equal
to 𝑝, i.e.,
lim
𝑛→∞
𝜔0 + 𝜔1 + . . . + 𝜔𝑛−1
𝑛 = 𝑝.

<!-- page 69 -->

70 3. MARTIN-L ¨OF RANDOMNESS
Theorem 27. The set 𝐴𝑝 has measure 1 with respect to Bernoulli distribution
with parameters 𝑝 and 𝑞.
In other terms, the complement of 𝐴𝑝, i.e., the set of all sequences that either
do not have limit frequency at all or have a limit frequency different from 𝑝, is a
null set (according to this distribution).
Proof. We prove this theorem for the uniform case (i.e., for 𝑝 = 𝑞 = 1/2) by
an explicit calculation. The general case is left as an exercise (see also Section 9.6).
Let us consider first a finite number of coin tossings and fix some 𝑛. All
binary strings of length 𝑛 have the same probability. We claim that most of them
have approximately 𝑛/2 ones. Assume that some threshold 𝜀 is fixed. How many
sequences have more than (1/2 + 𝜀)𝑛 ones? The answer can be found using the
Pascal triangle: we have to sum up all the terms in the 𝑛th row starting from some
point that is slightly on the right of the midpoint. In this part we have a decreasing
sequence of less than 𝑛 terms, so the sum in question is bounded by the first term
multiplied by 𝑛. (We do not need to be very accurate in our bounds and ignore
factors that are polynomial in 𝑛. So we can omit the factor 𝑛 in our bound.)
The first term of the sum is the binomial coefficient
𝑛!
𝑘!(𝑛 − 𝑘)! ,
where 𝑘 is the smallest integer not less than (1/2 + 𝜀)𝑛. We use the Stirling’s
approximation:
𝑚! =√︀ (2𝜋 + 𝑜(1))𝑚
(︁
 
𝑚
𝑒
)︁
𝑚
,
where 𝑒 is the base of natural logarithms. Ignoring polynomial (in 𝑛) factors and
using the notation 𝑢 = 𝑘/𝑛, 𝑣 = (𝑛 − 𝑘)/𝑛, we get
𝑛!
𝑘!(𝑛 − 𝑘)! ≈ (𝑛/𝑒)𝑛
(𝑘/𝑒)𝑘((𝑛 − 𝑘)/𝑒)𝑛−𝑘 = 𝑛𝑛
𝑘𝑘(𝑛 − 𝑘)𝑛−𝑘 =
= 𝑛𝑛
(𝑢𝑛)𝑢𝑛(𝑣𝑛)𝑣𝑛 = 1
𝑢𝑢𝑛𝑣𝑣𝑛 = 2𝐻(𝑢,𝑣)𝑛,
where
𝐻(𝑢, 𝑣) = −𝑢 log 𝑢 − 𝑣 log 𝑣.
The value 𝐻(𝑢, 𝑣) is called the Shannon entropy of the random variable that has
two values whose probabilities are 𝑢 and 𝑣. (We study the Shannon entropy in
Chapter 7.) Figure 1 shows the corresponding graph (note that 𝑣 = 1 − 𝑢). It
is easy to check that 𝐻(𝑢, 1 − 𝑢) achieves its maximal value (equal to 1) only
at 𝑢 = 1/2.
Now we see that the number of binary strings of length 𝑛 that have frequency of
ones greater than (1/2 + 𝜀) does not exceed poly(𝑛)2𝐻(1/2+𝜀,1/2−𝜀)𝑛 and therefore
is bounded by 2𝑐𝑛+𝑜(𝑛), where 𝑐 is some constant less than 1 (depending on 𝜀).
Therefore, the fraction of these strings (among all strings of length 𝑛) exponentially
decreases as 𝑛 increases. The same is true for the strings that have frequency of
ones less than (1/2 − 𝜀).
Let us see where we are. For each fixed 𝜀 > 0 we have proved the following
statement:

<!-- page 70 -->

3.2. THE STRONG LAW OF LARGE NUMBERS 71
0 1	1/2 𝑢
1
𝐻(𝑢, 1 − 𝑢)
Figure 1. Shannon entropy as a function of 𝑢.
Lemma. The fraction of strings of length 𝑛 where frequency of ones differs
from 1/2 at least by 𝜀 (among all strings of length 𝑛) does not exceed some 𝛿𝑛 that
decreases exponentially as 𝑛 increases.
This lemma (without any specific claims for the fast convergence 𝛿𝑛 → 0) is
called the Law of Large Numbers. To prove the Strong Law of Large Numbers we
need to know that the series∑︀ 𝑛 𝛿𝑛 is convergent.
We need to prove that the set 𝐴1/2 of all sequences that have limit frequency
of ones equal to 1/2 has measure 1. In other terms, we need to prove that the
complement of this set (we denote this complement by 𝐵) is a null set.
According to the definition of limit the set 𝐵 is the union (over all 𝜀 > 0) of
the sets 𝐵𝜀. Here 𝐵𝜀 is the set of all sequences such that frequency of ones in their
prefixes exceeds 1/2 + 𝜀 (or is less than 1/2 − 𝜀) infinitely many times.
Evidently, we can consider only a countable set of different 𝜀 (e.g., only rational
values), and the countable union of null sets is a null set. Therefore it remains to
prove that the set 𝐵𝜀 is a null set for each 𝜀.
The set 𝐵𝜀 consists of the sequences that have arbitrarily long “bad” prefixes.
Here “bad” prefix is a string where the frequency of ones differs from 1/2 more
than by 𝜀. Therefore, for each 𝑁 the set 𝐵𝜀 is covered by the family of intervals
Ω𝑥 where 𝑥 ranges over all bad strings of length at least 𝑁 . The total (uniform)
measure of all this intervals does not exceed
𝛿𝑁 + 𝛿𝑁 +1 + 𝛿𝑁 +2 + . . . ,
and this sum can be made small since the series∑︀ 𝑖 𝛿𝑖 is convergent.
(Probability theorists call this argument Borel–Cantelli lemma. In its general
form this lemma says that if the sum of measures of some sets 𝐴0, 𝐴1, . . . is finite,
then the set of all points that belong to infinitely many 𝐴𝑖 is a null set.) 
One can get a bound for the number of bad strings of length 𝑛 without Stirling’s
approximation. We do it separately for bad strings that have too many and too few
ones. For example, let us consider the set of all “bad” strings that have frequency
of ones greater than 1/2 + 𝜀. To get a bound for the cardinality of this set, consider
two distributions (measures) on the set of all strings of length 𝑛. The first one,
called 𝐿, is the uniform distribution: all strings have probability 2−𝑛. The second
one, called 𝑆, is biased (ones are more likely than zeros) and corresponds to 𝑛
independent coin tossing where 1 appears with probability 𝑝 = 1/2 + 𝜀. In other

<!-- page 71 -->

72 3. MARTIN-L ¨OF RANDOMNESS
terms, 𝑆(𝑥) = 𝑞𝑢𝑝𝑣 for a string 𝑥 that has 𝑢 zeros and 𝑣 ones (here 𝑞 = 1/2 − 𝜀 is
the probability of zero outcome). The ratio 𝑆(𝑥)/𝐿(𝑥) increases when the number
of ones in 𝑥 increases, and for all bad strings this ratio is at least 2𝑛/2𝐻(𝑝,𝑞)𝑛.
Therefore, the total 𝐿-measure of all bad strings does not exceed their total 𝑆-
measure divided by this lower bound. Recalling that the total 𝑆-measure of all bad
strings does not exceed 1, we conclude that the total 𝐿-measure (i.e., the fraction)
of all bad strings does not exceed 2𝐻(𝑝,𝑞)𝑛/2𝑛. So we get another proof of our bound,
which is less technical (though more difficult to find). This proof works not only for
the uniform Bernoulli measure (𝑝 = 1/2), but also for arbitrary 𝑝 (after appropriate
changes).
67 Prove the Strong Law of Large Numbers for arbitrary 𝑝. [Hint: Let
𝑝0 and 𝑞0 be fixed positive reals such that 𝑝0 + 𝑞0 = 1. Then the expression
−𝑝0 log 𝑝 − 𝑞0 log 𝑞, where 𝑝, 𝑞 are arbitrary positive reals such that 𝑝 + 𝑞 = 1, is
minimal when 𝑝 = 𝑝0, 𝑞 = 𝑞0. See also Section 9.6, p. 287.]
People often say that “the Strong Law of Large Numbers guarantees that in
every random (with respect to uniform Bernoulli measure) sequence the frequency
of 1s tends to 1/2”. (The case of nonuniform Bernoulli measures is similar.) How-
ever, in this sentence the word “random” should not be understood literally: the
phrase “every random sequence satisfies 𝛼” (for some condition 𝛼) is an idiomatic
expression that means that the set of all sequences that do not satisfy 𝛼 is a null
set.
A natural question arises: can we define the notion of random sequence in such
a way that this idiomatic expression can be understood literally? Let us fix some
distribution on Ω, say, the uniform Bernoulli distribution. We would like to find
some subset of Ω and call its elements “random sequences”. Our goal would be
achieved if for any condition 𝛼 the following two statements were equivalent:
∙ all random sequences satisfy the condition 𝛼;
∙ the set of all sequences that does not satisfy 𝛼 is a null set.
In other terms, the sets of measure 1 should be exactly those sets that contain
all random sequences (and, may be, some nonrandom ones).
One more reformulation: the set of all random sequences should be the smallest
(with respect to inclusion) set of measure 1, and the set of non-random sequences
should be the largest (with respect to inclusion) null set. Now it easy to see that
our goal cannot be achieved. Indeed, any singleton in Ω is a null set. However, the
union of all these singletons is the entire space Ω.
In 1965 Per Martin-L¨of (a Swedish mathematician, who was Kolmogorov’s
student at that time) found that we can save the game if we restrict ourselves to
“effectively null sets”. There exist a largest (with respect to inclusion) effectively
null set, and therefore we can define the notion of a random sequence is such a way
that any condition 𝛼 is satisfied for all random sequences if and only if the set of all
sequences that do not satisfy 𝛼 is an effectively null set. Martin-L¨of construction
is explained in the next section.
### 3.3. Effectively null sets
Let a measure on Ω be fixed and let 𝑝(𝑥) be the measure of the interval Ω𝑥.

<!-- page 72 -->

3.3. EFFECTIVELY NULL SETS 73
We say that a set 𝐴 ⊂ Ω is an effectively null set (with respect to the given
measure) if for every 𝜀 > 0 one can effectively find a family of intervals that cover
𝐴 and whose total measure does not exceed 𝜀.
Some details should be specified in this definition. First, we consider only
rational values of 𝜀 (otherwise it is not clear how 𝜀 could be given to an algorithm).
Second, we need to specify how the sequence of intervals (that cover 𝐴) is generated.
We do this as follows:
Definition. A set 𝐴 ⊂ Ω is called an effectively null set (with respect to a
given measure) if there exists a computable function 𝑥(·, ·) whose first argument is
a positive rational number, second argument is a natural number and values are
binary strings, such that:
(1) 𝐴 ⊂ Ω𝑥(𝜀,0) ∪ Ω𝑥(𝜀,1) ∪ Ω𝑥(𝜀,2) . . .;
(2) 𝑝(𝑥(𝜀, 0)) + 𝑝(𝑥(𝜀, 1)) + 𝑝(𝑥(𝜀, 2)) + . . . 6 𝜀
for any rational 𝜀 > 0. Note that we do not require the function 𝑥 to be total; if
𝑥(𝜀, 𝑖) is undefined, the corresponding term (in both conditions) is omitted.
68 Show that we get an equivalent version of the definition if we consider an
algorithm that gets 𝜀 > 0 as an input and enumerates a set of binary strings (by
printing its elements with arbitrary delays between elements) such that intervals
Ω𝑥 for generated 𝑥 cover 𝐴 and have total measure (the measure of the union of
the intervals) at most 𝜀. (Note that the total measure can be much smaller than
the sum of measures, if the intervals are not disjoint.)
69 Show that we get an equivalent definition if we consider only rational
numbers of the form 2−𝑘 (for integer 𝑘) instead of all rational 𝜀. Show that the
definition does not change if we replace the sign 6 by < in the second inequality.
[Hint: subtract from each interval its part covered by previous intervals, possibly
splitting it into several intervals.]
70 Show that we get an equivalent definition if we require that for each 𝜀 > 0
the domain of the function 𝑖 ↦ → 𝑥(𝜀, 𝑖) is an initial segment of N (or N itself).
71 Show that we get an equivalent definition if we require that the family
of intervals is decidable (instead of being enumerable). [Hint: An interval can
be split into small parts, so we may assume that intervals in the sequence have
non-increasing length, and the family of intervals becomes decicable.]
Let us give some examples of effectively null subsets of Ω (with respect to the
uniform measure).
A singleton whose only element is a sequence of zeros, is an effectively null
set. Indeed, for every 𝜀 > 0 we find an integer 𝑘 such that 2−𝑘 < 𝜀, and consider a
covering that consists of one interval Ω00...0 (corresponding to the string of 𝑘 zeros).
Formally speaking, 𝑥(𝜀, 0) = 0𝑘, where 0𝑘 stands for the sequence formed by
𝑘 zeros, and 𝑘 is the smallest integer such that 2−𝑘 < 𝜀. The values 𝑥(𝜀, 𝑖) are
undefined for 𝑖 > 0.
In this example the sequence 0000 . . . can be replaced by arbitrary computable
sequence of zeros and ones; we need only to consider its prefix of length 𝑘 instead
of 0𝑘.
However, for noncomputable sequences the situation could be different:
72 Prove that there exists a sequence 𝜔 ∈ Ω such that singleton {𝜔} is not
an effectively null set. [Hint: Consider all computable functions 𝑥 that satisfy

<!-- page 73 -->

74 3. MARTIN-L ¨OF RANDOMNESS
the second condition of the definition of effectively null set. There are countably
many such functions. For each of them consider the largest set 𝐴 that satisfies the
requirement (1) of the definition (i.e., the intersection of the unions of coverings
over all 𝜀). This set is an (effectively) null set, and the union of a countable family
of those sets is a null set. Therefore, there exists a sequence 𝜔 which does not
belong to this union.]
Let us note that the statement of this problem is a straightforward corollary
of the Martin-L¨of theorem on the existence of the largest effectively null set (The-
orem 28, p. 75) proved later in this section, and the hint just follows its proof. As
we will see later, the set {𝜔} is an effectively null set if and only if the sequence 𝜔
is not “Martin-L¨of random”.
It is easy to construct a non-computable sequence 𝜔 such that the singleton {𝜔}
is an effective null set. Indeed, consider any sequence of the form 𝜔 = 0?0?0?0 . . .
(each second term is zero, the rest is arbitrary). Let us show that {𝜔} is indeed an
effectively null set. To find a covering with total measure 2−𝑛, consider all strings
of length 2𝑛 that are formed by 𝑛 arbitrary bits interleaved with 𝑛 zeros (as in 𝜔).
There are 2𝑛 strings of this form, and each corresponds to an interval of length
2−2𝑛, so the total measure is 2−𝑛.
In fact we have proved a bit more: the set of all sequences that have only
zeros at even positions, is an effectively null set. Therefore, each of its subsets (in
particular, every singleton) is an effectively null set.
Let us now return to the definition of an effectively null set and separate the
requirements used in this definition. We say that a computable function 𝑥 is “regu-
lar” if is satisfies the requirement (2). The requirement (1) then says that for every
rational 𝜀 > 0 the set 𝐴 is a subset of the union
Ω𝑥(𝜀,0) ∪ Ω𝑥(𝜀,1) ∪ Ω𝑥(𝜀,2) . . .
Therefore, a regular function “serves” all the subsets of the set⋂︁
𝜀>0
(Ω𝑥(𝜀,0) ∪ Ω𝑥(𝜀,1) ∪ Ω𝑥(𝜀,2) . . .) =⋂︁
𝜀>0
⋃︁
 𝑖
Ω𝑥(𝜀,𝑖)
So for each (computable) regular function 𝑥 we get an effectively null set (defined
by the formula above), and effectively null sets are all these sets (for all regular
functions) and all their subsets, and that’s all.
Before we formulate Martin-L¨of theorem, let us give the definition of a com-
putable measure on the set Ω.
A real number 𝛼 is called computable if there exists an algorithm that computes
rational approximations to 𝛼 with any given precision. Formally, 𝛼 is a computable
real if there exists a computable function 𝜀 ↦ → 𝑎(𝜀) defined on all positive rational
numbers and having rational values such that
|𝛼 − 𝑎(𝜀)| < 𝜀
for all rational 𝜀 > 0.
73 Show that we get an equivalent definition if we additionally require that
all approximation given by 𝑎 are approximations from below, i.e., 𝑎(𝜀) < 𝛼 for all
𝜀. [Hint: we can transform any approximation to the approximation from below
losing only factor 2 in precision.]
74 Prove that the sum, difference, product and quotient of two computable
reals are computable reals.

<!-- page 74 -->

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

<!-- page 75 -->

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

<!-- page 76 -->

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

<!-- page 77 -->

78 3. MARTIN-L ¨OF RANDOMNESS
set, but just one ML-random (typical) sequence added is enough to destroy this
property.
For example, recall that any computable sequence forms an effectively null
singleton (with respect to uniform measure). We immediately get the following
corollary:
Theorem 30. The set of all computable sequences of zeros and ones is an
effectively null subset of Ω (with respect to the uniform measure).
It is interesting to note that this observation was made before Martin-L¨of gave
the definition of randomness, while developing the constructive version of calculus
(“Zaslavsky construction” [219] used for many counterexamples; it deals with real
numbers instead of bit sequences).
In the next section we explore the properties of ML-random sequences (with re-
spect to the uniform measure). We end this section with the following nice criterion
for ML-randomness which is attributed to R. Solovay in [34].
Theorem 31. A sequence 𝜔 is not ML-random with respect to a computable
measure 𝜇 if and only if there exists s computable sequence of intervals with finite
sum of measures that covers 𝜔 infinitely many times, i.e., a computable sequence
of binary strings 𝑥0, 𝑥1, 𝑥2, . . . such that∑︁
𝑖
𝜇(Ω𝑥𝑖 ) < ∞
and 𝜔 ∈ Ω𝑥𝑖 for infinitely many 𝑖.
Proof. Assume that 𝜔 is not ML-random. Then for each 𝜀 we can effectively
find a computable sequence of intervals that covers {𝜔} and has the sum of measures
less than 𝜀. Then we combine these sequences for 𝜀 = 1, 1/2, 1/4, 1/8, . . . and get a
computable sequence of intervals with sum of measures not exceeding 2 that covers
𝜔 infinitely many times (at least once for each 𝜀).
On the other hand, assume that there is a computable sequence 𝑥0, 𝑥1, 𝑥2 . . .
of strings such that the sum of measures of corresponding intervals Ω𝑥𝑖 does not
exceed some constant 𝑐 and infinitely many of them contain 𝜔. We may assume
without loss of generality that 𝑐 is a rational number. To find a covering for 𝜔 that
has sum of measures less than 𝜀, we consider the set 𝑀𝑁 of all sequences in Ω that
are covered at least 𝑁 times. Here 𝑁 is a positive integer such that 𝑐/𝑁 < 𝜀. It
is easy to see that 𝑀𝑁 can be represented as the union of a computable sequence
of disjoint intervals (while reading 𝑥0, 𝑥1, . . ., we discover more and more elements
of 𝑀𝑁 and add respective intervals as they appear). Therefore the set {𝜔} is an
effectively null set and the sequence 𝜔 is not ML-random. 
Remark. This result is a constructive version of Borel–Cantelli Lemma (if the
sum of measures of sets 𝐴0, 𝐴1, . . . is finite, then the set of all points that belong
to infinitely many 𝐴𝑖 is a null set), and our argument is an effective version of
a classical proof of Borel–Cantelli Lemma. However, we should be careful since
not any classical proof can be effectivized. The standard proof (since the series is
converging, its tails could be made as small is needed) does not work here, since
there is no way to find an appropriate tail given 𝜀.
Martin-L¨of randomness is defined for computable measures: we used com-
putability to prove that the largest effectively null set exists. One could refor-
mulate the definition and call a sequence random (for an arbitrary measure 𝜇 on

<!-- page 78 -->

3.4. PROPERTIES OF MARTIN-L ¨OF RANDOMNESS 79
Ω) if it does not belong to any effectively null set. For this notion B. Kjos-Hansen
suggested the name Hippocratic randomness (and P. G´acs suggested more neutral
name blind randomness). This is not the only existing notion of randomness with
respect to non-computable measures; we do not go into details here and mention
only that one can use uniform tests of randomness (following Levin and G´acs, see
[13]).
78 Prove that for an upper semicomputable measure there exists the largest
effectively null set. (We do not assume here that the measure of the entire Ω equals
1, otherwise all upper semicomputable measures would be computable.)
79 Construct an example of a (non-computable) measure for which there is no
largest effectively null set. [Hint: Construct a measure that has two properties at
the same time: (1) every computable sequence forms a singleton that is an effective
null set (moreover, some prefix already has measure zero); (2) every algorithm that
pretends to generate an effectively null set, either gives an interval whose measure
is too big, or does not cover some computable sequence. This can be done by a
diagonal argument where we consider one by one all the computable sequences and
all possible algorithms.]
80 Show that there is a non-computable measure for which there exists the
largest effectively null set. [Hint: consider a non-computable measure that is very
close to the uniform one (say, at most twice bigger and at most twice smaller for
all sets).]
### 3.4. Properties of Martin-L¨of randomness
The Strong Law of Large Numbers also provides an example of an effective null
set (with respect to the uniform measure).
Theorem 32. A set of all bit sequences that do no have limit frequency 1/2 is
an effectively null set with respect to the uniform measure.
Proof. It is enough to prove that for every rational 𝜀 > 0 the set of all
sequences such that frequency of ones is greater than 1/2 + 𝜀 infinitely many times
(or less than 1/2 − 𝜀 infinitely many times) is an effective null set.
Indeed, the upper bound for the measure of this set achieved in the proof of
the Strong Law of Large Numbers in the previous section (Theorem 27, p. 70) is
effective: the set of intervals was the set of all sufficiently long strings with large
frequency deviation, and its total measure was effectively bounded by a tail of the
converging geometric series. 
The statement of this theorem can be reformulated as the property of individual
ML-random sequences:
Theorem 33. Let 𝜔 = 𝜔0𝜔1 . . . be a ML-random sequence with respect to the
uniform measure. Then
lim
𝑛→∞
𝜔0 + 𝜔1 + . . . + 𝜔𝑛−1
𝑛 = 1
2 .
The similar statement is true for arbitrary Bernoulli measure. Let 𝑝 and 𝑞 be
computable positive reals such that 𝑝 + 𝑞 = 1. Consider the Bernoulli measure
with parameters 𝑞 and 𝑝 (the sequence of independent coin tossing with success
probability 𝑝). It is easy to check that this is a computable measure (since 𝑝 and 𝑞
are computable).

<!-- page 79 -->

80 3. MARTIN-L ¨OF RANDOMNESS
Theorem 34. Any ML-random sequence with respect to Bernoulli measure
with computable parameters 𝑞, 𝑝 has limit frequency 𝑝.
Proof. Indeed, the upper bound for the probability of large deviations (ob-
tained by comparing the given Bernoulli measure with the other one, with shifted
𝑝, see Problem 67, p. 72), gives an explicit bound and an explicit set of intervals,
so we get an effectively null set. 
There are several other properties of ML-randomness with respect to the uni-
form measure:
Theorem 35. Let 𝜔 be a ML-random sequnce with respect to the uniform
measure. Then any other sequence which is obtained from 𝜔 by a finite number of
insertions/deletions/changes, is also ML-random.
Proof. It is enough to show that adding a zero/one in the beginning of a
ML-random sequence or deleting the first term of a ML-random sequence gives a
ML-random sequence. Indeed, assume that sequence 𝜔 is not ML-random, i.e.,
forms an effectively null singleton: for each 𝜀 one can effective construct a covering
by intervals with total measure less than 𝜀. Let us add zero at the beginning of
all these intervals (i.e., the corresponding strings). We get a covering for 0𝜔 whose
measure is twice smaller. This argument shows that if 𝜔 is not ML-random, then
0𝜔 is not ML-random either. (Similar argument works for 1𝜔.)
On the other hand, if we delete the first bit of all strings that form a covering
for 𝜔, we get a family of intervals of twice larger measure that covers 𝜔′ (obtained
from 𝜔 by deleting the first bit). Therefore, 𝜔′ is not ML-random, too. 
81 Prove that by replacing all zeros by ones and vice versa in a ML-random
sequence (with respect to the uniform measure) we get a ML-random sequence.
The folllowing problem shows that a computable subsequence of a ML-random
sequence is ML-random.
82 Let 𝑛0, 𝑛1, 𝑛2, . . . be a computable sequence of different integers (𝑛𝑖̸ = 𝑛𝑗
if 𝑖̸ = 𝑗). Let 𝜔 = 𝜔0𝜔1𝜔2 . . . be a ML-random sequence. Then its subsequence
𝜔|𝑛 = 𝜔𝑛0 𝜔𝑛1 𝜔𝑛2 . . .
is ML-random. [Hint: any interval Ω𝑥 in a cover for 𝜔|𝑛 produces a finite family of
intervals whose union is the set of sequences whose (𝑛0, 𝑛1, . . . , 𝑛𝑖−1)-subsequence
coincides with 𝑥 (here 𝑖 is the length of the string 𝑥). The total measure of these
intervals equals 2−𝑖, the measure of Ω𝑥.]
More general selection rules are consider in Chapter 9 (p. 273) where the fre-
quency approach to the notion of randomness (von Mises’ approach) is considered.
83 Let 𝜔 be a ML-random sequence with respect to the uniform measure. Let
us split 𝜔 into two-bit blocks and then replace blocks 00 by zeros and blocks 01, 10
and 11 by ones. Prove that the resulting sequence is ML-random with respect to
Bernoulli measure with parameters 1/4, 3/4. [Hint. We described a transformation
𝐹 : Ω → Ω. The preimage of any open set 𝑈 is open, and the uniform measure of
that preimage equals the (1/4, 3/4)-measure of the set 𝑈 .]
84 (Continued.) Prove that every ML-random sequence with respect to the
nonuniform Bernoulli (1/4, 3/4)-measure can be obtained in this way from a se-
quence that is ML-random with respect to the uniform measure. [Hint: For any

<!-- page 80 -->

3.4. PROPERTIES OF MARTIN-L ¨OF RANDOMNESS 81
open set 𝐵 ⊂ Ω consider the set 𝐵′ of all sequences 𝜔 such that 𝐹 −1({𝜔}) ⊂ 𝐵
(the set of sequences that do not have a preimage outside 𝐵, i.e., the complement
to the image of the complement of 𝐵). The image of a compact set is a compact
set, therefore 𝐵′ is open. Show that if 𝐵 is a union of an enumerable family of
intervals, then 𝐵′ is also a union of enumerable family of intervals, and Bernoulli
measure of 𝐵′ does not exceed the uniform measure of 𝐵. See also the proof of a
more general statement (Theorem 123, p. 195).]
What can be said about the “complexity” of a ML-random sequence (with
respect to the uniform measure) from the viewpoint of the recursion theory? We
know already that ML-random sequence is not computable. It also cannot be
a characteristic function of an enumerable (recursively enumerable, computably
enumerable) set.
Theorem 36. Let 𝐴 be an enumerable set of natural numbers. Consider its
characteristic sequence 𝑎0𝑎1𝑎2 . . . (𝑎𝑖 = 0 for 𝑖 /∈ 𝐴 and 𝑎𝑖 = 1 for 𝑖 ∈ 𝐴). This
sequence is not ML-random.
Proof. Let 𝑘 be an arbitrary natural number. Let us enumerate the set 𝐴
and see what happens with 𝑘 first bits of its characteristic sequences. As (the
current version of) 𝐴 increases, we get more and more ones in this 𝑘-bit prefix. In
this way we get at most 𝑘 + 1 candidates; at some point we come to a final (true)
one, but we never know that this happened already. Anyway, the set of candidates
is enumerable and the number of candidates does not exceed 𝑘 + 1 (since 𝑘-bit
prefix can have 0 . . . 𝑘 ones). The total measure of these intervals is (𝑘 + 1)/2𝑘 and
therefore can be made arbitrarily small. (Note that the definition of the effectively
null set allows us to enumerate the intervals that form a covering, and this is exactly
what we can do in our case.) 
A natural question arises: in what sense one can provide explicitly a ML-
random sequence? As we have seen, neither computable sequences nor character-
istic sequences of enumerable sets are random. If you are familiar with the basics
of the recursion theory (see, e.g., [182]), you may appreciate the following result:
there exist a ML-random sequence that belongs to the class Σ2 ∩ Π2 of the arith-
metic hierarchy (this class can be also described as the class of all 0′-computable
sequences).
Theorem 37. There exists a 0′-computable sequence that is ML-random with
respect to the uniform measure.
Proof. It is enough to show that for any enumerable set of strings {𝑥0, 𝑥1, . . .}
such that∑︀ 2−𝑙(𝑥𝑖) < 1/2 there exists a 0′-computable sequence that does not have
any of 𝑥𝑖 as a prefix. (Indeed, the largest effective null set has such a covering with
total measure less than 1/2, and any sequence that is not covered is ML-random.)
The intervals Ω𝑥𝑖 are divided into two groups: some of them belong to the left
half of Ω (i.e., 𝑥𝑖 starts with 0) and some belong to the right half. Total measure of
both groups at most 1/2. Therefore, at least one of the groups has total measure
at most 1/4. However, looking at the sequence 𝑥𝑖, we cannot find out which half
has this property (since at any moment new large interval can arrive).
However, 0′-oracle allows us to make this choice, since the event “measure
exceeds 1/4” is enumerable. Then we divide this half into two parts of size 1/4

<!-- page 81 -->

82 3. MARTIN-L ¨OF RANDOMNESS
each and choose one of them where the total measure of corresponding intervals
does not exceed 1/8, and so on.
In this way we get a 0′-computable sequence with the following property: each
its prefix is at most half-covered by our intervals. In particular, no prefix of this
sequence can appear in the sequence 𝑥𝑖, and this is what we need. 
A similar but more geometric argument can be given if we consider reals in [0, 1]
instead of binary sequences. A point 𝑥 ∈ [0, 1] is ML-random with respect to the
Lebesgue measure on [0, 1] if its binary representation is ML-random with respect to
the uniform measure on the Cantor space. (A point can have two representations
but in this case both are computable and non-random, so we may ignore this
problem.) One can also give an equivalent definition of randomness directly. A set
𝑋 ⊂ [0, 1] is called an effectively null subset of [0, 1] if there exists an algorithm
that for every rational 𝜀 > 0 enumerates a cover of 𝑋 that consists of intervals with
rational endpoints whose sum of measures is less than 𝜀. Then a ML-random real
is a real not contained in any effectively null subset of [0, 1]. All this is just a simple
reformulation of corresponding notions and results for Cantor space since the only
difference is that some numbers have two representations (but this happens only
for countably many computable reals), and that we consider intervals with rational
endpoints instead of intervals with dyadic-rational endpoints (this does not matter
since we can split an interval with rational endpoints into a computable sequence
of dyadic intervals). In particular, the following statement is true:
85 Prove that there exists the largest effectively null subset of [0, 1], and its
elements are reals whose binary representations are not ML-random with respect
to the uniform measure in the Cantor space.
Now we can point out an “explicit” ML-random point. Consider an enumerable
family of open intervals that have total length less than 1 and cover all non-ML-
random points. The union of this intervals is an open set which is a proper subset
of [0, 1]. Its complement is a closed set, and this closed set has a minimal point.
By construction this point is ML-random.
86 Prove that the minimal point that is not covered by enumerable family of
open intervals with rational endpoints is lower semicomputable, i.e., it is a limit of
an increasing computable sequence of rational numbers (and therefore is computable
with the oracle for halting problem, 0′).
(See Section 5.7 (p. 170) for more details about random reals and for an alter-
native construction of a lower semicomputable ML-random real.)
The proof of Theorem 37 given above is a relativized version of the following
result:
87 Assume that 𝑥0, 𝑥1, 𝑥2, . . . is a computable sequence of binary strings and
the sum	∑︁
𝑖
2−𝑙(𝑥𝑖)
is less than 1 and is a computable real number. Then there exists a computable
sequence of zeros and ones that has neither of 𝑥𝑖 as its prefix.
[Hint: Let this sum be less than some rational 𝑆 < 1. By induction construct
a computable sequence 𝜔0𝜔1𝜔2 . . . with the following property: the fraction of the
set 𝑈 = ∪Ω𝑥𝑖 among the sequences that have prefix 𝜔0 . . . 𝜔𝑘 is less than 𝑆.]

<!-- page 82 -->

3.4. PROPERTIES OF MARTIN-L ¨OF RANDOMNESS 83
This problem is related to the definition of randomness suggested by C. Schnorr
in [165]. He gave a more restrictive definition of an effectively null set than Martin-
L¨of. The additional requirement: for every (rational) 𝜀 > 0 the total measure of
corresponding intervals is not only less than 𝜀 but also is a computable real (and the
approximation algorithm computably depends on 𝜀). This requirement is equivalent
to the following one: for every 𝜀 > 0 and 𝛿 > 0 one can effectively find out how
many terms in the series∑︀ 𝑖 𝑝(𝑥(𝜀, 𝑖)) are needed to make the tail less than 𝛿.
(For a series with non-negative terms the computability of sum is equivalent to
computable convergence.)
By Schnorr effectively null sets we mean the effectively null sets according
to this modified definition. (Schnorr calls them total rekursive Nullmenge, see
Definition 8.1 in [165]; effectively null sets (as in the Martin-L¨of defintion) are
called rekursive Nullmenge, see Definition 4.1.)
88 Let us change the definition of an effectively null set in another way: now
we require that the total measure of all intervals in the covering is exactly 𝜀. Show
that this definition is equivalent to the definition of Schnorr effectively null set.
(One can also consider the measure of the union of all intervals instead of the sum
of measures.)
Problem 87 shows that for every Schorr effectively null set there exists a com-
putable sequence outside this set. (For simplicity let us consider the case of uniform
measure.) On the other hand, every computable sequence (i.e., the singleton made
of it) is a Schnorr effectively null set. Therefore, none of the Schnorr effectively
null sets is the largest one in the class (in other words, the union of all Schnorr
effectively null sets is not a Schnorr effectively null set). Nevertheless we can call a
sequence which does not belong to any Schnorr null set a Schnorr random sequence
(or “Schnorr typical” sequence).
Since now we have less effectively null sets, we may get the broader class of
random sequences, and it is indeed the case. The following problem (together with
the results of Chapter 5) guarantees that there exist Schnorr random sequences
that are not Martin-L¨of random.
89 Prove that there exists a Schnorr random sequence 𝜔 = 𝜔0𝜔1𝜔2 . . . whose
prefixes have logarithmic complexity, i.e., 𝐶(𝜔0 . . . 𝜔𝑛−1) = 𝑂(log 𝑛).
[Hint: Problem 87 shows how one can construct a computable sequence that
does not belong to a given Schnorr effectively null set. At some point of this
construction we can take into account another Schnorr effectively null set and get
a computable sequence that does not belong to both. (Indeed, we need to take a
sufficiently small cover for the second set that does not go out of the safety margin
in the construction for the first set.) Moreover, we can consider infinitely many
Schnorr effectively null sets in this way (adding them one after another). This will
not give us a computable Schnorr random sequnce (it does not exist at all), because
we need additional information that says us which algorithms correspond to Schnorr
effectively null sets and which do not. But if we postpone the introduction of a new
algorithm until the moment when the constructed prefix of our sequence is rather
long, this additional information is logarithmic compared to the prefix length.]
We return to Schnorr’s definition of randomness in Section 9.8 where it is
reformulated in terms of computable martingales.

<!-- page 83 -->

84 3. MARTIN-L ¨OF RANDOMNESS
90 Prove that a sequence 𝜔 is not Schnorr random if and only if there exists a
computable sequence of strings 𝑥0, 𝑥1, . . . such that the series∑︀ 𝑖 𝑝(𝑥𝑖) computably
converges (has a computable sum) and infinitely many of 𝑥𝑖 are prefixes of 𝜔. [Hint:
This is a version of Theorem 31 for Schnorr randomness and can be proven in a
similar way. In fact, in this case even the standard proof of Borel–Cantelli lemma
works.]
Another version of effectively null sets is obtained if we consider only finite
families of intervals (each family is presented as the list of all intervals in the
family): given a rational 𝜀, the algorithm should output a finite list of intervals
that cover the set and have the sum of measures less than 𝜀. This corresponds to
Jordan contruction of measure often used in the elementary calculus textbooks. In
this way we get a smaller class of null sets (e.g., a null set cannot cover all rational
points).
91 Prove that a set is an effectively null set in this sense if and only if it is
contained in the complement of some effectively open set of measure 1.
The sequences not covered by any effectively null sets in this sense (=contained
in every effectively open set of full measure) are called Kurtz random. In this
definition we again restrict the class of effectively null sets and therefore enlarge
the class of random sequences. Indeed we get more random sequences, as the
following problem shows.
92 Show that every Schnorr random sequence (with respect to the uniform
measure) satisfies the Strong Law of Large Numbers, but there exists a Kurtz
random sequence that does not. [Hint: The proof of the Strong Law of Large
Numbers gives a cover with computable sum of measures since the series converges
exponentially fast. For the second part one can consider generic sequences, see
Section 5.9, p. 192.]
### 3.5. Randomness deficiencies
Martin-L¨of’s definition requires that for an effectively null set 𝐴 there is an
algorithm that, given 𝜀 > 0, produces a cover of 𝐴 by intervals whose total measure
does not exceed 𝜀. The union of these intervals in an open set of measure at most 𝜀.
In general, the unions of computable sequences of intervals are called effectively
open sets. As in the definition of effectively null sets (p. 73), we allow the com-
putable sequence to be non-total, so the empty set is also effectively open. In other
words, an effectively open set is a union of an enumerable family of intervals.
Now the definition of an effectively null set can be reformulated as follows:
Theorem 38. A set 𝐴 is an effectively null set with respect to a measure 𝜇 if
and only if 𝐴 ⊂⋂︀ 𝑛 𝑈𝑛 for some uniformly effectively open sets 𝑈𝑛 with 𝜇(𝑈𝑛) 6
2−𝑛. We may assume also that 𝑈1 ⊃ 𝑈2 ⊃ . . . .
Speaking about “uniformly effectively open sets”, we mean that there exists an
algorithm that, given 𝑛, enumerates a family of intervals whose union is 𝑈𝑛.
Proof. There are several differences between this definition and the one we
used earlier. First difference (a trivial one) is that we use only 𝜀 = 2−𝑛.
Second, we speak here about the measure of an effectively open set, not about
the sum of measures of intervals whose union it is. This does not matter either, since
we may assume without loss of generality that the intervals forming an effectively

<!-- page 84 -->

3.5. RANDOMNESS DEFICIENCIES 85
open set are disjoint. (When a new interval app

## Relationships

- **Section:** [Theory, Complexity & Optimization](/sections/04-theory-complexity-and-optimization.md)
- **Previous in the list:** [25 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton](/papers/25-coffee-automaton.md)
- **Next in the list:** [27 - Machine Super Intelligence](/papers/27-machine-super-intelligence.md)
- **Enables:** [22 - The First Law of Complexodynamics](/papers/22-first-law-of-complexodynamics.md), [25 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton](/papers/25-coffee-automaton.md), [27 - Machine Super Intelligence](/papers/27-machine-super-intelligence.md)
- **Alongside:** [19](/papers/19-gpipe-pipeline-parallelism.md), [20](/papers/20-adam-stochastic-optimization.md), [21](/papers/21-dropout-regularization.md), [22](/papers/22-first-law-of-complexodynamics.md), [23](/papers/23-keeping-neural-networks-simple.md), [24](/papers/24-tutorial-minimum-description-length.md) …
- **Topics:** [Kolmogorov Complexity](/topics/kolmogorov-complexity.md), [Minimum Description Length](/topics/minimum-description-length.md)
- **People:** [Alexander Shen](/people/alexander-shen.md)
- **Reading paths:** [Orientation in Seven Days](/reading-paths/orientation-seven-days.md), [Theory and Compression](/reading-paths/theory-and-compression.md)

## Source and provenance

- Listed at position 26 of the 30-paper reading list compiled by @rachit.speaks, the list Ilya Sutskever is reported to have given John Carmack.[^reading-list]
- Original: <https://www.lirmm.fr/~ashen/kolmbook-eng-scan.pdf>
- Full text not included in this bundle; follow the link above.

[^reading-list]: The 30 Papers to AI Mastery, curated by @rachit.speaks
[^original]: Kolmogorov Complexity and Algorithmic Randomness - AMS Mathematical Surveys and Monographs 220
