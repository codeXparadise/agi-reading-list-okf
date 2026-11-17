---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/24-tutorial-minimum-description-length.md
source: ../../papers/24-tutorial-minimum-description-length.md
paper_title: A Tutorial Introduction to the Minimum Description Length Principle
sequence: 24
section: "2.2 Information Theory I: Probabilities and Codelengths"
section_role: other
section_index: 11
pages: [23, 24, 25, 26, 27, 28, 29, 30, 31]
topics: ["../../topics/minimum-description-length.md", "../../topics/kolmogorov-complexity.md"]
description: "This first section is a mini-primer on information theory, focusing on the relationship between probability distributions and codes. A good…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.2 Information Theory I: Probabilities and Codelengths

> Section 11 of 23 from [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · `other` · pages 23-31

This first section is a mini-primer on information theory, focusing on the relationship between probability distributions and codes. A good understanding of this relationship is essential for a good understanding of MDL. After some preliminaries, Section 2.2.1 introduces prefix codes, the type of codes we work with in MDL. These are related to probability distributions in two ways. In Section 2.2.2 we discuss the first relationship, which is related to the Kraft inequality: for every probability mass function P, there exists a code with lengths −log P, and vice versa. Section 2.2.3 discusses the second relationship, related to the information inequality, which says that if the data are

24

distributed according to P, then the code with lengths −log P achieves the minimum expected codelength. Throughout the section we give examples relating our findings to our discussion of regularity and compression in Section 1.2 of Chapter 1.

Preliminaries and Notational Conventions - Codes We use log to denote logarithm to base 2. For real-valued x we use ⌈x⌉to denote the ceiling of x, that is, x rounded up to the nearest integer. We often abbreviate x1, . . . , xn to xn. Let X be a finite or countable set. A code for X is defined as a 1-to-1 mapping from X to ∪n≥1{0, 1}n. ∪n≥1{0, 1}n is the set of binary strings (sequences of 0s and 1s) of length 1 or larger. For a given code C, we use C(x) to denote the encoding of x. Every code C induces a function LC : X →N called the codelength function. LC(x) is the number of bits (symbols) needed to encode x using code C.

Our definition of code implies that we only consider lossless encoding in MDL1: for any description z it is always possible to retrieve the unique x that gave rise to it. More precisely, because the code C must be 1-to-1, there is at most one x with C(x) = z. Then x = C−1(z), where the inverse C−1 of C is sometimes called a ‘decoding function’ or ‘description method’.

Preliminaries and Notational Conventions - Probability Let P be a probability distribution defined on a finite or countable set X. We use P(x) to denote the probability of x, and we denote the corresponding random variable by X. If P is a function on finite or countable X such that P

x P(x) < 1, we call P a defective distribution. A defective distribution may be thought of as a probability distribution that puts some of its mass on an imagined outcome that in reality will never appear.

A probabilistic source P is a sequence of probability distributions P (1), P (2), . . . on X 1, X 2, . . . such that for all n, P (n) and P (n+1) are compatible: P (n) is equal to the ‘marginal’ distribution of P (n+1) restricted to n outcomes. That is, for all xn ∈X n, P (n)(xn) = P

y∈X P (n+1)(xn, y). Whenever this cannot cause any confusion, we write P(xn) rather than P (n)(xn). A probabilistic source may be thought of as a probability distribution on infinite sequences2. We say that the data are i.i.d. (independently and identically distributed) under source P if for each n, xn ∈X n, P(xn) = Qn

i=1 P(xi).

2.2.1 Prefix Codes

In MDL we only work with a subset of all possible codes, the so-called prefix codes. A prefix code3 is a code such that no codeword is a prefix of any other codeword. For example, let X = {a, b, c}. Then the code C1 defined by C1(a) = 0, C1(b) = 10, C1(c) = 11 is prefix. The code C2 with C2(a) = 0, C2(b) = 10 and C2(c) = 01, while allowing for lossless decoding, is not a prefix code since 0 is a prefix of 01. The prefix requirement is natural, and nearly ubiquitous in the data compression literature. We now explain why.

Example 2.1 Suppose we plan to encode a sequence of symbols (x1, . . . , xn) ∈X n.

25

We already designed a code C for the elements in X. The natural thing to do is to encode (x1, . . . , xn) by the concatenated string C(x1)C(x2) . . . C(xn). In order for this method to succeed for all n, all (x1, . . . , xn) ∈X n, the resulting procedure must define a code, i.e. the function C(n) mapping (x1, . . . , xn) to C(x1)C(x2) . . . C(xn) must be invertible. If it were not, we would have to use some marker such as a comma to separate the codewords. We would then really be using a ternary rather than a binary alphabet.

Since we always want to construct codes for sequences rather than single symbols, we only allow codes C such that the extension C(n) defines a code for all n. We say that such codes have ‘uniquely decodable extensions’. It is easy to see that (a) every prefix code has uniquely decodable extensions. Conversely, although this is not at all easy to see, it turns out that (b), for every code C with uniquely decodable extensions, there exists a prefix code C0 such that for all n, xn ∈X n, LC(n)(xn) = LC(n)

0 (xn) \[Cover

and Thomas 1991\]. Since in MDL we are only interested in code-lengths, and never in actual codes, we can restrict ourselves to prefix codes without loss of generality.

Thus, the restriction to prefix code may also be understood as a means to send concatenated messages while avoiding the need to introduce extra symbols into the alphabet.

Whenever in the sequel we speak of ‘code’, we really mean ‘prefix code’. We call a prefix code C for a set X complete if there exists no other prefix code that compresses at least one x more and no x less then C, i.e. if there exists no code C′ such that for all x, LC′(x) ≤LC(x) with strict inequality for at least one x.

2.2.2 The Kraft Inequality - Codelengths and Probabilities, Part I

In this subsection we relate prefix codes to probability distributions. Essential for understanding the relation is the fact that no matter what code we use, most sequences cannot be compressed, as demonstrated by the following example:

Example 2.2 \[Compression and Small Subsets: Example 1.2, Continued.\] In Example 1.2 we featured the following three sequences:

00010001000100010001 . . . 0001000100010001000100010001 (2.1)

01110100110100100110 . . . 1010111010111011000101100010 (2.2)

00011000001010100000 . . . 0010001000010000001000110000 (2.3)

We showed that (a) the first sequence - an n-fold repetition of 0001 - could be substantially compressed if we use as our code a general-purpose programming language (assuming that valid programs must end with a halt-statement or a closing bracket, such codes satisfy the prefix property). We also claimed that (b) the second sequence, n independent outcomes of fair coin tosses, cannot be compressed, and that (c) the third sequence could be compressed to αn bits, with 0 < α < 1. We are now in a position to prove statement (b): strings which are ‘intuitively’ random cannot be substantially

26

compressed. Let us take some arbitrary but fixed description method over the data alphabet consisting of the set of all binary sequences of length n. Such a code maps binary strings to binary strings. There are 2n possible data sequences of length n. Only two of these can be mapped to a description of length 1 (since there are only two binary strings of length 1: ‘0’ and ‘1’). Similarly, only a subset of at most 2m sequences can have a description of length m. This means that at most Pm

i=1 2m < 2m+1 data sequences can have a description length ≤m. The fraction of data sequences of length n that can be compressed by more than k bits is therefore at most 2−k and as such decreases exponentially in k. If data are generated by n tosses of a fair coin, then all 2n

possibilities for the data are equally probable, so the probability that we can compress the data by more than k bits is smaller than 2−k. For example, the probability that we can compress the data by more than 20 bits is smaller than one in a million.

We note that after the data (2.2) has been observed, it is always possible to design a code which uses arbitrarily few bits to encode this data - the actually observed sequence may be encoded as ‘1’ for example, and no other sequence is assigned a codeword. The point is that with a code that has been designed before seeing any data, it is virtually impossible to substantially compress randomly generated data.

The example demonstrates that achieving a short description length for the data is equivalent to identifying the data as belonging to a tiny, very special subset out of all a priori possible data sequences.

A Most Important Observation Let Z be finite or countable. For concreteness, we may take Z = {0, 1}n for some large n, say n = 10000. From Example 2.2 we know that, no matter what code we use to encode values in Z, ‘most’ outcomes in Z will not be substantially compressible: at most two outcomes can have description length 1 = −log 1/2; at most four outcomes can have length 2 = −log 1/4, and so on. Now consider any probability distribution on Z. Since the probabilities P(z) must sum up to one (P

z P(z) = 1), ‘most’ outcomes in Z must have small probability in the following sense: at most 2 outcomes can have probability ≥1/2; at most 4 outcomes can have probability ≥1/4; at most 8 can have ≥1/8-th etc. This suggests an analogy between codes and probability distributions: each code induces a code length function that assigns a number to each z, where most z’s are assigned large numbers. Similarly, each distribution assigns a number to each z, where most z’s are assigned small numbers.

It turns out that this correspondence can be made mathematically precise by means of the Kraft inequality \[Cover and Thomas 1991\]. We neither precisely state nor prove this inequality; rather, in Figure 2.1 we state an immediate and fundamental consequence: probability mass functions correspond to codelength functions. The following example illustrates this and at the same time introduces a type of code that will be frequently employed in the sequel:

Example 2.3 \[Uniform Distribution Corresponds to Fixed-length Code\] Suppose Z has M elements. The uniform distribution PU assigns probabilities 1/M to each

27

Probability Mass Functions correspond to Codelength Functions Let Z be a finite or countable set and let P be a probability distribution on Z. Then there exists a prefix code C for Z such that for all z ∈Z, LC(z) = ⌈−log P(z)⌉. C is called the code corresponding to P. Similarly, let C′ be a prefix code for Z. Then there exists a (possibly defective) probability distribution P ′ such that for all z ∈Z, −log P ′(z) = LC′(z). P ′ is called the probability distribution corresponding to C′.

Moreover C′ is a complete prefix code iﬀP is proper (P

z P(z) = 1).

Thus, large probability according to P means small code length according to the code corresponding to P and vice versa. We are typically concerned with cases where Z represents sequences of n outcomes; that is, Z = X n (n ≥1) where X is the sample space for one observation.

Figure 2.1: The most important observation of this tutorial.

element. We can arrive at a code corresponding to PU as follows. First, order and number the elements in Z as 0, 1, . . . , M −1. Then, for each z with number j, set C(z) to be equal to j represented as a binary number with ⌈log M⌉bits. The resulting code has, for all z ∈Z, LC(z) = ⌈log M⌉= ⌈−log PU(z)⌉. This is a code corresponding to PU (Figure 2.1). In general, there exist several codes corresponding to PU, one for each ordering of Z. But all these codes share the same length function LU(z) := ⌈−log PU(z)⌉.; therefore, LU(z) is the unique codelength function corresponding to PU.

For example, if M = 4, Z = {a, b, c, d}, we can take C(a) = 00, C(b) = 01, C(c) = 10, C(d) = 11 and then LU(z) = 2 for all z ∈Z. In general, codes corresponding to uniform distributions assign fixed lengths to each z and are called fixed-length codes. To map a non-uniform distribution to a corresponding code, we have to use a more intricate construction \[Cover and Thomas 1991\].

In practical applications, we almost always deal with probability distributions P and strings xn such that P(xn) decreases exponentially in n; for example, this will typically be the case if data are i.i.d., such that P(xn) = Q P(xi). Then −log P(xn) increases linearly in n and the eﬀect of rounding oﬀ−log P(xn) becomes negligible. Note that the code corresponding to the product distribution of P on X n does not have to be the n-fold extension of the code for the original distribution P on X – if we were to require that, the eﬀect of rounding oﬀwould be on the order of n . Instead, we directly design a code for the distribution on the larger space Z = X n. In this way, the eﬀect of rounding changes the codelength by at most 1 bit, which is truly negligible. For this and other4

reasons, we henceforth simply neglect the integer requirement for codelengths. This simplification allows us to identify codelength functions and (defective) probability

28

New Definition of Code Length Function

In MDL we are NEVER concerned with actual encodings; we are only concerned with code length functions. The set of all codelength functions for finite or countable sample space Z is defined as:

2−L(z) ≤1

X

LZ =

L : Z →\[0, ∞\] |

, (2.4)

z∈X

or equivalently, LZ is the set of those functions L on Z such that there exists a function Q with P

z Q(z) ≤1 and for all z, L(z) = −log Q(z). (Q(z) = 0 corresponds to L(z) = ∞). Again, Z usually represents a sample of n outcomes: Z = X n (n ≥1) where X is the sample space for one observation.

Figure 2.2: Code lengths are probabilities.

mass functions, such that a short codelength corresponds to a high probability and vice versa. Furthermore, as we will see, in MDL we are not interested in the details of actual encodings C(z); we only care about the code lengths LC(z). It is so useful to think about these as log-probabilities, and so convenient to allow for non-integer nonprobabilities, that we will simply redefine prefix code length functions as (defective) probability mass functions that can have non-integer code lengths – see Figure 2.2. The following example illustrates idealized codelength functions and at the same time introduces a type of code that will be frequently used in the sequel:

Example 2.4 ‘Almost’ Uniform Code for the Positive Integers Suppose we want to encode a number k ∈{1, 2, . . . }. In Example 2.3, we saw that in order to encode a number between 1 and M, we need log M bits. What if we cannot determine the maximum M in advance? We cannot just encode k using the uniform code for {1, . . . , k}, since the resulting code would not be prefix. So in general, we will need more than log k bits. Yet there exists a prefix-free code which performs ‘almost’ as well as log k. The simplest of such codes works as follows. k is described by a codeword starting with ⌈log k⌉0s. This is followed by a 1, and then k is encoded using the uniform code for {1, . . . , 2⌈log k⌉}. With this protocol, a decoder can first reconstruct ⌈log k⌉by counting all 0’s before the leftmost 1 in the encoding. He then has an upper bound on k and can use this knowledge to decode k itself. This protocol uses less than 2⌈log k⌉+ 1 bits. Working with idealized, non-integer code-lengths we can simplify this to 2 log k + 1 bits. To see this, consider the function P(x) = 2−2 log x−1. An easy

29

calculation gives

2−2 log x−1 = 1

x−2 < 1

2 + 1

1

X

X

X

X

P(x) =

x(x −1) = 1,

2

2

x∈1,2,...

x∈1,2,...

x∈1,2,...

x=2,3,...

so that P is a (defective) probability distribution. Thus, by our new definition (Figure 2.2), there exists a prefix code with, for all k, L(k) = −log P(k) = 2 log k + 1. We call the resulting code the ‘simple standard code for the integers’. In Section 2.5 we will see that it is an instance of a so-called ‘universal’ code.

The idea can be refined to lead to codes with lengths log k + O(log log k); the ‘best’ possible refinement, with code lengths L(k) increasing monotonically but as slowly as possible in k, is known as ‘the universal code for the integers’ \[Rissanen 1983\]. However, for our purposes in this tutorial, it is good enough to encode integers k with 2 log k + 1 bits.

Example 2.5 \[Example 1.2 and 2.2, Continued.\] We are now also in a position to prove the third and final claim of Examples 1.2 and 2.2. Consider the three sequences (2.1), (2.2) and (2.3) on page 26 again. It remains to investigate how much the third sequence can be compressed. Assume for concreteness that, before seeing the sequence, we are told that the sequence contains a fraction of 1s equal to 1/5 + ǫ for some small unknown ǫ. By the Kraft inequality, Figure 2.1, for all distributions P, there exists some code on sequences of length n such that for all xn ∈X n, L(xn) = ⌈−log P(xn)⌉. The fact that the fraction of 1s is approximately equal to 1/5 suggests to model xn as independent outcomes of a coin with bias 1/5-th. The corresponding distribution P0 satisfies

n\[1\]4

n\[0\]

1

1

log 1

5 − 4

log 4

−log P0(xn) = log

5 + ǫ 

5 −ǫ 

5 

= n

−

=

5

5

n\[log 5 −8

5 + 2ǫ\],

where n\[j\] denotes the number of occurrences of symbol j in xn. For small enough ǫ, the part between brackets is smaller than 1, so that, using the code L0 with lengths −log P0, the sequence can be encoded using αn bits were α satisfies 0 < α < 1. Thus, using the code L0, the sequence can be compressed by a linear amount, if we use a specially designed code that assigns short codelengths to sequences with about four times as many 0s than 1s.

We note that after the data (2.3) has been observed, it is always possible to design a code which uses arbitrarily few bits to encode xn - the actually observed sequence may be encoded as ‘1’ for example, and no other sequence is assigned a codeword. The point is that with a code that has been designed before seeing the actual sequence, given only the knowledge that the sequence will contain approximately four times as many 0s than 1s, the sequence is guaranteed to be compressed by an amount linear in n.

Continuous Sample Spaces How does the correspondence work for continuousvalued X? In this tutorial we only consider P on X such that P admits a density5.

30

The P that corresponds to L minimizes expected codelength Let P be a distribution on (finite, countable or continuous-valued) Z and let L be defined by

L:= arg min

EP \[L(Z)\]. (2.5)

L∈LZ

Then L exists, is unique, and is identical to the codelength function corresponding to P, with lengths L(z) = −log P(z).

Figure 2.3: The second most important observation of this tutorial.

Whenever in the following we make a general statement about sample spaces X and distributions P, X may be finite, countable or any subset of Rl, for any integer l ≥1, and P(x) represents the probability mass function or density of P, as the case may be. In the continuous case, all sums should be read as integrals. The correspondence between probability distributions and codes may be extended to distributions on continuous-valued X: we may think of L(xn) := −log P(xn) as a code-length function corresponding to Z = X n encoding the values in X n at unit precision; here P(xn) is the density of xn according to P. We refer to \[Cover and Thomas 1991\] for further details.

2.2.3 The Information Inequality - Codelengths & Probabilities, II

In the previous subsection, we established the first fundamental relation between probability distributions and codelength functions. We now discuss the second relation, which is nearly as important.

In the correspondence to codelength functions, probability distributions were treated as mathematical objects and nothing else. That is, if we decide to use a code C to encode our data, this definitely does not necessarily mean that we assume our data to be drawn according to the probability distribution corresponding to L: we may have no idea what distribution generates our data; or conceivably, such a distribution may not even exist6. Nevertheless, if the data are distributed according to some distribution P, then the code corresponding to P turns out to be the optimal code to use, in an expected sense – see Figure 2.3. This result may be recast as follows: for all distributions P and Q with Q̸ = P,

EP \[−log Q(X)\] > EP \[−log P(X)\].

In this form, the result is known as the information inequality. It is easily proved using concavity of the logarithm \[Cover and Thomas 1991\].

31

The information inequality says the following: suppose Z is distributed according to P (‘generated by P’). Then, among all possible codes for Z, the code with lengths −log P(Z) ‘on average’ gives the shortest encodings of outcomes of P. Why should we be interested in the average? The law of large numbers \[Feller 1968\] implies that, for large samples of data distributed according to P, with high P-probability, the code that gives the shortest expected lengths will also give the shortest actual codelengths, which is what we are really interested in. This will hold if data are i.i.d., but also more generally if P defines a ‘stationary and ergodic’ process.

Example 2.6 Let us briefly illustrate this. Let P ∗, QA and QB be three probability distributions on X, extended to Z = X n by independence. Hence P ∗(xn) = Q P ∗(xi) and similarly for QA and QB. Suppose we obtain a sample generated by P ∗. Mr. A and Mrs. B both want to encode the sample using as few bits as possible, but neither knows that P ∗has actually been used to generate the sample. A decides to use the code corresponding to distribution QA and B decides to use the code corresponding to QB. Suppose that EP ∗\[−log QA(X)\] < EP ∗\[−log QB(X)\]. Then, by the law of large numbers , with P ∗-probability 1, n−1\[−log Qj(X1, . . . , Xn)\] → EP ∗\[−log Qj(X)\], for both j ∈{A, B} (note −log Qj(Xn) = −Pn

i=1 log Qj(Xi)). It follows that, with probability 1, Mr. A will need less (linearly in n) bits to encode X1, . . . , Xn than Mrs. B.

The qualitative content of this result is not so surprising: in a large sample generated by P, the frequency of each x ∈X will be approximately equal to the probability P(x). In order to obtain a short codelength for xn, we should use a code that assigns a small codelength to those symbols in X with high frequency (probability), and a large codelength to those symbols in X with low frequency (probability).

Summary and Outlook In this section we introduced (prefix) codes and thoroughly discussed the relation between probabilities and codelengths. We are now almost ready to formalize a simple version of MDL – but first we need to review some concepts of statistics.

---

Full document: [24 - A Tutorial Introduction to the Minimum Description Length Principle](../../papers/24-tutorial-minimum-description-length.md) · Page-level evidence: [paper-pages/24-tutorial-minimum-description-length](../../paper-pages/24-tutorial-minimum-description-length/index.md)
