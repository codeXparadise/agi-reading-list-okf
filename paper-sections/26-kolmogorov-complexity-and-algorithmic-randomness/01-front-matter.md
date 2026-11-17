---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
section: Front matter
section_role: front-matter
section_index: 1
pages: [1, 2, 3, 4, 5, 6, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "The text below was extracted from the published source (book) on 2026-11-17. The open English text edition of the book, pages 1 to 85 of 519 - the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Front matter

> Section 1 of 11 from [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md) · `front-matter` · pages 1-28

The text below was extracted from the published source (book) on 2026-11-17. The open English text edition of the book, pages 1 to 85 of 519 - the fetch was capped at that length. The reading list points at chapter 14, *Algorithmic statistics* (page 425), which falls outside the fetched range; read it at the link. Book page numbers are preserved as `<!-- page N -->` markers, so page chunks below carry the book's own pagination.

To the memory of Andrei Muchnik

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

28 BASIC NOTIONS AND NOTATIONS
mutual information in random variables 𝜉 and 𝜂 and is denoted by 𝐼(𝜉 : 𝜂). A sim-
ilar notation 𝐼(𝑥 : 𝑦) is used in the algorithmic information theory. As 𝐼(𝑥 : 𝑦) is
commutative only up to a small error term, we usually say “the information in 𝑥
about 𝑦” and define this notion as 𝐶(𝑦) − 𝐶(𝑦 | 𝑥).

CHAPTER 1
Plain Kolmogorov complexity

---

Full document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md) · Page-level evidence: [paper-pages/26-kolmogorov-complexity-and-algorithmic-randomness](../../paper-pages/26-kolmogorov-complexity-and-algorithmic-randomness/index.md)
