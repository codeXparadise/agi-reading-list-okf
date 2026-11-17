---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
section: "2.5 Information Theory II: Universal Codes and Models"
section_role: other
section_index: 14
pages: [36, 37, 38, 39, 40, 41, 42, 43]
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "We have just indicated why the two-part code formulation of MDL needs to be refined. It turns out that the key concept we need is that of universal…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.5 Information Theory II: Universal Codes and Models

> Section 14 of 23 from [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · `other` · pages 36-43

We have just indicated why the two-part code formulation of MDL needs to be refined. It turns out that the key concept we need is that of universal coding. Broadly speaking, a code ¯L that is universal relative to a set of candidate codes L allows us to compress every sequence xn almost as well as the code in L that compresses that particular

37

sequence most. Two-part codes are universal (Section 2.5.1), but there exist other universal codes such as the Bayesian mixture code (Section 2.5.2) and the Normalized Maximum Likelihood (NML) code (Section 2.5.3). We also discuss universal models, which are just the probability distributions corresponding to universal codes. In this section, we are not concerned with learning from data; we only care about compressing data as much as possible. We reconnect our findings with learning in Section 2.6.

Coding as Communication Like many other topics in coding, ‘universal coding’ can best be explained if we think of descriptions as messages: we can always view a description as a message that some sender or encoder, say Mr. A, sends to some receiver or decoder, say Mr. B. Before sending any messages, Mr. A and Mr. B meet in person. They agree on the set of messages that A may send to B. Typically, this will be the set X n of sequences x1, . . . , xn, where each xi is an outcome in the space X . They also agree upon a (prefix) code that will be used by A to send his messages to B. Once this has been done, A and B go back to their respective homes and A sends his messages to B in the form of binary strings. The unique decodability property of prefix codes implies that, when B receives a message, he should always be able to decode it in a unique manner.

Universal Coding Suppose our encoder/sender is about to observe a sequence xn ∈ X n which he plans to compress as much as possible. Equivalently, he wants to send an encoded version of xn to the receiver using as few bits as possible. Sender and receiver have a set of candidate codes L for X n available14. They believe or hope that one of these codes will allow for substantial compression of xn. However, they must decide on a code for X n before sender observes the actual xn, and they do not know which code in L will lead to good compression of the actual xn. What is the best thing they can do? They may be tempted to try the following: upon seeing xn, sender simply encodes/sends xn using the L ∈L that minimizes L(xn) among all L ∈L. But this naive scheme will not work: since decoder/receiver does not know what xn

has been sent before decoding the message, he does not know which of the codes in L has been used by sender/encoder. Therefore, decoder cannot decode the message: the resulting protocol does not constitute a uniquely decodable, let alone a prefix code. Indeed, as we show below, in general no code ¯L exists such that for all xn ∈X n,

¯L(xn) ≤minL∈L L(xn): in words, there exists no code which, no matter what xn is, always mimics the best code for xn.

Example 2.9 Suppose we think that our sequence can be reasonably well-compressed by a code corresponding to some biased coin model. For simplicity, we restrict ourselves to a finite number of such models. Thus, let L = {L1, . . . , L9} where L1 is the code length function corresponding to the Bernoulli model P(· | θ) with parameter θ = 0.1, L2 corresponds to θ = 0.2 and so on. From (2.7) we see that, for example,

L8(xn) = −log P(xn|0.8) = −n\[0\] log 0.2 −n\[1\] log 0.8 L9(xn) = −log P(xn|0.9) = −n\[0\] log 0.1 −n\[1\] log 0.9.

38

Both L8(xn) and L9(xn) are linearly increasing in the number of 1s in xn. However, if the frequency n1/n is approximately 0.8, then minL∈L L(xn) will be achieved for L8. If n1/n ≈0.9 then minL∈L L(xn) is achieved for L9. More generally, if n1/n ≈j/10 then Lj achieves the minimum15. We would like to send xn using a code ¯L such that for all xn, we need at most ˆL(xn) bits, where ˆL(xn) is defined as ˆL(xn) := minL∈L L(xn). Since −log is monotonically decreasing, ˆL(xn) = −log P(xn | ˆθ(xn)). We already gave an informal explanation as to why a code with lengths ˆL does not exist. We can now explain this more formally as follows: if such a code were to exist, it would correspond to some distribution ¯P. Then we would have for all xn, ¯L(xn) = −log ¯P(xn). But, by definition, for all xn ∈X n, ¯L(xn) ≤ˆL(xn) = −log P(xn|ˆθ(xn)) where ˆθ(xn) ∈ {0.1, . . . , 0.9}. Thus we get for all xn, −log ¯P(xn) ≤−log P(xn | ˆθ(xn)) or ¯P(xn) ≥ P(xn | ˆθ(xn)), so that, since |L| > 1,

P(xn | ˆθ(xn)) =

θ P(xn | θ) > 1, (2.10)

¯P(xn) ≥

X

X

X

max

xn

xn

xn

where the last inequality follows because for any two θ1, θ2 with θ1̸ = θ2, there is at least one xn with P(xn | θ1) > P(xn | θ2). (2.10) says that ¯P is not a probability distribution. It follows that ¯L cannot be a codelength function. The argument can be extended beyond the Bernoulli model of the example above: as long as |L| > 1, and all codes in L correspond to a non-defective distribution, (2.10) must still hold, so that there exists no code ¯L with ¯L(xn) = ˆL(xn) for all xn. The underlying reason that no such code exists is the fact that probabilities must sum up to something ≤1; or equivalently, that there exists no coding scheme assigning short code words to many diﬀerent messages – see Example 2.2.

Since there exists no code which, no matter what xn is, always mimics the best code for xn, it may make sense to look for the next best thing: does there exist a code which, for all xn ∈X n, is ‘nearly’ (in some sense) as good as ˆL(xn)? It turns out that in many cases, the answer is yes: there typically exists codes ¯L such that no matter what xn arrives, ¯L(xn) is not much larger than ˆL(xn), which may be viewed as the code that is best ‘with hindsight’ (i.e., after seeing xn). Intuitively, codes which satisfy this property are called universal codes - a more precise definition follows below. The first (but perhaps not foremost) example of a universal code is the two-part code that we have encountered in Section 2.4.

2.5.1 Two-part Codes as simple Universal Codes

Example 2.10 \[finite L\] Let L be as in Example 2.9. We can devise a code ¯L2-p for all xn ∈X n as follows: to encode xn, we first encode the j ∈{1, . . . , 9} such that Lj(xn) = minL∈L L(xn), using a uniform code. This takes log 9 bits. We then encode xn itself using the code indexed by j. This takes Lj bits. Note that in contrast to the naive scheme discussed in Example 2.9, the resulting scheme properly defines a prefix code: a decoder can decode xn by first decoding j, and then decoding xn using Lj.

39

Thus, for every possible xn ∈X n, we obtain

¯L2-p(xn) = min

L∈L L(xn) + log 9.

For all L ∈L, minxn L(xn) grows linearly in n: minθ,xn −log P(xn | θ) = −n log 0.9 ≈ 0.15n. Unless n is very small, no matter what xn arises, the extra number of bits we need using ¯L2-p compared to ˆL(xn) is negligible.

More generally, let L = {L1, . . . , LM} where M can be arbitrarily large, and the Lj can be any codelength functions we like; they do not necessarily represent Bernoulli distributions any more. By the reasoning of Example 2.10, there exists a (two-part) code such that for all xn ∈X n,

¯L2-p(xn) = min

L∈L L(xn) + log M. (2.11)

In most applications min L(xn) grows linearly in n, and we see from (2.11) that, as soon as n becomes substantially larger than log M, the relative diﬀerence in performance between our universal code and ˆL(xn) becomes negligible. In general, we do not always want to use a uniform code for the elements in L; note that any arbitrary code on L will give us an analogue of (2.11), but with a worst-case overhead larger than log M corresponding to the largest codelength of any of the elements in L.

Example 2.11 \[Countably Infinite L\] We can also construct a 2-part code for arbitrary countably infinite sets of codes L = {L1, L2, . . . }: we first encode some k using our simple code for the integers (Example 2.4). With this code we need 2 log k + 1 bits to encode integer k. We then encode xn using the code Lk. ¯L2-p is now defined as the code we get if, for any xn, we encode xn using the Lk minimizing the total two-part description length 2 log k + 1 + Lk(xn).

In contrast to the case of finite L, there does not exist a constant c any more such that for all n, xn ∈X n, ¯L2-p(xn) ≤infL∈L L(xn) + c. Instead we have the following weaker, but still remarkable property: for all k, all n, all xn, ¯L2-p(xn) ≤Lk(xn) + 2 log k + 1, so that also,

¯L2-p(xn) ≤ inf L∈{L1,... ,Lk} L(xn) + 2 log k + 1.

For any k, as n grows larger, the code ¯L2-p starts to mimic whatever L ∈{L1, . . . , Lk} compresses the data most. However, the larger k, the larger n has to be before this happens.

2.5.2 From Universal Codes to Universal Models

Instead of postulating a set of candidate codes L, we may equivalently postulate a set M of candidate probabilistic sources, such that L is the set of codes corresponding to M. We already implicitly did this in Example 2.9.

40

The reasoning is now as follows: we think that one of the P ∈M will assign a high likelihood to the data to be observed. Therefore we would like to design a code that, for all xn we might observe, performs essentially as well as the code corresponding to the best-fitting, maximum likelihood (minimum codelength) P ∈M for xn. Similarly, we can think of universal codes such as the two-part code in terms of the (possibly defective, see Section 2.2 and Figure 2.1)) distributions corresponding to it. Such distributions corresponding to universal codes are called universal models. The use of mapping universal codes back to distributions is illustrated by the Bayesian universal model which we now introduce.

