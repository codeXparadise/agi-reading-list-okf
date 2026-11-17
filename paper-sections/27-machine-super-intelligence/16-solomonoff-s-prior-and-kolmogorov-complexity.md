---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: "2.4. Solomonoff’s prior and Kolmogorov complexity"
section_role: other
section_index: 16
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "In the 1960’s Ray J. Solomonoff (1926–) investigated the problem of inductive inference from the perspective of binary sequence prediction…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.4. Solomonoff’s prior and Kolmogorov complexity

> Section 16 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

In the 1960’s Ray J. Solomonoff (1926–) investigated the problem of inductive
inference from the perspective of binary sequence prediction (Solomonoff 1964;
1978). He was interested in a very general form of the problem, specifically,
learning to predict a binary sequence that has been sampled from an arbitrary
unknown computable distribution. Solomonoff defined his prior distribution
over sequences as follows: The prior probability that a sequence begins with
a string x ∈ B∗ is the probability that a universal Turing machine running
a randomly generated program computes a sequence that begins with x. By
randomly generated, we mean that the bits of the program have a uniform
distribution, for example, they could come from flipping a fair coin. Formally,

$$
x\in\mathbb{B}^*
$$

2.4.1 Definition.
with the string x ∈ B

The Solomonoff prior probability that a sequence begins
∗ is,
∑

$$
x\in\mathbb{B}^*
$$

$$
M(\underline{{x}}):=\sum_{p:\mathcal{U}(p)=x*}2^{-\ell(p)},
$$

where U (p) = x∗ means that the universal Turing machine U computes an
output sequence that begins with x ∈ B∗ when it runs the program p, and ℓ(p)
is the length of p in bits.

$$
\mathcal{U}(p)=x*
$$

$$
x\in\mathbb{B}^*
$$

$$
p,
$$

$$
\ell(p)
$$

Note that the 2−ℓ(p) term in this definition comes from the fact that the
probability of p under a uniform distribution halves for each additional bit.

$$
2^{-\ell(p)}
$$

We will assume that U is a prefix universal Turing machine. This means
that no valid program for U is a prefix of any other. More precisely, if p,q ∈ B∗
are valid programs on U, then there does not exist a string x ∈ B∗ such that
p = qx. Prefix universal Turing machines have technical properties that we
will need and so throughout this thesis we will assume that U is of this type.
Technically, U is actually a type of prefix universal Turing machine known as
a monotone universal Turing machine (see Section 5.1). For the moment we
can safely gloss over these details.

$$
p,q\in\mathbb{B}^{*}
$$

$$
\mathcal{U}.
$$

$$
x\in\mathbb{B}^*
$$

$$
p=qx
$$

2.4.2 Example. Rather than a classic universal Turing machine running a
program specified by a binary string on an input tape, it is often more intuitive
to think in terms of a program written in a high level programing language
that is being executed on a real computer. Indeed, if a computer had infinite
memory and never broke down it would be technically equivalent to a universal
Turing machine. Consider a short program in C that prints a binary sequence
of all 1’s:

$$
\mathrm{main}()\{\mathrm{while}(1)\mathrm{print}(1);\}
$$

As far as C programs go, this is nearly as simple as they get. This is not
surprising given that the output is also very simple. If we want a program that
generates a more complex sequence, such as an infinite sequence of successive
digits of the mathematical constant π = 3.141592..., such a program would
be at least ten times as long. It follows then that the probability of randomly
generating a program that outputs all 1’s is far higher than the probability of
randomly generating a program that computes π. Thus, Solomonoff’s prior
assigns much higher probability to the sequences of all 1’s than to the sequence
for π. More complex sequences would require still larger programs and thus
have even lower prior probability.

$$
\pi=3.141592\ldots
$$

$$
\pi
$$

$$
\pi
$$

$$
\diamondsuit
$$

Although Solomonoff’s definition requires nothing more than random bits
being fed into a universal Turing machine, we can see that the resulting distribution over sequences neatly formalises Occam’s razor. Specifically, sets
of sequences that have short programs, and are thus in some sense simple,
are given higher prior probability than sets of sequences that have only long
programs.

The idea that the complexity of a sequence is related to the length of the
shortest program that generates the sequence motivates the following definition:

2.4.3 Definition. The Kolmogorov complexity of a sequence ω ∈ B∞ is,

$$
\omega\in\mathbb{B}^{\infty}
$$

$$
K(\omega):=\min_{p\in\mathbb{B}^{*}}\left\{\ell(p):\mathcal{U}(p)=\omega\right\},
$$ where U is a prefix universal Turing machine. If no such p exists, we define
K(ω) = ∞. For a string x ∈ B∗, we define K(x) to be the length of the
shortest program that outputs x and then halts.

$$
K(\omega)=\infty
$$

$$
x\in\mathbb{B}^*
$$

$$
K(x)
$$

Kolmogorov complexity has many powerful theoretical properties and is a
central ingredient in the theory of universal artificial intelligence. Its most
important property is that the complexity it assigns to strings and sequences
does not depend too much on the choice of the universal Turing machine U.
This comes from the fact that universal Turing machines are universal in the
sense that they are able to simulate each other with a constant number of
additional input bits. Thus, if we change U above to some other universal
Turing machine U′, the minimal value of ℓ(p) and thus K(x), can only change
by a bounded number of bits. This bound depends on U and U′, but not on
x.

$$
\ell(p)
$$

$$
\mathcal{U}'
$$

$$
K(x)
$$

$$
\mathcal{U}'
$$

$$
x.
$$

The biggest problem with Kolmogorov complexity is that the value of K
is not in general computable. It can only be approximated from above. The
reason for this is that in general we cannot find the shortest program to compute a string x on U due to the halting problem. Intuitively, there might exist
a very short program p∗ such that U (p∗) = x, however we do not know this
because p∗ takes such a long time to run. Nevertheless, in theoretical applications the simplicity and theoretical power of Kolmogorov complexity often
outweighs this computability problem. In practical applications Kolmogorov
complexity is approximated, for example by using a compression algorithm to
estimate the length of the shortest program (Cilibrasi and Vit´anyi, 2005).

$$
\mathcal{U}
$$

$$
p^{*}
$$

$$
\mathcal{U}(p^*)=x
$$

$$
p^{*}
$$

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
