---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 5.5. Hard to predict sequences
section_role: other
section_index: 48
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "We have already seen that some individual sequences, such as the repeating string used in the proof of Lemma 5.2.3, can have arbitrarily high…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 5.5. Hard to predict sequences

> Section 48 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

We have already seen that some individual sequences, such as the repeating
string used in the proof of Lemma 5.2.3, can have arbitrarily high Kolmogorov
complexity but nevertheless can be predicted by trivial algorithms. Thus,
although these sequences contain a lot of information in the Kolmogorov sense,
in a deeper sense their structure is very simple and easily learnt.

What interests us in this section is the other extreme: individual sequences
that can only be predicted by complex predictors. As we are concerned with
prediction in the limit, this extra complexity in the predictor must be some
kind of special information which cannot be learnt through observing the sequence. Our first task is to show that these hard to predict sequences exist.

$$
\mathbf{5.5.1}\quad\mathbf{T h e o r e m.}\quad\forall n\in\mathbb{N},\exists\omega\in\mathcal{C}\quad:\quad n\quad\stackrel{+}{<}\quad\dot{K}(\omega)\quad\stackrel{+}{<}\quad K(\omega)\quad\stackrel{+}{<}\quad n+O(\log n).
$$

<n
Proof. For any n ∈ N, let Qn ⊂ B be the set of programs shorter than n
that are predictors, and let x1:k ∈ Bk be the observed initial string from the
sequence ω that is to be predicted. Now construct a meta-predictor pˆ:

$$
n\in\mathbb{N}
$$

$$
Q_{n}\subset\mathbb{B}^{<n}
$$

$$
x_{1:k}\in\mathbb{B}^k
$$

$$
\hat{p}\hat{:}
$$

By dovetailing the computations, run in parallel every program of length
less than n on every string in B≤k. Each time a program is found to halt on
all of these input strings, add the program to a set of “candidate prediction
algorithms”, called Q˜kn. As each element of Qn is a valid predictor, and thus
halts for all input strings in B∗ by definition, for every n and k it eventually
will be the case that |Q˜kn| = |Qn|. At this point the simulation to approximate
Qn terminates. It is clear that for sufficiently large values of k all of the valid
predictors, and only the valid predictors, will halt with a single symbol of
output on all tested input strings. That is, ∃r ∈ N, ∀k > r : Q˜kn = Qn.

$$
\mathbb{B}^{\leq k}
$$

$$
\tilde{Q}_{n}^{k}
$$

$$
Q_{n}
$$

$$
\mathbb{B}^*
$$

$$
\left|\widetilde{Q_{n}^{k}}\right|=\left|Q_{n}\right|
$$

$$
Q_{n}
$$

$$
\exists r\in\mathbb{N},\forall k>r:\tilde{Q}_n^k=Q_n
$$

The second part of the pˆ algorithm uses these candidate prediction algo-
∑k−1
rithms to make a prediction. For p ∈ Q˜kn define dk(p) := |p(x1:i) − xi+1|.
i=1
Informally, dk(p) is the number of prediction errors made by p so far. Compute this for all p ∈ Q˜kn and then let p∗k ∈ Q˜kn be the program with minimal
dk(p). If there is more than one such program, break the tie by letting p∗k be
the lexicographically first of these. Finally, pˆ computes the value of p∗k(x1:k)
and then returns this as its prediction and halts.

$$
\hat{p}
$$

$$
p\in\tilde{Q}_n^k
$$

$$
d^{k}(p):=\sum_{i=1}^{k-1}\left|p(x_{1:i})-x_{i+1}\right|
$$

$$
d^{k}(p)
$$

$$
p\in\tilde{Q}_n^k
$$

$$
p_{k}^{*}\in\tilde{Q}_{n}^{k}
$$

$$
d^{k}(p)
$$

$$
p_{k}^{*}
$$

$$
\hat{p}
$$

$$
p_{k}^{*}(x_{1:k})
$$

By Lemma 5.2.4, there exists ω′ ∈C such that pˆ makes a prediction error
for every k when trying to predict ω′. Thus, in each cycle at least one of
the finitely many predictors with minimal dk makes a prediction error and
so ∀p ∈ Qn: dk(p) → ∞ as k → ∞. Therefore, ∄p ∈ Qn: p ∈ P (ω′),
that is, no program of length less than n can learn to predict ω′ and so n ≤
+
K˙ (ω′). Further, from Lemma 5.2.1 we know that K˙ (ω′) < K(ω′), and from
+
Lemma 5.2.4 again, K(ω′)<K(ˆp).

$$
\omega^{\prime}\in\mathcal{C}
$$

$$
\hat{p}
$$

$$
\omega^{\prime}
$$

$$
d^{k}
$$

$$
\forall p\in Q_n:d^k(p)\to\infty
$$