Universal model: Twice Misleading Terminology The words ‘universal’ and ‘model’ are somewhat of a misnomer: first, these codes/models are only ‘universal’ relative to a restricted ‘universe’ M. Second, the use of the word ‘model’ will be very confusing to statisticians, who (as we also do in this paper) call a family of distributions such as M a ’model’. But the phrase originates from information theory, where a ‘model’ often refers to a single distribution rather than a family. Thus, a ‘universal model’ is a single distribution, representing a statistical ‘model’ M.

Example 2.12 \[Bayesian Universal Model\] Let M be a finite or countable set of probabilistic sources, parameterized by some parameter set Θ. Let W be a distribution on Θ. Adopting terminology from Bayesian statistics, W is usually called a prior distribution. We can construct a new probabilistic source ¯PBayes by taking a weighted (according to W) average or mixture over the distributions in M. That is, we define for all n, xn ∈X,

P(xn | θ)W(θ). (2.12)

¯PBayes(xn) :=

X

θ∈Θ

It is easy to check that ¯PBayes is a probabilistic source according to our definition. In case Θ is continuous, the sum gets replaced by an integral but otherwise nothing changes in the definition. In Bayesian statistics, ¯PBayes is called the Bayesian marginal likelihood or Bayesian mixture \[Bernardo and Smith 1994\]. To see that ¯PBayes is a universal model, note that for all θ0 ∈Θ,

