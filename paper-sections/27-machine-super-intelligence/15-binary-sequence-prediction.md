---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 2.3. Binary sequence prediction
section_role: other
section_index: 15
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "An alternate characterisation of inductive inference can be made in terms of binary sequence prediction. One reason this is useful is that binary…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.3. Binary sequence prediction

> Section 15 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

An alternate characterisation of inductive inference can be made in terms of
binary sequence prediction. One reason this is useful is that binary sequences
and strings provide a more natural setting in which to deal with issues of computability. The problem can be formulated as follows: There is an unknown
probability distribution µ over the space of binary sequences B∞. From this
distribution a sequence ω is drawn one bit at a time. At time t ∈ N we have
observed the initial string ω1:t:= ω1ω2...ωt, and our task is to predict what
the next bit in the sequence will be, that is, ωt+1. To do this we select a
model, or models, from a set of potential models that explain the observed
sequence so far and that, we hope, will be good at predicting future bits in
the sequence.

$$
\mu
$$

$$
\mathbb{B}^{\infty}
$$

$$
\omega
$$

$$
t\in\mathbb{N}
$$

$$
\omega_{1:t}:=\omega_{1}\omega_{2}\cdots\omega_{t}
$$

$$
\omega_{t+1}
$$

In terms of inductive inference the observed initial binary string ω1:t is the
observed data D, and our set of potential models of the data is the set of
hypotheses H. We would like to find a model ν ∈H, or models, that are as
close as possible to the unknown true model of the data µ, in the sense that ν
will allow us to predict future bits in the sequence as accurately as possible.

$$
\omega_{1:t}
$$

$$
\mathcal{D}.
$$

$$
\nu\in\mathcal{H}
$$

$$
\mathcal{H}.
$$

$$
\mu,
$$

We begin by clarifying what we mean by a probability distribution. In mathematical statistics a probability distribution is known as a probability measure

2. Universal Artificial Intelligence

as it belongs to the class of functions known as measures. Over the space of
binary strings these can be defined as follows:

2.3.1 Definition. A probability measure is a function ν : B∗ → [0, 1] such
that,
ν(ǫ) = 1,

$$
\nu:\mathbb{B}^{*}\to[0,1]
$$

$$
\nu(\underline{\epsilon})=1,
$$

$$
\forall x\in\mathbb{B}^*\quad\nu(\underline{x})=\nu(\underline{x}\underline{0})+\nu(\underline{x}\underline{1}).
$$

In this thesis we will interpret ν(x) to mean the probability that a binary
sequence sampled according to the distribution ν begins with the string x ∈ B∗.
As all strings and sequences begin with the null string ǫ, by definition, the first
condition above simply says that the ν probability that a sequence belongs to
the set of all sequences is 1. The second condition says that the ν probability
that a sequence begins with string x0, plus the ν probability that it begins with
x1, is equal to the ν probability that it begins with x. This makes sense given
that all sequences that begin with x must have either a 0 or a 1 as their next
bit and so we would expect the probabilities of these sets of sequences to add
up. This style of notation for measures will be convenient for our purposes,
however it is somewhat unusual. To see how it relates to conventional measure
theory see Appendix A.

$$
\nu(\underline{{x}})
$$

$$
x\in\mathbb{B}^*
$$

Sequence prediction forms a large part of this thesis and thus we will often
be interested in what comes next in a sequence given an initial string. More
precisely, if a sequence ω has been sampled from the distribution µ, and ω
begins with the string y ∈ B∗, what is the probability that the next bits from
ω will be the string x ∈ B∗? For this will we adopt the following notation for
the conditional probability, µ(yx) := µ(yx)/µ(y). The benefit of this notation
will become apparent later when we need to deal with complex interaction
sequences. Not only does it preserve the order in which the sequence occurs,
it also allows for more compact expressions when we need to condition on only
certain parts of a sequence.

$$
\omega
$$

$$
\mu,
$$

$$
\omega
$$

$$
y\in\mathbb{B}^*
$$

$$
x\in\mathbb{B}^*?
$$

$$
\mu(y\underline{x}):=\mu(\underline{y x})/\mu(\underline{y})
$$

As noted earlier in this section, sequence prediction can be viewed as an
inductive inference problem. Thus, we can use Bayes’ rule to estimate how
likely some model ν ∈H is given the observed sequence ω1:t:

$$
\nu\in\mathcal{H}
$$

$$
\omega_{1:t}:
$$

$$
P\left(\nu\middle|\omega_{1:t}\right)=\frac{P\left(\underline{\omega}_{1:t}\middle|\nu\right)P\left(\nu\right)}{P\left(\underline{\omega}_{1:t}\right)}=\frac{\nu\left(\underline{\omega}_{1:t}\right)P\left(\nu\right)}{\sum_{\varrho\in\mathcal{H}}\varrho\left(\underline{\omega}_{1:t}\right)P\left(\varrho\right)}.
$$

2.3.2 Example. Consider the problem of inferring whether a coin is a normal fair coin based on a sample of coin flips. To simplify things, assume
that the coin is either heads on both sides, tails on both sides, or a normal fair coin. Further assume that t = 4 and we have the observed data
D = head, head, head, head. In terms of binary sequence prediction, the outcome of t coin tosses can be expressed as a string ω1:t ∈ Bt, with each tail being
represented as a 0 bit, and each head as a 1 bit. Thus we have ω1:4 = 1111.

$$
\omega_{1:t}\in\mathbb{B}^t
$$

$$
\omega_{1:4}=1111
$$

