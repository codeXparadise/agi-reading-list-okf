---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/13-order-matters-sequence-to-sequence-for-sets.md
source: ../../papers/13-order-matters-sequence-to-sequence-for-sets.md
paper_title: "Order Matters: Sequence to Sequence for Sets"
sequence: 13
page: 7
pages: [7]
page_of: 11
topics: ["../../topics/sequence-to-sequence.md", "../../topics/attention.md"]
description: "the head variable. We expect that it should be easier to model the joint distribution by choosing any ordering which starts with the head variable.…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 7 of 11 - Order Matters: Sequence to Sequence for Sets

> Page 7 of the source PDF, verbatim as extracted. Canonical document: [13 - Order Matters: Sequence to Sequence for Sets](../../papers/13-order-matters-sequence-to-sequence-for-sets.md)

the head variable. We expect that it should be easier to model the joint distribution by choosing any ordering which starts with the head variable. We created several artificial datasets by varying the number of random variables to model (between 10 and 50, each of which was a multinomial over 10 symbols), the training set size (between 200 and 20000 training samples), and the randomness of the marginal distributions, or how deterministic, or peaky, they were. For each problem, we trained two LSTMs for 10,000 mini-batch iterations to model the joint probability, one where the head random variable was shown first, and one where it was shown last.

The results were as follows:

• when the training set size is large enough (20000), the LSTM is able to learn the joint probability in whichever order;

• when the marginal distributions are very peaky (and thus almost deterministic), the LSTM is also able to learn the joint probability independently of the order;

• in all other cases (small training set size, small or large number of random variables, and some amount of randomness in the marginal distributions), it was always easier to learn an LSTM with the optimal order of random variables than any other order.

5.2 FINDING OPTIMAL ORDERINGS WHILE TRAINING

Recall the model we proposed for dealing with input sets: given an embedding for each of the inputs, we have a generic module that is able to process its inputs in any order. This yields an embedding satisfying the key property of being invariant to reorderings, whilst being generic in the kinds of computations to do over the input set.

Unfortunately, placing a joint probability over a set of random variables y1, . . . yn when the structure of the joint probability function is unknown is a hard problem. Fortunately, and thanks to recurrent neural networks, we can apply the chain rule which decomposes this joint probability sequentially (see eq. 8) without independence assumptions. In this work, we focus on using the chain rule, discarding more naive decompositions that have strong and unrealistic assumptions (e.g., conditional independence).

An obvious drawback of the chain rule which violates the argument of treating y1, . . . yn as a set is that we condition these random variables in a particular order. Even though, in principle, the order should not matter, in the previous section we have shown that this is indeed not the case, and that certain orderings are better than others in a variety of tasks – most likely due to the parameterization of the joint probability (using an LSTM), and the non-convex nature of the optimization problem.

Our proposed solution to deal with the aforementioned drawback is extremely simple: as we train, we let the model decide which is the best ordering in which it will apply the chain rule. More formally, assume there exists an ordering which maximally simplifies the task, π(X) (where X is the input sequence or set, which can be empty). We would like to train the model as p(Yπ(X)|X). The number of possible orderings is large – n! where n is the length of the output, and the best order is unknown a priori.

Since n! can be very large, we could attempt to do (inexact) search as we train the model. Instead of maximizing the log probability of p(Y |X) for each training example pair, we also maximize over orderings as follows:

X

θ⋆= arg max

max π(Xi) log p(Yπ(Xi)|Xi; θ) (9)

θ

i

where maxπ(Xi) is computed either naively, or with an inexact search. Note that Equation (9) may not strictly improve the regular maximum likelihood framework due to non-convexity, but we found this to not be an issue in practice.

Besides not being scalable, we found that, if done naively and picking the max over ordering as we train, the model would pick a random ordering (as a function of the initial parameters), and would get stuck on it permanently (since it would reinforce it through learning). We added two ways to explore the space of all orderings as follows:

---

[previous page](page-006.md) · [next page](page-008.md) · [all pages](index.md)