P(xn | θ)W(θ) ≤−log P(xn | θ0) + cθ0 (2.13)

−log ¯PBayes(xn) := −log

X

θ∈Θ

where the inequality follows because a sum is at least as large as each of its terms, and cθ = −log W(θ) depends on θ but not on n. Thus, ¯PBayes is a universal model or equivalently, the code with lengths −log ¯PBayes is a universal code. Note that the derivation in (2.13) only works if Θ is finite or countable; the case of continuous Θ is treated in Section 2.6.

41

Bayes is Better than Two-part The Bayesian model is in a sense superior to the two-part code. Namely, in the two-part code we first encode an element of M or its parameter set Θ using some code L0. Such a code must correspond to some ‘prior’ distribution W on M so that the two-part code gives codelengths

¯L2-p(xn) = min

θ∈Θ −log P(xn|θ) −log W(θ) (2.14)

where W depends on the specific code L0 that was used. Using the Bayes code with prior W, we get as in (2.13),

P(xn | θ)W(θ) ≤min

−log ¯PBayes(xn) = −log

X

θ∈Θ −log P(xn|θ) −log W(θ).

θ∈Θ

The inequality becomes strict whenever P(xn|θ) > 0 for more than one value of θ. Comparing to (2.14), we see that in general the Bayesian code is preferable over the two-part code: for all xn it never assigns codelengths larger than ¯L2-p(xn), and in many cases it assigns strictly shorter codelengths for some xn. But this raises two important issues: (1) what exactly do we mean by ‘better’ anyway? (2) can we say that ‘some prior distributions are better than others’? These questions are answered below.

2.5.3 NML as an Optimal Universal Model

We can measure the performance of universal models relative to a set of candidate sources M using the regret:

Definition 2.13 \[Regret\] Let M be a class of probabilistic sources. Let ¯P be a probability distribution on X n ( ¯P is not necessarily in M). For given xn, the regret of ¯P relative to M is defined as

−log ¯P(xn) −min

P ∈M{−log P(xn)}. (2.15)

The regret of ¯P relative to M for xn is the additional number of bits needed to encode xn using the code/distribution ¯P, as compared to the number of bits that had been needed if we had used code/distribution in M that was optimal (‘best-fitting’) with hind-sight. For simplicity, from now on we tacitly assume that for all the models M we work with, there is a single ˆθ(xn) maximizing the likelihood for every xn ∈X n. In that case (2.15) simplifies to

−log ¯P(xn) −{−log P(xn | ˆθ(xn))}.

