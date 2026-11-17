---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/25-coffee-automaton.md
source: ../../papers/25-coffee-automaton.md
paper_title: "Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton"
sequence: 25
page: 2
pages: [2]
page_of: 22
topics: ["../../topics/kolmogorov-complexity.md"]
description: "We see that this is essentially equivalent to the Gibbs entropy, with a slight change of notation and vocabulary. Finally, in computability theory,…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 2 of 22 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton

> Page 2 of the source PDF, verbatim as extracted. Canonical document: [25 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton](../../papers/25-coffee-automaton.md)

We see that this is essentially equivalent to the Gibbs entropy, with a slight change of notation and vocabulary.

Finally, in computability theory, the entropy of an n-bit string x is often identified with its Kolmogorov complexity K(x): the length of the shortest computer program that outputs x.1 Strings that are highly patterned—meaning low in disorder—can be described by a short program that takes advantage of those patterns. For example, a string consisting of n ones could be output by a short program which simply loops n times, printing ‘1’ each time. Conversely, strings which have little regularity cannot be compressed in this way. For such strings, the shortest program to output them might simply be one that hard-codes the entire string.

Fortunately, these notions of entropy are closely related to each other, so that one can often switch between them depending on convenience. The Gibbs and Shannon entropies are clearly equivalent. The Boltzmann entropy is equivalent to the Gibbs entropy under the assumption that the distribution function is flat over microstates within the given macrostate, and zero elsewhere– i.e., given the knowledge of the system we would actually obtain via macroscopic observation. For a computable distribution D over n-bit strings, the Kolmogorov complexity of a string sampled from D tends to the entropy of D \[9\]. (Thus, the Kolmogorov complexity of a sequence of random numbers will be very high, even though there is no “interesting structure”in it.)

Despite these formal connections, the three kinds of entropy are calculated in very diﬀerent ways. The Boltzmann entropy is well-defined once a specific coarse-graining is chosen. To estimate the Shannon entropy H(D) of a distribution D (which we will henceforth treat as identical to the corresponding Gibbs entropy), one in general requires knowledge of the entire distribution D, which could potentially require exponentially many samples from D. At first glance, the Kolmogorov complexity K(x) seems even worse: it is well-known to be uncomputable (in fact, computing K(x) is equivalent to solving the halting problem). On the other hand, in practice one can often estimate K(x) reasonably well by the compressed file size, when x is fed to a standard compression program such as gzip. And crucially, unlike Shannon entropy, Kolmogorov complexity is well-defined even for an individual string x. For these reasons, we chose to use K(x) (or rather, a computable approximation to it) as our estimate of entropy.

Of course, none of the three measures of entropy capture “complexity,” in the sense discussed in Section 1. Boltzmann entropy, Shannon entropy, and Kolmogorov complexity are all maximized by “random” or “generic” objects and distributions, whereas a complexity measure should be low both for “simple” objects and for “random” objects, and large only for “interesting” objects that are neither simple nor random.

This issue has been extensively discussed in the complex systems and algorithmic information theory communities since the 1980s. We are aware of four quantitative ideas for how to define “complexity” or “interestingness” as distinct from entropy. While the definitions look extremely diﬀerent, it will turn out happily that they are all related to one another, much like with the diﬀerent definitions of entropy. Note that our primary interest here is in the complexity of a configuration defined at a single moment in time. One may also associate measures of complexity to dynamical processes, which for the most part we won’t discuss.

1A crucial fact justifying this definition is that switching from one (Turing-universal) programming language to another changes K(x) by at most an additive constant, independent of x. The reason is that in one language, we can always just write a compiler or interpreter for another language, then specify x using the second language. Also, throughout this paper, we will assume for convenience that the program receives x’s length n as input. This assumption can change K(x) by at most an additive O(log n) term.

3

---

[previous page](page-001.md) · [next page](page-003.md) · [all pages](index.md)
