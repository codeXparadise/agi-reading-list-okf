---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 5.4. Complexity of prediction
section_role: other
section_index: 47
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "Another way of viewing these results is in terms of an alternate notion of sequence complexity defined as the size of the smallest predictor able to…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 5.4. Complexity of prediction

> Section 47 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

Another way of viewing these results is in terms of an alternate notion of
sequence complexity defined as the size of the smallest predictor able to learn
to predict the sequence. This allows us to express the results of the previous
sections more concisely. Formally, for any sequence ω define the complexity
measure,
K˙ (ω) := min { ℓ(p) : p ∈P (ω)},

$$
\omega
$$

$$
\dot{K}(\omega):=\min_{p\in\mathbb{B}^{*}}\left\{\ell(p):p\in\mathcal{P}(\omega)\right\},
$$

and K˙ (ω) := ∞ if P (ω) = ∅. Thus, if K˙ (ω) is high then the sequence ω is
complex in the sense that only complex prediction algorithms are able to learn
to predict it. It can easily be seen that this notion of complexity has the same
invariance to the choice of reference universal Turing machine as the standard
Kolmogorov complexity measure.

$$
\dot{K}(\omega):=\infty if\mathcal{P}(\omega)=\varnothing
$$

$$
\dot{K}(\omega)
$$

$$
\omega
$$

It may be tempting to conjecture that this definition simply describes what
might be called the “tail complexity” of a sequence, that is, K˙ (ω) is equal to
lim infi→∞K(ωi:∞). This is not the case. In the proof of Lemma 5.2.3 we saw
that there exists a single predictor capable of learning to predict any sequence
that consists of a repeating string, and thus for these sequences K˙ is bounded.
It was further shown that there exist sequences of this form with arbitrarily
high tail complexity. Clearly then tail complexity and K˙ cannot be equal in
general.

$$
\dot{K}(\omega)
$$

$$
\operatorname{f}_{i\to\infty}K(\omega_{i:\infty})
$$

$$
\dot{K}
$$

Using K˙ we can now rewrite a number of our previous results much more
succinctly. From Lemma 5.2.1 it immediately follows that,

$$
\dot{K}
$$

$$
\forall\omega:0\leq\dot{K}(\omega)\stackrel{+}{<}K(\omega).
$$

From Lemma 5.2.2 we know that ∃c ∈ N, ∀n ∈ N, ∃ ω ∈C such that K˙ (ω) < c
and K(ω) > n, that is, K˙ can attain the lower bound above within a small
constant, no matter how large the value of K is. The sequences for which the
upper bound on K˙ is tight are interesting as they are the ones which demand
complex predictors. We prove the existence of these sequences and look at
some of their properties in the next section.

$$
\exists c\in\mathbb{N},\forall n\in\mathbb{N},\exists\omega\in\mathcal{C}
$$

$$
K(\omega)>n
$$

$$
\dot{K}(\omega)<c
$$

$$
\dot{K}
$$

$$
\dot{K}
$$

The complexity measure K˙ can also be generalised to sets of sequences, for
∞
S⊂B define K˙ (S) := minp { ℓ(p) : p ∈P (S)}. This allows us to rewrite
Lemma 5.3.2 and Theorem 5.3.3 as simply,

$$
\dot{K}
$$

$$
S\subset\mathbb{B}^{\infty}
$$

$$
\dot{K}(S):=\min_{p}\left\{\ell(p):p\in\mathcal{P}(S)\right\}
$$

$$
\forall n\in\mathbb{N}\::\:n\:\stackrel{+}{<}\dot{K}(\mathcal{C}_{n})\:\stackrel{+}{<}\:n+O(\log n).
$$

This is just a restatement of the fact that the simplest predictor capable of
predicting all sequences up to a Kolmogorov complexity of n, has itself a
Kolmogorov complexity of roughly n.

$$
n,
$$

Perhaps the most surprising thing about K˙ complexity is that this very natural definition of the complexity of a sequence, as viewed from the perspective
of prediction, does not appear to have been studied before.

$$
\dot{K}
$$

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