$$
\exists p\in Q_n:p\in\mathcal{P}(\omega')
$$

$$
k\to\infty
$$

$$
\dot{K}(\omega')
$$

$$
n\leq
$$

$$
\omega^{\prime}
$$

$$
\dot{K}(\omega')\stackrel{+}{<}K(\omega')
$$

$$
K(\omega^{\prime})\overset{+}{<}K(\hat{p})
$$

Examining the algorithm for pˆ, we see that it contains some fixed length
program code and an encoding of |Qn|, where |Qn|<2n − 1. Thus, using a
standard encoding method for integers, K(ˆp) < n + O(log n). Chaining these,+
+ + + +
n < K˙ (ω′) < K(ω′)<K(ˆp) < n + O(log n), which proves the theorem.

$$
\hat{p},
$$

$$
\left|Q_{n}\right|
$$

$$
\left|Q_{n}\right|<2^{n}-1
$$

$$
K(\hat{p})\stackrel{+}{<}n+O(\log n)
$$

$$
n\stackrel{\pm}{<}\dot{K}(\omega')\stackrel{\pm}{<}K(\omega')\stackrel{\pm}{<}K(\hat{p})\stackrel{\pm}{<}n+O(\log n)
$$

5. Limits of Computational Agents

This establishes the existence of sequences with arbitrarily high K˙ complexity which also have a similar level of Kolmogorov complexity. Next we
establish a fundamental property of high K˙ complexity sequences: they are
extremely difficult to compute.

$$
\dot{K}
$$

$$
\dot{K}
$$

For an algorithm q that generates ω ∈C, define tq(n) to be the number of
computation steps performed by q before the nth symbol of ω is written to the
output tape. For example, if q is a simple algorithm that outputs the sequence
010101..., then clearly tq(n) = O(n) and so ω can be computed quickly. The
following theorem proves that if a sequence can be computed in a reasonable
amount of time, then the sequence must have a low K˙ complexity:

$$
q
$$

$$
\omega\in\mathcal{C}
$$

$$
t_{q}(n)
$$

$$
q
$$

$$
n^{th}
$$

$$
\omega
$$

$$
q
$$

$$
010101\ldots
$$

$$
t_{q}(n)=O(n)
$$

$$
\omega
$$

$$
\dot{K}
$$

5.5.2 Lemma. ∀ω ∈C, if ∃q : U (q) = ω and ∃r ∈ N, ∀n > r : tq(n) < 2n,
then K˙ (ω) = 0.+

$$
\forall\omega\in\mathcal{C},\quad\exists q:\mathcal{U}(q)=\omega\quad and\quad\exists r\in\mathbb{N},\forall n>r:t_q(n)<2^n.
$$

$$
\dot{K}(\omega)\stackrel{+}{=}0
$$

Proof. Construct a prediction algorithm p˜ as follows:

$$
\tilde{p}
$$

On input x1:n, run all programs of length n or less, each for 2n+1 steps. In
a set Wn collect together all generated strings which are at least n + 1 symbols
long and where the first n symbols match the observed string x1:n. Now order
the strings in Wn according to a lexicographical ordering of their generating
programs. If Wn = ∅, then just return a prediction of 1 and halt. If |Wn|>1
then return the n + 1th symbol from the first sequence in the above ordering.

$$
x_{1:n}
$$

$$
2^{n+1}
$$

$$
n
$$

$$
W_{n}
$$

$$
n+1
$$

$$
x_{1:n}
$$

$$
W_{n}
$$

$$
\left|W_{n}\right|>1
$$

$$
W_{n}=\varnothing
$$

$$
n+1^{th}
$$

Assume that ∃q : U (q) = ω such that ∃r ∈ N, ∀n > r : tq(n) < 2n. If q is
not unique, take q to be the lexicographically first of these. Clearly ∀n > r
the initial string from ω generated by q will be in the set Wn. As there
is no lexicographically lower program which can generate ω within the time
constraint tq(n) < 2n for all n > r, for sufficiently large n the predictor ˜p must
converge on using q for each prediction and thus p˜ ∈P (ω). As ℓ(˜p) is clearly
a fixed constant that is independent of ω, it follows then that K˙ (ω) < ℓ(˜p) =+
0.

$$
q
$$

$$
\exists q:\mathcal{U}(q)=\omega
$$

$$
\exists r\in\mathbb{N},\forall n>r:t_q(n)<2^n
$$

$$
\forall n>r
$$

$$
q
$$

$$
W_{n}
$$

$$
\omega
$$

$$
\omega
$$

$$
t_{q}(n)<2^{n}
$$

$$
n>r
$$

$$
\tilde{p}
$$

$$
q
$$

$$
\tilde{p}\in\mathcal{P}(\omega)
$$

$$
\ell(\tilde{p})
$$

$$
\omega
$$

$$
\dot{K}(\omega)<\ell(\tilde{p})\stackrel{+}{=}
$$

$$
0
$$

We could replace the 2n bound in the above result with any monotonically
growing computable function, for example, 22n. In any case, this does not
change the fundamental result that sequences which have a high K˙ complexity
are practically impossible to compute. However, from our theoretical perspective, these sequences present no problem as they can be predicted, albeit with
immense difficulty.

$$
2^{n}
$$

$$
2^{2^{n}}
$$

$$
\dot{K}
$$

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