Let H be the set of models consisting of the distributions νp(ω1:t) := pr(1 −
{} ∑t
p)t−r, where p ∈ 0, 1/2, 1 and r :=i=1ωi is the number of observed heads.

$$
\nu_{p}(\underline{\omega}_{1:t}):=p^{r}(1-
$$

$$
p)^{t-r}
$$

$$
p\in\left\{0,\frac{1}{2},1\right\}
$$

$$
r:=\sum_{i=1}^{t}\omega_{i}
$$

As there are just three models in H, assume a uniform prior, that is, ∀p ∈
{}
0, 21, 1 let P (νp) := 1/3. Now from Bayes’ rule,

$$
\mathcal{H},
$$

$$
\forall p\in
$$

$$
\left\{0,\frac{1}{2},1\right\}
$$

$$
P(\nu_{p}):=\frac{1}{3}
$$

$$
P(\nu_{\frac{1}{2}}|\omega_{1:4}=1111)\;=\;\frac{\frac{1}{3}\left(\frac{1}{2}\right)^{4}\left(1-\frac{1}{2}\right)^{0}}{\frac{1}{3}\left[0^{4}(1-0)^{0}+\left(\frac{1}{2}\right)^{4}\left(1-\frac{1}{2}\right)^{0}+1^{4}(1-1)^{0}\right]}\;=\;\frac{1}{17}.
$$

Similarly, P (ν0|ω1:4 = 1111) = 0 and P (ν1|ω1:4 = 1111) = 16/17. Thus the results
clearly point towards the coin being double headed, as we would expect having
just observed four heads in a row.

$$
P(\nu_{0}|\omega_{1:4}=1111)=0
$$

$$
P(\nu_{1}|\omega_{1:4}=1111)=\frac{16}{17}
$$

More complex examples could involve data collected from medical measurements, music or weather satellite images. Good models would then have to
describe biological processes, music styles, or the dynamics of weather systems
respectively. In each case the binary string representing D could be simply the
string of bits as they would appear in a computer file. However, finding a good
prior over such spaces is not trivial. Furthermore, actually computing Bayes’
rule and finding the most likely models, as we did in the example above, can
become very computationally difficult and may need to be approximated. In
any case, Bayes’ rule at least tells us how to solve the induction problem in
theory, so long as we have a prior distribution.

Rather than just estimating which model or models are the most likely, we
may be interested in actually predicting the sequence. One possibility is to
calculate the probability that the next bit is a 1 based on the most likely model.
The full Bayesian approach, however, is to consider each possible model ν ∈H
and weight the prediction made by each according to how confident we are
about each model, i.e. P (ν|ω1:t). This gives us the mixture model predictor,

$$
\nu\in\mathcal{H}
$$

$$
P(\nu|\omega_{1:t})
$$

$$
\begin{align*}P(\omega_{1:t}\underline{1})\quad=&\quad\sum_{\nu\in\mathcal{H}}P(\nu|\omega_{1:t})\nu(\omega_{1:t}\underline{1})\\=&\quad\sum_{\nu\in\mathcal{H}}\frac{\nu(\underline{\omega}_{1:t})P(\nu)}{P(\underline{\omega}_{1:t})}\frac{\nu(\underline{\omega}_{1:t}\underline{1})}{\nu(\underline{\omega}_{1:t})}=\frac{P(\underline{\omega}_{1:t}\underline{1})}{P(\underline{\omega}_{1:t})}.\end{align*}
$$

As we can see, the Bayes mixture predictor reduces to the definition of conditional probability. This has removed the prior over H, and in its place we now
have the related prior over D, in this setting the space of binary sequences.
The fact that we can use one prior to define the other means that the two
unknown priors are in fact two perspectives on the same fundamental problem
of specifying our prior knowledge.

$$
\mathcal{H},
$$

2.3.3 Example. Continuing Example 2.3.2, we can compute the prior distribution over sequences from the prior distribution over H,
∑

$$
\mathcal{H}
$$

$$
\begin{array}{r c l}{P(\underline{{\omega}}_{1:t})}&{=}&{\sum_{\nu\in\mathcal{H}}\nu(\underline{{\omega}}_{1:t})P(\nu)}\\ {}&{=}&{\frac{1}{3}\left[0^{t}(1-0)^{t-r}+\left(\frac{1}{2}\right)^{t}\left(1-\frac{1}{2}\right)^{t-r}+1^{t}(1-1)^{t-r}\right]}\\ {}&{=}&{\frac{1}{3}\left[\left(\frac{1}{2}\right)^{2t-r}+\delta_{t r}\right].}\\ \end{array}
$$

∑t
where r :=i=1ωi is the number of observed heads, and the Kronecker delta
symbol δab is defined to be 1 if a = b, and 0 otherwise. Thus, given that
ω1:4 = 1111, according to the mixture model the probability that the next bit
is a 1 is,
[(1)2(5)−5]
1()5

$$
r:=\sum_{i=1}^{t}\omega_{i}
$$

$$
\delta_{ab}
$$

$$
a=b
$$

$$
\omega_{1:4}=1111
$$

$$
P(1111\underline{1})=\frac{\frac{1}{3}\left[\left(\frac{1}{2}\right)^{2(5)-5}+\delta_{5,5}\right]}{\frac{1}{3}\left[\left(\frac{1}{2}\right)^{2(4)-4}+\delta_{4,4}\right]}=\frac{\left(\frac{1}{2}\right)^{5}+1}{\left(\frac{1}{2}\right)^{4}+1}=\frac{33}{34}.
$$

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
