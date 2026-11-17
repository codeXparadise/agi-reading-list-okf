---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 5.6. The limits of mathematical analysis
section_role: other
section_index: 49
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "One way to interpret the results of the previous sections is in terms of constructive theories of prediction. Essentially, a constructive theory of…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 5.6. The limits of mathematical analysis

> Section 49 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

One way to interpret the results of the previous sections is in terms of constructive theories of prediction. Essentially, a constructive theory of prediction
expressed in some sufficiently rich formal system F, is in effect a description
of a prediction algorithm with respect to a universal Turing machine which
implements the required parts of F. Thus, from Theorems 5.3.3 and 5.5.1,
it follows that if we want to have a predictor that can learn to predict all

$$
\mathfrak{F}
$$

$$
\mathfrak{F}.
$$ sequences up to a high level of Kolmogorov complexity, or even just predict
individual sequences which have high K˙ complexity, the constructive theory of
prediction that we base our predictor on must be very complex. Elegant and
highly general constructive theories of prediction simply do not exist, even if
we assume unlimited computational resources. This is in marked contrast to
Solomonoff’s highly elegant but non-constructive theory of prediction.

$$
\dot{K}
$$

Naturally, highly complex theories of prediction will be very difficult to
mathematically analyse, if not practically impossible. Thus, at some point
the development of very general prediction algorithms must become mainly
an experimental endeavour due to the difficulty of working with the required
theory. Interestingly, an even stronger result can be proven showing that
beyond some point the mathematical analysis is in fact impossible, even in
theory:

5.6.1 Theorem. In any consistent formal axiomatic system F that is sufficiently rich to express statements of the form “p ∈Pn”, there exists m ∈ N
such that for all n > m and for all predictors p ∈ Pn the true statement
“p ∈Pn” cannot be proven in F.

$$
\mathfrak{F}
$$

$$
suf\bar{f}\bar{h}
$$

$$
“ p \in \mathcal {P} _ {n} ”
$$

$$
m\in\mathbb{N}
$$

$$
n>m
$$

$$
p\in\mathcal{P}_n
$$

$$
``\mathit{p}\in\mathcal{P}_{\mathit{n}}''
$$

$$
\mathfrak{F}
$$

In other words, even though we have proven that very powerful sequence
prediction algorithms exist, beyond a certain complexity it is impossible to
find any of these algorithms using mathematics. The proof has a similar
structure to Chaitin’s information theoretic proof (Chaitin, 1982) of G¨odel’s
incompleteness theorem for formal axiomatic systems (G¨odel, 1931).

Proof. For each n ∈ N let Tn be the set of statements expressed in the
formal system F of the form “p ∈Pn”, where p is filled in with the complete
description of some algorithm in each case. As the set of programs is denumerable, Tn is also denumerable and each element of Tn has finite length. From
Lemma 5.3.2 and Theorem 5.3.3 it follows that each Tn contains infinitely
many statements of the form “p ∈Pn” which are true.

$$
T_{n}
$$

$$
n\in\mathbb{N}
$$

$$
\mathfrak{F}
$$

$$
``p\in\mathcal{P}_n''
$$

$$
T_{n}
$$

$$
T_{n}
$$

$$
T_{n}
$$

$$
``p\in\mathcal{P}_n''
$$

Fix n and create a search algorithm s that enumerates all proofs in the
formal system F searching for a proof of a statement in the set Tn. As the set
Tn is recursive, s can always recognise a proof of a statement in Tn. If s finds
any such proof, it outputs the corresponding program p and then halts.

$$
\mathfrak{F}
$$

$$
T_{n}
$$

$$
T_{n}
$$

$$
T_{n}
$$

By way of contradiction, assume that s halts, that is, a proof of a theorem
in Tn is found and p such that p ∈ Pn is generated as output. The size of
the algorithm s is a constant (a description of the formal system F and some
proof enumeration code) as well as an O(log n) term needed to describe n. It
follows then that K(p) < O(log n).+ However, from Theorem 5.3.3 we know
that K(p) > n.+ Thus, for sufficiently large n, we have a contradiction and
so our assumption of the existence of a proof must be false. That is, for
sufficiently large n and for all p ∈Pn, the true statement “p ∈Pn” cannot be
proven within the formal system F.

$$
p\in\mathcal{P}_n
$$

$$
T_{n}
$$

$$
\mathfrak{F}
$$

$$
K(p)\stackrel{+}{<}O(\log n)
$$

$$
K(p)\stackrel{+}{>}n
$$

$$
p\in\mathcal{P}_n
$$

$$
``p\in\mathcal{P}_n''
$$

$$
\mathfrak{F}
$$

5. Limits of Computational Agents

The exact value of m depends on our choice of formal system F and which
reference machine U we measure complexity with respect to. However, for
reasonable choices of F and U the value of m would be in the order of 1000.
That is, the bound m is certainly not so large as to be vacuous.

$$
\mathfrak{F}
$$

$$
\mathfrak{F}
$$

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