We would like to measure the quality of a universal model ¯P in terms of its regret. However, ¯P may have small (even < 0) regret for some xn, and very large regret for other xn. We must somehow find a measure of quality that takes into account all xn ∈X n. We take a worst-case approach, and look for universal models ¯P with small

42

worst-case regret, where the worst-case is over all sequences. Formally, the maximum or worst-case regret of ¯P relative to M is defined as

−log ¯P(xn) −{−log P(xn | ˆθ(xn))}

Rmax( ¯P):= max

.

xn∈X n

If we use Rmax as our quality measure, then the ‘optimal’ universal model relative to M, for given sample size n, is the distribution minimizing

−log ¯P(xn) −{−log P(xn | ˆθ(xn))}

¯P Rmax( ¯P) = min

min

¯P max xn∈X n

(2.16)

where the minimum is over all defective distributions on X n. The ¯P minimizing (2.16) corresponds to the code minimizing the additional number of bits compared to code in M that is best in hindsight in the worst-case over all possible xn. It turns out that we can solve for ¯P in (2.16). To this end, we first define the complexity of a given model M as

P(xn | ˆθ(xn)). (2.17)

X

COMPn(M):= log

xn∈X n

This quantity plays a fundamental role in refined MDL, Section 2.6. To get a first idea of why COMPn is called model complexity, note that the more sequences xn with large P(xn | ˆθ(xn)), the larger COMPn(M). In other words, the more sequences that can be fit well by an element of M, the larger M’s complexity.

Proposition 2.14 \[Shtarkov 1987\] Suppose that COMPn(M) is finite. Then the minimax regret (2.16) is uniquely achieved for the distribution ¯Pnml given by

¯Pnml(xn):= P(xn | ˆθ(xn))

. (2.18)

yn∈X n P(yn | ˆθ(yn))

P

The distribution ¯Pnml is known as the Shtarkov distribution or the normalized maximum likelihood (NML) distribution.

Proof Plug in ¯Pnml in (2.16) and notice that for all xn ∈X n,

−log ¯P(xn) −{−log P(xn | ˆθ(xn))} = Rmax( ¯P) = COMPn(M), (2.19)

so that ¯Pnml achieves the same regret, equal to COMPn(M), no matter what xn

actually obtains. Since every distribution P on X n with P̸ = ¯Pnml must satisfy P(zn) <

¯Pnml(zn) for at least one zn ∈X n, it follows that

Rmax(P) ≥−log P(zn) + log P(zn | ˆθ(zn)) >

−log ¯Pnml(zn) + log P(zn | ˆθ(zn)) = Rmax( ¯Pnml).

43

✷

¯Pnml is quite literally a ‘normalized maximum likelihood’ distribution: it tries to assign to each xn the probability of xn according to the ML distribution for xn. By (2.10), this is not possible: the resulting ‘probabilities’ add to something larger than 1. But we can normalize these ‘probabilities’ by dividing by their sum P

yn∈X n P(yn | ˆθ(yn)), and then we obtain a probability distribution on X n after all.

Whenever X is finite, the sum COMPn(M) is finite so that the NML distribution is well-defined. If X is countably infinite or continuous-valued, the sum COMPn(M) may be infinite and then the NML distribution may be undefined. In that case, there exists no universal model achieving constant regret as in (2.19). If M is parametric, then ¯Pnml is typically well-defined as long as we suitably restrict the parameter space. The parametric case forms the basis of ‘refined MDL’ and will be discussed at length in the next section.

Summary: Universal Codes and Models Let M be a family of probabilistic sources. A universal model in an individual sequence sense16 relative to M, in this text simply called a ‘universal model for M’, is a sequence of distributions ¯P (1), ¯P (2), . . . on X 1, X 2, . . . respectively, such that for all P ∈M, for all ǫ > 0,

1

−log ¯P (n)(xn) −\[−log P(xn)\]

max xn∈X n

≤ǫ as n →∞.

n

Multiplying both sides with n we see that ¯P is universal if for every P ∈M, the codelength diﬀerence −log ¯P(xn) + log P(xn) increases sublinearly in n. If M is finite, then the two-part, Bayes and NML distributions are universal in a very strong sense: rather than just increasing sublinearly, the codelength diﬀerence is bounded by a constant. We already discussed two-part, Bayesian and minimax optimal (NML) universal models, but there several other types. We mention prequential universal models (Section 2.6.4), the Kolmogorov universal model, conditionalized two-part codes \[Rissanen 2001\] and Cesaro-average codes \[Barron, Rissanen, and Yu 1998\].

---

Full document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · Page-level evidence: [paper-pages/24-tutorial-minimum-description-length](../../paper-pages/24-tutorial-minimum-description-length/index.md)
