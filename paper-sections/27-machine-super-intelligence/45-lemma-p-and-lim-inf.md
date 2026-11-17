---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: "5.2.3 Lemma. P (ω) and lim inf"
section_role: other
section_index: 45
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "There exists a predictor p such that ∀n ∈ N, ∃ ω ∈ C : p ∈ i→∞K(ωi:∞) n. $$ mathcal{P}(omega) $$ $$ forall ninmathbb{N},existsomegainmathcal{C}:pin…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 5.2.3 Lemma. P (ω) and lim inf

> Section 45 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

There exists a predictor p such that ∀n ∈ N, ∃ ω ∈ C : p ∈ i→∞K(ωi:∞) > n.

$$
\mathcal{P}(\omega)
$$

$$
\forall n\in\mathbb{N},\exists\omega\in\mathcal{C}:p\in
$$

$$
\mathrm{f}_{i\to\infty}K(\omega_{i:\infty})>n
$$

Proof. A predictor p for eventually periodic sequences can be defined
as follows: On input ω1:k the predictor goes through the ordered pairs
(1, 1), (1, 2), (2, 1), (1, 3), (2, 2), (3, 1), (1, 4),... checking for each pair (a,b)
whether the string ω1:k consists of an initial string of length a followed by
a repeating string of length b. On the first match that is found p predicts that
the repeating string continues, and then p halts. If a + b > k before a match
is found, then p outputs a fixed symbol and halts. Clearly K(p) is a small
constant and p will learn to predict any sequence that is eventually periodic.

$$
p
$$

$$
\omega_{1:k}
$$

$$
(1,1),(1,2),(2,1),(1,3),(2,2),(3,1),(1,4),\ldots
$$

$$
\omega_{1:k}
$$

$$
a+b>k
$$

For any (m,n) ∈ N2, let ω := x(y∗) where x ∈ Bm, and y ∈ Bn is a random
string, that is, K(y) = n. As ω is eventually periodic p ∈P (ω) and also we see
that lim infi→∞K(ωi:∞) = min{K(ωm+1:∞),K(ωm+2:∞),...,K(ωm+n:∞)}.

$$
(m,n)\in\mathbb{N}^2
$$

$$
\omega:=x(y^*)
$$

$$
x\in\mathbb{B}^m
$$

$$
y\in\mathbb{B}^n
$$

$$
K(y)=n
$$

$$
p\in\mathcal{P}(\omega)
$$

$$
\inf_{i\to\infty}K(\omega_{i:\infty})=\operatorname*{m i n}\{K(\omega_{m+1:\infty}),K(\omega_{m+2:\infty}),\ldots,K(\omega_{m+n:\infty})\}
$$

For any k ∈ {1,...,n}
ate ωm+k:∞. We can define
this program consists of q
K(ωk:∞)+O(log n). As n = K(y) ≤ ℓ(q
As n and k are arbitrary the result follows.

let qk∗ be
a halting
k∗, n and k.

the shortest
program
Thus, ℓ(q
k′), we see that K(ω

program that can generqk′ that outputs y where
k′) = ℓ(qk∗) + O(log n) =
k:∞) > n−O(log n).

$$
k\;\in\;\{1,\ldots,n\}
$$

$$
q_{k}^{*}
$$

$$
q_{k}^{\prime}
$$

$$
\omega_{m+k:\infty}
$$

$$
q_{k}^{*}
$$

$$
\ell(q_{k}^{\prime})=\ell(q_{k}^{*})+O(\log n)
$$

$$
K(\omega_{k:\infty})+O(\log n)
$$

$$
n=K(y)\leq\ell(q_k')
$$

$$
K(\omega_{k:\infty})>n-O(\log n)
$$

Using a more sophisticated version of this proof it can be shown that there
exist predictors that can learn to predict arbitrary regular or primitive recursive sequences. Thus we might wonder whether there exists a computable
predictor able to learn to predict all computable sequences. Unfortunately, no
universal predictor exists, indeed for every predictor there exists a sequence
which it cannot predict at all:

5.2.4 Lemma. For any predictor p there constructively exists a sequence
+
ω := x1x2... ∈C such that ∀n ∈ N : p(x1:n) = xn+1 and K(ω) < K(p).

$$
\omega:=x_{1}x_{2}\ldots\in\mathcal{C}
$$

$$
\forall n\in\mathbb{N}:p(x_{1:n})\neq x_{n+1}
$$

$$
K(\omega)\stackrel{\mp}{<}K(p)
$$

Proof. For any computable predictor p there constructively exists a computable sequence ω = x1x2x3... computed by an algorithm q defined as follows: Set x1 = 1 − p(λ), then x2 = 1 − p(x1), then x3 = 1 − p(x1:2) and so on.
Clearly ω ∈C and ∀n ∈ N : p(x1:n) = 1 − xn+1.

$$
x_{1}=1-p(\lambda)
$$

$$
\omega=x_{1}x_{2}x_{3}\ldots
$$

$$
x_{2}=1-p(x_{1})
$$

$$
x_{3}=1-p(x_{1:2})
$$

$$
\omega\in\mathcal{C}
$$

$$
\forall n\in\mathbb{N}:p(x_{1:n})=1-x_{n+1}
$$

Let p∗ be the shortest program that computes the same function as p and
define a sequence generation algorithm q∗ based on p∗ using the procedure
above. By construction, ℓ(q∗) = ℓ(p∗) + c for some constant c that is independent of p∗. Because q∗ generates ω, it follows that K(ω) ≤ ℓ(q∗). By definition
+
K(p) = ℓ(p∗) and so K(ω) < K(p).

$$
p^{*}
$$

$$
q^{*}
$$

$$
p^{*}
$$

$$
\ell(q^*)=\ell(p^*)+c
$$

$$
p^{*}
$$

$$
q^{*}
$$

$$
\omega
$$

$$
K(\omega)\leq\ell(q^{*})
$$

$$
K(p)=\ell(p^*)
$$

$$
K(\omega)\stackrel{+}{<}K(p)
$$

5. Limits of Computational Agents

Allowing the predictor to be probabilistic, as we did in previous chapters,
does not fundamentally avoid the problem of Lemma 5.2.4. In each step, rather
than generating the opposite to what will be predicted by p, instead q attempts
to generate the symbol that p is least likely to predict given x1:n. To do this
q must simulate p in order to estimate the probability that p(x1:n) = 1. With
sufficient simulation effort, q can estimate this probability to any desired accuracy for any x1:n. This produces a computable sequence ω such that ∀n ∈ N
the probability that p(x1:n) = xn+1 is not significantly greater than 1/2, that
is, the performance of p is no better than a predictor that makes completely
random predictions. As probabilistic prediction complicates things without
avoiding this problem, in this chapter we will consider only deterministic predictors. This will also allow us to see the root of this problem as clearly as
possible.

$$
p,
$$

$$
p
$$

$$
x_{1:n}
$$

$$
p
$$

$$
p(x_{1:n})=1
$$

$$
x_{1:n}
$$

$$
\omega
$$

$$
\forall n\in\mathbb{N}
$$

$$
p(x_{1:n})=x_{n+1}
$$

$$
\frac{1}{2}
$$

With the preliminaries covered, we now move on to the central problem:
predicting sequences of limited Kolmogorov complexity.

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
